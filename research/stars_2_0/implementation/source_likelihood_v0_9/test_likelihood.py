import json,math,unittest
from pathlib import Path
import numpy as np
from likelihood import *
ROOT=Path(__file__).resolve().parent

def source():
 d=json.loads((ROOT/'receipts/run001/INFORMATION.json').read_text())
 return np.array(d['exclusive_kernel']),np.array(d['random_alpha_response'])

class LikelihoodTests(unittest.TestCase):
 def test_analytic_derivatives_against_finite_differences(self):
  x,_=source();a=[.76,.67*2*math.pi];p,d=distribution(x,*a)
  for j in range(2):
   hi=a.copy();lo=a.copy();hi[j]+=1e-6;lo[j]-=1e-6
   numeric=(distribution(x,*hi)[0]-distribution(x,*lo)[0])/2e-6
   np.testing.assert_allclose(d[:,j],numeric,rtol=1e-6,atol=1e-10)
  np.testing.assert_allclose(d.sum(axis=0),0,atol=1e-14)

 def test_kernel_matches_original_coherent_intensity(self):
  import sys
  sys.path.insert(0,str(ROOT.parent/'coherent_source_v0_8'))
  from amplitude import components,intensity,k,MA
  lab,initial=k.event(.675,np.random.default_rng(3));cm=np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab])
  a,_=components(cm,json.loads((ROOT.parent/'coherent_source_v0_8/CANDIDATE_CONFIG.json').read_text()))
  x=kernel_from_amplitudes(a[None,:,:]);w,_=weights_and_derivatives(x,.76,.67*2*math.pi)
  self.assertAlmostEqual(w[0],intensity(a,mix_coefficient=.76,relative_phase_radians=.67*2*math.pi,coherent=True),places=15)

 def test_stochastic_coarsening_cannot_add_information(self):
  x,R=source();np.testing.assert_allclose(R.sum(axis=0),1,atol=1e-15)
  diff=fisher(x,.76,4.21)-fisher(fold(x,R,append_missed=False),.76,4.21)
  self.assertGreaterEqual(np.linalg.eigvalsh(diff)[0],-1e-12)

 def test_basis_rescaling_changes_coefficient_not_physics(self):
  x,_=source()
  for scales in [[2.,.5],[.3,7.],[1.,1.]]:
   p,_=distribution(x,.76,4.21);q,_=distribution(basis_rescale(x,scales),rescaled_k(.76,scales),4.21)
   np.testing.assert_allclose(p,q,rtol=1e-12,atol=1e-14)
  q,_=distribution(basis_rescale(x,[2.,.5]),.76,4.21)
  self.assertGreater(np.max(abs(p-q)),1e-3) # mutation: no coefficient transformation

 def test_total_count_has_no_conditional_shape_information(self):
  x,_=source();np.testing.assert_allclose(fisher(x.sum(axis=0,keepdims=True),.76,4.21),0,atol=1e-20)

 def test_missed_response_is_explicit_and_conserves_mass(self):
  x,R=source();R=.8*R
  observed=fold(x,R,append_missed=False);with_missed=fold(x,R,append_missed=True)
  np.testing.assert_allclose(with_missed.sum(axis=0),x.sum(axis=0),rtol=1e-12)
  self.assertEqual(len(with_missed),len(observed)+1)
  np.testing.assert_allclose(with_missed[-1],.2*x.sum(axis=0),rtol=1e-12)

 def test_impossible_or_signed_response_rejected(self):
  x,R=source()
  for bad in [R*2,-R,R[:,1:],np.full_like(R,math.nan)]:
   with self.assertRaises(ValueError):fold(x,bad,append_missed=False)

 def test_nonpositive_gram_kernel_rejected(self):
  x,_=source();x[0,2]=1e6
  with self.assertRaises(ValueError):distribution(x,.76,4.21)

 def test_missing_counts_not_reinterpreted_as_zero(self):
  x,_=source()
  for bad in [None,[None]*len(x),np.full(len(x),math.nan)]:
   with self.assertRaises(ValueError):multinomial_nll(x,.76,4.21,bad)
  self.assertEqual(multinomial_nll(x,.76,4.21,np.zeros(len(x),int)),0.)

 def test_noninteger_and_negative_counts_rejected(self):
  x,_=source()
  for bad in [np.ones(len(x)),np.full(len(x),-1),np.ones(len(x)-1,int)]:
   with self.assertRaises(ValueError):multinomial_nll(x,.76,4.21,bad)

 def test_phase_periodicity_and_likelihood(self):
  x,_=source();n=np.arange(len(x),dtype=int)
  self.assertAlmostEqual(multinomial_nll(x,.76,4.21,n),multinomial_nll(x,.76,4.21+2*math.pi,n),places=10)

 def test_interior_parameterization_and_zero_support(self):
  x,_=source()
  for val in [0,1,True,math.nan]:
   with self.assertRaises(ValueError):distribution(x,val,4.21)
  x=np.vstack([x,np.zeros(4)]);n=np.zeros(len(x),int);n[-1]=1
  self.assertEqual(multinomial_nll(x,.76,4.21,n),math.inf)

if __name__=='__main__':unittest.main()
