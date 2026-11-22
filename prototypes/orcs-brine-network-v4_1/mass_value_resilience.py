#!/usr/bin/env python3
"""ORCS v4.1 seawater-brine minerals and resilience scenario model.
Uses reference seawater chemistry, not site assays. Standard library only.
All prices, extraction efficiencies, sales, OPEX, CAPEX, grid and disaster inputs are assumptions.
This is NOT mining feasibility, an investment guarantee or qualified emergency-power software.
"""
from math import isclose
import json

GALLON_M3=0.003785411784
CHEM_MG_L={"Na":10500,"Cl":19000,"Mg":1350,"Ca":410,"SO4":2700,"K":390,"Br":67,"Li":0.17}
PRICES={"NaCl":35,"MgOH2":350,"KCl":300,"Br2":3000,"gypsum":35} # UNVERIFIED $/t plant-gate assumptions

def model(mgd=100,util=.9,water_recovery=.5,ion_captured=.5,portion_sold=.6,
          opex_m3=1.5,freight_m3=.4,capex=750e6,rate=.08,life=20):
    assert mgd>0 and 0<water_recovery<1 and 0<=ion_captured<=1 and 0<=portion_sold<=1
    water=mgd*1e6*GALLON_M3*365*util
    feed=water/water_recovery
    brine=feed-water
    # 1 mg/L equals 1 g/m3 = 1e-6 metric tonnes/m3
    i={n:feed*c/1e6 for n,c in CHEM_MG_L.items()}
    equiv={
      "NaCl":min(i["Na"]*58.443/22.9898,i["Cl"]*58.443/35.453),
      "MgOH2":i["Mg"]*58.3197/24.305,
      "MgO":i["Mg"]*40.3044/24.305,
      "KCl":i["K"]*74.5513/39.0983,
      "K2Oeq":i["K"]*94.196/(2*39.0983),
      "Br2":i["Br"],
      "gypsum":min(i["Ca"]*172.171/40.078,i["SO4"]*172.171/96.06),
      "LCE":i["Li"]*73.89/(2*6.94),
    }
    # Product equivalents MgO and MgOH2 (also K2Oeq/KCl) are alternative grades, NOT additive.
    gross=sum(equiv[k]*ion_captured*v for k,v in PRICES.items())
    crf=rate*(1+rate)**life/((1+rate)**life-1)
    rev=gross*portion_sold
    costs=brine*(opex_m3+freight_m3)+capex*crf
    return {
      "freshwater_MGD":mgd,"reject_million_m3_y":round(brine/1e6,3),
      "feed_million_m3_y":round(feed/1e6,3),
      "feed_ions_t_y":{k:round(v) for k,v in i.items()},
      "product_theoretical_maximum_t_y":{k:round(v) for k,v in equiv.items()},
      "captured_product_scenario_t_y":{k:round(equiv[k]*ion_captured) for k in PRICES},
      "potential_price_times_capture_million_usd":round(gross/1e6,2),
      "sold_product_revenue_million_usd":round(rev/1e6,2),
      "variable_processing_cost_million_usd":round(opex_m3*brine/1e6,2),
      "freight_residual_cost_million_usd":round(freight_m3*brine/1e6,2),
      "annual_capex_charge_million_usd":round(capex*crf/1e6,2),
      "scenario_profit_before_tax_million_usd":round((rev-costs)/1e6,2),
      "min_sale_fraction_to_break_even":round(costs/gross,3),
      "WARNING":"No site output or prices measured; 50% simultaneous selective salt/mineral capture and OPEX may be physically unattainable; all amounts are ceilings/sensitivities, NOT forecast output, import displacement, or profit."
    }

def resilience(mgd=100,critical_fraction=.15,kwh_per_m3=3.5,days=3,
               usable_battery=.8,firm_backup_mw=0):
    emergency_m3_d=mgd*1e6*GALLON_M3*critical_fraction
    mw=emergency_m3_d*kwh_per_m3/24/1000
    need_mwh=mw*days*24
    batt=max(0,need_mwh-firm_backup_mw*days*24)/usable_battery
    return {"critical_fraction":critical_fraction,"required_critical_water_m3":round(emergency_m3_d*days),
            "electricity_MW":round(mw,2),"three_day_electricity_MWh":round(need_mwh,1),
            "nameplate_BESS_MWh":round(batt,1),
            "warning":"Power-only simplified. Flooded intake, unusable distribution, fuel, battery power rating, pretreatment, contamination, chlorine and repairs may prevent operation."}

def test():
    a=model(78)
    assert isclose(a["reject_million_m3_y"],96.994,abs_tol=.001)
    assert 5_100_000<a["product_theoretical_maximum_t_y"]["NaCl"]<5_200_000
    assert 12_900<a["product_theoretical_maximum_t_y"]["Br2"]<13_100
    assert isclose(model()["reject_million_m3_y"],124.351,abs_tol=.001)
    assert isclose(resilience()["electricity_MW"],8.28,abs_tol=.02)

if __name__=="__main__":
    test()
    print(json.dumps({
    "us_named_operating_seawater_subset_78MGD":model(78),
    "100MGD_25pct_capture_60pct_sales":model(ion_captured=.25,opex_m3=2),
    "100MGD_50pct_capture_60pct_sales":model(),
    "100MGD_50pct_capture_100pct_sales_optimistic":model(portion_sold=1),
    "100MGD_75pct_capture_100pct_sales_complex":model(ion_captured=.75,portion_sold=1,opex_m3=4,freight_m3=1,capex=2e9),
    "1BGD_future_capacity_only_not_actual":model(mgd=1000,portion_sold=.25,opex_m3=4,capex=6e9),
    "100MGD_site_72h_15pct_critical_water":resilience(),
    "100MGD_site_72h_15pct_critical_water_5MW_firm_backup":resilience(firm_backup_mw=5)},indent=2))
