import csv,json,math,unittest
import year

class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=list(csv.DictReader((year.OUT/'phase_energy.csv').read_text().splitlines()))
        cls.check=json.loads((year.OUT/'checks.json').read_text())
    def test_replay(self):
        self.assertLessEqual(self.check['replay_max_absolute_difference'],1e-9)
        self.assertLessEqual(self.check['B_unserved_burn_kg'],1e-8)
    def test_phase_clock(self):
        for name in {r['energy_case'] for r in self.rows}:
            rows=[r for r in self.rows if r['energy_case']==name]
            self.assertEqual(sum(float(r['hours']) for r in rows),8814.)
            self.assertEqual(float(next(r for r in rows if r['phase']=='B_operating_year')['hours']),8766.)
    def test_startup_B_has_no_energy(self):
        for r in self.rows:
            if r['phase']=='A_only_startup':
                self.assertEqual(float(r['B_actual_DT_J']),0.)
                self.assertEqual(float(r['B_laser_electric_J']),0.)
    def test_energy_and_hourly_import_balance(self):
        for r in self.rows:
            g=float(r['gross_generated_electric_J']);a=float(r['A_laser_electric_J']);b=float(r['B_laser_electric_J']);aux=float(r['auxiliary_electric_J']);n=float(r['net_electric_J'])
            self.assertTrue(math.isclose(g-a-b-aux,n,rel_tol=1e-11,abs_tol=.1))
            i=float(r['imported_electric_kWh']);o=float(r['positive_electric_before_campus_load_kWh'])
            self.assertTrue(math.isclose((o-i)*3.6e6,n,rel_tol=1e-11,abs_tol=.1))
    def test_negative_counter_rejected(self):
        with self.assertRaises(ValueError):
            year.delta_input(dict(time_hours=2,dd_birth=0,a_burn=0,b_burn=0),dict(time_hours=1,dd_birth=1),{})
    def test_daily_sums(self):
        daily=list(csv.DictReader((year.OUT/'daily_reference.csv').read_text().splitlines()))
        refs=[r for r in self.rows if r['energy_case']=='gain10_eta0.2']
        for key in ('net_electric_J','imported_electric_kWh','A_primary_DD_J','A_secondary_DT_J','B_actual_DT_J'):
            self.assertTrue(math.isclose(sum(float(r[key]) for r in refs),sum(float(r[key]) for r in daily),rel_tol=1e-11))
    def test_no_qualification_or_profit(self):
        self.assertFalse(self.check['physical_validation'])
        for r in self.rows:
            self.assertEqual(r['profit_USD'],'');self.assertEqual(r['qualified_export_kWh'],'')
if __name__=='__main__':unittest.main()
