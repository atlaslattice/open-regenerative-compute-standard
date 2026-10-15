#!/usr/bin/env python3
"""Maui Ocean-first circular reconstruction v0.4 — scenario calculator (stdlib only).

This is *not* a certified design, permitting opinion, actual metered island inventory,
technology performance guarantee, or authorized grant award.
Usage:
    python maui_circular_ocean_microgrid_v04.py
    python maui_circular_ocean_microgrid_v04.py --throughput 5000 --pv-mw 2 --water-mgd 0.1
    python maui_circular_ocean_microgrid_v04.py --capex 40000000 --value-per-ton 400 --zld-sec 5
"""
import argparse
import json

GALLON_M3 = 0.003785411784
DAYS = 365.0
HOURS_YEAR = 8760.0
def annuity(rate, years):
    if years <= 0 or rate < 0:
        raise ValueError("Years > 0 and rate >= 0 required")
    if rate == 0:
        return 1.0 / years
    return rate / (1.0 - (1.0 + rate) ** (-years))

def evaluate(throughput=15000.0, capex=25000000.0, opex_per_ton=175.0,
             net_contribution_per_ton=250.0, recovery=0.60,
             pv_mw=4.0, pv_yield_kwh_kw_y=1600.0,
             businesses=100, annual_business_mwh=40.0, district_other_mwh=300.0,
             water_mgd=0.20, water_sec=3.0, edge_it_kw=50.0, pue=1.2,
             critical_mw=0.4, outage_hours=72.0, battery_delivery_fraction=0.80,
             batt_cost_low=350.0, batt_cost_high=650.0,
             solar_cost_low=2.0, solar_cost_high=4.0,
             reference_desal_mgd=5.0, ro_recovery=0.45,
             zld_sec=10.0, electricity_price=0.20,
             discount=0.07, service_life_years=20):
    numeric = (throughput, capex, opex_per_ton, net_contribution_per_ton,
               pv_mw, pv_yield_kwh_kw_y, annual_business_mwh, district_other_mwh,
               water_mgd, water_sec, edge_it_kw, pue, critical_mw, outage_hours,
               batt_cost_low, batt_cost_high, solar_cost_low, solar_cost_high,
               reference_desal_mgd, zld_sec, electricity_price)
    if any(v < 0 for v in numeric) or throughput <= 0 or pue < 1:
        raise ValueError("All inputs nonnegative, throughput >0, PUE >=1")
    if not (0 <= recovery <= 1 and 0 < ro_recovery < 1 and
            0 < battery_delivery_fraction <= 1):
        raise ValueError("Check process recovery, reverse-osmosis recovery and battery fraction")
    if businesses < 0:
        raise ValueError("businesses must be nonnegative")

    crf = annuity(discount, service_life_years)
    annual_capex = capex * crf
    opex_y = throughput * opex_per_ton
    gross_net_contribution = throughput * net_contribution_per_ton
    net_y = gross_net_contribution - opex_y - annual_capex
    theoretical_break_even = (annual_capex + opex_y) / throughput
    district_energy_mwh = (businesses * annual_business_mwh + district_other_mwh +
                           (water_mgd * 1e6 * GALLON_M3 * water_sec * DAYS / 1000) +
                           (edge_it_kw * pue * HOURS_YEAR / 1000))
    pv_energy_mwh = pv_mw * 1000.0 * pv_yield_kwh_kw_y / 1000
    storage_mwh = critical_mw * outage_hours / battery_delivery_fraction
    ref_prod_m3_d = reference_desal_mgd * 1e6 * GALLON_M3
    ref_conc_m3_d = ref_prod_m3_d * (1 / ro_recovery - 1)
    zld_gwh_y = ref_conc_m3_d * zld_sec * DAYS / 1e6

    return {
        "status": "SCENARIO ONLY — no realized credits, permits or offtake",
        "boundaries": {
            "materials_throughput": "illustrative island collection, U.S. short tons/year",
            "power": "hypothetical Front Street mixed-use area; NOT an hour-by-hour dispatch",
            "desal": "separate 5-MGD open-seawater reference; do not add to Front Street 0.2 MGD",
            "epa_grant": "West Maui proposed collection centre, 1794 short tons/yr: not assumed available as confirmed feedstock"
        },
        "materials_campus": {
            "intake_short_tons_per_year": round(throughput),
            "throughput_short_tons_per_day_300_day_operation": round(throughput / 300, 2),
            "recovered_short_tons_per_year_SCENARIO": round(throughput * recovery),
            "residual_short_tons_per_year_SCENARIO": round(throughput * (1 - recovery)),
            "capex_usd_SCENARIO": round(capex),
            "annualized_capex_usd": round(annual_capex),
            "annual_opex_usd": round(opex_y),
            "annual_net_contributions_before_opex_capex_usd": round(gross_net_contribution),
            "net_annual_balance_usd_SCENARIO": round(net_y),
            "net_value_break_even_usd_per_intake_ton": round(theoretical_break_even, 2),
            "critical_warning": "Per-ton benefit must be verifiably net of product sale/import offset overlap; excludes additional unknown environmental and regulatory costs"
        },
        "front_street": {
            "business_count_SCENARIO": businesses,
            "annual_business_load_mwh": round(businesses * annual_business_mwh),
            "district_other_mwh": round(district_other_mwh),
            "water_mgd_SCENARIO": water_mgd,
            "annual_water_processing_mwh": round(water_mgd * 1e6 * GALLON_M3 * water_sec * DAYS / 1000),
            "optional_compute_mwh": round(edge_it_kw * pue * HOURS_YEAR / 1000),
            "annual_total_demand_mwh": round(district_energy_mwh),
            "annual_pv_supply_mwh_before_dispatch_losses": round(pv_energy_mwh),
            "annual_pv_minus_load_mwh_not_grid_savings": round(pv_energy_mwh - district_energy_mwh),
            "critical_load_mw": critical_mw,
            "sunless_outage_hours": outage_hours,
            "estimated_required_battery_nameplate_mwh": round(storage_mwh, 2),
            "solar_capex_stress_test_usd_range": [round(pv_mw * 1e6 * solar_cost_low),
                                                  round(pv_mw * 1e6 * solar_cost_high)],
            "battery_capex_stress_test_usd_range": [round(storage_mwh * 1000 * batt_cost_low),
                                                    round(storage_mwh * 1000 * batt_cost_high)],
            "warning": "Solar plus battery CAPEX excludes site, financing, O&M, utility fixed fees, backup fuel, network tariff and 8760-hour dispatch"
        },
        "separate_desal_zld_reference": {
            "freshwater_mgd": reference_desal_mgd,
            "concentrate_m3_per_day": round(ref_conc_m3_d),
            "extra_zld_gwh_per_year_stress_test": round(zld_gwh_y, 2),
            "extra_zld_electricity_usd_year": round(zld_gwh_y * 1e6 * electricity_price),
            "warning": "Not vendor design; alternative sources and mineral recovery can change costs"
        }
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--throughput", type=float, default=15000)
    p.add_argument("--capex", type=float, default=25e6)
    p.add_argument("--opex-per-ton", type=float, default=175)
    p.add_argument("--value-per-ton", type=float, default=250)
    p.add_argument("--recovery", type=float, default=.60)
    p.add_argument("--pv-mw", type=float, default=4)
    p.add_argument("--businesses", type=int, default=100)
    p.add_argument("--water-mgd", type=float, default=.20)
    p.add_argument("--edge-it-kw", type=float, default=50)
    p.add_argument("--zld-sec", type=float, default=10)
    args = p.parse_args()
    print(json.dumps(evaluate(
        throughput=args.throughput, capex=args.capex, opex_per_ton=args.opex_per_ton,
        net_contribution_per_ton=args.value_per_ton, recovery=args.recovery,
        pv_mw=args.pv_mw, businesses=args.businesses,
        water_mgd=args.water_mgd, edge_it_kw=args.edge_it_kw,
        zld_sec=args.zld_sec), indent=2))
