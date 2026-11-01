"""Source/auxiliary conversion-loss recovery is distinct from downstream energy."""
import unittest
from accounting_v003 import energy_frontier,conditional_facility
class Recovery(unittest.TestCase):
 def setUp(self):
  self.f=energy_frontier(10.,1.,2.,.5);self.p={'source_driver_physical_instance_id':'source','wall_to_beam_fraction':.2,'wall_to_laser_fraction':None,'laser_to_beam_fraction':None,'fired_fraction_per_attempt':1.,'attempt_rate_Hz':1.,'other_alpha_electric_recovery_fraction':1.,'non_alpha_electric_recovery_fraction':1.,'source_conversion_loss_electric_recovery_fraction':0.,'stored_energy_change_J_per_attempt':0.,'loads':[{'physical_instance_id':'load','wall_J_per_attempt':0.,'wall_J_per_fired':0.,'own_wall_loss_electric_recovery_fraction':0.}]}
 def test_zero_source_loss_credit_is_scoped_threshold(self):
  self.p['wall_to_beam_fraction']=self.f['source_loss_uncredited_necessary_eta_for_nonnegative_net'];self.assertAlmostEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],0.)
 def test_source_loss_recovery_can_change_boundary_conclusion(self):
  a=conditional_facility(self.f,self.p);self.p['source_conversion_loss_electric_recovery_fraction']=1.;b=conditional_facility(self.f,self.p);self.assertEqual(a['raw_net_electric_J_per_attempt'],-39.);self.assertEqual(b['raw_net_electric_J_per_attempt'],1.)
 def test_source_remainder_excludes_beam_energy(self):
  r=conditional_facility(self.f,self.p);self.assertEqual(r['source_gross_wall_J_per_fired'],50.);self.assertEqual(r['source_conversion_energy_remainder_J_per_fired'],40.)
 def test_auxiliary_own_input_recovery_not_double_counted(self):
  self.p['source_conversion_loss_electric_recovery_fraction']=1.;self.p['fired_fraction_per_attempt']=.4;self.p['loads'][0].update(wall_J_per_attempt=2.,wall_J_per_fired=3.,own_wall_loss_electric_recovery_fraction=1.)
  r=conditional_facility(self.f,self.p);self.assertAlmostEqual(r['raw_net_electric_J_per_attempt'],.4)
 def test_missing_recovery_is_not_zero_credit(self):
  self.p['source_conversion_loss_electric_recovery_fraction']=None;r=conditional_facility(self.f,self.p);self.assertIsNone(r['raw_net_electric_J_per_attempt'])
 def test_perfect_source_has_no_source_loss_credit(self):
  self.p['wall_to_beam_fraction']=1.;self.p['source_conversion_loss_electric_recovery_fraction']=1.;self.assertEqual(conditional_facility(self.f,self.p)['source_conversion_electric_recovery_J_per_fired'],0.)
 def test_direct_alpha_only_not_rescued_by_source_loss_credit(self):
  self.p['source_conversion_loss_electric_recovery_fraction']=1.;self.p['other_alpha_electric_recovery_fraction']=0.;self.p['non_alpha_electric_recovery_fraction']=0.;self.assertEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],-9.5)
 def test_no_recovery_fraction_above_unity(self):
  self.p['source_conversion_loss_electric_recovery_fraction']=1.1
  with self.assertRaises(ValueError):conditional_facility(self.f,self.p)
if __name__=='__main__':unittest.main()
