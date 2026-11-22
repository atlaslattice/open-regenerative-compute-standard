"""ORCS v2.0a capacity-and-chemistry scenario. Never interpret as real mined output."""
import json
MGD_TO_M3_DAY=3785.411784
CONCENTRATION_MG_L={"Mg":1350,"K":390,"Br":67,"Ca":410,"SO4":2700,"Na":10500,"Cl":19000}
SITES=[("Carlsbad CA",50,"operating"),("Tampa Bay FL",25,"operating"),("Santa Barbara CA",3,"operating"),("Harbor Island TX",100,"proposed"),("Doheny CA",5,"proposed"),("Monterey CA",4.8,"proposed"),("Laguna Madre TX",5,"proposed")]
PRICES_USD_T={"gypsum":[35,65],"MgO":[250,500],"K2O":[600,1200],"Br":[3000,3000],"NaCl":[35,75]}
IMPORTS_TPY={"gypsum":6800000,"MgO":640000,"K2O":5600000,"Br":None,"NaCl":None}
def screen(include_proposed=False,utilization=0.9,water_recovery=0.5,constituent_capture=0.5):
    assert 0<=utilization<=1 and 0<water_recovery<1 and 0<=constituent_capture<=1
    facilities=[s for s in SITES if include_proposed or s[2]=="operating"]
    capacity=sum(s[1] for s in facilities)
    freshwater_m3=capacity*MGD_TO_M3_DAY*365*utilization
    seawater_m3=freshwater_m3/water_recovery
    brine_m3=seawater_m3-freshwater_m3
    ions={k:seawater_m3*v/1e6 for k,v in CONCENTRATION_MG_L.items()}
    physical={"gypsum":min(ions["Ca"]*172.171/40.078,ions["SO4"]*172.171/96.06),
              "MgO":ions["Mg"]*40.304/24.305,
              "K2O":ions["K"]*94.196/(2*39.0983),"Br":ions["Br"],
              "NaCl":min(ions["Na"]*58.44/22.99,ions["Cl"]*58.44/35.45)}
    value=[sum(physical[k]*constituent_capture*PRICES_USD_T[k][j] for k in physical) for j in (0,1)]
    return {"sites":facilities,"seawater_product_nameplate_mgd":capacity,
       "hypothetical_annual_seawater_intake_m3":round(seawater_m3),
       "hypothetical_annual_reject_brine_m3":round(brine_m3),
       "gross_chemical_equivalent_tpy":{k:round(v) for k,v in physical.items()},
       "hypothetical_captured_equivalent_tpy":{k:round(v*constituent_capture) for k,v in physical.items()},
       "reference_gross_value_usd_range":[round(v) for v in value],
       "gross_imports_tpy":IMPORTS_TPY,
       "actual_mineral_recovery":"UNKNOWN","actual_revenue":"UNKNOWN",
       "prices_status":"USGS 2025 BR & POTASH UNIT VALUES, OTHER PRICES UNVERIFIED ILLUSTRATIVE"}
if __name__=="__main__":
 print(json.dumps({"operating":screen(),"operating_plus_proposed":screen(include_proposed=True)},indent=2))
