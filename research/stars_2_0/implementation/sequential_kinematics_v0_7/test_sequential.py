import itertools,json,math,unittest
from pathlib import Path
import numpy as np
from sequential import ROOT,allowed_channel,build_event,require_calibrated_source,k,MA,MP,MB,Q
from verify_sequential import verification
from extract_2025 import parse_table,TAG

def config():return dict(E_proton_LAB_MeV=.675,pair_relative_MeV=3.,primary_direction_CM=[0.,0.,1.],
    secondary_direction_pair_rest=[1.,0.,0.],parent_J=2,parent_parity=-1,pair_J=2,pair_parity=1,primary_l=1,secondary_l=2)

class SequentialTests(unittest.TestCase):
    def test_full_grid_physical_closure(self):
        r=verification();self.assertEqual(r['events'],800)
        self.assertLess(r['maximum_four_momentum_residual_MeV'],1e-8)
        self.assertLess(r['maximum_relative_mass_shell_residual'],1e-12)
        self.assertLess(r['maximum_intermediate_mass_residual_MeV'],1e-8)

    def test_selection_rules(self):
        c=config();q={x:c[x] for x in ['parent_J','parent_parity','pair_J','pair_parity','primary_l','secondary_l']}
        for l in [1,3]:self.assertTrue(allowed_channel(**dict(q,primary_l=l)))
        for l in [0,1,2,3,4,5]:
            self.assertFalse(allowed_channel(**dict(q,pair_J=0,secondary_l=0,primary_l=l)))
        self.assertTrue(allowed_channel(**dict(q,parent_J=3,pair_J=0,secondary_l=0,primary_l=3)))
        self.assertFalse(allowed_channel(**dict(q,pair_J=1,secondary_l=1,pair_parity=-1)))
        with self.assertRaises(ValueError):allowed_channel(**dict(q,parent_J=True))

    def test_forbidden_branch_cannot_generate(self):
        with self.assertRaises(ValueError):build_event(**dict(config(),pair_J=0,secondary_l=0,primary_l=2))

    def test_recover_rest_frames(self):
        c=config();r=build_event(**c);lab=np.array(r['alpha_four_vectors_LAB_MeV']);initial=np.array(r['initial_four_vector_LAB_MeV'])
        cm=np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab]);pair=cm[1]+cm[2]
        daughter=k.boost(cm[1],-pair[1:]/pair[0])
        np.testing.assert_allclose(cm,r['alpha_four_vectors_CM_MeV'],atol=1e-9,rtol=0)
        np.testing.assert_allclose(daughter[1:]/np.linalg.norm(daughter[1:]),c['secondary_direction_pair_rest'],atol=1e-12,rtol=0)
        self.assertAlmostEqual(math.sqrt(pair[0]**2-float(pair[1:]@pair[1:]))-2*MA,c['pair_relative_MeV'],places=8)

    def test_nonrelativistic_mutation_is_detected(self):
        r=build_event(**config());cm=np.array(r['alpha_four_vectors_CM_MeV']);initial=np.array(r['initial_four_vector_LAB_MeV'])
        beta=initial[1:]/initial[0];broken=cm.copy();broken[:,1:]+=MA*beta
        with self.assertRaises(ValueError):k.verify(broken,initial)

    def test_identical_alpha_export_permutations_conserve(self):
        r=build_event(**config());a=np.array(r['alpha_four_vectors_LAB_MeV'])
        for order in itertools.permutations(range(3)):k.verify(a[list(order)],r['initial_four_vector_LAB_MeV'])
        self.assertIn('NOT_PERFORMED',r['identical_particle_amplitude_symmetrization'])

    def test_inputs_are_not_silently_repaired(self):
        for patch in [dict(E_proton_LAB_MeV=-1),dict(E_proton_LAB_MeV=math.nan),dict(pair_relative_MeV=100),dict(pair_relative_MeV=0),dict(primary_direction_CM=[0,0,2]),dict(secondary_direction_pair_rest=[math.nan,0,1])]:
            with self.assertRaises(ValueError):build_event(**dict(config(),**patch))

    def test_no_implicit_probability_or_calibrated_promotion(self):
        r=build_event(**config());self.assertIsNone(r['event_probability']);self.assertIsNone(r['event_weight']);self.assertFalse(r['source_distribution_calibrated'])
        with self.assertRaises(ValueError):require_calibrated_source()

    def test_repeat_seed(self):self.assertEqual(verification(),verification())

class PublishedDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=json.loads((ROOT/'MAZZUCCONI2025_TABLE2.json').read_text())

    def test_all_published_rows_reparse(self):
        # Structured fixture and its exact source row text agree cell-for-cell.
        d=parse_table('\n'.join(r['source_row'] for r in self.data['rows']))
        self.assertEqual(d,self.data);self.assertEqual(len(d['rows']),28)
        self.assertEqual(sum(r['possible_Al_support_alpha_contribution_explicitly_flagged_by_authors'] for r in d['rows']),5)

    def test_published_numerical_anchors(self):
        d={r['E_proton_on_boron_MeV']:r for r in self.data['rows']}
        self.assertEqual(d[4.73]['reported_energy_plus_minus_MeV'],.239)
        self.assertEqual(d[.69]['total_reported']['value_mb_sr'],57.1)
        self.assertEqual(d[.58]['total_reported']['reported_plus_minus_mb_sr'],12.6)

    def test_upper_limit_is_not_zero_or_gaussian_error(self):
        r=self.data['rows'][-1]['alpha0'];self.assertIsNone(r['value_mb_sr']);self.assertIsNone(r['reported_plus_minus_mb_sr'])
        self.assertEqual(r['upper_limit_mb_sr'],.001);self.assertIsNone(r['limit_confidence_level'])

    def test_error_mutation_cannot_drop_column(self):
        text='\n'.join(r['source_row'] for r in self.data['rows'])
        with self.assertRaises(ValueError):parse_table(text.replace('0.239','',1))
        with self.assertRaises(ValueError):parse_table('\n'.join(text.splitlines()[:-1]))

    def test_no_automatic_event_cross_section_or_covariance(self):
        self.assertEqual(self.data['observable'],TAG)
        self.assertIn('UNRESOLVED',self.data['multiplicity_to_event_cross_section'])
        self.assertIn('NOT_PERFORMED',self.data['angular_extrapolation_to_total_cross_section'])
        self.assertIn('FWHM',self.data['energy_uncertainty'])
        self.assertIn('covariance',self.data['yield_uncertainty'])

if __name__=='__main__':unittest.main()
