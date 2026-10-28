import hashlib
import math
import unittest
from dataclasses import replace
import numpy as np
from transport import RangeTable,Layer,DomainError,through_path,transmit_proton,escape_alpha,normal_areal_mass
from detector import Response


def synthetic_table(material='TEST_A',species='proton',S=2.):
    # Constant synthetic mass stopping power S MeV cm2/g => R(E)=E/S.
    # This is dimensionally consistent artificial test data, not boron or BN.
    raw=('energy_MeV,csda_range_g_cm2\n'+''.join(f'{e},{e/S}\n' for e in (0.,1.,2.,4.,8.))).encode()
    return RangeTable.from_csv(raw,dataset_id=f'SYNTHETIC:{material}:{species}',material_id=material,
        species=species,sha256=hashlib.sha256(raw).hexdigest(),evidence_state='SYNTHETIC')


def response(matrix=((1.,0.),(0.,1.))):
    return Response('SYNTHETIC:response','alpha',(0.,1.,2.),(0.,1.,2.),matrix,'SYNTHETIC')


class TransportTests(unittest.TestCase):
    def test_constant_stopping_independent_oracle(self):
        tab=synthetic_table(); tables={('TEST_A','proton'):tab}
        # Compare against direct E-S*tau/mu; no range inversion in oracle.
        for E in (.2,1.,3.7,8.):
            for tau in (0.,.1,.8,5.):
                for mu in (.2,.5,1.):
                    with self.subTest(E=E,tau=tau,mu=mu):
                        r=transmit_proton(E,mu,[Layer('L','TEST_A',tau)],tables)
                        self.assertAlmostEqual(r['output_energy_MeV'],max(0,E-2*tau/mu),places=13)
                        self.assertAlmostEqual(r['closure_residual_MeV'],0,places=13)

    def test_vacuum_and_stopped_input(self):
        self.assertEqual(transmit_proton(2,1,[],{})['output_energy_MeV'],2)
        self.assertEqual(transmit_proton(0,1,[],{})['output_energy_MeV'],0)
        self.assertEqual(transmit_proton(2,1,[Layer('vac','vacuum',0)],{})['output_energy_MeV'],2)

    def test_material_specific_stack_and_loss(self):
        tables={(m,'proton'):synthetic_table(m,S=S) for m,S in [('TEST_A',2),('TEST_B',3)]}
        r=transmit_proton(4,.5,[Layer('A','TEST_A',.2),Layer('B','TEST_B',.3)],tables)
        self.assertAlmostEqual(r['output_energy_MeV'],1.4)
        self.assertAlmostEqual(r['primary_energy_loss_MeV'],2.6)
        self.assertAlmostEqual(r['layer_ledger'][0]['primary_energy_loss_MeV'],.8)
        self.assertAlmostEqual(r['layer_ledger'][1]['primary_energy_loss_MeV'],1.8)

    def test_split_layer_invariance(self):
        tab=synthetic_table(); tables={('TEST_A','proton'):tab}
        one=transmit_proton(4,.6,[Layer('all','TEST_A',.5)],tables)
        split=transmit_proton(4,.6,[Layer('a','TEST_A',.2),Layer('b','TEST_A',.3)],tables)
        self.assertAlmostEqual(one['output_energy_MeV'],split['output_energy_MeV'],places=13)

    def test_missing_or_mismatched_species_material_blocked(self):
        layers=[Layer('A','BN_UNQUALIFIED',.1)]
        with self.assertRaises(ValueError): transmit_proton(1,1,layers,{})
        with self.assertRaises(ValueError):
            transmit_proton(1,1,layers,{('BN_UNQUALIFIED','proton'):synthetic_table()})
        with self.assertRaises(ValueError):
            transmit_proton(1,1,[Layer('A','TEST_A',.1)],{('TEST_A','alpha'):synthetic_table(species='alpha')})

    def test_no_extrapolation_or_invented_low_energy_tail(self):
        t=replace(synthetic_table(),energies_mev=(1.,2.,4.),csda_ranges_g_cm2=(.5,1.,2.))
        for E in (.9,4.1):
            with self.assertRaises(DomainError):t.residual(E,.1)
        with self.assertRaises(DomainError):t.residual(1.1,.1)
        self.assertEqual(t.residual(1.1,1.),0) # Path exceeds supplied total CSDA range.

    def test_bad_tables_and_projected_range_header_rejected(self):
        for changes in ({'energies_mev':(0,2,1,4,8)}, {'csda_ranges_g_cm2':(0,1,1,2,4)},
                        {'energies_mev':(0,float('nan'),2,4,8)}, {'energies_mev':(0,-1,2,4,8)},
                        {'csda_ranges_g_cm2':(.1,.5,1,2,4)}):
            with self.subTest(changes=changes),self.assertRaises(ValueError):replace(synthetic_table(),**changes)
        raw=b'energy_MeV,projected_range_g_cm2\n1,1\n2,2\n'
        with self.assertRaises(ValueError):RangeTable.from_csv(raw,dataset_id='test',material_id='A',species='proton',sha256=hashlib.sha256(raw).hexdigest(),evidence_state='SYNTHETIC')

    def test_hash_mutation_rejected(self):
        raw=b'energy_MeV,csda_range_g_cm2\n1,1\n2,2\n'
        with self.assertRaises(ValueError):RangeTable.from_csv(raw,dataset_id='test',material_id='A',species='proton',sha256='0'*64,evidence_state='SYNTHETIC')

    def test_calibrated_mode_refuses_synthetic(self):
        with self.assertRaises(ValueError):transmit_proton(1,1,[Layer('A','TEST_A',.1)],{('TEST_A','proton'):synthetic_table()},calibrated=True)

    def test_invalid_geometry_and_floating_overflow_refused(self):
        for mu in (0,-1,1.1,float('nan')):
            with self.subTest(mu=mu),self.assertRaises(ValueError):transmit_proton(1,mu,[],{})
        with self.assertRaises(ValueError):normal_areal_mass(1,float('inf'))
        with self.assertRaises(ValueError):normal_areal_mass(1e308,1e308)
        with self.assertRaises(ValueError):Layer('A','A',-.1)
        with self.assertRaises(ValueError):transmit_proton(1,1e-320,[Layer('A','TEST_A',1)],{('TEST_A','proton'):synthetic_table()})

    def test_explicit_thickness_units(self):
        self.assertAlmostEqual(normal_areal_mass(5,2),.001)
        self.assertEqual(Layer('A','TEST_A','.1').areal_mass_g_cm2,.1)

    def test_birth_faces_and_substrate_orientation(self):
        tables={(m,'alpha'):synthetic_table(m,'alpha',S=S) for m,S in [('FILM',2),('BACKING',6)]}
        layers=[Layer('film','FILM',.2),Layer('back','BACKING',.5)]
        up=escape_alpha(3,-1,0,.25,layers,tables)
        down=escape_alpha(3,1,0,.25,layers,tables)
        self.assertAlmostEqual(up['output_energy_MeV'],2.9)
        self.assertEqual(up['exit_face'],'beam_upstream')
        self.assertEqual(down['output_energy_MeV'],0)
        self.assertIsNone(down['exit_face'])
        flipped=escape_alpha(3,1,1,.75,list(reversed(layers)),tables)
        self.assertAlmostEqual(flipped['output_energy_MeV'],up['output_energy_MeV'])

    def test_invalid_birth_location(self):
        for index,depth in ((2,.5),(0,-.1),(0,1.1),(True,.5)):
            with self.assertRaises(ValueError):escape_alpha(1,1,index,depth,[Layer('A','TEST_A',.1)],{})

    def test_uniform_isotropic_slab_against_analytic_oracle(self):
        # Fixed alpha range R=E/S. Uniform depth and isotropic mu; paired midpoint
        # quadrature integrates both exit hemispheres. Independent analytic Pescape:
        # 1-L/(2R) for L<=R; R/(2L) otherwise. No RNG, detector or fitted curve.
        tab=synthetic_table(species='alpha',S=1.); tables={('TEST_A','alpha'):tab}
        n=120
        for L,R in ((.5,2.),(2.,2.),(4.,2.)):
            escaped=0
            for j in range(n):
                for k in range(n):
                    out=escape_alpha(R,(k+.5)/n,0,(j+.5)/n,[Layer('slab','TEST_A',L)],tables)
                    escaped+=out['output_energy_MeV']>0
            probability=escaped/(n*n) # Symmetry makes the upstream average equal.
            oracle=1-L/(2*R) if L<=R else R/(2*L)
            self.assertLess(abs(probability-oracle),2/n) # Boundary-cell quadrature bound.

    def test_scalar_angle_material_mutations_detected(self):
        t=synthetic_table(); e=transmit_proton(3,.5,[Layer('A','TEST_A',.2)],{('TEST_A','proton'):t})['output_energy_MeV']
        self.assertAlmostEqual(e,2.2)
        self.assertGreater(abs(e-(3-2*.2)),.3) # Deliberately omit the oblique path factor.
        wrong=transmit_proton(3,.5,[Layer('A','TEST_A',.2)],{('TEST_A','proton'):synthetic_table(S=4)})['output_energy_MeV']
        self.assertGreater(abs(e-wrong),.7)


class DetectorTests(unittest.TestCase):
    def test_identity_response(self):
        r=response().fold('alpha',[10,20])
        self.assertEqual(r['signal_expected_counts'],[10,20])
        self.assertEqual(r['undetected_expected_counts'],0)

    def test_migration_efficiency_and_background_oracle(self):
        r=response(((.7,.1),(.2,.6))).fold('alpha',[100,50],[3,4])
        np.testing.assert_allclose(r['signal_expected_counts'],[75,50])
        np.testing.assert_allclose(r['total_expected_counts'],[78,54])
        self.assertAlmostEqual(r['undetected_expected_counts'],25)
        self.assertAlmostEqual(r['count_closure_residual'],0)

    def test_non_detection_not_renormalized(self):
        r=response(((.2,0.),(0.,.3))).fold('alpha',[100,100])
        self.assertEqual(r['signal_expected_counts'],[20,30])
        self.assertAlmostEqual(r['undetected_expected_counts'],150)
        self.assertGreater(abs(sum(r['signal_expected_counts'])-200),100)

    def test_zero_source_preserves_measured_background(self):
        r=response().fold('alpha',[0,0],[2,3])
        self.assertEqual(r['signal_expected_counts'],[0,0])
        self.assertEqual(r['total_expected_counts'],[2,3])

    def test_overflow_is_refused(self):
        with self.assertRaises(ValueError):response().fold('alpha',[1e308,1e308])
        with self.assertRaises(ValueError):response().fold('alpha',[1e308,0],[1e308,0])

    def test_probability_and_species_guards(self):
        for R in (((1.1,0.),(0.,1.)),((-.1,0.),(0.,1.)),((float('nan'),0.),(0.,1.))):
            with self.assertRaises(ValueError):response(R).fold('alpha',[1,1])
        with self.assertRaises(ValueError):response().fold('proton',[1,1])
        with self.assertRaises(ValueError):response().fold('alpha',[1,1],calibrated=True)
        with self.assertRaises(ValueError):response().fold('alpha',[-1,1])


if __name__=='__main__':unittest.main(verbosity=2)
