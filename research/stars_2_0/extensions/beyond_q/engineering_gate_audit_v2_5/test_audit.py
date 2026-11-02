import unittest
from audit import demonstrate,gas_volume_L,mean_DD_MeV
from routing import SPECIES,route,secondary_burn,assay_screen,UnresolvedInput


def coefficients():
    return {s:dict(forward=.8,recycle_bank=.1,permanent_loss=.05) for s in SPECIES}


class Checks(unittest.TestCase):
    def test_species_and_reaction_closure(self):
        rows,r=demonstrate()
        self.assertEqual(len(rows),35)
        self.assertLess(r['max_species_residual_mol'],1e-10)
        self.assertEqual(r['reaction_baryon_residual_mol'],0.)
        self.assertEqual(r['reaction_charge_residual_mol'],0.)
        self.assertIsNone(r['assay']['actual_qualified_product_mol'])

    def test_no_double_spend_consumed_He3(self):
        _,r=demonstrate()
        terminal=sum(d['He3'] for d in r['destinations'].values())
        self.assertAlmostEqual(terminal+r['secondary_He3_consumed_mol'],100.)

    def test_requires_deuterium(self):
        with self.assertRaises(ValueError):secondary_burn({'He3':10.,'D':1.},2.)

    def test_zero_birth_no_output(self):
        r=route({},coefficients())
        self.assertEqual(sum(sum(x.values()) for x in r['streams'].values()),0.)

    def test_capacity_and_shutdown_preserve_unprocessed(self):
        r=route({'He3':100.},coefficients(),capacity_mol_nuclei_day=10.,online_fraction=.5)
        self.assertEqual(r['processed_mol_nuclei'],5.)
        self.assertEqual(r['streams']['forward']['He3'],4.)
        self.assertEqual(r['streams']['retained']['He3'],95.25)
        off=route({'He3':100.},coefficients(),online_fraction=0.)
        self.assertEqual(off['streams']['retained']['He3'],100.)

    def test_unknown_does_not_become_perfect(self):
        with self.assertRaises(UnresolvedInput):route({'He3':1.},None)
        r=route({'He3':1.},coefficients())
        self.assertEqual(r['capacity_status'],'UNRESOLVED')
        self.assertIsNone(r['energy_kWh'])

    def test_reject_overlapping_destinations(self):
        c=coefficients();c['He3']['forward']=1.
        with self.assertRaises(ValueError):route({'He3':10.},c)

    def test_contamination_and_assay(self):
        r=assay_screen({'He3':100.,'He4':1.,'T':.1},min_He3_fraction_of_helium=.999,max_T_atoms_per_He3_atom=1e-6)
        self.assertEqual(r['conditional_screen'],'FAIL')
        self.assertIsNone(r['actual_qualified_product_mol'])
        perfect=assay_screen({'He3':100.},min_He3_fraction_of_helium=.999,max_T_atoms_per_He3_atom=1e-6)
        self.assertEqual(perfect['conditional_screen'],'PASS')
        self.assertIsNone(perfect['actual_qualified_product_mol'])

    def test_T2_factor_two_and_STP(self):
        t=gas_volume_L(10,'T_atom_equivalent');m=gas_volume_L(10,'T2')
        self.assertAlmostEqual(t,2*m)
        self.assertAlmostEqual(t,gas_volume_L(10,'He3'))
        self.assertAlmostEqual(gas_volume_L(1,'He3'),22.413969545014137)
        self.assertGreater(gas_volume_L(1,'He3',P_Pa=100000),gas_volume_L(1,'He3'))
        with self.assertRaises(ValueError):gas_volume_L(1,'T')

    def test_branch_labels_visible_off_midpoint(self):
        self.assertAlmostEqual(mean_DD_MeV(.5),3.65)
        self.assertEqual(mean_DD_MeV(1.),4.03)
        self.assertEqual(mean_DD_MeV(0.),3.27)
        self.assertAlmostEqual(mean_DD_MeV(.48096),3.6355296)
        self.assertNotAlmostEqual(mean_DD_MeV(.48096),.48096*3.27+(1-.48096)*4.03)


if __name__=='__main__':unittest.main()
