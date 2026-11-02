from pathlib import Path
from collections import deque
import copy,importlib.util,json,unittest
import numpy as np
from controller import Controller
from kernel import simulate
from finance import connected_financials
ROOT=Path(__file__).resolve().parent

class CascadeChecks(unittest.TestCase):
    def setUp(self):
        self.p=json.loads((ROOT/'inputs.json').read_text())

    def ready(self,n=3,policy='eligible_pool',mode='conditional'):
        control=Controller(self.p,n,mode,policy)
        x={'b_store':np.full(n,200.)};x['b_store'][-1]=0
        c={k:np.zeros(n) for k in ['fuel_sent','fuel_received','b_unserved','net_MWh']};c['net_MWh'][:-1]=100
        started=np.ones(n,dtype=bool);started[-1]=False;starts=np.zeros(n)
        control.state=['operating']*(n-1)+['waiting'];control.commissioned[:-1]=0
        control.history=deque([(0.,np.zeros(n),np.zeros(n))])
        return control,x,c,started,starts

    def test_third_campus_can_receive_from_both_predecessors(self):
        a,x,c,s,t=self.ready(policy='all_previous_qualified');a.before_step(500,x,c,s,t)
        self.assertEqual(a.approvals[0]['donors'],[1,2])
        self.assertTrue(all(x['b_store'][:2]>=a.startup))
        event=next(e for e in a.events if e['event']=='construction_authorized')
        self.assertEqual(event['donor_cash_required_USD'],0)
        self.assertEqual(event['capital_source'],'separate recipient external project financing')

    def test_reservation_blocks_duplicate_spending(self):
        a,x,c,s,t=self.ready();x['b_store'][0]=200;x['b_store'][1]=0;s[1]=False
        a.state=['operating','waiting','waiting'];a.commissioned[1:]=np.inf
        a.before_step(500,x,c,s,t);sent=c['fuel_sent'].sum()
        a.before_step(530,x,c,s,t)
        self.assertEqual(len(a.approvals),1);self.assertEqual(c['fuel_sent'].sum(),sent)
        self.assertTrue(np.all(x['b_store']>=0))

    def test_decay_loss_and_receipt_close_and_start_stock_is_sufficient(self):
        a,x,c,s,t=self.ready();a.before_step(500,x,c,s,t)
        lead=a.approvals[0]['ready_day']-500
        a.after_step(500+lead,lead,c);a.before_step(500+lead,x,c,s,t)
        a.after_step(500+lead+.25,.25,c)
        self.assertGreater(a.pool_decay,0);self.assertGreater(a.pool_loss,0)
        self.assertGreaterEqual(x['b_store'][2],a.startup)
        self.assertLess(a.max_pool_residual,1e-9)
        received=c['fuel_received'].copy();a.before_step(500+lead+1,x,c,s,t)
        np.testing.assert_array_equal(received,c['fuel_received'])

    def test_strict_readiness_blocks_unknown_full_costs(self):
        a,x,c,s,t=self.ready(mode='strict');a.before_step(500,x,c,s,t)
        self.assertFalse(a.approvals)
        self.assertEqual(a.events[-1]['reason'],'full_cost_financial_sustainability_UNRESOLVED')

    def test_separate_recipient_financing_is_mandatory(self):
        self.p['cascade']['financed_project_ids']=[1]
        a,x,c,s,t=self.ready();a.before_step(500,x,c,s,t)
        self.assertFalse(a.approvals);self.assertEqual(c['fuel_sent'].sum(),0)
        self.assertEqual(a.events[-1]['reason'],'recipient_financing_not_ready')

    def test_negative_trailing_energy_blocks_donors(self):
        a,x,c,s,t=self.ready();c['net_MWh'][:]=0;a.before_step(500,x,c,s,t)
        self.assertFalse(a.approvals)

    def test_all_predecessor_gate_differs_from_eligible_pool(self):
        a,x,c,s,t=self.ready(policy='all_previous_qualified');s[1]=False
        a.before_step(500,x,c,s,t);self.assertFalse(a.approvals)
        b,y,d,s,t=self.ready(policy='eligible_pool');s[1]=False
        b.before_step(500,y,d,s,t);self.assertTrue(b.approvals)

    def test_no_surplus_does_not_create_a_shipment(self):
        a,x,c,s,t=self.ready();x['b_store'][:2]=a.startup
        a.before_step(500,x,c,s,t);self.assertEqual(c['fuel_sent'].sum(),0)

    def test_parent_physics_regression_when_controller_disabled(self):
        p=copy.deepcopy(self.p);p['years']=1;p['intermodule_transfers']=False
        spec=importlib.util.spec_from_file_location('v20_physics',ROOT.parent/'module_fleet_v2_0/model.py')
        parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
        old,_,oc=parent.simulate(p,1);new,_,nc=simulate(p,1)
        for key in ['dd_birth','b_burn','a_burn','he3_born','net_MWh','T_end_kg']:
            self.assertAlmostEqual(old[0][key],new[0][key],places=8)
        self.assertAlmostEqual(oc['final_T_kg'],nc['final_T_kg'],places=10)

    def test_zero_retention_is_default_and_cash_is_not_doubled(self):
        self.assertEqual(self.p['He3_retained_fraction'],0.)
        p=copy.deepcopy(self.p);p['years']=1;p['intermodule_transfers']=False
        rows,_,_=simulate(p,1);r=connected_financials(rows,p,.375)[0]
        self.assertEqual(r['He3_retained_STP_L'],0.)
        self.assertIsNone(r['actual_profit_USD'])
        self.assertLess(abs(r['T_balance_residual_kg']),1e-8)

if __name__=='__main__':unittest.main()
