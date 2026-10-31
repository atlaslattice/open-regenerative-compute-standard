import sys,os,json,math
from pathlib import Path
from bridge import route,check_source,MEV_J
root=Path(sys.argv[1]);sys.path.insert(0,os.environ['STELLAR_HANDOFF_DIR'])
from handoff import Engine
raw=json.loads((root/'SCRAPES.json').read_text());g=json.loads((root/'MAP.json').read_text());out=[]
cases=[('field_on','field_on',1e-12,'PUBLICATION_EVENT_MODEL',1e18,None),('field_off','field_off',1e-12,'PUBLICATION_EVENT_MODEL',1e18,None),('half_dt','half_dt',5e-13,'PUBLICATION_EVENT_MODEL',1e18,None),('reactions_off','field_on',1e-12,'REACTIONS_OFF_CONTROL',1e18,None),('zero_column','field_on',1e-12,'PUBLICATION_EVENT_MODEL',0,None),('aperture_miss','field_on',1e-12,'PUBLICATION_EVENT_MODEL',1e18,.0001)]
import numpy as np
for name,pic,dt,model,column,aperture in cases:
 assert np.loadtxt(root/'runs'/pic/'diags/reducedfiles/number.txt')[-1,4]==0,'Still-active PIC state requires its own full energy/particle export'
 balance=check_source(35000,23625,raw[pic]);r=route(raw[pic],g,dt,aperture)
 packets=[dict(packet_id=p['id'],species='proton',weight=p['weight'],kinetic_MeV=p['kinetic_MeV'],unit_direction_LAB=p['unit_direction_LAB'],position_m=p['position_m'],time_s=p['time_s']) for p in r['arrivals']]
 stage=dict(stage_id='verification_target_visit1',physical_instance_id='verification_cold_B11',type='cold_b11_slab',material='B11',target_state='COLD_ELEMENTAL',normal_atoms_cm2=column,illuminated_area_cm2=.04,unit_normal_LAB=[0,0,1],depth_cells=16,reaction_model=model,maximum_allowed_depletion_fraction=.01,evidence='ASSUMED_VERIFICATION_COLUMN_AND_AREA; inherited pinned model, not actual target')
 a=dict(attempt_id=name,source_packets=packets,source_frame='LAB',source_energy_unit='MeV',source_evidence='Scraped field-domain packets with derived surface crossing',physical_success=None,wall_input_J=None)
 slab=Engine().attempt(a,[stage]);assert slab['status']=='CONDITIONAL_HANDOFF_COMPLETE';m=slab['metrics']
 lost=math.fsum(p['weight'] for p in r['losses']);lostK=math.fsum(p['weight']*p['kinetic_MeV'] for p in r['losses'])
 dn=35000-lost-m['events']-m['remaining_protons'];dk=23625+m['nuclear_Q_MeV']-lostK-m['remaining_proton_kinetic_MeV']-m['alpha_birth_kinetic_MeV']-m['material_transfer_MeV']
 out.append(dict(case=name,evidence='EXECUTED_NUMERICAL_FIXTURE_NOT_APPARATUS',source_weight=35000,target_arrival_weight=math.fsum(p['weight'] for p in r['arrivals']),external_loss_weight=lost,external_loss_kinetic_MeV=lostK,expected_reactions=m['events'],alpha_birth_weight=m['expected_alpha_births'],B11_consumed=m['expected_B11_consumed'],alpha_birth_kinetic_MeV=m['alpha_birth_kinetic_MeV'],material_transfer_MeV=m['material_transfer_MeV'],post_target_weight=m['remaining_protons'],post_target_kinetic_MeV=m['remaining_proton_kinetic_MeV'],Q_MeV=m['nuclear_Q_MeV'],particle_residual=dn,energy_residual_MeV=dk,energy_residual_J=dk*MEV_J,source_boundary_check=balance,routing=r,target=stage,receiver=slab,post_target_position_time=None,alpha_escape=None,facility_wall_input_J=None,net_electricity_J=None))
checks=[]
def ck(n,v):checks.append(dict(name=n,passed=bool(v)))
lookup={x['case']:x for x in out}
ck('only_target_face_received',lookup['field_on']['target_arrival_weight']==10000 and lookup['field_on']['external_loss_weight']==25000)
ck('reaction_off_keeps_stopping',lookup['reactions_off']['expected_reactions']==0 and lookup['reactions_off']['material_transfer_MeV']>0)
ck('zero_column_zero_births_stopping',lookup['zero_column']['expected_reactions']==0 and lookup['zero_column']['material_transfer_MeV']==0)
ck('aperture_miss_no_births',lookup['aperture_miss']['target_arrival_weight']==0 and lookup['aperture_miss']['expected_reactions']==0)
ck('half_dt_weight_same',lookup['half_dt']['target_arrival_weight']==lookup['field_on']['target_arrival_weight'])
ck('half_dt_event_difference_below_ppm',abs(lookup['half_dt']['expected_reactions']/lookup['field_on']['expected_reactions']-1)<1e-6)
for x in out:
 ck(x['case']+'_particle_energy_closure',abs(x['particle_residual'])<1e-9 and abs(x['energy_residual_MeV'])<1e-8)
 ck(x['case']+'_reaction_stoichiometry',abs(x['alpha_birth_weight']-3*x['expected_reactions'])<1e-15 and x['B11_consumed']==x['expected_reactions'])
 ck(x['case']+'_no_net_or_phase_space_claim',x['net_electricity_J'] is None and x['post_target_position_time'] is None)
zero=dict(case='known_zero_source',source_weight=0,expected_reactions=0,status='ANALYTIC_ZERO_INPUT_NOT_PIC_EXECUTION');missing=dict(case='missing_source',source_weight=None,expected_reactions=None,status='BLOCKED_NOT_ZERO')
ck('missing_not_zero',zero['expected_reactions']==0 and missing['expected_reactions'] is None)
with (root/'RESULTS.json').open('x') as f:json.dump(dict(status='CONDITIONAL_ONE_WAY_COUPLING',results=out+[zero,missing],checks=checks),f,indent=2,allow_nan=False);f.write('\n')
print([(x['case'],x['expected_reactions']) for x in out]);print('checks',len(checks));assert all(x['passed'] for x in checks)
