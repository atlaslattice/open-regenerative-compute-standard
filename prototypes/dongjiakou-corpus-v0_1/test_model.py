import json
import unittest
from pathlib import Path
from model import (water_balance, residual_envelope, allocate_minerals,
                   fate_gate, complete_total, domestic_component_share,
                   heat_match, crf, run)

class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=json.loads((Path(__file__).parent/'inputs.json').read_text())
        cls.result=run(cls.inputs)

    def test_water_and_salt_conservation_across_scenarios(self):
        for mgd in [1,30,50,100]:
            for plant in [.4,.425,.45]:
                b=water_balance(mgd,plant,.475)
                self.assertAlmostEqual(b['intake_m3_d'],b['product_m3_d']+b['pretreatment_residual_m3_d']+b['ro_concentrate_m3_d'])
                self.assertAlmostEqual(b['total_feed_salt_t_d'],b['pretreatment_salt_t_d']+b['ro_concentrate_salt_t_d'])
    def test_recovery_boundaries(self):
        for plant,ro in [(0,.5),(.6,.5),(.4,1)]:
            with self.assertRaises(ValueError):water_balance(30,plant,ro)
        self.assertEqual(water_balance(30,.45,.45)['pretreatment_residual_m3_d'],0)
    def test_residual_is_not_destroyed_by_zld(self):
        b=self.result['base']
        for r in [0,.5,.8,1]:
            e=residual_envelope(b,r)
            self.assertAlmostEqual(e['additional_water_m3_d']+e['remaining_liquid_m3_d'],b['combined_residual_m3_d'])
            self.assertEqual(e['conserved_salt_inventory_t_d'],b['total_feed_salt_t_d'])
            self.assertIsNone(e['capex_usd'])
        self.assertIsNone(residual_envelope(b,1)['apparent_salt_kg_m3'])
    def test_annual_availability_applied_once(self):
        self.assertAlmostEqual(self.result['annual_product_m3'],30*3785.411784*365*.9)
    def test_ion_conservation_competing_products(self):
        for mg in ['MgOH2','MgCl2']:
            for ca in ['gypsum','CaCO3']:
                for f in [0,.5,1]:
                    a=allocate_minerals(239078.64,self.inputs['representative_ions_mg_l'],f,mg,ca)
                    for ion,initial in a['initial_ions_t_d'].items():
                        consumed=sum(p['consumed_feed_ions_t_d'].get(ion,0) for p in a['products'])
                        self.assertAlmostEqual(initial,consumed+a['remaining_ions_t_d'][ion])
                        self.assertGreaterEqual(a['remaining_ions_t_d'][ion],-1e-9)
                    self.assertEqual(a['accepted_products_t_d'],0)
    def test_chloride_limiting_inventory(self):
        ions=self.inputs['representative_ions_mg_l'].copy();ions['Cl']=1
        a=allocate_minerals(1000,ions,1,'MgCl2','gypsum')
        self.assertLess(a['remaining_ions_t_d']['Cl'],1e-10)
        self.assertAlmostEqual(next(p['theoretical_t_d'] for p in a['products'] if p['product']=='NaCl'),0)
    def test_fate_gate_cannot_be_satisfied_by_relocation(self):
        self.assertEqual(fate_gate([]),'UNRESOLVED')
        self.assertEqual(fate_gate([{'permitted':True}]),'UNRESOLVED')
        self.assertEqual(fate_gate([{'permitted':True,'final_fate_verified':True,'routine_marine_release':True}]),'FAIL')
        self.assertEqual(fate_gate([{'permitted':True,'final_fate_verified':True,'routine_marine_release':False}]),'PASS_WITHIN_DECLARED_STREAM_BOUNDARY')
    def test_missing_cost_is_not_zero(self):
        self.assertIsNone(complete_total({'pump':5,'zld':None})['total'])
        self.assertEqual(complete_total({'pump':5,'zld':None})['known_subtotal'],5)
        self.assertIsNone(self.result['all_in_cost']['total'])
    def test_final_assembly_does_not_change_component_share(self):
        self.assertEqual(domestic_component_share(40,60,10000),.4)
    def test_heat_exchanger_approach(self):
        self.assertFalse(heat_match(60,60));self.assertTrue(heat_match(70,65))
    def test_compute_can_increase_net_consumption(self):
        row=next(x for x in self.result['energy_sensitivity'] if x['water_sec_kwh_m3']==2.2 and x['additional_compute_it_kw']==1000 and x['assumed_water_energy_saving']==.05)
        self.assertGreater(row['incremental_energy_vs_water_only_kwh_y'],0)
    def test_zero_realized_and_unresolved_clearance(self):
        self.assertTrue(all(v==0 for v in self.result['realized_credits'].values()))
        self.assertEqual(self.result['environmental_clearance'],'UNRESOLVED')
    def test_finance_zero_rate(self):
        self.assertAlmostEqual(crf(0,30),1/30)

if __name__=='__main__':unittest.main()
