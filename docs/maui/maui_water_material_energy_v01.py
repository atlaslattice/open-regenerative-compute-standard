#!/usr/bin/env python3
"""Maui ORCS v0.1: transparent illustrative water/energy/mineral scenario model.

Runs with Python 3.9+ standard library. Not investment engineering.
Parameters are assumptions, not site groundwater assays or public approvals.
"""
from __future__ import annotations
import argparse
import json
from math import ceil

GAL_TO_M3 = 0.003785411784
DAYS = 365.0

def simulate(
    finished_mgd: float = 5.0,
    recovery: float = 0.45,
    feed_salinity_kg_m3: float = 35.0,
    permeate_salinity_kg_m3: float = 0.5,
    electricity_kwh_m3: float = 3.5,
    pv_capacity_factor: float = 0.20,
    continuous_it_kw: float = 0.0,
    pue: float = 1.2,
    solar_fraction_annual: float = 1.0,
    reuse_county_mgd: float = 0.0,
    kwh_price_usd: float = 0.15,
) -> dict:
    if finished_mgd <= 0 or not 0 < recovery < 1:
        raise ValueError("Water product must be >0 MGD and recovery between 0 and 1")
    if any(x < 0 for x in (feed_salinity_kg_m3, permeate_salinity_kg_m3,
                          electricity_kwh_m3, continuous_it_kw, reuse_county_mgd, kwh_price_usd)):
        raise ValueError("Inputs must be nonnegative")
    if not 0 < pv_capacity_factor <= 1 or pue < 1 or not 0 <= solar_fraction_annual <= 1:
        raise ValueError("Invalid capacity factor, PUE, or solar fraction")
    product = finished_mgd * 1e6 * GAL_TO_M3
    feed = product / recovery
    reject = feed - product
    feed_salt_kg_day = feed * feed_salinity_kg_m3
    reject_salt_kg_day = feed_salt_kg_day - product * permeate_salinity_kg_m3
    if reject_salt_kg_day < 0:
        raise ValueError("Product salinity exceeds feed-salt balance")
    process_mwh_year = product * DAYS * electricity_kwh_m3 / 1_000.0
    it_mwh_year = continuous_it_kw * pue * 24.0 * DAYS / 1_000.0
    total_mwh_year = process_mwh_year + it_mwh_year
    pv_mwp_energy_equivalent = solar_fraction_annual * total_mwh_year / (8_760 * pv_capacity_factor) # MW
    total_mw_average = total_mwh_year / 8_760.0
    # Seawater chemistry values below are element feed inventories, never yields.
    element_kg_m3 = {
        "magnesium_element": 1.29,
        "calcium_element": 0.41,
        "potassium_element": 0.40,
        "bromide_ion": 0.065,
        "lithium_element": 0.00018,
        "deuterium_element": 0.034,  # approx seawater hydrogen isotope mass, NOT separated D2O
    }
    elements_t_year = {
        name: round(feed * DAYS * kg_m3 / 1000.0, 1)
        for name, kg_m3 in element_kg_m3.items()
    }
    gypsum_upper_t_year = elements_t_year["calcium_element"] * (172.17 / 40.078)
    return {
        "status": "PROPOSED; illustrative parameters only; zero realized benefits",
        "parameters": {
            "finished_mgd": finished_mgd, "recovery": recovery,
            "feed_salinity_kg_m3": feed_salinity_kg_m3,
            "permeate_salinity_kg_m3": permeate_salinity_kg_m3,
            "electricity_kwh_m3": electricity_kwh_m3,
            "pv_capacity_factor": pv_capacity_factor,
            "continuous_it_kw": continuous_it_kw, "pue": pue,
            "solar_fraction_annual": solar_fraction_annual,
            "reuse_county_mgd": reuse_county_mgd,
            "kwh_price_usd": kwh_price_usd
        },
        "water": {
            "product_m3_day": round(product, 1),
            "feed_m3_day": round(feed, 1),
            "reject_m3_day": round(reject, 1),
            "reject_salt_tonnes_year": round(reject_salt_kg_day * DAYS / 1000, 0),
            "feed_salt_tonnes_year": round(feed_salt_kg_day * DAYS / 1000, 0),
            "reject_salinity_kg_m3": round(reject_salt_kg_day / reject, 2),
            "county_reuse_billion_gallons_year": round(reuse_county_mgd * DAYS / 1000, 3),
            "county_reuse_note": "User scenario for COUNTY, never Maui-island-only without plant split",
        },
        "electricity": {
            "desal_gwh_year": round(process_mwh_year / 1000, 3),
            "inference_facility_gwh_year": round(it_mwh_year / 1000, 3),
            "combined_gwh_year": round(total_mwh_year / 1000, 3),
            "total_average_mw": round(total_mw_average, 3),
            "nameplate_solar_mw_annual_energy_equivalent": round(pv_mwp_energy_equivalent, 2),
            "12_hour_useful_battery_mwh_at_average_load": round(total_mw_average * 12, 1),
            "annual_electricity_spend_usd": round(total_mwh_year * 1000 * kwh_price_usd),
            "caveat": "Annual PV offset is not firm delivery. PV area, storage losses, pumps and redundancy unmodeled.",
        },
        "raw_feed_element_inventory_tonnes_year_NOT_recovered": elements_t_year,
        "pure_gypsum_stoichiometric_ceil_tonnes_year_NOT_recovery": round(gypsum_upper_t_year),
        "warnings": [
            "Use site-specific groundwater chemistry; this default assumes open-ocean seawater.",
            "Gross salt and isotope inventories are not products, economic yields or validated resource extraction.",
            "Real gypsum recovered from brine may be uneconomic; drywall diversion requires contamination controls.",
            "PV, inference and desal co-siting require permits, Hawaiian cultural consultation and resilience design.",
            "No import/export substitution without measured current Maui-island freight, supply and off-take data.",
            "Energy pricing is marginal illustrative only; excludes capital, maintenance and delivery charges.",
            "Public-health drinking water quality and nearshore ecology are different monitoring domains.",
        ],
    }

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--finished-mgd", type=float, default=5.0)
    p.add_argument("--recovery", type=float, default=0.45)
    p.add_argument("--feed-salinity-kg-m3", type=float, default=35.0)
    p.add_argument("--electricity-kwh-m3", type=float, default=3.5)
    p.add_argument("--pv-capacity-factor", type=float, default=0.20)
    p.add_argument("--continuous-it-kw", type=float, default=0)
    p.add_argument("--pue", type=float, default=1.2)
    p.add_argument("--solar-fraction-annual", type=float, default=1.0)
    p.add_argument("--reuse-county-mgd", type=float, default=0)
    p.add_argument("--kwh-price-usd", type=float, default=0.15)
    a = p.parse_args()
    results = simulate(**vars(a))
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
