"""US LNG regas cold energy scenario only: annual LNG imports, not rated import capacity."""
import json
EIA_2025_BCF = 13.786
GAS_BCF_PER_MILLION_TONNES_LNG = 48.7
COLD_KJ_PER_KG = 830
def calculate(lng_bcf=EIA_2025_BCF, electric_fraction=0.10, cooling_fraction=0.50,
              useful_cooling_fraction=0.65, displaced_chiller_cop=4, battery_hours=4,
              resilience_it_mw=1, data_center_pue=1.2):
    if not(0<=electric_fraction<=1 and 0<=cooling_fraction<=1 and electric_fraction+cooling_fraction<=1):
        raise ValueError("cold allocation fractions total >1")
    if not (0<=useful_cooling_fraction<=1 and displaced_chiller_cop>0 and battery_hours>=0 and resilience_it_mw>=0 and data_center_pue>=1):
        raise ValueError("bad assumption")
    mt = lng_bcf/GAS_BCF_PER_MILLION_TONNES_LNG
    # [Mt]*[kWh/t] = GWh; 830kJ/kg = 230.56 kWh per tonne.
    cold_gwh = mt*COLD_KJ_PER_KG/3.6
    power_gwh=cold_gwh*electric_fraction
    cooling_thermal_gwh=cold_gwh*cooling_fraction*useful_cooling_fraction
    cooling_electricity_avoided_gwh=cooling_thermal_gwh/displaced_chiller_cop
    battery_mwh=resilience_it_mw*data_center_pue*battery_hours
    return {"gas_import_bcf_y":round(lng_bcf,3),
       "lng_mass_million_tonnes_y":round(mt,6),
       "cold_thermal_energy_gwh_y":round(cold_gwh,3),
       "cold_thermal_average_mw":round(cold_gwh/8.76,3),
       "scenario_electric_generation_gwh_y":round(power_gwh,3),
       "scenario_generation_average_mw":round(power_gwh/8.76,3),
       "scenario_cooling_thermal_delivered_gwh_y":round(cooling_thermal_gwh,3),
       "scenario_cooling_electricity_avoided_gwh_y":round(cooling_electricity_avoided_gwh,3),
       "scenario_total_electricity_generated_plus_avoided_gwh_y":round(power_gwh+cooling_electricity_avoided_gwh,3),
       "site_resilience_battery_nameplate_mwh":round(battery_mwh,3),
       "battery_energy_generation_note":"Battery stores electricity; does not generate annual net new energy",
       "classification":"SCENARIO_NOT_MEASURED_US_SITE_POWER_OR_COOLING"}
if __name__=="__main__":
 print(json.dumps({"mid":calculate(),"electricity_only_5pct":calculate(electric_fraction=.05,cooling_fraction=0),
 "electricity_only_20pct":calculate(electric_fraction=.2,cooling_fraction=0),
 "cooling_only_50pct":calculate(electric_fraction=0,cooling_fraction=.5),
 "cooling_only_100pct":calculate(electric_fraction=0,cooling_fraction=1)},indent=2))
