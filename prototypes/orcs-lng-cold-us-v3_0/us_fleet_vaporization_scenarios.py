"""ORCS US LNG fleet-wide cold scenario. Site counts/tonnes are ASSUMPTIONS, not PHMSA measured vaporization."""
import json
PHMSA_IN_SERVICE_2025=186
KWH_THERMAL_PER_TONNE=830/3.6
CASES=[
 {"case":"low","active_vaporizers":25,"tonnes_vaporized_per_site_y":25000},
 {"case":"mid","active_vaporizers":75,"tonnes_vaporized_per_site_y":50000},
 {"case":"high","active_vaporizers":150,"tonnes_vaporized_per_site_y":100000}
]
def project(active_vaporizers,tonnes_vaporized_per_site_y, electric_share=0.10,cooling_share=0.50,
            cooling_useful_fraction=0.65,reference_cop=4,edge_it_mw=1,pue=1.2,battery_hours=4,battery_usable_fraction=0.8):
    assert 0<=active_vaporizers<=PHMSA_IN_SERVICE_2025
    assert tonnes_vaporized_per_site_y>=0
    assert 0<=electric_share<=1 and 0<=cooling_share<=1 and electric_share+cooling_share<=1
    annual_tonnes=active_vaporizers*tonnes_vaporized_per_site_y
    cold_gwh=annual_tonnes*KWH_THERMAL_PER_TONNE/1000000
    generated_gwh=cold_gwh*electric_share
    cooling_avoid_gwh=cold_gwh*cooling_share*cooling_useful_fraction/reference_cop
    battery_mwh=active_vaporizers*edge_it_mw*pue*battery_hours/battery_usable_fraction
    return {"hypothetical_active_sites":active_vaporizers,
       "national_phmsa_site_ceiling":PHMSA_IN_SERVICE_2025,
       "scenario_lng_vaporized_mt_y":round(annual_tonnes/1000000,3),
       "gross_available_cold_thermal_gwh_y":round(cold_gwh,1),
       "assumed_generated_electricity_gwh_y":round(generated_gwh,1),
       "assumed_chiller_electricity_avoided_gwh_y":round(cooling_avoid_gwh,1),
       "combined_electric_benefit_gwh_y":round(generated_gwh+cooling_avoid_gwh,1),
       "combined_annual_average_mw":round((generated_gwh+cooling_avoid_gwh)/8.76,2),
       "resilience_battery_nameplate_mwh":round(battery_mwh),
       "battery_delivered_hours":battery_hours,
       "note":"Cold-duty annual energy not guaranteed firm year-round; BESS MW/MWh is STORAGE, not new generation."}
if __name__=="__main__":
 print(json.dumps([dict(case=x["case"],**project(x["active_vaporizers"],x["tonnes_vaporized_per_site_y"])) for x in CASES],indent=2))
