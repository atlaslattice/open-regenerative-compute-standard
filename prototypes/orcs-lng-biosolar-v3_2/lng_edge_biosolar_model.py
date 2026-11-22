"""ORCS v3.2: distinct energy ledgers for process AI, repurposed regas LNG cold, biosolar rooftop potential.
All example parameters are assumptions except NREL 2016 technical rooftop potential and UTS summer measured case.
"""
import json
M2_PER_ACRE=4046.8564224
SF_PER_M2=10.7639104167
# Cheniere operator CCL >25Mtpa, site >1000 acres; entire site != covered roof.
EXAMPLE_SITE={"lng_mtpa":25.0,"land_acres":1000}
def industrial_solar(lng_mtpa=25,roof_sqft_per_tpa=0.02,roof_suitable_fraction=.65,
                     watts_per_m2=180,solar_kwh_per_kw_y=1450,biosolar_gain=.111):
    assert lng_mtpa>0 and roof_sqft_per_tpa>=0 and 0<=roof_suitable_fraction<=1
    annual_tonnes=lng_mtpa*1e6
    roof_sqft=annual_tonnes*roof_sqft_per_tpa
    suitable_m2=roof_sqft/SF_PER_M2*roof_suitable_fraction
    kw=suitable_m2*watts_per_m2/1000
    pv_gwh=kw*solar_kwh_per_kw_y/1e6
    return {"assumed_roof_sqft":round(roof_sqft),"roof_sqft_per_annual_tonne_capacity":roof_sqft_per_tpa,
       "suitable_roof_m2":round(suitable_m2),"pv_mw_dc":round(kw/1000,3),
       "pv_generation_gwh_y":round(pv_gwh,3),
       "biosolar_pv_generation_gwh_y":round(pv_gwh*(1+biosolar_gain),3),
       "incremental_biosolar_gwh_y":round(pv_gwh*biosolar_gain,3)}
def national_biosolar(coverage_of_nrel_technical_potential=.10,uplift=.111):
    # NREL 2016 all-suitable technical potential, not existing installed PV fleet.
    nrel_twh=1432
    return {"roof_pv_baseline_twh_y":round(nrel_twh*coverage_of_nrel_technical_potential,3),
            "biosolar_increment_twh_y":round(nrel_twh*coverage_of_nrel_technical_potential*uplift,3),
            "note":"Do not apply the uplift twice. Does not account for biosolar roof structural/water/shading impacts."}
def process_ai(lng_mtpa=25,specific_energy_kwh_per_kg=.281,process_saving=.02,
               it_kw=100,it_util=.8,pue=1.2,grid_usd_kwh=.10):
    assert 0<=process_saving<=1
    process_gwh=lng_mtpa*1e9*specific_energy_kwh_per_kg/1e6
    savings_gwh=process_gwh*process_saving
    edge_gwh=it_kw*it_util*8760*pue/1e6
    return {"process_reference_gwh_y":round(process_gwh,1),
            "scenario_process_savings_gwh_y":round(savings_gwh,1),
            "example_edge_node_gwh_y":round(edge_gwh,3),
            "net_process_minus_local_it_gwh_y":round(savings_gwh-edge_gwh,1),
            "scenario_net_annual_electricity_value_usd":round((savings_gwh-edge_gwh)*1e6*grid_usd_kwh),
            "status":"MODELED_NOT_ATTAINED"}
def main():
    case={"site":EXAMPLE_SITE,"roof_0_01":industrial_solar(roof_sqft_per_tpa=.01),
          "roof_0_02":industrial_solar(roof_sqft_per_tpa=.02),
          "roof_0_05":industrial_solar(roof_sqft_per_tpa=.05),
          "process_1pct":process_ai(process_saving=.01),
          "process_2pct":process_ai(process_saving=.02),
          "process_5pct":process_ai(process_saving=.05),
          "national_10pct":national_biosolar(.1),
          "national_25pct":national_biosolar(.25),
          "national_100pct":national_biosolar(1)}
    print(json.dumps(case,indent=2))
if __name__=="__main__":main()
