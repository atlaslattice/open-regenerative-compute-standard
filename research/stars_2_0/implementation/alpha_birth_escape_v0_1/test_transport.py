import math,unittest
import numpy as np
from transport_v002 import rotation_to,propagate

class ConstantStopping:
 # Numerical analytic fixture only: one MeV lost per unit column, floor0.004MeV.
 e=np.array([.004,12.])
 def outgoing(self,E,column):
  if not self.e[0]<=E<=self.e[-1]:raise ValueError('model domain')
  return E-column if E-column>=self.e[0] else None

class Tests(unittest.TestCase):
 def setUp(self):self.c=ConstantStopping()
 def test_forward_path(self):
  r=propagate(3.,.5,.25,1.,self.c);self.assertEqual(r['face'],'REAR');self.assertEqual(r['path_atoms_cm2'],1.5);self.assertEqual(r['escaped_E'],1.5)
 def test_backward_path(self):
  r=propagate(3.,-.5,.25,1.,self.c);self.assertEqual(r['face'],'FRONT');self.assertEqual(r['escaped_E'],2.5)
 def test_floor_is_not_stopped(self):
  r=propagate(1.,.1,.5,1.,self.c);self.assertIsNone(r['escaped_E']);self.assertEqual(r['unresolved_E'],.004);self.assertEqual(r['material_lower'],.996)
 def test_birth_below_floor(self):
  r=propagate(.001,.5,.5,1.,self.c);self.assertIsNone(r['escaped_E']);self.assertEqual(r['unresolved_E'],.001);self.assertEqual(r['material_lower'],0)
 def test_vacuum_subfloor_still_escapes(self):
  r=propagate(.001,.5,0.,0.,self.c);self.assertEqual(r['escaped_E'],.001);self.assertEqual(r['unresolved_E'],0)
 def test_surface_zero_path_subfloor(self):
  r=propagate(.001,-.5,0.,1.,self.c);self.assertEqual(r['escaped_E'],.001);self.assertEqual(r['path_atoms_cm2'],0)
 def test_grazing_is_unresolved(self):
  r=propagate(3.,0.,.5,1.,self.c);self.assertIsNone(r['escaped_E']);self.assertEqual(r['unresolved_E'],3.);self.assertEqual(r['material_lower'],0)
 def test_no_unknown_energy_dropped(self):
  for E,mu,d in [(3,.5,.25),(1,.1,.5),(.001,.5,.5),(3,0,.5)]:
   r=propagate(E,mu,d,1.,self.c);self.assertAlmostEqual((r['escaped_E'] or 0)+r['material_lower']+r['unresolved_E'],E,places=13)
 def test_invalid_values(self):
  for E,mu,d,N in [(-1,.5,.5,1),(math.nan,.5,.5,1),(1,2,.5,1),(1,.5,-1,1),(1,.5,2,1),(True,.5,.5,1)]:
   with self.subTest(E=E,mu=mu),self.assertRaises(ValueError):propagate(E,mu,d,N,self.c)
 def test_high_energy_domain_not_extrapolated(self):
  with self.assertRaises(ValueError):propagate(13.,.5,.5,1.,self.c)
 def test_proper_rotations(self):
  for u in [[0,0,1],[0,0,-1],[1,0,0],[math.sqrt(.5),0,math.sqrt(.5)]]:
   R=rotation_to(u);np.testing.assert_allclose(R@np.array([0,0,1]),u,atol=1e-14);np.testing.assert_allclose(R.T@R,np.eye(3),atol=1e-14);self.assertAlmostEqual(np.linalg.det(R),1)
 def test_nonunit_axis_rejected(self):
  with self.assertRaises(ValueError):rotation_to([0,0,2])
 def test_rotation_preserves_total_momentum(self):
  R=rotation_to([math.sqrt(.5),0,math.sqrt(.5)]);p=np.array([[1.,2.,3.],[-2.,1.,0.],[4.,-1.,2.]])
  np.testing.assert_allclose((p@R.T).sum(axis=0),R@p.sum(axis=0),atol=1e-14)
if __name__=='__main__':unittest.main()
