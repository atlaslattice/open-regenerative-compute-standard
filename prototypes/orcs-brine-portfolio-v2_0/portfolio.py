"""Capacity-only seawater brine mineral screen. No recovered output claims."""
import json

MGD_TO_M3_DAY = 3785.411784
CONC = {"Mg":1350,"K":390,"Br":67,"Ca":410,"SO4":2700,"Na":10500,"Cl":19000}
SEAWATER_SITES = [
 ("Carlsbad CA",50,"operating"),("Tampa Bay FL",25,"operating"),
 ("Santa Barbara CA",3,"operating"),("Harbor Island TX",100,"proposed"),
 ("Doheny CA",5,"proposed"),("Monterey CA",4.8,"proposed"),
 ("Laguna Madre TX",5,"proposed")
]
PRICES = {"gypsum":[35,65],"MgO":[250,500],"K2O":[350,700],"Br":[3000,3000],"NaCl":[35,75]}
def portfolio(utilization=0.9,water_recovery=0.5,chem_capture=0.5,include_proposed=False):
    assert 0<=utilization<=1 and 0<water_recovery<1 and 0<=chem_capture<=1
    sites=[s for s in SEAWATER_SITES if include_proposed or s[2]=="operating"]
    capacity=sum(s[1] for s in sites)
    freshwater=capacity*MGD_TO_M3_DAY*365*utilization
    seawater_intake=freshwater/water_recovery
    reject=seawater_intake-freshwater
    ions={k:seawater_intake*v/1e6 for k,v in CONC.items()}
    gypsum=min(ions["Ca"]*172.171/40.078,ions["SO4"]*172.171/96.06)
    nacl=min(ions["Na"]*58.44/22.99,ions["Cl"]*58.44/35.45)
    physical={"gypsum":gypsum,"MgO":ions["Mg"]*40.304/24.305,
       "K2O":ions["K"]*94.196/(2*39.0983),"Br":ions["Br"],"NaCl":nacl}
    return {"sites":sites,"product_water_nameplate_mgd":capacity,
      "scenario_intake_m3_y":round(seawater_intake),"scenario_brine_m3_y":round(reject),
      "scenario_gross_chemical_content_t_y":{k:round(v) for k,v in physical.items()},
      "scenario_extracted_content_t_y":{k:round(v*chem_capture) for k,v in physical.items()},
      "scenario_gross_reference_value_usd_low_high":[
        round(sum(physical[k]*chem_capture*PRICES[k][j] for k in physical)) for j in (0,1)],
      "actual_output":"UNKNOWN","actual_revenue":"UNKNOWN","pricing":"SCENARIO_ONLY_EXCEPT_USGS_BROMINE_2025_IMPORT_UNIT_VALUE"}
if __name__=="__main__":
 print(json.dumps({"operating_only":portfolio(),"including_proposed":portfolio(include_proposed=True)},indent=2))
