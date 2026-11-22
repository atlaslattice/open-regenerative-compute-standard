#!/usr/bin/env python3
"""ORCS v4.0 scenario workbook, evidence-grade inputs only. Python 3 standard library.
No plant-level claims, no policy eligibility determination, no field-verified AI savings.
"""
import json
from math import isclose

MW_P2O5 = 141.9445
MW_S = 32.065
MW_H2SO4 = 98.079
MW_GYPSUM = 172.17
SQFT_PER_M2 = 10.7639104167
LONG_TON_IN_METRIC_TON = 2240/2204.62262185

def phosphate_per_tonne_grade46():
    """Metric tonnes S, 100%-acid, pure gypsum theoretical per metric tonne 46% P2O5 fertilizer.
    Pure reaction rock mineralogy bracket: 1.5 to 5/3 moles sulfuric acid per P-mole.
    Excludes process loss, excess acid, recycled acids, mixed-product mismatch.
    """
    p_kmol = 2*460/MW_P2O5
    return {
        "s_t_low": p_kmol*1.5*MW_S/1000,
        "s_t_high": p_kmol*(5/3)*MW_S/1000,
        "acid_t_low": p_kmol*1.5*MW_H2SO4/1000,
        "acid_t_high": p_kmol*(5/3)*MW_H2SO4/1000,
        "gypsum_t_low": p_kmol*1.5*MW_GYPSUM/1000,
        "gypsum_t_high": p_kmol*(5/3)*MW_GYPSUM/1000,
    }

def fertilizer(grade46_tonnes=1_000_000, sulfur_old_usd_long_ton=522,
               sulfur_new_usd_long_ton=705):
    st=phosphate_per_tonne_grade46()
    factor=1/LONG_TON_IN_METRIC_TON
    return {
        "fertilizer_grade46_t_y":grade46_tonnes,
        "sulfur_req_metric_t_y_low":round(st["s_t_low"]*grade46_tonnes),
        "sulfur_req_metric_t_y_high":round(st["s_t_high"]*grade46_tonnes),
        "pure_h2so4_t_y_low":round(st["acid_t_low"]*grade46_tonnes),
        "pure_h2so4_t_y_high":round(st["acid_t_high"]*grade46_tonnes),
        "theoretical_phosphogypsum_t_y_low":round(st["gypsum_t_low"]*grade46_tonnes),
        "theoretical_phosphogypsum_t_y_high":round(st["gypsum_t_high"]*grade46_tonnes),
        "sulfur_price_usd_metric_t_old":round(sulfur_old_usd_long_ton*factor,2),
        "sulfur_price_usd_metric_t_new":round(sulfur_new_usd_long_ton*factor,2),
        "annual_cost_increment_usd_low":round(st["s_t_low"]*grade46_tonnes*(sulfur_new_usd_long_ton-sulfur_old_usd_long_ton)*factor),
        "annual_cost_increment_usd_high":round(st["s_t_high"]*grade46_tonnes*(sulfur_new_usd_long_ton-sulfur_old_usd_long_ton)*factor),
        "sensitivity_only":"If entire grade-46 product is produced from phosphate rock via wet-process acid; not CHS/OCP projected finishing plant imported-acid demand."
    }

def solar(existing_generation_twh=93, eligible_fraction=.25, annual_pv_uplift=.01,
          baseline_kwh_per_sqft_y=261/SQFT_PER_M2, installed_green_usd_sqft=.25,
          years=25, discount=.07, maintenance_usd_sqft_y=0):
    assert 0<=eligible_fraction<=1 and annual_pv_uplift>0
    eligible_gwh=existing_generation_twh*1000*eligible_fraction
    incremental_gwh=eligible_gwh*annual_pv_uplift
    treated_sqft=eligible_gwh*1e6/baseline_kwh_per_sqft_y
    capex=treated_sqft*installed_green_usd_sqft
    crf=discount*(1+discount)**years/((1+discount)**years-1)
    annual_charge=capex*crf+treated_sqft*maintenance_usd_sqft_y
    return {
        "existing_generation_twh_y":existing_generation_twh,
        "eligible_fraction":eligible_fraction,
        "hypothetical_annual_pv_uplift":annual_pv_uplift,
        "additional_generation_gwh_y":round(incremental_gwh,3),
        "treated_sqft_scenario":round(treated_sqft),
        "installed_green_capex_usd":round(capex),
        "annualized_incremental_electricity_cost_usd_mwh":round(annual_charge/(incremental_gwh*1000),2),
        "not_counted":"Green roof additional HVAC, stormwater, building-life and QOL benefits and any roof constraints."
    }

def cold_fleet(sites=75, tonnes_each_year=50000,
               cold_kwh_per_tonne=830/3.6,
               electric_allocation=.10, cooling_allocation=.50,
               captured_cooling_fraction=.65, displaced_chiller_cop=4):
    assert sites>=0 and tonnes_each_year>=0 and 0<=electric_allocation+cooling_allocation<=1
    thermal_gwh=sites*tonnes_each_year*cold_kwh_per_tonne/1e6
    electric_gwh=thermal_gwh*electric_allocation
    avoided_cooling_gwh=thermal_gwh*cooling_allocation*captured_cooling_fraction/displaced_chiller_cop
    return {
        "hypothetical_vaporizing_sites":sites,
        "total_lng_vaporized_mt_y":sites*tonnes_each_year/1e6,
        "theoretical_cold_gwh_thermal_y":round(thermal_gwh,2),
        "generated_gwh_electric_y_scenario":round(electric_gwh,2),
        "avoided_chiller_gwh_electric_y_scenario":round(avoided_cooling_gwh,2),
        "combined_electric_equivalent_gwh_y":round(electric_gwh+avoided_cooling_gwh,2),
        "warning":"No verified domestic LNG annual vaporization site-level throughput. LNG EXPORT cold is paid process energy, not free regas cold. No firm grid capacity proved."
    }

def node(it_kw=100, utilization=.8, pue=1.2, elec_usd_kwh=.10,
         process_baseline_gwh_y=100, process_efficiency_gain=.02):
    local_it_gwh=it_kw*utilization*8760*pue/1e6
    gross_saved=process_baseline_gwh_y*process_efficiency_gain
    return {
        "facility_compute_gwh_y":round(local_it_gwh,5),
        "process_gross_energy_saved_gwh_y":round(gross_saved,5),
        "net_site_energy_saved_gwh_y":round(gross_saved-local_it_gwh,5),
        "net_site_energy_usd_y_at_assumed_tariff":round((gross_saved-local_it_gwh)*1e6*elec_usd_kwh),
        "note":"Assumes process energy baseline uses electricity. Excludes capex, cybersecurity, sensor and other operating expenses; no measured AI causal gain."
    }

def bess_critical(it_mw=1, pue=1.2, hours=4, usable=.80, roundtrip=.85):
    deliver=it_mw*pue*hours
    return {"deliver_mwh":round(deliver,2),
            "nameplate_storage_mwh":round(deliver/usable,2),
            "inverter_mw_min":round(it_mw*pue,2),
            "upstream_charging_mwh_per_full_discharge":round(deliver/roundtrip,2),
            "not_included":"Additional pumps, safety margins, BESS degradation, industrial motor loads, regional transmission."}

def checks():
    s=phosphate_per_tonne_grade46()
    assert .30<s["s_t_low"]<.32 and .34<s["s_t_high"]<.36
    assert isclose(node()["facility_compute_gwh_y"],.84096,abs_tol=1e-7)
    assert isclose(bess_critical()["nameplate_storage_mwh"],6.0)
    assert 860<cold_fleet()["theoretical_cold_gwh_thermal_y"]<870
    assert isclose(solar(existing_generation_twh=389,eligible_fraction=.1,annual_pv_uplift=.111)["additional_generation_gwh_y"],4317.9,abs_tol=.01)

if __name__=="__main__":
    checks()
    print(json.dumps({
        "fertilizer_1mt_grade46":fertilizer(),
        "fertilizer_250kt_grade46":fertilizer(250000),
        "solar_existing_smallscale_25pct_1pct":solar(),
        "solar_existing_smallscale_25pct_11p1pct":solar(annual_pv_uplift=.111),
        "solar_us_all_10pct_11p1pct":solar(existing_generation_twh=389,eligible_fraction=.1,annual_pv_uplift=.111),
        "lng_mid":cold_fleet(),
        "edge_site_100gwh_2pct":node(),
        "critical_it_bess":bess_critical()}, indent=2))
