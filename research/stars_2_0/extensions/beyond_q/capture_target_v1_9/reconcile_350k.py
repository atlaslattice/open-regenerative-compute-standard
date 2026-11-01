"""Explain the existing capture result without changing source/recovery inputs.
This is a route-accounting replay using the same compartment operator, not an
independent plasma-physics validation or evidence that the original estimate failed.
"""
import json,math
import run as r
from dispatchcycle.inventory import advance
from dispatchcycle.physics import dd_source,T_KG_PER_ATOM,AVOGADRO
from target_controller import Controller

M_T=.00301604928;M_HE3=.0030160293201;V=22.414

def main():
    i=json.loads((r.ROOT/'inputs.json').read_text())
    parent=json.loads((r.PARENT/'paired_annual_v1_7/inputs.json').read_text())
    c=next(x for x in parent['configurations'] if x['id']=='arc_matched_1100_1100')
    p=r.paired.parameters(c,'B_replacement_A0',i['precharge_hours'],i['years']*i['hours_per_model_year'],i['fuel_step_days']);p['tbr_b']=1.
    policy=next(x for x in i['policies'] if x['id']=='captured350k_atom_equivalent')
    rows,_=r.simulate(p,r.permitted(i),schedule_policy=Controller(i,policy))
    decay=math.log(2)/(p['half_life_years']*365.25)
    dd=dd_source(p['power_a_dd_mw'],p['dd_t_branch'])
    plasma=process=route_decay=0.;route_recovered=route_loss=0.
    he_mobile=he_store=he_loss=0.;prior={};snapshots=[];max_replay=0.
    boundaries={i['precharge_hours']}|{i['precharge_hours']+k*i['hours_per_model_year'] for k in range(1,i['years']+1)}
    for row in rows:
        elapsed=0.
        while elapsed<1/24-1e-15:
            h=min(i['fuel_step_days'],1/24-elapsed)
            process,exits=advance(process,0.,{'processed':p['a_plasma_process_day'],'decay':decay},h)
            route_recovered+=exits['processed']*p['a_plasma_recovery'];route_loss+=exits['processed']*(1-p['a_plasma_recovery']);route_decay+=exits['decay']
            birth_rate=dd['t_atoms_s']*86400*T_KG_PER_ATOM*row['on_a']*p['a_source_duty']
            plasma,exits=advance(plasma,birth_rate*(1-p['a_fast_fraction']-p['a_fast_escape_fraction']),{'burn':p['a_reaction_day']*row['on_a'],'escape':p['a_escape_day'],'decay':decay},h)
            route_decay+=exits['decay'];process+=exits['escape']+birth_rate*h*p['a_fast_escape_fraction'];elapsed+=h
        max_replay=max(max_replay,abs(plasma-row['a_plasma']),abs(process-row['a_plasma_process']),abs(route_recovered-row['a_plasma_processed']),abs(route_loss-row['a_plasma_process_loss']))
        delta=lambda k:row[k]-prior.get(k,0.)
        he_birth=(delta('dd_events')-delta('dd_t_atoms'))*r.HE3
        he_mobile,he_store,he_loss=r.paired.helium_step(he_mobile,he_store,he_loss,he_birth,1, i['He3_collection_day'],i['He3_capture'])
        if round(row['time_hours']) in boundaries:
            snapshots.append(dict(hour=row['time_hours'],dd_birth=row['dd_birth'],a_burn=row['a_burn'],route_recovered=route_recovered,route_loss=route_loss,route_decay=route_decay,
               T_pipeline=plasma+process,He3_pipeline=he_mobile,He3_store=he_store,He3_loss=he_loss,dd_events=row['dd_events'],dd_t_atoms=row['dd_t_atoms']))
        prior=row
    if max_replay>1e-8:raise ArithmeticError('route reconstruction disagrees with archived engine')
    results=[]
    for year,(start,end) in enumerate(zip(snapshots,snapshots[1:]),1):
        d=lambda k:end[k]-start[k]
        liters_T=lambda kg:kg/M_T*V
        liters_He=lambda kg:kg/M_HE3*V
        gross_T=liters_T(d('dd_birth'));gross_He=(d('dd_events')-d('dd_t_atoms'))/AVOGADRO*V
        recovered=liters_T(d('route_recovered'));captured=liters_He(d('He3_store'))
        birth_only_He=i['He3_capture']*gross_He
        T_pipe=liters_T(start['T_pipeline']-end['T_pipeline'])
        He_pipe=i['He3_capture']*liters_He(start['He3_pipeline']-end['He3_pipeline'])
        T_burn=liters_T(d('a_burn'));T_loss=liters_T(d('route_loss'));T_decay=liters_T(d('route_decay'))
        results.append(dict(year=year,gross_T_branch_atom_STP_L=gross_T,gross_He3_branch_STP_L=gross_He,
          T_secondary_burn_atom_STP_L=T_burn,T_processing_loss_atom_STP_L=T_loss,T_route_decay_atom_STP_L=T_decay,
          T_pipeline_start_minus_end_atom_STP_L=T_pipe,T_recovered_atom_STP_L=recovered,
          He3_birth_only_capture_STP_L=birth_only_He,He3_pipeline_carry_capture_STP_L=He_pipe,He3_captured_STP_L=captured,
          He3_minus_T_delivered_STP_L=captured-recovered,T_identity_residual_STP_L=gross_T-T_burn-T_loss-T_decay+T_pipe-recovered,
          He3_identity_residual_STP_L=birth_only_He+He_pipe-captured,
          He3_percent_above_350k=(captured/350000-1)*100,T_percent_above_350k=(recovered/350000-1)*100))
    r.write('capture_difference_bridge.csv',results)
    k=p['a_reaction_day']+p['a_escape_day']+decay
    thermal_to_process=(1-p['a_fast_fraction']-p['a_fast_escape_fraction'])*p['a_escape_day']/k
    eventual_T=(p['a_fast_escape_fraction']+thermal_to_process)*p['a_plasma_process_day']/(p['a_plasma_process_day']+decay)*p['a_plasma_recovery']
    benchmark=dict(equal_branch=0.5,total_capture_target_STP_L=350000.,equal_capture_fraction=i['He3_capture'],
       equal_branch_birth_needed_STP_L=350000/i['He3_capture'],equal_path_reference_He3_STP_L=350000.,equal_path_reference_T_atom_STP_L=350000.,
       assumed_He3_eventual_capture_fraction=i['He3_capture'],candidate_T_eventual_recovery_fraction=eventual_T,
       candidate_eventual_T_to_He3_delivery_ratio=eventual_T/i['He3_capture'],
       observed_year2_T_to_He3_ratio=results[1]['T_recovered_atom_STP_L']/results[1]['He3_captured_STP_L'],
       finite_minus_asymptotic_ratio=results[1]['T_recovered_atom_STP_L']/results[1]['He3_captured_STP_L']-eventual_T/i['He3_capture'],
       max_route_replay_difference_kg=max_replay,physics_inputs_changed=False,
       original_exact_350k_input_sheet='UNRESOLVED; do not assume the original or simulator is incorrect',
       target_is_controller_input=True,physical_validation=False)
    (r.OUT/'capture_benchmark.json').write_text(json.dumps(benchmark,indent=2)+'\n')
    print(json.dumps(benchmark,indent=2))
    for x in results:print(x)
if __name__=='__main__':main()
