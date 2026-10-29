"""Relativistic three-alpha constant-matrix-element phase-space NULL model.
No Be8 reaction amplitude, resonance fit, Coulomb final-state factor or l=3 claim.
"""
import json,math
from pathlib import Path
import numpy as np

_s=json.loads((Path(__file__).parent/'MASS_SOURCE.json').read_text())
MP=_s['proton_MeV'];MA=_s['alpha_MeV']
MB=_s['B11_atomic_mass_u']*_s['atomic_mass_unit_MeV']-5*_s['electron_MeV']+sum(_s['B_electron_binding_components_eV'])*1e-6
Q=MP+MB-3*MA

def boost(v,beta):
    v=np.asarray(v,float);b=np.asarray(beta,float);b2=float(b@b)
    if not np.isfinite(v).all() or not np.isfinite(b).all() or b2>=1:raise ValueError('invalid boost')
    if b2==0:return v.copy()
    g=1/math.sqrt(1-b2);dot=v[1:]@b
    return np.r_[g*(v[0]+dot),v[1:]+(((g-1)*dot/b2)+g*v[0])*b]

def two_body_p(parent,a,b):
    if parent<a+b:raise ValueError('two-body threshold')
    return math.sqrt(max(0.,(parent-a-b)*(parent+a+b)*(parent-a+b)*(parent+a-b)))/(2*parent)

def direction(rng):
    z=rng.uniform(-1,1);phi=rng.uniform(0,2*math.pi);r=math.sqrt(max(0,1-z*z))
    return np.array([r*math.cos(phi),r*math.sin(phi),z])

def event(E_proton_LAB_MeV,rng):
    if not math.isfinite(E_proton_LAB_MeV) or E_proton_LAB_MeV<0:raise ValueError('invalid proton energy')
    Ep=MP+E_proton_LAB_MeV;pp=math.sqrt(E_proton_LAB_MeV*(E_proton_LAB_MeV+2*MP))
    initial=np.array([Ep+MB,0.,0.,pp]);W=math.sqrt((MP+MB)**2+2*MB*E_proton_LAB_MeV)
    low,high=2*MA,W-MA
    bound=two_body_p(W,low,MA)*two_body_p(high,MA,MA)
    for _ in range(100000):
        w=rng.uniform(low,high);p=two_body_p(W,w,MA);k=two_body_p(w,MA,MA)
        # Recursive invariant phase-space density in pair mass w is proportional to p*k.
        if rng.random()*bound<=p*k:break
    else:raise RuntimeError('phase-space rejection did not converge')
    axis=direction(rng);a3=np.r_[math.hypot(MA,p),p*axis];pair=np.r_[math.hypot(w,p),-p*axis]
    axis2=direction(rng);a1=np.r_[math.hypot(MA,k),k*axis2];a2=np.r_[math.hypot(MA,k),-k*axis2]
    pair_beta=pair[1:]/pair[0]
    cm=[boost(a1,pair_beta),boost(a2,pair_beta),a3]
    beta=initial[1:]/initial[0]
    lab=np.array([boost(v,beta) for v in cm])
    # Labels have no physical ordering in this identical-particle null model.
    return lab[rng.permutation(3)],initial

def verify(alphas,initial):
    a=np.asarray(alphas,float);initial=np.asarray(initial,float)
    if a.shape!=(3,4) or not np.isfinite(a).all() or initial.shape!=(4,) or not np.isfinite(initial).all() or initial[0]<=0:raise ValueError('finite initial and three alpha four-vectors required')
    delta=a.sum(axis=0)-initial
    shells=a[:,0]**2-np.sum(a[:,1:]**2,axis=1)-MA**2
    if np.max(np.abs(delta))>1e-8 or np.max(np.abs(shells))/MA**2>1e-12 or np.any(a[:,0]<MA):
        raise ValueError('four-momentum or alpha mass-shell failure')
    return dict(max_four_momentum_residual_MeV=float(np.max(np.abs(delta))),max_relative_mass_shell_residual=float(np.max(np.abs(shells))/MA**2))
