import unittest,json,copy
from pathlib import Path
from run_abc import run,payment

R=Path(__file__).resolve().parent
BASE=json.loads((R/'base-network-results.json').read_text())
CONFIG=json.loads((R/'scenario-inputs.json').read_text())['scenarios']

class ModelChecks(unittest.TestCase):
    def test_draws_principal_and_tail_reconcile(self):
        for cfg in CONFIG:
            r=run(BASE,cfg);s=r['summary'];a=r['annual']
            self.assertAlmostEqual(sum(x['capital_draw'] for x in a),s['installed_capital_with_planning_allowance'],places=3)
            self.assertAlmostEqual(sum(x['principal_repaid'] for x in a),s['installed_capital_with_planning_allowance'],places=3)
            self.assertLess(a[-1]['outstanding_principal'],.01)
            self.assertGreater(a[29]['outstanding_principal'],0)
            self.assertAlmostEqual(sum(x['principal_repaid'] for x in a[30:]),a[29]['outstanding_principal'],places=3)
    def test_loan_zero_rate(self):
        self.assertEqual(payment(300,0),10)
    def test_timing_and_maturity(self):
        for cfg in CONFIG:
            r=run(BASE,cfg);a=r['annual'];s=r['summary']
            self.assertEqual(a[0]['operating_fraction'],0)
            self.assertAlmostEqual(a[s['last_commissioning_year']-1]['commissioned_fraction'],1)
            self.assertAlmostEqual(a[s['last_commissioning_year']]['operating_fraction'],1)
            self.assertTrue(all(x['commissioned_fraction']<=1+1e-10 for x in a))
            self.assertTrue(all(a[i]['commissioned_fraction']<=a[i+1]['commissioned_fraction']+1e-10 for i in range(len(a)-1)))
    def test_physical_steady_outputs_match_inherited_model(self):
        for cfg in CONFIG:
            r=run(BASE,cfg);s=r['summary'];a=r['annual'][-1]
            self.assertAlmostEqual(a['new_net_power_MWh']/1e6,s['new_power_TWh_steady'])
            for k in ['N','P','K2O']:self.assertAlmostEqual(a['new_'+k+'_first_season_t'],s['new_first_season_nutrients_t'][k])
    def test_cash_and_debt_identity(self):
        for cfg in CONFIG:
            r=run(BASE,cfg)
            for a in r['annual']:
                self.assertAlmostEqual(a['interest']+a['principal_repaid'],a['debt_service'],places=4)
                self.assertAlmostEqual(a['modeled_receipts']-a['operating_costs_and_reserves']-a['construction_carry']-a['debt_service'],a['net_cash'],places=4)
                self.assertEqual(a['required_public_support'],max(0,-a['net_cash']))
    def test_higher_rate_same_physical_plan_increases_funding(self):
        c=copy.deepcopy(CONFIG[1]);low=run(BASE,c);c['interest_rate']=.07;high=run(BASE,c)
        self.assertGreater(high['summary']['public_support_first_30_years'],low['summary']['public_support_first_30_years'])
        self.assertEqual(high['summary']['new_power_TWh_steady'],low['summary']['new_power_TWh_steady'])
    def test_county_requirements_cannot_be_overridden(self):
        a=json.loads((R/'county-benefit-gates.json').read_text())
        self.assertEqual(len(a),3144);self.assertEqual(len({x['fips'] for x in a}),3144)
        self.assertTrue(all(x['reactor_required'] and x['state_wastewater_access_required'] and not x['regional_override_allowed'] for x in a))
        self.assertTrue(all(x['gate_status']=='MISSING_EVIDENCE' and x['verified_local_benefit'] is None for x in a))
    def test_no_unsourced_macro_credit(self):
        for c in CONFIG:
            s=run(BASE,c)['summary']
            for k in ['actual_import_displacement_t','net_GDP_effect_usd','net_trade_balance_effect_usd']:self.assertIsNone(s[k])
    def test_deterministic(self):
        self.assertEqual(run(BASE,CONFIG[1]),run(BASE,CONFIG[1]))

if __name__=='__main__':unittest.main(verbosity=2)
