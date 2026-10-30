import unittest
from dual_apparatus import evaluate
class TestDual(unittest.TestCase):
 def test_dd_insufficient_alone(self):
  c={"reactor_a_dd_fusion_power_w":20e6,"reactor_b_dt_fusion_power_w":1.13e9}
  x=evaluate(c)
  self.assertGreater(x["dd_only_coverage_fraction"],.04)
  self.assertLess(x["dd_only_coverage_fraction"],.05)
  self.assertGreater(x["required_external_tritium_atoms_per_s"],0)
 def test_breeding_reaches_balance(self):
  c={"reactor_a_dd_fusion_power_w":20e6,"reactor_b_dt_fusion_power_w":1.13e9,"effective_b_blanket_tritium_per_dt_reaction":1}
  x=evaluate(c)
  self.assertEqual(x["required_external_tritium_atoms_per_s"],0)
  self.assertGreater(x["net_tritium_surplus_atoms_per_s"],0)
 def test_extraction_and_loss(self):
  c={"reactor_a_dd_fusion_power_w":20e6,"reactor_b_dt_fusion_power_w":1.13e9,"dd_tritium_delivery_fraction":0,"additional_tritium_loss_atoms_per_s":1e18}
  x=evaluate(c)
  self.assertAlmostEqual(x["dd_only_coverage_fraction"],0)
  self.assertGreater(x["required_external_tritium_atoms_per_s"],x["reactor_b_dt_reactions_per_s"])
if __name__=="__main__":unittest.main()
