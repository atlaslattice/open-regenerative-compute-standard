import unittest
import model

class RoutingTests(unittest.TestCase):
 def test_routes_conserve(self):
  L=model.Ledger(100);L.add('feed',100)
  L.route('feed',[('product',.6,'product'),('cake',.4,'residual')],['wash'],'pass')
  self.assertAlmostEqual(L.summary('test')['remaining_percent'],40)
 def test_unresolved_gate_preserves_feed(self):
  L=model.Ledger(100);L.add('feed',100)
  L.route('feed',[('product',1,'product')],['wash'],'unresolved')
  self.assertEqual(L.summary('test')['remaining_percent'],100)
 def test_failed_gate_preserves_feed(self):
  L=model.Ledger(100);L.add('feed',100)
  L.route('feed',[('product',1,'product')],['wash'],'fail')
  self.assertEqual(L.summary('test')['remaining_percent'],100)
 def test_missing_mass_rejected(self):
  L=model.Ledger(100);L.add('feed',100)
  with self.assertRaises(ValueError):L.route('feed',[('product',.8,'product')],[],'pass')
 def test_negative_fraction_rejected(self):
  L=model.Ledger(100);L.add('feed',100)
  with self.assertRaises(ValueError):L.route('feed',[('a',1.1,'product'),('b',-.1,'residual')],[],'pass')
 def test_duplicate_outputs_rejected(self):
  L=model.Ledger(100);L.add('feed',100)
  with self.assertRaises(ValueError):L.route('feed',[('a',.5,'product'),('a',.5,'residual')],[],'pass')
 def test_product_cannot_be_consumed_twice(self):
  L=model.Ledger(100);L.add('feed',100)
  L.route('feed',[('product',1,'product')],[],'pass')
  with self.assertRaises(ValueError):L.route('product',[('other',1,'product')],[],'pass')
 def test_containment_does_not_erase_residual(self):
  L=model.Ledger(100);L.add('feed',100);model.contain_all(L)
  r=L.summary('test');self.assertEqual(r['remaining_percent'],100);self.assertEqual(r['contained'],100)
 def test_inherent_water_is_not_free_diversion(self):
  L=model.Ledger(100);L.add('unqualified_mineral_fines',100);model.wash(L)
  self.assertAlmostEqual(L.leaves['inherent_water_liability']['original_waste_t'],35)
  self.assertAlmostEqual(L.summary('test')['remaining_percent'],54.5)
 def test_ash_volume_not_automatically_mass(self):
  L=model.Ledger(100);L.add('incumbent_ash',100);L.add('incremental_fuel_ash',0)
  model.ash_recovery(L,.6)
  self.assertEqual(L.summary('test')['remaining_percent'],40)
  # No volume variable or conversion exists: volume projections stay unknown.
 def test_v01_decomposition_matches(self):
  m,c=model.load_v01();_,s=m.simulate(c,'check',tph=200,integrated=True)
  x=model.base_ledger(c,s['processed_t']).summary('same')
  self.assertAlmostEqual(x['source_mass_requiring_management_t'],s['disposal_plus_inventory_t'])
  self.assertAlmostEqual(x['removal_percent'],s['net_disposal_avoided_percent'])
 def test_full_capture_capacity_envelope(self):
  m,c=model.load_v01();feed=c['published_anchors']['wgsl_other_2024_us_short_tons']['value']*.90718474
  screen_capacity=200*8*300*.8
  self.assertLess(feed,screen_capacity)
  # This does not establish buffers, chemistry, or permission to process all feed.
 def test_ash_incumbent_not_atlas_credit(self):
  m,c=model.load_v01();L=model.base_ledger(c,0);model.ash_recovery(L)
  s=L.summary('incumbent');self.assertEqual(s['realized_project_credit_t'],0)
 def test_all_extreme_cases_close(self):
  m,c=model.load_v01();feed=c['published_anchors']['wgsl_other_2024_us_short_tons']['value']*.90718474
  for w in [0,.7,1]:
   for a in [0,.6,1]:
    L=model.base_ledger(c,feed);model.wash(L,w);model.ash_recovery(L,a);model.secondary(L)
    s=L.summary('test');self.assertAlmostEqual(s['mass_error_t'],0,places=6)
    self.assertGreaterEqual(s['remaining_percent'],0)
    self.assertFalse(s['all_material_remediated'])
 def test_input_cannot_exceed_feed(self):
  m,c=model.load_v01()
  with self.assertRaises(ValueError):model.base_ledger(c,1e9)

if __name__=='__main__':unittest.main()
