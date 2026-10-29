"""Ideal-observable diagnostic using literature-informed amplitudes, not fitted data."""
import argparse,hashlib,json,math,sys,platform
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
for row in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
    if hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch '+row['file'])
sys.path.insert(0,str(ROOT.parent/'coherent_source_v0_8'))
from amplitude import components,k,MA
from coulomb import BACKEND,VERSION
from likelihood import kernel_from_amplitudes,distribution,fisher,fold,basis_rescale,rescaled_k

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'
def blob(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def calculate(samples,seed,bins):
    if samples<2 or samples>100000 or bins<2 or bins>100:raise ValueError('supported explicit computational grid required')
    c=json.loads((ROOT.parent/'coherent_source_v0_8/CANDIDATE_CONFIG.json').read_text());rng=np.random.default_rng(seed)
    E=.675;arrays=[];keys=[];max_residual=0.
    for _ in range(samples):
        lab,initial=k.event(E,rng);max_residual=max(max_residual,k.verify(lab,initial)['max_four_momentum_residual_MeV'])
        cm=np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab]);a,_=components(cm,c);arrays.append(a)
        energy=cm[:,0]-MA;f=energy/energy.sum();ids=np.floor(f*bins).astype(int)
        if np.any(ids<0) or np.any(ids>=bins):raise ValueError('fraction outside support')
        keys.append(tuple(sorted(ids.tolist())))
    point_kernel=kernel_from_amplitudes(np.array(arrays));unique=sorted(set(keys));lookup={key:i for i,key in enumerate(unique)}
    exclusive=np.zeros((len(unique),4))
    for key,row in zip(keys,point_kernel):exclusive[lookup[key]]+=row
    # A random alpha chosen from one event: stochastic coarsening, not 3 independent events.
    R=np.zeros((bins,len(unique)))
    for col,key in enumerate(unique):
        for i in key:R[i,col]+=1/3
    inclusive=fold(exclusive,R,append_missed=False)
    collapsed=exclusive.sum(axis=0,keepdims=True);mix=.76;phase=.67*2*math.pi
    reports={}
    for name,x in [('EXCLUSIVE_SORTED_ENERGY_BIN_TRIPLE',exclusive),('ONE_RANDOM_ALPHA_ENERGY_BIN',inclusive),('TOTAL_EVENT_COUNT_ONLY',collapsed),('UNBINNED_PROPOSAL_POINT_UPPER_DIAGNOSTIC',point_kernel)]:
        I=fisher(x,mix,phase);eig=np.linalg.eigvalsh(I);p,_=distribution(x,mix,phase)
        reports[name]=dict(probabilities=p.tolist() if len(p)<1000 else None,fisher_per_conditional_event=I.tolist(),eigenvalues=eig.tolist(),rank=int(np.linalg.matrix_rank(I,tol=1e-12)),
            condition_number_in_declared_coordinates=float(eig[-1]/eig[0]) if eig[0]>1e-12 else None,bins=len(x))
    If=fisher(point_kernel,mix,phase);Ie=fisher(exclusive,mix,phase);Ii=fisher(inclusive,mix,phase)
    deltas=dict(unbinned_minus_exclusive_eigenvalues=np.linalg.eigvalsh(If-Ie).tolist(),exclusive_minus_random_alpha_eigenvalues=np.linalg.eigvalsh(Ie-Ii).tolist())
    if min(deltas['unbinned_minus_exclusive_eigenvalues']+deltas['exclusive_minus_random_alpha_eigenvalues'])<-1e-10:raise ValueError('information coarsening inequality failed')
    # Rescale both basis amplitudes without altering any conditional distribution.
    scales=[2.,.5];kp=rescaled_k(mix,scales)
    p,_=distribution(exclusive,mix,phase);q,_=distribution(basis_rescale(exclusive,scales),kp,phase)
    err=float(np.max(abs(p-q)))
    if err>1e-12:raise ValueError('basis covariance failure')
    return dict(run_class='IDEAL_OBSERVABLE_INFORMATION_DIAGNOSTIC',experimental_data_fitted=False,detector_response='NONE: explicitly ideal source observables',
        samples=samples,seed=seed,incident_proton_LAB_MeV=E,energy_fraction_bins=bins,config=c,coordinates=['raw_basis_k','relative_phase_radians'],
        evaluation_point=dict(raw_basis_k=mix,relative_phase_radians=phase),observables=reports,information_coarsening_checks=deltas,
        basis_rescaling_diagnostic=dict(amplitude_scales=scales,original_k=mix,transformed_k=kp,maximum_probability_difference=err,meaning='same physics distribution; k is basis-dependent, not automatically a branching fraction'),
        exclusive_keys=unique,exclusive_kernel=exclusive.tolist(),random_alpha_response=R.tolist(),
        maximum_four_momentum_residual_MeV=max_residual,
        uncertainty='No apparatus noise, acceptance, calibration nuisance parameters or model-discrepancy covariance assumed. Fisher values are local ideal-model diagnostics per event, not experimental confidence intervals. Finite proposal integration error is assessed separately.',
        counting='One exclusive reaction event or one randomly selected alpha per reaction. Do not multiply random-alpha information by3; alphas from the same event are correlated.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--samples',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--bins',type=int,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('choose a new run directory')
    r=calculate(a.samples,a.seed,a.bins);a.out.mkdir(parents=True,exist_ok=False);(a.out/'INFORMATION.json').write_text(encoded(r))
    (a.out/'RECEIPT.json').write_text(encoded(dict(python=platform.python_version(),numpy=np.__version__,Coulomb_backend=BACKEND,GSL_3j=VERSION,
        code_sha256={n:blob(ROOT/n) for n in ['likelihood.py','run_information.py']},dependency_lock_sha256=blob(ROOT/'DEPENDENCY_LOCK.json'))))
    print(encoded({key:{k:v for k,v in val.items() if k!='probabilities'} for key,val in r['observables'].items()}))
if __name__=='__main__':main()
