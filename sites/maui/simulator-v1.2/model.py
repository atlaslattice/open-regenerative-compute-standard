#!/usr/bin/env python3
"""Atlas Lattice Maui v1.2 research simulator: deterministic, entirely advisory.

All default economics, yields, process sizing, load shapes and site compatibility are
PROPOSED/SIMULATED, NOT measured Maui plant performance. No physical control output.
"""
from __future__ import annotations
import argparse, copy, datetime, hashlib, json, math, pathlib, statistics
from typing import Any

ROOT=pathlib.Path(__file__).resolve().parent
TONNE_PER_SHORT_TON=0.90718474
M3_PER_MG=3785.411784
KWH_PER_M3_METHANE=9.94


def read_inputs():
    return (json.loads((ROOT/'data'/'assumptions.json').read_text()),
            json.loads((ROOT/'data'/'scenarios.json').read_text()))


def resolve_scenario(name, scenarios):
    if name not in scenarios: raise ValueError('Unknown scenario: '+name)
    raw=copy.deepcopy(scenarios[name]); parent=raw.pop('extends',None)
    if parent:
        inherited=resolve_scenario(parent,scenarios)
        inherited.update(raw); return inherited
    return raw


def validate_scenario(s):
    """Reject impossible allocations for CLI, HTTP and imported scenarios alike."""
    for key in ('food_capture','green_capture','ad_share','htl_share','reuse_target_fraction'):
        value=s[key]
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(key+' must be finite and between 0 and 1')
    for key in ('solar_mw','desal_mgd','it_mw','battery_mwh','farm_short_tpy','biosolids_wet_short_tpy'):
        value=s.get(key,0)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value < 0:
            raise ValueError(key+' must be finite and nonnegative')
    if s['ad_share']+s['htl_share'] > 1+1e-9:
        raise ValueError('AD + HTL food share exceeds 100%')


def compute_year(year, scenario, p, s, weather_factor=1.0):
    validate_scenario(scenario)
    # 2026 pilot-year starts with small use. Full deployment in 2029; no claim of approvals.
    scale=0 if s=='status_quo' else min(1.0,max(0.0,(year-2026)/3))
    capture=max(0,min(1,scenario.get('collection_factor',1)))
    food_short=p['historical_disposed_food_short_tpy']*scenario['food_capture']*scale*capture
    green_short=p['historical_disposed_green_short_tpy']*scenario['green_capture']*scale*capture
    farm_short=scenario.get('farm_short_tpy',0)*scale*capture
    rescued_food_short=food_short*0.10
    convertible_food=food_short-rescued_food_short+farm_short
    ad_share=scenario['ad_share']; htl_share=scenario['htl_share']
    if ad_share+htl_share>1+1e-9: raise ValueError('AD + HTL food share exceeds 100%')
    ad_feed=convertible_food*ad_share
    htl_food_feed=convertible_food*htl_share
    compost_food=convertible_food-ad_feed-htl_food_feed
    biosolids_wet_short=scenario.get('biosolids_wet_short_tpy',0)*scale
    htl_wet_short=htl_food_feed+biosolids_wet_short
    conversion=scenario.get('conversion_yield_factor',1.0)
    methane_m3=ad_feed*p['methane_m3_per_short_ton_food']*conversion
    ad_electric_mwh=methane_m3*KWH_PER_M3_METHANE*p['methane_electric_conversion_efficiency']/1000
    htl_dry_tonnes=(htl_food_feed*p['food_dry_fraction']+biosolids_wet_short*p['sludge_dry_fraction'])*TONNE_PER_SHORT_TON
    biocrude_tonnes=htl_dry_tonnes*p['htl_oil_yield_per_dry_tonne']*conversion
    # Potential usable fuel is NOT certified production or sold fuel.
    upgraded_fuel_mwh_potential=biocrude_tonnes*1000*p['biocrude_hhv_mj_per_kg']/3600*p['htl_upgraded_energy_fraction']
    green_compost_short=green_short*.72
    other_compost_short=compost_food*.38
    total_compost_short=green_compost_short+other_compost_short
    target_fraction=scenario['reuse_target_fraction']
    eligible_mgd=min(p['freshwater_reuse_demand_mgd']*scenario.get('water_demand_multiplier',1),
                     p['maui_wwtp_reference_mgd']*target_fraction)*scenario.get('reuse_availability_fraction',1)*scale
    reuse_mgd=max(p['baseline_reuse_mgd_assumed'],eligible_mgd)
    extra_reuse_mgd=max(0,reuse_mgd-p['baseline_reuse_mgd_assumed'])
    avoided_potable_mgd=extra_reuse_mgd*p['potable_substitution_factor']
    desal_mgd=scenario['desal_mgd']*scale
    solar_mw=scenario['solar_mw']*scale
    solar_factor=scenario.get('pv_factor',1)*weather_factor
    solar_mwh=solar_mw*8760*p['pv_solar_capacity_factor']*solar_factor
    wwtp_kwh_m3=(p['mbropt_wwtp_kwh_per_m3'] if scenario['mbropt'] and scale>=1 else p['baseline_wwtp_kwh_per_m3'])
    wwtp_mwh=p['maui_wwtp_reference_mgd']*M3_PER_MG*365*wwtp_kwh_m3/1000
    desal_mwh=desal_mgd*M3_PER_MG*365*p['desal_kwh_per_m3']/1000
    extra_reuse_mwh=extra_reuse_mgd*M3_PER_MG*365*p['reclaimed_water_kwh_per_m3']/1000
    hauling_mwh=(food_short+green_short+farm_short)*p['microhaul_kwh_per_short_ton']/1000
    process_factor=scenario.get('process_energy_multiplier',1)
    processing_mwh=(ad_feed*p['ad_electric_kwh_per_wet_short_ton'] +
                    htl_wet_short*p['htl_electric_kwh_per_wet_short_ton'] +
                    green_short*p['green_processing_kwh_per_short_ton'])/1000*process_factor
    it_mw=scenario.get('it_mw',0)*scale
    compute_mwh=it_mw*p['data_center_pue']*8760
    # HTL thermal heat requirement is separate from electricity; preheating assumptions are not verified.
    htl_heat_need_mwh=htl_wet_short*p['htl_thermal_kwh_per_wet_short_ton']/1000
    ad_heat_potential_mwh=methane_m3*KWH_PER_M3_METHANE*p['ad_chp_recoverable_heat_fraction']/1000
    available_heat_mwh=(max(0,htl_heat_need_mwh)*p['htl_recoverable_heat_fraction']+
                        compute_mwh*p['data_center_heat_recovery_fraction']+ad_heat_potential_mwh)
    heat_need_mwh=p['annual_thermal_heat_demand_mwh']*scale+htl_heat_need_mwh
    thermal_use_mwh=min(heat_need_mwh, available_heat_mwh)
    heat_purchase_mwh=max(0,heat_need_mwh-thermal_use_mwh)
    gross_load_mwh=wwtp_mwh+desal_mwh+extra_reuse_mwh+hauling_mwh+processing_mwh+compute_mwh
    gross_generation_mwh=solar_mwh+ad_electric_mwh
    net_generation_mwh=gross_generation_mwh-gross_load_mwh
    # Annual aggregation isn't physical hourly export. Dispatch tab calculates an illustrative week.
    reduced_disposal_short=food_short+green_short
    raw_water_delta_mg=avoided_potable_mgd*365
    power_price=p['grid_purchase_dollars_per_kwh']*scenario.get('energy_price_multiplier',1)
    fuel_price=p['imported_fuel_value_dollars_per_mwh']*scenario.get('fuel_price_multiplier',1)
    products_price=scenario.get('product_price_multiplier',1)
    # Financial model: no speculative grants or social multipliers, and no guaranteed sale of biocrude.
    savings_disposal=reduced_disposal_short*p['landfill_cost_avoided_dollars_per_short_ton']
    sales_compost=total_compost_short*p['soil_product_value_dollars_per_short_ton']*products_price
    water_value=raw_water_delta_mg*1000*p['reclaimed_water_value_dollars_per_kgal']
    # Potential fuel value is shown but excluded from audited cash flow until offtake is proven.
    conditional_fuel_value=upgraded_fuel_mwh_potential*fuel_price
    # Export remuneration is excluded: annual balance cannot prove exportable hourly energy.
    potential_export_value=max(0,net_generation_mwh)*1000*p['grid_export_dollars_per_kwh']
    purchased_grid_cost=max(0,-net_generation_mwh)*1000*power_price
    heat_value=thermal_use_mwh*1000*p['heat_purchase_dollars_per_kwh_thermal']
    heat_purchase_cost=heat_purchase_mwh*1000*p['heat_purchase_dollars_per_kwh_thermal']
    collection_opex=(food_short+green_short+farm_short)*p['new_collection_opex_dollars_per_short_ton']
    op_cost=(p['annual_base_opex_dollars']*scale+collection_opex+
             p['restoration_annual_opex_dollars']*scale+purchased_grid_cost+heat_purchase_cost)
    # Existing wastewater power included as grid demand; capex and revenue are synthetic.
    # Hypothetical compost sale and recovered heat valuations are disclosed but excluded until verified.
    conservative_cashflow=savings_disposal+water_value-op_cost
    return {
      'year':year,'deployment_fraction':round(scale,3),'food_short_t':round(food_short,2),
      'green_short_t':round(green_short,2),'farm_short_t':round(farm_short,2),
      'rescued_food_short_t':round(rescued_food_short,2),'ad_feed_short_t':round(ad_feed,2),
      'htl_food_short_t':round(htl_food_feed,2),'biosolids_htl_wet_short_t':round(biosolids_wet_short,2),
      'food_compost_short_t':round(compost_food,2),'food_resource_mass_residual_short_t':0,
      'green_to_compost_short_t':round(green_short,2),'compost_saleable_short_t_potential':round(total_compost_short,2),
      'methane_m3_potential':round(methane_m3),'biocrude_tonnes_potential':round(biocrude_tonnes,2),
      'certification':'NOT CERTIFIED / NO OFFTAKE', 'upgraded_fuel_mwh_potential':round(upgraded_fuel_mwh_potential,2),
      'reuse_total_mgd':round(reuse_mgd,3),'reuse_incremental_mgd':round(extra_reuse_mgd,3),
      'potable_substitution_mgd_potential':round(avoided_potable_mgd,3),'desal_mgd':round(desal_mgd,3),
      'solar_mwh':round(solar_mwh,2),'ad_electric_mwh':round(ad_electric_mwh,2),
      'wwtp_electric_mwh':round(wwtp_mwh,2),'desal_electric_mwh':round(desal_mwh,2),
      'reclaimed_water_electric_mwh':round(extra_reuse_mwh,2),'haul_electric_mwh':round(hauling_mwh,2),
      'processing_electric_mwh':round(processing_mwh,2),'compute_electric_mwh':round(compute_mwh,2),
      'electric_load_mwh':round(gross_load_mwh,2),'electric_generation_mwh':round(gross_generation_mwh,2),
      'annual_net_generation_mwh_proxy':round(net_generation_mwh,2),
      'heat_useful_mwh_th_potential':round(thermal_use_mwh,2),
      'ad_chp_heat_potential_mwh_th':round(ad_heat_potential_mwh,2),
      'thermal_purchased_mwh_th':round(heat_purchase_mwh,2),
      'landfill_diversion_short_t':round(reduced_disposal_short,2),
      'avoided_disposal_dollars':round(savings_disposal),
      'water_value_dollars':round(water_value),
      'conditional_fuel_value_excluded_dollars':round(conditional_fuel_value),
      'annual_export_value_excluded_dollars':round(potential_export_value),
      'conditional_compost_sales_excluded_dollars':round(sales_compost),
      'conditional_thermal_value_excluded_dollars':round(heat_value),
      'opex_dollars':round(op_cost),'cashflow_before_capex_dollars':round(conservative_cashflow),
      'ecology_status':'UNVERIFIED: requires surveys and control sites',
      'carbon_status':'UNVERIFIED: no lifecycle carbon accounting',
      'equity_status':'UNVERIFIED: household distribution not yet modeled',
      'status':'SIMULATED'
    }


def capex(s,p,config):
    if s=='status_quo': return 0
    pv=config['solar_mw']*1000*p['pv_capex_dollars_per_kw']
    water=p['water_capex_dollars']*min(1,max(.25,config['reuse_target_fraction']/0.75))
    digestion=p['digestion_capex_dollars'] if config['ad_share'] else 0
    htl=p['htl_capex_dollars'] if config['htl_share'] else 0
    data=config.get('it_mw',0)*p['data_center_capex_dollars_per_it_mw']
    battery=config['battery_mwh']*1000*280  # synthetic USD/kWh installed
    return (pv+water+digestion+htl+data+battery+p['microhaul_capex_dollars']+
            p['restoration_capex_dollars'])*config.get('capex_multiplier',1)


def annual_run(name='hybrid_compute', p=None, configs=None, overrides=None):
    if p is None or configs is None: p,configs=read_inputs()
    config=resolve_scenario(name,configs)
    if overrides:config.update(overrides)
    if config['ad_share']+config['htl_share']>1.000001:raise ValueError('AD+HTL shares exceed 1')
    validate_scenario(config)
    cost=capex(name,p,config)
    rows=[]; npv=-cost; replacement_total=0
    for y in range(2026,2056): # 30 cash-flow calendar years 2026..2055 inclusive
        event=(config.get('hazard')=='storm' and y in (2031,2045)) or (config.get('hazard')=='wildfire' and y in (2032,2046))
        yearly_config=dict(config)
        if config.get('hazard')=='storm' and not event:
            yearly_config['collection_factor']=1.0
        if config.get('hazard')=='wildfire' and not event:
            yearly_config['collection_factor']=1.0;yearly_config['pv_factor']=1.0
        weather_factor=(1.0-config.get('pv_damage_fraction',.30)*.45) if event else 1.0
        r=compute_year(y,yearly_config,p,name,weather_factor=weather_factor)
        baseline=compute_year(y,resolve_scenario('status_quo',configs),p,'status_quo')
        r['incremental_cashflow_before_capex_dollars']=round(r['cashflow_before_capex_dollars']-baseline['cashflow_before_capex_dollars'])
        r['illustrative_hazard_event']=bool(event)
        age=y-2026
        replace=0
        if age in p['asset_replacement_schedule']['battery_years']:
            replace+=config['battery_mwh']*1000*180 # synthetic battery replacement cost
        if age in p['asset_replacement_schedule']['membrane_years']:
            replace+=p['water_capex_dollars']*.065*config.get('capex_multiplier',1)
        if age in p['asset_replacement_schedule']['compute_years']:
            replace+=config.get('it_mw',0)*p['data_center_capex_dollars_per_it_mw']*.30
        # Two hypothetical weather shock events in 30-year storm/wildfire paths.
        event_repair_cost=(5000000 if config.get('hazard')=='storm' else 2400000) if event else 0
        r['illustrative_event_repair_cost_dollars']=event_repair_cost
        yearly_cash=r['incremental_cashflow_before_capex_dollars']-replace-event_repair_cost
        npv+=yearly_cash/(1+p['discount_rate'])**age
        r['replacement_capex_dollars']=round(replace)
        r['cashflow_after_replacement_dollars']=round(yearly_cash)
        rows.append(r);replacement_total+=replace
    final=rows[-1]
    return {'scenario':name,'description':config.get('description',''),
        'status':'SIMULATED / PROPOSED (no actual credit)',
        'year_count':len(rows),'years':'2026–2055','initial_capex_dollars':round(cost),
        'replacements_nominal_dollars':round(replacement_total),
        'npv_30yr_dollars':round(npv),
        'last_year':final,'annual':rows,
        'financial_limitations':['Annual electrical netting is optimistic; hourly imports not yet priced over 8760 hours',
          'Desal-specific capex, financing, insurance, tax and terminal value are not resolved',
          'Do not use NPV for investment ranking until cost and hourly ledgers are calibrated'],
        'gates':{'health':'UNVERIFIED','ecology':'UNVERIFIED','culture':'UNVERIFIED',
                 'carbon':'UNVERIFIED','finance':'SIMULATED','siting':'NOT SCREENED',
                 'net_positive_everything':'NOT DEMONSTRATED'},
        'boundary_warning':'NOT a complete county baseline, hourly grid forecast, or validated lifecycle model.'}


def dispatch_168h(name='hybrid_compute', weather=None, p=None, configs=None, overrides=None):
    if p is None or configs is None:p,configs=read_inputs()
    scenario=resolve_scenario(name,configs)
    if overrides:scenario.update(overrides)
    validate_scenario(scenario)
    annual=compute_year(2029,scenario,p,name)
    # 2029 full deployment; representative week, not a recorded week.
    battery_capacity=scenario['battery_mwh']; soc=battery_capacity*.6
    max_battery_mw=max(0,battery_capacity/4)
    daily_it_mw=scenario.get('it_mw',0)*p['data_center_pue']
    base_mw=sum(annual[k] for k in ('wwtp_electric_mwh','reclaimed_water_electric_mwh','haul_electric_mwh','processing_electric_mwh'))/8760
    desal_mw=annual['desal_electric_mwh']/8760
    # Annual energy divided by all hours: no fictitious all-week CHP availability uplift.
    dispatch_bio_mw=annual['ad_electric_mwh']/8760
    rows=[]; imports=exports=unserved=critical_unserved=flexible_unserved=0.0; outages=0
    times=(weather or {}).get('time',[])
    rads=(weather or {}).get('shortwave_radiation',[])
    winds=(weather or {}).get('wind_gusts_10m',[])
    rain=(weather or {}).get('precipitation',[])
    hst=datetime.timezone(datetime.timedelta(hours=-10))
    today=datetime.datetime.now(hst).replace(hour=0,minute=0,second=0,microsecond=0)
    if times:
        try:
            first=datetime.datetime.fromisoformat(times[0])
            today=first.replace(tzinfo=hst) if first.tzinfo is None else first.astimezone(hst)
        except (TypeError,ValueError):pass
    forecast_count=0
    for i in range(168):
        h=(today+datetime.timedelta(hours=i)).hour
        if i<len(rads) and isinstance(rads[i],(int,float)) and math.isfinite(rads[i]) and rads[i]>=0:
            pv_mw=scenario['solar_mw']*max(0,min(1.0,rads[i]/1000))*p['pv_derating']
            origin='FORECAST'; forecast_count+=1
        else:
            pv_mw=scenario['solar_mw']*max(0,math.sin(math.pi*(h-6)/12))*0.78*scenario.get('pv_factor',1)
            origin='SYNTHETIC'
        # Assume short-lived storm-induced solar loss and reserve uncertainty.
        storm=scenario.get('hazard')=='storm' and 12<=i<84
        if storm:pv_mw*=max(0,1-scenario.get('pv_damage_fraction',.35))*.45
        critical_mw=base_mw*.7
        optional_mw=base_mw*.3+desal_mw+daily_it_mw
        gross_demand_mw=critical_mw+optional_mw
        outage=scenario.get('grid_outage_hours',0)>0 and 12<=i<12+scenario.get('grid_outage_hours',0)
        if outage:outages+=1
        onsite=pv_mw+dispatch_bio_mw
        used= min(onsite,gross_demand_mw)
        shortage=gross_demand_mw-used
        discharge=min(shortage,max_battery_mw,soc*.92)
        soc_before=soc
        soc-=discharge/.92
        shortage-=discharge
        grid_import=0.0 if outage else shortage
        unserved_this_hour=shortage if outage else 0.0
        # Available power serves critical loads first; flexible deficit is shed.
        critical_deficit=max(0,critical_mw-(onsite+discharge)) if outage else 0.0
        flexible_deficit=max(0,unserved_this_hour-critical_deficit)
        critical_unserved+=critical_deficit; flexible_unserved+=flexible_deficit
        leftover=max(0,onsite-gross_demand_mw)
        charge=min(leftover,max_battery_mw,(battery_capacity-soc)/.92 if soc<battery_capacity else 0)
        soc=min(battery_capacity,soc+charge*.92)
        # Disconnected microgrids cannot export to an unavailable grid.
        export=0.0 if outage else max(0,leftover-charge)
        curtailed=max(0,leftover-charge) if outage else 0.0
        imports+=grid_import;exports+=export;unserved+=unserved_this_hour
        timestamp=times[i] if i<len(times) else (today+datetime.timedelta(hours=i)).isoformat()
        rows.append({'hour':i,'time':timestamp,'solar_mw':round(pv_mw,3),'bio_mw':round(dispatch_bio_mw,3),
          'demand_mw':round(gross_demand_mw,3),'critical_mw':round(critical_mw,3),
          'grid_import_mwh':round(grid_import,3),'grid_export_mwh':round(export,3),
          'unserved_mwh':round(unserved_this_hour,3),'battery_soc_mwh':round(soc,3),
          'critical_unserved_mwh':round(critical_deficit,6),
          'flexible_unserved_mwh':round(flexible_deficit,6),
          'battery_charge_mwh':round(charge,6),'battery_discharge_mwh':round(discharge,6),
          'battery_soc_before_mwh':round(soc_before,6),'curtailed_mwh':round(curtailed,6),
          'grid_outage':outage,'source':origin,
          'precip_mm':rain[i] if i<len(rain) else None,'gust_kmh':winds[i] if i<len(winds) else None})
    return {'scenario':name,'hours':168,'data_origin':('MIXED FORECAST/SYNTHETIC' if forecast_count else 'SYNTHETIC'),
      'forecast_hours':forecast_count,'synthetic_hours':168-forecast_count,
      'time_zone':'Pacific/Honolulu (UTC-10)',
      'critical_unserved_mwh':round(critical_unserved,2),
      'flexible_unserved_mwh':round(flexible_unserved,2),
      'weather_horizon_note':'Current 7-day weather is never extrapolated into 30-year financial projections.',
      'grid_import_mwh':round(imports,2),'grid_export_mwh':round(exports,2),
      'unserved_critical_and_flexible_mwh':round(unserved,2),'outage_hours':outages,'rows':rows,
      'limitations':['Hourly load is a synthetic average, not actual Hawaiian Electric dispatch',
                     'Battery and emergency load-shedding are illustrative, not reliability-certified',
                     'Site thermal matching, grid interconnection and emergency permits unverified']}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scenario',default='hybrid_compute')
    ap.add_argument('--output',default='-')
    ap.add_argument('--mode',choices=['annual','hourly','all'],default='all')
    ap.add_argument('--set', action='append',default=[],help='Override scenario numeric e.g. solar_mw=30; no saved modifications')
    ap.add_argument('--weather-file',help='File exported by live_feeds.py; live weather used for 168-hour run only')
    args=ap.parse_args()
    p,configs=read_inputs();weather=None
    if args.weather_file:
        src=json.loads(pathlib.Path(args.weather_file).read_text())
        from live_feeds import usable_weather
        weather=usable_weather(src)
    overrides={}
    for item in args.set:
        k,sep,v=item.partition('=')
        if not sep or k not in ('solar_mw','food_capture','green_capture','farm_short_tpy','biosolids_wet_short_tpy','ad_share','htl_share','reuse_target_fraction','desal_mgd','it_mw','battery_mwh'):raise ValueError('Not a permitted override: '+item)
        overrides[k]=float(v)
    result={}
    if args.mode in ('annual','all'):result['annual_model']=annual_run(args.scenario,p,configs,overrides)
    if args.mode in ('hourly','all'):result['dispatch']=dispatch_168h(args.scenario,weather,p,configs,overrides)
    s=json.dumps(result,indent=2,allow_nan=False)
    if args.output=='-':print(s)
    else:pathlib.Path(args.output).write_text(s+'\n');print('Wrote',args.output)
if __name__=='__main__':main()
