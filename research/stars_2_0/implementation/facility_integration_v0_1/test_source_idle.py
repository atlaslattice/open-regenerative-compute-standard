import unittest
from accounting_v004 import energy_frontier,conditional_facility
class Idle(unittest.TestCase):
 def setUp(self):
  self.f=energy_frontier(10.,1.,2.,.5);self.p={'source_driver_physical_instance_id':'source','wall_to_beam_fraction':.2,'wall_to_laser_fraction':None,'laser_to_beam_fraction':None,'fired_fraction_per_attempt':0.,'attempt_rate_Hz':1.,'other_alpha_electric_recovery_fraction':1.,'non_alpha_electric_recovery_fraction':1.,'source_conversion_loss_electric_recovery_fraction':1.,'source_driver_idle_preparation_wall_J_per_attempt':3.,'source_idle_loss_electric_recovery_fraction':0.,'stored_energy_change_J_per_attempt':0.,'loads':[]}
 def test_nonfiring_attempt_still_pays_source_preparation(self):self.assertEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],-3.)
 def test_idle_loss_recovery_distinct(self):
  self.p['source_idle_loss_electric_recovery_fraction']=.5;r=conditional_facility(self.f,self.p);self.assertEqual(r['raw_net_electric_J_per_attempt'],-1.5)
 def test_perfect_all_input_recovery_conserves_energy(self):
  self.p['fired_fraction_per_attempt']=.4;self.p['source_idle_loss_electric_recovery_fraction']=1.;self.assertAlmostEqual(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'],.4)
 def test_missing_idle_wall_not_silently_zero(self):
  self.p['source_driver_idle_preparation_wall_J_per_attempt']=None;self.assertIsNone(conditional_facility(self.f,self.p)['raw_net_electric_J_per_attempt'])
if __name__=='__main__':unittest.main()
