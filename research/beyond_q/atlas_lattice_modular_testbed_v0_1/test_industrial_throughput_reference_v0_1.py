import unittest
from industrial_throughput_reference_v0_1 import evaluate, Sector
class TestModel(unittest.TestCase):
 def test_internal_elimination(self):
  m=evaluate()["annual_million_usd"]
  self.assertAlmostEqual(m["gross_sector_invoiced_sales"]-m["internal_sales_eliminated"],m["consolidated_external_sales"])
 def test_zero_fusion_sales(self):
  r=evaluate()["sector_inputs"]
  self.assertEqual(next(s for s in r if s["name"]=="fusion_isotopes")["external_sales_m"],0)
 def test_commute_benefit(self):
  self.assertGreater(evaluate()["workforce"]["commute_hours_avoided_per_year"],0)
 def test_no_commute_when_no_residents(self):
  self.assertEqual(evaluate(resident_fraction=0)["workforce"]["commute_hours_avoided_per_year"],0)
 def test_invalid_inputs(self):
  with self.assertRaises(ValueError):evaluate(resident_fraction=1.2)
if __name__=="__main__":unittest.main()
