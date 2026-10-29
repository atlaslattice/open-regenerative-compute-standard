import copy
import json
import math
from pathlib import Path
import unittest
from scipy.integrate import quad
from transport_interval import atom_column_between, transmit, validate, MATERIAL

ROOT=Path(__file__).resolve().parent


def constant(s=1e-15):
    return [dict(E_proton_LAB_MeV=e,epsilon_eV_cm2_atom=s) for e in [.1,1.,3.]]


class TransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.points=json.loads((ROOT/'CURVE.json').read_text())['points']

    def test_constant_analytic(self):
        self.assertAlmostEqual(atom_column_between(constant(),.5,1.5)/1e21,1.)
        r=transmit(constant(),E_in_LAB_MeV=1.,atoms_cm2=2e20,material=MATERIAL)
        self.assertAlmostEqual(r['E_out_LAB_MeV'],.8)

    def test_linear_analytic(self):
        points=[dict(E_proton_LAB_MeV=e,epsilon_eV_cm2_atom=e*1e-15) for e in [.1,1.,3.]]
        self.assertAlmostEqual(atom_column_between(points,.5,2.)/1e21,math.log(4))

    def test_independent_quadrature(self):
        import numpy as np
        e,s=validate(self.points)
        lo,hi=.25,2.5
        numeric=quad(lambda x:1e6/float(np.interp(x,e,s)),lo,hi,
            points=[x for x in e if lo<x<hi],epsabs=1e7,epsrel=1e-11)[0]
        self.assertAlmostEqual(atom_column_between(self.points,lo,hi)/numeric,1.,places=11)

    def test_zero_thickness_and_energy_loss(self):
        r=transmit(self.points,E_in_LAB_MeV=.65,atoms_cm2=0,material=MATERIAL)
        self.assertEqual(r['E_out_LAB_MeV'],.65)
        for n in [1e17,1e18,1e19]:
            r=transmit(self.points,E_in_LAB_MeV=.65,atoms_cm2=n,material=MATERIAL)
            self.assertGreater(r['primary_energy_loss_MeV'],0)
            self.assertAlmostEqual(r['E_in_LAB_MeV'],r['E_out_LAB_MeV']+r['primary_energy_loss_MeV'])

    def test_layers_compose(self):
        def t(e,n):return transmit(self.points,E_in_LAB_MeV=e,atoms_cm2=n,material=MATERIAL)['E_out_LAB_MeV']
        self.assertAlmostEqual(t(t(.65,1e18),2e18),t(.65,3e18),places=13)

    def test_low_energy_boundary_is_not_stopped(self):
        r=transmit(self.points,E_in_LAB_MeV=.65,atoms_cm2=1e24,material=MATERIAL)
        self.assertIsNone(r['E_out_LAB_MeV']);self.assertIsNone(r['stopped'])
        self.assertGreater(r['unmodeled_atoms_cm2'],0)

    def test_material_mismatch(self):
        for material in ['B11','BN','B4C','aluminum']:
            with self.assertRaises(ValueError):transmit(self.points,E_in_LAB_MeV=.65,atoms_cm2=1e18,material=material)

    def test_invalid_grid_and_extrapolation(self):
        for bad in [constant(-1e-15),constant()[:1],list(reversed(constant())),[constant()[0]]*2]:
            with self.assertRaises(ValueError):validate(bad)
        for e in [.01,3.1,float('nan')]:
            with self.assertRaises(ValueError):transmit(self.points,E_in_LAB_MeV=e,atoms_cm2=1e18,material=MATERIAL)

    def test_unit_mutation_caught_by_reference(self):
        mutated=constant(1e-9) # erroneous eV -> MeV factor applied in source
        wrong=atom_column_between(mutated,.5,1.5)
        self.assertAlmostEqual(wrong/1e21,1e-6)
        self.assertFalse(math.isclose(wrong,1e21,rel_tol=1e-4))

    def test_intervals_add_and_stopping_scale(self):
        self.assertAlmostEqual((atom_column_between(self.points,.3,.7)+atom_column_between(self.points,.7,2.))/atom_column_between(self.points,.3,2.),1.)
        changed=copy.deepcopy(self.points)
        for r in changed:r['epsilon_eV_cm2_atom']*=2
        a=transmit(self.points,E_in_LAB_MeV=.65,atoms_cm2=1e18,material=MATERIAL)
        b=transmit(changed,E_in_LAB_MeV=.65,atoms_cm2=1e18,material=MATERIAL)
        self.assertLess(b['E_out_LAB_MeV'],a['E_out_LAB_MeV'])

if __name__=='__main__':unittest.main()
