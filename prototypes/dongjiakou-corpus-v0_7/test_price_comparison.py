import json,csv,unittest
from pathlib import Path
from price_comparison import cny_to_usd,matched_component_price,regional_total,price_outputs
from model import run
ROOT=Path(__file__).parent
class PriceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=json.loads((ROOT/'inputs.json').read_text());cls.r=run(cls.inputs)
 def test_conversion_explicit_fx(self):self.assertEqual(cny_to_usd(725,7.25),100)
 def test_conversion_missing_not_zero(self):self.assertIsNone(cny_to_usd(None,7.25))
 def test_reference_price_columns_identical(self):
  for r in self.r['component_price_comparison']:
   for suffix in ['','_low','_high']:self.assertEqual(r['deepseek_reference_usd'+suffix],r['atlas_lattice_reference_usd'+suffix])
 def test_corpus_missing_match_is_null(self):
  self.assertTrue(all(x['corpus_matched_component_usd'] is None for x in self.r['component_price_comparison']))
 def test_matched_price_requires_evidence(self):
  ref=dict(component='membrane',price_unit='USD/element',quantity=10,supply_scope='elementonly',duty_basis='SWRO')
  c=dict(ref,amount_usd=100,scope_match_confirmed=True,source_url='https://example.com/doc')
  self.assertEqual(matched_component_price(ref,c),100)
  c['source_url']=None;self.assertIsNone(matched_component_price(ref,c))
 def test_installed_aggregate_cannot_fill_element_price(self):
  ref=dict(component='membrane',price_unit='USD/element',quantity=10,supply_scope='elementonly',duty_basis='SWRO')
  c=dict(ref,amount_usd=100,scope_match_confirmed=True,source_url='https://example.com/doc',supply_scope='installedplantaggregate')
  self.assertIsNone(matched_component_price(ref,c))
 def test_baseline_not_populated_by_anchors(self):
  self.assertIsNone(self.r['all_in_cost']['total']);self.assertTrue(all(x['include_in_total'] is False for x in self.r['component_price_comparison']))
 def test_mvr_correct_order_not_bound(self):
  m=self.r['mvr_linear_exposure'][0]
  self.assertGreater(m['linear_extrapolation_cny'],13e9);self.assertFalse(m['is_lower_bound']);self.assertFalse(m['is_upper_bound'])
 def test_regional_total_requires_direct_and_overlap(self):
  self.assertIsNone(regional_total(28,None,0));self.assertIsNone(regional_total(28,3,None));self.assertEqual(regional_total(28,3,0),31)
 def test_city_industrial_share_not_added_twice(self):self.assertEqual(regional_total(28,3,3),28)
 def test_ammonia_recovery_separate_slot(self):self.assertIn('ammonia_recovery_equipment',self.inputs['corpus_cost_slots_usd'])
 def test_no_automatic_shared_pump_saving(self):
  self.assertFalse(self.inputs['pump_policy']['shared_operating_pump_approved']);self.assertIsNone(self.inputs['pump_policy']['actual_shared_pump_capex_saving_usd'])
 def test_all_new_anchors_need_urls(self):
  with (ROOT/'china_price_anchors_needs_sourcing.csv').open() as f:r=list(csv.DictReader(f))
  self.assertEqual(len(r),27);self.assertTrue(all(x['source_status']=='NEEDS SOURCING URLS' and not x['source_url'] for x in r))
 def test_opex_and_product_prices_distinct(self):
  kinds={r['price_kind'] for r in self.r['component_price_comparison']};self.assertTrue({'OPEX','PRODUCT_PRICE','CAPEX_OR_EQUIPMENT'}<=kinds)
if __name__=='__main__':unittest.main()

class PumpTrainTests(unittest.TestCase):
 def test_product_is_not_feed(self):
  from price_comparison import train_block
  r=train_block(30,.475,3,0)
  self.assertAlmostEqual(r['ro_feed_mgd'],63.1578947368)
  self.assertIsNone(r['actual_high_pressure_pump_flow_mgd'])
 def test_train_parallelism_not_full_redundancy(self):
  from price_comparison import train_block
  self.assertEqual(train_block(30,.475,3,0)['product_with_one_complete_train_unavailable_mgd'],20)
  self.assertEqual(train_block(30,.475,3,1)['product_with_one_complete_train_unavailable_mgd'],30)
 def test_reuse_30_requires_more_than_city_average(self):
  from price_comparison import train_block
  self.assertGreater(train_block(30,.9,3,1)['ro_feed_mgd'],28)
