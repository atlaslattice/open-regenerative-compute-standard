#!/usr/bin/env python3
"""Reproduce national screening scenarios. No network or third-party dependencies."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def crf(rate,years):return rate/(1-(1+rate)**(-years)) if rate else 1/years

def calculate(inputs):
 base=inputs['previous_nutrient_research'];a=inputs['parameters'];result={'schema_version':'1.0','analysis_version':'0.3','status':'NATIONAL_SCREENING_NOT_ENGINEERING_FORECAST','as_of':'2026-10-16 America/Chicago','parameters':a,'sources':inputs['sources'],'scope':inputs['scope'],'scenarios':[]}
 for b in base['scenarios']:
  f=b['net_qualified_recovery_fraction_or_energy_deployment_share'];n=b['gross_nutrient_screen'];nutval=b['nutrient_valuation'];st=b['all_recovered_P_as_pure_struvite_illustration'];s={'fraction':f,'nutrients':n,'nutrient_valuation':nutval,'disposal_P_subset':b['largest_plants_disposal_P_subset'],'struvite_illustration':st}
  # All qualified P is represented as struvite in this particular COST stress test.
  # Its nitrogen is already in the overall N inventory and bears no separate N-recovery cost.
  cost=[]
  realized=nutval['total_P_N_K_replacement_value_usd_year']*a['nutrient_realization_fraction']
  for k,unit in a['nutrient_allin_USD_per_kg_qualified_nutrient'].items():
   total=n['P_t_year']*1000*unit['P']+st['standalone_ammonium_N_after_struvite_t_year']*1000*unit['standalone_N']+n['K2O_equivalent_t_year']*1000*unit['K2O']
   cost.append({'case':k,'annual_allin_cost_usd':total,'modeled_realized_nutrient_receipts_usd':realized,'margin_before_avoided_baseline_usd':realized-total,'nonoverlapping_avoided_baseline_needed_for_break_even_usd':max(0,total-realized)})
  s['nutrient_cost_stress_tests']=cost;s['legacy_HTL_disposal_savings_reference']={'usd_year':1.4e9*f,'basis':'Linear scaling of an older national-model estimate only (S33). Not a current measured baseline; excluded from all margins and product totals.'}
  methane=a['historic_wastewater_methane_potential_t_year']*f;energy_GJ=methane*a['methane_HHV_GJ_t'];energy_MWh=energy_GJ/3.6
  grossE=energy_MWh*a['CHP_electric_fraction_HHV'];netE=grossE*(1-a['CHP_electric_parasitic_fraction']);heat=energy_MWh*a['CHP_heat_fraction_HHV'];availableHeat=heat*a['CHP_heat_fraction_available_for_external_offset']
  usefulHeatUSD=a['industrial_gas_USD_Mcf']/a['gas_MMBtu_Mcf']/a['displaced_boiler_efficiency']
  elecvalue=netE*a['electricity_avoided_proxy_USD_MWh'];heatvalue=availableHeat*3.412141633*usefulHeatUSD
  nameplate_kw=grossE/(8760*a['CHP_capacity_factor'])*1000
  capcases=[]
  for k,c in a['CHP_capital_budget_USD_kW'].items():
   capex=nameplate_kw*c;annualcap=capex*crf(a['finance_rate'],a['finance_years']);om=grossE*1000*a['CHP_variable_OM_USD_gross_kWh'];benefit=elecvalue+heatvalue
   capcases.append({'case':k,'capital_budget_usd':capex,'annualized_capital_usd':annualcap,'annual_OM_usd':om,'annual_energy_value_usd':benefit,'margin_before_unbudgeted_costs_and_baseline_adjustment_usd':benefit-annualcap-om})
  s['CHP']={'methane_input_t_year':methane,'fuel_energy_GJ_year':energy_GJ,'gross_electric_MWh_year':grossE,'net_electric_MWh_year':netE,'recoverable_heat_MWh_year':heat,'heat_available_for_external_offset_MWh_year':availableHeat,'net_electricity_import_volume_equivalent_percent':netE/a['electricity_gross_imports_MWh_2025']*100,'electric_value_at_avoided_proxy_usd_year':elecvalue,'electric_value_at_wholesale_proxy_usd_year':netE*a['electricity_wholesale_proxy_USD_MWh'],'heat_avoided_fuel_value_usd_year':heatvalue,'total_energy_value_at_avoided_proxy_usd_year':elecvalue+heatvalue,'generator_nameplate_kW':nameplate_kw,'capital_budget_stress_tests':capcases,'limits':'Gross historic resource deployment, not additional net recovery. Retail-average electricity is a proxy; only avoidable bill components qualify. Useful heat assumes a matched sink. Capital budgets are assumptions; full project costs need site engineering. Existing generation/heat use and costs are not known.'}
  rng_GJ=energy_GJ*(1-a['RNG_gas_reserved_for_process_heat'])*a['RNG_upgrade_methane_recovery'];rngMMBtu=rng_GJ/1.05505585262;rngbcf=rngMMBtu/a['gas_MMBtu_Mcf']/1e6
  s['RNG']={'saleable_MMBtu_year':rngMMBtu,'saleable_billion_cubic_feet_year':rngbcf,'Henry_Hub_gross_value_usd_year':rngMMBtu*a['Henry_Hub_USD_MMBtu'],'gross_gas_import_volume_equivalent_percent':rngbcf/a['gas_gross_imports_bcf_2025']*100,'net_margin_usd':None,'limits':'Alternative to burning the same gas in CHP. Upgrading, compression, grid connection, methane slip, O&M and capex must be priced; environmental credits excluded. U.S. is a net gas exporter.'}
  crude=a['rounded_biocrude_potential_gal_year']*f;finished=crude*a['HTL_finished_fuel_volume_yield'];diesel=finished*a['HTL_diesel_fraction_finished'];other=finished-diesel
  s['HTL']={'biocrude_gal_year':crude,'assumed_finished_fuels_gal_year':finished,'assumed_diesel_gal_year':diesel,'other_finished_fuel_gal_year':other,'diesel_only_gross_wholesale_value_usd_year':diesel*a['Gulf_ULSD_USD_gal'],'other_product_value_usd_year':None,'diesel_volume_equivalent_percent_of_distillate_imports':diesel/(a['distillate_gross_imports_bbl_2025']*42)*100,'raw_biocrude_volume_percent_of_crude_imports':crude/42/(a['crude_gross_imports_bpd_2025']*365)*100,'net_margin_usd':None,'limits':'Alternative raw-sludge route to full AD potential. Finished volume yield and diesel split are explicit assumptions, not national engineering outputs. Upgrading H2/energy, transport, rejects, aqueous treatment, catalysts and capex missing. No credit revenue assumed.'}
  # Nutrient and energy price levels and counterfactuals differ. Do not sum into a profit headline.
  result['scenarios'].append(s)
 Q=base['baseline']['annual_wastewater_m3'];sourceHeat=Q*4.186*a['wastewater_heat_delta_C']/3600*a['wastewater_heat_accessible_fraction'];electric=sourceHeat/(a['heat_pump_COP']-1);delivered=sourceHeat+electric
 result['thermal_heat_pump_screen']={'accessible_source_heat_MWh_year':sourceHeat,'electricity_required_MWh_year':electric,'heat_delivered_MWh_year':delivered,'gross_avoided_boiler_fuel_value_usd_year':delivered*3.412141633*usefulHeatUSD,'electricity_expense_usd_year':electric*a['electricity_avoided_proxy_USD_MWh'],'operating_balance_before_capex_OM_usd_year':delivered*3.412141633*usefulHeatUSD-electric*a['electricity_avoided_proxy_USD_MWh'],'limits':'Separate thermal source, not sludge methane. Accessibility, temperature draw and COP are assumptions. Preserve process/receiving-water temperatures and prevent overlap with CHP heat sinks. No cooling benefit credited.'}
 result['efficiency_screen']={'historic_sector_electric_MWh_year':30.2e6,'saving_fraction':.06,'electricity_saving_MWh_year':30.2e6*.06,'gross_avoided_electricity_proxy_usd_year':30.2e6*.06*a['electricity_avoided_proxy_USD_MWh'],'limits':'DOE historic baseline with illustrative 6% improvement; do not add with CHP if the same baseline purchase is already displaced.'}
 # Context-only inventory proxies, never treated as qualified recoverable output.
 result['other_resources']=json.loads(json.dumps(inputs['other_resources']))
 result['other_resources'].append({'resource':'Raw biogas CO2','content_proxy_t_year_at_50pct':a['historic_wastewater_methane_potential_t_year']*.5*(.4/.6)*(44.01/16.043),'qualified_recovery_t_year':None,'value_usd_year':None,'basis':'Illustrative 60/40 methane/CO2 volume mix. Purification, local demand and carbon accounting unestablished; carbon is already in sludge.'})
 result['energy_literature_sensitivity']={'NREL_based_model_full_gross_electric_TWh':result['scenarios'][1]['CHP']['gross_electric_MWh_year']/1e6/.5,'federal_2014_roadmap_full_electric_TWh':5.6,'roadmap_50pct_share_TWh_before_harmonization':2.8,'limits':'Different scope/method/year; not a confidence interval. Do not treat the higher modeled output as confirmed current capacity.'};result['gaps']=inputs['gaps'];result['accounting_rules']=inputs['accounting_rules'];return result

def validate(r):
 assert len(r['scenarios'])==3
 for s in r['scenarios']:
  c=s['CHP'];assert c['net_electric_MWh_year']<=c['gross_electric_MWh_year'];assert c['heat_available_for_external_offset_MWh_year']<=c['recoverable_heat_MWh_year']
  assert (c['gross_electric_MWh_year']+c['recoverable_heat_MWh_year'])*3.6<=c['fuel_energy_GJ_year']+1e-5
  assert math.isclose(s['HTL']['assumed_diesel_gal_year']+s['HTL']['other_finished_fuel_gal_year'],s['HTL']['assumed_finished_fuels_gal_year'])
  st=s['struvite_illustration'];assert math.isclose(st['N_contained_t_year']+st['standalone_ammonium_N_after_struvite_t_year'],s['nutrients']['ammonium_N_t_year'])
  assert s['RNG']['net_margin_usd'] is None and s['HTL']['net_margin_usd'] is None
 h=r['thermal_heat_pump_screen'];assert math.isclose(h['heat_delivered_MWh_year'],h['electricity_required_MWh_year']+h['accessible_source_heat_MWh_year'])
 def finite(v):
  if isinstance(v,float):assert math.isfinite(v)
  elif isinstance(v,dict):
   for x in v.values():finite(x)
  elif isinstance(v,list):
   for x in v:finite(x)
 finite(r)

if __name__=='__main__':
 inputs=json.loads((ROOT/'inputs.json').read_text());results=calculate(inputs);validate(results);(ROOT/'results.json').write_text(json.dumps(results,indent=2,allow_nan=False)+'\n');print('PASS: nutrient allocation, energy conservation, fuel split, finite numbers and unknown margins retained.');print(json.dumps(results['scenarios'][1],indent=2));print(json.dumps(results['thermal_heat_pump_screen'],indent=2))
