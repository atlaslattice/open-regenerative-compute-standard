import copy,json,math,unittest
from pathlib import Path
from unittest.mock import patch
import numpy as np
import reference as ref
from calibration_bundle import authorize,load_catalog,audit
ROOT=Path(__file__).resolve().parent

def config():
 c=json.loads((ROOT/'examples/assumed_reference.json').read_text());c.update(depth_bins=1,samples_per_depth=8);return c

class EvidenceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.c=config();cls.r,cls.trace=ref.execute(cls.c)
 def test_all_attempts_and_true_zero_retained(self):
  self.assertEqual(self.r['all_attempt_count'],3);a=self.r['attempts'][1];self.assertEqual(a['expected_reactions'],0)
  for m in a['models'].values():self.assertEqual(sum(m['expected_geometry_accepted_true_exit_bins']),0);self.assertIsNone(m['detector_counts'])
 def test_missing_protons_not_zero(self):
  c=config();c['attempts'][1]['incident_protons']=None
  with self.assertRaises(ValueError):ref.execute(c)
 def test_per_depth_normalization_preserves_hazard(self):
  total=sum(e['coherent_event_probability_weight_per_incident_proton'] for e in self.trace)
  self.assertAlmostEqual(total,self.r['per_proton_reaction_probability'],places=18)
  for cell in self.r['source_cells']:
   self.assertEqual(cell['models']['COHERENT']['probability_per_incident_proton'],cell['models']['PHASE_SPACE_NULL']['probability_per_incident_proton'])
 def test_arbitrary_amplitude_scale_cannot_change_transport(self):
  original=ref.intensity
  with patch.object(ref,'intensity',side_effect=lambda *a,**kw:37.*original(*a,**kw)):b,_=ref.execute(config())
  self.assertEqual(b['per_proton_reaction_probability'],self.r['per_proton_reaction_probability'])
  for x,y in zip(self.r['attempts'],b['attempts']):
   np.testing.assert_allclose(x['models']['COHERENT']['expected_geometry_accepted_true_exit_bins'],y['models']['COHERENT']['expected_geometry_accepted_true_exit_bins'],rtol=1e-12,atol=1e-16)
 def test_proton_inventory_scales_expected_counts(self):
  a,b=self.r['attempts'][0],self.r['attempts'][2];self.assertEqual(b['expected_reactions'],2*a['expected_reactions'])
  for key in ['COHERENT','PHASE_SPACE_NULL']:
   np.testing.assert_allclose(b['models'][key]['expected_geometry_accepted_true_exit_bins'],2*np.array(a['models'][key]['expected_geometry_accepted_true_exit_bins']))
 def test_bounded_energy_ledger_closes_without_heat_credit(self):
  for a in self.r['attempts']:
   for m in a['models'].values():
    total=m['expected_beam_kinetic_input_MeV']+m['expected_nuclear_Q_MeV'];proton=m['expected_unreacted_proton_exit_kinetic_MeV'];alpha=m['expected_alpha_exit_energy_bounds_MeV'];loss=m['primary_particle_loss_remainder_bounds_MeV']
    self.assertAlmostEqual(proton+alpha[1]+loss[0],total,places=9);self.assertAlmostEqual(proton+alpha[0]+loss[1],total,places=9)
    self.assertIsNone(m['recoverable_heat_MeV']);self.assertIsNone(m['net_energy_MeV']);self.assertIsNone(m['financial_result'])
 def test_event_four_momentum_conservation(self):
  self.assertLess(self.r['maximum_four_momentum_residual_MeV'],1e-8)
  for e in self.trace:
   a=np.array([v['birth_four_vector_LAB_MeV'] for v in e['alphas']]);self.assertEqual(a.shape,(3,4));self.assertTrue(np.isfinite(a).all())
 def test_MC_covariance_positive_semidefinite(self):
  for a in self.r['attempts']:
   for m in a['models'].values():self.assertGreaterEqual(np.linalg.eigvalsh(m['finite_importance_integration_covariance'])[0],-1e-12)
 def test_zero_target_has_zero_nuclear_output(self):
  c=config();c['total_atoms_cm2']=0;r,e=ref.execute(c);self.assertEqual(r['all_attempt_expected_reactions'],0);self.assertEqual(e,[])
 def test_unqualified_detector_and_calibration_claim_rejected(self):
  for key,value in [('detector_response',{'efficiency':1}),('run_class','CALIBRATED'),('material','OVERLEY_B10_ENRICHED')]:
   c=config();c[key]=value
   with self.assertRaises(ValueError):ref.execute(c)
 def test_calibrated_source_claim_rejected_even_with_zero_target(self):
  c=config();c['total_atoms_cm2']=0;c['source_config']['run_class']='CALIBRATED'
  with self.assertRaises(ValueError):ref.execute(c)
 def test_alpha0_not_admitted_as_pure2minus_fit_data(self):
  with self.assertRaises(ValueError):authorize('MUNCH_PREPRINT_V1_ALPHA0','coherent_shape_fit',projectile='proton',material='B11',energy_LAB_MeV=.675)
 def test_calibration_material_and_projectile_transfer_rejected(self):
  authorize('OVERLEY_DIGITIZED_PROTON_STOPPING','proton_stopping_calibration',projectile='proton',material='OVERLEY_B10_ENRICHED',energy_LAB_MeV=.675,state='cold')
  for projectile,material,state in [('alpha','OVERLEY_B10_ENRICHED','cold'),('proton','B11','cold'),('proton','OVERLEY_B10_ENRICHED','hot')]:
   with self.assertRaises(ValueError):authorize('OVERLEY_DIGITIZED_PROTON_STOPPING','proton_stopping_calibration',projectile=projectile,material=material,energy_LAB_MeV=.675,state=state)
 def test_shared_ancestry_preserved(self):
  rows={r['id']:r for r in load_catalog()['datasets']};self.assertEqual(rows['SIKORA2016_EVENT_NORMALIZATION']['experimental_ancestry_group'],rows['SPRAKER2012_SPECTRA']['experimental_ancestry_group'])
 def test_catalog_integrity_and_module_retention(self):
  self.assertEqual(len(load_catalog()['datasets']),6);a=audit();self.assertIsNone(a['coherent_exclusive_fit_dataset'])
  m=json.loads((ROOT/'MODULE_COVERAGE.json').read_text());self.assertEqual(m['retained_count'],26);self.assertTrue(all(x['installed_CAPEX'] is None for x in m['retained_modules']))

class PackagingTests(unittest.TestCase):
 def test_spectrum_reconstruction_is_explicit_in_portable_audit(self):
  rows={x['id']:x for x in audit(metadata_only=True)['datasets']}
  self.assertIn('RECONSTRUCTION',rows['SPRAKER2012_SPECTRA']['availability'])
  self.assertEqual(rows['SPRAKER2012_SPECTRA']['rows'],22100)
  self.assertIsNone(rows['SPRAKER2012_SPECTRA']['entries_excluded_from_automatic_use'])

if __name__=='__main__':unittest.main()
