import math,unittest
import numpy as np
from geometry import exit_box,energy_through_column,apparatus_gate
class ConstantStopping:
 # Pure numerical fixture in MeV per column unit, not a physical material.
 e=np.array([.1,10.])
 def outgoing(self,E,path):
  if E>10:raise ValueError('out of domain')
  value=E-path
  return None if value<.1 else value
class Tests(unittest.TestCase):
 def setUp(self):self.lo=[-1.,-1.,0.];self.hi=[1.,1.,1.];self.mid=[0.,0.,.5]
 def hit(self,u,p=None,lo=None,hi=None):return exit_box(p or self.mid,u,lo or self.lo,hi or self.hi)
 def test_rear(self):
  h=self.hit([0,0,1]);self.assertEqual(h['faces'],['Z+']);self.assertEqual(h['path_column_atoms_cm2'],.5)
 def test_front(self):self.assertEqual(self.hit([0,0,-1])['faces'],['Z-'])
 def test_grazing_has_finite_edge(self):
  h=self.hit([1,0,0]);self.assertEqual(h['faces'],['X+']);self.assertEqual(h['path_column_atoms_cm2'],1.)
 def test_oblique_path(self):self.assertAlmostEqual(self.hit([.6,0,.8])['path_column_atoms_cm2'],.625)
 def test_surface_outward_zero_path(self):self.assertEqual(self.hit([0,0,1],p=[0,0,1])['path_column_atoms_cm2'],0.)
 def test_surface_inward(self):self.assertEqual(self.hit([0,0,-1],p=[0,0,1])['path_column_atoms_cm2'],1.)
 def test_corner_reports_both_faces(self):
  h=self.hit([1/math.sqrt(2),1/math.sqrt(2),0]);self.assertEqual(h['faces'],['X+','Y+'])
 def test_scale_covariance(self):
  u=[.6,0,.8];a=self.hit(u);b=exit_box(np.array(self.mid)*1e18,u,np.array(self.lo)*1e18,np.array(self.hi)*1e18)
  self.assertAlmostEqual(b['path_column_atoms_cm2']/1e18,a['path_column_atoms_cm2']);np.testing.assert_allclose(np.array(b['exit_column_position_atoms_cm2'])/1e18,a['exit_column_position_atoms_cm2'])
 def test_translation_covariance(self):
  shift=np.array([4.,-5.,7.]);a=self.hit([.6,0,.8]);b=exit_box(np.array(self.mid)+shift,[.6,0,.8],np.array(self.lo)+shift,np.array(self.hi)+shift)
  np.testing.assert_allclose(np.array(b['exit_column_position_atoms_cm2'])-shift,a['exit_column_position_atoms_cm2'])
 def test_outside_is_rejected(self):
  with self.assertRaises(ValueError):self.hit([0,0,1],p=[2,0,.5])
 def test_bad_axis_rejected(self):
  for u in [[0,0,0],[0,0,2],[math.nan,0,1]]:
   with self.assertRaises(ValueError):self.hit(u)
 def test_inverted_box_rejected(self):
  with self.assertRaises(ValueError):self.hit([0,0,1],hi=[-2,1,1])
 def test_random_path_is_first_surface(self):
  rng=np.random.default_rng(20261031)
  for _ in range(500):
   p=rng.uniform(self.lo,self.hi);u=rng.normal(size=3);u/=np.linalg.norm(u);h=exit_box(p,u,self.lo,self.hi);d=h['path_column_atoms_cm2'];before=p+.999999*d*u
   self.assertTrue(np.all(before>=self.lo) and np.all(before<=self.hi));after=p+(d+1e-7)*u
   self.assertTrue(np.any(after<self.lo) or np.any(after>self.hi))
 def test_wider_box_path_nondecreasing(self):
  u=[.99,0,math.sqrt(1-.99**2)];a=self.hit(u);b=self.hit(u,lo=[-10,-10,0],hi=[10,10,1]);self.assertGreater(b['path_column_atoms_cm2'],a['path_column_atoms_cm2'])
 def test_constant_loss_budget(self):
  r=energy_through_column(1.,.2,ConstantStopping());self.assertAlmostEqual(r['escaped_E'],.8);self.assertAlmostEqual(r['material_lower'],.2)
 def test_floor_crossing_unresolved(self):
  r=energy_through_column(1.,2.,ConstantStopping());self.assertIsNone(r['escaped_E']);self.assertEqual(r['unresolved_E'],.1);self.assertEqual(r['material_lower'],.9)
 def test_subfloor_birth(self):
  r=energy_through_column(.05,.2,ConstantStopping());self.assertIsNone(r['escaped_E']);self.assertEqual(r['unresolved_E'],.05)
 def test_zero_path_subfloor(self):self.assertEqual(energy_through_column(.05,0.,ConstantStopping())['escaped_E'],.05)
 def test_no_high_energy_extrapolation(self):
  with self.assertRaises(ValueError):energy_through_column(11.,1.,ConstantStopping())
 def test_bad_scalar_rejected(self):
  for E,path in [(-1.,1.),(1.,-1.),(math.inf,1.),(True,1.)]:
   with self.assertRaises(ValueError):energy_through_column(E,path,ConstantStopping())
 def test_placeholder_blocked(self):self.assertEqual(apparatus_gate({})['status'],'BLOCKED_MISSING_APPARATUS_INPUTS')
 def test_presence_does_not_validate_adapter(self):
  p={k:1 for k in apparatus_gate({})['missing']};self.assertEqual(apparatus_gate(p)['status'],'REQUIRES_QUALIFIED_APPARATUS_ADAPTER')
if __name__=='__main__':unittest.main()
