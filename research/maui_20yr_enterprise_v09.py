#!/usr/bin/env python3
"""Maui ORCS 20y steady-state enterprise SCREENING — nominal 2026 USD.
Run: python3 maui_20yr_enterprise_v09.py
All unmarked items are adjustable MODEL ASSUMPTIONS, not tender bids.
All assets assumed complete at year-one; no phasing, grants, inflation or escalation.
"""
import csv, os
OUT=os.path.dirname(os.path.abspath(__file__))
REPORTED_DWS_REVENUE=82473555 # audited FY2025 Maui County DWS
REPORTED_DWS_EXPENSE=82819253 # includes depreciation
REPORTED_DWS_DEPRECIATION=16876258
HISTORICAL_PIPE_MILES=1014 # cross-year countywide inventory; excludes service lines
CAPEX_USD={
    "Launiupoko/Olowalu proposed purchase":6e6, # council-authorized UP TO, not completed
    "Other private water/wastewater supplier acquisition allowance":144e6,
    "36 MGD three-campus desal RO":864e6,
    "RO concentrate/wastewater ZLD and useful salts":700e6,
    "Existing wastewater treatment and greywater upgrades":550e6,
    "12,200 onsite cesspools x $35k":427e6,
    "Microgrids PV batteries firm backup":420e6,
    "Emergency storage pumping and interties":275e6,
    "Organics minerals and local rPET processing":170e6,
    "County bottling product line":40e6,
    "Distributed AI PLC/SCADA fiber and metering":110e6,
}
NEW_OPEX_USD={
    "RO treatment":55e6,"ZLD power/process":120e6,
    "Wastewater reuse":32e6,"Pumping and pipe management":38e6,
    "Microgrid operations":18e6,"Cesspool cluster operations":14e6,
    "Waste/mineral/rPET operation":14e6,"AI/OT/cyber":13e6,
    "Disaster reserve":6e6
}
OTHER_REVENUE_USD={
    "Acquired customers—not supplier upstream double count":11e6,
    "Additional reclaimed sales":12e6,
    "Mineral and nutrient products":6e6,
    "Third-party waste processing services":7e6,
}
# Imported single-serve water model: US demand extrapolation, NOT measured Maui sales
MODEL_BOTTLE_UNITS=53_926_000*0.80*0.75
WHOLESALE_UNIT_USD=.75
FULL_BOTTLE_CASH_OPEX_UNIT=.50 # before $40M plant debt
RETIRED_OLD_DWS_CASH_COSTS=16e6 # no double count with above OPEX
PIPE_CAPEX_PER_MILE=4e6
INTEREST=.05
BASE_DWS_CASH_OPEX=REPORTED_DWS_EXPENSE-REPORTED_DWS_DEPRECIATION

def annuity(principal, r, years):
    return principal*r/(1-(1+r)**(-years)) if r else principal/years

def case(name,pct,years):
    cap=sum(CAPEX_USD.values())+HISTORICAL_PIPE_MILES*pct*PIPE_CAPEX_PER_MILE
    debt=annuity(cap,INTEREST,years)
    income=REPORTED_DWS_REVENUE+sum(OTHER_REVENUE_USD.values())+MODEL_BOTTLE_UNITS*WHOLESALE_UNIT_USD
    op=BASE_DWS_CASH_OPEX-RETIRED_OLD_DWS_CASH_COSTS+sum(NEW_OPEX_USD.values())+MODEL_BOTTLE_UNITS*FULL_BOTTLE_CASH_OPEX_UNIT
    gap=max(0,op+debt-income)
    return dict(scenario=name,pipe_miles=HISTORICAL_PIPE_MILES*pct,capex_usd=cap,
       debt_term=years,annual_debt_usd=debt,annual_revenue_usd=income,
       annual_cash_opex_usd=op,annual_gap_usd=gap,
       annual_cash_surplus_usd=income-op-debt)

def main():
    cases=[case("25pct pipes 20-year debt",.25,20),
           case("50pct pipes 20-year debt",.50,20),
           case("100pct pipes 20-year debt",1.0,20),
           case("100pct pipes 40-year debt",1.0,40)]
    with open(os.path.join(OUT,"maui_enterprise_scenarios_v09.csv"),"w",newline="") as f:
        w=csv.DictWriter(f,cases[0].keys());w.writeheader();w.writerows(cases)
    with open(os.path.join(OUT,"maui_enterprise_cashflow_2027_2046_v09.csv"),"w",newline="") as f:
        keys=["scenario","year","revenue_usd","cash_opex_usd","annual_debt_usd","net_usd","cumulative_usd"]
        w=csv.DictWriter(f,keys);w.writeheader()
        for c in cases:
            for i in range(20):
                w.writerow(dict(scenario=c["scenario"],year=2027+i,
                   revenue_usd=round(c["annual_revenue_usd"]),cash_opex_usd=round(c["annual_cash_opex_usd"]),
                   annual_debt_usd=round(c["annual_debt_usd"]),
                   net_usd=round(c["annual_cash_surplus_usd"]),
                   cumulative_usd=round((i+1)*c["annual_cash_surplus_usd"])))
    for c in cases:
        print(c["scenario"],f'CAPEX={c["capex_usd"]/1e9:.3f}B',
              f'DEBT={c["annual_debt_usd"]/1e6:.1f}M/y',
              f'GAP={c["annual_gap_usd"]/1e6:.1f}M/y')
if __name__=="__main__": main()
