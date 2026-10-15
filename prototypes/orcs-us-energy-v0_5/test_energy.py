import unittest
from energy_model import GridHour, accounting_gap, critical_load_coverage

class EnergyTest(unittest.TestCase):
    def test_unknown_not_zero(self):
        self.assertEqual('UNKNOWN', accounting_gap(GridHour('ERCO','2025-01-01T00:00Z',None,None))['status'])
    def test_balance_not_surplus(self):
        out=accounting_gap(GridHour('ERCO','2025-01-01T00:00Z',100,120,-20))
        self.assertEqual(0,out['accounting_gap_mw'])
        self.assertIsNone(out['surplus_mw'])
    def test_shortfall_not_blackout_probability(self):
        self.assertIsNone(accounting_gap(GridHour('ERCO','x',100,80,0))['blackout_risk'])
    def test_unknown_critical_inputs(self):
        self.assertEqual('UNKNOWN',critical_load_coverage(None,2,1,4)['status'])
    def test_no_invented_islanding(self):
        self.assertIsNone(critical_load_coverage(2,1,4,4)['can_cover'])
    def test_adequate_verified(self):
        self.assertTrue(critical_load_coverage(2,1,5,4,True,True)['can_cover'])
    def test_insufficient_verified(self):
        self.assertFalse(critical_load_coverage(2,1,3,4,True,True)['can_cover'])
    def test_negative_rejected(self):
        with self.assertRaises(ValueError):critical_load_coverage(-2,1,5,4)

if __name__=='__main__':unittest.main()
