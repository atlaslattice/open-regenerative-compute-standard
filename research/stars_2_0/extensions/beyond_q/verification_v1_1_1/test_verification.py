import unittest
import json,math
import hashlib
from pathlib import Path
import numpy as np
from benchmark import reproduce,system,exact_at
from extraction import compare
from run_verification import run_case,threshold

ROOT=Path(__file__).resolve().parent

class Verification(unittest.TestCase):
    def test_upstream_exact_snapshots(self):
        for name,expected in [('fuel_cycle.i','ce9e463a20cb2588a79e0aae44a783456a56fcd2'),
             ('gold.csv','e1b670bbf2bdb161d8c2ebecad54d82212e7ced6'),
             ('tests.txt','c9c09dabde532a09dcda463f14847591419ced60')]:
            b=(ROOT/'upstream'/name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),expected)

    def test_external_fixture(self):
        gold,actual,metrics=reproduce()
        self.assertLess(metrics['max_abs_error_kg'],1e-8)
        self.assertGreater(len(gold),20)

    def test_published_network_conservation(self):
        m,s,lam,loss=system()
        # Every donor's ordinary outflow appears in exactly one destination
        # or split fractions summing to one; only explicit losses/decay leave.
        np.testing.assert_allclose(m.sum(axis=0),-lam-loss,atol=1e-18)
        self.assertAlmostEqual(s.sum(),(1.067-1)*8.99e-7,places=18)

    def test_oracle_initial_and_nonnegative(self):
        x=exact_at([0,1350,1800,17000,18000])
        self.assertAlmostEqual(x[0].sum(),1.14)
        self.assertGreaterEqual(x.min(),0)

    def test_extraction_cycle_conservation(self):
        from fuelcycle.inventory import advance
        eps=.85;S=.2;minutes=10;loss=.001
        r=compare(eps,minutes,S,loss)
        end,exits=advance(r['discrete_post_kg'],S,{'loss':loss},minutes/1440)
        self.assertAlmostEqual(end,r['discrete_pre_kg'])
        self.assertAlmostEqual(end*(1-eps),r['discrete_post_kg'])
        self.assertAlmostEqual(S*minutes/1440,eps*end+exits['loss'])

    def test_zero_loss_recovery_and_mean(self):
        r=compare(1,10,.2,0)
        self.assertEqual(r['discrete_post_kg'],0)
        self.assertAlmostEqual(r['discrete_recovery'],1)
        self.assertAlmostEqual(r['discrete_mean_kg'],r['mixed_stock_kg']/2)

    def test_processor_failure_and_invariant(self):
        p=json.loads((ROOT/'reference.json').read_text());p['days']=70
        _,good=run_case(p,'baseline',10)
        rows,bad=run_case(p,'processor_30d',10)
        self.assertGreater(bad['b_unserved_burn_kg'],good['b_unserved_burn_kg'])
        self.assertLess(bad['maximum_mass_residual_kg'],1e-9)
        self.assertIsNone(bad['qualified_usable_surplus_kg'])
        self.assertGreater(rows[59]['b_process'],rows[29]['b_process'])

    def test_startup_bracket_classifies_endpoints(self):
        p=json.loads((ROOT/'reference.json').read_text());p['days']=70
        b=threshold(p,'processor_7d')
        self.assertGreater(run_case(p,'processor_7d',b['lower_kg'])[1]['b_unserved_burn_kg'],1e-8)
        self.assertLessEqual(run_case(p,'processor_7d',b['upper_kg'])[1]['b_unserved_burn_kg'],1e-8)

if __name__=='__main__':unittest.main()
