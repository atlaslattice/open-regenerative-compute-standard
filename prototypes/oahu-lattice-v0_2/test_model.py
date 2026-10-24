import json
import unittest
from pathlib import Path
import model

class Tests(unittest.TestCase):
 def test_mass_and_contaminant_conservation(self):
  for f in [.1,.5,.7,.9]:
   x=model.washing_ledger(1000,1000,2000,product_fraction=f)
   self.assertAlmostEqual(x['mass_error_t'],0)
   self.assertAlmostEqual(x['contaminant_error_kg'],0)
 def test_unresolved_never_passes(self):
  x=model.washing_ledger(1000,1000,2000)
  self.assertEqual(x['accepted_product_dry_t'],0)
  self.assertEqual(x['rejected_product_dry_t'],700)
 def test_quality_veto_overrides_external_clearance(self):
  x=model.washing_ledger(1000,1000,2000,contaminant_partition=(.2,.79,.01),clearance=True)
  self.assertFalse(x['accepted'])
 def test_hypothetical_gate_pass(self):
  x=model.washing_ledger(1000,1000,2000,clearance=True)
  self.assertTrue(x['accepted'])
  self.assertEqual(x['accepted_product_dry_t'],700)
 def test_contaminant_cannot_disappear(self):
  with self.assertRaises(ValueError):
   model.washing_ledger(1000,1000,2000,contaminant_partition=(0,.5,0))
 def test_impossible_cake_moisture(self):
  with self.assertRaises(ValueError): model.washing_ledger(1000,0,0)
 def test_cake_is_wet_not_just_dry_residue(self):
  x=model.washing_ledger(1000,1000,2000)
  self.assertEqual(x['cake_dry_t'],300)
  self.assertEqual(x['cake_wet_t'],600)
  self.assertGreater(x['contaminant_water_kg'],0)
 def test_unknown_cost_blocks_ranking(self):
  x=model.complete_cost(1000,*([None]*10))
  self.assertFalse(x['rankable']);self.assertIsNone(x['net_cost_usd_per_t'])
 def test_complete_cost_includes_residue(self):
  x=model.complete_cost(100,0,0,1000,0,0,0,0,500,200,300)
  self.assertEqual(x['net_cost_usd_per_t'],10)
 def test_financing(self):
  self.assertEqual(model.annualized_capital(100000,0,10),10000)
  self.assertIsNone(model.annualized_capital(None,.05,10))
 def test_high_screen_rate_does_not_expand_washer(self):
  x=model.capacity_case(200,.2,15)
  self.assertEqual(x['fines_offered_t_per_shift'],256)
  self.assertEqual(x['washed_t_per_shift'],96)
  self.assertEqual(x['unwashed_t_per_shift'],160)
 def test_capacity_bypass_not_lost(self):
  for s in [0,50,200]:
   x=model.capacity_case(s,.4,20)
   self.assertAlmostEqual(x['washed_t_per_shift']+x['unwashed_t_per_shift'],x['fines_offered_t_per_shift'])
 def test_expensive_cake_can_reverse_economics(self):
  self.assertAlmostEqual(model.cost_ceiling(.7,100,100,10),77)
  self.assertAlmostEqual(model.cost_ceiling(.7,100,400,10),-13)
 def test_catalog_complete_named_mobile_suite(self):
  c=json.loads((Path(__file__).parent/'catalog.json').read_text())
  ids=[x['id'] for x in c['modules']]
  self.assertEqual(len(ids),len(set(ids)))
  for i in ['D_FIXED','D_MOBILE_TRAIN','D_SCREEN','D_01','D_02','D_03','D_04','D_SOIL_APP','D_OIL_APP','D_SLUDGE_APP','D_BULK_APP','D_MATERIAL_APP']:
   self.assertIn(i,ids)
 def test_recipes_reference_real_modules(self):
  p=Path(__file__).parent
  ids={x['id'] for x in json.loads((p/'catalog.json').read_text())['modules']}
  r=json.loads((p/'pathways.json').read_text())
  for row in r['pathways']:
   self.assertTrue(set(row['modules']).issubset(ids),row['id'])
 def test_v01_adapter_does_not_recount_minerals(self):
  m,c=model.load_v01()
  blocked=model.attach_to_v01(m,c,200,clearance=False)
  passed=model.attach_to_v01(m,c,200,clearance=True)
  self.assertEqual(blocked['incremental_accepted_dry_product_t'],0)
  self.assertGreater(passed['incremental_accepted_dry_product_t'],0)
  self.assertEqual(passed['credited_to_real_world_t'],0)

class PortfolioTests(unittest.TestCase):
 def test_losses_can_be_subsidized(self):
  x=model.portfolio({'metals':300000,'fines':-200000},50000,0,{'environment':'pass'})
  self.assertEqual(x['combined_project_cash_usd'],50000)
  self.assertTrue(x['decision_eligible'])
 def test_public_value_separate_from_operating_cash(self):
  x=model.portfolio({'metals':300000,'fines':-400000},100000,300000,{'environment':'pass'})
  self.assertEqual(x['combined_project_cash_usd'],-200000)
  self.assertEqual(x['public_comparison_usd'],100000)
  self.assertEqual(x['minimum_avoidable_cost_to_offset_cash_gap_usd'],200000)
 def test_profit_never_overrides_veto(self):
  x=model.portfolio({'metals':1000000,'fines':-1},0,300000,{'environment':'fail'})
  self.assertFalse(x['decision_eligible'])
 def test_unknown_public_value_cannot_be_claimed(self):
  x=model.portfolio({'metals':300000,'fines':-400000},100000,None,{'environment':'unresolved'})
  self.assertIsNone(x['public_comparison_usd'])
  self.assertFalse(x['decision_eligible'])

if __name__=='__main__': unittest.main()
