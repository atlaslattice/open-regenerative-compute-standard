import json,math,unittest
from pathlib import Path
from model import load_tables,stopping,transport,nuclear_zbl,PROJECTILES,MATERIALS

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.t=load_tables()
    def s(self,**kw):
        args=dict(model='srim13',projectile='proton',material='B11',E_MeV=.65);args.update(kw)
        return stopping(self.t,**args)
    def tport(self,**kw):
        args=dict(model='srim13',projectile='proton',material='B11',E_MeV=.65,total_atoms_cm2=1e18);args.update(kw)
        return transport(self.t,**args)
    def test_native_nodes_roundtrip(self):
        for key,t in self.t.items():
            for i in [0,60,120]:
                z=key[1];particle='proton' if z==1 else 'alpha';m=PROJECTILES[particle][1]
                if key[2]!=5:continue
                value=stopping(self.t,model=key[0],projectile=particle,material='B11',E_MeV=t['energy_keV_u'][i]*m/1000)['electronic_eV_cm2_per_average_atom']
                self.assertAlmostEqual(value/(t['electronic_stopping_in_1e_minus15_eV_cm2_atom'][i]*1e-15),1.,places=12)
    def test_helium_energy_unit(self):
        r=self.s(projectile='alpha',E_MeV=3.)
        t=self.t[('srim13',2,5)]
        from model import log_interpolate
        expected=log_interpolate(t['energy_keV_u'],t['electronic_stopping_in_1e_minus15_eV_cm2_atom'],3000/PROJECTILES['alpha'][1])*1e-15
        self.assertEqual(r['electronic_eV_cm2_per_average_atom'],expected)
        wrong=log_interpolate(t['energy_keV_u'],t['electronic_stopping_in_1e_minus15_eV_cm2_atom'],3000)*1e-15
        self.assertGreater(abs(wrong/expected-1),.1)
    def test_electronic_plus_nuclear(self):
        r=self.s();self.assertEqual(r['total_eV_cm2_per_average_atom'],r['electronic_eV_cm2_per_average_atom']+r['nuclear_eV_cm2_per_average_atom'])
    def test_atomic_isotope_transfer_explicit(self):
        a=self.s();b=self.s(material='OVERLEY_B10_ENRICHED')
        self.assertEqual(a['electronic_eV_cm2_per_average_atom'],b['electronic_eV_cm2_per_average_atom'])
        self.assertNotEqual(a['total_MeV_cm2_g'],b['total_MeV_cm2_g'])
        self.assertIn('isotope',a['electronic_assumption'])
    def test_bn_average_atom_and_boron_inventory(self):
        r=self.s(material='BN_B11_N14',bn_electronic_multiplier=1.)
        b=self.s()['electronic_eV_cm2_per_average_atom']
        from model import log_interpolate
        t=self.t[('srim13',1,7)];n=log_interpolate(t['energy_keV_u'],t['electronic_stopping_in_1e_minus15_eV_cm2_atom'],650/PROJECTILES['proton'][1])*1e-15
        self.assertAlmostEqual(r['electronic_eV_cm2_per_average_atom']/((b+n)/2),1.)
        out=self.tport(material='BN_B11_N14',bn_electronic_multiplier=1.,total_atoms_cm2=2e18)
        self.assertEqual(out['boron_atoms_cm2'],1e18)
    def test_bn_factor_changes_only_electronic(self):
        a=self.s(material='BN_B11_N14',bn_electronic_multiplier=1.)
        b=self.s(material='BN_B11_N14',bn_electronic_multiplier=.8)
        self.assertEqual(a['nuclear_eV_cm2_per_average_atom'],b['nuclear_eV_cm2_per_average_atom'])
        self.assertAlmostEqual(b['electronic_eV_cm2_per_average_atom']/a['electronic_eV_cm2_per_average_atom'],.8)
    def test_missing_mixing_and_domain(self):
        for args in [dict(material='BN_B11_N14'),dict(E_MeV=.0001),dict(E_MeV=2000),dict(model='unknown')]:
            with self.assertRaises(ValueError):self.s(**args)
    def test_zero_column_exact(self):
        r=self.tport(total_atoms_cm2=0);self.assertEqual(r['E_out_MeV'],.65);self.assertEqual(r['primary_loss_MeV'],0)
    def test_refinement_and_layer_composition(self):
        a=self.tport();b=self.tport(refinement=8)
        self.assertLess(abs(a['E_out_MeV']-b['E_out_MeV']),1e-6)
        twice=self.tport(E_MeV=a['E_out_MeV']);whole=self.tport(total_atoms_cm2=2e18)
        self.assertLess(abs(twice['E_out_MeV']-whole['E_out_MeV']),1e-6)
    def test_uncovered_end_is_not_zero(self):
        r=self.tport(total_atoms_cm2=1e25);self.assertIsNone(r['E_out_MeV']);self.assertIsNone(r['stopped'])
    def test_zbl_formula_reference(self):
        z1,m1,z2,m2=2.,4.,5.,11.
        for E in [.001,.1]:
            rm=(m1+m2)*(z1**.23+z2**.23);e=32.536*m2*E*1000/(z1*z2*rm)
            reduced=(.5*math.log(1+1.1383*e)/(e+.01312*e**.21226+.19593*math.sqrt(e))) if e<=30 else .5*math.log(e)/e
            expected=reduced*8.462*z1*z2*m1/rm*1e-15
            self.assertAlmostEqual(nuclear_zbl(E,z1,m1,z2,m2,'ZBL_GEANT4_10_7_4')/expected,1.)
    def test_two_models_not_averaged(self):
        self.assertNotEqual(self.s(model='srim96')['total_eV_cm2_per_average_atom'],self.s()['total_eV_cm2_per_average_atom'])

if __name__=='__main__':unittest.main()
