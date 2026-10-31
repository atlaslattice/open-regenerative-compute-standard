"""Conditional one-FPY startup scheduling; no operational qualification."""
from pathlib import Path
import sys,json,csv,math
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'multiscale_v1_4'))
from fuelcycle.model import simulate
from fuelcycle.physics import dd_source,FPY_S,T_KG_PER_ATOM,dt_events
OUT=ROOT/'outputs';FPY_HOURS=8766

def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def base(case):
 records=json.loads((ROOT.parent/'multiscale_v1_4/inputs/scenarios.json').read_text())
 p=dict(next(x['parameters'] for x in records if x['configuration_id']=='dual_laser_1100_1100' and x['case']==case and x['condition']=='continuous'))
 p.update(schedule_interval_days=1/24,step_days=1/24,initial_a_kg=0,initial_b_kg=0)
 return p

def run(p,pre_hours,run_hours=FPY_HOURS,source_A=True):
 schedule=[(1,0)]*pre_hours+[(int(source_A),1)]*run_hours
 return simulate(dict(p,schedule_slots=len(schedule)),schedule)

def main():
 OUT.mkdir(exist_ok=True)
 # Gross/steady arithmetic, explicitly not qualified delivered production.
 annual=[]
 for case in ('A0','A1','A2'):
  p=base(case);birth=dd_source(1100)['t_atoms_s']*FPY_S*T_KG_PER_ATOM
  k=p['a_reaction_day']/(p['a_reaction_day']+p['a_escape_day'])
  f=p['a_fast_fraction']+(1-p['a_fast_fraction']-p['a_fast_escape_fraction'])*k
  plasma=birth*(1-f)*p['a_plasma_recovery'];blanket=(birth*p['a_dd_blanket_yield']+birth*f*p['a_dt_blanket_yield'])*p['a_blanket_recovery']
  B=dt_events(1100)*FPY_S*T_KG_PER_ATOM
  annual.append(dict(case=case,FPY_days=365.25,A_T_gross_birth_kg=birth,A_internal_burn_fraction=f,A_internal_burn_kg=birth*f,
     A_plasma_eventual_recovery_screen_kg=plasma,A_blanket_eventual_recovery_screen_kg=blanket,B_full_power_burn_kg=B,
     plasma_only_A_to_B_burn_ratio=plasma/B,
     status='POTENTIAL-DERIVED steady arithmetic before route delay, decay, holdup and repeated processing; not qualified annual surplus'))
 write('annual_screening.csv',annual)
 # Reserve capable of one FPY with no A contribution and NO B breeding credit.
 # This is an isolated B-bank requirement, not a combined full-facility mass ledger.
 p=base('A0');p['tbr_b']=0
 lo,hi=0.,100.
 for _ in range(17):
  mid=(lo+hi)/2;_,s=run(dict(p,initial_b_kg=mid),0,source_A=False)
  if s['b_unserved_burn_kg']>1e-8:lo=mid
  else:hi=mid
 bank=hi;traj,s=run(dict(p,initial_b_kg=bank),0,source_A=False)
 bank_result=dict(lower_kg=lo,upper_kg=hi,criterion='One365.25day FPY, unserved burn<=1e-8kg, no A, B breeding=0, no regulatory reserve',B_burn_kg=traj[-1]['b_burn'],decay_kg=traj[-1]['decay'],processing_loss_kg=traj[-1]['process_loss'],final_mobile_kg=s['final_kg'],max_mass_residual_kg=s['maximum_mass_residual_kg'],qualified_startup_inventory_kg=None)
 (OUT/'one_year_bank.json').write_text(json.dumps(bank_result,indent=2)+'\n')
 print('bank',bank_result,flush=True)
 outputs=[];refinements=[]
 for case in ('A0','A1','A2'):
  p=base(case)
  # Earliest whole-hour start, A continues and inherited B breeding is credited.
  lo,hi=0,24*30
  while lo<hi:
   mid=(lo+hi)//2;_,s=run(p,mid)
   if s['b_unserved_burn_kg']>1e-8:lo=mid+1
   else:hi=mid
  coarse=hi;start=coarse
  # Independently refine within each hourly schedule slot; increase precharge if necessary.
  for _ in range(48):
   trajectory,s=run(dict(p,step_days=1/96),start)
   if s['b_unserved_burn_kg']<=1e-8:break
   start+=1
  else:raise ValueError('refined startup search failed')
  while start>1:
   prior,check=run(dict(p,step_days=1/96),start-1)
   if check['b_unserved_burn_kg']>1e-8:break
   start-=1;trajectory,s=prior,check
  launch=trajectory[start-1];end=trajectory[-1]
  outputs.append(dict(case=case,policy='A continues; inherited B testbed breeding credited',coarse_start_hours=coarse,refined_fuel_available_start_hours=start,
    refined_fuel_available_start_days=start/24,B_available_at_start_kg=launch['b_store'],total_mobile_at_start_kg=launch['total_inventory'],
    one_FPY_B_burn_kg=end['b_burn'],unserved_burn_kg=s['b_unserved_burn_kg'],stock_growth_during_B_year_kg=end['total_inventory']-launch['total_inventory'],
    A_delivered_to_B_during_B_year_kg=end['a_to_b']-launch['a_to_b'],B_available_end_kg=end['b_store'],
    max_mass_residual_kg=s['maximum_mass_residual_kg'],qualified_surplus_kg=None))
  # A-only charging profile; B sources and B feed are absent, transfers still operate.
  charge,_=simulate(dict(p,schedule_slots=24*240),[(1,0)]*(24*240))
  hit=next((r for r in charge if r['b_store']>=bank),None)
  outputs.append(dict(case=case,policy='Bank entire B year, no future A/B breeding credit',coarse_start_hours=None,refined_fuel_available_start_hours=None,
    refined_fuel_available_start_days=hit['time_hours']/24 if hit else None,B_available_at_start_kg=hit['b_store'] if hit else None,
    total_mobile_at_start_kg=hit['total_inventory'] if hit else None,one_FPY_B_burn_kg=bank_result['B_burn_kg'],unserved_burn_kg=None,
    stock_growth_during_B_year_kg=None,A_delivered_to_B_during_B_year_kg=None,B_available_end_kg=None,
    max_mass_residual_kg=max(abs(r['mass_residual_kg']) for r in charge),qualified_surplus_kg=None))
  if case=='A1':
   # Reduced trajectory for inspectable start/end accounting, no repeated throughput summed as births.
   write('A1_staged_year.csv',[{k:r[k] for k in ['time_hours','on_a','on_b','total_inventory','b_store','a_store','b_process','b_burn','a_to_b','mass_residual_kg']} for r in trajectory])
   # Boundary falsification: preceding hour at the finer timestep.
   _,previous=run(dict(p,step_days=1/96),max(0,start-1))
   refinements.append(dict(case=case,selected_start_hours=start,selected_unserved_kg=s['b_unserved_burn_kg'],previous_hour_unserved_kg=previous['b_unserved_burn_kg'],step_minutes=15))
  print(case,outputs[-2:],flush=True)
 write('startup_policies.csv',outputs);write('startup_boundary_check.csv',refinements)
 (OUT/'assumptions.json').write_text(json.dumps(dict(reference='v1.4 current dual_laser_1100_1100',A_gross_fusion_W=1.1e9,B_gross_fusion_W=1.1e9,FPY_days=365.25,
  B_initial_inventory_source='A-only DD production in staged scenarios; isolated bank-sizing run starts from explicit inventory',A_to_B_reserve_kg=.25,
  physical_validation=False,qualified_usable_surplus_kg=None,
  limits=['Prescribed fusion power; no demonstrated laser operating point','Uncalibrated plasma escape and recovery','Inherited unqualified spherical-testbed TBR','No outages in one-year reference','Hourly precharge search,15minute staged-year refinement','Finite-horizon condition cannot establish indefinite operation']),indent=2)+'\n')
 print(json.dumps(annual,indent=2))
if __name__=='__main__':main()
