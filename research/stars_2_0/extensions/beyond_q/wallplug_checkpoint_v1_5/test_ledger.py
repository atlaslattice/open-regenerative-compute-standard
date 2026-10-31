import unittest,csv,json,math
from pathlib import Path
from ledger import electricity,energies,allocate_T
ROOT=Path(__file__).resolve().parent
def source(condition='continuous'):
 rows=list(csv.DictReader((ROOT.parent/'multiscale_v1_4/outputs/eight_hour_summary.csv').read_text().splitlines()))
 return next(r for r in rows if r['configuration_id']=='dual_laser_1100_1100' and r['case']=='A1' and r['condition']==condition)
def params():return json.loads((ROOT/'inputs.json').read_text())[0]
class Checks(unittest.TestCase):
 def test_primary_and_secondary_are_disjoint(self):
  r=energies(source());self.assertAlmostEqual(r['total_fusion_Q_J'],r['A_primary_DD_J']+r['A_secondary_DT_J']+r['B_actual_DT_J']);self.assertGreater(r['A_secondary_DT_J'],0)
 def test_missing_gain_not_substituted(self):
  p=params();p['gain_A_primary_DD']=None
  with self.assertRaises(ValueError):electricity(source(),p)
 def test_ambiguous_gain_basis_rejected(self):
  p=params();p['gain_basis']='total reactor maybe'
  with self.assertRaises(ValueError):electricity(source(),p)
 def test_electric_balance(self):
  r=electricity(source(),params());self.assertAlmostEqual((r['gross_generated_electric_J']-r['A_laser_electric_J']-r['B_laser_electric_J']-r['auxiliary_electric_J'])/r['net_electric_J'],1)
 def test_no_export_and_import_of_same_net_energy(self):
  for p in json.loads((ROOT/'inputs.json').read_text()):
   r=electricity(source(),p);self.assertEqual(r['imported_electric_kWh']*r['positive_electric_before_campus_load_kWh'],0);self.assertIsNone(r['qualified_export_electric_kWh'])
 def test_unfueled_scheduled_drive_is_charged(self):
  r=electricity(source('zero_initial_B'),params());self.assertEqual(r['B_actual_DT_J'],0);self.assertGreater(r['B_laser_electric_J'],0)
 def test_isotope_not_both_consumed_and_sold(self):
  with self.assertRaises(ValueError):allocate_T(1,.7,.5,0)
  self.assertAlmostEqual(allocate_T(1,.7,.1,.1),.1)
 def test_costs_do_not_become_profit(self):
  rows=list(csv.DictReader((ROOT/'outputs/cost_sensitivity.csv').read_text().splitlines()));self.assertEqual(len(rows),18)
  self.assertTrue(all(r['profit_USD']=='' and r['qualified_isotope_revenue_USD']=='' for r in rows))
 def test_source_units_locked(self):
  r=source();r['A_gross_fusion_W']='20000000'
  with self.assertRaises(ValueError):energies(r)
if __name__=='__main__':unittest.main()
