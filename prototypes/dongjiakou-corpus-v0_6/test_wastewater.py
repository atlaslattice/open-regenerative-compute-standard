import unittest,json
from pathlib import Path
from wastewater_model import (split_reuse,struvite_balance,tank_footprint,circulation_makeup,
 irrigation_envelope,import_displacement,supplemented_struvite,bioreactor_outputs)
from model import run
class WastewaterTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=json.loads((Path(__file__).parent/'inputs.json').read_text());cls.result=run(cls.inputs)
 def test_water_splits_conserve(self):
  for f in [0,8,16]:
   for d in [0,.5,1]:
    r=split_reuse(f,d,.9,.02)
    self.assertAlmostEqual(r['direct_fit_for_use_mgd']+r['advanced_product_mgd']+r['residual_mgd']+r['process_loss_mgd'],f)
 def test_direct_reuse_not_new_freshwater(self):
  r=split_reuse(16,1,.9);self.assertEqual(r['total_reusable_mgd'],16);self.assertIsNone(r['actual_authorized_delivered_mgd'])
 def test_ammonia_not_nitrate_limits_struvite(self):
  r=struvite_balance(8,3.2,.08,1);self.assertAlmostEqual(r['theoretical_struvite_t_d'],.0424462096,places=8)
  self.assertAlmostEqual(r['n_to_struvite_t_d'],r['ammonium_n_feed_t_d'])
 def test_each_nutrient_inventory_conserved(self):
  r=struvite_balance(8,3.2,.08,1)
  self.assertAlmostEqual(r['p_to_struvite_t_d']+r['remaining_total_p_t_d'],r['p_feed_t_d'])
  self.assertAlmostEqual(r['n_to_struvite_t_d']+r['remaining_ammonium_n_t_d'],r['ammonium_n_feed_t_d'])
  self.assertAlmostEqual(r['mg_to_struvite_t_d']+r['unconsumed_mg_t_d'],1)
 def test_no_magnesium_no_struvite(self):self.assertEqual(struvite_balance(8,3.2,20,0)['theoretical_struvite_t_d'],0)
 def test_total_p_not_all_reactive(self):self.assertEqual(struvite_balance(8,3.2,20,1,1,0)['theoretical_struvite_t_d'],0)
 def test_tank_is_not_campus(self):
  r=tank_footprint(16,8,5,1.5);self.assertAlmostEqual(r['assumed_tank_plot_acres'],1.4966329966);self.assertIsNone(r['full_treatment_campus_acres'])
 def test_return_loop_conserves(self):
  r=circulation_makeup(10,.05,.95)
  self.assertAlmostEqual(r['makeup_mgd'],.975)
  self.assertAlmostEqual(r['recovered_return_mgd']+r['makeup_mgd'],10)
  self.assertAlmostEqual(r['evaporated_mgd']+r['liquid_purge_mgd'],r['makeup_mgd'])
 def test_agriculture_is_envelope_not_entitlement(self):
  r=irrigation_envelope(1,.85,3);self.assertIsNone(r['authorized_crop_acres']);self.assertGreater(r['illustrative_irrigation_acres'],300)
 def test_import_offset_needs_evidence_and_cap(self):
  self.assertIsNone(import_displacement(100,None,1));self.assertEqual(import_displacement(100,20,.5),20)
 def test_mg_reallocated_not_duplicated(self):
  for r in self.result['magnesium_competing_allocation']:
   self.assertAlmostEqual(r['mg_redirected_to_struvite_t_d']+r['remaining_mg_for_hydroxide_t_d'],r['parent_captured_mg_t_d'])
 def test_residuals_still_block_environmental_gate(self):
  self.assertEqual(self.result['environmental_clearance'],'UNRESOLVED');self.assertIsNone(self.result['all_in_cost']['total'])
 def test_actual_reuse_and_imports_unknown(self):
  self.assertIsNone(self.inputs['wastewater_screening']['actual_available_feed_mgd']);self.assertIsNone(self.inputs['wastewater_screening']['actual_import_displacement_t_year'])
 def test_bioreactors_central_but_unpriced(self):
  self.assertTrue(self.inputs['bioreactor_policy']['central_design_element']);self.assertIsNone(self.inputs['corpus_cost_slots_usd']['bioreactor_retrofit_or_addition'])
 def test_added_ammonia_increases_ceiling(self):
  r=supplemented_struvite(8,3.2,.08,.8,1,'domestic_purchase')
  self.assertGreater(r['theoretical_struvite_t_d'],.6);self.assertLess(r['supplemental_nh3_pure_equivalent_t_d'],.041)
 def test_imported_n_not_recovered_n(self):
  r=supplemented_struvite(8,3.2,.08,.8,1,'international_import')
  self.assertAlmostEqual(r['nitrogen_recovered_from_final_effluent_t_d'],.0024226635)
  self.assertAlmostEqual(r['imported_n_consumed_t_d'],r['supplemental_n_in_product_t_d'])
  self.assertGreater(r['imported_n_consumed_t_d'],r['nitrogen_recovered_from_final_effluent_t_d'])
 def test_ammonia_sources_same_chemistry_different_trade(self):
  d=supplemented_struvite(8,3.2,.08,1,1,'domestic_purchase');i=supplemented_struvite(8,3.2,.08,1,1,'international_import')
  self.assertEqual(d['theoretical_struvite_t_d'],i['theoretical_struvite_t_d']);self.assertEqual(d['imported_n_consumed_t_d'],0)
 def test_supplement_mg_inventory_not_duplicated(self):
  for r in self.result['magnesium_supplement_allocation']:
   self.assertAlmostEqual(r['redirected_mg_t_d']+r['remaining_mg_t_d'],r['parent_captured_mg_t_d'])
 def test_ai_flags_do_not_authorize_penalties(self):
  self.assertTrue(self.inputs['contract_safeguards']['independent_review_required']);self.assertFalse(self.inputs['contract_safeguards']['first_water_alone_triggers_award'])
 def test_no_qualified_struvite_from_arithmetic(self):
  for r in self.result['ammonia_supplement_sensitivity']:self.assertEqual(r['actual_qualified_product_t_d'],0)
if __name__=='__main__':unittest.main()
