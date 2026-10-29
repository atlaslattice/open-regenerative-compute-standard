import json,math,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import numpy as np
import response
from response import ReferenceResponse,REQUIRED_CONDITIONS
from run_reference import calculate
from digitize import recover
ROOT=Path(__file__).resolve().parent

class ResponseTests(unittest.TestCase):
 def setUp(self):self.r=ReferenceResponse();self.c=dict(REQUIRED_CONDITIONS)
 def test_reported_4p42_anchor_reproduced_with_pixel_allowance(self):
  row=self.r.mean(4.42,conditions=self.c);s=self.r.data['figure4']['source_statistics']
  self.assertLess(abs(row['mean_diameter_um']-s['gaussian_fit_mean_um']),.06)
  self.assertLess(abs(row['reported_or_interpolated_core_spread_um']-s['gaussian_fit_sigma_um']),.08)
 def test_coverage_refuses_7p5_and_low_energy_extrapolation(self):
  for e in [.1,7.5]:
   x=self.r.mean(e,conditions=self.c);self.assertEqual(x['status'],'UNCOVERED');self.assertIsNone(x['mean_diameter_um'])
 def test_3p3_and_3p9_are_interpolations_not_measurements(self):
  for e in [3.3,3.9]:self.assertEqual(self.r.mean(e,conditions=self.c)['status'],'INTERPOLATED_REFERENCE_MEAN_NOT_INDEPENDENT_CALIBRATION')
 def test_species_and_etch_transfer_rejected(self):
  for key,val in [('species','proton'),('species','carbon'),('detector','BARYOTRAK'),('temperature_C',70.),('etch_time_hours',6.)]:
   c=dict(self.c);c[key]=val
   with self.assertRaises(ValueError):self.r.mean(3.3,conditions=c)
 def test_nonmonotonic_inverse_preserves_multiple_solutions(self):
  a=self.r.energy_candidates(13.,conditions=self.c);self.assertEqual(a['status'],'MULTIPLE_ENERGY_CANDIDATES');self.assertGreaterEqual(len(a['energy_candidates_MeV']),2)
  for e in a['energy_candidates_MeV']:self.assertAlmostEqual(self.r.mean(e,conditions=self.c)['mean_diameter_um'],13.)
 def test_conditional_registered_count_normalization(self):
  for n in [0,1,100]:
   a=self.r.fold_registered_display_subset(4.42,n,conditions=self.c);self.assertAlmostEqual(sum(a['expected_display_counts']),n);self.assertIsNone(a['absolute_efficiency']);self.assertIsNone(a['missed_tracks'])
 def test_mean_curve_does_not_invent_full_probability_response(self):
  a=self.r.fold_registered_display_subset(3.9,100,conditions=self.c);self.assertIsNone(a['expected_display_counts']);self.assertEqual(a['status'],'FULL_RESPONSE_UNAVAILABLE_AT_THIS_ENERGY')
 def test_missing_or_negative_count_not_zero(self):
  for n in [None,-1,1.5,True]:
   with self.assertRaises(ValueError):self.r.fold_registered_display_subset(4.42,n,conditions=self.c)
 def test_nonfinite_energy_rejected(self):
  for e in [math.nan,math.inf,0,True]:
   with self.assertRaises(ValueError):self.r.mean(e,conditions=self.c)
 def test_source_nongaussian_and_digitization_mismatch_preserved(self):
  r=calculate()['figure4_source_anchor_comparison'];self.assertGreater(r['source_gaussian_chi_squared_per_ndf'],50);self.assertLess(r['standard_deviation_relative_difference'],-.05)
 def test_fixture_mutation_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   d=Path(td);(d/'ZHANG2019_DIGITIZED.json').write_bytes((ROOT/'ZHANG2019_DIGITIZED.json').read_bytes()+b' ')
   with patch.object(response,'ROOT',d):
    with self.assertRaises(ValueError):ReferenceResponse()
 def test_source_image_reextraction(self):
  if not (ROOT/'sources/Zhang2019_Fig10.png').exists():self.skipTest('download original source images with digitize.py before this source-dependent test')
  self.assertEqual(recover(ROOT/'sources'),self.r.data)

if __name__=='__main__':unittest.main()
