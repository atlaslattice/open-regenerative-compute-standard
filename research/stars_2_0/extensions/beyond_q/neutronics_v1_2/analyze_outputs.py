"""Inspectable ledgers and conditional matched comparisons; no inferred deposited heat."""
import csv,json,statistics
from pathlib import Path
from integrate import response,apply_responses,write
from fuelcycle.model import simulate
from fuelcycle.physics import T_KG_PER_ATOM,MEV_J
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'outputs'
def main():
    rows=list(csv.DictReader((OUT/'integrated_cases.csv').read_text().splitlines()))
    comparisons=[]
    for on in [r for r in rows if r['secondary_dt']=='True']:
        off=next(r for r in rows if r['case']==on['case'] and r['condition']==on['condition'] and r['secondary_dt']=='False')
        comparisons.append(dict(case=on['case'],condition=on['condition'],
            delta_recovered_A_plasma_kg=float(on['recovered_A_plasma_T_kg'])-float(off['recovered_A_plasma_T_kg']),
            delta_recovered_A_blanket_kg=float(on['recovered_A_blanket_T_kg'])-float(off['recovered_A_blanket_T_kg']),
            delta_A_to_B_kg=float(on['A_to_B_kg'])-float(off['A_to_B_kg']),
            delta_campus_inventory_kg=float(on['inventory_change_kg'])-float(off['inventory_change_kg']),
            qualification='POTENTIAL-DERIVED matched finite-horizon accounting; damage and economic benefit UNRESOLVED'))
    write('secondary_burn_comparison.csv',comparisons)
    annual=[]
    for r in rows:
        burn=float(r['B_burn_kg']);growth=float(r['inventory_change_kg'])
        annual.append(dict(case=r['case'],secondary_dt=r['secondary_dt'],condition=r['condition'],
            horizon_calendar_days=365,B_actual_burn_kg=burn,inventory_change_kg=growth,
            inventory_change_percent_B_actual_burn=100*growth/burn if burn else None,
            qualified_usable_surplus_kg=None,classification='POTENTIAL-DERIVED; stock change is not qualified surplus'))
    write('calendar_balance_percent.csv',annual)
    energies=[]
    mapping={'A0':('DD_A0_both_Li_zero','DT_A0_both_Li_zero'),
             'A1':('DD_Li0.075_cm90','DT_Li0.075_cm90'),
             'A2_grid_candidate':('DD_Li0.9_cm120','DT_Li0.9_cm120')}
    for label,(dd,dt) in mapping.items():
        daily=list(csv.DictReader((OUT/f'{label}_daily.csv').read_text().splitlines()));last=daily[-1]
        ddn=float(last['dd_events'])-float(last['dd_t_atoms'])
        at=float(last['a_burn'])/T_KG_PER_ATOM;bt=float(last['b_burn'])/T_KG_PER_ATOM
        fusion=(float(last['dd_t_atoms'])*4.03+ddn*3.27+(at+bt)*17.6)*MEV_J
        neutron=(ddn*2.45+(at+bt)*14.1)*MEV_J;charged=fusion-neutron
        ids=(dd,dt,'DT_Li0.075_cm90');counts=(ddn,at,bt)
        kerma=sum(json.loads((OUT/'runs'/name/'result.json').read_text())['tallies']['global_heat:heating']['mean']*count*MEV_J/1e6 for name,count in zip(ids,counts))
        energies.append(dict(case=label,primary_DD_neutrons=ddn,secondary_DT_neutrons=at,B_DT_neutrons=bt,
            fusion_Q_J=fusion,fusion_neutron_initial_J=neutron,fusion_charged_initial_J=charged,
            partition_residual_J=fusion-neutron-charged,transport_neutron_kerma_J=kerma,
            deposited_heat_J=None,net_electric_J=None,
            boundary='Kerma is a separate tally, not additive to full fusion Q. Photon deposition, reaction-Q and full material energy closure UNRESOLVED.'))
    write('neutron_thermal_energy_ledger.csv',energies)
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);a=ap.parse_args()
    p=json.loads((ROOT/'inputs/fuel_cycle.json').read_text())
    cfg=apply_responses(p,a.cache/'DD_Li0.075_cm90',a.cache/'DT_Li0.075_cm90',a.cache/'DT_Li0.075_cm90')
    convergence=[]
    for h in (.125,.0625,.03125):
        _,s=simulate(dict(cfg,step_days=h),[(1,1)]*365)
        convergence.append(dict(step_days=h,final_kg=s['final_kg'],unserved_burn_kg=s['b_unserved_burn_kg'],mass_residual_kg=s['maximum_mass_residual_kg']))
    write('inventory_timestep_sensitivity.csv',convergence)
    print(json.dumps(dict(reference_secondary_comparisons=[r for r in comparisons if r['condition']=='reference'],timestep=convergence),indent=2))
if __name__=='__main__':main()
