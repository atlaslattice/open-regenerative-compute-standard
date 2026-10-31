"""Wall-plug adapter over actual saved fuel-cycle scenario outputs.
All target gains/efficiencies below are assumed bounds, NOT laser results.
No isotope sales price or blanket energy multiplier is silently supplied.
"""
from pathlib import Path
import csv,json,math
ROOT=Path(__file__).resolve().parent
MEV_J=1.602176634e-13;KG_T=.00301604928/6.02214076e23;J_PER_KWH=3.6e6

def require_positive(name,x):
 if x is None or not math.isfinite(x) or x<=0:raise ValueError(name+' must be known, finite and positive')
def energies(r):
 # Equal DD branches are the inherited scenario convention, not a new fit.
 dd=(float(r['DD_T_birth_kg'])/KG_T)*2*3.65*MEV_J
 secondary=float(r['A_internal_burn_kg'])/KG_T*17.6*MEV_J
 dt=float(r['B_actual_burn_kg'])/KG_T*17.6*MEV_J
 scheduled=float(r['B_gross_fusion_W'])*float(r['B_on_minutes'])*60
 expected=float(r['A_gross_fusion_W'])*float(r['A_on_minutes'])*60
 if not math.isclose(dd,expected,rel_tol=1e-9,abs_tol=1):raise ValueError('DD source/power normalization mismatch')
 return dict(A_primary_DD_J=dd,A_secondary_DT_J=secondary,B_actual_DT_J=dt,B_scheduled_fusion_target_J=scheduled,total_fusion_Q_J=dd+secondary+dt)

def electricity(r,p):
 for key in ('gain_A_primary_DD','gain_B_DT','laser_wallplug_efficiency','thermal_to_electric_efficiency','captured_fusion_fraction'):
  require_positive(key,p.get(key))
 for key in ('laser_wallplug_efficiency','thermal_to_electric_efficiency','captured_fusion_fraction'):
  if p[key]>1:raise ValueError('efficiency exceeds unity')
 if p.get('gain_basis')!='A_primary_DD_Q_only;B_DT_Q':raise ValueError('ambiguous gain basis')
 if p.get('B_drive_policy') not in ('scheduled','fuel_adaptive'):raise ValueError('unknown drive policy')
 E=energies(r);eta=p['laser_wallplug_efficiency'];hours=float(r['duration_hours'])
 A_optical=E['A_primary_DD_J']/p['gain_A_primary_DD']
 B_basis=E['B_scheduled_fusion_target_J'] if p['B_drive_policy']=='scheduled' else E['B_actual_DT_J']
 B_optical=B_basis/p['gain_B_DT']
 aux=p.get('auxiliary_electric_W')
 if aux is None or not math.isfinite(aux) or aux<0:raise ValueError('explicit nonnegative auxiliary load required')
 gross=E['total_fusion_Q_J']*p['captured_fusion_fraction']*p['thermal_to_electric_efficiency']
 A_electric=A_optical/eta;B_electric=B_optical/eta;auxJ=aux*hours*3600
 net=gross-A_electric-B_electric-auxJ
 return dict(**E,A_laser_on_target_J=A_optical,B_laser_on_target_J=B_optical,A_laser_electric_J=A_electric,B_laser_electric_J=B_electric,
  gross_generated_electric_J=gross,auxiliary_electric_J=auxJ,net_electric_J=net,average_net_electric_MW=net/(hours*3600*1e6),
  imported_electric_kWh=max(0,-net)/J_PER_KWH,positive_electric_before_campus_load_kWh=max(0,net)/J_PER_KWH,
  qualified_export_electric_kWh=None,realized_isotope_sales_USD=None,
  evidence='POTENTIAL-DERIVED energy scenarios; prescribed fusion, assumed gain/efficiency; no wall-plug validation')

def allocate_T(available_kg,internal_kg,external_sales_kg,reserve_kg):
 if any(not math.isfinite(x) or x<0 for x in (available_kg,internal_kg,external_sales_kg,reserve_kg)):raise ValueError('invalid mass allocation')
 if internal_kg+external_sales_kg+reserve_kg>available_kg+1e-12:raise ValueError('same T allocated more than once')
 return available_kg-internal_kg-external_sales_kg-reserve_kg

def main():
 source=ROOT.parent/'multiscale_v1_4/outputs/eight_hour_summary.csv'
 fuel=list(csv.DictReader(source.read_text().splitlines()));fuel=[r for r in fuel if r['configuration_id']=='dual_laser_1100_1100']
 cases=[];results=[];costs=[]
 for gain in (1.,10.,100.):
  for eta in (.1,.2):
   p=dict(gain_A_primary_DD=gain,gain_B_DT=gain,laser_wallplug_efficiency=eta,thermal_to_electric_efficiency=.4,captured_fusion_fraction=.9,
      auxiliary_electric_W=50e6,gain_basis='A_primary_DD_Q_only;B_DT_Q',B_drive_policy='scheduled',status='ASSUMED exploratory stress case, no technology forecast')
   name=f'gain{gain:g}_eta{eta:g}';cases.append(dict(case_id=name,**p))
   for r in fuel:
    x=electricity(r,p);results.append(dict(energy_case=name,A_case=r['case'],fuel_condition=r['condition'],**x))
    if r['case']=='A1' and r['condition']=='continuous':
     for price in (.05,.10,.20):
      # DD's entire input charge assigned to gross T solely as a screening denominator.
      # No He3 coproduct credit, heat credit or sales qualification implied.
      charge=x['A_laser_electric_J']/J_PER_KWH*price
      costs.append(dict(energy_case=name,electricity_USD_per_kWh=price,price_evidence='ASSUMED sensitivity, not a market quote',
       A_laser_input_charge_USD=charge,campus_net_import_charge_USD=x['imported_electric_kWh']*price,
       A_gross_T_birth_kg=float(r['DD_T_birth_kg']),unallocated_DD_laser_charge_per_gross_T_kg_USD=charge/float(r['DD_T_birth_kg']),
       total_production_cost_USD=None,profit_USD=None,qualified_isotope_revenue_USD=None))
 for file,data in [('electricity_scenarios.csv',results),('cost_sensitivity.csv',costs)]:
  with (ROOT/'outputs'/file).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 (ROOT/'inputs.json').write_text(json.dumps(cases,indent=2)+'\n')
 (ROOT/'outputs/unresolved.json').write_text(json.dumps(dict(measured_laser_on_target_energy_J=None,qualified_target_gains=None,
  independently_qualified_capture_efficiency=None,campus_load_W=None,maintenance_CAPEX_OPEX=None,qualified_T_sales_price_USD_per_kg=None,
  qualified_He3_capture_kg=None,qualified_He3_sales_price=None,market_absorption_limit=None,all_physical_gates='OPEN',profit=None),indent=2)+'\n')
 print('Energy rows',len(results),'price sensitivities',len(costs))
if __name__=='__main__':main()
