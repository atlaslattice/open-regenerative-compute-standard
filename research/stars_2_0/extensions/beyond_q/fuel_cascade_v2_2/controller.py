"""Donor-reserved fuel escrow, independent finance readiness and gated expansion.

All qualification/financing permissions in conditional mode are assumptions.
Escrow is physically removed from donor inventory, decays during construction
and transport, and is credited once on receipt. No donor cash finances CAPEX.
"""
from collections import deque
import math
import numpy as np
from kernel import YEAR,T_ATOM,MEV

class Controller:
    def __init__(self,p,n,readiness='conditional',predecessors='eligible_pool'):
        self.p=p;self.c=p['cascade'];self.n=n
        if readiness not in ('strict','conditional') or predecessors not in ('all_previous_qualified','eligible_pool'):
            raise ValueError('unknown readiness policy')
        for k in ['check_interval_days','sustainability_window_days','construction_days','transport_days','shipment_safety_fraction']:
            if self.c[k]<0:raise ValueError(k)
        if self.c['check_interval_days']<=0 or not 0<=self.c['transport_loss_fraction']<1 or self.c['max_parallel_projects']<1:
            raise ValueError('invalid queue/transport')
        if not 0<p['source_duty']<=1:raise ValueError('source duty')
        self.readiness=readiness;self.predecessors=predecessors
        self.commissioned=np.full(n,np.inf);self.commissioned[0]=0.
        self.state=['operating']+['waiting']*(n-1)
        self.startup=p['B_fusion_MW']*1e6/(17.6*MEV)*86400*T_ATOM*YEAR*p['startup_full_power_years_B']+p['B_storage_reserve_kg']
        self.decay=math.log(2)/(p['T_half_life_years']*YEAR)
        self.events=[];self.shipments=[];self.history=deque();self.last_day=-1
        self.next_check=0.;self.last_block=None;self.pool_decay=0.;self.pool_loss=0.;self.max_pool_residual=0.
        self.sending_floor_violations=0;self.approvals=[]

    def emit(self,time,event,**kw):
        self.events.append(dict(day=float(time),event=event,readiness=self.readiness,predecessor_policy=self.predecessors,**kw))

    def block(self,time,module,reason):
        key=(module,reason)
        if key!=self.last_block:self.emit(time,'waiting',module=module+1,reason=reason)
        self.last_block=key

    def eligible(self,time,counters,started,start_time):
        c=self.c
        if not self.history:return np.zeros(self.n,dtype=bool)
        ref=self.history[0]
        window=time-ref[0]
        enough=window+1e-9>=c['sustainability_window_days']
        mature=started & ((time-np.nan_to_num(start_time))>=c['sustainability_window_days'])
        positive=(counters['net_MWh']-ref[1])>0
        served=(counters['b_unserved']-ref[2])<1e-10
        return mature & positive & served & enough

    def before_step(self,time,x,counters,started,start_time):
        # Complete queued deliveries first. The reserved material has already
        # decayed in escrow; routing loss is charged once here.
        for project in self.approvals:
            if project['delivered'] or time+1e-9<project['ready_day']:continue
            target=project['recipient']
            parts=[s for s in self.shipments if s['recipient']==target and not s['delivered']]
            for s in parts:
                loss=s['mass']*self.c['transport_loss_fraction'];self.pool_loss+=loss
                receipt=s['mass']-loss
                x['b_store'][target]+=receipt;counters['fuel_received'][target]+=receipt
                self.emit(time,'receipt',shipment=s['id'],donor=s['donor']+1,module=target+1,received_kg=float(receipt),loss_kg=float(loss))
                s['mass']=0.;s['delivered']=True
            if x['b_store'][target]+1e-8<self.startup:raise ArithmeticError('recipient startup commitment underdelivered')
            self.commissioned[target]=time;self.state[target]='operating';project['delivered']=True
            self.emit(time,'commissioned',module=target+1,received_storage_kg=float(x['b_store'][target]),
                      finance_source='separate recipient external project financing',donor_cash_used_USD=0.)
        if time+1e-9<self.next_check:return
        self.next_check=time+self.c['check_interval_days']
        candidates=[i for i in range(1,self.n) if self.state[i]=='waiting']
        if not candidates:return
        target=candidates[0]
        if sum(self.state[i]=='building' for i in range(self.n))>=self.c['max_parallel_projects']:
            self.block(time,target,'construction_capacity');return
        ready=float(self.c['finance_ready_day_by_module'].get(str(target+1),0.))
        if target+1 not in self.c['financed_project_ids'] or time<ready:
            self.block(time,target,'recipient_financing_not_ready');return
        if self.readiness=='strict':
            if not self.c['complete_cost_readiness_verified']:
                self.block(time,target,'full_cost_financial_sustainability_UNRESOLVED');return
            if not self.c['financial_assumptions_physically_validated']:
                self.block(time,target,'physical_operating_and_fuel_qualification_UNRESOLVED');return
        elif not (self.c['donor_financial_sustainability_assumed'] and self.c['fuel_qualification_assumed']):
            self.block(time,target,'conditional_qualification_permission_absent');return
        eligible=self.eligible(time,counters,started,start_time)
        eligible[target:]=False
        if self.predecessors=='all_previous_qualified' and not eligible[:target].all():
            self.block(time,target,'all_predecessors_must_qualify');return
        if not eligible.any():self.block(time,target,'no_sustainable_mature_donors');return
        available=np.where(eligible,np.maximum(0.,x['b_store']-self.startup),0.)
        lead=self.c['construction_days']+self.c['transport_days']
        required=self.startup*math.exp(self.decay*lead)/(1-self.c['transport_loss_fraction'])*(1+self.c['shipment_safety_fraction'])
        if available.sum()+1e-9<required:self.block(time,target,'insufficient_uncommitted_donor_stock');return
        reserved=available/available.sum()*required
        donors=[]
        for donor,mass in enumerate(reserved):
            if mass<=0:continue
            x['b_store'][donor]-=mass;counters['fuel_sent'][donor]+=mass
            if x['b_store'][donor]<self.startup-1e-9:self.sending_floor_violations+=1
            shipment=dict(id=len(self.shipments)+1,donor=donor,recipient=target,mass=float(mass),loaded_kg=float(mass),delivered=False)
            self.shipments.append(shipment);donors.append(donor+1)
            self.emit(time,'fuel_reserved',shipment=shipment['id'],donor=donor+1,module=target+1,reserved_kg=float(mass),
                donor_floor_kg=self.startup,donor_remaining_kg=float(x['b_store'][donor]),
                illustrative_external_sale_value_foregone_USD=float(mass)*1000*self.p['T_price_USD_per_gram'],
                actual_transfer_receipts_USD=None)
        self.state[target]='building';self.last_block=None
        self.approvals.append(dict(recipient=target,approved_day=time,ready_day=time+lead,delivered=False,donors=donors))
        self.emit(time,'construction_authorized',module=target+1,eligible_donors=donors,loaded_fuel_kg=required,
            ready_day=time+lead,capital_source='separate recipient external project financing',
            hardware_subtotal_commitment_USD=self.p['historical_two_chassis_USD']+self.p['adaptation_USD'],
            complete_installed_CAPEX_USD=None,donor_cash_required_USD=0.)

    def after_step(self,time,dt,counters):
        self.last_counters=counters
        factor=-math.expm1(-self.decay*dt)
        for s in self.shipments:
            if not s['delivered']:
                lost=s['mass']*factor;s['mass']-=lost;self.pool_decay+=lost
        pool=sum(s['mass'] for s in self.shipments)
        residual=float(counters['fuel_sent'].sum()-counters['fuel_received'].sum())-pool-self.pool_decay-self.pool_loss
        self.max_pool_residual=max(self.max_pool_residual,abs(residual))
        if abs(residual)>1e-7:raise ArithmeticError('reserved/transit fuel conservation failure')
        if int(time)!=self.last_day:
            self.last_day=int(time)
            self.history.append((time,counters['net_MWh'].copy(),counters['b_unserved'].copy()))
            target=time-self.c['sustainability_window_days']
            while len(self.history)>1 and self.history[1][0]<=target:self.history.popleft()

    def summary(self,counters):
        return dict(commissioned_modules=int(np.isfinite(self.commissioned).sum()),
            building_modules=self.state.count('building'),waiting_modules=self.state.count('waiting'),
            fuel_reserved_sent_kg=float(counters['fuel_sent'].sum()),fuel_received_kg=float(counters['fuel_received'].sum()),
            reserved_and_transit_inventory_kg=sum(s['mass'] for s in self.shipments),
            escrow_transport_decay_kg=self.pool_decay,transport_loss_kg=self.pool_loss,
            max_pool_mass_residual_kg=self.max_pool_residual,donor_reserve_floor_violations=self.sending_floor_violations,
            physical_validation=False,full_cost_profit=None)
