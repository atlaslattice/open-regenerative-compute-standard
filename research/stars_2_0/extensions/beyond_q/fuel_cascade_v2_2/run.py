"""Run new cascade and policy controls, preserving all earlier versions."""
from pathlib import Path
import argparse,csv,json,time,hashlib,platform
import numpy as np
from kernel import simulate,YEAR,T_ATOM,MEV
from controller import Controller
from finance import connected_financials

ROOT=Path(__file__).resolve().parent

def write(path,rows):
    if not rows:return
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)

def case(p,n,name):
    q=json.loads(json.dumps(p));control=None
    if name=='fixed_calendar':q['intermodule_transfers']=False
    elif name=='synchronized_seeded_control':
        q['intermodule_transfers']=False;q['commissioning_interval_years']=0
        q['initial_T_kg']=q['B_fusion_MW']*1e6/(17.6*MEV)*86400*T_ATOM*YEAR*q['startup_full_power_years_B']+q['B_storage_reserve_kg']
    else:
        readiness='strict' if name=='strict_unresolved' else 'conditional'
        policy='all_previous_qualified' if name=='sequential_predecessors' else 'eligible_pool'
        if name=='financing_denied':q['cascade']['financed_project_ids']=[1]
        if name=='no_surplus':q['A_macro_availability']=0.
        control=Controller(q,n,readiness,policy)
    rows,stocks,checks=simulate(q,n,control)
    events=control.events if control else []
    if control:
        checks.update(control.summary(control.last_counters))
        checks['B_started_modules']=sum(r['startup_day'] is not None for r in rows[-n:])
    else:
        checks['commissioned_modules']=n;checks['B_started_modules']=sum(r['startup_day'] is not None for r in rows[-n:])
    checks.update(scenario=name,modules=n,initial_T_per_module_kg=q['initial_T_kg'],
        resolved_overrides={k:q[k] for k in q if q[k]!=p[k]})
    finances=[]
    for recovery in q['He3_overall_recovery_cases']:
        for cap in [None,q['He3_market_cap_STP_L_per_year_fleet']]:
            market=dict(q,offtake_case='full_offtake_sensitivity' if cap is None else 'fleet_cap_stress',He3_market_cap_STP_L_per_year_fleet=cap)
            for price in [1500.,500.]:
                prices=dict(market,He3_price_USD_per_STP_L=price,T_price_USD_per_gram=price,
                    price_case='requested_1500' if price==1500 else 'pressure_500')
                for r in connected_financials(rows,prices,recovery):r['scenario']=name;finances.append(r)
    return rows,stocks,events,finances,checks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--years',type=int);ap.add_argument('--modules',type=int,default=50)
    ap.add_argument('--cases',nargs='+',default=['strict_unresolved','sequential_predecessors','eligible_pool','fixed_calendar','synchronized_seeded_control'])
    ap.add_argument('--out',default='outputs');ap.add_argument('--inputs',default=str(ROOT/'inputs.json'));args=ap.parse_args()
    p=json.loads(Path(args.inputs).read_text())
    if args.years:p['years']=args.years
    out=ROOT/args.out;out.mkdir(exist_ok=True);start=time.time();all_fin=[];all_stocks=[];checks=[]
    for name in args.cases:
        rows,stocks,events,finances,check=case(p,args.modules,name)
        write(out/f'module_ledger_{name}.csv',rows)
        with (out/f'events_{name}.jsonl').open('w') as f:
            for e in events:f.write(json.dumps(e)+'\n')
        for r in stocks:r['scenario']=name
        all_stocks+=stocks;all_fin+=finances;checks.append(check)
        print(json.dumps(check),flush=True)
    write(out/'annual_finance.csv',all_fin);write(out/'fleet_inventory.csv',all_stocks)
    write(out/'summary.csv',[r for r in all_fin if r['year'] in [1,2,5,10,20,30,31,40,50,60]])
    (out/'execution.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,inputs=p,modules=args.modules,
        checks=checks,runtime_seconds=time.time()-start),indent=2)+'\n')
    (out/'input_code_hashes.json').write_text(json.dumps({f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['inputs.json','kernel.py','controller.py','finance.py','run.py']},indent=2)+'\n')
    print(f'Completed {len(checks)} cases, {len(all_fin)} finance rows, {time.time()-start:.1f}s',flush=True)

if __name__=='__main__':main()
