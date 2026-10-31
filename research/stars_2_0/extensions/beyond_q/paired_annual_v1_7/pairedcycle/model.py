"""Conservative dual-reactor inventory research simulator.

Compartments: A plasma T, A/B blanket T, separate A plasma/blanket and B processing, A/B storage.
Every transfer has a donor and recipient. B unburned throughput returns to
processing, not to a new nuclear source. No imports after initial inventory.
Substeps end exactly on schedule-day boundaries. Shutdown stops nuclear
sources, while extraction/processing continue (explicit scenario assumption).
"""
import math
from .physics import (dd_source, dt_events, reaction_ledger, T_KG_PER_ATOM,
                      nonnegative, probability)
from .inventory import advance

def validate(p):
    required = ['schedule_slots','schedule_interval_days','configuration_id','step_days','power_a_dd_mw','power_b_dt_mw','dd_t_branch',
                'a_reaction_day','a_escape_day','tbr_b',
                'extract_a_day','extract_b_day','permeation_day','process_day',
                'process_recovery','b_pass_burn_fraction','half_life_years',
                'initial_a_kg','initial_b_kg','transfer_day','reserve_a_kg',
                'blanket_li6_birth_fraction','case','seed','availability_a',
                'availability_b','common_outage']
    for key in required:
        if key not in p:
            raise ValueError(f'missing parameter {key}')
    for key, value in p.items():
        if isinstance(value,(int,float)):
            nonnegative(**{key:value})
    for key in ['dd_t_branch','process_recovery','b_pass_burn_fraction',
                'blanket_li6_birth_fraction','availability_a','availability_b','common_outage']:
        probability(key,p[key])
    for key in ('a_plasma_recovery','a_blanket_recovery'):
        probability(key,p[key])
    for key in ('a_plasma_process_day','a_blanket_process_day','a_dd_blanket_yield','a_dt_blanket_yield'):
        nonnegative(**{key:p[key]})
    if p['case']=='A0' and (p['a_dd_blanket_yield'] or p['a_dt_blanket_yield']):
        raise ValueError('A0 has no breeding')
    probability('a_source_duty',p['a_source_duty'])
    probability('b_source_duty',p['b_source_duty'])
    probability('a_fast_fraction',p.get('a_fast_fraction',0.))
    if p['step_days'] <= 0 or p['half_life_years'] <= 0 or p['b_pass_burn_fraction'] <= 0:
        raise ValueError('positive timestep, half life and B burn fraction required')
    if p['schedule_slots'] < 1 or int(p['schedule_slots']) != p['schedule_slots']:
        raise ValueError('schedule_slots must be a positive integer')
    if p['schedule_interval_days']<=0:raise ValueError('positive interval required')
    probability('a_fast_escape_fraction',p.get('a_fast_escape_fraction',0.))
    if p.get('a_fast_fraction',0)+p.get('a_fast_escape_fraction',0)>1:raise ValueError('overlapping fast outcomes')
    if p['case'] not in ('A0','A1','A2'):
        raise ValueError('unknown case')
    locks={'historical_20_1130':(20.,1130.),'dual_laser_1100_1100':(1100.,1100.),'arc_1100_1130':(1100.,1130.),'arc_matched_1100_1100':(1100.,1100.)}
    if p['configuration_id'] not in locks:raise ValueError('unknown power-basis identity')
    expected=locks[p['configuration_id']]
    if (p['power_a_dd_mw'],p['power_b_dt_mw'])!=expected:raise ValueError('power-basis lock mismatch')
    if p.get('A_gross_fusion_W')!=p['power_a_dd_mw']*1e6 or p.get('B_gross_fusion_W')!=p['power_b_dt_mw']*1e6:raise ValueError('gross power unit mismatch')

def simulate(p, schedule, component_schedule=None):
    validate(p)
    if len(schedule)!=p['schedule_slots'] or any(len(v)!=2 or any(x not in (0,1) for x in v) for v in schedule):
        raise ValueError('schedule requires one binary A/B pair per day')
    if component_schedule is None:
        component_schedule=[(1,1,1,1)]*p['schedule_slots']
    if len(component_schedule)!=p['schedule_slots'] or any(len(v)!=4 or any(a not in (0,1) for a in v) for v in component_schedule):
        raise ValueError('component schedule requires extraction A/B, processing A/B binary pairs')
    minimum_b=p['initial_b_kg']
    x = dict(a_plasma=0.,a_blanket=0.,b_blanket=0.,a_plasma_process=0.,a_blanket_process=0.,b_process=0.,
             a_store=p['initial_a_kg'],b_store=p['initial_b_kg'])
    initial = sum(x.values())
    c = dict(dd_birth=0.,blanket_a_birth=0.,blanket_b_birth=0.,a_burn=0.,
             b_burn=0.,decay=0.,permeation=0.,process_loss=0.,
             a_to_b=0.,b_to_a=0.,a_extracted=0.,b_extracted=0.,
             b_feed=0.,b_recirculated=0.,a_processed=0.,b_processed=0.,
             a_plasma_processed=0.,a_blanket_processed=0.,
             a_plasma_process_loss=0.,a_blanket_process_loss=0.,
             b_unserved_burn=0.,dd_events=0.,dd_t_atoms=0.)
    decay = math.log(2)/(p['half_life_years']*365.25)
    dd = dd_source(p['power_a_dd_mw'],p['dd_t_branch'])
    rows=[]
    for day,(on_a,on_b) in enumerate(schedule):
        ext_a,ext_b,proc_a,proc_b=component_schedule[day]
        t=0.
        while t < p['schedule_interval_days']-1e-15:
            h=min(p['step_days'],p['schedule_interval_days']-t)
            # Decay storage and processing FIRST; new arrivals process next step.
            for compartment in ('a_store','b_store'):
                x[compartment], exits = advance(x[compartment],0.,{'decay':decay},h)
                c['decay'] += exits['decay']
            for route,compartment,rate,recovery,enabled,store in [
                ('a_plasma','a_plasma_process',p['a_plasma_process_day'],p['a_plasma_recovery'],proc_a,'a_store'),
                ('a_blanket','a_blanket_process',p['a_blanket_process_day'],p['a_blanket_recovery'],proc_a,'a_store'),
                ('b','b_process',p['process_day'],p['process_recovery'],proc_b,'b_store')]:
                x[compartment], exits = advance(x[compartment],0.,
                    {'processed':rate*enabled,'decay':decay},h)
                c['decay']+=exits['decay']
                recovered=exits['processed']*recovery
                loss=exits['processed']-recovered
                c['process_loss']+=loss
                c[route+'_processed']+=recovered
                if route.startswith('a_'):
                    c['a_processed']+=recovered
                    c[route+'_process_loss']+=loss
                x[store]+=recovered
            # Newly created DD T either burns or exits to processing.
            dd_birth=dd['t_atoms_s']*86400*T_KG_PER_ATOM*on_a*p['a_source_duty']
            fast_burn=dd_birth*h*p.get('a_fast_fraction',0.)
            x['a_plasma'], exits = advance(x['a_plasma'],dd_birth*(1-p.get('a_fast_fraction',0.)-p.get('a_fast_escape_fraction',0.)),
                {'burn':p['a_reaction_day']*on_a,'escape':p['a_escape_day'],'decay':decay},h)
            a_burn=exits['burn']+fast_burn
            c['a_burn']+=a_burn
            c['dd_birth']+=dd_birth*h
            c['decay']+=exits['decay']
            x['a_plasma_process']+=exits['escape']+dd_birth*h*p.get('a_fast_escape_fraction',0.)
            events=dd['events_s']*86400*h*on_a*p['a_source_duty']
            dd_n=dd['n_atoms_s']*86400*h*on_a*p['a_source_duty']
            c['dd_events']+=events
            c['dd_t_atoms']+=dd['t_atoms_s']*86400*h*on_a*p['a_source_duty']
            # B feeder competes with A storage reserve policy; transfers are local.
            moved=max(0.,x['a_store']-p['reserve_a_kg'])*(-math.expm1(-p['transfer_day']*h))
            x['a_store']-=moved; x['b_store']+=moved; c['a_to_b']+=moved
            demand=dt_events(p['power_b_dt_mw'])*86400*T_KG_PER_ATOM*h*on_b*p['b_source_duty']
            feed=min(x['b_store'],demand/p['b_pass_burn_fraction'])
            b_burn=feed*p['b_pass_burn_fraction']
            x['b_store']-=feed
            x['b_process']+=feed-b_burn
            c['b_feed']+=feed; c['b_recirculated']+=feed-b_burn
            c['b_burn']+=b_burn; c['b_unserved_burn']+=demand-b_burn
            # Optional reverse transfer is explicit and bounded, not a new source.
            reverse=min(x['b_store'],p.get('reverse_transfer_kg_day',0.)*h)
            x['b_store']-=reverse; x['a_store']+=reverse; c['b_to_a']+=reverse
            # Independent assumed birth yields per DD-source and DT-source neutron.
            births={'a':p['a_dd_blanket_yield']*dd_n*T_KG_PER_ATOM+p['a_dt_blanket_yield']*a_burn,
                    'b':p['tbr_b']*b_burn}
            for r in ('a','b'):
                c['blanket_'+r+'_birth']+=births[r]
                x[r+'_blanket'],exits=advance(x[r+'_blanket'],births[r]/h,
                    {'extract':p['extract_'+r+'_day']*(ext_a if r=='a' else ext_b),'permeation':p['permeation_day'],
                     'decay':decay},h)
                x['a_blanket_process' if r=='a' else 'b_process']+=exits['extract']
                c[r+'_extracted']+=exits['extract']
                c['permeation']+=exits['permeation']; c['decay']+=exits['decay']
            minimum_b=min(minimum_b,x['b_store'])
            t+=h
        born=c['dd_birth']+c['blanket_a_birth']+c['blanket_b_birth']
        sinks=c['a_burn']+c['b_burn']+c['decay']+c['permeation']+c['process_loss']
        residual=initial+born-sinks-sum(x.values())
        if min(x.values()) < -1e-12 or abs(residual)>1e-8*max(1.,initial+born):
            raise ArithmeticError('global inventory conservation failure')
        rows.append(dict(day=(day+1)*p['schedule_interval_days'],time_hours=(day+1)*p['schedule_interval_days']*24,on_a=on_a,on_b=on_b,**x,**c,
                         total_inventory=sum(x.values()),mass_residual_kg=residual))
    energy=reaction_ledger(c['dd_events'],c['dd_t_atoms'],c['a_burn']/T_KG_PER_ATOM,
              c['b_burn']/T_KG_PER_ATOM,c['blanket_a_birth']/T_KG_PER_ATOM,
              c['blanket_b_birth']/T_KG_PER_ATOM,p['blanket_li6_birth_fraction'])
    summary=dict(case=p['case'],status='POTENTIAL-DERIVED',initial_kg=initial,
        final_kg=sum(x.values()),inventory_change_kg=sum(x.values())-initial,
        min_b_store_kg=minimum_b,
        b_unserved_burn_kg=c['b_unserved_burn'],
        maximum_mass_residual_kg=max(abs(r['mass_residual_kg']) for r in rows),
        qualified_usable_surplus_kg=None,self_sufficiency='UNRESOLVED',**energy)
    return rows, summary
