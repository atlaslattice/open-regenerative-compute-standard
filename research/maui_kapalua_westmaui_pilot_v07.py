#!/usr/bin/env python3
"""ORCS Maui v0.7 — Kapalua resort + West Maui residential micro-hauler test.
Reproducible SCENARIO, not Ritz-Carlton meter data, facility design, verified sales
or actual business contracts. stdlib-only. All money in USD, tonnage in METRIC tonnes
unless explicitly short tons. Resort name is an illustrative, unaffiliated case.
Run: python maui_kapalua_westmaui_pilot_v07.py
     python maui_kapalua_westmaui_pilot_v07.py --roof-sqft 70000 --solar-yield 1450 --res-homes 2500
"""
import argparse
import json

GALLON_L = 3.785411784
DAYS=365
WEEKS=52

def crf(rate: float, years: int):
    if years<=0 or rate<0: raise ValueError("invalid rate or years")
    return rate/(1-(1+rate)**(-years)) if rate>0 else 1/years

def model(
  rooms=468, occupancy=0.72, hotel_electric_kwh_per_available_room_year=20000,
  roof_sqft=90000, roof_usable=0.60, canopy_sqft=60000, canopy_usable=0.65,
  pv_w_per_covered_sqft=15, pv_kwh_per_kw_year=1600, pv_self_use=0.85,
  avoided_electricity_price_usd_kwh=0.338, installed_pv_usd_w=3,
  pv_annual_opex_fraction=0.015, battery_kwh=2000, battery_cost_usd_kwh=500,
  roomnight_water_liters=1962.08, water_reuse_fraction=0.25,
  hotel_total_waste_kg_roomnight=2.5, hotel_food_kg_roomnight=0.9,
  hotel_landscape_metric_tonnes_year=100, wet_compost_yield=0.35,
  resort_visits_week=5, resort_fee_per_visit=500, resort_cost_per_visit=250,
  res_homes=1400, res_visits_week=1, res_fee_per_visit=15,
  res_driver_usd_per_visit=8, res_vehicle_usd_per_visit=4,
  res_hub_receive_usd_per_visit=2, res_kg_per_visit=9,
  stops_per_route_hour=8, fte_route_hours_year=1800,
  processor_eligible_fraction=1, processor_net_usd_metric_ton=80,
  shared_hub_operating_cost_year=120000, hub_capex_usd=1500000,
  hub_capital_interest=0.07, hub_capital_life_years=10
):
    numeric=locals().copy()
    if any(v < 0 for v in numeric.values()):raise ValueError("All arguments nonnegative")
    if rooms<=0 or res_visits_week>7 or resort_visits_week>7 or fte_route_hours_year<=0 or stops_per_route_hour<=0:
        raise ValueError("invalid counts, weekly frequency or labor denominator")
    for key in ("occupancy","roof_usable","canopy_usable","pv_self_use",
                "water_reuse_fraction","wet_compost_yield","processor_eligible_fraction"):
        if not 0<=numeric[key]<=1:raise ValueError(key+" must be in [0,1]")
    if hotel_food_kg_roomnight>hotel_total_waste_kg_roomnight:
        raise ValueError("Food must be subset of total hotel waste")

    occupied_roomnights=rooms*occupancy*DAYS
    # This is all-in electricity per AVAILABLE ROOM/year, not just occupied-room incremental load.
    hotel_kwh=rooms*hotel_electric_kwh_per_available_room_year
    roof_kw=roof_sqft*roof_usable*pv_w_per_covered_sqft/1000
    canopy_kw=canopy_sqft*canopy_usable*pv_w_per_covered_sqft/1000
    pv_kw=roof_kw+canopy_kw
    solar_kwh=pv_kw*pv_kwh_per_kw_year
    self_used_kwh=min(solar_kwh*pv_self_use,hotel_kwh)
    gross_solar_bill_offset=self_used_kwh*avoided_electricity_price_usd_kwh
    pv_capex=pv_kw*1000*installed_pv_usd_w
    batt_capex=battery_kwh*battery_cost_usd_kwh
    # No battery revenue, bill management, credits or battery replacement savings assumed.
    pv_opex=pv_capex*pv_annual_opex_fraction
    energy_simple_payback=pv_capex/(gross_solar_bill_offset-pv_opex) if gross_solar_bill_offset>pv_opex else None

    # Marriott lists footprint per room night, not verified meter gallons or water quality.
    hotel_water_l=occupied_roomnights*roomnight_water_liters
    notional_reuse_gal=hotel_water_l/GALLON_L*water_reuse_fraction
    hotel_waste_mt=occupied_roomnights*hotel_total_waste_kg_roomnight/1000
    hotel_food_mt=occupied_roomnights*hotel_food_kg_roomnight/1000
    hotel_total_with_landscape_mt=hotel_waste_mt+hotel_landscape_metric_tonnes_year
    hotel_organics_mt=hotel_food_mt+hotel_landscape_metric_tonnes_year
    compost_mt=hotel_organics_mt*wet_compost_yield
    resort_stops=resort_visits_week*WEEKS
    # Resort vehicles need high enough weight capacity; not pickup-truck residential vehicle assumption!
    average_resort_load_kg=hotel_total_with_landscape_mt*1000/resort_stops if resort_stops>0 else None
    resort_margin=resort_stops*(resort_fee_per_visit-resort_cost_per_visit)

    homes_stops=res_homes*res_visits_week*WEEKS
    res_unit_cost=res_driver_usd_per_visit+res_vehicle_usd_per_visit+res_hub_receive_usd_per_visit
    res_revenue=homes_stops*res_fee_per_visit
    res_direct_cost=homes_stops*res_unit_cost
    res_margin=res_revenue-res_direct_cost
    res_kg=homes_stops*res_kg_per_visit
    res_route_hours=homes_stops/stops_per_route_hour
    # Commingled waste never automatically becomes 3D-print suitable or agronomic output.
    total_collection_mt=hotel_total_with_landscape_mt+res_kg/1000
    processor_net=total_collection_mt*processor_eligible_fraction*processor_net_usd_metric_ton
    hub_before_capital=resort_margin+res_margin+processor_net-shared_hub_operating_cost_year
    hub_annuity=hub_capex_usd*crf(hub_capital_interest,hub_capital_life_years)
    annual_hub_surplus=hub_before_capital-hub_annuity

    return {
      "status":"ILLUSTRATIVE SCENARIO — not Marriott meter or scrap/tipping receipt; no contracts or grants",
      "boundary":"one Kapalua property plus West Maui subscribed households; no actual site participation",
      "hotel":{
        "available_rooms":rooms,
        "hotel_occupied_roomnights_at_modeled_occupancy":round(occupied_roomnights),
        "modeled_annual_electricity_GWh_NOT_METERED":round(hotel_kwh/1e6,3),
        "rooftop_roof_assumed_gross_sqft_NOT_SURVEYED":roof_sqft,
        "roof_useable_sqft":round(roof_sqft*roof_usable),
        "carport_candidate_gross_sqft_NOT_SURVEYED":canopy_sqft,
        "roof_pv_kWdc":round(roof_kw,1),
        "carport_pv_kWdc":round(canopy_kw,1),
        "total_pv_kWdc":round(pv_kw,1),
        "pv_output_GWh_year_assumed_Kapalua_site_not_yet_PVWatts":round(solar_kwh/1e6,3),
        "pv_share_of_modeled_electric_load_percent":round(100*solar_kwh/hotel_kwh,2) if hotel_kwh else None,
        "self_used_energy_GWh_year":round(self_used_kwh/1e6,3),
        "gross_avoided_purchased_electricity_USD_no_fixed_charges":round(gross_solar_bill_offset),
        "pv_capex_assumed_usd":round(pv_capex),
        "battery_capex_assumed_usd_NO_BILL_CREDIT":round(batt_capex),
        "pv_annual_opex_usd":round(pv_opex),
        "pv_only_simple_payback_years_excludes_financing":round(energy_simple_payback,2) if energy_simple_payback else None,
        "water_footprint_million_gallons_at_modeled_occupancy":round(hotel_water_l/GALLON_L/1e6,2),
        "potential_nonpotable_reuse_million_gallons_SCENARIO":round(notional_reuse_gal/1e6,2),
        "room_and_hotel_operational_waste_metric_tonnes_SCENARIO":round(hotel_waste_mt,2),
        "food_subset_metric_tonnes_SCENARIO":round(hotel_food_mt,2),
        "additional_landscape_waste_metric_tonnes_SCENARIO":round(hotel_landscape_metric_tonnes_year,2),
        "all_referenced_waste_metric_tonnes_SCENARIO":round(hotel_total_with_landscape_mt,2),
        "food_plus_landscape_organics_metric_tonnes":round(hotel_organics_mt,2),
        "compost_wet_tonnes_if_aerobic_treatment_SCENARIO":round(compost_mt,2),
        "resort_pickups_per_year":resort_stops,
        "average_waste_weight_per_resort_pickup_kg":round(average_resort_load_kg,2) if average_resort_load_kg is not None else None,
        "resort_service_revenue_usd_year":round(resort_stops*resort_fee_per_visit),
        "resort_service_direct_cost_usd_year":round(resort_stops*resort_cost_per_visit),
        "resort_route_contribution_usd_year":round(resort_margin),
        "warning":"Marriott room count differs between resort pages (466–468); 468 primary. Not confirmed roof footprint, property electricity meter, source-separated waste, or current existing renewable system."
      },
      "west_maui_homes":{
        "subscriber_homes_SCENARIO":res_homes,
        "annual_household_pickups":homes_stops,
        "residential_price_usd_per_pickup":res_fee_per_visit,
        "residential_monthly_fee_usd":round(res_visits_week*WEEKS*res_fee_per_visit/12,2),
        "total_residential_revenue_usd_year":round(res_revenue),
        "residential_route_direct_cost_usd_year":round(res_direct_cost),
        "residential_route_contribution_before_overhead_usd_year":round(res_margin),
        "resident_collected_metric_tonnes_year_SCENARIO":round(res_kg/1000,2),
        "driver_gross_labor_budget_usd_year":round(homes_stops*res_driver_usd_per_visit),
        "driver_route_hours_year":round(res_route_hours),
        "route_driver_full_time_equivalent_FTE_SCENARIO":round(res_route_hours/fte_route_hours_year,2),
        "daily_five_day_week_stops":round(res_homes*res_visits_week/5,2),
        "truck_equivalent_5h_daily_shifts":round((res_homes*res_visits_week/5)/(5*stops_per_route_hour),2),
        "warning":"Driver count FTE excludes business/resort truck crews and hub employees; hourly earnings $8/stop×8 stops/hour only if route assumptions hold."
      },
      "combined_network":{
        "annual_feed_metric_tonnes_SCENARIO":round(total_collection_mt,2),
        "eligible_processed_metric_tonnes_SCENARIO":round(total_collection_mt*processor_eligible_fraction,2),
        "annual_net_processing_contribution_usd_AFTER_PROCESSING_OPEX_assumed":round(processor_net),
        "combined_route_margin_before_shared_overhead_usd":round(resort_margin+res_margin),
        "shared_hub_opex_usd_year_assumed":round(shared_hub_operating_cost_year),
        "cash_before_hub_capital_usd":round(hub_before_capital),
        "annual_hub_capital_recovery_usd_assumed":round(hub_annuity),
        "annual_surplus_after_capital_charge_usd":round(annual_hub_surplus),
        "financial_caveat":"Net material contribution cannot double-count lost scrap export and imported substitute values; no signed customers, no rate uplift, no grant allocation, no permit or greenhouse claims."
      }
    }

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rooms",type=int,default=468)
    p.add_argument("--occupancy",type=float,default=.72)
    p.add_argument("--hotel-kwh-room-year",type=float,default=20000)
    p.add_argument("--roof-sqft",type=float,default=90000)
    p.add_argument("--canopy-sqft",type=float,default=60000)
    p.add_argument("--solar-yield",type=float,default=1600)
    p.add_argument("--res-homes",type=int,default=1400)
    p.add_argument("--resort-fee",type=float,default=500)
    p.add_argument("--hub-capex",type=float,default=1500000)
    p.add_argument("--processor-margin",type=float,default=80)
    a=p.parse_args()
    print(json.dumps(model(rooms=a.rooms,occupancy=a.occupancy,
         hotel_electric_kwh_per_available_room_year=a.hotel_kwh_room_year,
         roof_sqft=a.roof_sqft,canopy_sqft=a.canopy_sqft,
         pv_kwh_per_kw_year=a.solar_yield,res_homes=a.res_homes,
         resort_fee_per_visit=a.resort_fee,hub_capex_usd=a.hub_capex,
         processor_net_usd_metric_ton=a.processor_margin),indent=2))
