"""Illustrative industrial throughput and resident-benefit accounting, NOT a forecast."""
from dataclasses import dataclass
import json
@dataclass
class Sector:
    name:str; external_sales_m:float; internal_sales_m:float; outside_cost_m:float; renewal_capex_m:float; output:str
SECTORS=[
 Sector("compute",950,65,570,170,"120 MW illustrative IT demand"),
 Sector("fusion_isotopes",0,0,0,0,"1.13 GW D-T + 20 MW D-D hypothetical fusion thermal; zero sales credit"),
 Sector("water_brine",85,42,72,22,"30,000 m3/day assumed water capacity"),
 Sector("fabrication",130,60,132,28,"25,000 tonnes/year hypothetical"),
 Sector("robotics",115,40,100,25,"1,000 robot service equivalents/year hypothetical"),
 Sector("food_bioreactors",65,35,76,16,"7,500 tonnes/year hypothetical"),
 Sector("retail_wellness_education",18,2,17,2,"resident services, hypothetical"),
 Sector("housing_utilities",0,0,32,14,"3,000 dwellings; zero resident markup")]
def evaluate(sectors=SECTORS,workers=5000,resident_fraction=.8,family_multiplier=1.7,commute_minutes_each_way=35,workdays=230):
    if not (0<=resident_fraction<=1):raise ValueError("resident fraction")
    if any(min(s.external_sales_m,s.internal_sales_m,s.outside_cost_m,s.renewal_capex_m)<0 for s in sectors):raise ValueError("negative sector input")
    resident_workers=round(workers*resident_fraction)
    commutes_avoided_hours=resident_workers*2*commute_minutes_each_way/60*workdays
    gross=sum(s.external_sales_m+s.internal_sales_m for s in sectors)
    internal=sum(s.internal_sales_m for s in sectors)
    external=sum(s.external_sales_m for s in sectors)
    opex=sum(s.outside_cost_m for s in sectors)
    capex=sum(s.renewal_capex_m for s in sectors)
    return {"evidence":"HYPOTHETICAL_SCENARIO_NOT_REALIZED","sector_inputs":[vars(s) for s in sectors],
      "annual_million_usd":{"gross_sector_invoiced_sales":gross,"internal_sales_eliminated":internal,
      "consolidated_external_sales":external,"external_opex_excluding_compensation_and_other_missing_items":opex,
      "annual_renewal_capex_proxy":capex,
      "incomplete_cash_proxy_not_FCF":external-opex-capex},
      "workforce":{"employees":workers,"resident_workers":resident_workers,
      "residents_including_family":round(resident_workers*family_multiplier),
      "nonresident_workers":workers-resident_workers,
      "commute_hours_avoided_per_year":round(commutes_avoided_hours),
      "monetized_commute_value_in_campus_revenue":0},
      "limitations":["No firm or public partner commitments","No verified industrial capacity","Cash proxy omits wages, debt, tax, insurance, working capital, construction, contingencies and prices uncertainty","No saleable fusion or helium-3 production assumed","Internal transfers eliminated; wages and local consumption cannot be added to economic output","Commuting time is resident benefit not automatic employer savings"]}
if __name__=="__main__":print(json.dumps(evaluate(),indent=2))
