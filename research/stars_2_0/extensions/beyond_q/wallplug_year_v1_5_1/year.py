"""Replay the archived A1 staged year; hourly energy accounting, no new physics."""
from pathlib import Path
import csv, hashlib, importlib.util, json, math, sys
ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent
sys.path.insert(0,str(PARENT/'startup_year_v1_4_1'))
from calculate import base,run
spec=importlib.util.spec_from_file_location('wallplug',PARENT/'wallplug_checkpoint_v1_5/ledger.py')
wallplug=importlib.util.module_from_spec(spec);spec.loader.exec_module(wallplug)
OUT=ROOT/'outputs'

def delta_input(row,prior,p):
    hours=row['time_hours']-prior.get('time_hours',0.)
    if not math.isclose(hours,1.):raise ValueError('adapter requires hourly output slots')
    vals={dest:row[src]-prior.get(src,0.) for dest,src in [('DD_T_birth_kg','dd_birth'),('A_internal_burn_kg','a_burn'),('B_actual_burn_kg','b_burn')]}
    if min(vals.values()) < -1e-12:raise ValueError('nonmonotonic reaction counter')
    return dict(**vals,duration_hours=hours,A_gross_fusion_W=p['A_gross_fusion_W'],B_gross_fusion_W=p['B_gross_fusion_W'],
                A_on_minutes=60*hours*row['on_a'],B_on_minutes=60*hours*row['on_b'])

def validate_replay(rows, archived):
    if len(rows)!=len(archived):raise ValueError('archived clock length mismatch')
    error=0.
    for r,a in zip(rows,archived):
        if float(a['time_hours'])!=r['time_hours']:raise ValueError('archived clock mismatch')
        for k,v in a.items():error=max(error,abs(r[k]-float(v)))
    if error>1e-9:raise ValueError('archived trajectory replay disagreement')
    return error

def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    OUT.mkdir(exist_ok=True)
    policies=list(csv.DictReader((PARENT/'startup_year_v1_4_1/outputs/startup_policies.csv').read_text().splitlines()))
    policy=next(x for x in policies if x['case']=='A1' and x['policy'].startswith('A continues'))
    pre=int(policy['refined_fuel_available_start_hours'])
    p=base('A1');p['step_days']=1/96
    rows,summary=run(p,pre)
    archived=list(csv.DictReader((PARENT/'startup_year_v1_4_1/outputs/A1_staged_year.csv').read_text().splitlines()))
    error=validate_replay(rows,archived)
    inputs=json.loads((PARENT/'wallplug_checkpoint_v1_5/inputs.json').read_text())
    phase_results=[];daily=[];costs=[]
    energy_keys=['A_primary_DD_J','A_secondary_DT_J','B_actual_DT_J','total_fusion_Q_J','A_laser_electric_J','B_laser_electric_J','gross_generated_electric_J','auxiliary_electric_J','net_electric_J','imported_electric_kWh','positive_electric_before_campus_load_kWh']
    for q in inputs:
        bins={};days={};prior={}
        for row in rows:
            r=delta_input(row,prior,p);e=wallplug.electricity(r,q)
            phase='A_only_startup' if row['time_hours']<=pre else 'B_operating_year'
            day=int((row['time_hours']-1)//24)+1
            for bucket,key in [(bins,phase),(days,day)]:
                b=bucket.setdefault(key,dict(hours=0.,**{k:0. for k in energy_keys}))
                b['hours']+=r['duration_hours']
                for k in energy_keys:b[k]+=e[k]
            prior=row
        for phase,b in bins.items():
            phase_results.append(dict(energy_case=q['case_id'],phase=phase,**b,average_net_electric_MW=b['net_electric_J']/b['hours']/3.6e9,qualified_export_kWh=None,profit_USD=None,status='POTENTIAL-DERIVED; assumed gain and engineering inputs'))
            for price in (.05,.10,.2):
                costs.append(dict(energy_case=q['case_id'],phase=phase,assumed_import_price_USD_per_kWh=price,
                    interval_import_charge_USD=b['imported_electric_kWh']*price,export_credit_USD=None,isotope_revenue_USD=None,total_cost_USD=None,profit_USD=None))
        if q['case_id']=='gain10_eta0.2':
            daily=[dict(day=d,**b) for d,b in days.items()]
    write('phase_energy.csv',phase_results);write('daily_reference.csv',daily);write('import_price_sensitivity.csv',costs)
    check=dict(physical_validation=False,all_physical_gates='OPEN',replay_max_absolute_difference=error,hours=len(rows),startup_hours=pre,B_operating_hours=8766,
        B_unserved_burn_kg=summary['b_unserved_burn_kg'],maximum_mass_residual_kg=summary['maximum_mass_residual_kg'],qualified_surplus_kg=None,profit_USD=None,
        source_commit='3ed8d2029f14c4446527a53ed84c3114cc55c3fe',scenario='dual_laser_1100_1100/A1/continuous',
        caveat='Prescribed 1.1GW primary DD plus additional secondary DT for A; prescribed 1.1GW DT for B. Historical20MW/1130MW is separate. No laser simulation or new transport run.')
    (OUT/'checks.json').write_text(json.dumps(check,indent=2)+'\n')
    files=[PARENT/'startup_year_v1_4_1/calculate.py',PARENT/'startup_year_v1_4_1/outputs/A1_staged_year.csv',PARENT/'startup_year_v1_4_1/outputs/startup_policies.csv',PARENT/'wallplug_checkpoint_v1_5/ledger.py',PARENT/'wallplug_checkpoint_v1_5/inputs.json',PARENT/'multiscale_v1_4/inputs/scenarios.json']+list((PARENT/'multiscale_v1_4/fuelcycle').glob('*.py'))
    (OUT/'source_sha256.json').write_text(json.dumps({str(f.relative_to(PARENT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},indent=2)+'\n')
    print(json.dumps(check,indent=2))
    for r in phase_results:
        if r['energy_case'] in ('gain10_eta0.2','gain100_eta0.2'):print(r['energy_case'],r['phase'],'mean MW',r['average_net_electric_MW'],'import GWh',r['imported_electric_kWh']/1e6)
if __name__=='__main__':main()
