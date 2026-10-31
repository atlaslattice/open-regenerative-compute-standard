"""Receiver cells → correlated exploratory source → bounded cold-slab alpha escape."""
import argparse,hashlib,json,math,sys,platform,time
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--receiver',required=True);p.add_argument('--models',required=True);p.add_argument('--samples-per-cell',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out',required=True);a=p.parse_args()
if a.samples_per_cell<16 or a.samples_per_cell>8192 or a.seed<0:raise ValueError('explicit supported verification sample count and seed required')
root=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False);models=Path(a.models).resolve()
sys.path.insert(0,str(models/'coherent_source_v0_8'))
from amplitude import k,components,intensity,check_config
from coulomb import BACKEND,_path as cpc_path
sys.path.insert(0,str(models/'particle_handoff_v0_1'))
from handoff import Engine
from transport_v002 import rotation_to,propagate
engine=Engine();physics,_,_,Q=engine.p,engine.coordinate,engine.rows,engine.q
if abs(k.Q-Q)>1e-10:raise ValueError('source/receiver Q conventions differ')
config=json.loads((models/'coherent_source_v0_8/CANDIDATE_CONFIG.json').read_text());check_config(config)
raw=Path(a.receiver).read_bytes();receipt=json.loads(raw);case=next(x for x in receipt['results'] if x['case']=='field_on');record=case['receiver']['stage_records'][0];cells=record['ledger']['cells'];stage=case['target'];N=stage['normal_atoms_cm2'];R=rotation_to(record['input']['unit_direction_LAB'])
model,tables=physics.load_model();lo=model.PROJECTILES['alpha'][1]/1000
fn=lambda e:model.stopping(tables,model='srim13',projectile='alpha',material='B11',E_MeV=e,bn_electronic_multiplier=None,nuclear_variant='ZBL_SIMNRA_7_04')['total_eV_cm2_per_average_atom']
coordinates=[physics.Coordinate(fn,lo,12.,steps=n) for n in [8192,16384]]
source_cases=[('PHASE_SPACE_NULL',None,None,None),('COHERENT_L1_L3_RAW',.76,.67*2*math.pi,True),('INCOHERENT_RAW_ABLATION',.76,0.,False),('PURE_L1_CONTROL',1.,0.,True),('PURE_L3_CONTROL',0.,0.,True)]
rng=np.random.default_rng(a.seed);lab_bank=[];event_weights=[];cell_bank=[];Eout=[];Elower=[];Etail=[];facebank=[];depthbank=[];cellmeta=[];max_four=0.;max_shell=0.;max_birth_energy=0.;max_refine=0.;failed=[];max_budget=0.;start=time.time()
for j,cell in enumerate(cells):
 E=cell['local_proton_LAB_MeV'];expected=cell['expected_events'];depth=N*(j+.5)/len(cells)
 local_lab=[];local_amp=[];local_transport=[]
 for i in range(a.samples_per_cell):
  lab,initial=k.event(E,rng);cm=np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab]);amp,_=components(cm,config)
  rotated=lab.copy();rotated[:,1:]=lab[:,1:]@R.T;rotated_initial=initial.copy();rotated_initial[1:]=R@initial[1:];checks=k.verify(rotated,rotated_initial)
  max_four=max(max_four,checks['max_four_momentum_residual_MeV']);max_shell=max(max_shell,checks['max_relative_mass_shell_residual'])
  kinetic=rotated[:,0]-k.MA;max_birth_energy=max(max_birth_energy,abs(float(kinetic.sum())-(E+Q)))
  trans=[]
  for alpha,energy in zip(rotated,kinetic):
   mu=float(alpha[3]/np.linalg.norm(alpha[1:]));coarse=propagate(float(energy),mu,depth,N,coordinates[0]);fine=propagate(float(energy),mu,depth,N,coordinates[1])
   if coarse['escaped_E'] is not None and fine['escaped_E'] is not None:max_refine=max(max_refine,abs(coarse['escaped_E']-fine['escaped_E']))
   elif coarse['status']!=fine['status']:failed.append(dict(cell=j,sample=i,coarse=coarse['status'],fine=fine['status']))
   max_budget=max(max_budget,abs(float(energy)-(fine['escaped_E'] or 0)-fine['material_lower']-fine['unresolved_E']));trans.append(fine)
  local_lab.append(rotated);local_amp.append(amp);local_transport.append(trans)
 weights=[];ess=[]
 for name,mix,phase,coh in source_cases:
  w=np.ones(a.samples_per_cell) if mix is None else np.array([intensity(amp,mix_coefficient=mix,relative_phase_radians=phase,coherent=coh) for amp in local_amp])
  if not np.isfinite(w).all() or np.any(w<0) or w.sum()<=0:raise ValueError('invalid source weights; events not silently dropped')
  ess.append(float(w.sum()**2/(w@w)));weights.append(w/w.sum()*expected)
 lab_bank.extend(local_lab);event_weights.extend(np.array(weights).T);cell_bank.extend([j]*a.samples_per_cell);depthbank.extend([depth]*a.samples_per_cell)
 for row in local_transport:
  Eout.append([0. if t['escaped_E'] is None else t['escaped_E'] for t in row]);Elower.append([t['material_lower'] for t in row]);Etail.append([t['unresolved_E'] for t in row]);facebank.append([0 if t['escaped_E'] is None else (1 if t['face']=='REAR' else -1) for t in row])
 cellmeta.append(dict(cell=j,E_proton_LAB_MeV=E,normal_depth_atoms_cm2=depth,expected_events=expected,importance_ESS_by_case=dict(zip([x[0] for x in source_cases],ess))))
 print('cell',j,'done',flush=True)
lab=np.array(lab_bank);weights=np.array(event_weights);escaped=np.array(Eout);material=np.array(Elower);tail=np.array(Etail);faces=np.array(facebank);birth=lab[:,:,0]-k.MA
results=[]
for idx,(name,_,_,_) in enumerate(source_cases):
 w=weights[:,idx];alpha_w=np.broadcast_to(w[:,None],birth.shape);Rsum=float(w.sum());born=float(np.sum(alpha_w*birth));escape=float(np.sum(alpha_w*escaped));lower=float(np.sum(alpha_w*material));unresolved=float(np.sum(alpha_w*tail));counts=float(np.sum(alpha_w*(faces!=0)));unknown=float(np.sum(alpha_w*(faces==0)))
 result=dict(source=name,evidence='EXPLORATORY_SOURCE_AND_CALCULATED_COLD_STOPPING_NOT_CALIBRATED',expected_events=Rsum,alpha_birth_weight=3*Rsum,alpha_resolved_escape_weight=counts,alpha_unresolved_weight=unknown,birth_kinetic_MeV=born,resolved_escape_kinetic_MeV=escape,material_transfer_lower_MeV=lower,unresolved_kinetic_budget_MeV=unresolved,escape_energy_conditional_bounds_MeV=[escape,escape+unresolved],rear_escape_kinetic_MeV=float(np.sum(alpha_w*escaped*(faces==1))),front_escape_kinetic_MeV=float(np.sum(alpha_w*escaped*(faces==-1))),energy_budget_residual_MeV=born-escape-lower-unresolved,count_budget_residual=3*Rsum-counts-unknown,physical_uncertainty=None,collector_electricity_J=None,facility_net_electricity_J=None,exit_position_time=None)
 results.append(result)
checks=[dict(name='birth_four_momentum',passed=max_four<1e-8),dict(name='birth_mass_shell',passed=max_shell<1e-12),dict(name='each_birth_kinetic_sum',passed=max_birth_energy<1e-8),dict(name='each_alpha_escape_budget',passed=max_budget<1e-10),dict(name='stopping_refinement_1e_minus6_MeV',passed=max_refine<1e-6 and not failed)]
for x in results:
 for n,v in [('reaction_normalization_fixed',abs(x['expected_events']-case['expected_reactions'])<1e-12),('birth_energy_matches_receiver',abs(x['birth_kinetic_MeV']-case['alpha_birth_kinetic_MeV'])<1e-10),('alpha_count_budget',abs(x['count_budget_residual'])<1e-12),('alpha_energy_budget',abs(x['energy_budget_residual_MeV'])<1e-10),('no_net_power_promotion',x['facility_net_electricity_J'] is None)]:checks.append(dict(name=x['source']+'_'+n,passed=bool(v)))
np.savez_compressed(out/'EVENT_BANK.npz',alpha_LAB_four_vectors_MeV=lab,conditional_event_weights=weights,cell_index=np.array(cell_bank),normal_depth_atoms_cm2=np.array(depthbank),escaped_energy_MeV=escaped,material_transfer_lower_MeV=material,unresolved_energy_MeV=tail,face_code=faces)
report=dict(status='CONDITIONAL_INFINITE_SLAB_ALPHA_ESCAPE',receiver_sha256=hashlib.sha256(raw).hexdigest(),seed=a.seed,RNG='NumPy default_rng PCG64',samples_per_cell=a.samples_per_cell,total_proposals=len(lab),source_cases=[x[0] for x in source_cases],source_config=config,source_domain='Exploratory isolated unpolarized2-minus candidate extended to each local receiver energy; not fitted across this energy interval',material='COLD_ELEMENTAL_B11',geometry='LATERALLY_INFINITE_SLAB_NORMAL_COLUMN_CONTROL_NOT_REAL_POCKET',lower_stopping_energy_MeV=lo,stopping_grid_steps=[8192,16384],maximum_stopping_refinement_difference_MeV=max_refine,refinement_status_changes=failed,maximum_four_momentum_residual_MeV=max_four,maximum_birth_energy_residual_MeV=max_birth_energy,cells=cellmeta,results=results,checks=checks,physical_uncertainty='NOT_PROPAGATED; source conventions/material calibration unresolved; ESS is numerical diagnostic only',runtime_seconds=time.time()-start)
(out/'RESULTS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
(out/'RECEIPT.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,Coulomb_backend=BACKEND,CPC_library_sha256=hashlib.sha256(cpc_path.read_bytes()).hexdigest(),code_sha256={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in [Path(__file__).name,'transport_v002.py']},event_bank_sha256=hashlib.sha256((out/'EVENT_BANK.npz').read_bytes()).hexdigest(),scientific_freeze=False),indent=2)+'\n')
print('checks',len(checks),sum(x['passed'] for x in checks),'refinement',max_refine,'status_changes',len(failed));assert all(x['passed'] for x in checks)
