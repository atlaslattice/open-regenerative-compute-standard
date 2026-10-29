"""Source -> reaction depth -> phase-space NULL -> bounded escape -> response.
Conditional integration reference; not calibrated Stars output or a burn calculation.
"""
import argparse,hashlib,json,math,platform,sys
from pathlib import Path
import numpy as np
from kinematics import event,verify,MA,MP,MB,Q
from physics import Coordinate,load_model,reactions,sample_depth
from vendor.detector import Response

ROOT=Path(__file__).resolve().parent

def encoded(x):return json.dumps(x,indent=2,allow_nan=False,sort_keys=True)+'\n'

def check_dependencies():
    for r in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
        if hashlib.sha256((ROOT/r['file']).read_bytes()).hexdigest()!=r['sha256']:
            raise ValueError('dependency identity mismatch: '+r['file'])

def execute(c,keep_events=True):
    check_dependencies()
    required={'schema','run_class','source_model','proton_energy_frame','model','material','bn_electronic_multiplier','total_atoms_cm2','sampled_events_per_nonzero_shot','seed','shots','detector_axis_LAB','detector_half_angle_deg','response'}
    if set(c)!=required or c['schema']!='0.5' or c['run_class']!='CONDITIONAL_NULL_REFERENCE' or c['source_model']!='CONSTANT_MATRIX_ELEMENT_PHASE_SPACE_NULL' or c['proton_energy_frame']!='LAB':
        raise ValueError('explicit supported null-model schema and LAB energies required')
    n=c['sampled_events_per_nonzero_shot'];seed=c['seed']
    if isinstance(n,bool) or not isinstance(n,int) or not 2<=n<=100000:raise ValueError('at least two conditional event samples required')
    if isinstance(seed,bool) or not isinstance(seed,int) or seed<0:raise ValueError('nonnegative integer seed required')
    if not c['shots']:raise ValueError('all-shot input required')
    ids=set()
    for s in c['shots']:
        if set(s)!={'attempt_id','incident_protons','E_proton_LAB_MeV'} or not s['attempt_id'] or s['attempt_id'] in ids:raise ValueError('unique complete attempt inputs required')
        ids.add(s['attempt_id']);Np=s['incident_protons']
        if isinstance(Np,bool) or not isinstance(Np,int) or Np<0:raise ValueError('nonnegative integer proton count required')
        if isinstance(s['E_proton_LAB_MeV'],bool) or not isinstance(s['E_proton_LAB_MeV'],(int,float)) or not math.isfinite(s['E_proton_LAB_MeV']) or s['E_proton_LAB_MeV']<=0:raise ValueError('positive finite LAB proton energy required')
    N=float(c['total_atoms_cm2'])
    if not math.isfinite(N) or N<0:raise ValueError('invalid target column')
    if c['material'] not in {'B11','BN_B11_N14'}:raise ValueError('p-B11 reaction lane requires explicit B11 inventory; generic boron is insufficient')
    model,tables=load_model();material=c['material'];mix=c['bn_electronic_multiplier']
    coordinates={}
    for species,maximum in [('proton',3.8),('alpha',12.)]:
        _,m=model.PROJECTILES[species];floor=m/1000
        def stopping(E,species=species):
            return model.stopping(tables,model=c['model'],projectile=species,material=material,E_MeV=E,bn_electronic_multiplier=mix)['total_eV_cm2_per_average_atom']
        coordinates[species]=Coordinate(stopping,floor,maximum)
    fB=model.stopping(tables,model=c['model'],projectile='proton',material=material,E_MeV=.65,bn_electronic_multiplier=mix)['boron_atom_fraction']
    response=Response(**c['response']);R=response.arrays()
    if response.species!='alpha' or response.evidence_state!='SYNTHETIC':raise ValueError('reference requires explicit SYNTHETIC alpha response')
    edges=np.array(response.true_edges_mev)
    if edges[0]<coordinates['alpha'].e[0]:raise ValueError('detector threshold below unresolved stopping floor')
    axis=np.asarray(c['detector_axis_LAB'],float)
    if axis.shape!=(3,) or not np.isfinite(axis).all() or not math.isclose(float(axis@axis),1.,abs_tol=1e-12):raise ValueError('unit LAB detector axis required')
    half=float(c['detector_half_angle_deg'])
    if not math.isfinite(half) or not 0<=half<=180:raise ValueError('invalid detector cone')
    angular_cut=math.cos(math.radians(half));rows=json.loads((ROOT/'EVENT_CROSS_SECTIONS.json').read_text())
    attempts=[];records=[];seed_sequences=np.random.SeedSequence(seed).spawn(len(c['shots']))
    for shot,sequence in zip(c['shots'],seed_sequences):
        E=float(shot['E_proton_LAB_MeV']);Np=shot['incident_protons']
        coarse=reactions(coordinates['proton'],rows,E,N,fB,128)
        hazard=reactions(coordinates['proton'],rows,E,N,fB,256)
        p=hazard['probability'];lam=Np*p
        delta=abs(p-coarse['probability'])
        if delta>1e-4*max(p,1e-30):raise ValueError('reaction integration refinement failed')
        values=[];energy_out_bounds=[];exit_count_bounds=[];geometry_count_bounds=[];max_residual=0.;unresolved=0
        rng=np.random.default_rng(sequence)
        if lam>0:
            for j in range(n):
                depth=sample_depth(hazard,rng);localE=coordinates['proton'].outgoing(E,depth)
                alphas,initial=event(localE,rng);checks=verify(alphas,initial)
                max_residual=max(max_residual,checks['max_four_momentum_residual_MeV'])
                y=np.zeros(len(edges)-1);details=[];lower=upper=0.;resolved_count=0;geometry_resolved=0;geometry_unknown=0
                for a in alphas:
                    born=float(a[0]-MA);momentum=float(np.linalg.norm(a[1:]));mu=float(a[3]/momentum)
                    path=(N-depth)/mu if mu>0 else depth/(-mu) if mu<0 else math.inf
                    if born<coordinates['alpha'].e[0] or not math.isfinite(path):out=None
                    else:out=coordinates['alpha'].outgoing(born,path)
                    geometry=float(a[1:]@axis)/momentum>=angular_cut
                    if out is None:
                        bound=min(born,float(coordinates['alpha'].e[0]));unresolved+=1
                        status='BELOW_POSITIVE_STOPPING_FLOOR; OUTGOING_ENERGY_UNKNOWN'
                        lower+=0.;upper+=bound
                        if geometry:geometry_unknown+=1
                    else:
                        bound=out;lower+=out;upper+=out;status='EXIT_ENERGY_RESOLVED_IN_MODEL'
                        resolved_count+=1
                        if geometry:geometry_resolved+=1
                        if geometry and out>=edges[0]:
                            k=int(np.searchsorted(edges,out,side='right')-1)
                            if not 0<=k<len(y):raise ValueError('detector upper energy coverage missing')
                            y[k]+=1
                    details.append(dict(birth_four_vector_LAB_MeV=a.tolist(),birth_kinetic_MeV=born,mu_LAB=mu,
                        exit_energy_MeV=out,exit_energy_upper_bound_MeV=bound,geometry_accepts=geometry,status=status))
                values.append(y);energy_out_bounds.append((lower,upper));exit_count_bounds.append((resolved_count,3));geometry_count_bounds.append((geometry_resolved,geometry_resolved+geometry_unknown))
                if keep_events:records.append(dict(attempt_id=shot['attempt_id'],conditional_sample=j,weight_expected_events=lam/n,
                    reaction_depth_total_atoms_cm2=depth,proton_at_reaction_LAB_MeV=localE,
                    initial_four_vector_LAB_MeV=initial.tolist(),alphas=details,checks=checks))
            values=np.asarray(values);true_counts=lam*values.mean(axis=0)
            measured_per_event=values@R.T
            covariance=(lam*lam/n)*np.atleast_2d(np.cov(measured_per_event,rowvar=False,ddof=1))
            alpha_bounds=(lam*np.mean(energy_out_bounds,axis=0)).tolist()
            exit_bounds=(lam*np.mean(exit_count_bounds,axis=0)).tolist();geometry_bounds=(lam*np.mean(geometry_count_bounds,axis=0)).tolist()
        else:
            true_counts=np.zeros(len(edges)-1);covariance=np.zeros((R.shape[0],R.shape[0]));alpha_bounds=[0.,0.];exit_bounds=geometry_bounds=[0.,0.]
        folded=response.fold('alpha',true_counts)
        proton_exit=Np*(1-p)*hazard['unreacted_exit_energy_MeV'];particle_budget=Np*E+lam*Q
        loss_bounds=[particle_budget-proton_exit-alpha_bounds[1],particle_budget-proton_exit-alpha_bounds[0]]
        attempts.append(dict(**shot,per_proton_reaction_probability=p,expected_fusion_events=lam,
            expected_alpha_births=3*lam,probability_at_least_one_event=-math.expm1(-Np*hazard['optical_depth']),
            expected_alpha_exit_count_bounds=exit_bounds,expected_geometry_accepted_exit_count_bounds=geometry_bounds,
            unreacted_proton_exit_energy_MeV=hazard['unreacted_exit_energy_MeV'],
            expected_unreacted_proton_exit_kinetic_MeV=proton_exit,
            expected_beam_kinetic_input_MeV=Np*E,expected_nuclear_Q_MeV=lam*Q,
            expected_primary_particle_loss_bounds_MeV=loss_bounds,
            loss_scope='ledger remainder conditional on the modeled primary particles; NOT a heat-recovery estimate',
            expected_alpha_exit_kinetic_bounds_MeV=alpha_bounds,source_reaction_refinement_delta=delta,
            sampled_conditional_events=n if lam>0 else 0,unresolved_alpha_exits_in_samples=unresolved,
            maximum_four_momentum_residual_MeV=max_residual,detector=folded,
            conditional_monte_carlo_detector_covariance=covariance.tolist(),
            covariance_scope='finite-event-sampling error only; not physical shot noise or calibration/source uncertainty'))
    return dict(schema='0.5',status='CONDITIONAL_NULL_REFERENCE_NOT_CALIBRATED',scientific_outcome='NOT_TESTED',
        source_shape='CONSTANT_MATRIX_ELEMENT_PHASE_SPACE_NULL; not the publication sequential l=3 spectrum',
        source_normalization='Sikora–Weller2016 model-extrapolated event table with explicit linear LAB-energy interpolation >=0.22MeV',
        source_consistency_warning='normalization was extracted using a different spectrum ansatz; this alternate null shape is not a self-consistent refit of those data',
        masses=dict(proton_MeV=MP,B11_nucleus_MeV=MB,alpha_MeV=MA,Q_MeV=Q),
        attempts=attempts,all_attempt_count=len(attempts),expected_fusion_events_all_attempts=sum(s['expected_fusion_events'] for s in attempts),
        heat_recovery='UNAVAILABLE; primary particle energy loss is not recoverable heat',net_energy='UNAVAILABLE; no burn or full wall-plug ledger',
        experimental_calibration='NOT_RUN',acoustic_effect='NO COUPLING ASSIGNED',
        limitations=['no Be8 dynamics, resonance amplitudes or interference in null shape','no competing channels, neutrons or impurity reactions calculated','no scattering/straggling or target evolution','synthetic detector response','mass and stopping/source uncertainty not propagated','conditional samples are not actual shots']),records

def main():
    p=argparse.ArgumentParser();p.add_argument('config',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=False)
    try:
        c=json.loads(a.config.read_text());(a.out/'CONFIG.json').write_text(encoded(c));result,events=execute(c)
        (a.out/'RESULTS.json').write_text(encoded(result))
        with (a.out/'EVENTS.jsonl').open('w') as f:
            for event_record in events:f.write(json.dumps(event_record,allow_nan=False,sort_keys=True)+'\n')
        receipt=dict(python=platform.python_version(),numpy=np.__version__,seed=c['seed'],generator='NumPy default_rng PCG64, SeedSequence child per attempt',
            code_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.glob('*.py')},event_samples=len(events))
        (a.out/'RECEIPT.json').write_text(encoded(receipt))
        (a.out/'MANIFEST.json').write_text(encoded({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in a.out.iterdir()}))
        print(encoded(dict(status=result['status'],attempts=len(result['attempts']),sampled_events=len(events),expected_fusion_events_all_attempts=result['expected_fusion_events_all_attempts'])))
    except Exception as e:
        (a.out/'FAILURE.json').write_text(encoded(dict(status='FAILED',error=type(e).__name__,reason=str(e))))
        raise

if __name__=='__main__':main()
