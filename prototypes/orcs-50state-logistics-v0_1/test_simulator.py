import json
import unittest
from pathlib import Path
from simulator import STATES, check_network, optimize, reserve_gate

BASE = json.loads(Path(__file__).with_name('network.json').read_text())


def route(fr='TX', to='NY', price=2, days=2, capacity=200, **kw):
    e = {'from': fr, 'to': to, 'grade': 'D', 'cost_usd_per_bbl': price,
         'time_days': days, 'capacity_bbl': capacity, 'permitted': True, 'safe': True}
    e.update(kw)
    return e


class Tests(unittest.TestCase):
    def test_50_states(self):
        self.assertEqual(50, len(STATES))
        self.assertTrue(check_network(BASE))

    def test_no_invented_edges(self):
        self.assertEqual('UNVERIFIED_OR_INFEASIBLE',optimize(BASE,'TX','NY','D',100)['status'])

    def test_route(self):
        out=optimize({**BASE,'edges':[route()]},'TX','NY','D',100)
        self.assertEqual(['TX','NY'],out['path'])
        self.assertEqual(200,out['cost_usd'])

    def test_unknown_capacity(self):
        d={**BASE,'edges':[route(capacity_bbl=None)]}
        self.assertEqual(1,optimize(d,'TX','NY','D',100)['unknown_edges_excluded'])

    def test_grade_veto(self):
        d={**BASE,'edges':[route()]}
        self.assertEqual('UNVERIFIED_OR_INFEASIBLE',optimize(d,'TX','NY','jet',100)['status'])

    def test_permission_veto(self):
        d={**BASE,'edges':[route(permitted=False)]}
        self.assertEqual('UNVERIFIED_OR_INFEASIBLE',optimize(d,'TX','NY','D',100)['status'])

    def test_capacity_veto(self):
        d={**BASE,'edges':[route(capacity=5)]}
        self.assertEqual('UNVERIFIED_OR_INFEASIBLE',optimize(d,'TX','NY','D',100)['status'])

    def test_shock(self):
        d={**BASE,'edges':[route()]}
        self.assertEqual('UNVERIFIED_OR_INFEASIBLE',optimize(d,'TX','NY','D',100,disabled_edges=[0])['status'])

    def test_cost_and_time(self):
        d={**BASE,'edges':[route(price=3,days=1),
            route(fr='TX',to='LA',price=1,days=2),route(fr='LA',to='NY',price=1,days=2)]}
        self.assertEqual(['TX','LA','NY'],optimize(d,'TX','NY','D',100)['path'])
        self.assertEqual(['TX','NY'],optimize(d,'TX','NY','D',100,max_days=2)['path'])

    def test_reserve(self):
        x=reserve_gate(365,0,500)
        self.assertEqual(90,x['target_stock_bbl'])
        self.assertEqual(45,x['export_candidate_bbl'])
        self.assertFalse(x['export_authorized'])

    def test_reserve_shortage(self):
        x=reserve_gate(365,10,300)
        self.assertEqual(55,x['unmet_demand_bbl'])
        self.assertEqual(0,x['export_candidate_bbl'])

    def test_invalid_capacity(self):
        d={**BASE,'edges':[route(capacity=-1)]}
        with self.assertRaises(ValueError):
            check_network(d)


if __name__=='__main__':
    unittest.main()
