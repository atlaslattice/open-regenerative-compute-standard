"""Finite measured-domain CSDA interval transport in atomic areal density.

The curve is a digitized cold B10-enriched measurement; material transfer is forbidden.
No full range to zero, straggling, scattering or deposited-heat claim.
"""
import bisect
import hashlib
import json
import math
from pathlib import Path

MATERIAL='OVERLEY_COLD_B10_ENRICHED_95.96_PERCENT'


def load_curve(path):
    lock=json.loads((Path(__file__).parent/'CURVE_LOCK.json').read_text())
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=lock['curve_sha256']:
        raise ValueError('curve identity mismatch; add a separately qualified version')
    curve=json.loads(raw);validate(curve['points'])
    return curve


def validate(points):
    if len(points)<2:raise ValueError('at least two points required')
    e=[p['E_proton_LAB_MeV'] for p in points]
    s=[p['epsilon_eV_cm2_atom'] for p in points]
    if not all(math.isfinite(v) and v>0 for v in e+s) or any(b<=a for a,b in zip(e,e[1:])):
        raise ValueError('invalid stopping grid')
    return e,s


def atom_column_between(points,low_MeV,high_MeV):
    """Integral dE / epsilon(E); epsilon piecewise linear, exact per segment."""
    e,s=validate(points)
    if not all(math.isfinite(v) for v in [low_MeV,high_MeV]) or not e[0]<=low_MeV<=high_MeV<=e[-1]:
        raise ValueError('outside measured domain')
    cuts=[low_MeV]+[v for v in e if low_MeV<v<high_MeV]+[high_MeV]
    result=0.
    for a,b in zip(cuts,cuts[1:]):
        if a==b:continue
        i=min(bisect.bisect_right(e,(a+b)/2)-1,len(e)-2)
        slope=(s[i+1]-s[i])/(e[i+1]-e[i])
        sa=s[i]+slope*(a-e[i]);delta=slope*(b-a)
        # log1p form is stable for small slope; no arbitrary numerical zero cutoff.
        result += (b-a)/sa if slope==0 else math.log1p(delta/sa)/slope
    return result*1e6


def transmit(points,*,E_in_LAB_MeV,atoms_cm2,material):
    if material!=MATERIAL:raise ValueError('material/isotope transfer requires a separate qualified model')
    if isinstance(atoms_cm2,bool) or not isinstance(atoms_cm2,(int,float)) or not math.isfinite(atoms_cm2) or atoms_cm2<0:
        raise ValueError('invalid areal atom column')
    e,_=validate(points)
    capacity=atom_column_between(points,e[0],E_in_LAB_MeV)
    if atoms_cm2>capacity:
        return dict(status='LOW_ENERGY_DATA_BOUNDARY_REACHED',E_out_LAB_MeV=None,
            boundary_energy_MeV=e[0],covered_atoms_cm2=capacity,unmodeled_atoms_cm2=atoms_cm2-capacity,
            stopped=None,stopped_status='UNKNOWN_NOT_ZERO_ENERGY')
    if atoms_cm2==0:out=E_in_LAB_MeV
    else:
        lo,hi=e[0],E_in_LAB_MeV
        for _ in range(90):
            mid=(lo+hi)/2
            if atom_column_between(points,mid,E_in_LAB_MeV)>atoms_cm2:lo=mid
            else:hi=mid
        out=(lo+hi)/2
    return dict(status='WITHIN_SUPPLIED_CURVE_DOMAIN_CSDA_MODEL',E_in_LAB_MeV=E_in_LAB_MeV,
        E_out_LAB_MeV=out,primary_energy_loss_MeV=E_in_LAB_MeV-out,
        atoms_cm2=atoms_cm2,material=material,
        qualification='conditional on supplied stopping curve; no independent transmission validation',
        interpolation='piecewise linear atomic stopping versus LAB proton energy')


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--curve',type=Path,required=True);p.add_argument('--energy',type=float,required=True);p.add_argument('--atoms-cm2',type=float,required=True);p.add_argument('--material',required=True);a=p.parse_args()
    points=load_curve(a.curve)['points']
    print(json.dumps(transmit(points,E_in_LAB_MeV=a.energy,atoms_cm2=a.atoms_cm2,material=a.material),indent=2,allow_nan=False))
