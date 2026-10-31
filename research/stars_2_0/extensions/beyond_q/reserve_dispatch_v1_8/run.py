"""Continuous-stock three-year heuristic dispatch, energy scenarios and provenance."""
from pathlib import Path
import csv,json,sys,hashlib,math
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;OUT=ROOT/'outputs'
sys.path.insert(0,str(PARENT/'paired_annual_v1_7'))
import compare as paired
from dispatchcycle.model import simulate
from dispatchcycle.physics import T_KG_PER_ATOM,AVOGADRO
from controller import Controller,HE3

def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def permitted(inputs):
    pre=inputs['precharge_hours'];hours=inputs['years']*inputs['hours_per_model_year']
    result=[(1,0)]*pre+[(1,1)]*hours
    start=pre+inputs['hours_per_model_year']+inputs['scheduled_common_outage_year2_start_day']*24
    for h in range(start,start+inputs['scheduled_common_outage_days']*24):result[h]=(0,0)
    return result

def execute(inputs,policy,tbr):
    parent=json.loads((PARENT/'paired_annual_v1_7/inputs.json').read_text())
    arc=next(c for c in parent['configurations'] if c['id']=='arc_matched_1100_1100')
    laser=next(c for c in parent['configurations'] if c['id']=='laser_matched_duty_1100_1100')
    if inputs['A_fusion_power_MW']!=1100 or inputs['B_fusion_power_MW']!=1100:raise ValueError('canonical two1100MW source lock')
    if inputs['source_duty']!=arc['a_source_duty'] or inputs['source_duty']!=arc['b_source_duty']:raise ValueError('source exposure mismatch')
    pre=inputs['precharge_hours'];H=inputs['hours_per_model_year']
    p=paired.parameters(arc,'B_replacement_A0',pre,inputs['years']*H,inputs['fuel_step_days']);p['tbr_b']=tbr
    control=Controller(inputs,policy);rows,summary=simulate(p,permitted(inputs),schedule_policy=control)
    energy_cases=[dict(architecture='ARC',case='net_A_'+('unknown' if x is None else str(-x))+'_MW',config=arc,parameters=dict(A_draw_MW=x)) for x in inputs['ARC_A_net_draw_MW_sensitivities']]
    energy_cases+=[dict(architecture='LASER',case=f"gain{q['gain']}_eta{q['eta']}",config=laser,parameters=q) for q in inputs['laser_energy_cases']]
    years={};energy={};prior={};he_mobile=he_store=he_loss=0.;he_born=0.;he4_mobile=he4_store=he4_loss=he4_born=0.;weekly=[]
    for index,r in enumerate(rows):
        year=0 if index<pre else 1+(index-pre)//H
        e=paired.step_energy(r,prior,arc,p);h=e['hours']
        d=lambda k:r[k]-prior.get(k,0.)
        before_he=he_store;before_he4=he4_store
        birth=(d('dd_events')-d('dd_t_atoms'))*HE3;he_born+=birth
        he_mobile,he_store,he_loss=paired.helium_step(he_mobile,he_store,he_loss,birth,h,inputs['He3_collection_day'],inputs['He3_capture'])
        birth4=(d('a_burn')+d('b_burn'))/T_KG_PER_ATOM*paired.HE4;he4_born+=birth4
        he4_mobile,he4_store,he4_loss=paired.helium_step(he4_mobile,he4_store,he4_loss,birth4,h,1.,.9)
        b=years.setdefault(year,dict(hours=0.,A_on_hours=0.,B_on_hours=0.,T_start_kg=prior.get('total_inventory',0.),T_end_kg=0.,T_B_store_end_kg=0.,
           T_DD_birth_kg=0.,T_B_blanket_birth_kg=0.,T_A_burn_kg=0.,T_B_burn_kg=0.,T_decay_kg=0.,T_process_loss_kg=0.,T_permeation_kg=0.,T_unserved_kg=0.,He3_start_captured_kg=before_he,He3_birth_kg=0.,He3_captured_to_store_kg=0.,He4_start_captured_kg=before_he4,He4_birth_kg=0.,He4_captured_to_store_kg=0.))
        b['hours']+=h;b['A_on_hours']+=r['on_a']*h;b['B_on_hours']+=r['on_b']*h;b['T_end_kg']=r['total_inventory'];b['T_B_store_end_kg']=r['b_store']
        for field,counter in [('T_DD_birth_kg','dd_birth'),('T_B_blanket_birth_kg','blanket_b_birth'),('T_A_burn_kg','a_burn'),('T_B_burn_kg','b_burn'),('T_decay_kg','decay'),('T_process_loss_kg','process_loss'),('T_permeation_kg','permeation'),('T_unserved_kg','b_unserved_burn')]:b[field]+=d(counter)
        b['He3_birth_kg']+=birth;b['He3_captured_to_store_kg']=he_store-b['He3_start_captured_kg']
        b['He4_birth_kg']+=birth4;b['He4_captured_to_store_kg']=he4_store-b['He4_start_captured_kg']
        for q in energy_cases:
            key=(year,q['architecture'],q['case'])
            total=energy.setdefault(key,{k:0. for k in ('generated_J','draw_J','net_J','import_kWh','positive_before_export_kWh')})
            ev=paired.electrical(e,q['config'],parent,q['parameters'])
            if ev is None:
                for k in total:total[k]=None
            else:
                for k in total:total[k]+=ev[k]
        if (index+1)%168==0 or index+1==len(rows) or index+1==pre or index+1 in [pre+j*H for j in range(1,inputs['years']+1)]:
            weekly.append(dict(policy=policy['id'],B_gross_TBR_assumed=tbr,time_hours=r['time_hours'],on_A=r['on_a'],on_B=r['on_b'],T_total_kg=r['total_inventory'],T_B_storage_kg=r['b_store'],He3_captured_stock_kg=he_store,He4_captured_stock_kg=he4_store))
        prior=r
    source=[];erows=[]
    for year,b in years.items():
        candidate=b['He3_captured_to_store_kg']*(1-inputs['He3_retained_fraction'])*inputs['He3_quality_acceptance']/.0030160293201*22.414
        target=policy['He3_external_candidate_target_STP_L_per_year'] if year else 0
        source.append(dict(policy=policy['id'],B_gross_TBR_assumed=tbr,year=year,**{k:v for k,v in b.items() if not k.startswith('_')},
          T_stock_change_kg=b['T_end_kg']-b['T_start_kg'],He3_external_candidate_STP_L=candidate,He3_external_candidate_target_STP_L=target,
          He3_target_shortfall_STP_L=max(0.,target-candidate),qualified_He3_kg=None,T_external_sales_kg=0,actual_revenue_USD=None,He4_blanket_Li_path_birth_unavailable_kg=b['T_B_blanket_birth_kg']/T_KG_PER_ATOM*paired.HE4))
        for q in energy_cases:
            total=energy[(year,q['architecture'],q['case'])]
            erows.append(dict(policy=policy['id'],B_gross_TBR_assumed=tbr,year=year,architecture=q['architecture'],energy_case=q['case'],hours=b['hours'],
              **total,mean_net_MW=total['net_J']/b['hours']/3.6e9 if total['net_J'] is not None else None,qualified_export_kWh=None,total_cost_USD=None,profit_USD=None))
    check=dict(policy=policy['id'],B_gross_TBR_assumed=tbr,controller_switches=control.switches,max_T_mass_residual_kg=summary['maximum_mass_residual_kg'],
      T_unserved_kg=summary['b_unserved_burn_kg'],He3_mass_residual_kg=he_born-he_mobile-he_store-he_loss,final_T_kg=rows[-1]['total_inventory'],
      final_He3_captured_kg=he_store,final_He4_captured_kg=he4_store,He4_mass_residual_kg=he4_born-he4_mobile-he4_store-he4_loss,physical_validation=False)
    return source,erows,weekly,check

def main():
    from provenance import verify
    OUT.mkdir(exist_ok=True)
    (OUT/'source_sha256.json').write_text(json.dumps(verify(),indent=2)+'\n')
    inputs=json.loads((ROOT/'inputs.json').read_text());sources=[];energies=[];weekly=[];checks=[]
    for tbr in inputs['B_gross_TBR_sensitivities']:
        for policy in inputs['policies']:
            s,e,w,c=execute(inputs,policy,tbr);sources+=s;energies+=e;weekly+=w;checks.append(c);print(c,flush=True)
    write('annual_dispatch.csv',sources);write('annual_energy.csv',energies);write('weekly_stocks.csv',weekly)
    (OUT/'checks.json').write_text(json.dumps(dict(cases=checks,physical_validation=False,gates='G1-G5 OPEN',actual_profit_USD=None,years=inputs['years'],source_simulations=len(checks),
       limitation='One shared candidate fuel model across architectures at matched fusion exposures; energy adapters differ. No actual He3 sales, replacements, certified capture or physically demonstrated DD operating point.'),indent=2)+'\n')
if __name__=='__main__':main()
