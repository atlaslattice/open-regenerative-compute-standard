import csv,json,math,sys,unittest
import compare as c
from pairedcycle.model import simulate,validate

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=json.loads((c.ROOT/'inputs.json').read_text())
        cls.sources=c.readcsv(c.OUT/'annual_isotopes.csv');cls.energy=c.readcsv(c.OUT/'annual_energy.csv')
    def test_legacy_unit_duty_replay(self):
        sys.path.insert(0,str(c.PARENT/'multiscale_v1_4'))
        from fuelcycle.model import simulate as original
        config=self.inputs['configurations'][2]
        p=c.parameters(config,'inherited_A1',48,24,1/96);s=c.schedules('continuous',48,24)
        old,_=original(p,s);new,_=simulate(p,s)
        self.assertEqual(old,new)
    def test_power_lock_rejects_electricity_as_fusion(self):
        p=c.parameters(self.inputs['configurations'][0],'inherited_A1',0,1,1/96)
        p.update(power_b_dt_mw=400,B_gross_fusion_W=400e6)
        with self.assertRaises(ValueError):validate(p)
    def test_arc_400_net_not_twice_averaged_or_debited(self):
        config=self.inputs['configurations'][0];i=dict(self.inputs,additional_campus_and_isotope_processing_MW=0)
        e=dict(hours=1,on_a=1,on_b=1,B_DT_J=100,B_scheduled_J=100)
        r=c.electrical(e,config,i,dict(A_draw_MW=0))
        self.assertAlmostEqual(r['net_J']/3.6e9,400)
    def test_arc_unfueled_still_pays_own_load(self):
        e=dict(hours=1,on_a=1,on_b=1,B_DT_J=0,B_scheduled_J=100)
        r=c.electrical(e,self.inputs['configurations'][0],self.inputs,dict(A_draw_MW=0))
        self.assertAlmostEqual(r['net_J']/3.6e9,-110)
    def test_unknown_arc_A_draw_stays_unknown(self):
        self.assertIsNone(c.electrical({'hours':1},self.inputs['configurations'][0],self.inputs,dict(A_draw_MW=None)))
        rows=[r for r in self.energy if r['energy_case']=='A_draw_None']
        self.assertTrue(rows);self.assertTrue(all(r['net_J']=='' for r in rows))
    def test_B_reference_replaces_burn_without_startup_creation(self):
        rows=[r for r in self.sources if r['blanket_mode'].startswith('B_replacement_')]
        self.assertTrue(rows)
        for r in rows:
            self.assertAlmostEqual(float(r['year_T_B_blanket_birth_kg']),float(r['year_T_B_burn_kg']),places=8)
            if r['schedule']=='cold_start':self.assertGreater(float(r['T_unserved_B_burn_kg']),0)
    def test_T_phase_mass_closure(self):
        for r in self.sources:
            birth=sum(float(r[k]) for k in ['year_T_DD_birth_kg','year_T_A_blanket_birth_kg','year_T_B_blanket_birth_kg'])
            sink=sum(float(r[k]) for k in ['year_T_A_burn_kg','year_T_B_burn_kg','year_T_decay_kg','year_T_permeation_kg','year_T_processing_loss_kg'])
            self.assertAlmostEqual(birth-sink,float(r['year_T_inventory_change_kg']),places=7)
    def test_helium_DD_DT_sources_and_capture_closure(self):
        for r in self.sources:
            for n in (3,4):
                birth=float(r['He3_direct_birth_kg']) if n==3 else float(r['He4_A_DT_birth_kg'])+float(r['He4_B_DT_birth_kg'])
                remaining=sum(float(r[f'He{n}_{tail}']) for tail in ['mobile_kg','capture_loss_kg','stored_candidate_kg'])
                self.assertAlmostEqual(birth,remaining,places=7)
    def test_fusion_energy_is_partitioned_once(self):
        for r in self.sources:
            self.assertTrue(math.isclose(float(r['fusion_Q_J']),float(r['fusion_neutron_partition_J'])+float(r['fusion_charged_partition_J']),rel_tol=1e-14))
            self.assertEqual(r['qualified_deposited_heat_J'],'')
    def test_zero_helium_source(self):
        self.assertEqual(c.helium_step(0,0,0,0,1,1,.9),(0.,0.,0.))
    def test_no_T_sales_or_profit_or_certification(self):
        for r in self.sources:self.assertEqual(float(r['T_external_sales_kg']),0);self.assertEqual(r['qualified_He4_kg'],'')
        for r in self.energy:self.assertEqual(r['profit_USD'],'');self.assertEqual(r['qualified_export_kWh'],'')
    def test_matched_sources_are_driver_independent(self):
        for mode in self.inputs['blanket_modes']:
            a=next(r for r in self.sources if r['configuration']=='arc_matched_1100_1100' and r['blanket_mode']==mode and r['schedule']=='continuous')
            b=next(r for r in self.sources if r['configuration']=='laser_matched_duty_1100_1100' and r['blanket_mode']==mode and r['schedule']=='continuous')
            for k in ('year_T_DD_birth_kg','year_T_B_burn_kg','He3_direct_birth_kg','He4_B_DT_birth_kg','T_final_total_kg'):self.assertEqual(a[k],b[k])
    def test_outage_and_cold_start_falsification(self):
        for config in self.inputs['configurations']:
            rows=[r for r in self.sources if r['configuration']==config['id'] and r['blanket_mode']=='zero_breeding']
            self.assertLess(float(next(r for r in rows if r['schedule']=='continuous')['T_unserved_B_burn_kg']),1e-8)
            self.assertGreater(float(next(r for r in rows if r['schedule']=='A_90day')['T_unserved_B_burn_kg']),1)
            self.assertGreater(float(next(r for r in rows if r['schedule']=='cold_start')['T_unserved_B_burn_kg']),.01)
    def test_interval_import_export_and_energy_closure(self):
        for r in self.energy:
            if r['net_J']=='':continue
            net=float(r['net_J']);imp=float(r['import_kWh']);pos=float(r['positive_before_export_kWh'])
            self.assertTrue(math.isclose(float(r['generated_J'])-float(r['draw_J']),net,rel_tol=1e-10,abs_tol=2))
            self.assertTrue(math.isclose((pos-imp)*c.KWH,net,rel_tol=1e-10,abs_tol=2))
            self.assertTrue(math.isclose(imp,float(r['startup_import_kWh'])+float(r['year_import_kWh']),rel_tol=1e-12,abs_tol=1e-7))
            for key in ('generated_J','draw_J','net_J'):
                self.assertTrue(math.isclose(float(r[key]),float(r['startup_'+key])+float(r['year_'+key]),rel_tol=1e-11,abs_tol=2))
    def test_explicit_clock_and_duty(self):
        for r in self.sources:
            self.assertEqual(float(r['B_year_clock_hours']),8766)
            self.assertEqual(float(r['total_clock_hours']),8766+float(r['precharge_hours']))
            if r['schedule']=='continuous':self.assertAlmostEqual(float(r['B_scheduled_fusion_FPY_exposure']),float(r['B_source_duty']))
    def test_demand_caps_not_unlimited_revenue(self):
        for r in c.readcsv(c.OUT/'economics_sensitivity.csv'):
            self.assertLessEqual(float(r['full_qualification_sensitivity_sale_STP_L']),float(r['assumed_demand_cap_STP_L']))
            self.assertEqual(r['actual_qualified_revenue_USD'],'');self.assertEqual(r['total_cost_USD'],'')
if __name__=='__main__':unittest.main()
