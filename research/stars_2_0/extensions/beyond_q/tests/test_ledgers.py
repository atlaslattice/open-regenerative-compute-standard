import importlib.util
import math
import unittest
from pathlib import Path

p=Path(__file__).resolve().parents[1]/'models/rebuild_ledgers.py'
s=importlib.util.spec_from_file_location('ledgers',p)
m=importlib.util.module_from_spec(s)
s.loader.exec_module(m)


class AccountingTests(unittest.TestCase):
    def test_no_reactions_at_zero_power_or_availability(self):
        self.assertEqual(m.dd_births(0,.85),(0,0))
        self.assertEqual(m.dd_births(25,0),(0,0))
        self.assertEqual(m.dt_burn(525,0),0)

    def test_branch_endpoints_and_energy_closure(self):
        for f in [0,.1,.5,.9,1]:
            h,t=m.dd_births(25,.85,f)
            energy=(h*m.Q_DD_HE3+t*m.Q_DD_T)*1e6*m.EV_J
            self.assertTrue(math.isclose(energy,25e6*.85*365*86400,rel_tol=1e-12))
            self.assertTrue(math.isclose(h/(h+t),f,abs_tol=1e-12))

    def test_direct_fuel_balance_ratio_independent_of_calendar(self):
        # Analytic ratio: equal CF cancels; one T per D-T event.
        _,t=m.dd_births(25,.85)
        ratio=t*.8/m.dt_burn(525,.85)
        self.assertTrue(math.isclose(ratio,(25/525)*(17.6/3.65)*.5*.8))
        self.assertLess(ratio,.1)

    def test_invalid_physical_inputs_rejected(self):
        for args in [(-1,.85,.5),(25,1.1,.5),(25,.85,-.1)]:
            with self.assertRaises(ValueError):m.dd_births(*args)


if __name__=='__main__':unittest.main()
