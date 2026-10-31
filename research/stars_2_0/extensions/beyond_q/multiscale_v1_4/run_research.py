"""Reduced slowing/escape sensitivities and explicit8h event-clock inventories."""
from pathlib import Path
import json,csv,sys,math
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'kinetic_source_v1_3'))
from analyze import read_reduced
from slowing import coefficients,K_to_W,W_to_K,candidate,e,rate_table,rate_from,MT,MD,c
from fuelcycle.model import simulate
from fuelcycle.physics import T_KG_PER_ATOM,dd_source
OUT=ROOT/'outputs'
def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def drag_comparison():
 co=coefficients(1e20,1e4,1e20,2e4);ae=co['alpha_e_s'];ai=co['alpha_i_J32_s'];W0=K_to_W(1e6*e);errors=[];trajectories=[]
 for case in ('drag_100','drag_200'):
  d=read_reduced(OUT/'warpx'/case/'energy.txt');times=d['time(s)']
  sol=solve_ivp(lambda t,w:[-2*ae*w[0]-ai/math.sqrt(w[0])],[0,.101],[W0],method='DOP853',rtol=1e-11,atol=1e-30,dense_output=True)
  for species in ('T_e','T_i','T_both','T_control'):
   obs=d[species+'_mean(J)']/e;theory=[]
   for t in times:
    W=W0*math.exp(-2*ae*t) if species=='T_e' else max(0,W0**1.5-1.5*ai*t)**(2/3) if species=='T_i' else sol.sol(t)[0] if species=='T_both' else W0
    theory.append(W_to_K(W)/e)
   errors.append(dict(case=case,species=species,max_relative_error=float(np.max(np.abs(obs-np.array(theory))/np.array(theory))),duration_s=float(times[-1]),label='Shared approximate-drag numerical comparison; not physical validation'))
   for t,o,q in zip(times,obs,theory):trajectories.append(dict(case=case,species=species,time_s=t,WarpX_energy_eV=o,continuous_model_energy_eV=q))
 write('drag_comparison.csv',errors);write('drag_trajectories.csv',trajectories)
 # Independent continuous survival ODE vs actual simultaneous WarpX drag+DT.
 coupled=[];tab=rate_table(2e4)
 for case in ('coupled_100','coupled_200','coupled_no_drag'):
  n=read_reduced(OUT/'warpx'/case/'number.txt');en=read_reduced(OUT/'warpx'/case/'energy.txt');initial=n['T_weight()'][0]
  def rhs(t,y):
   W=y[0]*W0;dW=0 if case=='coupled_no_drag' else -2*ae*W-ai/math.sqrt(W)
   dK=dW/math.sqrt(1+2*W/(MT*c*c))
   return [dW/W0,-1e20*rate_from(tab,W_to_K(W))*y[1],-dK*y[1]/(1e6*e)]
  sol=solve_ivp(rhs,[0,.1],[1,1,0],method='DOP853',rtol=1e-11,atol=1e-13)
  obs=n['He4_weight()'][-1]/initial;pred=1-sol.y[1,-1]
  fusion_Q=n['He4_weight()'][-1]*17.58929696e6*e
  external_sink=en['total(J)'][0]+fusion_Q-en['total(J)'][-1]
  predicted_sink=sol.y[2,-1]*initial*1e6*e
  coupled.append(dict(case=case,duration_s=n['time(s)'][-1],WarpX_burn_fraction=obs,reduced_burn_fraction=pred,relative_difference=pred/obs-1,
    T_closure_fraction=float(np.max(abs(n['T_weight()']+n['He4_weight()']-initial)))/initial,
    neutron_coproduct_fraction=float(np.max(abs(n['neutron_weight()']-n['He4_weight()'])))/initial,
    final_T_energy_eV=en['T_mean(J)'][-1]/e,initial_total_kinetic_J=en['total(J)'][0],final_total_kinetic_J=en['total(J)'][-1],fusion_reaction_Q_J=fusion_Q,external_background_sink_J=external_sink,reduced_predicted_background_sink_J=predicted_sink,physical_validation=False))
 write('coupled_burn_comparison.csv',coupled)
 return errors,coupled

def main():
 OUT.mkdir(exist_ok=True);errors,coupled=drag_comparison();scans=[]
 for density in (5e19,1e20,2e20):
  for Te in (5e3,1e4,2e4):
   for tau in (.1,1.,10.,60.):
    r,_=candidate(ne=density,nD=density,Te_eV=Te,tau_fast_s=tau,tau_thermal_s=tau);scans.append(r)
 write('slowing_escape_sensitivity.csv',scans);base,_=candidate()
 (ROOT/'inputs/slowing_reference.json').write_text(json.dumps(base,indent=2)+'\n')
 transitions=[candidate(switch_eV=v)[0] for v in (1e5,2e5,3e5)];write('transition_sensitivity.csv',transitions)
 convergence=[]
 for order,tol in [(8,1e-9),(12,1e-9),(16,1e-9),(12,1e-7),(12,1e-11)]:
  r,_=candidate(order=order,rtol=tol);convergence.append(dict(quadrature_order=order,rtol=tol,p_fast_burn=r['p_fast_burn'],p_total_burn=r['p_total_burn'],time_s=r['time_to_switch_s']))
 write('slowing_numerical_convergence.csv',convergence)
 tr=ROOT.parent/'neutronics_v1_2/outputs/runs'
 def response(name):return json.loads((tr/name/'result.json').read_text())['tallies']['salt_T_tracklength:H3-production']['mean']
 settings=json.loads((ROOT.parent/'neutronics_v1_2/inputs/fuel_cycle.json').read_text());settings.pop('days')
 settings.update(schedule_slots=480,schedule_interval_days=1/1440,step_days=1/1440,
  a_fast_fraction=base['p_fast_burn'],a_fast_escape_fraction=base['p_fast_escape'],
  a_reaction_day=base['thermal_reaction_rate_s']*86400,a_escape_day=86400/base['tau_thermal_s'],
  a_density_m3=base['nD_m3'],a_reactivity_m3_s=base['thermal_reaction_rate_s']/base['nD_m3'],a_residence_s=base['tau_thermal_s'],
  source_reduction_status='POTENTIAL-DERIVED approximate drag and imposed escape, not reactor confinement')
 definitions={'A0':('DD_A0_both_Li_zero','DT_A0_both_Li_zero'),'A1':('DD_Li0.075_cm90','DT_Li0.075_cm90'),'A2':('DD_Li0.9_cm120','DT_Li0.9_cm120')}
 rows=[];recorded=[]
 for identity,Pa,Pb in [('historical_20_1130',20.,1130.),('dual_laser_1100_1100',1100.,1100.)]:
  for label,(DD,DT) in definitions.items():
   for condition in ('continuous','B_15min_outage','common_30min_outage','processor_30min_outage','extractor_30min_outage','zero_initial_B','poor_recovery','zero_A_transfer_reserve','secondary_off'):
    cfg=dict(settings,configuration_id=identity,power_a_dd_mw=Pa,power_b_dt_mw=Pb,A_gross_fusion_W=Pa*1e6,B_gross_fusion_W=Pb*1e6,A_net_electric_W=20e6 if identity.startswith('dual') else None,
     case=label,a_dd_blanket_yield=response(DD),a_dt_blanket_yield=response(DT),tbr_b=response('DT_Li0.075_cm90'),a_yield_status='Reused v1.2 assumed spherical-testbed transport; no new laser/geometry/source-spectrum qualification')
    schedule=[(1,1)]*480;components=[(1,1,1,1)]*480
    if condition=='B_15min_outage':
     for j in range(120,135):schedule[j]=(1,0)
    if condition=='common_30min_outage':
     for j in range(240,270):schedule[j]=(0,0)
    if condition=='processor_30min_outage':
     for j in range(180,210):components[j]=(1,1,1,0)
    if condition=='extractor_30min_outage':
     for j in range(180,210):components[j]=(1,0,1,1)
    if condition=='zero_initial_B':cfg['initial_b_kg']=0
    if condition=='poor_recovery':cfg.update(a_plasma_recovery=.7,a_blanket_recovery=.6,process_recovery=.99)
    if condition=='zero_A_transfer_reserve':cfg['reserve_a_kg']=0
    if condition=='secondary_off':cfg.update(a_fast_fraction=0,a_reaction_day=0)
    trajectory,s=simulate(cfg,schedule,components);z=trajectory[-1]
    recorded.append(dict(configuration_id=identity,case=label,condition=condition,parameters=cfg,reactor_schedule=schedule,component_schedule=components))
    rows.append(dict(configuration_id=identity,case=label,condition=condition,duration_hours=z['time_hours'],A_gross_fusion_W=Pa*1e6,B_gross_fusion_W=Pb*1e6,
      A_on_minutes=sum(v[0] for v in schedule),B_on_minutes=sum(v[1] for v in schedule),DD_T_birth_kg=z['dd_birth'],A_internal_burn_kg=z['a_burn'],
      A_blanket_birth_kg=z['blanket_a_birth'],B_blanket_birth_kg=z['blanket_b_birth'],A_plasma_recovered_kg=z['a_plasma_processed'],A_blanket_recovered_kg=z['a_blanket_processed'],
      A_to_B_kg=z['a_to_b'],B_actual_burn_kg=z['b_burn'],B_unserved_burn_kg=z['b_unserved_burn'],B_recirculated_kg=z['b_recirculated'],
      initial_kg=s['initial_kg'],final_kg=s['final_kg'],stock_change_kg=s['inventory_change_kg'],stock_change_percent_B_burn=100*s['inventory_change_kg']/z['b_burn'] if z['b_burn'] else None,
      B_store_final_kg=z['b_store'],processing_stock_kg=z['a_plasma_process']+z['a_blanket_process']+z['b_process'],decay_kg=z['decay'],processing_loss_kg=z['process_loss'],permeation_kg=z['permeation'],
      mass_residual_kg=s['maximum_mass_residual_kg'],qualified_surplus_kg=None,neglected_fast_transit_inventory_upper_kg=dd_source(Pa)['t_atoms_s']*T_KG_PER_ATOM*base['time_to_switch_s'],evidence='POTENTIAL-DERIVED8h accounting; no qualified reactor/laser performance'))
    if condition=='continuous':write(identity+'_'+label+'_trajectory.csv',trajectory)
 write('eight_hour_summary.csv',rows)
 def runs(schedule):
  out=[];start=0
  for j in range(1,len(schedule)+1):
   if j==len(schedule) or schedule[j]!=schedule[start]:
    out.append([start,j,*schedule[start]]);start=j
  return out
 saved=[dict(configuration_id=x['configuration_id'],case=x['case'],condition=x['condition'],parameters=x['parameters'],reactor_schedule_runs=runs(x['reactor_schedule']),component_schedule_runs=runs(x['component_schedule'])) for x in recorded]
 (ROOT/'inputs/scenarios.json').write_text(json.dumps(saved,indent=2)+'\n')
 refine=[];startup=[]
 for identity in ('historical_20_1130','dual_laser_1100_1100'):
  source=next(x for x in recorded if x['configuration_id']==identity and x['case']=='A1' and x['condition']=='continuous')
  for h in (1/1440,1/2880,1/5760):
   _,o=simulate(dict(source['parameters'],step_days=h),source['reactor_schedule']);refine.append(dict(configuration_id=identity,step_seconds=h*86400,final_kg=o['final_kg'],unserved_burn_kg=o['b_unserved_burn_kg'],mass_residual_kg=o['maximum_mass_residual_kg']))
  for condition in ('continuous','processor_30min_outage'):
   source=next(x for x in recorded if x['configuration_id']==identity and x['case']=='A1' and x['condition']==condition);lo,hi=0.,10.
   for _ in range(20):
    mid=(lo+hi)/2;_,o=simulate(dict(source['parameters'],initial_b_kg=mid),source['reactor_schedule'],source['component_schedule'])
    if o['b_unserved_burn_kg']>1e-10:lo=mid
    else:hi=mid
   startup.append(dict(configuration_id=identity,case='A1',condition=condition,initial_B_lower_kg=lo,initial_B_upper_kg=hi,criterion='8h unmet burn<=1e-10kg, no regulatory floor',qualified_startup_inventory_kg=None))
 write('eight_hour_timestep_refinement.csv',refine);write('eight_hour_startup_brackets.csv',startup)
 (OUT/'execution_summary.json').write_text(json.dumps(dict(actual_WarpX_runs=6,upstream_stopping_analysis_passed=True,physical_WarpX_drag_duration_s=.1,slowing_sensitivity_cases=len(scans),integrated_8hour_cases=len(rows),all_physical_gates='OPEN',qualified_surplus_kg=None,reference=base,maximum_drag_error=max(r['max_relative_error'] for r in errors),coupled_comparisons=coupled),indent=2)+'\n')
 print(json.dumps(dict(drag=errors,coupled=coupled,reference=base),indent=2))
if __name__=='__main__':main()
