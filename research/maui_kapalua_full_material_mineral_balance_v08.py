#!/usr/bin/env python3
"""Atlas Lattice Maui v0.8 resort recovery and independent seawater mineral scenario.

All default inputs are hypothetical EXCEPT Marriott-published water footprint,
and representative USGS seawater chemistry / literature-derived conversion ratios.
No operator data, permit, revenue or capture/production is verified.
Python 3.9+, standard library only.
Run: python maui_kapalua_resource_recovery_v08.py
     python maui_kapalua_resource_recovery_v08.py --all-food 410 --saline-mgd 0
     python maui_kapalua_resource_recovery_v08.py --occupancy 0.8 --compost-yield 0.35
"""
from __future__ import annotations
import argparse
import json

DAYS=365
GAL_M3=0.003785411784
ROOMS=468
WATER_L_ROOMNIGHT=1962.08

# Representative seawater, USGS circ1262. Concentrations mg/L == g/m3.
SEAWATER_MG_L = {
    "Na":10500, "Cl":19000, "SO4":2700, "Mg":1350, "Ca":410,
    "K":390, "HCO3":142, "Br":67, "B":4.6, "Sr":8.0, "Li":0.18
}
# Literature-derived compost nutrient masses for FOOD input only, kg / wet tonne food input.
FOOD_COMPOST_NPK_KG_PER_WET_INPUT_TONNE={"N":9.91, "P":1.41, "K":2.78}
MW={"Ca":40.078, "gypsum":172.17, "calcite":100.087,
    "Mg":24.305, "MgOH2":58.3197, "K":39.0983, "KCl":74.5513,
    "Na":22.989769, "NaCl":58.44277, "P":30.973762,
    "N":14.0067, "struvite":245.41}

def simulate(rooms=468, occupancy=0.72, hotel_waste_kg_roomnight=2.5,
             food_kg_roomnight=0.9, garden_waste_t=100,
             compost_yield=0.52, all_food=None, wastewater_fraction=0.75,
             nutrient_N_mg_L=30, nutrient_P_mg_L=5,
             N_recovery_frac=0.50, P_struvite_frac=0.60,
             reuse_fraction=0.25, saline_mgd=5, ro_recovery=0.45,
             ro_kwh_m3=3.5, saline_tds_g_L=35, product_tds_g_L=0.5,
             energy_kwh_per_m3_brine_zld=10,
             electricity_usd_kwh=0.20):
    x=locals()
    for k,v in x.items():
        if v is not None and isinstance(v,(int,float)) and v<0:raise ValueError(f"{k} must be nonnegative")
    for k in ("occupancy","compost_yield","wastewater_fraction","N_recovery_frac",
              "P_struvite_frac","reuse_fraction"):
        if not 0<=x[k]<=1:raise ValueError(f"{k} must be in [0,1]")
    if rooms<=0 or food_kg_roomnight>hotel_waste_kg_roomnight:raise ValueError("rooms positive and food subset of hotel waste")
    if saline_mgd and not 0<ro_recovery<1:raise ValueError("RO recovery must be in (0,1)")
    nights=rooms*occupancy*DAYS
    hotel_waste=nights*hotel_waste_kg_roomnight/1000
    food=nights*food_kg_roomnight/1000
    garden=garden_waste_t
    if all_food is not None:
        # Independent user sensitivity case, not Marriott's modeled stream composition.
        food=float(all_food);garden=0.0
        hotel_waste=food

    other=hotel_waste-food
    fixed_dry={"paper_cardboard":70.0,"glass":45.0,"plastic":40.0,
               "metal":14.0,"textiles":10.0}
    if all_food is not None:
        fixed_dry={k:0.0 for k in fixed_dry}
    residual=other-sum(fixed_dry.values())
    if residual < -1e-7:
        raise ValueError("Hotel nonfood waste cannot fit default example dry fractions. Increase hotel waste/occupancy or use original defaults.")
    dry_recovery={"paper_cardboard":0.85,"glass":0.90,"plastic":0.60,
                  "metal":0.90,"textiles":0.0,"mixed_residual":0.0}
    dry_input=dict(fixed_dry,mixed_residual=max(residual,0))
    recovered={k:dry_input[k]*dry_recovery[k] for k in dry_input}
    compost_input=food+garden
    compost=compost_input*compost_yield
    emitted_water_CO2_process=compost_input-compost
    recover_dry=sum(recovered.values())
    reject_dry=sum(dry_input.values())-recover_dry
    total=hotel_waste+garden
    direct_recovery=compost+recover_dry
    assert abs(total-(direct_recovery+reject_dry+emitted_water_CO2_process))<1e-5

    food_npk={key:val*food/1000 for key,val in FOOD_COMPOST_NPK_KG_PER_WET_INPUT_TONNE.items()}
    # THIS IS A PARALLEL route, not stacked onto full composting of same food mass.
    # EBMUD wet tonnes food: ~75–135 m3 methane / WET METRIC TONNE,
    # highly variable; thermal conversion at approx 9.94 kWh/m3 CH4.
    methane_low=food*75
    methane_high=food*135
    elec_MWh_low=methane_low*9.94*0.30/1000
    elec_MWh_high=methane_high*9.94*0.35/1000

    water_m3_y=nights*WATER_L_ROOMNIGHT/1000
    wastewater_m3_y=water_m3_y*wastewater_fraction
    # mg/L = g/m3, tonnes = [m3 * g/m3]/1e6
    eff_N_t=wastewater_m3_y*nutrient_N_mg_L/1e6
    eff_P_t=wastewater_m3_y*nutrient_P_mg_L/1e6
    recovered_N=eff_N_t*N_recovery_frac
    P_into_struvite=eff_P_t*P_struvite_frac
    struvite=P_into_struvite*MW["struvite"]/MW["P"]
    N_in_struvite=struvite*MW["N"]/MW["struvite"]
    Mg_in_struvite=struvite*MW["Mg"]/MW["struvite"]
    if N_in_struvite>recovered_N+1e-9:raise ValueError("Struvite N larger than recovered total N; adjust recovery assumptions")
    ww={
      "water_footprint_gallons_y_PROXY":water_m3_y/GAL_M3,
      "nonpotable_reuse_gallons_y_UPPER_SCENARIO":water_m3_y/GAL_M3*reuse_fraction,
      "wastewater_m3_y_CONDITIONAL":wastewater_m3_y,
      "incoming_N_t_y_ASSUMED":eff_N_t,
      "incoming_P_t_y_ASSUMED":eff_P_t,
      "recovered_total_N_t_y_IF_FEASIBLE":recovered_N,
      "recovered_P_t_y_in_struvite_IF_FEASIBLE":P_into_struvite,
      "struvite_t_y_STOICHIOMETRIC_SCENARIO":struvite,
      "struvite_N_t_y":N_in_struvite,
      "struvite_Mg_t_y":Mg_in_struvite,
      "other_recovered_N_t_y_after_struvite":recovered_N-N_in_struvite,
      "warning":"Hotel water footprint is NOT a measured wastewater flow; N/P concentrations and nutrient forms are assumed; Mg may require external supply."
    }

    saline={}
    if saline_mgd>0:
        prod_m3_d=saline_mgd*1e6*GAL_M3
        feed_m3_d=prod_m3_d/ro_recovery
        brine_m3_d=feed_m3_d-prod_m3_d
        input_ions_t_y={k:feed_m3_d*DAYS*c/1e6 for k,c in SEAWATER_MG_L.items()}
        total_salt_input=feed_m3_d*DAYS*saline_tds_g_L/1000
        total_salt_product=prod_m3_d*DAYS*product_tds_g_L/1000
        saline={
          "warning":"Separate hypothetical island water plant, not resort wastewater or a permitted Kapalua facility. Element masses are NOT saleable product, not simultaneously recoverable.",
          "freshwater_product_MGD":saline_mgd,
          "seawater_feed_m3_day":feed_m3_d,
          "concentrate_m3_day":brine_m3_d,
          "reference_RO_GWh_year":prod_m3_d*ro_kwh_m3*DAYS/1e6,
          "ZLD_additional_GWh_year_STRESS_TEST":brine_m3_d*energy_kwh_per_m3_brine_zld*DAYS/1e6,
          "ZLD_energy_only_cost_usd_y_STRESS_TEST":brine_m3_d*energy_kwh_per_m3_brine_zld*DAYS*electricity_usd_kwh,
          "feed_total_salts_t_year":total_salt_input,
          "concentrate_salts_t_year_APPROX":total_salt_input-total_salt_product,
          "element_ion_feed_inventory_t_year":input_ions_t_y,
          "stoichiometric_exclusive_alternative_ceiling_t_year":{
            "gypsum_Ca_limited":input_ions_t_y["Ca"]*MW["gypsum"]/MW["Ca"],
            "calcium_carbonate_Ca_limited_INSTEAD_OF_GYPSUM":input_ions_t_y["Ca"]*MW["calcite"]/MW["Ca"],
            "magnesium_hydroxide_Mg_limited":input_ions_t_y["Mg"]*MW["MgOH2"]/MW["Mg"],
            "potassium_chloride_K_limited":input_ions_t_y["K"]*MW["KCl"]/MW["K"],
            "sodium_chloride_Na_limited":input_ions_t_y["Na"]*MW["NaCl"]/MW["Na"],
          }
        }
    return {
      "version":"v0.8",
      "status":"SCENARIO/NON-CANON/ZERO REALIZED CREDIT",
      "hotel":{
        "roomnights_y":nights,
        "operating_waste_input_t_y":hotel_waste,
        "food_within_operating_t_y":food,
        "additional_landscape_t_y":garden,
        "dry_input_t_y":dry_input,
        "TOTAL_SOLID_INPUT_t_y":total,
        "compost_feed_t_y":compost_input,
        "compost_finished_wet_t_y":compost,
        "dry_recovered_products_t_y":recovered,
        "direct_recovered_total_t_y":direct_recovery,
        "reject_dry_t_y":reject_dry,
        "organic_water_gases_mass_loss_t_y_not_zero_emissions":emitted_water_CO2_process,
        "mass_balance_residual_t_y":total-direct_recovery-reject_dry-emitted_water_CO2_process,
        "food_compost_NPK_t_elemental_y_LITERATURE_MODEL":food_npk,
        "alternate_FOOD_ONLY_AD_route_NO_FULL_FOOD_COMPOST":{
          "methane_low_high_m3_y":[methane_low,methane_high],
          "gross_electricity_MWh_y_before_parasitics":[elec_MWh_low,elec_MWh_high],
          "digestate_quantity":"UNKNOWN: quantify by digestion moisture and solids assay"
        },
        "important":"Food fraction is SUBSET of hotel mixed solid waste. Do not add all hotel waste as food or co-credit full compost+AD energy for identical mass."
      },
      "conditional_resort_wastewater":ww,
      "separate_regional_desal_seawater_reference":saline,
    }

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--occupancy",type=float,default=.72)
    p.add_argument("--compost-yield",type=float,default=.52)
    p.add_argument("--all-food",type=float,default=None)
    p.add_argument("--saline-mgd",type=float,default=5)
    p.add_argument("--ro-recovery",type=float,default=.45)
    p.add_argument("--zld-sec",type=float,default=10)
    args=p.parse_args()
    r=simulate(occupancy=args.occupancy,compost_yield=args.compost_yield,
               all_food=args.all_food,saline_mgd=args.saline_mgd,
               ro_recovery=args.ro_recovery,
               energy_kwh_per_m3_brine_zld=args.zld_sec)
    print(json.dumps(r,indent=2))
