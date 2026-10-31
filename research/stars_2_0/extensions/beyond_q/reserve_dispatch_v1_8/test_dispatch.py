import csv,json,math,sys,unittest
import run as r
from controller import Controller
from dispatchcycle.model import simulate

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.i=json.loads((r.ROOT/'inputs.json').read_text());cls.rows=r.paired.readcsv(r.OUT/'annual_dispatch.csv');cls.e=r.paired.readcsv(r.OUT/'annual_energy.csv')
    def test_canonical_power_and_projection_separate(self):
        self.assertEqual(self.i['A_fusion_power_MW'],1100);self.assertEqual(self.i['A_projected_net_electric_MW_owner_historical'],20)
        self.assertIsNone(self.i['B_published_TBR_numeric'])
    def test_uncontrolled_engine_replay(self):
        c=json.loads((r.PARENT/'paired_annual_v1_7/inputs.json').read_text())['configurations'][1]
        p=r.paired.parameters(c,'B_replacement_A0',48,24,1/96);s=[(1,0)]*48+[(1,1)]*24
        a,_=r.paired.simulate(p,s);b,_=simulate(p,s)
        self.assertEqual(a,b)
    def test_policy_cannot_override_maintenance(self):
        c=json.loads((r.PARENT/'paired_annual_v1_7/inputs.json').read_text())['configurations'][1]
        p=r.paired.parameters(c,'B_replacement_A0',0,1,1/96)
        with self.assertRaises(ValueError):simulate(p,[(0,0)],schedule_policy=lambda *args:(1,0))
    def test_reserve_hysteresis_and_emergency(self):
        i=dict(self.i,precharge_hours=0);p=dict(always_on=False,He3_external_candidate_target_STP_L_per_year=0)
        ctl=Controller(i,p);c=dict(dd_events=0,dd_t_atoms=0)
        self.assertEqual(ctl(24,dict(b_store=21),c,(1,1))[0],0)
        self.assertEqual(ctl(25,dict(b_store=5),c,(1,1))[0],1)
        self.assertEqual(ctl(26,dict(b_store=5),c,(0,0)),(0,0))
    def test_yearly_T_closure(self):
        for x in self.rows:
            born=float(x['T_DD_birth_kg'])+float(x['T_B_blanket_birth_kg'])
            sinks=sum(float(x[k]) for k in ['T_A_burn_kg','T_B_burn_kg','T_decay_kg','T_process_loss_kg','T_permeation_kg'])
            self.assertAlmostEqual(born-sinks,float(x['T_stock_change_kg']),places=7)
    def test_no_inventory_reset_at_new_year(self):
        for tbr in self.i['B_gross_TBR_sensitivities']:
            for policy in self.i['policies']:
                rows=sorted([x for x in self.rows if float(x['B_gross_TBR_assumed'])==tbr and x['policy']==policy['id']],key=lambda x:int(x['year']))
                self.assertEqual(len(rows),4)
                for a,b in zip(rows,rows[1:]):
                    self.assertEqual(a['T_end_kg'],b['T_start_kg'])
                    for n in (3,4):self.assertAlmostEqual(float(a[f'He{n}_start_captured_kg'])+float(a[f'He{n}_captured_to_store_kg']),float(b[f'He{n}_start_captured_kg']),places=8)
    def test_reserve_only_reduces_A_runtime(self):
        for tbr in self.i['B_gross_TBR_sensitivities']:
            total=lambda policy:sum(float(x['A_on_hours']) for x in self.rows if x['policy']==policy and float(x['B_gross_TBR_assumed'])==tbr)
            self.assertLess(total('reserve_only'),total('always_on'))
    def test_unreachable_production_target_is_visible(self):
        self.assertTrue(any(float(x['He3_target_shortfall_STP_L'])>1000 for x in self.rows if x['policy']=='reserve_He3_500k' and int(x['year'])>0))
    def test_no_T_sale_no_actual_revenue_or_profit(self):
        for x in self.rows:self.assertEqual(float(x['T_external_sales_kg']),0);self.assertEqual(x['actual_revenue_USD'],'')
        for x in self.e:self.assertEqual(x['profit_USD'],'');self.assertEqual(x['total_cost_USD'],'')
    def test_unknown_A_energy_stays_unknown(self):
        rows=[x for x in self.e if 'unknown' in x['energy_case']];self.assertTrue(rows)
        self.assertTrue(all(x['net_J']=='' for x in rows))
    def test_energy_draw_and_interval_import_balance(self):
        for x in self.e:
            if x['net_J']=='':continue
            n=float(x['net_J'])
            self.assertTrue(math.isclose(float(x['generated_J'])-float(x['draw_J']),n,rel_tol=1e-10,abs_tol=2))
            self.assertTrue(math.isclose((float(x['positive_before_export_kWh'])-float(x['import_kWh']))*r.paired.KWH,n,rel_tol=1e-10,abs_tol=2))
    def test_helium_and_T_case_conservation(self):
        checks=json.loads((r.OUT/'checks.json').read_text())
        for x in checks['cases']:
            self.assertLess(abs(x['He3_mass_residual_kg']),1e-8);self.assertLess(abs(x['He4_mass_residual_kg']),1e-8);self.assertLess(x['max_T_mass_residual_kg'],1e-7)
        self.assertFalse(checks['physical_validation'])
if __name__=='__main__':unittest.main()
