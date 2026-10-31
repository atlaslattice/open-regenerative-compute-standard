"""Replay a fixed alpha bank through finite aspect-ratio numerical controls."""
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
from geometry import exit_box,energy_through_column,apparatus_gate
p=argparse.ArgumentParser();p.add_argument('--models',required=True);p.add_argument('--bank',required=True);p.add_argument('--receiver',required=True);p.add_argument('--out',required=True);a=p.parse_args()
root=Path(a.models).resolve();bank=Path(a.bank).resolve();out=Path(a.out).resolve();out.mkdir(exist_ok=False,parents=True);start=time.time()
package=Path(__file__).resolve().parent
for row in json.loads((package/'DEPENDENCY_LOCK.json').read_text()):
 if hashlib.sha256((root/row['path']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch: '+row['path'])
# Reject inconsistent bank/result/receipt pairs rather than accepting a convenient archive.
r=json.loads((bank.parent/'RESULTS.json').read_text());receipt=json.loads((bank.parent/'RECEIPT.json').read_text())
if hashlib.sha256(bank.read_bytes()).hexdigest()!=receipt['event_bank_sha256']:raise ValueError('bank receipt mismatch')
receiver_path=Path(a.receiver);receiver_bytes=receiver_path.read_bytes()
if hashlib.sha256(receiver_bytes).hexdigest()!=r['receiver_sha256']:raise ValueError('receiver mismatch')
receiver=json.loads(receiver_bytes);case=next(x for x in receiver['results'] if x['case']=='field_on');stage=case['receiver']['stage_records'][0]
u=np.array(stage['input']['unit_direction_LAB']);N=case['target']['normal_atoms_cm2']
if u[2]<=0 or case['target']['unit_normal_LAB']!=[0,0,1]:raise ValueError('this control requires forward beam and laboratory z normal')
b=np.load(bank);lab=b['alpha_LAB_four_vectors_MeV'];weights=b['conditional_event_weights'];depth=b['normal_depth_atoms_cm2'];M=json.loads((root/'coupled_reference_v0_5/MASS_SOURCE.json').read_text())['alpha_MeV'];energy=lab[:,:,0]-M
sys.path.insert(0,str(root/'particle_handoff_v0_1'));from handoff import Engine
engine=Engine();physics=engine.p;model,tables=physics.load_model();floor=model.PROJECTILES['alpha'][1]/1000
fn=lambda E:model.stopping(tables,model='srim13',projectile='alpha',material='B11',E_MeV=E,bn_electronic_multiplier=None,nuclear_variant='ZBL_SIMNRA_7_04')['total_eV_cm2_per_average_atom']
coordinate=physics.Coordinate(fn,floor,12.,steps=16384)
# Mean beam ray in homogeneous uniform material. Finite beam profile is NOT recovered.
positions=np.column_stack([depth*u[0]/u[2],depth*u[1]/u[2],depth]);directions=lab[:,:,1:]/np.linalg.norm(lab[:,:,1:],axis=2)[:,:,None]
controls=[2.,10.,100.,1e6];results=[];checks=[];last_escape=None;max_path_residual=0.
for aspect in controls:
 lower=np.array([-aspect*N/2,-aspect*N/2,0]);upper=np.array([aspect*N/2,aspect*N/2,N]);escape=np.zeros_like(energy);material=np.zeros_like(energy);tail=np.zeros_like(energy);exit_pos=np.zeros_like(directions);path=np.zeros_like(energy);edge=np.zeros_like(energy,dtype=bool);face_codes=np.zeros_like(energy,dtype=np.int8)
 for i in range(len(lab)):
  for j in range(3):
   hit=exit_box(positions[i],directions[i,j],lower,upper);d=hit['path_column_atoms_cm2'];path[i,j]=d;exit_pos[i,j]=hit['exit_column_position_atoms_cm2'];faces=hit['faces'];edge[i,j]=any(f[0]!='Z' for f in faces)
   face_codes[i,j]=0 if len(faces)>1 else (1 if faces[0]=='Z+' else -1 if faces[0]=='Z-' else 2)
   t=energy_through_column(float(energy[i,j]),d,coordinate);escape[i,j]=t['escaped_E'] or 0.;material[i,j]=t['material_lower'];tail[i,j]=t['unresolved_E']
   max_path_residual=max(max_path_residual,float(np.max(abs(exit_pos[i,j]-(positions[i]+d*directions[i,j]))))/N)
 checks.append({'name':str(aspect)+'_per_alpha_energy_budget','passed':bool(np.max(abs(energy-escape-material-tail))<1e-10)})
 if last_escape is not None:checks.append({'name':str(aspect)+'_wider_target_does_not_increase_each_escape_energy','passed':bool(np.all(escape<=last_escape+1e-10))})
 last_escape=escape.copy();rows=[]
 for k,name in enumerate(r['source_cases']):
  w=weights[:,k,None];ex=float(np.sum(w*escape));un=float(np.sum(w*tail));born=float(np.sum(w*energy));mat=float(np.sum(w*material));baseline=r['results'][k]['resolved_escape_kinetic_MeV']
  rows.append({'source':name,'expected_reactions':float(weights[:,k].sum()),'birth_kinetic_MeV':born,'resolved_escape_kinetic_MeV':ex,'material_transfer_lower_MeV':mat,'unresolved_kinetic_budget_MeV':un,'escape_conditional_bounds_MeV':[ex,ex+un],'edge_crossing_alpha_weight':float(np.sum(w*edge)),'resolved_escape_difference_from_infinite_control_MeV':ex-baseline,'budget_residual_MeV':born-ex-mat-un,'collector_electricity_J':None,'net_electricity_J':None})
 checks.append({'name':str(aspect)+'_fixed_reaction_counts','passed':all(abs(x['expected_reactions']-case['expected_reactions'])<1e-12 for x in rows)})
 results.append({'aspect_ratio_width_to_normal_thickness':aspect,'rows':rows})
 np.savez_compressed(out/('aspect_'+str(aspect)+'.npz'),birth_column_positions_atoms_cm2=positions,exit_column_positions_atoms_cm2=exit_pos,path_columns_atoms_cm2=path,face_codes=face_codes,escaped_energy_MeV=escape,material_transfer_lower_MeV=material,unresolved_energy_MeV=tail)
checks.append({'name':'ray_endpoint_residual','passed':max_path_residual<1e-12});checks.append({'name':'wide_box_recovers_saved_infinite_slab_escape','passed':all(abs(x['resolved_escape_difference_from_infinite_control_MeV'])<1e-12 for x in results[-1]['rows'])})
# Informative comparison only: finite-box controls have no observed length scale.
report={'status':'FINITE_UNIFORM_BOX_NUMERICAL_CONTROLS_ONLY','bank_sha256':hashlib.sha256(bank.read_bytes()).hexdigest(),'receiver_sha256':hashlib.sha256(receiver_bytes).hexdigest(),'normal_column_atoms_cm2':N,'material':'COLD_ELEMENTAL_B11','birth_position_model':'CENTROID_RAY_FROM_INHERITED_PROTON_DIRECTION_AND_MIDPOINT_DEPTH','physical_positions_m':None,'exit_times_s':None,'support_transport':'NOT_IMPLEMENTED','original_pocket_gate':apparatus_gate({}),'controls':results,'checks':checks,'runtime_seconds':time.time()-start,'numerical_scope':'Not matched physical targets: fixed event bank and normal column, lateral boundaries only; not a full source/target rerun or pocket prediction.'}
(out/'RESULTS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
(out/'RECEIPT.json').write_text(json.dumps({'code_sha256':{f:hashlib.sha256((package/f).read_bytes()).hexdigest() for f in ['run.py','geometry.py']},'numpy':np.__version__,'outputs_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in out.glob('*.npz')}},indent=2)+'\n')
print('checks',sum(x['passed'] for x in checks),'/',len(checks));assert all(x['passed'] for x in checks)
