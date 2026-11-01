import unittest,math,copy
from accounting_v002 import energy_frontier,conditional_facility
class Tests(unittest.TestCase):
 def setUp(self):
  self.f=energy_frontier(10.,1.,2.,.5)
  self.p={'source_driver_physical_instance_id':'source','wall_to_beam_fraction':1.,'wall_to_laser_fraction':None,'laser_to_beam_fraction':None,'fired_fraction_per_attempt':1.,'attempt_rate_Hz':1.,'other_alpha_electric_recovery_fraction':1.,'non_alpha_electric_recovery_fraction':1.,'stored_energy_change_J_per_attempt':0.,'loads':[{'physical_instance_id':'prep','wall_J_per_attempt':0.,'wall_J_per_fired':0.}]}
 def test_full_recovery_yields_Q_once(self):
  r=conditional_facility(self.f,self.p);self.assertAlmostEqual(r['output_electric_J_per_fired'],11.);self.assertAlmostEqual(r['storage_neutral_net_J_per_attempt'],1.)
 def test_alpha_direct_only(self):
  self.p['other_alpha_electric_recovery_fraction']=0.;self.p['non_alpha_electric_recovery_fraction']=0.;r=conditional_facility(self.f,self.p);self.assertEqual(r['output_electric_J_per_fired'],.5);self.assertEqual(r['raw_net_electric_J_per_attempt'],-9.5)
 def test_efficiency_threshold(self):
  self.p['wall_to_beam_fraction']=self.f['necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic'];self.assertAlmostEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],0.)
 def test_grid_and_source_not_counted_twice(self):
  self.p['loads'].append({'physical_instance_id':'source','wall_J_per_attempt':1.,'wall_J_per_fired':0.})
  with self.assertRaises(ValueError):conditional_facility(self.f,self.p)
 def test_duplicate_physical_load_rejected(self):
  self.p['loads']*=2
  with self.assertRaises(ValueError):conditional_facility(self.f,self.p)
 def test_attempt_costs_not_removed_when_no_fire(self):
  self.p['fired_fraction_per_attempt']=0.;self.p['loads'][0]['wall_J_per_attempt']=2.;r=conditional_facility(self.f,self.p);self.assertEqual(r['output_electric_J_per_attempt'],0.);self.assertEqual(r['raw_net_electric_J_per_attempt'],-2.)
 def test_firing_throughput_does_not_change_per_fire_energy(self):
  a=conditional_facility(self.f,self.p);self.p['fired_fraction_per_attempt']=.25;b=conditional_facility(self.f,self.p);self.assertEqual(a['output_electric_J_per_fired'],b['output_electric_J_per_fired']);self.assertEqual(b['output_electric_J_per_attempt'],.25*a['output_electric_J_per_attempt'])
 def test_known_auxiliary_draw_reduces_net(self):
  self.p['loads'][0]['wall_J_per_attempt']=.2;self.p['loads'][0]['wall_J_per_fired']=.3;self.assertAlmostEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],.5)
 def test_missing_load_is_not_zero(self):
  self.p['loads'][0]['wall_J_per_attempt']=None;r=conditional_facility(self.f,self.p);self.assertIsNone(r['wall_electric_J_per_attempt']);self.assertIsNone(r['raw_net_electric_J_per_attempt'])
 def test_missing_source_efficiency_unknown(self):
  self.p['wall_to_beam_fraction']=None;self.assertIsNone(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'])
 def test_optical_chain_product(self):
  self.p['wall_to_beam_fraction']=None;self.p['wall_to_laser_fraction']=.5;self.p['laser_to_beam_fraction']=.2;self.assertAlmostEqual(conditional_facility(self.f,self.p)['source_efficiency'],.1)
 def test_alternative_source_accounting_rejected(self):
  self.p['wall_to_laser_fraction']=.5
  with self.assertRaises(ValueError):conditional_facility(self.f,self.p)
 def test_noncyclic_storage_has_no_steady_gain_claim(self):
  self.p['stored_energy_change_J_per_attempt']=-4.;r=conditional_facility(self.f,self.p);self.assertTrue(r['noncyclic_storage_adapter_required']);self.assertIsNone(r['storage_neutral_net_W']);self.assertEqual(r['formal_storage_correction_if_all_flows_were_measured_J'],-3.)
 def test_unknown_attempt_rate_preserves_energy_but_not_power(self):
  self.p['attempt_rate_Hz']=None;r=conditional_facility(self.f,self.p);self.assertEqual(r['storage_neutral_net_J_per_attempt'],1.);self.assertIsNone(r['storage_neutral_net_W'])
 def test_zero_reaction_limit(self):
  f=energy_frontier(10.,0.,0.,0.);self.assertEqual(f['necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic'],1.);self.assertIsNone(f['alpha_direct_only_required_source_efficiency'])
 def test_common_scale_preserves_frontier(self):
  f=energy_frontier(1e13,1e12,2e12,.5e12);self.assertEqual(f['necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic'],self.f['necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic'])
 def test_impossible_partition_rejected(self):
  with self.assertRaises(ValueError):energy_frontier(10.,1.,12.,.5)
  with self.assertRaises(ValueError):energy_frontier(10.,1.,2.,3.)
 def test_bad_efficiency_rejected(self):
  for value in [0.,1.1,True,float('nan')]:
   self.p['wall_to_beam_fraction']=value
   with self.assertRaises(ValueError):conditional_facility(self.f,self.p)
if __name__=='__main__':unittest.main()
