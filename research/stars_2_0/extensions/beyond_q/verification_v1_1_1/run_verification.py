#!/usr/bin/env python3
"""Run external fixture benchmark, resilience envelope and error budget."""
from pathlib import Path
import csv,json,hashlib,platform
import numpy as np
import scipy
from benchmark import reproduce,exact_at,NAMES,system
from extraction import compare
from fuelcycle.model import simulate
from fuelcycle.physics import dt_events,T_KG_PER_ATOM

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'

def csvout(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def scenario(name,days):
    ops=[(1,1)]*days;components=[(1,1,1,1)]*days
    windows={'baseline':(0,0),'extractor_7d':(30,37),'processor_7d':(30,37),
             'processor_30d':(30,60),'A_off_60d':(30,90),'B_off_40d':(100,140),
             'common_off_30d':(30,60)}
    lo,hi=windows[name]
    for d in range(lo,min(hi,days)):
        if name.startswith('extractor'):components[d]=(1,0,1,1)
        elif name.startswith('processor'):components[d]=(1,1,1,0)
        elif name.startswith('A_off'):ops[d]=(0,1)
        elif name.startswith('B_off'):ops[d]=(1,0)
        else:ops[d]=(0,0)
    return ops,components

def run_case(p,name,stock,step=.125):
    cfg=dict(p,initial_b_kg=stock,step_days=step)
    return simulate(cfg,*scenario(name,cfg['days']))

def threshold(p,name,step=.125):
    lo=0.;hi=200.
    if run_case(p,name,hi,step)[1]['b_unserved_burn_kg']>1e-8:
        return dict(lower_kg=hi,upper_kg=None,status='NOT BRACKETED')
    for _ in range(20):
        mid=(lo+hi)/2
        if run_case(p,name,mid,step)[1]['b_unserved_burn_kg']>1e-8:lo=mid
        else:hi=mid
    return dict(lower_kg=lo,upper_kg=hi,status='CONDITIONAL: unmet burn <=1e-8 kg over 180 days')

def main():
    OUT.mkdir(exist_ok=True)
    gold,actual,metrics=reproduce();oracle=exact_at(gold['time'])
    assert metrics['max_abs_error_kg']<1e-8,'External fixture reproduction failed'
    metrics.update(reference_commit='7dfbc71378fb243afba23db80a8284cd4b6429a4',
        gold_rows=len(gold),max_gold_vs_continuous_oracle_kg=float(np.max(abs(actual-oracle))),
        scope='TMAP8 reduced-runtime fixture; not direct MATLAB reproduction or dual-reactor validation')
    (OUT/'benchmark_metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
    csvout('benchmark_curves.csv',[dict(time_s=float(t),**{f'{k}_{kind}':float(arr[i,j])
       for j,k in enumerate(NAMES) for kind,arr in [('gold',np.column_stack([gold[n] for n in NAMES])),('reproduced',actual),('continuous',oracle)]}) for i,t in enumerate(gold['time'])])
    p=json.loads((ROOT/'reference.json').read_text());p['days']=180
    scenarios=['baseline','extractor_7d','processor_7d','processor_30d','A_off_60d','B_off_40d','common_off_30d']
    results=[];bounds=[];plot={}
    energy_per_kg=17.6*1.602176634e-13/T_KG_PER_ATOM/3.6e12
    for name in scenarios:
        rows,s=run_case(p,name,10)
        results.append(dict(scenario=name,initial_kg=10,final_kg=s['final_kg'],min_B_storage_kg=s['min_b_store_kg'],
             unmet_T_burn_kg=s['b_unserved_burn_kg'],unmet_fusion_GWh=s['b_unserved_burn_kg']*energy_per_kg,
             mass_residual_kg=s['maximum_mass_residual_kg']))
        bounds.append(dict(scenario=name,**threshold(p,name)))
        plot[name]=[{k:r[k] for k in ['day','total_inventory','b_store','b_unserved_burn']} for r in rows]
    csvout('stress_tests.csv',results);csvout('startup_brackets.csv',bounds)
    # Numerical/parameter/model-structure uncertainties are reported separately.
    error=[]
    for h in (.25,.125,.0625,.03125):
        bound=threshold(p,'processor_7d',h)
        rows,s=run_case(p,'processor_7d',10,h)
        error.append(dict(step_days=h,startup_upper_kg=bound['upper_kg'],unmet_burn_kg=s['b_unserved_burn_kg'],final_kg=s['final_kg']))
    csvout('numerical_budget.csv',error)
    param=[]
    for key,vals in [('tbr_b',[.95,1.02,1.10]),('process_day',[2,4,8]),('b_pass_burn_fraction',[.025,.05,.1])]:
        for val in vals:param.append(dict(parameter=key,value=val,**threshold(dict(p,**{key:val}),'processor_7d')))
    csvout('parameter_budget.csv',param)
    extract=[compare(e,t,64.362/365.25,np.log(2)/(12.32*365.25)+.0001)
             for e,t in [(.1,30),(.25,15),(.5,10),(.85,10),(1.,10)]]
    csvout('extraction_comparison.csv',extract)
    (OUT/'stress_trajectories.json').write_text(json.dumps(plot,separators=(',',':')))
    report(metrics,results,bounds,error)
    manifest=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        source_commit='83dc89600c4956e08acd5d38df70d3cce83797e1',
        hashes={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(ROOT.rglob('*'))
          if f.is_file() and not any(a in f.parts for a in ('outputs','__pycache__'))})
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(metrics,indent=2))

def report(metrics,results,bounds,error):
    text=f'''# Beyond Q v1.1.1 — Benchmark and resilience verification

Research direction: Dave Sheldon / Atlas Lattice. GPT-6 computational work;
DeepSeek and Gemini Argon contributions retained from v1.1. No institutional
endorsement or experimental validation. G1–G5 remain physically OPEN.

## External computational benchmark

Independent Python implementation of the 11-stock Meschini equations in INL
TMAP8 reproduces all {metrics['gold_rows']} rows of its reduced-runtime gold
fixture to a maximum stock error of {metrics['max_abs_error_kg']:.3g} kg.
This is VERIFIED-DERIVED computational reproduction, not physical validation.
Source: Meschini et al., Nuclear Fusion 63 (2023) 126005,
doi:10.1088/1741-4326/acf3fc, via pinned TMAP8 input and gold CSV at commit
7dfbc71378fb243afba23db80a8284cd4b6429a4.

Matching the reference required backward Euler at the published timestamps,
with source forcing evaluated at the preceding accepted step. The upstream
test overrides initial_refinement_time to 17000 seconds; after that it uses
averaged 75% activity. A matrix-exponential continuous-time oracle splits at
each true source jump. Maximum difference between the reproduced gold and
continuous oracle is {metrics['max_gold_vs_continuous_oracle_kg']:.6g} kg:
agreement with a solver's recorded output does not remove discretization bias.
At t=0 upstream total_tritium is reported as zero despite 1.14 kg in storage;
we compare the 11 actual stocks, not that initial diagnostic artifact.

This literature fixture uses its own published burn rate, half-life, startup
stock and schedule; it does not replace our reference power configuration.
TMAP8/Matlab executables were not run here. The direct MATLAB CSV is not the
comparison target; this result reproduces INL's computational reference.

## Mapping to the dual-reactor model

The seven-stock Beyond Q model cannot be expected to match the 11-stock case
by changing scalars alone: it lumps cleanup/ISS, omits wall/divertor/HX and
detritiation recovery, uses different A/B sources and fuel-limited B operation.
The published fixture prescribes burn and terminates on exhausted storage.
We therefore reproduce the full fixture separately and retain Beyond Q as a
screening model. Benchmark success does not validate its lumping assumptions.

## Resilience scenarios — POTENTIAL-DERIVED

B remains 1130 MW D-T fusion; A hypothetical 20 MW primary D-D. Horizon 180
days; all requested on except explicit scenario windows. Initial A stock zero;
initial B stock 10 kg. Extraction/processing states are independent of reactor
states. With a failed processor, unburned fuel accumulates in processing,
cannot return to storage, and actual burn and breeding fall when feed runs out.

| Scenario | Final stock kg-T | Unmet B fusion GWh | Conditional startup bracket kg-T |
|---|---:|---:|---:|
'''
    for s,b in zip(results,bounds):text+=f"| {s['scenario']} | {s['final_kg']:.4f} | {s['unmet_fusion_GWh']:.4f} | {b['lower_kg']:.4f}–{b['upper_kg']:.4f} |\n"
    text+=f'''
Startup brackets use bisection on initial B storage, with a 200 kg upper
search bound, tolerance 1e-8 kg cumulative unmet burn, and 20 iterations.
They are finite-horizon fuel-availability bounds under assumed parameters,
not safe/qualified startup inventories or licensing reserves. No positive
regulatory reserve floor is imposed. Track substep minimum B storage as well
as daily final stocks; bisection width is not physical uncertainty.

## Error budget

Numerical: processor-7-day startup upper bracket changes from
{error[0]['startup_upper_kg']:.6f} kg at step .25 day to
{error[-1]['startup_upper_kg']:.6f} kg at .03125 day. See numerical_budget.csv
for all steps, unmet burn and final inventory. Exact single-compartment
updates still have coupling/scheduling discretization error.

Parameter: parameter_budget.csv varies TBR_B, processing residence rate and
pass burn fraction independently at fixed outage windows. These are assumed
input sensitivities, not statistical confidence intervals.

Structure: extraction_comparison.csv contrasts continuous well-mixed turnover
k=epsilon/tau with periodic discrete-pass removal at the same source/loop and
loss rate. Discrete stock has separate pre-pass, post-pass and cycle-mean
values; a continuous steady stock cannot be compared only to its post-pass
minimum. This is a standalone extraction module comparison, not a full
dual-reactor discrete-loop prediction. Full delay/age-structured coupling,
temperature/speciation and empirically calibrated failures remain open.

Independent measured parameter covariance, model discrepancy, transport,
startup qualification and wall-plug energy closure remain missing. No usable
surplus or physical self-sufficiency follows from these tests.
'''
    (OUT/'REPORT.md').write_text(text)

if __name__=='__main__':main()
