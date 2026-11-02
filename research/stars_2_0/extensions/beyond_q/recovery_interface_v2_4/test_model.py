import math
import unittest
from model import advance, simulate, required_downstream


def parameters():
    return dict(birth_mol_day=10.,plasma_burn_day=3/7,plasma_exhaust_day=1.,
                exhaust_delivery_fraction=.9,pump_release_day=1.,
                pump_capture_regeneration_fraction=.9,purifier_release_day=4.,purifier_yield=.95)


class ModelTests(unittest.TestCase):
    def test_scalar_solution_and_closure(self):
        x,flow=advance(3.,2.,{'a':1.,'b':3.},.25)
        self.assertAlmostEqual(x,.5+2.5*math.exp(-1))
        self.assertAlmostEqual(x+sum(flow.values()),3.5)
        self.assertAlmostEqual(flow['b']/flow['a'],3.)

    def test_tiny_and_stiff_hazards(self):
        for rate in [0.,1e-16,1.,1e8]:
            x,flow=advance(3.,2.,{'a':rate},.25)
            self.assertGreaterEqual(x,0)
            self.assertAlmostEqual(x+flow['a'],3.5,places=11)

    def test_no_birth_no_products(self):
        p=parameters();p['birth_mol_day']=0.
        r=simulate(p,days=10)
        self.assertEqual(r['candidate_product_STP_L'],0)
        self.assertEqual(r['additional_He4_born_mol'],0)

    def test_ledger_and_consumption(self):
        r=simulate(parameters(),days=10)
        self.assertLess(r['max_abs_residual_mol'],1e-10)
        self.assertEqual(r['DHe3_reactions_mol'],r['additional_He4_born_mol'])
        self.assertEqual(r['additional_deuterium_consumed_mol'],r['DHe3_reactions_mol'])
        self.assertLess(r['stocks_mol']['candidate_storage']+r['cumulative_mol']['secondary_burn'],r['cumulative_mol']['born'])
        self.assertIsNone(r['qualified_product_STP_L'])
        self.assertIsNone(r['energy_J'])

    def test_shutdown_retains_inventory(self):
        p=parameters();p['pump_off']=[(0,10)]
        r=simulate(p,days=10)
        self.assertGreater(r['stocks_mol']['pump'],0)
        self.assertEqual(r['candidate_product_STP_L'],0)
        self.assertLess(r['max_abs_residual_mol'],1e-10)

    def test_zero_exhaust_and_zero_capture(self):
        for key in ['plasma_exhaust_day','pump_capture_regeneration_fraction']:
            p=parameters();p[key]=0.
            r=simulate(p,days=10)
            self.assertEqual(r['candidate_product_STP_L'],0)
            self.assertLess(r['max_abs_residual_mol'],1e-10)

    def test_refinement_and_steady_flow(self):
        results=[simulate(parameters(),dt=dt,days=2) for dt in [.25,.125,.0625]]
        values=[r['candidate_product_STP_L'] for r in results]
        self.assertLess(abs(values[2]-values[1]),abs(values[1]-values[0]))
        last=simulate(parameters(),dt=.0625,days=100)['rows']
        flux=(last[-1]['purified_mol']-last[-2]['purified_mol'])/(last[-1]['day']-last[-2]['day'])
        self.assertAlmostEqual(flux,10*.7*.9*.9*.95,places=7)

    def test_independent_rk4_transient(self):
        # Independent coupled ODE estimator, no calls to advance().
        def rhs(y):
            a,b,c,product=y
            return [10-(1+3/7)*a,.9*a-b,.9*b-4*c,.95*4*c]
        y=[0.]*4;h=1/8192
        for _ in range(8192):
            k1=rhs(y);k2=rhs([v+h*k/2 for v,k in zip(y,k1)])
            k3=rhs([v+h*k/2 for v,k in zip(y,k2)])
            k4=rhs([v+h*k for v,k in zip(y,k3)])
            y=[v+h*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(y,k1,k2,k3,k4)]
        coarse=simulate(parameters(),dt=.125,days=1)['stocks_mol']['candidate_storage']
        fine=simulate(parameters(),dt=.03125,days=1)['stocks_mol']['candidate_storage']
        self.assertLess(abs(fine-y[3]),abs(coarse-y[3])/10)
        self.assertLess(abs(fine/y[3]-1),.001)

    def test_secondary_burn_disabled(self):
        p=parameters();p['plasma_burn_day']=0.
        r=simulate(p,days=10)
        self.assertEqual(r['DHe3_reactions_mol'],0)
        self.assertGreater(r['candidate_product_STP_L'],simulate(parameters(),days=10)['candidate_product_STP_L'])

    def test_invalid_parameter_rejected(self):
        p=parameters();p['purifier_yield']=1.01
        with self.assertRaises(ValueError):simulate(p,days=10)

    def test_overall_target_cannot_exceed_survival(self):
        self.assertTrue(required_downstream(.375,.7)['feasible'])
        self.assertFalse(required_downstream(.75,.7)['feasible'])
        self.assertEqual(required_downstream(.75,.8)['required_fraction'],.9375)
        self.assertFalse(required_downstream(.9,.8)['feasible'])


if __name__=='__main__':unittest.main()
