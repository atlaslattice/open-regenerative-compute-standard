import json,math,unittest
import run as r
from target_controller import Controller

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.i=json.loads((r.ROOT/'inputs.json').read_text());cls.rows=r.paired.readcsv(r.OUT/'annual_dispatch.csv');cls.e=r.paired.readcsv(r.OUT/'annual_energy.csv')
    def test_total_capture_targets_not_sales_targets(self):
        p=self.i['policies'][0]
        self.assertEqual(p['He3_total_captured_target_STP_L_per_year'],350000)
        self.assertEqual(p['T_total_recovered_target_STP_L_per_year'],350000)
        for retained in (0.,1.):
            i=dict(self.i,precharge_hours=0,He3_retained_fraction=retained)
            ctl=Controller(i,p);ctl.year=0;ctl.stored=350001/22.414*.0030160293201
            c=dict(dd_events=0,dd_t_atoms=0,a_plasma_processed=350001/22.414*.00301604928)
            self.assertEqual(ctl(24,dict(b_store=30),c,(1,1))[0],0)
    def test_missing_volume_convention_rejected(self):
        p=dict(self.i['policies'][0],T_volume_convention='unspecified')
        with self.assertRaises(ValueError):Controller(self.i,p)
    def test_STP_and_molecular_factor_two(self):
        for x in self.rows:
            self.assertAlmostEqual(float(x['T_atom_equivalent_STP_L']),2*float(x['T2_molecular_STP_L']),places=7)
            self.assertAlmostEqual(float(x['T_A_direct_recovered_to_store_kg']),float(x['T_atom_equivalent_STP_L'])/22.414*.00301604928,places=10)
    def test_B_is_scheduled_every_post_start_hour(self):
        s=r.permitted(self.i);pre=self.i['precharge_hours']
        self.assertTrue(all(b==0 for a,b in s[:pre]));self.assertTrue(all(b==1 for a,b in s[pre:]))
        for x in self.rows:
            if int(x['year']):self.assertEqual(float(x['B_on_hours']),8766)
    def test_targets_met_in_reference(self):
        for x in self.rows:
            if x['policy']=='captured350k_atom_equivalent' and float(x['B_gross_TBR_assumed'])==1 and int(x['year']):
                self.assertLess(float(x['He3_total_captured_shortfall_STP_L']),1e-6);self.assertLess(float(x['T_target_shortfall_STP_L']),1e-6)
    def test_direct_delivery_minus_gross_burn_is_not_campus_surplus(self):
        rows=[x for x in self.rows if x['policy']=='captured350k_atom_equivalent' and float(x['B_gross_TBR_assumed'])==1 and int(x['year'])]
        self.assertTrue(rows)
        for x in rows:
            self.assertLess(float(x['T_A_delivery_minus_B_burn_without_B_breeding_kg']),0)
            self.assertGreater(float(x['T_stock_change_kg']),0)
            self.assertAlmostEqual(float(x['T_B_blanket_birth_kg']),float(x['T_B_burn_kg']),places=8)
    def test_zero_breeding_control_produces_no_blanket_source(self):
        for x in self.rows:
            if float(x['B_gross_TBR_assumed'])==0:self.assertEqual(float(x['T_B_blanket_birth_kg']),0)
    def test_yearly_T_conservation(self):
        for x in self.rows:
            born=float(x['T_DD_birth_kg'])+float(x['T_B_blanket_birth_kg'])
            sink=sum(float(x[k]) for k in ('T_A_burn_kg','T_B_burn_kg','T_decay_kg','T_process_loss_kg','T_permeation_kg'))
            self.assertAlmostEqual(born-sink,float(x['T_stock_change_kg']),places=7)
    def test_continuous_stocks(self):
        for tbr in self.i['B_gross_TBR_sensitivities']:
            for policy in self.i['policies']:
                rows=sorted([x for x in self.rows if float(x['B_gross_TBR_assumed'])==tbr and x['policy']==policy['id']],key=lambda x:int(x['year']))
                for a,b in zip(rows,rows[1:]):self.assertEqual(a['T_end_kg'],b['T_start_kg'])
    def test_energy_and_no_qualified_revenue(self):
        for x in self.e:
            if x['net_J']!='':self.assertTrue(math.isclose(float(x['generated_J'])-float(x['draw_J']),float(x['net_J']),rel_tol=1e-10,abs_tol=2))
            self.assertEqual(x['profit_USD'],'')
        for x in self.rows:self.assertEqual(float(x['T_external_sales_kg']),0);self.assertEqual(x['actual_revenue_USD'],'')
    def test_recovered_T_no_double_counting_across_horizon(self):
        for tbr in self.i['B_gross_TBR_sensitivities']:
            for policy in self.i['policies']:
                rows=[x for x in self.rows if float(x['B_gross_TBR_assumed'])==tbr and x['policy']==policy['id']]
                recovered=sum(float(x['T_A_direct_recovered_to_store_kg']) for x in rows)
                born=sum(float(x['T_DD_birth_kg']) for x in rows)
                burn=sum(float(x['T_A_burn_kg']) for x in rows)
                self.assertLessEqual(recovered,born-burn+1e-8)
    def test_mass_checks_and_physical_status(self):
        checks=json.loads((r.OUT/'checks.json').read_text())
        self.assertFalse(checks['physical_validation'])
        for x in checks['cases']:
            self.assertLess(abs(x['He3_mass_residual_kg']),1e-8);self.assertLess(abs(x['He4_mass_residual_kg']),1e-8);self.assertLess(x['max_T_mass_residual_kg'],1e-7)
if __name__=='__main__':unittest.main()
