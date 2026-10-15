#!/usr/bin/env python3
"""Maui v0.6: distributed owner-operated pickup routes and large-generator economics.

Illustrative steady-state scenario ONLY. Not a legal interpretation, customer census,
price quote, actual capacity contract, labor survey or real savings assertion.
No third-party grants, taxes, debt financing, ramp-up or ecological credits by default.

Run:
  python maui_microhauler_commercial_standards_v06.py
  python maui_microhauler_commercial_standards_v06.py --household-cost 20 --resort-fee 300 --capital 25000000
  python maui_microhauler_commercial_standards_v06.py --driver-pay-per-stop 10 --vehicle-per-stop 6 --depot-per-stop 3
"""
from __future__ import annotations
import argparse
import json

KG_US_SHORT_TON = 907.18474
WEEKS = 52

def cash_model(
    households=4200, small_businesses=380, large_sites=23,
    residential_visits_week=1, business_visits_week=2, large_visits_week=3,
    residential_kg_visit=9, business_kg_visit=75, large_kg_visit=350,
    residential_fee=15, business_fee=75, large_fee=500,
    driver_per_res_visit=8, vehicle_per_res_visit=4, depot_per_res_visit=2,
    business_cost=45, large_cost=180,
    overhead_annual=800000,
    net_processor_usd_ton=200, eligible_feed_fraction=1,
    capital=25000000, operator_stops_hour=8,
    operator_fte_hours=1800, route_days_year=260,
    route_hours_shift=5, bin_cost=20, enrollment_fee=20
):
    values=(households,small_businesses,large_sites,residential_visits_week,
            business_visits_week,large_visits_week,residential_kg_visit,
            business_kg_visit,large_kg_visit,residential_fee,business_fee,
            large_fee,driver_per_res_visit,vehicle_per_res_visit,depot_per_res_visit,
            business_cost,large_cost,overhead_annual,net_processor_usd_ton,
            eligible_feed_fraction,capital,operator_stops_hour,
            operator_fte_hours,route_days_year,route_hours_shift,bin_cost,
            enrollment_fee)
    if any(x < 0 for x in values):
        raise ValueError("All inputs must be nonnegative")
    if operator_stops_hour<=0 or operator_fte_hours<=0 or route_days_year<=0 or route_hours_shift<=0:
        raise ValueError("Stops/hour, FTE-hours, route days, shift hours must be >0")
    if not 0<=eligible_feed_fraction<=1:
        raise ValueError("eligible_feed_fraction must be in [0,1]")

    res_stops=households*WEEKS*residential_visits_week
    business_stops=small_businesses*WEEKS*business_visits_week
    large_stops=large_sites*WEEKS*large_visits_week
    res_cost=driver_per_res_visit+vehicle_per_res_visit+depot_per_res_visit
    res_margin=res_stops*(residential_fee-res_cost)
    business_margin=business_stops*(business_fee-business_cost)
    large_margin=large_stops*(large_fee-large_cost)
    collection_net=res_margin+business_margin+large_margin-overhead_annual
    kg=(res_stops*residential_kg_visit+
        business_stops*business_kg_visit+
        large_stops*large_kg_visit)
    mass_short=kg/KG_US_SHORT_TON
    eligible_short=mass_short*eligible_feed_fraction
    processing_net=eligible_short*net_processor_usd_ton
    cash=collection_net+processing_net
    simple_payback=(capital/cash if cash>0 else None)

    payroll_gross=res_stops*driver_per_res_visit
    vehicle_reimburse=res_stops*vehicle_per_res_visit
    truck_operator_hours=res_stops/operator_stops_hour
    daily_res_stops=res_stops/route_days_year
    truck_route_days=daily_res_stops/(operator_stops_hour*route_hours_shift)

    def breakeven_target(years):
        if eligible_short<=0:
            return None
        return (capital/years-collection_net)/eligible_short

    # Baseline difference holds subscriber counts, prices and other direct costs constant.
    v05_collection=res_stops*(residential_fee-20)+business_margin+large_margin-overhead_annual

    return {
        "evidence_grade":"SCENARIO — no customer contracts, actual routes, certified processing yield or awards",
        "years_per_model":1,"weekly_to_annual":WEEKS,
        "subscribers":{"residential":households,"small_business":small_businesses,"large_generators_NOT_mandated":large_sites},
        "annual_pickups":{"residential":res_stops,"small_business":business_stops,"large_generators":large_stops},
        "residential_microhaulers":{
            "fee_usd_visit":residential_fee,
            "driver_labor_gross_per_visit_usd":driver_per_res_visit,
            "vehicle_allowance_per_visit_usd":vehicle_per_res_visit,
            "hub_handling_per_visit_usd":depot_per_res_visit,
            "total_residential_cost_per_visit_usd":res_cost,
            "driver_pay_gross_annually_usd":round(payroll_gross),
            "vehicle_reimbursement_annually_usd":round(vehicle_reimburse),
            "driver_route_hours_per_year":round(truck_operator_hours),
            "driver_equivalent_FTE_assumed":round(truck_operator_hours/operator_fte_hours,2),
            "residential_stops_per_route_day":round(daily_res_stops,2),
            "5_hour_equivalent_trucks_per_day":round(truck_route_days,2),
            "labor_warning":"Route hours and FTE are scenario equivalents, not jobs created. Vehicle allowance, payroll classification and worker insurance must be verified."
        },
        "input":{
            "mass_metric_tonnes":round(kg/1000,2),
            "mass_US_short_tons":round(mass_short,2),
            "processor_eligible_US_short_tons":round(eligible_short,2),
            "material_net_per_US_short_ton_unverified_usd":net_processor_usd_ton,
            "bin_upfront_cost_all_sites_usd":round((households+small_businesses+large_sites)*bin_cost),
            "enrollment_upfront_all_sites_usd":round((households+small_businesses+large_sites)*enrollment_fee),
            "bin_warning":"$20 per site ignores commercial multi-bin and food-safe sealed containers; not included in annual cash."
        },
        "annual_cash_in_USD":{
            "residential_route_margin":round(res_margin),
            "small_business_route_margin":round(business_margin),
            "large_generator_route_margin_unverified":round(large_margin),
            "admin_and_shared_overhead":round(overhead_annual),
            "collections_net_before_processing":round(collection_net),
            "net_incremental_processor_contribution":round(processing_net),
            "cash_before_capital_financing_tax":round(cash),
            "simple_payback_years_if_positive":round(simple_payback,2) if simple_payback else None,
            "target_net_processor_margin_USD_per_eligible_short_ton_10yr":round(breakeven_target(10),2) if breakeven_target(10) is not None else None,
            "target_net_processor_margin_USD_per_eligible_short_ton_5yr":round(breakeven_target(5),2) if breakeven_target(5) is not None else None,
            "v05_household_cost_20_collection_margin":round(v05_collection),
            "conditional_annual_savings_vs_v05":round(collection_net-v05_collection),
            "important":"Gross processing sales must NOT be used: material margin must include processor capex? Here capital is separate; all processor OPEX, reject handling, QA, disposal and net verified receipts must be priced. Full-cost ROI requires working capital, inflation, taxes and debt."
        },
        "regulatory_checklist":{
            "carrier":"Refuse HRS271-5 exemption; confirm clean recyclable hauling classification",
            "loads":"HRS291C-131 covers and securement",
            "workforce":"Hawaii HRS383-6 and FLSA worker status review",
            "facility":"Maui commercial landfill rules and Hawaii DOH approvals",
            "resort":"No automatic direct hotel mandate in Hawaii Act 173 of 2026"
        }
    }

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--households",type=int,default=4200)
    p.add_argument("--small-businesses",type=int,default=380)
    p.add_argument("--large-sites",type=int,default=23)
    p.add_argument("--residential-fee",type=float,default=15)
    p.add_argument("--resort-fee",type=float,default=500)
    p.add_argument("--driver-pay-per-stop",type=float,default=8)
    p.add_argument("--vehicle-per-stop",type=float,default=4)
    p.add_argument("--depot-per-stop",type=float,default=2)
    p.add_argument("--household-cost",type=float,default=None,
                   help="Override residential total direct cost; allocated fully to vehicle portion, retaining driver pay and depot, must be >= those costs")
    p.add_argument("--eligible-feed-fraction",type=float,default=1)
    p.add_argument("--processor-net-per-ton",type=float,default=200)
    p.add_argument("--capital",type=float,default=25000000)
    p.add_argument("--stops-hour",type=float,default=8)
    args=p.parse_args()
    vehicle=args.vehicle_per_stop
    if args.household_cost is not None:
        vehicle=args.household_cost-args.driver_pay_per_stop-args.depot_per_stop
        if vehicle<0:
            p.error("household-cost must cover driver pay and depot receiving")
    print(json.dumps(cash_model(
        households=args.households,small_businesses=args.small_businesses,
        large_sites=args.large_sites,residential_fee=args.residential_fee,
        large_fee=args.resort_fee,driver_per_res_visit=args.driver_pay_per_stop,
        vehicle_per_res_visit=vehicle,depot_per_res_visit=args.depot_per_stop,
        eligible_feed_fraction=args.eligible_feed_fraction,
        net_processor_usd_ton=args.processor_net_per_ton,
        capital=args.capital,operator_stops_hour=args.stops_hour
    ),indent=2))
