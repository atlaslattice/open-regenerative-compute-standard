import json,math,unittest
from pathlib import Path
from calibrate import ROOT,analyse,fit_scale,adjusted_stopping,model_module,MATERIAL
from reproduce_gemini import inspect_outputs,EXPECTED,sha

class CalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=analyse();cls.model=model_module();cls.tables=cls.model.load_tables()

    def test_analytic_scale(self):
        self.assertAlmostEqual(fit_scale([2.,4.,8.],[1.,2.,4.]),2.)
        for y,x in [([],[]),([1],[1,2]),([0],[1]),([1],[math.nan])]:
            with self.assertRaises(ValueError):fit_scale(y,x)

    def test_log_objective_stationary_and_minimum(self):
        for m in self.result['models']:
            s=m['fit']['total_stopping_scale']
            logs=[math.log(r['observed_eV_cm2_atom']/(s*r['base_total_eV_cm2_atom'])) for r in m['residuals']]
            self.assertLess(abs(sum(logs)),1e-12)
            loss=lambda t:sum((x-math.log(t))**2 for x in logs)
            self.assertLess(loss(1.),loss(.99));self.assertLess(loss(1.),loss(1.01))

    def test_no_holdout_leakage_in_fit(self):
        for m in self.result['models']:
            seen=[]
            for f in m['energy_block_diagnostics']:
                train=f['training_indices'];held=f['held_out_indices'];seen+=held
                self.assertFalse(set(train)&set(held));self.assertEqual(set(train)|set(held),set(range(27)))
                r=m['residuals']
                expected=fit_scale([r[i]['observed_eV_cm2_atom'] for i in train],[r[i]['base_total_eV_cm2_atom'] for i in train])
                self.assertEqual(expected,f['total_stopping_scale'])
            self.assertEqual(sorted(seen),list(range(27)))

    def test_holdout_training_excludes_mutated_outcomes(self):
        m=self.result['models'][0];f=m['energy_block_diagnostics'][0];r=m['residuals']
        y=[x['observed_eV_cm2_atom'] for x in r]
        for i in f['held_out_indices']:y[i]*=1e6
        self.assertEqual(fit_scale([y[i] for i in f['training_indices']],
            [r[i]['base_total_eV_cm2_atom'] for i in f['training_indices']]),f['total_stopping_scale'])

    def test_material_species_and_domain_guards(self):
        fit=self.result['models'][0]['fit']
        for projectile,material,E in [('alpha',MATERIAL,.65),('proton','B11',.65),('proton','BN_B11_N14',.65),('proton',MATERIAL,.05),('proton',MATERIAL,4.),('proton',MATERIAL,math.nan)]:
            with self.assertRaises(ValueError):adjusted_stopping(self.model,self.tables,fit,projectile=projectile,material=material,E_MeV=E)

    def test_no_fitted_decomposition_or_fake_confidence(self):
        fit=self.result['models'][0]['fit'];r=adjusted_stopping(self.model,self.tables,fit,projectile='proton',material=MATERIAL,E_MeV=.65)
        self.assertGreater(r['epsilon_total_eV_cm2_atom'],0)
        self.assertIsNone(r['fitted_Se_Sn_decomposition']);self.assertIsNone(r['confidence_interval']);self.assertFalse(r['independent_validation'])

    def test_global_systematic_scale_is_coherent(self):
        m=self.result['models'][0];r=m['residuals'];y=[x['observed_eV_cm2_atom'] for x in r];p=[x['base_total_eV_cm2_atom'] for x in r]
        self.assertAlmostEqual(fit_scale([1.04*x for x in y],p),1.04*fit_scale(y,p))
        self.assertEqual(len(m['coherent_stress_cases']),8)

    def test_degraded_block_is_not_discarded(self):
        folds=self.result['models'][0]['energy_block_diagnostics']
        self.assertTrue(any(f['after']['rms_fractional_discrepancy']>f['before']['rms_fractional_discrepancy'] for f in folds))

    def test_repeat_calculation(self):self.assertEqual(self.result,analyse())

class ReproductionTests(unittest.TestCase):
    def test_exact_original_bytes(self):
        raw=(ROOT/'original/GEMINI_V04_ATTACHMENT.md').read_bytes()
        code=ROOT/'original/stars_v04_original_extracted.py'
        self.assertEqual(b''.join(raw.splitlines(keepends=True)[1:-1]),code.read_bytes());self.assertEqual(sha(code),EXPECTED)

    def test_independent_physical_mass_gate_rejects_original(self):
        r=inspect_outputs(ROOT/'receipts/gemini_original_run003')
        self.assertEqual(r['physical_mass_conservation_status'],'FAIL');self.assertFalse(r['qualified_for_calibrated_source'])
        self.assertGreater(r['max_abs_physical_longitudinal_momentum_residual_MeV_c'],1e-8)
        self.assertGreater(r['max_abs_physical_energy_residual_MeV'],1e-8)

if __name__=='__main__':unittest.main()
