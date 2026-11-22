import unittest
from screen import screen

def case(**changes):
    x=dict(mode='CONTINUOUSLY_DRIVEN',startup_wall_J=10,sustaining_wall_J=100,auxiliary_wall_J=10,
           fusion_J=100,alpha_self_heat_fraction=.3,alpha_collection_fraction=.5,
           conversion_efficiency=.4,duration_s=2)
    x.update(changes);return screen(**x)
class Tests(unittest.TestCase):
    def test_independent_arithmetic(self):
        r=case();self.assertEqual(r['net_electric_J'],-100);self.assertEqual(r['fusion_J_required_for_electric_breakeven'],600)
    def test_zero_fusion_no_output(self):self.assertEqual(case(fusion_J=0)['gross_electric_J'],0)
    def test_zero_conversion_undefined_threshold(self):self.assertIsNone(case(conversion_efficiency=0)['fusion_J_required_for_electric_breakeven'])
    def test_no_double_alpha_credit(self):
        with self.assertRaises(ValueError):case(alpha_self_heat_fraction=.6)
    def test_startup_not_omitted(self):
        a=case(startup_wall_J=0);b=case(startup_wall_J=10)
        self.assertEqual(a['net_electric_J']-b['net_electric_J'],10)
    def test_hidden_sustaining_drive_rejected(self):
        with self.assertRaises(ValueError):case(mode='STARTUP_THEN_BURN_HYPOTHESIS')
    def test_positive_screen_never_proves_ignition(self):
        r=case(fusion_J=1000);self.assertGreater(r['net_electric_J'],0)
        self.assertTrue(r['ignition_status'].startswith('NOT_EVALUATED'))
    def test_invalid_inputs(self):
        for x in [-1,float('nan'),float('inf')]:
            with self.subTest(x=x),self.assertRaises(ValueError):case(fusion_J=x)
if __name__=='__main__':unittest.main()
