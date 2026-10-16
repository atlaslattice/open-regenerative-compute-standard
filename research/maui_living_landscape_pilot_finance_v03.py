#!/usr/bin/env python3
"""Maui Living Landscape inference-first pilot v0.3: CAPEX, OPEX, funding and hourly-resilience warnings.
Stdlib only. Input assumptions are NOT vendor bids, grants, tax advice or actual electricity meters.
python maui_living_landscape_pilot_finance_v03.py --pretty
python maui_living_landscape_pilot_finance_v03.py --pv-kw 150 --grant-committed 0 --other-program-income 90000
"""
import argparse,json
DAYS=365
def annualize(rate,years):
    if rate == 0: return 1/years
    return rate/(1-(1+rate)**(-years))
def calculate(pv_kw=100, pv_yield=1600, biosolar_gain=0.015, average_it_kw=10,
              pue=1.2, non_it_critical_kw=3, battery_kwh=450,
              battery_delivery_fraction=0.8, self_consumption=0.70,
              avoided_energy_price=0.28, exported_energy_price=0.08,
              pv_installed_per_kw=3000, battery_installed_per_kwh=500,
              it_network_capex=180000, sensors_ai_capex=160000,
              nursery_restoration_capex=280000, training_public_capex=180000,
              site_civil_capex=350000, contingency_rate=.25,
              annual_staff_cost=180000, annual_facilities_ops=55000,
              annual_replacement_reserve=20000, other_program_income=0,
              grant_committed=0, state_tax_credit_realized=0, federal_tax_credit_realized=0,
              annual_finance_rate=.05, finance_years=20):
    if any(x<0 for x in [pv_kw,pv_yield,average_it_kw,pue,non_it_critical_kw,
         battery_kwh,avoided_energy_price,exported_energy_price,pv_installed_per_kw,
         battery_installed_per_kwh,it_network_capex,sensors_ai_capex,nursery_restoration_capex,
         training_public_capex,site_civil_capex,annual_staff_cost,annual_facilities_ops,
         annual_replacement_reserve,other_program_income,grant_committed,state_tax_credit_realized,
         federal_tax_credit_realized,annual_finance_rate]):
        raise ValueError("All numeric values must be nonnegative")
    if pue < 1 or not(0<=self_consumption<=1) or not(0<=biosolar_gain<=.1) or not(0<=contingency_rate<=1) or not(0<battery_delivery_fraction<=1) or finance_years<=0:
        raise ValueError("Invalid constrained ratio")
    annual_load_kwh=(average_it_kw*pue+non_it_critical_kw)*8760
    solar_kwh=pv_kw*pv_yield*(1+biosolar_gain)
    onsite_solar_kwh=min(solar_kwh*self_consumption,annual_load_kwh)
    exports_kwh=max(0,solar_kwh-onsite_solar_kwh)
    grid_import_kwh=max(0,annual_load_kwh-onsite_solar_kwh)
    solar_avoided_usd=onsite_solar_kwh*avoided_energy_price
    export_usd=exports_kwh*exported_energy_price
    listed_components={
       "biosolar_pv":pv_kw*pv_installed_per_kw,
       "battery_storage":battery_kwh*battery_installed_per_kwh,
       "inference_IT_and_network":it_network_capex,
       "sensor_AI_soil_canopy_water_grid":sensors_ai_capex,
       "native_nursery_restoration":nursery_restoration_capex,
       "training_public_education":training_public_capex,
       "civil_interconnection_firesafety":site_civil_capex
    }
    direct=sum(listed_components.values())
    total=direct*(1+contingency_rate)
    reliable_credits=grant_committed+state_tax_credit_realized+federal_tax_credit_realized
    unfunded_capital=max(0,total-reliable_credits)
    fixed_opex=annual_staff_cost+annual_facilities_ops+annual_replacement_reserve
    grid_bill=grid_import_kwh*avoided_energy_price
    annual_net_opex=fixed_opex+grid_bill-export_usd-other_program_income
    annuity=unfunded_capital*annualize(annual_finance_rate,finance_years)
    critical_kw=average_it_kw*pue+non_it_critical_kw
    return {
      "status":"SCENARIO ONLY: zero signed agreements, zero promised grants, tax credits default to zero",
      "energy":{
        "average_critical_kw":round(critical_kw,3),
        "annual_total_load_MWh":round(annual_load_kwh/1000,2),
        "annual_biosolar_MWh":round(solar_kwh/1000,2),
        "onsite_self_consumed_MWh":round(onsite_solar_kwh/1000,2),
        "grid_import_MWh":round(grid_import_kwh/1000,2),
        "export_MWh":round(exports_kwh/1000,2),
        "onsite_self_consumption_value_usd":round(solar_avoided_usd),
        "export_revenue_usd_scenario":round(export_usd),
        "battery_nameplate_kWh":battery_kwh,
        "sunless_emergency_hours_at_continuous_design_load":
          round(battery_kwh*battery_delivery_fraction/critical_kw,1) if critical_kw>0 else None,
        "warning":"Annual PV energy surplus and average-load storage duration do NOT establish true hourly off-grid autonomy. Protect native stewardship and essential communications."
      },
      "investment":{
        "direct_components_usd":{k:round(v) for k,v in listed_components.items()},
        "pre_contingency_direct_usd":round(direct),
        "contingency_rate":contingency_rate,
        "illustrative_total_capex_usd":round(total),
        "confirmed_grants_usd_user_input":round(grant_committed),
        "confirmed_state_tax_credits_usd_user_input":round(state_tax_credit_realized),
        "confirmed_federal_tax_credits_usd_user_input":round(federal_tax_credit_realized),
        "remaining_financed_principal_usd":round(unfunded_capital),
        "annual_capital_service_usd":round(annuity)
      },
      "annual_operating":{
        "staff_cost_usd":round(annual_staff_cost),
        "other_fixed_operations_usd":round(annual_facilities_ops),
        "battery_IT_replacement_reserve_usd":round(annual_replacement_reserve),
        "grid_energy_import_cost_usd":round(grid_bill),
        "solar_export_value_usd":round(export_usd),
        "program_service_income_USD_scenario":round(other_program_income),
        "net_annual_operating_funding_requirement_usd":round(annual_net_opex),
        "total_annual_funding_requirement_if_financed_usd":round(annual_net_opex+annuity)
      },
      "constraints":{
        "zld_desal_housing_and_land_purchase":"EXCLUDED: different capital projects",
        "actual_utility_demand_charges_export_limits_insurance_and_tax":"NOT CONFIRMED; variable model cannot be used as bid",
        "grant_policy":"Only committed executed grants passed by user may reduce debt; new prospective awards are zero baseline.",
        "credit_policy":"Never assume 25D homeowner credit for 2026; state RETITC and business 48E require taxpayer/date-specific counsel.",
        "economic_value":"Energy savings, grant proceeds, avoided costs and operational program revenue are different accounting categories."
      }
    }
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pv-kw",type=float,default=100)
    p.add_argument("--grant-committed",type=float,default=0)
    p.add_argument("--other-program-income",type=float,default=0)
    p.add_argument("--pretty",action="store_true")
    a=p.parse_args()
    print(json.dumps(calculate(pv_kw=a.pv_kw,grant_committed=a.grant_committed,
              other_program_income=a.other_program_income),ensure_ascii=False,
              indent=2 if a.pretty else None))
if __name__=="__main__":main()
