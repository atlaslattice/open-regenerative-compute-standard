import json,copy,math,unittest
from pathlib import Path
import run_model
ROOT=Path(__file__).parent
class ResourceChecks(unittest.TestCase):
 def setUp(self):self.i=json.loads((ROOT/'inputs.json').read_text())
 def test_reproducible_without_mutating_inputs(self):
  before=copy.deepcopy(self.i);a=run_model.calculate(self.i);b=run_model.calculate(self.i);self.assertEqual(a,b);self.assertEqual(self.i,before)
 def test_energy_and_nutrient_conservation(self):run_model.validate(run_model.calculate(self.i))
 def test_no_unsupported_margin_or_additional_supply(self):
  for s in run_model.calculate(self.i)['scenarios']:
   self.assertIsNone(s['RNG']['net_margin_usd']);self.assertIsNone(s['HTL']['net_margin_usd']);self.assertIn('NOT_ESTABLISHED',s['nutrients']['additionality'])
 def test_zero_product_realization_retains_cost(self):
  self.i['parameters']['nutrient_realization_fraction']=0;r=run_model.calculate(self.i)
  for s in r['scenarios']:
   for c in s['nutrient_cost_stress_tests']:self.assertEqual(c['modeled_realized_nutrient_receipts_usd'],0);self.assertLess(c['margin_before_avoided_baseline_usd'],0)
 def test_parasitics_reduce_power_but_not_gross_generation(self):
  a=run_model.calculate(self.i)['scenarios'][1]['CHP'];self.i['parameters']['CHP_electric_parasitic_fraction']=.30;b=run_model.calculate(self.i)['scenarios'][1]['CHP'];self.assertEqual(a['gross_electric_MWh_year'],b['gross_electric_MWh_year']);self.assertLess(b['net_electric_MWh_year'],a['net_electric_MWh_year'])
 def test_heat_without_customer_has_no_heat_credit(self):
  self.i['parameters']['CHP_heat_fraction_available_for_external_offset']=0
  for s in run_model.calculate(self.i)['scenarios']:self.assertEqual(s['CHP']['heat_avoided_fuel_value_usd_year'],0)
if __name__=='__main__':unittest.main()
