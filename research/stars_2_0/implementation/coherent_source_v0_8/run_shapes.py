"""Common invariant-phase-space proposal, explicitly reweighted by candidate amplitudes.
Reports conditional shapes only; no fusion-yield or experimental calibration claim.
"""
import argparse,hashlib,json,math,platform
from pathlib import Path
import numpy as np
import scipy
from amplitude import ROOT,k,MA,components,intensity,check_config
from coulomb import VERSION,BACKEND

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'

def calculate(config,*,samples,seed):
    check_config(config)
    if isinstance(samples,bool) or not isinstance(samples,int) or samples<2 or samples>100000:raise ValueError('explicit supported sample count required')
    if isinstance(seed,bool) or not isinstance(seed,int) or seed<0:raise ValueError('explicit nonnegative seed required')
    rng=np.random.default_rng(seed);arrays=[];energies=[];max_res=0.
    # Only the isolated 2-minus resonance is explored; not an energy-independent source law.
    E=.675
    for _ in range(samples):
        lab,initial=k.event(E,rng);max_res=max(max_res,k.verify(lab,initial)['max_four_momentum_residual_MeV'])
        cm=np.array([k.boost(v,-initial[1:]/initial[0]) for v in lab])
        amp,_=components(cm,config);arrays.append(amp);energies.append(cm[:,0]-MA)
    amp=np.array(arrays);energies=np.array(energies);edges=np.linspace(0.,k.Q+E,41)
    cases=[('PURE_L1_CONTROL',1.,0.,True),('PURE_L3_CONTROL',0.,0.,True),
        ('COHERENT_RAW_COEFFICIENT_0p76_PHASE_0p67_2PI',.76,.67*2*math.pi,True),
        ('COHERENT_RAW_COEFFICIENT_0p85_PHASE_ZERO',.85,0.,True),
        ('INCOHERENT_0p76_ABLATION',.76,0.,False)]
    results={}
    for name,mix,phase,coherent in cases:
        weights=np.array([intensity(a,mix_coefficient=mix,relative_phase_radians=phase,coherent=coherent) for a in amp])
        total=float(weights.sum())
        if not np.isfinite(weights).all() or total<=0:raise ValueError('invalid candidate importance weights')
        normalized=weights/total
        counts=np.histogram(energies.ravel(),bins=edges,weights=np.repeat(normalized,3))[0]
        if abs(float(counts.sum())-3)>1e-10:raise ValueError('three-alpha spectrum normalization failure')
        results[name]=dict(mix_coefficient=mix,relative_phase_radians=phase,coherent=coherent,
            raw_weight_mean=float(weights.mean()),importance_ESS=float(total*total/(weights@weights)),
            alpha_CM_counts_per_conditional_event=counts.tolist(),
            alpha_CM_fraction_below_1MeV=float(np.sum(normalized*np.sum(energies<1.,axis=1))/3),
            calibrated=False)
    return dict(run_class='EXPLORATORY_LITERATURE_MODEL',incident_proton_LAB_MeV=E,samples=samples,seed=seed,
        rng='NumPy default_rng PCG64',proposal='constant-matrix-element Lorentz invariant phase space; proposal is computational, weights specify candidate shape',
        basis='RAW_EQUATIONS_NOT_BRANCH_FRACTIONS; reported fit percentages not asserted reproducible in this basis',
        maximum_input_four_momentum_residual_MeV=max_res,alpha_CM_energy_edges_MeV=edges.tolist(),cases=results,
        source_fit='NOT_RUN',predicted_reaction_events=None,detector_fold='NOT_RUN',
        experimental_uncertainty='NOT_PROPAGATED; ESS is only an importance-weight diagnostic, not a confidence interval or model validation')

def main():
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--samples',type=int,required=True);p.add_argument('--seed',type=int,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('choose a new output directory')
    c=json.loads(a.config.read_text());r=calculate(c,samples=a.samples,seed=a.seed);a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'CONFIG.json').write_text(encoded(c));(a.out/'SHAPES.json').write_text(encoded(r))
    (a.out/'RECEIPT.json').write_text(encoded(dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,GSL_3j=VERSION,Coulomb_backend=BACKEND,
        code_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['amplitude.py','coulomb.py','run_shapes.py']},
        config_sha256=hashlib.sha256(a.config.read_bytes()).hexdigest())))
    print(encoded({name:{key:value for key,value in case.items() if key!='alpha_CM_counts_per_conditional_event'} for name,case in r['cases'].items()}))

if __name__=='__main__':main()
