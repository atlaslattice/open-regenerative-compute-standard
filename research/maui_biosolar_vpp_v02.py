#!/usr/bin/env python3
"""ORCS Maui resident-first BioSolar and virtual-power-plant simulator v0.2.
SCENARIO ONLY, not certified dispatch, HECO tariff quote, or proven ROI.
Reference: Maui v0.1 land + power and Sunrun/Tesla 745 MW California VPP.
Run: python maui_biosolar_vpp_v02.py --pretty
All costs and performance inputs are illustrative; no guaranteed incentive.
"""
import argparse
import json

def scenario(
    homes=500, participation=0.60, solar_kw_home=7, solar_yield_kwh_kw_y=1600,
    biosolar_gain=0.015, battery_usable_kwh_home=20,
    backup_reserve_frac=0.50, committed_kw_home=3,
    dispatch_hours=2, household_use_during_dispatch_kwh=2,
    delivery_efficiency=0.90, lmi_share_of_participants=0.50,
    upfront_incentive_usd_kw=400, lmi_additional_usd_kw=400,
    essential_kwh_home_day=5, campus_pv_mw=8,
    campus_islanded_critical_mw=0.4, emergency_outage_hours=72,
    campus_battery_delivery_fraction=0.8
):
    fractions=[participation,biosolar_gain,backup_reserve_frac,delivery_efficiency,
               lmi_share_of_participants,campus_battery_delivery_fraction]
    if homes < 0 or any(not 0 <= v <= 1 for v in fractions) or delivery_efficiency==0 or campus_battery_delivery_fraction==0:
        raise ValueError("Invalid household count, fraction, or efficiency")
    other=[solar_kw_home,solar_yield_kwh_kw_y,battery_usable_kwh_home,
           committed_kw_home,dispatch_hours,household_use_during_dispatch_kwh,
           upfront_incentive_usd_kw,lmi_additional_usd_kw,essential_kwh_home_day,
           campus_pv_mw,campus_islanded_critical_mw,emergency_outage_hours]
    if any(v<0 for v in other):
        raise ValueError("Inputs must be nonnegative")
    members=round(homes*participation)
    gross_per_home=battery_usable_kwh_home*(1-backup_reserve_frac)
    avail_kwh_before_eff=max(0,gross_per_home-household_use_during_dispatch_kwh)
    dispatch_capacity_by_energy_kw=avail_kwh_before_eff*delivery_efficiency/dispatch_hours if dispatch_hours>0 else 0
    actual_kw_home=min(committed_kw_home,dispatch_capacity_by_energy_kw)
    actual_mw=members*actual_kw_home/1000
    energy_mwh=actual_mw*dispatch_hours
    nameplate_mwh=homes*battery_usable_kwh_home/1000
    home_pv_gwh=homes*solar_kw_home*solar_yield_kwh_kw_y/1e6
    site_pv_gwh=campus_pv_mw*1000*solar_yield_kwh_kw_y/1e6
    incentive_capacity_kw=members*committed_kw_home
    # Forecast payout is hypothetical and only for systems enrolled, accepted and delivering contract requirements.
    simple_upfront=incentive_capacity_kw*upfront_incentive_usd_kw
    lmi_additional=incentive_capacity_kw*lmi_share_of_participants*lmi_additional_usd_kw
    essential_reserve_kwh=battery_usable_kwh_home*backup_reserve_frac
    essential_days=essential_reserve_kwh/essential_kwh_home_day if essential_kwh_home_day>0 else None
    campus_battery_mwh=(campus_islanded_critical_mw*emergency_outage_hours/
                          campus_battery_delivery_fraction)
    return {
      "status":"PROPOSED/SIMULATED: NOT METERED, NOT PERMITTED, NOT PROMISED INCENTIVES",
      "assumptions":{
        "homes":homes,"participation_rate":participation,
        "committed_kw_home":committed_kw_home,
        "household_battery_usable_kwh":battery_usable_kwh_home,
        "resident_backup_reserve_fraction":backup_reserve_frac,
        "home_load_kwh_during_dispatch":household_use_during_dispatch_kwh,
        "delivery_efficiency":delivery_efficiency,
        "dispatch_duration_hours":dispatch_hours,
        "lmi_fraction_of_participants":lmi_share_of_participants,
        "biosolar_pv_uplift_assumption":biosolar_gain
      },
      "aggregate":{
        "enrolled_homes_hypothetical":members,
        "total_household_batteries_usable_MWh":round(nameplate_mwh,3),
        "resident_reserve_kwh_per_battery":round(essential_reserve_kwh,2),
        "max_feasible_dispatched_kW_per_home_in_this_idealized_energy_check":round(actual_kw_home,3),
        "max_idealized_export_peak_MW":round(actual_mw,3),
        "max_idealized_export_MWh_for_event":round(energy_mwh,3),
        "zero_reliability_derating_used":True,
        "backup_days_at_essential_load_without_sun_idealized":round(essential_days,2) if essential_days is not None else None,
        "LMI_or_general_cash_incentive_NOT_GUARANTEED_USD":round(simple_upfront),
        "conditional_LMI_adder_NOT_GUARANTEED_USD":round(lmi_additional),
        "total_conditional_upfront_incentives_NOT_GUARANTEED_USD":round(simple_upfront+lmi_additional),
        "credit_revenue_usd":None
      },
      "solar":{
        "rooftop_base_GWh_yr":round(home_pv_gwh,3),
        "rooftop_BioSolar_increment_GWh_yr":round(home_pv_gwh*biosolar_gain,3),
        "campus_base_GWh_yr":round(site_pv_gwh,3),
        "campus_BioSolar_increment_GWh_yr":round(site_pv_gwh*biosolar_gain,3),
        "BioSolar_uplift_is_test_hypothesis":True,
        "solar_has_no_72h_firm_supply_guarantee":True
      },
      "emergency":{
        "campus_critical_load_MW":campus_islanded_critical_mw,
        "campus_72h_battery_MWh_rating_reference":round(campus_battery_mwh,3),
        "resilience_priority":"emergency reserve > household demand > ecological life-support > permitted grid export",
        "warning":"VPP dispatch is NOT a physical neighborhood microgrid or blackout guarantee."
      },
      "regulatory":{
        "hawaiian_electric_program":"BYOD Plus Rule 33; any forecast incentives depend on enrollment and verification",
        "LMI_incentive_multiplier":"additional $400/kW only if eligible; illustrative share",
        "hybrid_microgrid_note":"Maui >1MW peak hybrid islanding requires approval outside Phase 1 Rule 30",
        "california_reference":"2026-10-06 745MW PEAK power, not proven MWh; not a Maui performance forecast."
      }
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--homes",type=int,default=500)
    p.add_argument("--participation",type=float,default=.60)
    p.add_argument("--battery-kwh",type=float,default=20)
    p.add_argument("--reserve",type=float,default=.50)
    p.add_argument("--committed-kw",type=float,default=3)
    p.add_argument("--biosolar-gain",type=float,default=.015)
    p.add_argument("--lmi-share",type=float,default=.50)
    p.add_argument("--pretty",action="store_true")
    a=p.parse_args()
    result=scenario(homes=a.homes,participation=a.participation,
                    battery_usable_kwh_home=a.battery_kwh,
                    backup_reserve_frac=a.reserve,
                    committed_kw_home=a.committed_kw,
                    biosolar_gain=a.biosolar_gain,
                    lmi_share_of_participants=a.lmi_share)
    print(json.dumps(result,indent=2 if a.pretty else None,ensure_ascii=False))
if __name__=="__main__":
    main()
