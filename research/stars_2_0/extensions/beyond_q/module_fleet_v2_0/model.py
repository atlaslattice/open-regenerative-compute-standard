"""Vectorized conservative compartment research model; days, kg, MWh.

Exact constant-source first-order compartment updates; upstream-to-downstream
coupling uses operator splitting. Refinement is required, especially for feed
recirculation. No plasma, transport, purity or plant-performance validation.
"""
import math
import numpy as np

NA=6.02214076e23
EV=1.602176634e-19
MEV=EV*1e6
YEAR=365.25
T_ATOM=.00301604928/NA
HE3_ATOM=.0030160293201/NA
HE4_ATOM=.00400260325413/NA
L_PER_KG=22.414/.0030160293201

def advance(x, source, hazards, dt):
    k=sum(hazards.values())
    if k == 0:
        return x+source*dt, {name:np.zeros_like(x) for name in hazards}
    z=k*dt
    phi=-math.expm1(-z)/k
    psi=dt*dt*(.5-z/6+z*z/24-z*z*z/120) if z<1e-4 else (dt-phi)/k
    integral=x*phi+source*psi
    return x*math.exp(-z)+source*phi, {name:rate*integral for name,rate in hazards.items()}

def validate(p, n):
    if not 1<=n<=50: raise ValueError('fleet must have 1..50 modules')
    for key in ['source_duty','A_macro_availability','B_macro_availability',
                'A_T_fast_burn_fraction','A_T_fast_escape_fraction','A_T_processing_recovery',
                'B_T_processing_recovery','He3_retained_fraction','He4_overall_recovery_assumed']:
        if not 0<=p[key]<=1: raise ValueError(key)
    if p['A_T_fast_burn_fraction']+p['A_T_fast_escape_fraction']>1: raise ValueError('overlapping fast outcomes')
    if not 0<p['B_single_pass_burn_fraction']<=1: raise ValueError('burn fraction')
    if p['step_days']<=0 or p['years']<1 or p['T_half_life_years']<=0: raise ValueError('time')
    if p['A_fusion_MW']!=1100 or p['B_fusion_MW'] not in (1100,1130): raise ValueError('power lock')
    if p['A_blanket_birth_yield']!=0: raise ValueError('A0 only: transport-qualified A breeding not yet connected')
    if p['intermodule_transfers']: raise ValueError('intermodule transfer network not implemented')
    common=p['common_outage_probability_per_day']
    if not 0<=common<1 or any(p[k]>1-common for k in ['A_macro_availability','B_macro_availability']):
        raise ValueError('availability incompatible with common outage probability')
    if p['B_gross_TBR_assumed']<0 or p['initial_T_kg']<0: raise ValueError('negative source/inventory')
    for key in ['commissioning_interval_years','A_T_burn_day','A_T_escape_day','A_T_processing_day',
                'B_T_processing_day','B_T_extract_day','B_T_permeation_day','He3_collection_day',
                'He3_purification_day','T_export_cap_kg_per_module_year','T_market_cap_kg_per_year_fleet',
                'B_storage_reserve_kg','startup_full_power_years_B','replacement_outage_days']:
        if not math.isfinite(p[key]) or p[key]<0:raise ValueError(key)
    if p['replacement_interval_operating_years']<=0:raise ValueError('replacement interval')
    for r in p['He3_overall_recovery_cases']:
        if not 0<=r<=1: raise ValueError('recovery')

def simulate(p, n):
    validate(p,n)
    rng=np.random.default_rng(p['seed']); dt=p['step_days']
    zero=lambda:np.zeros(n)
    names=['a_plasma','a_process','a_store','b_blanket','b_process','b_store']
    x={k:zero() for k in names}; x['b_store'][:]=p['initial_T_kg']
    initial=sum(x.values()).copy(); started=np.zeros(n,dtype=bool)
    start_time=np.full(n,np.nan); commissioned=np.arange(n)*p['commissioning_interval_years']*YEAR
    counters={k:zero() for k in ['dd_birth','a_burn','b_burn','b_birth','decay','permeation','process_loss',
        'exports','a_delivery','a_transfer','b_extract','b_recirculated','b_demand','b_unserved',
        'he3_born','he3_pipeline_exit','he4_born','he4_pipeline_exit','A_on_days','B_on_days',
        'net_MWh','export_MWh','import_MWh','DD_fusion_J','A_DT_fusion_J','B_DT_fusion_J',
        'primary_DD_neutrons','DT_neutrons','assumed_blanket_Q_J','A_replacements','B_replacements']}
    he3_mobile=zero(); he3_purify=zero(); he4_mobile=zero()
    decay=math.log(2)/(p['T_half_life_years']*YEAR)
    dd_events_day=p['A_fusion_MW']*1e6/(3.65*MEV)*86400*p['source_duty']
    t_source_day=dd_events_day*.5*T_ATOM
    he3_source_day=dd_events_day*.5*HE3_ATOM
    b_burn_day=p['B_fusion_MW']*1e6/(17.6*MEV)*86400*T_ATOM*p['source_duty']
    startup_threshold=b_burn_day/p['source_duty']*YEAR*p['startup_full_power_years_B']+p['B_storage_reserve_kg']
    total_steps=int(round(YEAR*p['years']/dt))
    if not math.isclose(total_steps*dt,YEAR*p['years'],abs_tol=1e-9): raise ValueError('step must divide horizon')
    rows=[]; checkpoints=[]; previous={k:zero() for k in counters}; max_residual=0.; max_he_residual=0.
    year_min=np.full(n,np.inf); year_start=sum(x.values()).copy(); last_day=-1
    on_a=on_b=np.zeros(n,dtype=bool); previous_replacement_a=zero();previous_replacement_b=zero()
    for step in range(total_steps):
        time=step*dt; age=np.maximum(0.,time-commissioned); active=time>=commissioned
        if int(time)!=last_day:
            last_day=int(time); common=rng.random()<p['common_outage_probability_per_day']
            available_a=(rng.random(n)<p['A_macro_availability']/(1-p['common_outage_probability_per_day'])) & (not common)
            available_b=(rng.random(n)<p['B_macro_availability']/(1-p['common_outage_probability_per_day'])) & (not common)
        replacement_period=p['replacement_interval_operating_years']*YEAR
        number=np.floor(age/replacement_period)
        replace=active & (age>=replacement_period) & (np.mod(age,replacement_period)<p['replacement_outage_days'])
        # A replacement age is measured from commission; B from actual startup.
        b_age=np.where(started,np.maximum(0.,time-np.nan_to_num(start_time)),0.)
        number_b=np.floor(b_age/replacement_period)
        replace_b=started & (b_age>=replacement_period) & (np.mod(b_age,replacement_period)<p['replacement_outage_days'])
        counters['A_replacements']+=np.maximum(0,number-previous_replacement_a)*active
        counters['B_replacements']+=np.maximum(0,number_b-previous_replacement_b)*started
        previous_replacement_a=number;previous_replacement_b=number_b
        on_a=active & available_a & ~replace
        new_start=active & ~started & (x['b_store']>=startup_threshold)
        started |= new_start;start_time[new_start]=time
        on_b=active & started & available_b & ~replace_b
        for key in ['a_store','b_store']:
            x[key],e=advance(x[key],0.,{'decay':decay},dt);counters['decay']+=e['decay']
        for key,rate,recovery,store in [('a_process',p['A_T_processing_day'],p['A_T_processing_recovery'],'a_store'),
                                      ('b_process',p['B_T_processing_day'],p['B_T_processing_recovery'],'b_store')]:
            x[key],e=advance(x[key],0.,{'processed':rate,'decay':decay},dt)
            counters['decay']+=e['decay'];counters['process_loss']+=e['processed']*(1-recovery)
            x[store]+=e['processed']*recovery
            if key=='a_process': counters['a_delivery']+=e['processed']*recovery
        birth=t_source_day*on_a
        # Burn hazard is zero when A is off; split enabled cohorts separately.
        for enabled in (False,True):
            mask=on_a==enabled
            remaining,e=advance(x['a_plasma'][mask],birth[mask]*(1-p['A_T_fast_burn_fraction']-p['A_T_fast_escape_fraction']),
                {'burn':p['A_T_burn_day']*int(enabled),'escape':p['A_T_escape_day'],'decay':decay},dt)
            x['a_plasma'][mask]=remaining
            counters['a_burn'][mask]+=e['burn']+birth[mask]*dt*p['A_T_fast_burn_fraction']
            counters['decay'][mask]+=e['decay']
            x['a_process'][mask]+=e['escape']+birth[mask]*dt*p['A_T_fast_escape_fraction']
        # Explicit donor-bounded transfer; only mobile storage is available.
        moved=np.maximum(0.,x['a_store']-.25)*(-math.expm1(-2*dt))
        x['a_store']-=moved;x['b_store']+=moved;counters['a_transfer']+=moved
        demand=b_burn_day*dt*on_b
        feed=np.minimum(x['b_store'],demand/p['B_single_pass_burn_fraction'])
        burn=feed*p['B_single_pass_burn_fraction']
        x['b_store']-=feed;x['b_process']+=feed-burn
        counters['b_recirculated']+=feed-burn;counters['b_burn']+=burn
        counters['b_demand']+=demand;counters['b_unserved']+=demand-burn
        bred=p['B_gross_TBR_assumed']*burn
        x['b_blanket'],e=advance(x['b_blanket'],bred/dt,{'extract':p['B_T_extract_day'],'permeation':p['B_T_permeation_day'],'decay':decay},dt)
        x['b_process']+=e['extract'];counters['b_extract']+=e['extract']
        counters['permeation']+=e['permeation'];counters['decay']+=e['decay']
        counters['dd_birth']+=birth*dt;counters['b_birth']+=bred
        # Candidate He3 train: mobile -> captured/cleanup -> product-candidate.
        # The overall fraction is applied AFTER this loss-free transient train.
        he3_purify,e=advance(he3_purify,0.,{'out':p['He3_purification_day']},dt)
        counters['he3_pipeline_exit']+=e['out']
        he3_mobile,e=advance(he3_mobile,he3_source_day*on_a,{'out':p['He3_collection_day']},dt)
        he3_purify+=e['out'];counters['he3_born']+=he3_source_day*on_a*dt
        current_a_burn=counters['a_burn']-previous.get('_step_a_burn',zero())
        previous['_step_a_burn']=counters['a_burn'].copy()
        he4_birth=(current_a_burn+burn)/T_ATOM*HE4_ATOM
        he4_mobile,e=advance(he4_mobile,he4_birth/dt,{'out':1.},dt)
        counters['he4_born']+=he4_birth;counters['he4_pipeline_exit']+=e['out']
        fraction=np.divide(burn,demand,out=zero(),where=demand>0)
        gross=p['B_gross_electric_MW_at_1130_fusion']*p['B_fusion_MW']/1130*fraction
        loads=(np.where(on_a,p['A_net_draw_MW_assumed'],p['A_shutdown_draw_MW'])+
               np.where(on_b,p['B_own_draw_MW'],p['B_shutdown_draw_MW'])+p['shared_processing_draw_MW_assumed'])*active
        net=(gross-loads)*dt*24
        counters['net_MWh']+=net;counters['export_MWh']+=np.maximum(0.,net);counters['import_MWh']+=np.maximum(0.,-net)
        counters['A_on_days']+=on_a*dt;counters['B_on_days']+=on_b*dt
        counters['DD_fusion_J']+=dd_events_day*on_a*dt*3.65*MEV
        counters['A_DT_fusion_J']+=current_a_burn/T_ATOM*17.6*MEV
        counters['B_DT_fusion_J']+=burn/T_ATOM*17.6*MEV
        counters['primary_DD_neutrons']+=dd_events_day*.5*on_a*dt
        counters['DT_neutrons']+=(current_a_burn+burn)/T_ATOM
        counters['assumed_blanket_Q_J']+=bred/T_ATOM*4.783*MEV
        year_min=np.minimum(year_min,x['b_store'])
        residual=initial+counters['dd_birth']+counters['b_birth']-counters['a_burn']-counters['b_burn']-counters['decay']-counters['permeation']-counters['process_loss']-counters['exports']-sum(x.values())
        max_residual=max(max_residual,float(np.max(np.abs(residual))))
        he_res=counters['he3_born']-he3_mobile-he3_purify-counters['he3_pipeline_exit']
        max_he_residual=max(max_he_residual,float(np.max(np.abs(he_res))))
        if min(float(np.min(v)) for v in x.values()) < -1e-10 or np.max(np.abs(residual))>1e-7:
            raise ArithmeticError('T mass/positivity failure')
        end=(step+1)*dt
        if abs(end/YEAR-round(end/YEAR))<1e-9:
            year=int(round(end/YEAR))
            # Actual withdrawal in this CONDITIONAL export scenario; never sell
            # a delivered A atom also used by B. Preserve one FPY buffer.
            eligible=np.where(started,np.maximum(0.,x['b_store']-startup_threshold),0.)
            exports=np.minimum(eligible,p['T_export_cap_kg_per_module_year']*active)
            if exports.sum()>p['T_market_cap_kg_per_year_fleet']:
                exports*=p['T_market_cap_kg_per_year_fleet']/exports.sum()
            x['b_store']-=exports;counters['exports']+=exports
            for m in range(n):
                delta={key:float(value[m]-previous[key][m]) for key,value in counters.items()}
                total=float(sum(x.values())[m])
                rows.append(dict(fleet_modules=n,module=m+1,year=year,operating_age_years=max(0.,(end-commissioned[m])/YEAR),
                    startup_day=None if np.isnan(start_time[m]) else float(start_time[m]),
                    T_start_kg=float(year_start[m]),T_end_kg=total,T_B_storage_end_kg=float(x['b_store'][m]),
                    T_min_B_storage_kg=float(year_min[m]),**delta))
            checkpoints.append(dict(year=year,T_total_kg=float(sum(x.values()).sum()),
                started_modules=int(started.sum()),He3_gross_cumulative_kg=float(counters['he3_born'].sum()),
                net_energy_cumulative_MWh=float(counters['net_MWh'].sum())))
            for key in counters:previous[key]=counters[key].copy()
            year_start=sum(x.values()).copy();year_min=np.full(n,np.inf)
    return rows,checkpoints,dict(max_T_mass_residual_kg=max_residual,max_He3_mass_residual_kg=max_he_residual,
        physical_validation=False,gates='G1-G5 OPEN',startup_B_threshold_kg=startup_threshold,
        annual_source_full_exposure_T_kg=t_source_day*YEAR,
        He3_final_pipeline_kg=float((he3_mobile+he3_purify).sum()),
        He4_mass_residual_kg=float(np.max(np.abs(counters['he4_born']-he4_mobile-counters['he4_pipeline_exit']))),
        final_T_kg=float(sum(x.values()).sum()),unserved_B_T_kg=float(counters['b_unserved'].sum()))
