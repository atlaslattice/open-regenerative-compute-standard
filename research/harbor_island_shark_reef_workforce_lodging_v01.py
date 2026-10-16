#!/usr/bin/env python3
"""Shark Reef / Harbor Island hypothetical workforce hospitality economics v0.1.
Monthly-rate and mixed tourism sensitivity. No contract, sale, restaurant license,
hotel occupancy verification, or project construction authorization is presumed.
"""
import argparse,json
def calc(rooms=58,blocked=40,worker_monthly=1650,contracted_paid_frac=.90,
         visitor_nightly=125,visitor_occ=.55,meal_workers_per_room=1.0,
         meal_participation=.70,meal_days_month=22,meal_price=13,
         meal_contribution_margin=.25,room_contribution_margin=.35,
         refresh_capex=850000,acquisition=7000000,
         interest=.07,years=20):
    if not 0<=blocked<=rooms or not 0<=visitor_occ<=1 or not 0<=contracted_paid_frac<=1:
        raise ValueError("Check counts/occupancies")
    if any(x<0 for x in [rooms,worker_monthly,visitor_nightly,meal_workers_per_room,
                        meal_participation,meal_days_month,meal_price,
                        refresh_capex,acquisition,interest]):
        raise ValueError("Nonnegative inputs required")
    if not 0<=room_contribution_margin<=1 or not 0<=meal_contribution_margin<=1 or not 0<=meal_participation<=1 or years<=0:
        raise ValueError("Check margins and term")
    worker_rev=blocked*worker_monthly*12*contracted_paid_frac
    visitor_rev=(rooms-blocked)*visitor_nightly*365*visitor_occ
    meal_sales=blocked*meal_workers_per_room*meal_participation*meal_days_month*12*meal_price
    meals_contribution=meal_sales*meal_contribution_margin
    room_contribution=(worker_rev+visitor_rev)*room_contribution_margin
    capital=acquisition+refresh_capex
    crf=interest/(1-(1+interest)**(-years)) if interest else 1/years
    return {
     "status":"SCENARIO ONLY. Model margins are illustrative contributions, NOT verified hotel NOI or EBITDA.",
     "inputs":{"rooms":rooms,"reserved_for_workers":blocked,"monthly_contract_rate_usd":worker_monthly,
               "percent_of_reserved_room_months_paid":contracted_paid_frac,
               "tourist_avg_daily_rate_usd":visitor_nightly,
               "tourist_occupancy":visitor_occ,
               "meals_per_month_per_participating_worker":meal_days_month,
               "assumed_workers_per_reserved_room":meal_workers_per_room,
               "breakfast_or_dinner_uptake":meal_participation,
               "per_meal_sales_price":meal_price,
               "purchase_asking_benchmark_usd":acquisition,
               "refresh_capex_usd":refresh_capex},
     "annual":{"crew_rooms_revenue":round(worker_rev),
               "tourist_rooms_revenue":round(visitor_rev),
               "room_revenue_total":round(worker_rev+visitor_rev),
               "meal_sales_not_profit":round(meal_sales),
               "lodging_contribution_before_unallocated_costs":round(room_contribution),
               "meal_contribution_before_unallocated_costs":round(meals_contribution),
               "total_illustrative_contribution_before_unallocated_costs":round(room_contribution+meals_contribution),
               "full_debt_service_if_total_purchase_plus_refresh_financed":round(capital*crf),
               "unfunded_before_debt_reserve_taxes_unallocated_costs":
                   round(capital*crf-room_contribution-meals_contribution)},
     "cautions":["$1300/month pet-inclusive observation from user: not guaranteed current group rate",
                 "Lounge/cafe conversion requires zoning, kitchen/food permits and inspection",
                 "Construction schedule, EPC room-block needs and ferry shift windows not committed",
                 "Published $7m asking benchmark, not owner-approved deal or appraisal",
                 "Never convert occupancy or gross sales to profit without statements and full operating expenses"]
    }
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--blocked",type=int,default=40)
    p.add_argument("--worker-monthly",type=float,default=1650)
    p.add_argument("--refresh-capex",type=float,default=850000)
    p.add_argument("--pretty",action="store_true")
    a=p.parse_args()
    print(json.dumps(calc(blocked=a.blocked,worker_monthly=a.worker_monthly,
                         refresh_capex=a.refresh_capex),indent=2 if a.pretty else None))
if __name__=="__main__":main()
