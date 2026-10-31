import copy,math,unittest
from bridge import route,check_source

def fixture():
 g=dict(lo_m=[-.001,-.001,0],hi_m=[.001,.001,.0035],B_upper_T=.012)
 r=dict(id='9223372036871553024',face='zhi',weight=10.,mass_kg=1.67262192595e-27,charge_C=1.602176634e-19,position_m=[0,0,.003500001],momentum_kg_m_s=[0,0,1.9e-20],time_s=1e-10,step=100,delta_s=0)
 return r,g

class Tests(unittest.TestCase):
 def test_projection_preserves_raw(self):
  r,g=fixture();old=copy.deepcopy(r);p=route([r],g,1e-12)['arrivals'][0];self.assertEqual(r,old);self.assertEqual(p['position_m'][2],.0035);self.assertNotEqual(p['raw_position_m'][2],.0035)
 def test_id_precision(self):
  r,g=fixture();self.assertEqual(route([r],g,1e-12)['arrivals'][0]['id'],'9223372036871553024')
 def test_duplicate(self):
  r,g=fixture()
  with self.assertRaises(ValueError):route([r,r],g,1e-12)
 def test_missing_vs_empty(self):
  r,g=fixture();self.assertIsNone(route(None,g,1e-12)['arrivals']);self.assertEqual(route([],g,1e-12)['arrivals'],[])
 def test_inward(self):
  r,g=fixture();r['momentum_kg_m_s'][2]*=-1
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_far_overshoot(self):
  r,g=fixture();r['position_m'][2]=.004
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_clock(self):
  r,g=fixture();r['step']=99
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_EB_convention(self):
  r,g=fixture();r['delta_s']=1e-13
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_mass(self):
  r,g=fixture();r['mass_kg']*=2
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_charge(self):
  r,g=fixture();r['charge_C']*=2
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_aperture_ambiguity(self):
  r,g=fixture();r['position_m'][0]=.001
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_side_loss(self):
  r,g=fixture();r.update(face='xhi',position_m=[.001000001,0,.001],momentum_kg_m_s=[1.9e-20,0,0]);p=route([r],g,1e-12);self.assertEqual(p['arrivals'],[]);self.assertEqual(p['losses'][0]['weight'],10)
 def test_incomplete_source(self):
  r,g=fixture()
  with self.assertRaises(ValueError):check_source(100,1,[r])
 def test_wrong_energy(self):
  r,g=fixture()
  with self.assertRaises(ValueError):check_source(10,100,[r])
 def test_nan_momentum(self):
  r,g=fixture();r['momentum_kg_m_s'][0]=math.nan
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_negative_weight(self):
  r,g=fixture();r['weight']=-1
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_nan_source(self):
  r,g=fixture()
  with self.assertRaises(ValueError):check_source(math.nan,1,[r])
 def test_nan_charge(self):
  r,g=fixture();r['charge_C']=math.nan
  with self.assertRaises(ValueError):route([r],g,1e-12)
 def test_known_zero_balance(self):self.assertEqual(check_source(0,0,[])['status'],'PASS')

if __name__=='__main__':unittest.main()
