"""Regression guards for exposure, boundary duplication and isotope custody."""
import json
import math
import unittest
from audit import ROOT, gross_liters, product_ledger, decay_comparator


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.p = json.loads((ROOT / 'inputs.json').read_text())

    def test_paste_normalization(self):
        born = gross_liters(self.p, .85)
        self.assertAlmostEqual(born, 938967.9946786301, places=6)
        self.assertAlmostEqual(product_ledger(born, overall=.375)['product_candidate'], 352112.9980044863, places=6)

    def test_parent_separate_duty(self):
        self.assertAlmostEqual(gross_liters(self.p, .85 * .9375) / gross_liters(self.p, .85), .9375)

    def test_no_double_recovery(self):
        with self.assertRaises(ValueError):
            product_ledger(100, overall=.75, stages={'capture': .75})

    def test_chain_losses_close(self):
        result = product_ledger(100, stages={'plasma_survival': .7, 'exhaust': .9, 'pump': .9, 'purification': .95})
        self.assertAlmostEqual(result['product_candidate'], 53.865)
        self.assertAlmostEqual(result['closure_residual'], 0)
        self.assertLess(result['product_candidate'], 70)

    def test_zero_source_and_invalid_survival(self):
        self.assertEqual(product_ledger(0, overall=.9)['product_candidate'], 0)
        for value in [-.1, 1.1, math.nan, math.inf]:
            with self.assertRaises(ValueError):
                product_ledger(100, overall=value)

    def test_decay_inventory_and_delay(self):
        r = decay_comparator(self.p)
        ratio = self.p['He3_molar_mass_g'] / self.p['T_molar_mass_g']
        lam = math.log(2) / self.p['T_half_life_years']
        self.assertAlmostEqual(r['required_T_aging_inventory_kg'] * lam * ratio, 1.97)
        t = r['empty_store_years_to_target_flow']
        self.assertAlmostEqual(4 / lam * (-math.expm1(-lam*t)), r['required_T_aging_inventory_kg'])
        self.assertLess(r['first_year_He3_mass_kg'], .12)
        self.assertGreater(t, 12)

    def test_historical_claim_not_enabled_calibration(self):
        self.assertFalse(self.p['historical_benchmark']['calibration_enabled'])
        self.assertIn('Full article equations and parameter tables', self.p['historical_benchmark']['missing'])


if __name__ == '__main__':
    unittest.main()
