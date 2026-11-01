import hashlib,json,math,unittest
import run as r

class ReconciliationChecks(unittest.TestCase):
    def test_physics_inputs_and_controller_are_unchanged(self):
        expected=json.loads((r.OUT/'reconciliation_baseline_hashes.json').read_text())
        for name,sha in expected.items():
            b=(r.ROOT/name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),sha)
    def test_equal_births_and_separate_route_identities(self):
        data=json.loads((r.OUT/'capture_benchmark.json').read_text())
        self.assertEqual(data['equal_path_reference_He3_STP_L'],350000)
        self.assertEqual(data['equal_path_reference_T_atom_STP_L'],350000)
        for x in r.paired.readcsv(r.OUT/'capture_difference_bridge.csv'):
            gross=float(x['gross_T_branch_atom_STP_L'])
            self.assertTrue(math.isclose(gross,float(x['gross_He3_branch_STP_L']),rel_tol=1e-11))
            self.assertLess(abs(float(x['T_identity_residual_STP_L']))/gross,1e-11)
            self.assertLess(abs(float(x['He3_identity_residual_STP_L']))/gross,1e-11)
        self.assertFalse(data['physics_inputs_changed']);self.assertFalse(data['physical_validation'])
    def test_reconstruction_reproduces_existing_outputs(self):
        ref={x['year']:x for x in r.paired.readcsv(r.OUT/'reference_350k.csv')}
        for x in r.paired.readcsv(r.OUT/'capture_difference_bridge.csv'):
            y=ref[x['year']]
            self.assertAlmostEqual(float(x['T_recovered_atom_STP_L']),float(y['T_atom_equivalent_STP_L']),places=6)
            self.assertAlmostEqual(float(x['He3_captured_STP_L']),float(y['He3_total_captured_STP_L']),places=6)
        b=json.loads((r.OUT/'capture_benchmark.json').read_text())
        self.assertGreater(b['observed_year2_T_to_He3_ratio'],1.)
        self.assertIsInstance(b['finite_minus_asymptotic_ratio'],float)
if __name__=='__main__':unittest.main()
