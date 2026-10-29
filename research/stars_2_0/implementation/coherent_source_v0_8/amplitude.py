"""Explicit single-level coherent, Bose-symmetrized 2-minus candidate amplitude.
Literature-informed model variant, not a calibrated source or exact paper reproduction.
"""
import cmath,hashlib,importlib.util,json,math
from pathlib import Path
import numpy as np
from scipy.special import sph_harm_y,loggamma
from coulomb import waves,cg

ROOT=Path(__file__).resolve().parent
for row in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
    if hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch: '+row['file'])
spec=importlib.util.spec_from_file_location('physical_v05',ROOT.parent/'coupled_reference_v0_5/kinematics.py')
k=importlib.util.module_from_spec(spec);spec.loader.exec_module(k);MA=k.MA
ALPHA=7.2973525643e-3 # CODATA2022, NIST allascii; uncertainty1.1e-12, not propagated here.
HBARC=6.62607015e-34*299792458/(2*math.pi*1.602176634e-19*1e6)*1e15 # exact SI definitions

def check_config(c):
    required={'primary_radius_fm','secondary_radius_fm','pair_level_above_threshold_MeV','pair_reduced_width_squared_MeV',
        'boundary_convention','coulomb_phase_convention','basis_convention','run_class'}
    if set(c)!=required or c['run_class']!='EXPLORATORY_LITERATURE_MODEL':raise ValueError('explicit exploratory model configuration required')
    for name in ['primary_radius_fm','secondary_radius_fm','pair_level_above_threshold_MeV','pair_reduced_width_squared_MeV']:
        if isinstance(c[name],bool) or not isinstance(c[name],(int,float)) or not math.isfinite(c[name]) or c[name]<=0:raise ValueError('positive finite '+name+' required')
    if c['boundary_convention']!='S_AT_DECLARED_PAIR_LEVEL':raise ValueError('explicit boundary convention required')
    if c['coulomb_phase_convention'] not in ['RELATIVE_TO_SIGMA0','ABSOLUTE_LOG_GAMMA']:raise ValueError('explicit Coulomb phase convention required')
    if c['basis_convention']!='RAW_EQUATIONS_NOT_BRANCH_FRACTIONS':raise ValueError('basis coefficient convention unresolved; calibrated percentage transfer blocked')

def channel(E,mu,zproduct,l,radius,convention):
    if E<=0 or not math.isfinite(E):raise ValueError('open external channel required')
    momentum=math.sqrt(2*mu*E);rho=momentum*radius/HBARC;eta=zproduct*ALPHA*mu/momentum
    r=dict(waves(l,eta,rho));omega=sum(math.atan2(eta,n) for n in range(1,l+1))
    if convention=='ABSOLUTE_LOG_GAMMA':omega+=float(loggamma(1+1j*eta).imag)
    elif convention!='RELATIVE_TO_SIGMA0':raise ValueError('unknown phase convention')
    r.update(rho=rho,eta=eta,omega=omega)
    return r

def Y(l,m,v):
    length=float(np.linalg.norm(v))
    if not math.isfinite(length) or length<=0:raise ValueError('undefined angular direction')
    theta=math.acos(float(np.clip(v[2]/length,-1,1)));phi=math.atan2(v[1],v[0])%(2*math.pi)
    return complex(sph_harm_y(l,m,theta,phi))

def components(alphas_CM,c):
    """Return l1=1,3 amplitudes per m=-2..2 after coherent cyclic sum.
    Relativistic event geometry; nonrelativistic external R-matrix channel factors.
    """
    check_config(c);a=np.asarray(alphas_CM,float)
    if a.shape!=(3,4) or not np.isfinite(a).all():raise ValueError('three finite CM four-vectors required')
    initial=a.sum(axis=0);k.verify(a,initial)
    if np.max(np.abs(initial[1:]))>1e-8:raise ValueError('CM frame required')
    W=float(initial[0]);pole=c['pair_level_above_threshold_MeV'];g2=c['pair_reduced_width_squared_MeV'];conv=c['coulomb_phase_convention']
    B=channel(pole,MA/2,4,2,c['secondary_radius_fm'],conv)['S']
    parts=np.zeros((2,3,5),complex)
    for chart,(i,j,h) in enumerate([(0,1,2),(1,2,0),(2,0,1)]):
        pair=a[j]+a[h];pair_mass=math.sqrt(float(pair[0]**2-pair[1:]@pair[1:]));E23=pair_mass-2*MA
        E1=W-MA-pair_mass;mu=MA*pair_mass/(MA+pair_mass)
        sec=channel(E23,MA/2,4,2,c['secondary_radius_fm'],conv)
        denominator=pole-E23-(sec['S']-B+1j*sec['P'])*g2
        radial2=math.sqrt(g2*2*sec['P']/sec['rho'])*cmath.exp(1j*(sec['omega']-sec['phi']))/denominator
        daughter=k.boost(a[j],-pair[1:]/pair[0]);ys={m:Y(2,m,daughter[1:]) for m in range(-2,3)}
        for slot,l in enumerate([1,3]):
            prim=channel(E1,mu,8,l,c['primary_radius_fm'],conv)
            radial=math.sqrt(2*prim['P']/prim['rho'])*cmath.exp(1j*(prim['omega']-prim['phi']))*radial2*(1j)**(l+2)
            yp={m:Y(l,m,a[i,1:]) for m in range(-l,l+1)}
            for idx,M in enumerate(range(-2,3)):
                parts[slot,chart,idx]=radial*sum(cg(2,m,l,M-m,2,M)*yp.get(M-m,0)*ys[m] for m in range(-2,3))
    return parts.sum(axis=1),parts

def intensity(amplitudes,*,mix_coefficient,relative_phase_radians,coherent):
    a=np.asarray(amplitudes,complex)
    if a.shape!=(2,5) or not np.isfinite(a).all() or isinstance(mix_coefficient,bool) or not math.isfinite(mix_coefficient) or not 0<=mix_coefficient<=1 or not math.isfinite(relative_phase_radians) or not isinstance(coherent,bool):
        raise ValueError('finite explicit amplitude mixture required')
    if coherent:
        combined=math.sqrt(mix_coefficient)*a[0]+math.sqrt(1-mix_coefficient)*cmath.exp(1j*relative_phase_radians)*a[1]
        return float(np.vdot(combined,combined).real/5)
    return float((mix_coefficient*np.vdot(a[0],a[0]).real+(1-mix_coefficient)*np.vdot(a[1],a[1]).real)/5)
