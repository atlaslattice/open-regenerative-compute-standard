#!/usr/bin/env python3
"""Reproduce benchmarks, schedules, sweeps and report from versioned inputs.

Python standard library only. Run from any directory. Existing outputs replaced;
audit history is never rewritten by this script. Default ensemble N=64 is a
scenario distribution, NOT a calibrated physical posterior or confidence bound.
"""
import argparse
import csv
import hashlib
import json
import platform
import random
import statistics
import subprocess
import sys
from pathlib import Path
from fuelcycle.model import simulate
from fuelcycle.schedules import generate
from fuelcycle.physics import dd_source, dt_events, T_KG_PER_ATOM, FPY_S, argon_burn_fraction, argon_extraction, MEV_J

ROOT=Path(__file__).resolve().parent

def write_csv(path, rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def schedule(p):
    return generate(p['days'],p['seed'],p['availability_a'],p['availability_b'],
                    p['common_outage'],planned_a=range(180,195),planned_b=range(365,395))

def quantile(values,q):
    a=sorted(values);x=q*(len(a)-1);i=int(x)
    return a[i]+(a[min(i+1,len(a)-1)]-a[i])*(x-i)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=ROOT/'inputs/reference_v1_1.json')
    ap.add_argument('--output',type=Path,default=ROOT/'outputs');ap.add_argument('--samples',type=int,default=64)
    args=ap.parse_args()
    if args.samples<2:ap.error('--samples must be >=2')
    p=json.loads(args.input.read_text());out=args.output;out.mkdir(parents=True,exist_ok=True)
    # Check published benchmark CSV before using any dynamic physics.
    checks=[]
    with (ROOT/'baseline_v1/SCENARIOS.csv').open() as f:
        for r in csv.DictReader(f):
            actual=float(r['a_preprocessing_kg_fpy'])+float(r['eta_b'])*float(r['tbr_b'])*float(r['burn_kg_fpy'])-float(r['burn_kg_fpy'])
            error=actual-float(r['net_kg_fpy'])
            if abs(error)>.000051:raise ArithmeticError('v1 benchmark failure')
            checks.append(dict(tbr_b=r['tbr_b'],eta_b=r['eta_b'],published_kg=r['net_kg_fpy'],reproduced_kg=actual,error_kg=error,evidence='VERIFIED-DERIVED arithmetic only'))
    write_csv(out/'v1_benchmark_checks.csv',checks)
    argon=[]
    for eps,minutes,loss,grams,net in [(.85,10,.005,1.44,4.590),(.5,10,.01,2.45,4.268),(.25,15,.025,7.34,3.303),(.1,30,.058,36.7,1.179)]:
        z=argon_extraction(eps,minutes,0,12.32,loss,64.362/365.25)
        computed=3.65+z['eta_salt_and_one_iss']*64.362-63.1
        argon.append(dict(epsilon=eps,loop_minutes=minutes,assumed_k_perm_day=0,
            assumed_iss_loss=loss,holdup_g=z['inventory_ss_kg']*1000,
            supplied_holdup_g=grams,eta=z['eta_salt_and_one_iss'],
            static_balance_kg_fpy=computed,supplied_balance_kg_fpy=net,
            qualification='POTENTIAL-DERIVED; not usable surplus'))
    write_csv(out/'argon_table_audit.csv',argon)
    dd=dd_source();maximum=dd['t_atoms_s']*17.6*MEV_J/1e6
    (out/'argon_g1_audit.json').write_text(json.dumps(dict(
        convention='17.6 MeV D-T matches v1 and dynamic energy ledger; Argon used 17.59',
        maximum_secondary_mw=maximum,implied_18mw_fraction=18/maximum,
        implied_18mw_consumption_kg_fpy=dt_events(18)*FPY_S*T_KG_PER_ATOM,
        assumed_candidate_fraction=argon_burn_fraction(p.get('a_fast_fraction',0),p['a_density_m3'],p['a_reactivity_m3_s'],p['a_residence_s']),
        classification='VERIFIED-DERIVED arithmetic; candidate inputs POTENTIAL-DERIVED; G1 OPEN'),indent=2)+'\n')
    for e in ('.85','1'):
        text=subprocess.check_output([sys.executable,str(ROOT/'baseline_v1/tritium_ledger.py'),'--efficiency',e],text=True)
        (out/f'v1_original_eta_{e}.csv').write_text(text)
    sched=schedule(p)
    write_csv(out/'schedule.csv',[dict(day=i+1,on_a=a,on_b=b) for i,(a,b) in enumerate(sched)])
    case_summaries=[];trajectories={}
    # No optimized A2 yield exists in v1. Explicit 0.70 is an exploratory surrogate.
    for case,tbr in [('A0',0.),('A1',p['tbr_a']),('A2',.70)]:
        cfg=dict(p,case=case,tbr_a=tbr)
        rows,s=simulate(cfg,sched);s['assumed_tbr_a']=tbr
        case_summaries.append(s);write_csv(out/f'{case}_daily.csv',rows)
        trajectories[case]=[dict(day=0,total_inventory=s['initial_kg'],b_store=p['initial_b_kg'],b_unserved_burn=0)]+[
            {k:round(r[k],8) for k in ('day','total_inventory','b_store','b_unserved_burn')} for r in rows]
        (out/f'{case}_input.json').write_text(json.dumps(cfg,indent=2)+'\n')
    (out/'case_summaries.json').write_text(json.dumps(case_summaries,indent=2)+'\n')
    write_csv(out/'case_ledgers.csv',case_summaries)
    # Local one-at-a-time sensitivity; same schedule separates physics parameter from outages.
    sensitivity=[]
    for key,values in [('tbr_b',[.95,1.02,1.10]),('extract_b_day',[4.8,36.,122.4]),
        ('process_recovery',[.99,.999,.9999]),('a_reaction_day',[0,864,2000]),
        ('initial_b_kg',[0,1,10]),('b_pass_burn_fraction',[.01,.05,.2])]:
        for value in values:
            _,s=simulate(dict(p,**{key:value}),sched)
            sensitivity.append(dict(parameter=key,value=value,final_kg=s['final_kg'],
               unserved_burn_kg=s['b_unserved_burn_kg'],evidence='POTENTIAL-DERIVED'))
    write_csv(out/'sensitivity.csv',sensitivity)
    # Versioned uncertainty specification: independent uniform epistemic ranges,
    # except common shock mechanism couples outages. No covariance dataset exists.
    uncertainty=json.loads((ROOT/'inputs/uncertainty_v1_1.json').read_text())
    rng=random.Random(uncertainty['seed']);samples=[]
    for i in range(args.samples):
        cfg=dict(p,seed=1000+i)
        for key,(lo,hi) in uncertainty['uniform_ranges'].items():cfg[key]=rng.uniform(lo,hi)
        _,s=simulate(cfg,schedule(cfg))
        samples.append(dict(sample=i,**{k:cfg[k] for k in uncertainty['uniform_ranges']},
                            schedule_seed=cfg['seed'],final_kg=s['final_kg'],
                            unserved_burn_kg=s['b_unserved_burn_kg'],evidence='POTENTIAL-DERIVED'))
    write_csv(out/'ensemble.csv',samples)
    bounds={key:{str(q):quantile([r[key] for r in samples],q) for q in (0,.05,.5,.95,1)}
            for key in ('final_kg','unserved_burn_kg')}
    (out/'scenario_bounds.json').write_text(json.dumps(dict(label='Assumption-conditioned ensemble quantiles; not confidence/credible bounds',samples=args.samples,metrics=bounds),indent=2)+'\n')
    # Time refinement on identical schedule: exact compartments != exact coupled model.
    refine=[]
    for step in (.5,.25,.125,.0625):
        _,s=simulate(dict(p,step_days=step),sched)
        refine.append(dict(step_days=step,final_kg=s['final_kg'],unserved_burn_kg=s['b_unserved_burn_kg']))
    for r in refine:r['final_difference_from_finest_kg']=r['final_kg']-refine[-1]['final_kg']
    write_csv(out/'timestep_refinement.csv',refine)
    # Reproducibility manifest includes source and input SHA256; runtime outputs have
    # no wall-clock timestamp, so identical environment+inputs generate identical files.
    manifest=dict(python=platform.python_version(),platform=platform.platform(),samples=args.samples,
                  baseline_commit='876bb375d278e9ccb934638fbfbe64852fbcbfbd',files={})
    for f in sorted(ROOT.rglob('*')):
        if f.is_file() and f.suffix in ('.py','.json','.csv','.md','.jsonl','.html','.cjs') and not any(a in f.parts for a in ('outputs','__pycache__')):
            manifest['files'][str(f.relative_to(ROOT))]=hashlib.sha256(f.read_bytes()).hexdigest()
    manifest['invoked_input_sha256']=hashlib.sha256(args.input.read_bytes()).hexdigest()
    (out/'run_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    template=(ROOT/'dashboard_template.html').read_text()
    (out/'dashboard.html').write_text(template.replace('__TRAJECTORIES__',json.dumps(trajectories,separators=(',',':'))))
    write_report(p,case_summaries,bounds,refine,args.samples,out)
    print(json.dumps(dict(output=str(out),benchmarks=len(checks),samples=args.samples,cases=case_summaries),indent=2))

def write_report(p,summaries,bounds,refine,n,out):
    source=dd_source();dd_kg=source['t_atoms_s']*FPY_S*T_KG_PER_ATOM
    b_kg=dt_events(1130)*FPY_S*T_KG_PER_ATOM
    text=f'''# Beyond Q v1.1 — Dynamic Fuel-Cycle Computational Results

Atlas Lattice / STARS 2.0 / Stellar Forge extension. Candidate research release.
Reference baseline commit: `876bb375d278e9ccb934638fbfbe64852fbcbfbd`.

**No physical self-sufficiency or qualified usable surplus is established.**
Gemini Argon's exact candidate equations were supplied during implementation.
They are implemented and audited; their physical inputs remain unvalidated.

## Reproduction and configuration

All 28 v1 CSV scenarios reproduce within 0.000051 kg rounding tolerance.
Original script also runs at eventual recovery 1.0 and 0.85. Exact legacy
display benchmarks remain +4.912 and -4.7423 kg/FPY; A=3.65 kg is explicitly
an unqualified annual assumption. v1 remains unchanged.

B is locked at 1130 MW D-T fusion. A is locked at hypothetical 20 MW primary
D-D. Rounded reaction energies and the stated atomic mass give A direct
birth {dd_kg:.6f} kg/FPY and B burn {b_kg:.6f} kg/FPY. These use a common
stoichiometric constant; the legacy 55.8 kg/GW FPY and 63.1 display basis
are retained only in the benchmark module. These differences expose rounding/
conversion drift in inherited numbers, not a new physical effect. Argon quoted
2.712 kg/FPY primary birth and 1.013 kg/FPY secondary consumption; this common
conversion yields 2.702640 and 1.008883 kg/FPY respectively. Classification: VERIFIED-DERIVED
conditional stoichiometry; reactor operating points remain assumed/design targets.

## Illustrative dynamic cases ({p['days']} calendar days)

| Case | Assumed A births/source neutron | Final inventory kg-T | Change kg-T | Unserved B burn kg-T |
|---|---:|---:|---:|---:|
'''
    for s in summaries:
        text+=f"| {s['case']} | {s['assumed_tbr_a']:.3f} | {s['final_kg']:.6f} | {s['inventory_change_kg']:.6f} | {s['b_unserved_burn_kg']:.6f} |\n"
    text+=f'''
Every dynamic case is POTENTIAL-DERIVED. A0 means nonbreeding functional
shield/coolant, not no shielding. A1 uses an illustrative yield of 0.52
T atoms per primary-plus-secondary source neutron. A2=0.70 is an explicitly
assumed exploratory surrogate, **not an optimized blanket calculation**.
v1 defines no numerical A2 blanket; natural-lithium chemistry does not determine
a TBR by itself. Initial B stock is {p['initial_b_kg']} kg externally acquired T,
not a prediction of required startup inventory. No subsequent imports are modeled.

Common outage probability is {p['common_outage']}; independent on-probabilities
are {p['availability_a']}/{p['availability_b']} before the common outage.
Planned A outage days 180–194 and B outage days 365–394 are zero-based.
Extraction/processing continue during reactor outages; no processor-failure
model is inferred. Minimum daily B storage is reported, but substep minima
and licensing reserves are not qualified. Unserved burn measures inability to
meet requested power: the simulator reduces B burn and blanket births together,
so fuel starvation cannot manufacture fuel at rated power.

## Uncertainty and numerical limits

{n} reproducible parameter/schedule draws use the explicit uniform ranges in
`inputs/uncertainty_v1_1.json`. They are assumption-conditioned scenario bounds,
not measured uncertainty, confidence bounds, or a calibrated Bayesian posterior.
The assumed ranges are independent; input covariance and model discrepancy
are missing. Common shocks correlate outages. The 5/50/95% final inventory
quantiles are {bounds['final_kg']['0.05']:.4f} / {bounds['final_kg']['0.5']:.4f} /
{bounds['final_kg']['0.95']:.4f} kg-T. Compare unserved burn alongside inventory:
a high remaining inventory alone does not prove successful operation.

All compartments integrate constant source/linear hazards analytically and
remain nonnegative. Coupled updates use first-order operator splitting; this
has timestep bias. Default step {p['step_days']} day differs from 0.0625-day
final stock by {summaries[1]['final_kg']-refine[-1]['final_kg']:.6g} kg in this run.
Refinement is a numerical check, not physical validation. Benchmark and tests
do not certify reactor feasibility.

## Independently checkable ledgers

Daily CSV columns record each compartment, source, sink, feed, recirculation,
transfer and cumulative residual. Identity in kg-T:
`initial + DD births + A blanket births + B blanket births = remaining +
A burn + B burn + decay + permeation + processing losses`.
Transfers cancel globally. One consumed T atom cannot reach a storage account.
Decay is tracked as kg-T-equivalent transformed into He-3, not unaccounted T.
This is a tritium isotope mass ledger, not total elemental/isotopic depletion.
Li/Be/F/D and structural depletion are not solved; blanket reactants are an
assumed inexhaustible reservoir within the short screening horizon.

The JSON summaries partition fusion energy into charged-particle and neutron
kinetic energy. Their sum equals fusion Q; neutron heat is never added again.
Blanket Q uses an assumed Li-6/Li-7 birth partition and is separately named.
This is source nuclear release, not deposited thermal heat or net electricity.
Neutron source births are countable, but capture/leakage/multiplication fate
closure is UNRESOLVED without transport. No assumed TBR can close that ledger.

## Gate status

| Gate | Computational progress | Evidence still required / status |
|---|---|---|
| G1 | Conservative DD birth and candidate secondary-burn hazards; 18 MW no longer independently forced | Density / T distribution / reactivity / confinement and power balance; OPEN |
| G2 | OpenMC preflight and surrogate input generator | Installed engine/data plus V3A-compatible documented geometry/materials/ports; OPEN |
| G3 | Extraction, holdup, permeation, recirculation and decay compartments | Measured FLiBe transport/speciation/recovery under relevant loads; OPEN |
| G4 | Time-resolved inventory, independent schedules, common outages, seed and conservation tests | Calibrated schedules, subcomponent failures, startup/reserve qualification; OPEN for physical closure |
| G5 | Nuclear source energy partition without duplicate neutron energy | Full heat deposition, wall-plug/RF/cooling/magnets/materials/economics; OPEN |

v1 G6 is preserved as cross-cutting independent replication/provenance.
No gate is declared physically validated. See `TECHNICAL_METHODS.md` for equations,
`SOURCES.md` for exact source relevance and access limits, and `AUDIT_HISTORY.jsonl`
for append-only corrections and Argon review.

## Credit and direction

Research conception/direction: Dave Sheldon / Atlas Lattice. GPT-6: documented
v1 audit/synthesis and v1.1 computational implementation through ChatGPT Work.
DeepSeek: v1 conditional blanket/recovery scenarios and critique. Gemini Argon:
v1 literature and material/enrichment challenges; candidate burn and extraction equations supplied by the user. Contributions are analytical discourse/software, not experiments,
institutional endorsements, or independent peer review.
'''
    (out/'TECHNICAL_REPORT.md').write_text(text)

if __name__=='__main__':main()
