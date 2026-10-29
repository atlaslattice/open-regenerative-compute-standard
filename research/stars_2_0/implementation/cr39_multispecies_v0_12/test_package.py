import json,math,tempfile,unittest
from pathlib import Path
from scipy.integrate import quad
from extract_package import extract
from literal_audit import literal_equation2,log_slope,apparatus_response
from spectra import density,integral
from run_audit import calculate,PACKAGE
ROOT=Path(__file__).resolve().parent

def data():return json.loads((ROOT/PACKAGE).read_text())
class PackageTests(unittest.TestCase):
 def test_four_source_rows_and_independent_PDF_agreement(self):
  d=data();self.assertEqual(len(d['table1']),4);self.assertTrue(d['table1_PDF_and_XML_numeric_agreement']);self.assertEqual(d['table1'][1]['p2'],.49)
 def test_independent_40_digit_arithmetic(self):
  x=calculate()['numeric_formula_check'];self.assertEqual(x['points'],28);self.assertLess(x['max_relative_difference'],1e-12)
 def test_failed_source_gate_is_preserved_and_production_blocked(self):
  x=calculate()['source_reconciliation'];self.assertIn('FAILED',x['status']);self.assertFalse(x['literal_values_in_graphical_envelope'])
  with self.assertRaises(ValueError):apparatus_response(7.5,'He')
 def test_carbon_boundary_mismatch_not_silently_smoothed(self):
  x=calculate()['source_reconciliation'];self.assertGreater(x['carbon_piecewise_jump_um'],.4);self.assertLess(x['carbon_at3_right_um'],.001)
 def test_helium_log_derivative_and_nonmonotonic_conflict(self):
  p=data()['table1'][1]
  for E in [.1,.5,1.,2.,7.5]:
   eps=1e-6;numeric=(math.log(literal_equation2(E*math.exp(eps),p))-math.log(literal_equation2(E*math.exp(-eps),p)))/(2*eps)
   self.assertAlmostEqual(numeric,log_slope(E,p),places=8);self.assertLess(log_slope(E,p),0)
 def test_analytic_proton_integral_matches_independent_quadrature(self):
  kw=dict(equation=4,N0=1e3,kBT=4.36)
  a=integral(0,10,**kw);b=quad(lambda E:density(E,**kw),0,10,epsabs=1e-6)[0];self.assertAlmostEqual(a,b,places=5)
  self.assertEqual(integral(0,math.inf,**kw),kw['N0'])
 def test_Eq3_low_cutoff_is_required_not_a_total_count(self):
  kw=dict(equation=3,N0=100,kBT=2.01)
  with self.assertRaises(ValueError):integral(0,10,**kw)
  self.assertGreater(integral(.001,10,**kw),integral(.1,10,**kw))
  self.assertNotAlmostEqual(integral(.1,10,**kw),kw['N0'])
 def test_finite_domain_integrals_match_both_density_forms(self):
  for eq in [3,4]:
   kw=dict(equation=eq,N0=123,kBT=.7);q=quad(lambda E:density(E,**kw),.1,5)[0];self.assertAlmostEqual(integral(.1,5,**kw),q,places=8)
 def test_bad_density_or_domains_rejected(self):
  for E in [0,-1,math.nan,math.inf]:
   with self.assertRaises(ValueError):density(E,equation=4,N0=1,kBT=1)
  for lo,hi in [(-1,2),(2,1),(math.nan,3)]:
   with self.assertRaises(ValueError):integral(lo,hi,equation=4,N0=1,kBT=1)
 def test_known_filters_do_not_imply_qualified_transmission(self):
  d=data();self.assertEqual(len(d['filter_array']['nominal_stacks']),6);self.assertIsNone(d['filter_array']['thickness_tolerance_um']);self.assertIsNone(d['filter_array']['full_transmission_tables']);self.assertFalse(calculate()['benchmark_qualification']['ready_for_complete_TPS_reproduction'])
 def test_calibration_drift_and_absolute_flux_discrepancy_retained(self):
  d=data()['reported_campaign_adjustments'];self.assertEqual(d['proton_calibration_shift_percent_approx'],-15);self.assertEqual(d['proton_CR39_to_TP_flux_ratio_approx'],2)
 def test_supplement_spread_ranges_are_not_covariance(self):
  s=data()['supplement_table_S1'];self.assertEqual(s['rows'][1]['sigma_L_range_um'],[.03,.06]);self.assertIn('not parameter covariance',s['semantics'])
 def test_reextract_primary_package(self):
  if not (ROOT/'sources/Schollmeier2023.xml').exists():self.skipTest('download primary sources with extract_package.py for source-dependent verification')
  self.assertEqual(extract(ROOT/'sources'),data())
 def test_source_mutation_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);(p/'Schollmeier2023.xml').write_bytes(b'changed source')
   with self.assertRaises(ValueError):extract(p)

if __name__=='__main__':unittest.main()
