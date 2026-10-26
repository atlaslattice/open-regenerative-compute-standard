import unittest
from texas_dpa_scenario import Case, simulate, cases

class Tests(unittest.TestCase):
    def test_baseline_zero(self):
        self.assertEqual(0,simulate(cases()[0])['import_displacement_bbl_y'])
    def test_incremental_not_total(self):
        r=simulate(cases()[2])
        self.assertEqual(20000*365*.3,r['incremental_qualified_distillate_bbl_y'])
    def test_access_fraction(self):
        r=simulate(cases()[2])
        self.assertAlmostEqual(20000*365*.3*.75,r['hypothetical_deliverable_bbl_y'])
    def test_imports_cap(self):
        r=simulate(Case('cap',1000000,1,1,1,0))
        self.assertEqual(45.424e6,r['import_displacement_bbl_y'])
    def test_export_diversion_offsets(self):
        r=simulate(cases()[4])
        self.assertEqual(0,r['first_order_merchandise_balance_change_usd_y'])
    def test_incremental_nondiversion(self):
        r=simulate(cases()[2])
        self.assertEqual(r['gross_import_goods_value_avoided_usd_y'],r['first_order_merchandise_balance_change_usd_y'])
    def test_nonexistent_net_gdp(self):
        r=simulate(cases()[2])
        self.assertIsNone(r['net_incremental_gdp_usd_y'])
        self.assertIsNone(r['total_domestic_turnover_increment_usd_y'])
    def test_no_export_authorization(self):
        self.assertFalse(simulate(cases()[2])['export_authorization'])
    def test_fraction_validation(self):
        with self.assertRaises(ValueError):
            simulate(Case('bad',100,2,1,1,0))
    def test_cost_validation(self):
        with self.assertRaises(ValueError):
            simulate(Case('bad',100,.2,1,1,0,domestic_freight_usd_per_bbl=-1))

if __name__=='__main__': unittest.main()
