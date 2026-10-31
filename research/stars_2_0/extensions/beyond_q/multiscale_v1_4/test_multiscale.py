"""Research software acceptance; no physical-validation promotion."""
import unittest,json,csv,math
from pathlib import Path
import numpy as np
from slowing import candidate,coefficients,K_to_W,W_to_K,e
from fuelcycle.model import simulate,validate
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'outputs'
def rows(name):return list(csv.DictReader((OUT/name).read_text().splitlines()))
def scenarios():return json.loads((ROOT/'inputs/scenarios.json').read_text())
class Checks(unittest.TestCase):
 def test_actual_warpx_cases(self):
  data=json.loads((OUT/'warpx_status.json').read_text());self.assertEqual(len(data),6)
  self.assertTrue(all(r['exit_code']==0 and r.get('analysis_exit',0)==0 for r in data))
 def test_initial_kinetic_energy_is_not_zero(self):
  from analyze import read_reduced
  for name in ('coupled_100','coupled_200','coupled_no_drag'):
   d=read_reduced(OUT/'warpx'/name/'energy.txt');self.assertAlmostEqual(d['T_mean(J)'][0]/e/1e6,1,places=10)
 def test_drag_agreement_and_refinement(self):
  d=rows('drag_comparison.csv');self.assertEqual(len(d),8)
  self.assertTrue(all(float(r['max_relative_error'])<1e-3 for r in d))
  a=next(float(r['max_relative_error']) for r in d if r['case']=='drag_100' and r['species']=='T_both')
  b=next(float(r['max_relative_error']) for r in d if r['case']=='drag_200' and r['species']=='T_both');self.assertLess(b,a)
 def test_simultaneous_drag_and_DT_comparison(self):
  for r in rows('coupled_burn_comparison.csv'):
   self.assertLess(abs(float(r['relative_difference'])),.10)
   self.assertLess(float(r['T_closure_fraction']),1e-10);self.assertLess(float(r['neutron_coproduct_fraction']),1e-10)
 def test_open_background_energy_boundary(self):
  for r in rows('coupled_burn_comparison.csv'):
   sink=float(r['external_background_sink_J']);pred=float(r['reduced_predicted_background_sink_J'])
   if r['case']=='coupled_no_drag':self.assertLess(abs(sink),1e-6)
   else:
    self.assertGreater(sink,0);self.assertLess(abs(sink-pred)/pred,.01)
 def test_failed_initialization_is_retained(self):
  self.assertEqual(json.loads((OUT/'failures/cold_triton_initialization/DISPOSITION.json').read_text())['status'],'REJECTED_SETUP')
 def test_probability_and_energy_ledgers(self):
  for r in rows('slowing_escape_sensitivity.csv'):
   self.assertLess(abs(float(r['probability_residual'])),1e-7)
   self.assertAlmostEqual(float(r['p_total_burn'])+float(r['p_total_escape']),1,places=7)
   self.assertLess(abs(float(r['fast_kinetic_partition_residual_eV'])),.1)
 def test_invalid_kinetic_inputs(self):
  with self.assertRaises(ValueError):coefficients(-1,1e4,1e20,2e4)
  with self.assertRaises(ValueError):candidate(tau_fast_s=0)
  with self.assertRaises(ValueError):candidate(switch_eV=2e6)
 def test_energy_variable_conversion(self):
  for E in (1e3,1e5,1e6):self.assertAlmostEqual(W_to_K(K_to_W(E*e))/(E*e),1,places=12)
 def test_power_basis_identities(self):
  data=scenarios();self.assertEqual({x['configuration_id'] for x in data},{'historical_20_1130','dual_laser_1100_1100'})
  p=dict(data[0]['parameters'],configuration_id='dual_laser_1100_1100')
  with self.assertRaises(ValueError):validate(p)
 def test_net_electric_assumption_does_not_become_fusion_source(self):
  p=next(x['parameters'] for x in scenarios() if x['configuration_id']=='dual_laser_1100_1100')
  a,_=simulate(dict(p,schedule_slots=2,A_net_electric_W=0),[(1,1)]*2)
  b,_=simulate(dict(p,schedule_slots=2,A_net_electric_W=20e6),[(1,1)]*2)
  self.assertEqual(a[-1]['dd_birth'],b[-1]['dd_birth'])
 def test_8hour_case_count_and_mass(self):
  data=rows('eight_hour_summary.csv');self.assertEqual(len(data),54)
  self.assertTrue(all(float(r['duration_hours'])==8 for r in data));self.assertTrue(all(abs(float(r['mass_residual_kg']))<1e-8 for r in data))
  self.assertTrue(all(r['qualified_surplus_kg']=='' for r in data))
 def test_B_consumption_seconds_and_days(self):
  data=rows('eight_hour_summary.csv')
  for r in data:
   if r['condition']!='continuous':continue
   expected=float(r['B_gross_fusion_W'])*28800/(17.6*1.602176634e-13)*(.00301604928/6.02214076e23)
   self.assertAlmostEqual(float(r['B_actual_burn_kg'])/expected,1,places=10)
 def test_no_source_no_new_T(self):
  p=dict(scenarios()[0]['parameters'],schedule_slots=3,initial_a_kg=0,initial_b_kg=0)
  t,s=simulate(p,[(0,1)]*3);self.assertEqual(s['final_kg'],0);self.assertEqual(t[-1]['b_burn'],0)
 def test_zero_initial_B_cannot_fake_full_power(self):
  data=[r for r in rows('eight_hour_summary.csv') if r['condition']=='zero_initial_B']
  self.assertTrue(all(float(r['B_unserved_burn_kg'])>0 for r in data))
 def test_secondary_off_keeps_primary_neutron_breeding(self):
  for r in rows('eight_hour_summary.csv'):
   if r['condition']=='secondary_off' and r['case']=='A1':
    self.assertEqual(float(r['A_internal_burn_kg']),0);self.assertGreater(float(r['A_blanket_birth_kg']),0)
 def test_disjoint_fast_routes(self):
  p=dict(scenarios()[0]['parameters'],a_fast_fraction=.8,a_fast_escape_fraction=.8)
  with self.assertRaises(ValueError):validate(p)
 def test_schedule_run_lengths_cover_actual_clock(self):
  for record in scenarios():
   for name,n in [('reactor_schedule_runs',2),('component_schedule_runs',4)]:
    schedule=[]
    for block in record[name]:
     self.assertEqual(block[0],len(schedule));self.assertGreater(block[1],block[0]);self.assertEqual(len(block[2:]),n)
     schedule.extend([block[2:]]*(block[1]-block[0]))
    self.assertEqual(len(schedule),480)
   if record['condition']=='B_15min_outage':self.assertEqual(sum((b-a)*v[1] for a,b,*v in record['reactor_schedule_runs']),465)
 def test_numerical_refinement_is_recorded(self):
  data=rows('slowing_numerical_convergence.csv');a=float(data[1]['p_total_burn']);b=float(data[2]['p_total_burn']);self.assertLess(abs(a-b),1e-4)
  self.assertEqual(len(rows('eight_hour_timestep_refinement.csv')),6)
if __name__=='__main__':unittest.main()
