"""Traceable coherent transport benchmark with explicit assumptions and blocked readout."""
import argparse,hashlib,json,math,platform,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
for row in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
 if hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch '+row['file'])
sys.path.insert(0,str(ROOT.parent/'coupled_reference_v0_5'))
from physics import Coordinate,load_model,reactions
sys.path.insert(0,str(ROOT.parent/'coherent_source_v0_8'))
from amplitude import components,intensity,check_config,k,MA

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'

def summary(w,y):
 """Self-normalized importance mean and event-cluster delta-method MC covariance."""
 w=np.asarray(w,float);y=np.asarray(y,float)
 if w.ndim!=1 or y.ndim!=2 or len(w)!=len(y) or len(w)<2 or not np.isfinite(w).all() or not np.isfinite(y).all() or np.any(w<0) or w.sum()<=0:raise ValueError('finite nonnegative importance weights and event vectors required')
 norm=w/w.sum();mean=norm@y;res=y-mean
 cov=len(w)/(len(w)-1)*(res*norm[:,None]).T@(res*norm[:,None])
 return mean,cov,norm,float(1/(norm@norm))

def execute(c):
 expected={'schema','run_class','E_proton_LAB_MeV','material','stopping_model','nuclear_variant','total_atoms_cm2','depth_bins','samples_per_depth','seed','raw_mix_coefficient','relative_phase_radians','source_config','collection_axis_LAB','collection_half_angle_deg','true_exit_edges_MeV','detector_response','attempts'}
 if set(c)!=expected or c['schema']!='0.10' or c['run_class']!='ASSUMED_COHERENT_TRANSPORT_BENCHMARK':raise ValueError('explicit assumed benchmark required; CALIBRATED is not supported')
 check_config(c['source_config'])
 intensity(np.ones((2,5),complex),mix_coefficient=c['raw_mix_coefficient'],relative_phase_radians=c['relative_phase_radians'],coherent=True)
 if c['detector_response'] is not None:raise ValueError('no calibrated detector adapter in this benchmark; no invented response accepted')
 if c['material']!='B11':raise ValueError('this benchmark is explicitly B11, no calibration transfer from B10 or compounds')
 E=c['E_proton_LAB_MeV'];N=c['total_atoms_cm2'];n=c['samples_per_depth'];nb=c['depth_bins'];seed=c['seed']
 for v in [E,N]:
  if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:raise ValueError('nonnegative finite physical benchmark inputs required')
 if not .65<=E<=.70:raise ValueError('isolated resonance benchmark only; no universal source model')
 for v in [n,nb,seed]:
  if isinstance(v,bool) or not isinstance(v,int) or v<0:raise ValueError('explicit nonnegative integer numerical settings required')
 if not 2<=n<=4096 or not 1<=nb<=256:raise ValueError('supported integration settings required')
 if not c['attempts']:raise ValueError('all-attempt input required')
 ids=set()
 for a in c['attempts']:
  if set(a)!={'attempt_id','incident_protons'} or not a['attempt_id'] or a['attempt_id'] in ids:raise ValueError('unique complete attempt records required')
  ids.add(a['attempt_id']);v=a['incident_protons']
  if isinstance(v,bool) or not isinstance(v,int) or v<0:raise ValueError('nonnegative integer proton inventory required; missing is not zero')
 axis=np.asarray(c['collection_axis_LAB'],float);half=c['collection_half_angle_deg'];edges=np.asarray(c['true_exit_edges_MeV'],float)
 if axis.shape!=(3,) or not np.isfinite(axis).all() or not math.isclose(float(axis@axis),1.,abs_tol=1e-12) or not math.isfinite(half) or not 0<=half<=180:raise ValueError('explicit unit LAB cone required')
 if edges.ndim!=1 or len(edges)<2 or not np.isfinite(edges).all() or np.any(np.diff(edges)<=0):raise ValueError('ordered finite energy edges required')
 cut=math.cos(math.radians(half));model,tables=load_model();coords={}
 for species,maximum in [('proton',3.8),('alpha',12.)]:
  floor=model.PROJECTILES[species][1]/1000
  coords[species]=Coordinate(lambda e,s=species:model.stopping(tables,model=c['stopping_model'],projectile=s,material='B11',E_MeV=e,bn_electronic_multiplier=None,nuclear_variant=c['nuclear_variant'])['total_eV_cm2_per_average_atom'],floor,maximum)
 if edges[0]<coords['alpha'].e[0]:raise ValueError('threshold below unresolved alpha stopping floor')
 rows=json.loads((ROOT.parent/'coupled_reference_v0_5/EVENT_CROSS_SECTIONS.json').read_text())
 hazard=reactions(coords['proton'],rows,E,N,1.,nb);fine=reactions(coords['proton'],rows,E,N,1.,2*nb)
 if abs(hazard['probability']-fine['probability'])>1e-4*max(fine['probability'],1e-30):raise ValueError('reaction probability refinement gate failed')
 p=hazard['probability'];D=len(edges)-1;feature_names=[f'geometry_accepted_true_exit_bin_{j}' for j in range(D)]+['alpha_exit_energy_lower_MeV','alpha_exit_energy_upper_MeV','exit_count_lower','exit_count_upper']
 sums={name:np.zeros(D+4) for name in ['COHERENT','PHASE_SPACE_NULL']};covs={name:np.zeros((D+4,D+4)) for name in sums};trace=[];cells=[];max_res=0.
 rngs=np.random.SeedSequence(seed).spawn(nb)
 if p>0:
  for j,(cell,child) in enumerate(zip(hazard['bins'],rngs)):
   depth=cell['start_atoms_cm2']+cell['width_atoms_cm2']/2;localE=coords['proton'].outgoing(E,depth)
   if not .65<=localE<=.70:raise ValueError('target traverses beyond declared isolated-resonance benchmark interval')
   rng=np.random.default_rng(child);features=[];weights=[];records=[]
   for t in range(n):
    lab,initial=k.event(localE,rng);check=k.verify(lab,initial);max_res=max(max_res,check['max_four_momentum_residual_MeV'])
    cm=np.array([k.boost(a,-initial[1:]/initial[0]) for a in lab]);amp,_=components(cm,c['source_config'])
    w=intensity(amp,mix_coefficient=c['raw_mix_coefficient'],relative_phase_radians=c['relative_phase_radians'],coherent=True)
    y=np.zeros(D+4);alphas=[]
    for a in lab:
     birth=float(a[0]-MA);mom=float(np.linalg.norm(a[1:]));mu=float(a[3]/mom);path=(N-depth)/mu if mu>0 else depth/-mu if mu<0 else math.inf
     out=coords['alpha'].outgoing(birth,path) if birth>=coords['alpha'].e[0] and math.isfinite(path) else None
     geom=float(a[1:]@axis)/mom>=cut
     if out is None:lo=0.;hi=min(birth,float(coords['alpha'].e[0]));y[D+3]+=1;status='BELOW_STOPPING_MODEL_FLOOR_OUTCOME_UNRESOLVED'
     else:
      lo=hi=out;y[D+2:D+4]+=1;status='MODEL_EXIT_ENERGY_RESOLVED'
      if geom and out>=edges[0]:
       b=int(np.searchsorted(edges,out,side='right')-1)
       if not 0<=b<D:raise ValueError('true exit spectrum upper coverage missing')
       y[b]+=1
     y[D]+=lo;y[D+1]+=hi
     alphas.append(dict(birth_four_vector_LAB_MeV=a.tolist(),exit_energy_MeV=out,exit_energy_bounds_MeV=[lo,hi],geometry_accepts=bool(geom),status=status))
    features.append(y);weights.append(w);records.append(dict(depth_bin=j,proposal=t,reaction_depth_total_atoms_cm2=depth,local_proton_LAB_MeV=localE,raw_coherent_weight=w,alphas=alphas,conservation=check))
   y=np.asarray(features);cell_info={}
   for name,w in [('COHERENT',weights),('PHASE_SPACE_NULL',np.ones(n))]:
    mean,cov,norm,ess=summary(w,y);q=cell['event_probability'];sums[name]+=q*mean;covs[name]+=q*q*cov
    cell_info[name]=dict(probability_per_incident_proton=q,normalized_weights_sum=float(norm.sum()),importance_ESS=ess)
    if name=='COHERENT':
     for rec,weight in zip(records,norm):rec['coherent_event_probability_weight_per_incident_proton']=float(q*weight)
   cells.append(dict(depth_bin=j,local_proton_LAB_MeV=localE,source_normalization='separate within this depth bin; arbitrary amplitude scale cannot alter hazard',models=cell_info));trace.extend(records)
 attempts=[]
 for a in c['attempts']:
  Np=a['incident_protons'];by_model={}
  for name,y in sums.items():
   alpha=Np*y[D:D+2];proton=Np*(1-p)*hazard['unreacted_exit_energy_MeV'];budget=Np*E+Np*p*k.Q;loss=[budget-proton-alpha[1],budget-proton-alpha[0]]
   if loss[0]<-1e-8*max(1,budget):raise ValueError('primary particle energy ledger failed')
   by_model[name]=dict(expected_geometry_accepted_true_exit_bins=(Np*y[:D]).tolist(),expected_alpha_exit_energy_bounds_MeV=alpha.tolist(),expected_alpha_exit_count_bounds=(Np*y[D+2:D+4]).tolist(),expected_unreacted_proton_exit_kinetic_MeV=proton,primary_particle_loss_remainder_bounds_MeV=loss,expected_beam_kinetic_input_MeV=Np*E,expected_nuclear_Q_MeV=Np*p*k.Q,finite_importance_integration_covariance=(Np*Np*covs[name]).tolist(),detector_counts=None,recoverable_heat_MeV=None,wall_plug_energy_MeV=None,net_energy_MeV=None,financial_result=None)
  attempts.append(dict(**a,expected_reactions=Np*p,expected_alpha_births=3*Np*p,models=by_model))
 return dict(status='ASSUMED_COHERENT_TRANSPORT_BENCHMARK_NOT_CALIBRATED',proton_LAB_MeV=E,all_attempt_count=len(attempts),attempts=attempts,source_cells=cells,per_proton_reaction_probability=p,reaction_probability_depth_refinement_difference=abs(p-fine['probability']),feature_order=feature_names,maximum_four_momentum_residual_MeV=max_res,all_attempt_expected_reactions=sum(a['expected_reactions'] for a in attempts),coherence_affects_total_reaction_probability=False,
  source_rate_compatibility='Sikora2016 normalization was extracted with a different source ansatz; combining it with coherent or null shapes is a conditional benchmark, not a joint refit.',source_orientation='unpolarized parent assumed; not calibrated reaction alignment or LAB anisotropy',detector_status='BLOCKED_NO_MEASURED_RESPONSE; true exit/geometry quantities are not detector counts',stopping_status='SRIM_MODEL_ONLY_FOR_B11; B10 empirical calibration intentionally not transferred',MC_scope='Self-normalized importance delta-method covariance, finite integration only; alphas clustered by reaction. Proposals shared across attempts: their MC errors are correlated; do not sum attempt covariances as independent.',depth_scope='Midpoint transport per hazard cell; probability refinement checked, transport/depth and source-shape convergence not claimed',energy_scope='Primary-particle remainder is not recovered heat. Full startup/burn/grid/wall-plug/secondary-particle and economic ledgers remain unavailable.'),trace

def main():
 a=argparse.ArgumentParser();a.add_argument('config',type=Path);a.add_argument('--out',type=Path,required=True);a=a.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 try:
  c=json.loads(a.config.read_text());(a.out/'CONFIG.json').write_text(encoded(c));r,events=execute(c);(a.out/'RESULTS.json').write_text(encoded(r))
  with (a.out/'EVENTS.jsonl').open('w') as f:
   for event in events:f.write(json.dumps(event,sort_keys=True,allow_nan=False)+'\n')
  (a.out/'RECEIPT.json').write_text(encoded(dict(python=platform.python_version(),numpy=np.__version__,source_code_sha256=hashlib.sha256((ROOT/'reference.py').read_bytes()).hexdigest(),dependency_lock_sha256=hashlib.sha256((ROOT/'DEPENDENCY_LOCK.json').read_bytes()).hexdigest(),events=len(events),result_sha256=hashlib.sha256((a.out/'RESULTS.json').read_bytes()).hexdigest(),events_sha256=hashlib.sha256((a.out/'EVENTS.jsonl').read_bytes()).hexdigest())))
  print(encoded(dict(status=r['status'],events=len(events),all_attempts=r['all_attempt_count'],expected_reactions_assumed_scenario=r['all_attempt_expected_reactions'])))
 except Exception as e:
  (a.out/'FAILURE.json').write_text(encoded(dict(error=type(e).__name__,reason=str(e))));raise
if __name__=='__main__':main()
