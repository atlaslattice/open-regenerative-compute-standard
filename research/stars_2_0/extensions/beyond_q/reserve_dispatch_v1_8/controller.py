"""Heuristic dispatch with explicit reserve and production targets, not optimal control."""
from dispatchcycle.inventory import advance
from dispatchcycle.physics import AVOGADRO
HE3=.0030160293201/AVOGADRO

class Controller:
    def __init__(self,inputs,policy):
        self.i=inputs;self.policy=policy;self.mobile=0.;self.stored=0.;self.previous_birth=0.;self.year=-1;self.year_start_stored=0.
        self.reserve_call=True;self.state=1;self.last_switch=0;self.switches=0
    def __call__(self,hour,stock,counters,allowed):
        total_birth=(counters['dd_events']-counters['dd_t_atoms'])*HE3
        if hour:
            birth=total_birth-self.previous_birth
            self.mobile,exits=advance(self.mobile,birth*24,{'collection':self.i['He3_collection_day']},1/24)
            self.stored+=exits['collection']*self.i['He3_capture']
        self.previous_birth=total_birth
        if hour<self.i['precharge_hours']:
            return (allowed[0],allowed[1])
        year=(hour-self.i['precharge_hours'])//self.i['hours_per_model_year']
        if year!=self.year:self.year=year;self.year_start_stored=self.stored
        if stock['b_store']<=self.i['reserve_low_B_storage_kg']:self.reserve_call=True
        if stock['b_store']>=self.i['reserve_high_B_storage_kg']:self.reserve_call=False
        candidate=(self.stored-self.year_start_stored)*(1-self.i['He3_retained_fraction'])*self.i['He3_quality_acceptance']/.0030160293201*22.414
        production_call=candidate<self.policy['He3_external_candidate_target_STP_L_per_year']
        desired=int(self.policy['always_on'] or self.reserve_call or production_call)
        since=hour-self.last_switch
        if desired!=self.state:
            minimum=self.i['minimum_A_on_hours'] if self.state else self.i['minimum_A_off_hours']
            emergency=desired and stock['b_store']<=self.i['reserve_low_B_storage_kg']
            if since<minimum and not emergency:desired=self.state
        actual=min(desired,allowed[0])
        if actual!=self.state:self.switches+=1;self.last_switch=hour;self.state=actual
        return (actual,allowed[1])
