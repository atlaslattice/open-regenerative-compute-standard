#!/usr/bin/env python3
"""Maui v0.5: community-priced separated-material pickup and organics pilot.

Pure Python 3 standard library. Inputs are HYPOTHETICAL, not signed customers,
actual waste weights, permit-approved plants, product-sales forecasts or vendor quotes.
Annual results are steady-state and omit multi-year ramp-up and tax/debt schedules.

Examples:
python maui_collection_bioreactor_network_v05.py
python maui_collection_bioreactor_network_v05.py --residential-fee 12.75 --material-net-per-short-ton 200
python maui_collection_bioreactor_network_v05.py --residential-frequency 2 --resort-fee 400 --capital 20000000
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict
from typing import Dict

KG_PER_METRIC_TON = 1000.0
KG_PER_US_SHORT_TON = 907.18474
WEEKS = 52

@dataclass(frozen=True)
class Region:
    residents: int
    businesses: int
    resorts: int

DEFAULT_REGIONS: Dict[str, Region] = {
    "West Maui": Region(1400, 120, 15),
    "North Shore": Region(700, 80, 1),
    "Central Maui": Region(1600, 140, 6),
    "Kula/Upcountry": Region(500, 40, 1),
}

def capital_recovery_factor(rate: float, years: int) -> float:
    if rate < 0 or years <= 0:
        raise ValueError("rate must be >=0 and life years >0")
    return 1.0 / years if rate == 0 else rate / (1 - (1 + rate) ** -years)

def simulate(*, regions=None, res_fee=15.0, business_fee=75.0,
             resort_fee=500.0, res_cost=20.0, business_cost=45.0,
             resort_cost=180.0, res_frequency=1, business_frequency=2,
             resort_frequency=3, res_kg_pickup=9.0,
             business_kg_pickup=75.0, resort_kg_pickup=350.0,
             startup_bin_cost=20.0, signup_fee=20.0,
             shared_overhead=800000.0, capital=15000000.0,
             capital_rate=0.07, project_years=20,
             feed_eligible_fraction=1.0,
             material_net_per_short_ton=200.0,
             organics_share=0.45, compost_wet_yield=0.35,
             annual_documented_operating_grants=0.0,
             one_time_documented_capital_grants=0.0):
    regions = regions or DEFAULT_REGIONS
    prices_costs = (res_fee, business_fee, resort_fee, res_cost,
                    business_cost, resort_cost, startup_bin_cost,
                    signup_fee, shared_overhead, capital,
                    res_kg_pickup, business_kg_pickup, resort_kg_pickup,
                    material_net_per_short_ton, annual_documented_operating_grants,
                    one_time_documented_capital_grants)
    if any(v < 0 for v in prices_costs):
        raise ValueError("all monetary, weight, and direct costs must be nonnegative")
    if not (0 <= feed_eligible_fraction <= 1 and 0 <= organics_share <= 1
            and 0 <= compost_wet_yield <= 1):
        raise ValueError("recovery and organic fractions must be in [0,1]")
    for f in (res_frequency, business_frequency, resort_frequency):
        if not (1 <= f <= 7):
            raise ValueError("pickup frequency 1–7 times/week required")
    if not regions:
        raise ValueError("at least one region required")

    streams = (
        ("residents", res_fee, res_cost, res_frequency, res_kg_pickup),
        ("businesses", business_fee, business_cost, business_frequency, business_kg_pickup),
        ("resorts", resort_fee, resort_cost, resort_frequency, resort_kg_pickup),
    )
    region_out = {}
    totals = {"sites": 0, "annual_stops": 0, "pickup_revenue_usd": 0.0,
              "pickup_direct_cost_usd": 0.0, "intake_kg": 0.0}
    for name, r in regions.items():
        if any(v < 0 for v in asdict(r).values()):
            raise ValueError("site counts must be nonnegative")
        detail = {"sites": 0, "annual_stops": 0, "revenue_usd": 0.0,
                  "direct_cost_usd": 0.0, "intake_kg": 0.0, "streams": {}}
        for type_name, fee, cost, freq, kg_per in streams:
            n = getattr(r, type_name)
            stops = n * freq * WEEKS
            rev, expense, mass_kg = stops * fee, stops * cost, stops * kg_per
            detail["streams"][type_name] = {
                "subscribers": n, "annual_stops": stops,
                "fee_usd_per_stop": fee, "direct_cost_usd_per_stop": cost,
                "monthly_revenue_usd_per_site": round(fee * freq * WEEKS / 12, 2),
                "net_route_usd_before_shared_overhead": round(rev - expense, 2),
                "annual_intake_metric_tonnes": round(mass_kg / KG_PER_METRIC_TON, 2)}
            detail["sites"] += n
            detail["annual_stops"] += stops
            detail["revenue_usd"] += rev
            detail["direct_cost_usd"] += expense
            detail["intake_kg"] += mass_kg
        for key, tkey in (("sites", "sites"),
                          ("annual_stops", "annual_stops"),
                          ("revenue_usd", "pickup_revenue_usd"),
                          ("direct_cost_usd", "pickup_direct_cost_usd"),
                          ("intake_kg", "intake_kg")):
            totals[tkey] += detail[key]
        region_out[name] = {
            "sites": detail["sites"], "annual_stops": detail["annual_stops"],
            "metric_tonnes_year": round(detail["intake_kg"] / 1000, 2),
            "route_margin_usd_year": round(detail["revenue_usd"] - detail["direct_cost_usd"], 2),
            "streams": detail["streams"]
        }

    route_margin = totals["pickup_revenue_usd"] - totals["pickup_direct_cost_usd"]
    collection_contribution = route_margin - shared_overhead + annual_documented_operating_grants
    collected_short_tons = totals["intake_kg"] / KG_PER_US_SHORT_TON
    eligible_short_tons = collected_short_tons * feed_eligible_fraction
    processing_contribution = eligible_short_tons * material_net_per_short_ton
    annual_cash = collection_contribution + processing_contribution
    net_investment = max(0.0, capital - one_time_documented_capital_grants)
    crf = capital_recovery_factor(capital_rate, project_years)
    capital_charge = net_investment * crf
    net_annualized = annual_cash - capital_charge

    # Cash payback is not discounted payback or a debt amortization; negative is never "profitable."
    simple_payback_years = (net_investment / annual_cash) if annual_cash > 0 else None
    threshold_10 = ((net_investment / 10.0 - collection_contribution) / eligible_short_tons
                    if eligible_short_tons > 0 else None)
    threshold_5 = ((net_investment / 5.0 - collection_contribution) / eligible_short_tons
                   if eligible_short_tons > 0 else None)
    start_bins = totals["sites"] * startup_bin_cost
    start_enrollment_revenue = totals["sites"] * signup_fee
    organics_metric = totals["intake_kg"] / 1000 * organics_share
    dry_other_metric = totals["intake_kg"] / 1000 - organics_metric
    compost_metric = organics_metric * compost_wet_yield

    return {
        "evidence_status": "SCENARIO ONLY: 0 signed service agreements; 0 verified material income or grants by default",
        "geographic_scope": "Hypothetical Maui-island nodes, not selected sites; historic county food waste is NOT the model's collected supply",
        "assumptions": {
            "weeks_per_year": WEEKS, "monthly_pricing_note": "52 weeks divided by 12",
            "residential_fee_per_pickup_usd": res_fee,
            "residential_cost_per_pickup_usd": res_cost,
            "resident_frequency_weekly": res_frequency,
            "resort_fee_per_pickup_usd_UNVERIFIED": resort_fee,
            "material_net_contribution_per_ELIGIBLE_short_ton_usd_UNVERIFIED": material_net_per_short_ton,
            "eligible_feed_fraction": feed_eligible_fraction,
            "shared_overhead_usd_per_year": shared_overhead,
            "capital_usd_STRESS_TEST": capital,
            "capital_rate": capital_rate, "asset_life_years": project_years,
            "separate_biological_and_dry_material_streams": True,
        },
        "regions": region_out,
        "island_collection": {
            "locations": totals["sites"],
            "annual_stops": totals["annual_stops"],
            "annual_pickup_revenue_usd": round(totals["pickup_revenue_usd"]),
            "annual_direct_collection_cost_usd": round(totals["pickup_direct_cost_usd"]),
            "annual_net_route_usd": round(route_margin),
            "annual_contribution_after_shared_overhead_before_processing_usd": round(collection_contribution),
            "one_time_bins_cost_usd": round(start_bins),
            "one_time_signup_revenue_usd": round(start_enrollment_revenue),
            "bin_cash_difference_usd": round(start_enrollment_revenue - start_bins),
        },
        "material_balances": {
            "collected_metric_tonnes_year": round(totals["intake_kg"] / 1000, 2),
            "collected_US_short_tons_year": round(collected_short_tons, 2),
            "eligible_US_short_tons_year": round(eligible_short_tons, 2),
            "organics_input_metric_tonnes_year_HYPOTHETICAL": round(organics_metric, 2),
            "other_dry_mixed_input_metric_tonnes_year": round(dry_other_metric, 2),
            "compost_wet_tonnes_year_IF_ALL_ORGANICS_ARE_COMPOSTED": round(compost_metric, 2),
            "warning": "Compost mass is NOT fertilizer-equivalent nutrient mass, no anaerobic gas or digestate co-credit, and other dry stream contains contamination."
        },
        "financial_screen": {
            "annual_net_processor_contribution_after_its_operating_cost_usd_UNVERIFIED": round(processing_contribution),
            "annual_unlevered_operating_cash_before_capital_and_tax_usd_SCENARIO": round(annual_cash),
            "investment_net_of_ACTUALLY_SPECIFIED_capital_grants_usd": round(net_investment),
            "capital_recovery_factor": round(crf, 6),
            "annualized_capital_recovery_cost_usd": round(capital_charge),
            "annual_cash_less_annuitized_capital_usd_SCENARIO": round(net_annualized),
            "simple_payback_years_if_positive_NOT_DISCOUNTED": round(simple_payback_years, 2) if simple_payback_years is not None else None,
            "10yr_payback_required_processor_net_usd_per_eligible_short_ton": round(threshold_10, 2) if threshold_10 is not None else None,
            "5yr_payback_required_processor_net_usd_per_eligible_short_ton": round(threshold_5, 2) if threshold_5 is not None else None,
            "warning": "No forecast: excludes multi-year ramp, taxes, debt service, capex overruns, extra residuals, and product qualification failures. Processor contribution must be after ALL processor operating costs and not double-counting pickups."
        },
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--residential-fee", type=float, default=15)
    p.add_argument("--business-fee", type=float, default=75)
    p.add_argument("--resort-fee", type=float, default=500)
    p.add_argument("--residential-cost", type=float, default=20)
    p.add_argument("--residential-frequency", type=int, default=1)
    p.add_argument("--material-net-per-short-ton", type=float, default=200)
    p.add_argument("--eligible-feed-fraction", type=float, default=1)
    p.add_argument("--capital", type=float, default=15_000_000)
    p.add_argument("--overhead", type=float, default=800_000)
    p.add_argument("--organics-share", type=float, default=.45)
    p.add_argument("--compost-wet-yield", type=float, default=.35)
    args = p.parse_args()
    result = simulate(res_fee=args.residential_fee,
                      business_fee=args.business_fee,
                      resort_fee=args.resort_fee,
                      res_cost=args.residential_cost,
                      res_frequency=args.residential_frequency,
                      material_net_per_short_ton=args.material_net_per_short_ton,
                      feed_eligible_fraction=args.eligible_feed_fraction,
                      capital=args.capital,
                      shared_overhead=args.overhead,
                      organics_share=args.organics_share,
                      compost_wet_yield=args.compost_wet_yield)
    print(json.dumps(result, indent=2))
