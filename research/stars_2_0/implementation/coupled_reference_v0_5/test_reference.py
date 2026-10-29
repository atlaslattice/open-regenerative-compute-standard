import copy,json,math
from pathlib import Path
import unittest
import numpy as np
from kinematics import MP,MB,MA,Q,event,verify,boost,two_body_p
from physics import Coordinate,reactions,sigma
from run import execute,check_dependencies

ROOT=Path(__file__).resolve().parent

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config=json.loads((ROOT/'examples/reference.json').read_text())
        cls.config['sampled_events_per_nonzero_shot']=64
        cls.result,cls.records=execute(cls.config)

    def test_bare_nuclear_mass_and_Q(self):
        s=json.loads((ROOT/'MASS_SOURCE.json').read_text())
        self.assertAlmostEqual(MB-(s['B11_atomic_mass_u']*s['atomic_mass_unit_MeV']-5*s['electron_MeV']),sum(s['B_electron_binding_components_eV'])*1e-6,places=10)
        self.assertTrue(8.67<Q<8.70)

    def test_event_conservation_and_physical_mass(self):
        rng=np.random.default_rng(99)
        for E in [.22,.65,3.8]:
            for _ in range(100):
                a,p=event(E,rng);verify(a,p)
                self.assertLess(abs(float((a[:,0]-MA).sum())-(E+Q)),1e-8)
                self.assertTrue(np.all(a[:,0]-MA<=E+Q+1e-8))

    def test_bad_alpha_rejected(self):
        a,p=event(.65,np.random.default_rng(1));a[0,0]+=.001
        with self.assertRaises(ValueError):verify(a,p)
        with self.assertRaises(ValueError):verify(a[:2],p)
        a,p=event(.65,np.random.default_rng(1));p[0]=np.nan
        with self.assertRaises(ValueError):verify(a,p)

    def test_boost_inverse(self):
        v=np.array([math.hypot(MA,3),1.,2.,2.]);b=np.array([.1,-.2,.05])
        np.testing.assert_allclose(boost(boost(v,b),-b),v,rtol=1e-13,atol=1e-10)

    def test_phase_space_against_independent_invariant_mass_integral(self):
        E=.65;W=math.sqrt((MP+MB)**2+2*MB*E);s=np.linspace((2*MA)**2,(W-MA)**2,20001)
        # Density in s12 from recursive dPhi3, independently expressed through the Kallen polynomial.
        lam1=(W*W-s-MA*MA)**2-4*s*MA*MA;lam2=s*s-4*s*MA*MA
        weight=np.sqrt(np.maximum(0,lam1)*np.maximum(0,lam2))/s
        mean=float(np.trapezoid(np.sqrt(s)*weight,s)/np.trapezoid(weight,s))
        rng=np.random.default_rng(814);sample=[]
        for _ in range(2000):
            a,_=event(E,rng);v=a[0]+a[1];sample.append(math.sqrt(v[0]**2-float(v[1:]@v[1:])))
        error=float(np.std(sample,ddof=1)/math.sqrt(len(sample)))
        self.assertLess(abs(float(np.mean(sample))-mean),6*error)

    def test_relative_coordinate_is_not_absolute_range(self):
        c=Coordinate(lambda E:1e-15,.1,2.,128)
        self.assertAlmostEqual(c.outgoing(1.,2e20),.8)
        self.assertIsNone(c.outgoing(.2,2e20))
        self.assertEqual(c.outgoing(.2,0),.2)

    def test_variable_sigma_constant_limit(self):
        rows=[dict(E_lab_MeV=str(e),sigma_event_b=2.,observable='PUBLICATION_MODEL_EXTRAPOLATED_FUSION_EVENT_CROSS_SECTION') for e in [.22,3.8]]
        c=Coordinate(lambda E:1e-15,.1,2.,128)
        r=reactions(c,rows,1.,1e18,.5,64)
        self.assertAlmostEqual(r['probability']/(-math.expm1(-1e-6)),1.,places=12)
        with self.assertRaises(ValueError):sigma(rows,.162)

    def test_all_shots_and_zero_source(self):
        self.assertEqual(self.result['all_attempt_count'],3)
        s=self.result['attempts'][1]
        self.assertEqual(s['incident_protons'],0);self.assertEqual(s['expected_fusion_events'],0)
        self.assertEqual(s['detector']['signal_expected_counts'],[0.]*4)
        self.assertEqual(s['sampled_conditional_events'],0)

    def test_counts_closure_and_bounds(self):
        for s in self.result['attempts']:
            self.assertEqual(s['expected_alpha_births'],3*s['expected_fusion_events'])
            self.assertLessEqual(s['detector']['true_expected_counts'],s['expected_alpha_births']+1e-15)
            self.assertLess(abs(s['detector']['count_closure_residual']),1e-15)
            lo,hi=s['expected_alpha_exit_kinetic_bounds_MeV'];self.assertGreaterEqual(lo,0);self.assertLessEqual(lo,hi)
            a,b=s['expected_primary_particle_loss_bounds_MeV'];self.assertGreaterEqual(a,-1e-8);self.assertLessEqual(a,b)
            budget=s['expected_beam_kinetic_input_MeV']+s['expected_nuclear_Q_MeV']
            self.assertAlmostEqual(a+hi+s['expected_unreacted_proton_exit_kinetic_MeV'],budget)
            self.assertEqual(s['detector']['background_expected_counts'],[0.]*4)

    def test_event_grouped_covariance(self):
        s=self.result['attempts'][0];events=[r for r in self.records if r['attempt_id']==s['attempt_id']]
        edges=np.array(self.config['response']['true_edges_mev']);ys=[]
        for r in events:
            y=np.zeros(4)
            for a in r['alphas']:
                e=a['exit_energy_MeV']
                if a['geometry_accepts'] and e is not None and e>=edges[0]:y[np.searchsorted(edges,e,side='right')-1]+=.6
            ys.append(y)
        expected=np.cov(np.array(ys),rowvar=False,ddof=1)*s['expected_fusion_events']**2/len(events)
        np.testing.assert_allclose(expected,s['conditional_monte_carlo_detector_covariance'],rtol=1e-13,atol=1e-20)

    def test_repeatability(self):
        r,e=execute(self.config);self.assertEqual(r,self.result);self.assertEqual(e,self.records)

    def test_frame_and_null_model_guards(self):
        for key,value in [('proton_energy_frame','CM'),('source_model','CALIBRATED'),('run_class','VALIDATED')]:
            c=copy.deepcopy(self.config);c[key]=value
            with self.assertRaises(ValueError):execute(c)

    def test_missing_threshold_coverage(self):
        c=copy.deepcopy(self.config);c['response']['true_edges_mev'][0]=0.
        with self.assertRaises(ValueError):execute(c)

    def test_zero_target(self):
        c=copy.deepcopy(self.config);c['total_atoms_cm2']=0
        r,events=execute(c);self.assertEqual(r['expected_fusion_events_all_attempts'],0);self.assertFalse(events)

    def test_target_isotope_guard(self):
        c=copy.deepcopy(self.config);c['material']='OVERLEY_B10_ENRICHED'
        with self.assertRaises(ValueError):execute(c)

    def test_bn_inventory_and_no_heat_credit(self):
        c=copy.deepcopy(self.config);c.update(material='BN_B11_N14',bn_electronic_multiplier=1.,total_atoms_cm2=2e18)
        r,_=execute(c,False);self.assertGreater(r['expected_fusion_events_all_attempts'],0)
        self.assertTrue(r['net_energy'].startswith('UNAVAILABLE'));self.assertTrue(r['heat_recovery'].startswith('UNAVAILABLE'))

if __name__=='__main__':unittest.main()
