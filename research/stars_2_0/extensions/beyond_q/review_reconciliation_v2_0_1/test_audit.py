from pathlib import Path
import json,unittest
from audit import number_rows,reconcile,PARENT

class ReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        p=json.loads((PARENT/'outputs/execution.json').read_text())['inputs']
        products=number_rows(PARENT/'outputs/annual_products_finance.csv')
        physical=[]
        for n in p['module_counts']:physical+=number_rows(PARENT/f'outputs/module_ledger_{n}.csv')
        cls.rows,cls.stages,cls.check=reconcile(products,physical,p)

    def test_equal_DD_branch_atoms(self):
        self.assertLess(self.check['largest_equal_branch_atom_ratio_error'],1e-9)
        r=next(x for x in self.rows if x['fleet_modules']==1 and x['year']==1)
        self.assertAlmostEqual(r['T_A_DD_birth_kg'],121.04130904279312,places=8)
        self.assertNotAlmostEqual(r['He3_A_DD_birth_kg'],r['T_B_gross_breeding_kg'])

    def test_decay_and_full_mass_balance_visible(self):
        r=next(x for x in self.rows if x['fleet_modules']==1 and x['year']==1)
        self.assertAlmostEqual(r['T_decay_kg'],2.964505424555794,places=8)
        self.assertLess(abs(r['T_accounting_residual_kg']),1e-8)

    def test_two_reactors_and_transfer_cancellation(self):
        rows=[r for r in self.stages if r['fleet_modules']==1 and r['year']==1]
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['T_transfer_out_kg'],rows[1]['T_transfer_in_kg'])
        self.assertGreater(rows[0]['T_consumed_kg'],0)
        self.assertGreater(rows[1]['He4_plasma_birth_kg'],0)

    def test_unsold_bank_retained_as_a_result(self):
        r=next(x for x in self.rows if x['fleet_modules']==50 and x['year']==60 and x['He3_overall_recovery_assumed']==.75 and x['price_case']=='requested_prices' and x['offtake_case']=='fleet_cap_stress')
        self.assertAlmostEqual(r['He3_unsold_bank_end_STP_L'],890924155.3669351,places=3)
        self.assertGreater(r['gross_He3_candidate_market_cap_share'],.01)

    def test_all_scenario_combinations_exist(self):
        keys={(r['fleet_modules'],r['He3_overall_recovery_assumed'],r['price_case'],r['offtake_case']) for r in self.rows}
        self.assertEqual(len(keys),24)
        self.assertEqual(len(self.rows),1440)

if __name__=='__main__':unittest.main()
