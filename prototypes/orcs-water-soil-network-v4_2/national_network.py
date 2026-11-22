#!/usr/bin/env python3
"""ORCS v4.2 national wastewater, PolyPod and aquifer-offset scenario audit.
NO verified vendor quote or full-flow performance; EPA municipal inventory as published.
Values do not include remediation costs, pipe costs, freshwater environmental flows or groundwater rights.
"""
import json, math
EPA_POTWS=17544
EPA_MUNICIPAL_BGD=34.0
POLYPOD_NAMEPLATE_MGD=10
USER_POLYPOD_PRICE_USD=110000
USGS_2015_IRRIGATION_GROUNDWATER_BGD=57.2
HISTORIC_EPA_REUSED_BGD=2.2 # historic 2019 draft, not measured 2026
MGD_PER_BGD=1000
KG_PER_GAL=3.785411784 # assumes freshwater density kg/L
D_H_ATOMIC=.000156
D_ATOMIC=2.014102
H_ATOMIC=1.007825
O_ATOMIC=15.999
M_D2O=2*D_ATOMIC+O_ATOMIC

def national_units(volume_bgd=EPA_MUNICIPAL_BGD,potws=EPA_POTWS,
                   rated_mgd=POLYPOD_NAMEPLATE_MGD,price=USER_POLYPOD_PRICE_USD,
                   duty_factor=.8,extra_per_site=0):
    assert 0<duty_factor<=1 and extra_per_site>=0
    flow_floor=math.ceil(volume_bgd*1000/(rated_mgd*duty_factor))
    # Since site flows are unknown, one unit per plant + enough additional for national flow is a lower bound;
    # true sum_i ceil(site_flow_i / rated_effective) CAN BE GREATER.
    site_floor=potws*(1+extra_per_site)
    lower_bound=max(flow_floor,site_floor)
    return {"potws":potws,"volume_bgd":volume_bgd,
            "nominal_nameplate_mgd_per_pod":rated_mgd,"duty_factor_scenario":duty_factor,
            "aggregate_flow_unit_floor":flow_floor,"site_coverage_floor":site_floor,
            "combined_floor_not_actual_site_schedule":lower_bound,
            "pod_equipment_only_usd":lower_bound*price,
            "unverified":"Actual site-by-site size and operating hours; quote; capture spectrum; effluent guarantees; electricity; residue service; regulatory certification."}

def reuse(target_fraction=.25, groundwater_substitution_fraction=.5,
          current_reuse_bgd=HISTORIC_EPA_REUSED_BGD):
    gross_target=EPA_MUNICIPAL_BGD*target_fraction
    incremental=max(0,gross_target-current_reuse_bgd)
    net_gw=incremental*groundwater_substitution_fraction
    return {"national_wastewater_bgd":EPA_MUNICIPAL_BGD,
            "target_total_reuse_bgd":round(gross_target,3),
            "historic_current_reuse_bgd_unverified_2026":current_reuse_bgd,
            "gross_incremental_new_reuse_bgd":round(incremental,3),
            "fraction_substituting_groundwater":groundwater_substitution_fraction,
            "additional_irrigation_groundwater_withdrawals_avoided_bgd":round(net_gw,3),
            "2015_usgs_irrigation_groundwater_bgd":USGS_2015_IRRIGATION_GROUNDWATER_BGD,
            "percentage_of_2015_groundwater_withdrawal":round(100*net_gw/USGS_2015_IRRIGATION_GROUNDWATER_BGD,2),
            "annual_new_groundwater_avoided_trillion_gallons":round(net_gw*365/1000,3),
            "caveat":"Historic baselines, discharge permit/ecological-flow obligations, distance to farms, salinity, contaminants, rights and seasonal demand unknown."}

def deuterium_in_water(flow_mgd=100,days=365,usable_fraction=0):
    # D/H is atomic molar ratio; D mass fraction in natural H2O ~ 34.6 ppm.
    d_fraction=(2*D_H_ATOMIC*D_ATOMIC)/(2*(1-D_H_ATOMIC)*H_ATOMIC+2*D_H_ATOMIC*D_ATOMIC+O_ATOMIC)
    water_kg=flow_mgd*1e6*days*KG_PER_GAL
    d_t=water_kg*d_fraction/1000
    return {"water_throughput_mgd":flow_mgd,
            "water_million_m3_y":round(water_kg/1e9,3),
            "D_natural_mass_fraction_ppm":round(d_fraction*1e6,2),
            "D_atoms_gross_t_y_not_recovered":round(d_t),
            "theoretical_heavy_water_equivalent_t_y_not_recovered":round(d_t*M_D2O/(2*D_ATOMIC)),
            "hypothetical_usable_deuterium_t_y":round(d_t*usable_fraction,5),
            "disclaimer":"Feed-water isotope inventory, NOT deuterium recovered in RO or wastewater polishing. Isotope separation/energy/offtake unknown; regulated industrial operations require specific controls."}

def harbor_reconciliation(fresh_mgd=100, discharge_mgd=191.2, existing_standard_util=.9):
    # MAX project intake is finished + quoted total discharge, not verified all high-salinity concentrate.
    # Compare different intake bases, and flag RO-brine vs pretreatment stream.
    old_intake=fresh_mgd+discharge_mgd
    standard_intake=fresh_mgd/.5
    factor=(old_intake*365)/(standard_intake*365*existing_standard_util)
    return {"prior_harbor_freshwater_mgd":fresh_mgd,
            "prior_project_mixed_discharge_mgd":discharge_mgd,
            "prior_implied_full_design_intake_mgd":old_intake,
            "new_100mgd_50percent_recovery_intake_mgd":standard_intake,
            "volume_plus_utilization_factor":round(factor,3),
            "prior_gypsum_t_y":733000,"later_standard_gypsum_t_y":438000,
            "theoretical_gypsum_ratio":round(733000/438000,3),
            "technical_veto":"191.2MGD reported discharge may mix RO reject and other pretreatment/outfalls. Neither all-discharge seawater minerals nor all-discharge hot concentrated brine is validated."}

def delivered_import_value(product_t,like_grade_import_gap_t,domestic_delivered_import_usd_t,
                           domestic_substitute_usd_t,actual_incremental_qualified_t=None):
    q=product_t if actual_incremental_qualified_t is None else actual_incremental_qualified_t
    eligible=max(0,min(q,like_grade_import_gap_t))
    return {
        "qualified_import_replacement_t":round(eligible),
        "gross_import_invoice_avoided_usd":round(eligible*domestic_delivered_import_usd_t),
        "domestic_supplier_gross_invoice_usd":round(eligible*domestic_substitute_usd_t),
        "buyer_price_savings_usd":round(eligible*(domestic_delivered_import_usd_t-domestic_substitute_usd_t)),
        "warning":"Gross import bill avoided, domestic seller revenues and purchaser savings overlap: do NOT sum as three additive national gains. Record net foreign exchange, imported inputs, taxes, environmental/energy costs, transport and resilience loss separately."
    }

def audit():
    assert national_units(duty_factor=1)["aggregate_flow_unit_floor"]==3400
    assert national_units(duty_factor=1)["site_coverage_floor"]==17544
    assert national_units(duty_factor=1)["pod_equipment_only_usd"]==1929840000
    assert reuse()["percentage_of_2015_groundwater_withdrawal"]==5.51
    assert round(deuterium_in_water(100)["D_atoms_gross_t_y"])==round(4780) or abs(deuterium_in_water(100)["D_atoms_gross_t_y"]-4780)<25

if __name__=="__main__":
    audit()
    print(json.dumps({
       "polypod_nameplate_only":national_units(duty_factor=1),
       "polypod_80pct_dispatch_sensitivity":national_units(duty_factor=.8),
       "polypod_two_units_per_plant_floor":national_units(duty_factor=.8,extra_per_site=1),
       "reuse_10pct_target":reuse(.10),
       "reuse_25pct_target":reuse(.25),
       "reuse_50pct_target":reuse(.50),
       "d2o_100mgd_water_throughput":deuterium_in_water(100),
       "d2o_harbor_theoretical_291p2mgd":deuterium_in_water(291.2),
       "d2o_national_wastewater_theoretical":deuterium_in_water(34000),
       "harbor_comparison":harbor_reconciliation(),
       "not_additive_import_ledger_example":delivered_import_value(100000,640000,500,350)},indent=2))
