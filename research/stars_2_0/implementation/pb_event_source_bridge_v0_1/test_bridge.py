import copy,json,math,unittest
from pathlib import Path
from derive_event_data import extract,derive
from thin_target import expected_events
ROOT=Path(__file__).parent

def source_rows():return sum([extract((ROOT/'source_tables'/f'table{n}.html').read_bytes(),n) for n in [1,2,3]],[])
class Bridge(unittest.TestCase):
    def test_source_row_counts_and_transformation(self):
        raw=source_rows();self.assertEqual(len(raw),59);rows=derive(raw);self.assertEqual(len(rows),41)
        r=next(x for x in rows if x['E_lab_MeV']=='0.65');self.assertAlmostEqual(r['sigma_event_b'],333.7993*4*math.pi/3000)
    def test_channel_sum(self):
        rows=derive(source_rows());r=next(x for x in rows if x['E_lab_MeV']=='2.60')
        self.assertAlmostEqual(r['sigma_event_b'],(150.4627+17.1879)*4*math.pi/3000)
    def test_published_025_not_silently_026(self):
        rows=derive(source_rows());self.assertIn('0.25',[r['E_lab_MeV'] for r in rows]);self.assertNotIn('0.26',[r['E_lab_MeV'] for r in rows])
    def test_constant_cross_section_independent_binomial_oracle(self):
        rows=derive(source_rows());r=expected_events(rows,E_lab_MeV=.65,incident_protons=100,B11_atoms_cm2=1e21)
        p=1-math.exp(-r['sigma_event_b']*.001)
        self.assertAlmostEqual(r['expected_fusion_events'],100*p)
        self.assertAlmostEqual(r['probability_at_least_one_event_per_attempt'],1-(1-p)**100)
    def test_zero_input(self):
        rows=derive(source_rows())
        for n,b in [(0,1e18),(100,0)]:
            r=expected_events(rows,E_lab_MeV=.65,incident_protons=n,B11_atoms_cm2=b)
            self.assertEqual(r['expected_fusion_events'],0);self.assertEqual(r['probability_at_least_one_event_per_attempt'],0)
    def test_no_extrapolation_or_unresolved_peak_interpolation(self):
        with self.assertRaises(ValueError):expected_events(derive(source_rows()),E_lab_MeV=.162,incident_protons=1,B11_atoms_cm2=1e18)
    def test_wrong_observable_refused(self):
        rows=derive(source_rows());rows[7]['observable']='DETECTED_WINDOW_ALPHA_PRODUCTION'
        with self.assertRaises(ValueError):expected_events(rows,E_lab_MeV=.65,incident_protons=1,B11_atoms_cm2=1e18)
    def test_duplicate_rows_refused(self):
        r=source_rows()
        with self.assertRaises(ValueError):derive(r+[r[0]])
    def test_stability_scenario_not_acoustic_enhancement(self):
        rows=derive(source_rows());a=expected_events(rows,E_lab_MeV=.65,incident_protons=1000000,B11_atoms_cm2=1e18);b=expected_events(rows,E_lab_MeV=.65,incident_protons=2000000,B11_atoms_cm2=1e18)
        self.assertAlmostEqual(a['expected_fusion_events'],.5*b['expected_fusion_events'])
        self.assertGreater(a['probability_at_least_one_event_per_attempt'],.5*b['probability_at_least_one_event_per_attempt'])
if __name__=='__main__':unittest.main()
