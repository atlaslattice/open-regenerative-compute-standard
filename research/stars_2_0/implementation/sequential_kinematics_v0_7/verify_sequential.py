"""Seeded numerical verification inputs are not experimental draws or source parameters."""
import argparse,hashlib,json,platform
from pathlib import Path
import numpy as np
from sequential import build_event,k,MA,MP,MB,Q

ROOT=Path(__file__).resolve().parent
def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'

def verification():
    rng=np.random.default_rng(20261029);samples=[];four=mass=pair=energy=0.;n=0
    for E in [.162,.675,1.,2.64,3.8]:
        W=np.sqrt((MP+MB)**2+2*MB*E)
        # Fraction grid and random unit directions exercise the map only; not a physics density.
        for fraction in [1e-4,.1,.5,.9,.9999]:
            for _ in range(32):
                a=build_event(E_proton_LAB_MeV=E,pair_relative_MeV=float(fraction*(W-3*MA)),
                    primary_direction_CM=k.direction(rng),secondary_direction_pair_rest=k.direction(rng),
                    parent_J=2,parent_parity=-1,pair_J=2,pair_parity=1,primary_l=1,secondary_l=2)
                n+=1;c=a['checks'];four=max(four,c['max_four_momentum_residual_MeV'])
                mass=max(mass,c['max_relative_mass_shell_residual']);pair=max(pair,c['intermediate_invariant_mass_residual_MeV'])
                T=sum(v[0]-MA for v in a['alpha_four_vectors_LAB_MeV'])
                energy=max(energy,abs(T-(Q+E)))
                if len(samples)<3:samples.append(a)
    return dict(seed=20261029,rng='NumPy default_rng PCG64',events=n,input_class='NUMERICAL_VERIFICATION_ONLY',
        E_proton_LAB_MeV=[.162,.675,1.,2.64,3.8],
        pair_available_energy_fraction_grid=[1e-4,.1,.5,.9,.9999],
        maximum_four_momentum_residual_MeV=four,maximum_relative_mass_shell_residual=mass,
        maximum_intermediate_mass_residual_MeV=pair,maximum_LAB_kinetic_energy_sum_residual_MeV=energy,
        source_amplitude_tested=False,predicted_yield=None,calibrated_source=False,sample_events=samples)

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve earlier receipts')
    result=verification();a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'KINEMATICS.json').write_text(encoded(result))
    (a.out/'RECEIPT.json').write_text(encoded(dict(python=platform.python_version(),numpy=np.__version__,
        code_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['sequential.py','verify_sequential.py']},
        dependency_lock_sha256=hashlib.sha256((ROOT/'DEPENDENCY_LOCK.json').read_bytes()).hexdigest())))
    print(encoded({k:v for k,v in result.items() if k!='sample_events'}))

if __name__=='__main__':main()
