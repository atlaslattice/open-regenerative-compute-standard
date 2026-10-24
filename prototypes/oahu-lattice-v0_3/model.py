#!/usr/bin/env python3
"""Annual residual routing sensitivities, NOT measured cleanup or a cost forecast.

Tracks original-waste mass equivalents, not complete reaction/air/water mass.
External water/reagents, trace contaminants and density require separate design.
"""
import copy
import csv
import importlib.util
import json
import math
from pathlib import Path
P=Path(__file__).parent

def load_v01():
 for name in ['oahu-lattice-v0_1','oahu-lattice-v01']:
  p=P.parent/name
  if p.exists():
   spec=importlib.util.spec_from_file_location('v01',p/'model.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
   return m,json.loads((p/'inputs.json').read_text())
 raise FileNotFoundError('Sibling v0.1 required')

class Ledger:
 def __init__(self,baseline):
  
  if not math.isfinite(baseline) or baseline<=0: raise ValueError('invalid baseline')
  self.baseline=baseline; self.leaves={}; self.events=[]
 def add(self,key,mass,endpoint='residual'):
  if endpoint not in ['product','energy_or_gas','residual','contained']: raise ValueError('unknown endpoint')
  if key in self.leaves: raise ValueError('duplicate material identifier')
  if not math.isfinite(mass) or mass<0: raise ValueError('invalid mass')
  self.leaves[key]={'original_waste_t':mass,'endpoint':endpoint}
 def route(self,key,outputs,module,gate='unresolved'):
  if gate not in ['pass','unresolved','fail']: raise ValueError('invalid gate')
  if key not in self.leaves or self.leaves[key]['endpoint']!='residual':raise ValueError('cannot reconsume accepted/missing material')
  if any(e not in ['product','energy_or_gas','residual','contained'] for _,_,e in outputs):raise ValueError('unknown endpoint')
  if any(f<0 or not math.isfinite(f) for _,f,_ in outputs): raise ValueError('invalid fraction')
  if not math.isclose(sum(f for _,f,_ in outputs),1,abs_tol=1e-10):raise ValueError('route does not conserve source mass')
  if len({n for n,_,_ in outputs})!=len(outputs) or any(n in self.leaves for n,_,_ in outputs):raise ValueError('duplicate destination')
  mass=self.leaves[key]['original_waste_t']
  self.events.append(dict(input=key,feed_t=mass,module=module,gate=gate,actual_cost_usd=None))
  if gate!='pass':return
  self.leaves.pop(key)
  for name,f,endpoint in outputs:self.add(name,mass*f,endpoint)
 def summary(self,name):
  endpoints={k:sum(x['original_waste_t'] for x in self.leaves.values() if x['endpoint']==k) for k in ['product','energy_or_gas','residual','contained']}
  total=sum(x['original_waste_t'] for x in self.leaves.values())
  if not math.isclose(total,self.baseline,abs_tol=1e-6): raise ValueError('mass balance failed')
  avoided=endpoints['product']+endpoints['energy_or_gas']
  return dict(scenario=name,baseline_original_waste_t=self.baseline,**endpoints,
   source_mass_requiring_management_t=endpoints['residual']+endpoints['contained'],
   remaining_percent=100*(endpoints['residual']+endpoints['contained'])/self.baseline,
   removal_percent=100*avoided/self.baseline,
   mass_error_t=total-self.baseline,realized_project_credit_t=0,
   full_cost_usd=None,roi=None,all_material_remediated=False,
   final_streams=copy.deepcopy(self.leaves),routes=copy.deepcopy(self.events))

def base_ledger(cfg,processed):
 a=cfg['assumptions'];q=cfg['published_anchors'];conv=.90718474
 feed=q['wgsl_other_2024_us_short_tons']['value']*conv
 ash=q['wgsl_ash_residue_2024_us_short_tons']['value']*conv
 if not 0<=processed<=feed+1e-6:raise ValueError('processing exceeds feed')
 L=Ledger(feed+ash);f=a['feed_fraction'];metal=(f['ferrous']+f['nonferrous'])*a['metal_recovery']*a['metal_buyer_acceptance']
 fuel=f['combustibles']*a['conditional_combustible_acceptance'];fuelash=fuel*a['conditional_fuel_ash_fraction']
 mineral=f['mineral_fines']*a['conditional_mineral_qualified_fraction']*a['conditional_mineral_conversion_yield']
 for key,mass,endpoint in [
  ('incumbent_ash',ash,'residual'),('unprocessed_other_msw',max(0,feed-processed),'residual'),
  ('primary_metals',processed*metal,'product'),('unrecovered_metal_fraction',processed*(f['ferrous']+f['nonferrous']-metal),'residual'),
  ('accepted_primary_minerals',processed*mineral,'product'),('unqualified_mineral_fines',processed*(f['mineral_fines']-mineral),'residual'),
  ('fuel_nonash_original_mass',processed*(fuel-fuelash),'energy_or_gas'),('incremental_fuel_ash',processed*fuelash,'residual'),
  ('rejected_combustibles',processed*(f['combustibles']-fuel),'residual'),('uncharacterized_other',processed*f['other'],'residual')]:L.add(key,mass,endpoint)
 return L

def wash(L,yield_dry=.7,gate='pass'):
 # All split factors synthetic. Water remains a liability, not free diversion.
 dry=.65
 L.route('unqualified_mineral_fines',[
 ('washed_mineral_product',dry*yield_dry,'product'),
 ('wash_concentrate_dry',dry*(1-yield_dry),'residual'),
 ('inherent_water_liability',1-dry,'residual')],['D_01','D_02','D_03','D_04'],gate)

def ash_recovery(L,effective_yield=.6,gate='pass'):
 # Combined metal/aggregate accepted ORIGINAL mass fraction; not density/volume.
 # Eligible bottom/fly-ash split and mineral/metal assay remain unresolved.
 for key in ['incumbent_ash','incremental_fuel_ash']:
  L.route(key,[(key+'_qualified_products',effective_yield,'product'),
    (key+'_residual',1-effective_yield,'residual')],['P03','P04','M02','M12','X03'],gate)

def secondary(L,other_accept=.2,fuel_accept=.35,metal_accept=.5,gate='pass'):
 # These are accepted fractions of residual parent streams, not whole mixed feed.
 for key,fraction,mods in [('uncharacterized_other',other_accept,['P01','P05','M01','R02','O01']),
   ('rejected_combustibles',fuel_accept,['P05','R02']),
   ('unrecovered_metal_fraction',metal_accept,['P04','P06'])]:
  L.route(key,[(key+'_secondary_product',fraction,'product'),(key+'_secondary_reject',1-fraction,'residual')],mods,gate)

def contain_all(L):
 for key,row in list(L.leaves.items()):
  if row['endpoint']=='residual':
   L.route(key,[(key+'_contained',1,'contained')],['M10','M14','X03'],'pass')
 # Containment is an endpoint example; no assertion of site cleanup attainment.

def run():
 m,cfg=load_v01();_,v01=m.simulate(cfg,'conditional_integrated_200',tph=200,integrated=True)
 feed=cfg['published_anchors']['wgsl_other_2024_us_short_tons']['value']*.90718474
 first=base_ledger(cfg,v01['processed_t']);cases=[first.summary('S0_prior_conditional_integrated')]
 # Annual upper envelope: 300 shifts could accommodate feed IF permitted buffers,
 # schedules, all downstream capacities and acceptance exist. Not a daily forecast.
 L=base_ledger(cfg,feed);cases.append(L.summary('S1_full_incoming_capture_ENVELOPE'))
 wash(L);cases.append(L.summary('S2_add_selective_fines_washing'))
 ash_recovery(L);cases.append(L.summary('S3_add_60pct_ash_mass_recovery_TARGET'))
 secondary(L);cases.append(L.summary('S4_add_secondary_material_recovery'))
 before=copy.deepcopy(L);contain_all(L);cases.append(L.summary('S5_containment_does_not_increase_removal'))
 # Failed gate examples retain their input without imaginary output credit.
 failed=base_ledger(cfg,feed);wash(failed,gate='unresolved');ash_recovery(failed,gate='fail')
 cases.append(failed.summary('GATES_unresolved_washing_failed_ash'))
 # Isolate the existing ash initiative from proposed incremental MSW handling.
 incumbent=base_ledger(cfg,0)
 ash_recovery(incumbent);cases.append(incumbent.summary('INCUMBENT_ash_target_only_counterfactual'))
 # Fully unresolved new project baseline: all source material stays managed.
 unresolved=Ledger(first.baseline);unresolved.add('all_feed_without_project_clearance',first.baseline)
 cases.append(unresolved.summary('NO_NEW_ROUTE_CLEARANCE'))
 sensitivity=[]
 for wash_yield in [.4,.7,.85]:
  for ash_yield in [0,.3,.6,.8]:
   for other_yield in [0,.2,.4]:
    x=base_ledger(cfg,feed);wash(x,wash_yield);ash_recovery(x,ash_yield);secondary(x,other_yield)
    row=x.summary('SENSITIVITY_ONLY')
    sensitivity.append(dict(wash_dry_yield_ASSUMED=wash_yield,ash_accepted_mass_yield_TARGET=ash_yield,
      other_residual_accepted_yield_ASSUMED=other_yield,remaining_percent=row['remaining_percent'],
      source_mass_requiring_management_t=row['source_mass_requiring_management_t']))
 # Normalized policy/support budget frontier, not estimated treatment prices.
 frontier=[]
 prior=cases[0]
 for prev,cur in zip(cases[:4],cases[1:5]):
  added=prev['source_mass_requiring_management_t']-cur['source_mass_requiring_management_t']
  for unit in [25,50,100,200]:
   frontier.append(dict(step=cur['scenario'],additional_original_mass_removed_t=added,
    hypothetical_allowable_net_cost_usd_per_additional_t=unit,
    hypothetical_allowable_annual_incremental_net_cost_usd=added*unit,
    estimated_actual_cost_usd=None))
 out=P/'results';out.mkdir(exist_ok=True)
 results=dict(status='CONDITIONAL ANNUAL ENVELOPES; NO PROBABILITIES; ZERO REALIZED CREDIT',
  mass_basis='Original waste mass equivalents, not full chemical/wet-mass balance or permitted volume. energy_or_gas is original waste no longer solid, not total flue gas or emission credit.',
  baseline_scope='Fixed 2024 WGSL other MSW plus ash/residue, current annual inflow. No legacy inventory or separate C&D.',
  original_v01_reference=v01,scenarios=cases,
  changed_assumptions={'full_capture':'annual buffered-feed target, not daily simulation',
   'washing_dry_fraction':.65,'washing_dry_product_yield':.7,
   'ash_mass_product_yield_TARGET':.6,'other_residual_secondary_product_yield':.2,
   'rejected_fuel_secondary_polymer_product_yield':.35,'remaining_metal_secondary_product_yield':.5},
  incremental_credit_rule='Existing ash-recovery initiatives are incumbent counterfactuals, not new Atlas achievements. At same ash yield, compare S4 with INCUMBENT for numerical marginal contribution; counterfactual commissioning/timing unverified.',
  gross_washing_contact_water_t_per_year_assumed=feed*.155*.65*2,
  fresh_makeup_water_t=None,purge_t=None,added_reagent_residue_t=None,
  actual_residual_wet_disposal_t=None,net_airspace_m3=None,
  all_contaminants_cleared=False,bankable_cost_comparison=None,
  artifact_date_user_timezone='2026-10-23')
 (out/'summary.json').write_text(json.dumps(results,indent=2)+'\n')
 def write(name,rows):
  with (out/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 write('frontier.csv',frontier);write('sensitivity.csv',sensitivity)
 write('stages.csv',[{k:s[k] for k in ['scenario','product','energy_or_gas','source_mass_requiring_management_t','remaining_percent','removal_percent']} for s in cases])
 print(json.dumps([{k:s[k] for k in ['scenario','source_mass_requiring_management_t','remaining_percent']} for s in cases],indent=2))
 return results

if __name__=='__main__':run()
