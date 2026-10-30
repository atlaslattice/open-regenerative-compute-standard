"""Numerical acceptance tests, not experimental validation."""
import unittest,csv,json,hashlib
from pathlib import Path
import numpy as np
from analyze import cross_section,thermal_reactivity
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'outputs'
def rows(name):return list(csv.DictReader((OUT/name).read_text().splitlines()))
def results():return {p.parent.name:json.loads(p.read_text()) for p in (OUT/'runs').glob('*/analysis.json')}
class Benchmark(unittest.TestCase):
 def test_upstream_unmodified_tests(self):
    r=json.loads((OUT/'upstream_status.json').read_text());self.assertEqual(len(r),2)
    self.assertTrue(all(x['passed'] and not x['upstream_input_overrides'] for x in r))
 def test_actual_case_count(self):self.assertEqual(len(results()),9)
 def test_provenance_and_raw_logs(self):
    for p in (OUT/'runs').glob('*/provenance.json'):
        r=json.loads(p.read_text());self.assertFalse(r['physical_validation'])
        for name,h in r['input_hashes'].items():self.assertEqual(hashlib.sha256((p.parent/name).read_bytes()).hexdigest(),h)
 def test_T_source_consumption_closure(self):
    for r in results().values():
        self.assertLessEqual(r['max_T_residual_atoms'],max(1e-8,1e-12*r['DD_T_birth_atoms']))
        self.assertLessEqual(r['DT_burn_atoms'],r['DD_T_birth_atoms'])
 def test_neutron_stoichiometry(self):self.assertTrue(all(r['max_neutron_residual_atoms']==0 for r in results().values()))
 def test_D_pool_compensated_reduction(self):
    # Eight ULPs at the8e17-atom background scale; not individual-atom precision.
    self.assertTrue(all(abs(r['compensated_final_D_residual_atoms'])<=1024 for r in results().values()))
 def test_energy_and_momentum(self):
    for r in results().values():
        self.assertLess(r['energy_residual_fraction_released'],1e-5)
        self.assertLess(r['max_momentum_residual_kg_m_s'],1e-16)
 def test_secondary_off_preserves_DD_neutrons(self):
    r=results()['secondary_off'];self.assertEqual(r['DT_burn_atoms'],0);self.assertGreater(r['DD_n_birth_atoms'],0);self.assertGreater(r['remaining_T_atoms'],0)
 def test_without_T_birth_no_DT(self):
    r=results()['no_T_birth'];self.assertEqual(r['DD_T_birth_atoms'],0);self.assertEqual(r['DT_burn_atoms'],0);self.assertGreater(r['DD_n_birth_atoms'],0)
 def test_creation_off_no_delivered_source(self):
    r=results()['no_reactions'];self.assertEqual(r['DD_T_birth_atoms'],0);self.assertEqual(r['DT_burn_atoms'],0)
 def test_cross_sections_and_DD_symmetry(self):
    for rx in ['DDT','DDN','DT']:
        self.assertEqual(float(cross_section(.1,rx)),0);self.assertGreater(thermal_reactivity(20,rx),0)
    for n,r in results().items():
        if n in ('no_T_birth','no_reactions'):continue
        for rx,col,se in [('DDT','DD_T_birth_atoms','DDT_sampling_SE_proxy_atoms'),('DDN','DD_n_birth_atoms','DDN_sampling_SE_proxy_atoms')]:
            self.assertLess(abs(r[col]-r['expected_thermal_'+rx+'_atoms']),5*r[se])
 def test_multiplier_does_not_multiply_physical_yield(self):
    r=results();a=r['chain_on'];b=r['lower_multiplier']
    self.assertLess(abs(a['DD_T_birth_atoms']-b['DD_T_birth_atoms']),5*(a['DDT_sampling_SE_proxy_atoms']+b['DDT_sampling_SE_proxy_atoms']))
 def test_existing_compartment_kernel_comparison(self):
    r=rows('inventory_kernel_comparison.csv');self.assertEqual(len(r),6)
    for x in r:
        # Declared10% screen; no calibrated physical confidence interval.
        self.assertLess(abs(float(x['relative_difference'])),.10)
        self.assertLess(abs(float(x['closure_kg'])),1e-30)
 def test_source_export_and_reference_lock(self):
    s=json.loads((OUT/'source_interface.json').read_text());self.assertEqual(s['reference_primary_DD_MW'],20);self.assertEqual(s['reference_B_DT_MW'],1130)
    self.assertFalse(s['physical_validation']);self.assertFalse(s['stationary_reactor_source_qualified'])
    data=rows('normalized_A_source_spectrum.csv')
    self.assertAlmostEqual(sum(float(x['probability_per_all_source_neutrons']) for x in data),1)
    for species in ['nDD','nDT']:self.assertAlmostEqual(sum(float(x['probability_given_source_type']) for x in data if x['species']==species),1)
 def test_archived_particle_moments(self):
    source=json.loads((OUT/'source_interface.json').read_text());p=OUT/'baseline_daughter_particles.npz'
    self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),source['raw_particle_archive_sha256'])
    r=results()['chain_on']
    with np.load(p) as z:
        self.assertAlmostEqual(z['P_weight'].sum()/r['DD_T_birth_atoms'],1,places=12)
        self.assertAlmostEqual(z['nDT_weight'].sum()/r['DT_burn_atoms'],1,places=12)
 def test_mass_conventions_explicit(self):
    q=json.loads((OUT/'source_interface.json').read_text());self.assertAlmostEqual(q['B_convention_fractional_difference'],17.6/17.58929696-1)
if __name__=='__main__':unittest.main()
