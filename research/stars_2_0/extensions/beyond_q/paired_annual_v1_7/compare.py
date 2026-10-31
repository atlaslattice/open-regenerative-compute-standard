"""Paired conditional annual energy/isotope accounting. Standard library only."""
from pathlib import Path
import csv,json,math,hashlib
from pairedcycle.model import simulate
from pairedcycle.physics import dd_source,dt_events,T_KG_PER_ATOM,FPY_S,AVOGADRO,MEV_J
from pairedcycle.inventory import advance
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'outputs';PARENT=ROOT.parent
HE3=.0030160293201/AVOGADRO;HE4=.00400260325413/AVOGADRO;KWH=3.6e6

def readcsv(p):return list(csv.DictReader(p.read_text().splitlines()))
def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)

def parameters(c,mode,pre,hours,step):
    base_case='A0' if mode=='B_replacement_A0' else ('A2' if mode=='B_replacement_A2' else 'A1')
    raw=json.loads((PARENT/'multiscale_v1_4/inputs/scenarios.json').read_text())
    p=dict(next(x['parameters'] for x in raw if x['configuration_id']=='dual_laser_1100_1100' and x['case']==base_case and x['condition']=='continuous'))
    p.update(configuration_id=c.get('engine_id',c['id']),power_a_dd_mw=c['A_primary_DD_MW'],power_b_dt_mw=c['B_DT_MW'],
       A_gross_fusion_W=c['A_primary_DD_MW']*1e6,B_gross_fusion_W=c['B_DT_MW']*1e6,
       a_source_duty=c['a_source_duty'],b_source_duty=c['b_source_duty'],initial_a_kg=0.,initial_b_kg=0.,
       schedule_interval_days=1/24,step_days=step,schedule_slots=pre+hours)
    if mode.startswith('B_replacement_'):p['tbr_b']=1.0
    if mode=='zero_breeding':p.update(case='A0',a_dd_blanket_yield=0.,a_dt_blanket_yield=0.,tbr_b=0.)
    return p

def schedules(kind,pre,hours):
    pairs=[(1,0)]*pre
    for h in range(hours):
        a=b=1
        if kind=='independent_14day':a=int(not 10*24<=h<24*24);b=int(not 60*24<=h<74*24)
        elif kind=='correlated_14day':a=b=int(not 10*24<=h<24*24)
        elif kind=='A_90day':a=int(not 24<=h<91*24)
        elif kind=='B_90day':b=int(not 24<=h<91*24)
        elif kind not in ('continuous','cold_start'):raise ValueError('unknown schedule')
        pairs.append((a,b))
    return pairs

def step_energy(row,prior,c,p):
    d=lambda k:row[k]-prior.get(k,0.)
    h=row['time_hours']-prior.get('time_hours',0.)
    if min(d(k) for k in ('dd_birth','a_burn','b_burn')) < -1e-12:raise ValueError('counter reversal')
    dd=d('dd_birth')/T_KG_PER_ATOM*2*3.65*MEV_J
    scheduled_a=c['A_primary_DD_MW']*1e6*c['a_source_duty']*row['on_a']*h*3600
    if not math.isclose(dd,scheduled_a,rel_tol=1e-9,abs_tol=1):raise ValueError('primary source power mismatch')
    b_scheduled=c['B_DT_MW']*1e6*c['b_source_duty']*row['on_b']*h*3600
    return dict(hours=h,DD_J=dd,A_DT_J=d('a_burn')/T_KG_PER_ATOM*17.6*MEV_J,B_DT_J=d('b_burn')/T_KG_PER_ATOM*17.6*MEV_J,
                B_scheduled_J=b_scheduled,on_a=row['on_a'],on_b=row['on_b'])

def electrical(e,c,assumptions,energy_case):
    h=e['hours'];duration=h*3600
    extra=assumptions['additional_campus_and_isotope_processing_MW']*1e6*duration
    if c['architecture']=='ARC':
        draw=energy_case['A_draw_MW']
        if draw is None:return None
        fraction=e['B_DT_J']/e['B_scheduled_J'] if e['B_scheduled_J'] else 0.
        if fraction>1+1e-9:raise ValueError('B fusion exceeds scheduled source')
        # Published gross and own loads are already pulse averaged. Do NOT apply duty twice.
        gross=assumptions['ARC_B_gross_electric_reference_MW']*c['B_DT_MW']/assumptions['ARC_B_reference_flattop_MW']*fraction*1e6*duration
        b_load=(assumptions['ARC_B_own_electric_MW']*e['on_b']+assumptions['ARC_B_shutdown_draw_MW']*(1-e['on_b']))*1e6*duration
        a_load=(draw*e['on_a']+assumptions['ARC_A_shutdown_draw_MW']*(1-e['on_a']))*1e6*duration
        loads=a_load+b_load+extra
    else:
        gain=energy_case['gain'];eta=energy_case['eta']
        if gain<=0 or not 0<eta<=1:raise ValueError('invalid laser gain/efficiency')
        gross=(e['DD_J']+e['A_DT_J']+e['B_DT_J'])*assumptions['laser_capture_fraction']*assumptions['laser_conversion_efficiency']
        a_load=e['DD_J']/gain/eta;b_load=e['B_scheduled_J']/gain/eta
        loads=a_load+b_load+assumptions['laser_combined_auxiliary_MW']*1e6*duration+extra
    net=gross-loads
    return dict(generated_J=gross,draw_J=loads,A_input_or_net_draw_J=a_load,B_input_or_own_draw_J=b_load,
      net_J=net,import_kWh=max(0.,-net)/KWH,positive_before_export_kWh=max(0.,net)/KWH)

def helium_step(mobile,stored,loss,birth,h,rate,capture):
    mobile,exits=advance(mobile,birth/(h/24),{'capture':rate},h/24)
    return mobile,stored+exits['capture']*capture,loss+exits['capture']*(1-capture)

def evaluate(c,mode,kind,inputs):
    pre=0 if kind=='cold_start' else inputs['precharge_hours']
    p=parameters(c,mode,pre,inputs['calendar_hours'],inputs['timestep_days'])
    rows,s=simulate(p,schedules(kind,pre,inputs['calendar_hours']))
    eid=lambda x:dict(energy_case=x,totals={k:0. for k in ('generated_J','draw_J','A_input_or_net_draw_J','B_input_or_own_draw_J','net_J','import_kWh','positive_before_export_kWh')},startup_import_kWh=0.,year_import_kWh=0.,startup_generated_J=0.,startup_draw_J=0.,startup_net_J=0.,year_generated_J=0.,year_draw_J=0.,year_net_J=0.)
    energy_cases=[dict(**eid('A_draw_'+str(x)),A_draw_MW=x) for x in inputs['ARC_A_net_draw_MW_sensitivities']] if c['architecture']=='ARC' else [dict(**eid(f'gain{g}_eta{eta}'),gain=g,eta=eta) for g in inputs['laser_gains'] for eta in inputs['laser_wallplug_efficiencies']]
    prior={};he={3:(0.,0.,0.),4:(0.,0.,0.)};births={3:0.,4:0.};daily=[];on_a=on_b=0;decay_he3=0.;phase={};phase_he3_born=phase_he3_stored=phase_he4_stored=0.
    for i,r in enumerate(rows):
        d=lambda k:r[k]-prior.get(k,0.)
        e=step_energy(r,prior,c,p);h=e['hours']
        on_a+=r['on_a']*h;on_b+=r['on_b']*h
        b3=(d('dd_events')-d('dd_t_atoms'))*HE3
        b4=(d('a_burn')+d('b_burn'))/T_KG_PER_ATOM*HE4
        decay_he3+=d('decay')/T_KG_PER_ATOM*HE3
        for n,b,capture in [(3,b3,inputs['helium3_capture_fraction']),(4,b4,inputs['helium4_capture_fraction'])]:
            he[n]=helium_step(*he[n],b,h,inputs['helium_collection_day'],capture);births[n]+=b
            if abs(births[n]-sum(he[n]))>1e-8:raise ArithmeticError('He isotope mass closure')
        for q in energy_cases:
            x=electrical(e,c,inputs,q)
            if x is None:continue
            for k,v in x.items():q['totals'][k]+=v
            q['startup_import_kWh' if i<pre else 'year_import_kWh']+=x['import_kWh']
            for key in ('generated_J','draw_J','net_J'):q[('startup_' if i<pre else 'year_')+key]+=x[key]
        if i+1==pre:
            phase=dict(r);phase_he3_born=births[3];phase_he3_stored=he[3][1];phase_he4_stored=he[4][1]
        if kind=='continuous' and ((i+1)%24==0 or i==len(rows)-1):
            daily.append(dict(configuration=c['id'],blanket_mode=mode,time_hours=r['time_hours'],T_total_kg=r['total_inventory'],T_B_storage_kg=r['b_store'],He3_stored_candidate_kg=he[3][1],He4_stored_candidate_kg=he[4][1]))
        prior=r
    end=rows[-1];dyear=lambda k:end[k]-phase.get(k,0.)
    row=dict(configuration=c['id'],architecture=c['architecture'],blanket_mode=mode,schedule=kind,
       B_gross_TBR_assumed=p['tbr_b'],A_primary_DD_flattop_MW=c['A_primary_DD_MW'],B_DT_flattop_MW=c['B_DT_MW'],A_source_duty=c['a_source_duty'],B_source_duty=c['b_source_duty'],
       precharge_hours=pre,B_year_clock_hours=inputs['calendar_hours'],total_clock_hours=end['time_hours'],
       A_fusion_FPY_exposure=on_a*c['a_source_duty']/8766,B_scheduled_fusion_FPY_exposure=on_b*c['b_source_duty']/8766,
       year_T_DD_birth_kg=dyear('dd_birth'),year_T_A_blanket_birth_kg=dyear('blanket_a_birth'),year_T_B_blanket_birth_kg=dyear('blanket_b_birth'),
       year_T_A_burn_kg=dyear('a_burn'),year_T_B_burn_kg=dyear('b_burn'),year_T_decay_kg=dyear('decay'),year_T_permeation_kg=dyear('permeation'),year_T_processing_loss_kg=dyear('process_loss'),
       year_T_inventory_change_kg=end['total_inventory']-phase.get('total_inventory',0.),
       T_A_to_B_transfer_kg=end['a_to_b'],T_unserved_B_burn_kg=s['b_unserved_burn_kg'],T_final_total_kg=end['total_inventory'],T_final_A_storage_kg=end['a_store'],T_final_B_storage_kg=end['b_store'],
       T_external_sales_kg=0.,fusion_Q_J=s['fusion_j'],fusion_neutron_partition_J=s['fusion_neutron_j'],fusion_charged_partition_J=s['fusion_charged_j'],blanket_assumed_reaction_Q_J=s['assumed_blanket_reaction_q_j'],qualified_deposited_heat_J=None,max_T_mass_residual_kg=s['maximum_mass_residual_kg'],year_He3_direct_birth_kg=births[3]-phase_he3_born,year_He3_recovered_to_storage_candidate_kg=he[3][1]-phase_he3_stored,year_He4_A_DT_birth_kg=dyear('a_burn')/T_KG_PER_ATOM*HE4,year_He4_B_DT_birth_kg=dyear('b_burn')/T_KG_PER_ATOM*HE4,year_He4_recovered_to_storage_candidate_kg=he[4][1]-phase_he4_stored,He3_direct_birth_kg=births[3],He3_decay_birth_unavailable_kg=decay_he3,
       He4_blanket_Li_path_birth_unavailable_kg=(end['blanket_a_birth']+end['blanket_b_birth'])/T_KG_PER_ATOM*HE4,He4_A_DT_birth_kg=end['a_burn']/T_KG_PER_ATOM*HE4,He4_B_DT_birth_kg=end['b_burn']/T_KG_PER_ATOM*HE4,
       He3_mobile_kg=he[3][0],He3_capture_loss_kg=he[3][2],He3_stored_candidate_kg=he[3][1],
       He4_mobile_kg=he[4][0],He4_capture_loss_kg=he[4][2],He4_stored_candidate_kg=he[4][1],
       He3_sale_candidate_kg=he[3][1]*(1-inputs['He3_retained_fraction'])*inputs['helium_quality_acceptance'],
       He4_internal_candidate_kg=min(he[4][1]*inputs['helium_quality_acceptance'],inputs['assumed_He4_internal_allocation_kg']),
       qualified_He3_kg=None,qualified_He4_kg=None,qualified_T_surplus_kg=None,cooling_energy_saved_kWh=None,operational_self_sufficient='UNRESOLVED')
    erows=[]
    for q in energy_cases:
        known=not(c['architecture']=='ARC' and q['A_draw_MW'] is None)
        erows.append(dict(configuration=c['id'],blanket_mode=mode,schedule=kind,energy_case=q['energy_case'],hours=end['time_hours'],
           **(q['totals'] if known else {k:None for k in q['totals']}),startup_import_kWh=q['startup_import_kWh'] if known else None,year_import_kWh=q['year_import_kWh'] if known else None,
           **{k:q[k] if known else None for k in ('startup_generated_J','startup_draw_J','startup_net_J','year_generated_J','year_draw_J','year_net_J')},year_mean_net_MW=q['year_net_J']/inputs['calendar_hours']/3.6e9 if known else None,mean_net_MW=q['totals']['net_J']/end['time_hours']/3.6e9 if known else None,qualified_export_kWh=None,profit_USD=None,
           evidence='POTENTIAL-DERIVED assumed complete-boundary screen' if known else 'UNRESOLVED A retrofit net draw'))
    return row,erows,daily

def main():
    from provenance import verify
    OUT.mkdir(exist_ok=True)
    (OUT/'source_sha256.json').write_text(json.dumps(verify(),indent=2)+'\n')
    inputs=json.loads((ROOT/'inputs.json').read_text());sources=[];energy=[];daily=[];economics=[]
    for c in inputs['configurations']:
        for mode in inputs['blanket_modes']:
            for kind in inputs['schedules']:
                r,ee,dd=evaluate(c,mode,kind,inputs);sources.append(r);energy+=ee;daily+=dd
                for e in ee:
                    if e['import_kWh'] is None:continue
                    he_l=r['He3_sale_candidate_kg']/.0030160293201*22.414
                    for price in inputs['He3_assumed_price_USD_per_STP_L']:
                        for cap in inputs['He3_assumed_demand_STP_L']:
                            sales=min(he_l,cap);rev=sales*price;charge=e['import_kWh']*inputs['import_price_USD_per_kWh']
                            economics.append(dict(configuration=c['id'],blanket_mode=mode,schedule=kind,energy_case=e['energy_case'],
                             He3_candidate_STP_L=he_l,assumed_He3_price_USD_per_STP_L=price,assumed_demand_cap_STP_L=cap,
                             full_qualification_sensitivity_sale_STP_L=sales,conditional_He3_revenue_USD=rev,import_electricity_charge_USD=charge,
                             electricity_only_margin_USD=rev-charge,actual_qualified_revenue_USD=None,total_cost_USD=None,profit_USD=None,
                             status='ASSUMED full-qualification/price/demand sensitivity; no actual sales or complete economics'))
                print(c['id'],mode,kind,'unserved T kg',r['T_unserved_B_burn_kg'],flush=True)
    write('annual_isotopes.csv',sources);write('annual_energy.csv',energy);write('economics_sensitivity.csv',economics);write('daily_reference.csv',daily)
    (OUT/'checks.json').write_text(json.dumps(dict(source_cases=len(sources),energy_cases=len(energy),economic_sensitivities=len(economics),
       physical_validation=False,gates={f'G{i}':'OPEN' for i in range(1,6)},actual_profit_USD=None,
       core_change='Inherited v1.4 engine copied; add architecture-neutral source-power locks and explicit A/B source-duty factors; no changes to recovery kinetics',
       He4_scope='A/B DT plasma He4 recovery candidate; blanket He4 birth assumes all modeled blanket T from Li6/Li7 pathways and is unavailable; D-He3 consumption omitted',
       calendar='365.25 days after 7 day A-only precharge, except cold-start control',source_commit=inputs['source_commit']),indent=2)+'\n')
if __name__=='__main__':main()
