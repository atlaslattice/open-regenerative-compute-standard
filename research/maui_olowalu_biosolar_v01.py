#!/usr/bin/env python3
"""Olowalu–Launiupoko Botanical Village / Lahaina BioSolar microgrid v0.1.
PROPOSED / SIMULATED, NOT SURVEYED, PERMITTED, ENGINEERED OR FINANCED.
Stdlib only. Run: python maui_olowalu_biosolar_v01.py --pretty
Change assumptions: --homes 500 --desal-mgd 1 --pv-mw 8 --biosolar-gain 0.015
"""
import argparse
import json

ACRE_SQFT = 43560
GAL_TO_M3 = 0.003785411784
HOURS_YEAR = 8760
DAYS = 365
SEAWATER_SALT_KG_M3 = 35.0
ALLOCATION = {
    "native_dry_forest_stream_cultural_coastal_protection": 240,
    "regenerative_agroforestry_and_farm_land": 150,
    "resident_homes_commons": 80,
    "public_botanical_gardens_contained_rainforest": 60,
    "screened_water_energy_zld_minerals": 28,
    "community_nursery_food_trucks_training_workshops": 20,
    "roads_emergency_access_shared_corridors": 35,
}
assert sum(ALLOCATION.values()) == 613

def model(homes=500, annual_pv_yield_kwh_kw=1600, rooftop_kw=7,
          biosolar_gain=0.015, pv_mw=8.0, islanded_critical_mw=0.4,
          outage_hours=72, battery_delivery_fraction=0.80,
          desal_mgd=1.0, ro_recovery=0.45, ro_kwh_m3=3.5,
          zld_kwh_m3_concentrate=10.0, plant_capacity_factor=0.85,
          electricity_usd_kwh=0.25,
          conventional_home_usd=450000, hybrid_home_usd=360000,
          printed_home_usd=300000):
    if homes <= 0 or pv_mw < 0 or desal_mgd < 0 or not (0 < ro_recovery < 1):
        raise ValueError("Homes >0, PV/desal >=0, 0<RO recovery<1")
    if not (0 < battery_delivery_fraction <= 1 and 0 <= plant_capacity_factor <= 1):
        raise ValueError("Check delivery fraction and plant capacity factor")
    if not (0 <= biosolar_gain <= 0.10):
        raise ValueError("BioSolar gain is fractional 0 through 0.10")
    if any(x < 0 for x in [ro_kwh_m3,zld_kwh_m3_concentrate,rooftop_kw,
                           annual_pv_yield_kwh_kw,islanded_critical_mw,
                           outage_hours,electricity_usd_kwh]):
        raise ValueError("Inputs must be nonnegative")
    feed_mgd = desal_mgd / ro_recovery
    concentrate_mgd = feed_mgd - desal_mgd
    product_m3_d = desal_mgd * 1e6 * GAL_TO_M3
    concentrate_m3_d = concentrate_mgd * 1e6 * GAL_TO_M3
    feed_m3_d = feed_mgd * 1e6 * GAL_TO_M3
    # Simplified 35 kg/m3 incoming salt inventory; product residual salt, additives and solids moisture excluded.
    salt_t_d = feed_m3_d * SEAWATER_SALT_KG_M3 / 1000
    duty_days = DAYS * plant_capacity_factor
    ro_gwh_y = product_m3_d * ro_kwh_m3 * duty_days / 1e6
    zld_gwh_y = concentrate_m3_d * zld_kwh_m3_concentrate * duty_days / 1e6
    site_pv_gwh_y = pv_mw * 1000 * annual_pv_yield_kwh_kw / 1e6
    site_biosolar_extra_gwh_y = site_pv_gwh_y * biosolar_gain
    town_rooftop_gwh_y = homes * rooftop_kw * annual_pv_yield_kwh_kw / 1e6
    town_biosolar_extra_gwh_y = town_rooftop_gwh_y * biosolar_gain
    critical_battery_nameplate_mwh = islanded_critical_mw * outage_hours / battery_delivery_fraction
    return {
       "status":"PROPOSED SIMULATION, ZERO REALIZED CREDIT",
       "land": {
          "historic_olowalu_town_footprint_acres_NOT_a_current_entitlement":613,
          "historic_olowalu_town_footprint_sqft":613*ACRE_SQFT,
          "separate_state_owned_restored_TDS_acres_NOT_INCLUDED":19.4,
          "allocation":[{"use":k,"acres":v,"sqft":v*ACRE_SQFT,
                         "share_percent":round(100*v/613,2)}
                        for k,v in ALLOCATION.items()],
          "unallocated_acres":613-sum(ALLOCATION.values()),
          "garden_rainforest_note":"Contain 5–10 acre irrigated attraction within 60 garden acres, contingent on nonpotable sustainable supply and invasive-species screening"
       },
       "homes": {
          "modeled_units":homes,
          "gross_density_on_80_residential_acres_du_acre":round(homes/80,2),
          "conventional_housing_only_capex_usd":homes*conventional_home_usd,
          "hybrid_housing_only_capex_usd":homes*hybrid_home_usd,
          "printed_housing_only_capex_usd":homes*printed_home_usd,
          "hypothetical_hybrid_savings_usd":homes*(conventional_home_usd-hybrid_home_usd),
          "hypothetical_print_savings_usd":homes*(conventional_home_usd-printed_home_usd),
          "cost_note":"No land, uncertain infrastructure, common gardens, permitting, utilities; print-material qualification and bids required"
       },
       "microgrid": {
          "site_pv_MWp_DC":pv_mw,
          "site_baseline_pv_GWh_per_year":round(site_pv_gwh_y,3),
          "site_biosolar_additional_GWh_per_year_SCENARIO":round(site_biosolar_extra_gwh_y,3),
          "site_biosolar_avoided_energy_value_usd_per_year_SCENARIO":
             round(site_biosolar_extra_gwh_y*1e6*electricity_usd_kwh),
          "home_rooftops_total_MWp_DC":round(homes*rooftop_kw/1000,3),
          "home_rooftops_baseline_GWh_per_year":round(town_rooftop_gwh_y,3),
          "home_rooftops_biosolar_increment_GWh_per_year":round(town_biosolar_extra_gwh_y,3),
          "outage_design_hours":outage_hours,
          "critical_load_MW":islanded_critical_mw,
          "battery_nameplate_MWh_72h_no_sun_assumption":round(critical_battery_nameplate_mwh,2),
          "caution":"Annual PV >= load does not establish 72-hour autonomy; Hawaiian Electric Rule 30 Maui hybrid >1MW peak restriction requires alternate approval"
       },
       "desal_ZLD": {
          "finished_RO_nameplate_MGD":desal_mgd,
          "intake_at_nameplate_MGD":round(feed_mgd,4),
          "RO_concentrate_at_nameplate_MGD":round(concentrate_mgd,4),
          "feed_seawater_m3_per_day_at_nameplate":round(feed_m3_d),
          "theoretical_dissolved_salt_feed_tonnes_per_day_at_nameplate":round(salt_t_d,1),
          "theoretical_dissolved_salt_feed_tonnes_per_operating_year":round(salt_t_d*duty_days),
          "RO_energy_GWh_per_year_SCENARIO":round(ro_gwh_y,2),
          "ZLD_concentrate_processing_energy_GWh_per_year_SCENARIO":round(zld_gwh_y,2),
          "RO_plus_ZLD_energy_GWh_per_year_SCENARIO":round(ro_gwh_y+zld_gwh_y,2),
          "RO_plus_ZLD_annual_energy_cost_usd_scenario":
             round((ro_gwh_y+zld_gwh_y)*1e6*electricity_usd_kwh),
          "note":"ZLD condensate additional recovery and sales not counted; mineral product purity, residual solids, on-site demand and firm power not modeled. No routine liquid brine outfall is proposed.",
          "deuterium":"research inventory in water molecules; not modeled as salt-brine revenue"
       }
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--homes",type=int,default=500)
    p.add_argument("--desal-mgd",type=float,default=1.0)
    p.add_argument("--pv-mw",type=float,default=8.0)
    p.add_argument("--biosolar-gain",type=float,default=0.015,
                   help="Fraction, e.g. .015=1.5 percent")
    p.add_argument("--outage-hours",type=float,default=72.0)
    p.add_argument("--pretty",action="store_true")
    a=p.parse_args()
    result=model(homes=a.homes,desal_mgd=a.desal_mgd,pv_mw=a.pv_mw,
                 biosolar_gain=a.biosolar_gain,outage_hours=a.outage_hours)
    print(json.dumps(result,indent=2 if a.pretty else None,ensure_ascii=False))
if __name__=="__main__":
    main()
