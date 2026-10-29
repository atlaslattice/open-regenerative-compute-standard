import itertools,json,math,unittest
import numpy as np
from amplitude import ROOT,components,intensity,check_config,k,MA,channel
from coulomb import waves,cg,BACKEND
from extract_munch import parse

def config():return json.loads((ROOT/'CANDIDATE_CONFIG.json').read_text())
def event():
    lab,initial=k.event(.675,np.random.default_rng(17))
    return np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab])

class CoherentTests(unittest.TestCase):
    def test_six_permutations_amplitude_symmetry(self):
        a=event();ref,_=components(a,config())
        for order in itertools.permutations(range(3)):
            actual,_=components(a[list(order)],config());np.testing.assert_allclose(actual,ref,rtol=1e-10,atol=1e-13)

    def test_rotation_invariance_unpolarized(self):
        a=event();A,_=components(a,config());R,_=np.linalg.qr(np.random.default_rng(98).normal(size=(3,3)));R[:,0]*=np.linalg.det(R)
        b=a.copy();b[:,1:]=a[:,1:]@R.T;B,_=components(b,config())
        for mix,delta in [(.76,.67*2*math.pi),(.85,0),(1,0),(0,0)]:
            self.assertAlmostEqual(intensity(A,mix_coefficient=mix,relative_phase_radians=delta,coherent=True),intensity(B,mix_coefficient=mix,relative_phase_radians=delta,coherent=True),places=12)

    def test_equilateral_symmetry_zero(self):
        W=math.sqrt((k.MP+k.MB)**2+2*k.MB*.675);T=(W-3*MA)/3;p=math.sqrt(T*(T+2*MA))
        a=np.array([[MA+T,p*math.cos(j*2*math.pi/3),p*math.sin(j*2*math.pi/3),0] for j in range(3)])
        A,parts=components(a,config());self.assertLess(float(np.vdot(A,A).real/np.vdot(parts,parts).real),1e-20)

    def test_coherence_and_symmetry_ablation_are_detectable(self):
        A,parts=components(event(),config())
        coh=intensity(A,mix_coefficient=.76,relative_phase_radians=.67*2*math.pi,coherent=True)
        inc=intensity(A,mix_coefficient=.76,relative_phase_radians=0.,coherent=False)
        self.assertGreater(abs(coh-inc),1e-5*max(coh,inc))
        self.assertGreater(abs(np.vdot(A,A).real-np.vdot(parts,parts).real),1e-5*np.vdot(parts,parts).real)

    def test_phase_periodicity_and_pure_limits(self):
        A,_=components(event(),config())
        for mix in [0.,.76,1.]:
            f=lambda d:intensity(A,mix_coefficient=mix,relative_phase_radians=d,coherent=True)
            self.assertAlmostEqual(f(.2),f(.2+2*math.pi),places=14)
            if mix in [0.,1.]:self.assertAlmostEqual(f(.2),intensity(A,mix_coefficient=mix,relative_phase_radians=0,coherent=False),places=14)

    def test_cg_orthonormal_and_known_sign(self):
        self.assertAlmostEqual(cg(1,0,0,0,1,0),1.)
        for l in [1,3]:
            for M in range(-2,3):self.assertAlmostEqual(sum(cg(2,m,l,M-m,2,M)**2 for m in range(-2,3)),1.)

    def test_coulomb_analytic_zero_charge(self):
        for rho in [.5,1.,2.,5.]:
            c=waves(0,0.,rho);self.assertAlmostEqual(c['F'],math.sin(rho),places=9);self.assertAlmostEqual(c['G'],math.cos(rho),places=9)
            self.assertAlmostEqual(c['P'],rho,places=9);self.assertAlmostEqual(c['S'],0.,places=9)

    def test_precise_independent_coulomb_reference(self):
        receipt=json.loads((ROOT/'receipts/high_precision_run001/COMPARISON.json').read_text())
        for r in receipt['rows']:
            c=waves(r['l'],r['eta'],r['rho']);self.assertLess(abs(c['P']/r['mpmath']['P']-1),1e-7);self.assertLess(abs(c['S']-r['mpmath']['S']),1e-7)
        self.assertIn('MICHEL_CPC',BACKEND)

    def test_invalid_points_and_calibrated_claim_rejected(self):
        for args in [(-1,1.,1.),(2,math.nan,1.),(2,1.,0.)]:
            with self.assertRaises(ValueError):waves(*args)
        c=config();c['run_class']='CALIBRATED'
        with self.assertRaises(ValueError):check_config(c)
        a=event();a[0,0]+=.001
        with self.assertRaises(ValueError):components(a,config())

    def test_energy_reference_and_boundary_are_explicit(self):
        c=config();self.assertAlmostEqual(c['pair_level_above_threshold_MeV']-3.037,.09184,places=12)
        B=channel(c['pair_level_above_threshold_MeV'],MA/2,4,2,c['secondary_radius_fm'],c['coulomb_phase_convention'])['S']
        self.assertTrue(math.isfinite(B))
        for key in ['boundary_convention','basis_convention','coulomb_phase_convention']:
            d=dict(c);d.pop(key)
            with self.assertRaises(ValueError):check_config(d)

    def test_recovered_alpha0_values_and_ambiguous_energies(self):
        d=json.loads((ROOT/'MUNCH_PREPRINT_V1_TABLE1.json').read_text());rows=d['rows']
        self.assertEqual(len(rows),45);self.assertEqual(sum(r['source_energy_duplicated'] for r in rows),4)
        self.assertEqual([r['alpha0_angle_integrated_mb'] for r in rows if r['E_proton_LAB_keV']==1900],[7.9,9.1])
        text='\n'.join(str(r['E_proton_LAB_keV'])+' '+r['source_token'] for r in rows)
        self.assertEqual(parse(text),d)

    def test_preprint_errors_are_preserved_and_ambiguous_fit_excluded(self):
        rows=json.loads((ROOT/'MUNCH_PREPRINT_V1_TABLE1.json').read_text())['rows']
        self.assertAlmostEqual(rows[0]['reported_error_mb'],.3)
        self.assertAlmostEqual(next(r for r in rows if r['source_token']=='12.0(12)')['reported_error_mb'],1.2)
        for r in rows:
            if r['E_proton_LAB_keV'] in [950,1900]:self.assertFalse(r['eligible_for_future_fit'])

if __name__=='__main__':unittest.main()
