#!/usr/bin/env python3
from pathlib import Path
import csv,json,hashlib,sys,subprocess,unittest
from reconciliation import *
from fuelcycle.model import simulate
from fuelcycle.physics import argon_burn_fraction
from fuelcycle.schedules import generate

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'
def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def threshold(p,schedule):
    # Finite-horizon fuel-available storage non-depletion; not physical closure.
    lo,hi=.8,1.5
    def evaluate(t):
        rows,s=simulate(dict(p,tbr_b=t),schedule)
        return rows[-1]['b_store']>=p['initial_b_kg'] and s['b_unserved_burn_kg']<=1e-8
    if not evaluate(hi):return None
    for _ in range(22):
        mid=(lo+hi)/2
        if evaluate(mid):hi=mid
        else:lo=mid
    return hi

def main():
    OUT.mkdir(exist_ok=True)
    # Tests gate release; failures retained in text and machine-readable summary.
    proc=subprocess.run([sys.executable,'-m','unittest','test_review','-v'],cwd=ROOT,text=True,capture_output=True)
    (OUT/'regression_results.txt').write_text(proc.stdout+proc.stderr)
    (OUT/'regression_status.json').write_text(json.dumps({'passed':proc.returncode==0,'exit_code':proc.returncode},indent=2)+'\n')
    if proc.returncode:raise SystemExit('REGRESSION FAILURE; see outputs/regression_results.txt')
    p=json.loads((ROOT/'reference.json').read_text())
    f=argon_burn_fraction(p['a_fast_fraction'],p['a_density_m3'],p['a_reactivity_m3_s'],p['a_residence_s'])
    factors=[dict(convention=n,kg_per_GW_FPY=v,burn_B_kg_FPY=1.13*v) for n,v in
        [('legacy_55.8',55.8),('stoichiometric_17.6MeV',tritium_factor()),('17.59MeV_sensitivity',tritium_factor(17.59))]]
    write('mass_conventions.csv',factors)
    stat=[]
    for secondary in [False,True]:
        source=source_case(f if secondary else 0,p['a_dd_blanket_yield'],p['a_dt_blanket_yield'])
        for ep,eb in [(1.,1.),(.95,.90),(.85,.70),(0.,0.)]:
            b=static_balance(1.13*tritium_factor(),source['plasma_net_kg'],source['blanket_gross_kg'],ep,eb,1.02,.95)
            stat.append(dict(secondary_dt=secondary,eta_A_plasma=ep,eta_A_blanket=eb,**source,**b))
    write('annual_screening.csv',stat)
    legacy=static_balance(63.1,3.65,0,1,1,1.02,1)
    dynamic=[]
    for secondary in [False,True]:
        cfg=dict(p)
        if not secondary:cfg.update(a_reaction_day=0,a_fast_fraction=0)
        for regime in ['continuous','independent_common_outages']:
            schedule=[(1,1)]*p['days'] if regime=='continuous' else generate(p['days'],119,.9,.9,.05)
            rows,s=simulate(cfg,schedule)
            last=rows[-1]
            current_threshold=threshold(cfg,schedule)
            unified_cfg=dict(cfg,a_plasma_recovery=p['process_recovery'],
                a_blanket_recovery=p['process_recovery'],
                a_plasma_process_day=p['process_day'],a_blanket_process_day=p['process_day'])
            unified_threshold=threshold(unified_cfg,schedule)
            # Annual calendar mass sources, sinks and inventory change are separate.
            dynamic.append(dict(secondary_dt=secondary,schedule=regime,
                days_A=sum(a for a,b in schedule),days_B=sum(b for a,b in schedule),
                actual_B_burn_kg=last['b_burn'],A_plasma_recovered_kg=last['a_plasma_processed'],
                A_blanket_recovered_kg=last['a_blanket_processed'],
                A_plasma_loss_kg=last['a_plasma_process_loss'],A_blanket_loss_kg=last['a_blanket_process_loss'],
                gross_A_blanket_birth_kg=last['blanket_a_birth'],gross_B_blanket_birth_kg=last['blanket_b_birth'],
                initial_stock_kg=s['initial_kg'],final_stock_kg=s['final_kg'],stock_growth_kg=s['inventory_change_kg'],
                stock_growth_percent_actual_B_burn=100*s['inventory_change_kg']/last['b_burn'],
                decay_kg=last['decay'],process_loss_kg=last['process_loss'],permeation_kg=last['permeation'],
                A_storage_to_B_kg=last['a_to_b'],unmet_B_burn_kg=s['b_unserved_burn_kg'],
                residual_kg=s['maximum_mass_residual_kg'],
                finite_horizon_storage_threshold_tbr=current_threshold,
                unified_processing_counterfactual_threshold_tbr=unified_threshold,
                threshold_shift_from_split_processing=current_threshold-unified_threshold,
                qualified_usable_surplus_kg=None,status='POTENTIAL-DERIVED; self-sufficiency UNRESOLVED'))
            write(f'daily_secondary_{secondary}_{regime}.csv',rows)
    write('dynamic_reconciliation.csv',dynamic)
    write('enrichment_comparison_plan.csv',enrichment_plan())
    (OUT/'summary.json').write_text(json.dumps(dict(legacy_screening=legacy,constant_inventory_tonnes=constant_inventory_example(),
       all_physical_gates='OPEN',blanket_envelope='RETIRED as derived performance; retained only as historical unvalidated test range'),indent=2)+'\n')
    manifest={str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(ROOT.rglob('*'))
        if x.is_file() and not any(a in x.parts for a in ('outputs','__pycache__'))}
    (OUT/'source_hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(factor=tritium_factor(),annual_screening=stat,dynamic=dynamic),indent=2))

if __name__=='__main__':main()
