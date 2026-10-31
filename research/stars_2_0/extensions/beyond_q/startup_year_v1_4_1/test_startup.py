import unittest,json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'outputs'
def rows(name):return list(csv.DictReader((OUT/name).read_text().splitlines()))
class Planning(unittest.TestCase):
 def test_annual_power_and_mass(self):
  for r in rows('annual_screening.csv'):
   self.assertAlmostEqual(float(r['B_full_power_burn_kg']),61.65398062583694,places=9)
   self.assertGreater(float(r['A_plasma_eventual_recovery_screen_kg']),float(r['B_full_power_burn_kg']))
 def test_bank_has_explicit_sinks(self):
  r=json.loads((OUT/'one_year_bank.json').read_text())
  self.assertAlmostEqual(r['upper_kg'],r['B_burn_kg']+r['decay_kg']+r['processing_loss_kg']+r['final_mobile_kg'],places=8)
  self.assertLess(r['max_mass_residual_kg'],1e-8)
 def test_calendar_and_bank_bounds(self):
  r=json.loads((OUT/'one_year_bank.json').read_text());self.assertGreater(r['upper_kg'],r['B_burn_kg']);self.assertLess(r['upper_kg'],65)
  self.assertLess(r['upper_kg']-r['lower_kg'],.001)
 def test_all_physical_qualification_remains_null(self):
  self.assertTrue(all(r['qualified_surplus_kg']=='' for r in rows('startup_policies.csv')))
  self.assertIsNone(json.loads((OUT/'assumptions.json').read_text())['qualified_usable_surplus_kg'])
 def test_full_year_delivered_in_staged_cases(self):
  for r in rows('startup_policies.csv'):
   if not r['unserved_burn_kg']:continue
   self.assertLess(float(r['unserved_burn_kg']),1e-8)
   self.assertAlmostEqual(float(r['one_FPY_B_burn_kg']),61.65398062583694,places=8)
 def test_preceding_hour_fails_A1_refined_boundary(self):
  r=rows('startup_boundary_check.csv')[0];self.assertLess(float(r['selected_unserved_kg']),1e-8);self.assertGreater(float(r['previous_hour_unserved_kg']),1e-8)
 def test_zero_breeding_control(self):
  r=rows('zero_breeding_control.csv')[0];self.assertEqual(float(r['B_TBR']),0);self.assertLess(float(r['unserved_burn_kg']),1e-8)
  self.assertGreater(float(r['stock_growth_B_year_kg']),0);self.assertLess(float(r['maximum_mass_residual_kg']),1e-8)
 def test_bank_charge_dates_exist(self):
  for r in rows('startup_policies.csv'):
   if not r['policy'].startswith('Bank'):continue
   self.assertGreater(float(r['B_available_at_start_kg']),64.45);self.assertGreater(float(r['refined_fuel_available_start_days']),80)
if __name__=='__main__':unittest.main()
