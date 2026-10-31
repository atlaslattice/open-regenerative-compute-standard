import csv,json,math,unittest
import account as a

class Checks(unittest.TestCase):
    def test_helium_no_source(self):
        r=dict(time_hours=1,dd_events=0,dd_t_atoms=0,decay=0)
        self.assertEqual(a.helium([r],1,.9)[0]['He3_stored_candidate_kg'],0)
    def test_capture_zero_is_no_revenue_inventory(self):
        r=dict(time_hours=24,dd_events=2e20,dd_t_atoms=1e20,decay=0)
        h=a.helium([r],1,0)[0]
        self.assertEqual(h['He3_stored_candidate_kg'],0)
        self.assertAlmostEqual(h['He3_direct_born_kg'],h['He3_mobile_kg']+h['He3_capture_loss_kg'])
    def test_constant_source_analytic(self):
        r=dict(time_hours=24,dd_events=2e20,dd_t_atoms=1e20,decay=0)
        h=a.helium([r],2,.9)[0];born=1e20*a.HE3_KG_PER_ATOM
        mobile=born*(1-math.exp(-2))/2
        self.assertTrue(math.isclose(h['He3_mobile_kg'],mobile,rel_tol=1e-14))
        self.assertTrue(math.isclose(h['He3_stored_candidate_kg'],(born-mobile)*.9,rel_tol=1e-14))
    def test_decay_atom_conversion_not_equal_mass(self):
        h=a.helium([dict(time_hours=1,dd_events=0,dd_t_atoms=0,decay=1)],1,.9)[0]
        self.assertTrue(math.isclose(h['He3_T_decay_born_kg']/a.HE3_KG_PER_ATOM,1/a.T_KG_PER_ATOM))
        self.assertNotEqual(h['He3_T_decay_born_kg'],1)
        self.assertEqual(h['He3_stored_candidate_kg'],0)
    def test_terminal_allocations_disjoint(self):
        r=dict(a_store=5,b_store=8,total_inventory=15);h=dict(He3_stored_candidate_kg=10)
        x=a.terminal_allocation(r,h,10,.5,.9)
        self.assertEqual(x['T_terminal_sale_candidate_kg'],0)
        self.assertEqual(x['T_storage_above_assumed_reserve_kg'],3)
        self.assertEqual(x['T_storage_after_sale_kg'],13)
        self.assertEqual(a.terminal_allocation(r,h,10,.5,.9,T_policy='sell_terminal')['T_terminal_sale_candidate_kg'],3)
        self.assertEqual(x['He3_retained_kg']+x['He3_quality_held_kg']+x['He3_terminal_sale_candidate_kg'],10)
        self.assertEqual(a.terminal_allocation(r,h,100,.5,.9)['T_terminal_sale_candidate_kg'],0)
    def test_unqualified_is_not_revenue(self):
        self.assertIsNone(a.realized_revenue(10,None,10,100))
        self.assertIsNone(a.realized_revenue(10,10,None,100))
    def test_demand_cap_and_excess_qualification(self):
        self.assertEqual(a.realized_revenue(10,8,2,100),200)
        with self.assertRaises(ValueError):a.realized_revenue(10,11,2,100)
    def test_threshold_no_inventory(self):
        self.assertIsNone(a.threshold(100,0))
        self.assertEqual(a.threshold(100,10),10)
    def test_tritium_birth_sink_ledger(self):
        rows=csv.DictReader((a.OUT/'isotope_birth_sink_ledger.csv').read_text().splitlines())
        for r in rows:
            born=sum(float(r[k]) for k in ('T_DD_gross_birth_kg','T_A_blanket_gross_birth_kg','T_B_blanket_gross_birth_kg'))
            sinks=sum(float(r[k]) for k in ('T_A_internal_burn_kg','T_B_burn_kg','T_decay_kg','T_processing_loss_kg','T_permeation_kg'))
            self.assertAlmostEqual(born-sinks,float(r['T_mobile_inventory_change_kg']),places=8)
    def test_normalized_source_comparison(self):
        rows=list(csv.DictReader((a.OUT/'source_comparison.csv').read_text().splitlines()))
        self.assertAlmostEqual(float(rows[0]['T_branch_fraction']),.5)
        self.assertNotEqual(float(rows[0]['T_branch_fraction']),float(rows[1]['T_branch_fraction']))
        self.assertEqual(rows[1]['reactor_annual_output_kg'],'')
    def test_direct_capture_reference(self):
        from direct_capture_reference import evaluate
        r=evaluate('test',500,500,.85,.8)
        self.assertAlmostEqual(r['He3_STP_L'],341442.9071558655,places=5)
        self.assertAlmostEqual(r['T_atom_equivalent_STP_L'],2*r['T2_molecular_STP_L'])
        self.assertEqual(r['decay_He3_credit_kg'],0)
        self.assertGreater(r['direct_T_balance_before_internal_burn_delays_losses_reserves_kg'],0)
    def test_generation_is_not_sales(self):
        for r in csv.DictReader((a.OUT/'terminal_allocations.csv').read_text().splitlines()):
            self.assertEqual(r['realized_He3_revenue_USD'],'')
            self.assertEqual(r['realized_T_revenue_USD'],'')
            self.assertLessEqual(float(r['He3_terminal_sale_candidate_kg']),float(r['He3_direct_born_kg'])+1e-9)
            self.assertLess(abs(float(r['He3_residual_kg'])),1e-8)

if __name__=='__main__':unittest.main()
