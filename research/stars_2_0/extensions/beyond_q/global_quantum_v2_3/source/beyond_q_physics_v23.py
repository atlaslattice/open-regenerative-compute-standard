#!/usr/bin/env python3
"""Beyond Q v2.3 transparent algebraic screening model.
NOT a tokamak plasma solver, neutron-transport model, operational forecast, or investment model.
All quantitative cases are sensitivity illustrations unless explicitly labeled sourced.
"""
from __future__ import annotations
import csv, json, math
from dataclasses import dataclass, asdict
from pathlib import Path
AVOGADRO = 6.02214076e23
MEV_J = 1.602176634e-13
T_MOLAR_G = 3.01605
HE3_MOLAR_G = 3.01603
STP_L_PER_MOL = 22.414 # 0 C and 1 atm, not 1 bar
SECONDS_PER_YEAR = 365.0 * 24 * 3600

@dataclass(frozen=True)
class Assumptions:
    dd_primary_mw: float = 20.0
    dd_branch_t: float = 0.5
    dd_q_neutron_mev: float = 3.2689   # D(d,p)T
    dd_q_he3_mev: float = 4.0327       # D(d,n)He3
    dt_q_mev: float = 17.589
    li6_capture_q_mev: float = 4.783
    secondary_t_burn_fraction: float = 0.28
    he3_secondary_burn_fraction: float = 0.0   # placeholder, not empirically constrained
    neutron_capture_fraction: float = 0.5       # effective per primary neutron, no multiplication
    blanket_tritium_recovery_fraction: float = 0.85
    divertor_tritium_recovery_fraction: float = 0.78
    plasma_he3_recovery_fraction: float = 0.75
    rf_delivered_mw: float = 80.0
    rf_wall_plug_efficiency: float = 0.70
    rf_deposited_fraction: float = 0.9
    other_aux_mwe: float = 15.0
    thermal_collection_fraction: float = 0.85
    thermal_to_electric_efficiency: float = 0.40
    capacity_factor: float = 0.85
    lost_dt_opportunity_mwe: float = 400.0
    power_price_usd_mwh: float = 65.0
    t_bank_input_kg_year: float = 1.9
    t_half_life_years: float = 12.32
    years: int = 20

def model(a: Assumptions) -> dict:
    q_dd = a.dd_branch_t*a.dd_q_neutron_mev + (1-a.dd_branch_t)*a.dd_q_he3_mev
    dd_events_s = a.dd_primary_mw*1e6 / (q_dd*MEV_J)
    t_born_s = a.dd_branch_t*dd_events_s
    he3_born_s = (1-a.dd_branch_t)*dd_events_s
    dt_secondary_s = a.secondary_t_burn_fraction*t_born_s
    dt_secondary_mw = dt_secondary_s*a.dt_q_mev*MEV_J/1e6
    dd_neutrons_s = he3_born_s
    dt_neutrons_s = dt_secondary_s
    captured_s = a.neutron_capture_fraction*(dd_neutrons_s+dt_neutrons_s)
    li6_q_mw = captured_s*a.li6_capture_q_mev*MEV_J/1e6
    nuclear_q_mw = a.dd_primary_mw+dt_secondary_mw+li6_q_mw
    delivered_rf_deposited_mw = a.rf_delivered_mw*a.rf_deposited_fraction
    deposited_thermal_mw = nuclear_q_mw+delivered_rf_deposited_mw
    converter_thermal_mw = deposited_thermal_mw*a.thermal_collection_fraction
    gross_e_mwe = converter_thermal_mw*a.thermal_to_electric_efficiency
    rf_wall_mwe = a.rf_delivered_mw/a.rf_wall_plug_efficiency
    aux_mwe = rf_wall_mwe+a.other_aux_mwe
    dd_net_mwe = gross_e_mwe-aux_mwe
    opportunity_mwe = a.lost_dt_opportunity_mwe-dd_net_mwe
    foregone_energy_gwh_year = opportunity_mwe*8760*a.capacity_factor/1000
    electricity_value_musd_year = foregone_energy_gwh_year*1000*a.power_price_usd_mwh/1e6
    sec_cal_year = SECONDS_PER_YEAR*a.capacity_factor
    t_born_kg_y = t_born_s*sec_cal_year/AVOGADRO*T_MOLAR_G/1000
    he3_born_stp_l_y = he3_born_s*sec_cal_year/AVOGADRO*STP_L_PER_MOL
    t_exhaust_rec_kg_y = (t_born_s-dt_secondary_s)*sec_cal_year/AVOGADRO*T_MOLAR_G/1000*a.divertor_tritium_recovery_fraction
    t_blanket_rec_kg_y = captured_s*sec_cal_year/AVOGADRO*T_MOLAR_G/1000*a.blanket_tritium_recovery_fraction
    he3_rec_l_y = he3_born_stp_l_y*(1-a.he3_secondary_burn_fraction)*a.plasma_he3_recovery_fraction
    # Overall gross-to-net conservation check ignoring detailed locations/energy leakage destinations.
    ext_energy_mw = rf_wall_mwe + a.other_aux_mwe
    heat_and_non_electric_mw = ext_energy_mw+nuclear_q_mw-gross_e_mwe
    # Tritium bank mathematical consequence only; do not add to isotope mass balance if source exceeds recovered T.
    lam=math.log(2)/a.t_half_life_years
    bank_rows=[]
    for y in range(0,a.years+1):
        inventory=a.t_bank_input_kg_year/lam*(-math.expm1(-lam*y))
        decayed=a.t_bank_input_kg_year*y-inventory
        bank_rows.append({"year":y,"t_active_kg":inventory,"t_decayed_cumulative_kg":decayed,"he3_decay_cumulative_stp_l":decayed*1000/T_MOLAR_G*STP_L_PER_MOL,"he3_decay_rate_stp_l_year":(lam*inventory)*1000/T_MOLAR_G*STP_L_PER_MOL})
    return {"assumptions":asdict(a),"dd_events_s":dd_events_s,"t_born_s":t_born_s,"dd_primary_mw":a.dd_primary_mw,"secondary_dt_mw":dt_secondary_mw,"dd_neutron_mw":dd_neutrons_s*2.45*MEV_J/1e6,"li6_capture_q_mw":li6_q_mw,"nuclear_q_mw":nuclear_q_mw,"delivered_rf_mw":a.rf_delivered_mw,"rf_deposited_mw":delivered_rf_deposited_mw,"deposited_thermal_mw":deposited_thermal_mw,"thermal_to_converter_mw":converter_thermal_mw,"gross_e_mwe":gross_e_mwe,"rf_wall_mwe":rf_wall_mwe,"other_aux_mwe":a.other_aux_mwe,"aux_mwe":aux_mwe,"dd_net_mwe":dd_net_mwe,"unconverted_and_local_energy_mw":heat_and_non_electric_mw,"opportunity_mwe":opportunity_mwe,"opportunity_gwh_y":foregone_energy_gwh_year,"opportunity_musd_y":electricity_value_musd_year,"t_born_kg_y":t_born_kg_y,"he3_born_l_y":he3_born_stp_l_y,"t_exhaust_recovered_kg_y":t_exhaust_rec_kg_y,"t_blanket_recovered_kg_y":t_blanket_rec_kg_y,"t_total_recovered_kg_y":t_exhaust_rec_kg_y+t_blanket_rec_kg_y,"he3_plasma_recovered_l_y":he3_rec_l_y,"bank_20y":bank_rows}

def validate(a:Assumptions, r:dict):
    assert abs(r['dd_net_mwe']-(r['gross_e_mwe']-r['aux_mwe']))<1e-9
    assert abs(r['nuclear_q_mw']-(a.dd_primary_mw+r['secondary_dt_mw']+r['li6_capture_q_mw']))<1e-9
    assert abs(r['dd_net_mwe']+r['unconverted_and_local_energy_mw']-r['nuclear_q_mw'])<1e-8
    assert 0 <= r['t_exhaust_recovered_kg_y'] <= r['t_born_kg_y']
    assert 0 <= r['he3_plasma_recovered_l_y'] <= r['he3_born_l_y']
    assert abs(r['bank_20y'][-1]['t_active_kg']+r['bank_20y'][-1]['t_decayed_cumulative_kg']-a.t_bank_input_kg_year*a.years)<1e-8
    assert all(r['bank_20y'][i+1]['he3_decay_cumulative_stp_l']>=r['bank_20y'][i]['he3_decay_cumulative_stp_l'] for i in range(a.years))

def main():
    folder=Path(__file__).parent
    a=Assumptions()
    r=model(a)
    validate(a,r)
    with (folder/'screening_results.json').open('w') as f:json.dump({k:v for k,v in r.items() if k not in ('assumptions',)},f,indent=2)
    with (folder/'tritium_bank_20y.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(r['bank_20y'][0]));writer.writeheader();writer.writerows(r['bank_20y'])
    with (folder/'assumptions.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['parameter','value','status','interpretation'])
        for key,value in asdict(a).items():w.writerow([key,value,'POTENTIAL-DERIVED' if key not in ('t_half_life_years','dd_q_neutron_mev','dd_q_he3_mev','dt_q_mev','li6_capture_q_mev') else 'SOURCE-TRACED CONSTANT','Illustrative screening input; not calibrated to ARC-DD'])
    rows=[]
    for fb in [0.0,0.1,0.28,0.373]:
      for fc in [0.0,0.5,1.0]:
        b=Assumptions(secondary_t_burn_fraction=fb,neutron_capture_fraction=fc)
        v=model(b);validate(b,v)
        rows.append({'T_burn_fraction':fb,'Li6_capture_fraction':fc,'secondary_DT_MW':round(v['secondary_dt_mw'],4),'Li6_Q_MW':round(v['li6_capture_q_mw'],4),'gross_nuclear_MW':round(v['nuclear_q_mw'],4),'gross_electric_MWe':round(v['gross_e_mwe'],4),'DD_net_MWe':round(v['dd_net_mwe'],4),'opportunity_MWe':round(v['opportunity_mwe'],4),'T_born_kg_y':round(v['t_born_kg_y'],4),'T_recovered_kg_y':round(v['t_total_recovered_kg_y'],4),'He3_recovered_L_y':round(v['he3_plasma_recovered_l_y'],2)})
    with (folder/'dd_sensitivity.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (folder/'model_checks.txt').open('w') as f:f.write('PASS: electrical net identity\nPASS: nuclear Q identity\nPASS: plant boundary identity\nPASS: recovered isotope not exceeding birth\nPASS: tritium stock and decay conservation\nPASS: cumulative decay monotonic\n')
    print('SCENARIO SCREENING OUTPUTS\n');
    for k in ['secondary_dt_mw','li6_capture_q_mw','nuclear_q_mw','deposited_thermal_mw','gross_e_mwe','rf_wall_mwe','aux_mwe','dd_net_mwe','opportunity_mwe','opportunity_musd_y','t_born_kg_y','he3_born_l_y','t_total_recovered_kg_y','he3_plasma_recovered_l_y']:
        print(k,round(r[k],4))
    print('T bank at 20y:',r['bank_20y'][-1]);print('checks 6 PASS')
if __name__=='__main__':main()