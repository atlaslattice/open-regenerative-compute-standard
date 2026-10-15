#!/usr/bin/env python3
"""Maui circular water + materials v0.3: transparent SCENARIO mass balances.
No installed dependencies. Not validated engineering design or a revenue forecast.
Python 3.9+. Example: python maui_circular_resource_model_v03.py --mgd 5 --recovery 0.45
"""
import argparse
import json

GALLON_TO_M3 = 0.003785411784
DAYS = 365
# Representative *OPEN SEAWATER* g/L. Do NOT apply to brackish/saline wells untested.
SEAWATER_G_PER_L = {
    "Na": 10.8, "Cl": 19.4, "Mg": 1.29, "Ca": 0.412,
    "K": 0.399, "SO4": 2.71, "Br": 0.067, "Li": 0.00018,
}
D_H_ATOMIC_RATIO = 155.76e-6
MW_D = 2.014101778
MW_WATER = 18.01528
MW_GYPSUM = 172.17
MW_CALCIUM = 40.078

def evaluate(mgd=5.0, recovery=0.45, ro_sec=3.5,
             tds_g_l=35.0, product_tds_g_l=0.5,
             zld_sec_per_brine_m3=10.0, elec_price=0.20,
             lahaina_ww_mgd=4.2, lahaina_r1_mgd=1.7,
             nitrogen_mg_l=7.0, material_capture=0.25,
             edge_it_kw=0.0, pue=1.2):
    if mgd <= 0 or not 0 < recovery < 1 or ro_sec < 0 or tds_g_l < 0:
        raise ValueError("MGD>0, recovery 0..1, RO SEC>=0 and TDS>=0 required")
    if any(x < 0 for x in (product_tds_g_l, zld_sec_per_brine_m3,
                           elec_price, lahaina_ww_mgd, lahaina_r1_mgd,
                           nitrogen_mg_l, edge_it_kw)):
        raise ValueError("Inputs must be non-negative")
    if not 0 <= material_capture <= 1 or pue < 1:
        raise ValueError("material_capture in [0,1] and PUE>=1 required")
    if lahaina_r1_mgd > lahaina_ww_mgd:
        raise ValueError("R-1 output cannot exceed wastewater input")

    water_m3_d = mgd * 1_000_000 * GALLON_TO_M3
    feed_m3_d = water_m3_d / recovery
    brine_m3_d = feed_m3_d - water_m3_d
    ro_gwh_y = water_m3_d * ro_sec * DAYS / 1e6
    zld_gwh_y = brine_m3_d * zld_sec_per_brine_m3 * DAYS / 1e6
    feed_salts_t_y = feed_m3_d * tds_g_l * DAYS / 1000
    product_salts_t_y = water_m3_d * product_tds_g_l * DAYS / 1000
    brine_salts_t_y = feed_salts_t_y - product_salts_t_y
    # Every species below is an INVENTORY (not recovered) and overlaps total salts.
    ions_t_y = {
        k: feed_m3_d * value * DAYS / 1000
        for k, value in SEAWATER_G_PER_L.items()
    }
    # Molar calcium limit only; sulfate and industrial product specs may tighten it.
    max_gypsum_t_y = ions_t_y["Ca"] * MW_GYPSUM / MW_CALCIUM
    # Treat feed density as 1,000 kg/m3 for a first-pass order-of-magnitude isotope audit.
    # D is principally in water molecules, not salinity concentrate.
    d_fraction = 2 * D_H_ATOMIC_RATIO * MW_D / MW_WATER
    deuterium_inventory_t_y = feed_m3_d * 1000 * d_fraction * DAYS / 1000

    ww_m3_d = lahaina_ww_mgd * 1e6 * GALLON_TO_M3
    # 1 mg/L == 1 g/m3; result kg/y = m3 * g/m3 * days / 1000
    effluent_n_t_y = ww_m3_d * nitrogen_mg_l * DAYS / 1e6
    r1_headroom_mgd = lahaina_ww_mgd - lahaina_r1_mgd
    # Capability delta, not verified demand, nor unrestricted potable supply.
    extra_r1_million_gal_y = r1_headroom_mgd * 365
    edge_gwh_y = edge_it_kw * pue * 24 * DAYS / 1e6

    return {
        "status": "SCENARIO ONLY; no verified yields, revenues or projects",
        "geography_warning": "Lahaina figures are facility-level; seawater case hypothetical; county volumes cannot be silently merged",
        "parameters": {
            "finished_water_mgd": mgd, "ro_recovery_fraction": recovery,
            "ro_sec_kwh_per_m3_finished": ro_sec,
            "zld_sec_kwh_per_m3_brine_additional": zld_sec_per_brine_m3,
            "electricity_price_usd_per_kwh_assumed": elec_price,
            "material_capture_fraction_illustrative": material_capture,
        },
        "water": {
            "freshwater_m3_per_day": round(water_m3_d, 2),
            "seawater_feed_m3_per_day": round(feed_m3_d, 2),
            "brine_m3_per_day": round(brine_m3_d, 2),
            "lahaina_extra_r1_capability_mgd_not_demand": round(r1_headroom_mgd, 3),
            "lahaina_extra_r1_capability_million_gallons_per_year_upper_bound": round(extra_r1_million_gal_y, 2),
        },
        "energy": {
            "ro_gwh_per_year": round(ro_gwh_y, 3),
            "extra_zld_stress_test_gwh_per_year": round(zld_gwh_y, 3),
            "optional_edge_compute_gwh_per_year": round(edge_gwh_y, 3),
            "total_power_stress_test_gwh_per_year": round(ro_gwh_y + zld_gwh_y + edge_gwh_y, 3),
            "extra_zld_energy_cost_usd_per_year": round(zld_gwh_y * 1e6 * elec_price),
        },
        "minerals_inventory_not_products": {
            "feed_total_dissolved_salts_tonnes_per_year": round(feed_salts_t_y),
            "brine_total_dissolved_salts_tonnes_per_year": round(brine_salts_t_y),
            "element_and_ion_feed_tonnes_per_year": {k: round(v, 3) for k, v in ions_t_y.items()},
            "illustrative_25pct_material_capture_tonnes_per_year": {
                k: round(v * material_capture, 3) for k, v in ions_t_y.items()
            },
            "calcium_limited_theoretical_gypsum_tonnes_per_year": round(max_gypsum_t_y),
            "deuterium_in_whole_feedwater_elemental_equiv_tonnes_per_year_no_recovery_claim": round(deuterium_inventory_t_y),
        },
        "wastewater_and_nutrients": {
            "assumed_total_nitrogen_mg_per_l": nitrogen_mg_l,
            "illustrative_treated_effluent_nitrogen_tonnes_per_year_not_recovered": round(effluent_n_t_y, 2),
            "phosphorus_inventory": "UNKNOWN — requires plant samples",
            "manure_collection": "UNKNOWN — requires farm surveys",
        },
        "financial": "No mineral revenue, avoided import spend, housing savings, or ecological credits included without local prices, demand, costs and permits",
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mgd", type=float, default=5)
    p.add_argument("--recovery", type=float, default=.45)
    p.add_argument("--ro-sec", type=float, default=3.5)
    p.add_argument("--zld-sec", type=float, default=10)
    p.add_argument("--electricity-usd-kwh", type=float, default=.20)
    p.add_argument("--material-capture", type=float, default=.25)
    p.add_argument("--edge-it-kw", type=float, default=0)
    args = p.parse_args()
    print(json.dumps(evaluate(mgd=args.mgd, recovery=args.recovery,
                              ro_sec=args.ro_sec, zld_sec_per_brine_m3=args.zld_sec,
                              elec_price=args.electricity_usd_kwh,
                              material_capture=args.material_capture,
                              edge_it_kw=args.edge_it_kw), indent=2))
