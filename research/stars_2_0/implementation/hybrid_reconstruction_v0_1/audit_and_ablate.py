#!/usr/bin/env python3
"""Independent deterministic audit; outputs are NEW derived toys, never historical runs."""
from pathlib import Path
import argparse, ast, csv, hashlib, itertools, json, math
import numpy as np
ROOT=Path(__file__).resolve().parent
Q=8.68*1.602176634e-13

def loss(R,E,V,orbit=1., convention='archived'):
    if R<1 or E<=0 or V<0 or orbit<0:raise ValueError('Invalid mirror scenario')
    t=1-1/R+V/(E if convention=='archived' else R*E)
    return min(1.,max(0.,orbit*(1-math.sqrt(min(1.,max(0.,t))))))

def ledger(admitted,p,escape,passes):
    if admitted<0 or not 0<=p<=1 or not 0<=escape<=1 or not isinstance(passes,int) or passes<0:raise ValueError('Invalid particle inputs')
    alive=admitted;events=escaped=0.
    for _ in range(passes):
        fused=alive*p;after=alive-fused
        events+=fused;escaped+=after*escape;alive=after*(1-escape)
    return dict(fusion_events=events,protons_lost=escaped,protons_remaining=alive,particle_residual=admitted-events-escaped-alive,nuclear_Q_J=events*Q)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    d=Path(args.out);d.mkdir(parents=True,exist_ok=False)
    checks={}
    def check(k,v):
        checks[k]=bool(v)
        if not v:raise AssertionError(k)
    # Execute only byte-sourced function definitions, with their original NumPy namespace.
    # No historical script top-level side effects or modifications.
    pth=ROOT/'sources/mirror/stars_prism_three_module_toy_2026-10-29.py'
    tree=ast.parse(pth.read_text());defs=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
    ns={'np':np};exec(compile(defs,str(pth),'exec'),ns)
    refs=list(csv.DictReader((ROOT/'sources/mirror/stars_prism_three_module_toy_2026-10-29.csv').open()))
    comparisons=[]
    for row in refs:
        args0=(row['scenario'],float(row['mirror_ratio']),float(row['proton_barrier_keV']),float(row['alpha_barrier_keV']),float(row['capture_assumed']),float(row['orbit_loss_multiplier']))
        n=1 if row['scenario']=='single_pass_no_mirror' else 10
        old=ns['case'](*args0,attempts=n)
        l=loss(args0[1],200,args0[2],args0[5]);x=ledger(5e8*args0[4],1e-5,l,n)
        check(row['scenario']+': original rounded count',old['fusion_events_per_pulse']==float(row['fusion_events_per_pulse']))
        check(row['scenario']+': independent recurrence',math.isclose(round(x['fusion_events'],3),old['fusion_events_per_pulse'],abs_tol=1e-9))
        check(row['scenario']+': particle closure',abs(x['particle_residual'])<1e-6)
        corrected=ledger(5e8*args0[4],1e-5,loss(args0[1],200,args0[2],args0[5],'throat_potential'),n)
        comparisons.append(dict(scenario=row['scenario'],original_events_unrounded=x['fusion_events'],original_events_rounded=old['fusion_events_per_pulse'],conditional_throat_potential_events=corrected['fusion_events'],conditional_difference=corrected['fusion_events']-x['fusion_events'],admitted_200keV_kinetic_J=5e8*args0[4]*200e3*1.602176634e-19,**{k:v for k,v in x.items() if k!='fusion_events'}))
    # Algebraically independent finite-geometric-series comparator and extreme conservation cases.
    for p,escape,n in itertools.product([0.,1e-5,.2,1.],[0.,.04,1.],[0,1,10,100]):
        x=ledger(1e6,p,escape,n);s=(1-p)*(1-escape)
        closed=1e6*p*(n if s==1 else (1-s**n)/(1-s))
        check(f'geometric/conservation p={p} l={escape} n={n}',math.isclose(x['fusion_events'],closed,rel_tol=1e-10,abs_tol=1e-8) and abs(x['particle_residual'])<1e-8 and x['fusion_events']<=1e6)
    check('zero sigma gives zero nuclear Q',ledger(1e6,0,.1,10)['nuclear_Q_J']==0)
    check('one-use protons at unit fusion probability',ledger(100,1,.5,10)['fusion_events']==100)
    check('zero capture gives zero events',ledger(0,.1,.2,10)['fusion_events']==0)
    # Check the inferred loss cone against midplane energy conservation at the critical pitch.
    t=1-1/5+30/(5*200)
    check('throat threshold closes kinetic + potential energy',abs(200-5*200*(1-t)-30)<1e-12)
    check('archived threshold would encode 150 keV throat barrier at R5',abs((1-1/5+30/200-(1-1/5))*5*200-150)<1e-10)
    factorial=[]
    for convention,R,V,orbit,capture in itertools.product(['archived','throat_potential'],[1.,5.],[0.,30.],[1.,1.5],[.3,.6]):
        l=loss(R,200,V,orbit,convention);x=ledger(5e8*capture,1e-5,l,10)
        factorial.append(dict(evidence='NEW_POTENTIAL_DERIVED_TOY',loss_convention=convention,mirror_ratio=R,proton_barrier_keV=V,orbit_loss_multiplier=orbit,capture=capture,proton_escape_per_pass=l,gain_over_same_capture_one_pass=x['fusion_events']/(5e8*capture*1e-5),gain_over_full_capture_one_pass=x['fusion_events']/5000,**x))
    acoustic=[]
    for r in csv.DictReader((ROOT/'sources/acoustic_v10/scenario_sweep.csv').open()):
        if r['phase_deg'] in ('0','180') and r['memory_chi'] in ('0.0','1.0'):
            acoustic.append({**r,'nuclear_coupling_status':'NOT_IMPLEMENTED_IN_RECOVERED_SCRIPT','wall_energy_status':'NOT_BUDGETED'})
    for name,rows in [('BASELINE_AUDIT.csv',comparisons),('MIRROR_FACTORIAL_ABLATIONS.csv',factorial),('ACOUSTIC_PROXY_ABLATIONS.csv',acoustic)]:
        with (d/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    interaction=[]
    for convention in ['archived','throat_potential']:
        def value(R,V):return ledger(1.5e8,1e-5,loss(R,200,V,1.,convention),10)['fusion_events']
        interaction.append({'convention':convention,'contrast':'mirror x barrier; Y(5,30)-Y(5,0)-Y(1,30)+Y(1,0)','interaction_events':value(5,30)-value(5,0)-value(1,30)+value(1,0),'interpretation':'Nonadditivity inside this toy only; not measured synergy'})
    receipt={'status':'NEW_DERIVED_AUDIT_NOT_ORIGINAL_HYBRID','checks_passed':sum(checks.values()),'checks':checks,'factorial_rows':len(factorial),'interactions':interaction,'conditional_loss_formula_source':'Kolmes, Ochs & Fisch (2024), DOI 10.1017/S0022377824000205, Eqs 2.3–2.4; inferred threshold for monotone adiabatic throat barrier. Not a rotating-mirror calibration.','unmodeled_outputs':['full hybrid fusion yield','shot success / readiness to nuclear coupling','stopping and catcher stages','measured source-to-mirror capture','alpha collector recovered electricity','wall-plug net power']}
    (d/'AUDIT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','checks_passed','factorial_rows','interactions')},indent=2))
if __name__=='__main__':main()
