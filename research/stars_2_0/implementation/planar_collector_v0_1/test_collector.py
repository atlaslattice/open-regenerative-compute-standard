import math,unittest
from collector import planar,midpoint_potential_gain,apparatus_gate
M=3727.3794118 # Nominal inherited mass; numerical tests only.
class Tests(unittest.TestCase):
 def test_zero_bias_is_heat_not_electricity(self):
  r=planar(3.,.7,2.,0.,M);self.assertEqual(r['circuit_work_MeV'],0.);self.assertEqual(r['electrode_heat_MeV'],3.)
 def test_normal_incidence_recovery(self):
  r=planar(3.,1.,2.,1.,M);self.assertEqual(r['status'],'COLLECTED_IDEAL_PLANE');self.assertEqual(r['circuit_work_MeV'],2.);self.assertEqual(r['electrode_heat_MeV'],1.)
 def test_transverse_momentum_can_prevent_collection(self):
  r=planar(3.,.1,2.,1.,M);self.assertGreater(3.,r['barrier_MeV']);self.assertEqual(r['status'],'REFLECTED_AND_RETURNED')
 def test_reflection_does_not_credit_turning_energy(self):
  r=planar(3.,.1,2.,1.,M);self.assertGreater(r['temporary_turning_transfer_MeV'],0.);self.assertEqual(r['circuit_work_MeV'],0.);self.assertEqual(r['returned_kinetic_MeV'],3.)
 def test_acceleration_debits_circuit(self):
  r=planar(3.,.5,2.,-.25,M);self.assertEqual(r['circuit_work_MeV'],-.5);self.assertEqual(r['electrode_heat_MeV'],3.5)
 def test_charge_zero_force_null(self):
  r=planar(3.,.1,0.,5.,M);self.assertEqual(r['status'],'COLLECTED_IDEAL_PLANE');self.assertEqual(r['circuit_work_MeV'],0.)
 def test_marginal_not_silently_collected(self):
  r=planar(3.,1.,2.,1.5,M);self.assertEqual(r['status'],'MARGINAL_NOT_COLLECTED');self.assertEqual(r['deferred_kinetic_MeV'],3.)
 def test_transverse_mass_shell(self):
  T,mu=3.,.8;r=planar(T,mu,2.,.25,M);pt2=T*(T+2*M)*(1-mu*mu)
  self.assertAlmostEqual(math.sqrt(M*M+pt2+r['exit_normal_momentum_MeV']**2)-M,T-r['barrier_MeV'],places=10)
 def test_reflected_normal_momentum_reverses(self):self.assertLess(planar(3.,.2,2.,2.,M)['exit_normal_momentum_MeV'],0.)
 def test_potential_integration_refines(self):
  r=planar(3.,.8,2.,5.,M);exact=r['normal_available_MeV'];e=[]
  for n in [16,32,64,128]:e.append(abs(midpoint_potential_gain(3.,.8,M,n)-exact))
  self.assertTrue(all(b<a for a,b in zip(e,e[1:])));self.assertLess(e[-1],1e-6)
 def test_random_energy_ledger(self):
  import random
  rng=random.Random(20261031)
  for _ in range(1000):
   T=rng.uniform(.0041,9.);mu=rng.uniform(.0001,1.);V=rng.uniform(-1.,5.);r=planar(T,mu,2.,V,M)
   self.assertAlmostEqual(T,sum(r[k] for k in ['circuit_work_MeV','electrode_heat_MeV','returned_kinetic_MeV','deferred_kinetic_MeV']),places=12)
 def test_bad_parameters(self):
  for args in [(3.,0.,2.,1.,M),(3.,1.1,2.,1.,M),(-1.,1.,2.,1.,M),(3.,1.,-2.,1.,M),(True,1.,2.,1.,M),(3.,1.,2.,math.nan,M)]:
   with self.assertRaises(ValueError):planar(*args)
 def test_apparatus_still_blocked(self):self.assertIsNone(apparatus_gate()['net_wall_plug_J'])
if __name__=='__main__':unittest.main()
