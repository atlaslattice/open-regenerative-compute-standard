import copy,json,math,unittest
from pathlib import Path
import numpy as np
from model import simulate,advance,MEV,T_ATOM,YEAR
from finance import connected_financials,annuity
ROOT=Path(__file__).resolve().parent

class ResearchChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=json.loads((ROOT/'inputs.json').read_text());cls.p['years']=1
        cls.rows,_,cls.check=simulate(cls.p,1)

    def test_compartment_matches_scalar_reference(self):
        import sys
        sys.path.insert(0,str(ROOT.parent/'reserve_dispatch_v1_8'))
        from dispatchcycle.inventory import advance as scalar
        for dt in [1e-9,.25,10]:
            x,e=advance(np.array([3.]),.8,{'a':.1,'b':9.},dt)
            sx,se=scalar(3.,.8,{'a':.1,'b':9.},dt)
            self.assertAlmostEqual(float(x[0]),sx,places=12)
            self.assertAlmostEqual(float(e['a'][0]),se['a'],places=12)

    def test_tritium_export_is_a_sink(self):
        r=self.rows[0]
        residual=r['T_start_kg']+r['dd_birth']+r['b_birth']-r['a_burn']-r['b_burn']-r['decay']-r['permeation']-r['process_loss']-r['exports']-r['T_end_kg']
        self.assertLess(abs(residual),1e-8)
        self.assertLessEqual(r['exports'],self.p['T_export_cap_kg_per_module_year'])
        self.assertGreaterEqual(r['T_B_storage_end_kg'],self.check['startup_B_threshold_kg'])

    def test_startup_does_not_import_T(self):
        self.assertEqual(self.p['initial_T_kg'],0)
        self.assertGreater(self.rows[0]['startup_day'],0)
        self.assertEqual(self.check['unserved_B_T_kg'],0)

    def test_no_source_no_products_or_B_start(self):
        p=copy.deepcopy(self.p);p['A_macro_availability']=0
        rows,_,check=simulate(p,1)
        self.assertEqual(rows[0]['dd_birth'],0);self.assertEqual(rows[0]['b_burn'],0)
        self.assertEqual(rows[0]['he3_born'],0);self.assertEqual(rows[0]['exports'],0)
        self.assertIsNone(rows[0]['startup_day']);self.assertEqual(check['final_T_kg'],0)

    def test_no_B_breeding_does_not_remove_DD_neutrons(self):
        p=copy.deepcopy(self.p);p['B_gross_TBR_assumed']=0
        rows,_,check=simulate(p,1)
        self.assertEqual(rows[0]['b_birth'],0)
        self.assertGreater(rows[0]['primary_DD_neutrons'],0)
        self.assertLess(check['max_T_mass_residual_kg'],1e-8)

    def test_no_secondary_T_burn_preserves_primary_source(self):
        p=copy.deepcopy(self.p);p['A_T_burn_day']=0;p['A_T_fast_burn_fraction']=0
        rows,_,_=simulate(p,1)
        self.assertEqual(rows[0]['a_burn'],0)
        self.assertAlmostEqual(rows[0]['primary_DD_neutrons'],self.rows[0]['primary_DD_neutrons'])

    def test_source_energy_and_neutrons(self):
        r=self.rows[0]
        self.assertAlmostEqual(r['DD_fusion_J']/(r['primary_DD_neutrons']*2*3.65*MEV),1.,places=10)
        self.assertAlmostEqual(r['DT_neutrons']/((r['a_burn']+r['b_burn'])/T_ATOM),1.,places=10)

    def test_recovery_applied_once(self):
        low=connected_financials(self.rows,self.p,.375)[0]
        high=connected_financials(self.rows,self.p,.75)[0]
        self.assertAlmostEqual(high['He3_product_candidate_STP_L'],2*low['He3_product_candidate_STP_L'])
        self.assertAlmostEqual(low['He3_retained_STP_L'],low['He3_product_candidate_STP_L']*.5)
        self.assertIsNone(low['actual_qualified_sales_USD'])

    def test_market_cap_and_unsold_inventory(self):
        p=copy.deepcopy(self.p);p['He3_market_cap_STP_L_per_year_fleet']=1
        r=connected_financials(self.rows,p,.75)[0]
        self.assertEqual(r['He3_sale_candidate_STP_L'],1)
        self.assertAlmostEqual(r['He3_unsold_bank_end_STP_L']+r['He3_sale_candidate_STP_L']+r['He3_retained_STP_L'],r['He3_product_candidate_STP_L'])

    def test_missing_costs_never_become_profit(self):
        r=connected_financials(self.rows,self.p,.75)[0]
        self.assertIsNone(r['annual_OPEX_USD']);self.assertIsNone(r['conditional_cash_flow_before_tax_USD'])
        self.assertIsNone(r['actual_profit_USD']);self.assertFalse(r['capital_scope_complete'])

    def test_financing_amortizes_and_costs_add_once(self):
        balance=5.9e9;payment=annuity(balance,.05,30)
        for _ in range(30):balance=balance*1.05-payment
        self.assertLess(abs(balance),.001)
        self.assertEqual(annuity(300,0,30),10)
        p=copy.deepcopy(self.p);p.update(A_housing_site_USD=1e8,B_housing_site_USD=1e8,shared_site_USD=1e8)
        r=connected_financials(self.rows,p,.75)[0]
        self.assertAlmostEqual(r['debt_service_USD_if_capital_incomplete_is_partial'],annuity(6.2e9,.05,30))

    def test_50_independent_commissioning_and_one_market_cap(self):
        rows,_,check=simulate(self.p,50)
        self.assertEqual(len(rows),50)
        self.assertEqual(rows[-1]['dd_birth'],0)
        f=connected_financials(rows,self.p,.75)[0]
        self.assertLessEqual(f['He3_sale_candidate_STP_L'],self.p['He3_market_cap_STP_L_per_year_fleet'])
        self.assertLessEqual(sum(r['exports'] for r in rows),self.p['T_market_cap_kg_per_year_fleet'])
        self.assertLess(check['max_T_mass_residual_kg'],1e-8)

    def test_timestep_refinement(self):
        p=copy.deepcopy(self.p);p['step_days']=.125
        rows,_,_=simulate(p,1)
        self.assertLess(abs(rows[0]['b_burn']-self.rows[0]['b_burn'])/max(1,rows[0]['b_burn']),.02)
        self.assertAlmostEqual(rows[0]['he3_born'],self.rows[0]['he3_born'],places=8)

    def test_negative_energy_case_stays_negative(self):
        p=copy.deepcopy(self.p);p['A_net_draw_MW_assumed']=800
        rows,_,_=simulate(p,1)
        self.assertLess(rows[0]['net_MWh'],0);self.assertGreater(rows[0]['import_MWh'],0)

    def test_invalid_market_and_recovery_fail_visibly(self):
        p=copy.deepcopy(self.p);p['He3_market_cap_STP_L_per_year_fleet']=-1
        with self.assertRaises(ValueError):connected_financials(self.rows,p,.75)
        p=copy.deepcopy(self.p);p['He3_overall_recovery_cases']=[1.1]
        with self.assertRaises(ValueError):simulate(p,1)

    def test_fully_specified_cost_case_is_still_conditional(self):
        p=copy.deepcopy(self.p)
        for k in ['A_housing_site_USD','B_housing_site_USD','shared_site_USD','annual_operating_USD_per_module',
                  'replacement_cost_USD_each_reactor','construction_interest_fees_USD_per_module',
                  'decommissioning_reserve_USD_per_module_year']:p[k]=1e6
        p['housing_not_in_chassis_verified']=True;p['electricity_export_USD_per_kWh']=.05
        r=connected_financials(self.rows,p,.75)[0]
        self.assertIsInstance(r['conditional_cash_flow_before_tax_USD'],float)
        self.assertIsNone(r['actual_profit_USD'])

if __name__=='__main__':unittest.main()
