"""Physical-mass sequential kinematic map. No default decay probability law.

The chosen alpha/pair partition is a coordinate chart, not an observable history.
An amplitude model must sum identical-particle alternatives before squaring.
"""
import hashlib,importlib.util,json,math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
for row in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
    if hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()!=row['sha256']:
        raise ValueError('dependency hash mismatch: '+row['file'])
_spec=importlib.util.spec_from_file_location('physical_kinematics_v05',ROOT.parent/'coupled_reference_v0_5/kinematics.py')
k=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(k)
MP,MB,MA,Q=k.MP,k.MB,k.MA,k.Q

def allowed_channel(*,parent_J,parent_parity,pair_J,pair_parity,primary_l,secondary_l):
    ints=[parent_J,pair_J,primary_l,secondary_l]
    if any(isinstance(x,bool) or not isinstance(x,int) or x<0 for x in ints):
        raise ValueError('nonnegative integer angular momenta required')
    if parent_parity not in (-1,1) or pair_parity not in (-1,1) or isinstance(parent_parity,bool) or isinstance(pair_parity,bool):
        raise ValueError('parities must be +/-1')
    # Alpha has spin/parity 0+. Two identical spin-zero alphas require even l2.
    return (abs(pair_J-primary_l)<=parent_J<=pair_J+primary_l
        and parent_parity==pair_parity*(-1)**primary_l
        and secondary_l==pair_J and secondary_l%2==0
        and pair_parity==(-1)**secondary_l)

def unit(v):
    a=np.asarray(v,float)
    if a.shape!=(3,) or not np.isfinite(a).all() or not math.isclose(float(a@a),1.,rel_tol=0,abs_tol=1e-12):
        raise ValueError('explicit finite unit direction required; no silent normalization')
    return a

def build_event(*,E_proton_LAB_MeV,pair_relative_MeV,primary_direction_CM,secondary_direction_pair_rest,
        parent_J,parent_parity,pair_J,pair_parity,primary_l,secondary_l):
    """Map a fully specified conditional state into three physical LAB four-vectors.

    pair_relative_MeV means invariant(pair)-2*m_alpha, NOT Be8 excitation energy.
    Rest-frame directions use rotationless boost axes parallel to CM Cartesian axes.
    No branching fraction, resonance width, angular density, rate or weight is implied.
    """
    channel=dict(parent_J=parent_J,parent_parity=parent_parity,pair_J=pair_J,pair_parity=pair_parity,
        primary_l=primary_l,secondary_l=secondary_l)
    if not allowed_channel(**channel):raise ValueError('angular momentum/parity/Bose-pair forbidden channel')
    E=E_proton_LAB_MeV;r=pair_relative_MeV
    if isinstance(E,bool) or not isinstance(E,(int,float)) or not math.isfinite(E) or E<0:
        raise ValueError('finite nonnegative LAB proton kinetic energy required')
    if isinstance(r,bool) or not isinstance(r,(int,float)) or not math.isfinite(r) or r<=0:
        raise ValueError('positive finite pair relative energy required')
    u=unit(primary_direction_CM);v=unit(secondary_direction_pair_rest)
    initial=np.array([MP+MB+E,0.,0.,math.sqrt(E*(E+2*MP))])
    W=math.sqrt((MP+MB)**2+2*MB*E);pair_mass=2*MA+r
    if not pair_mass<W-MA:raise ValueError('no open sequential two-body phase space')
    p=k.two_body_p(W,MA,pair_mass);q=k.two_body_p(pair_mass,MA,MA)
    primary=np.r_[math.hypot(MA,p),p*u]
    pair=np.r_[math.hypot(pair_mass,p),-p*u]
    daughters=[np.r_[math.hypot(MA,q),sign*q*v] for sign in [1,-1]]
    cm=np.array([primary,*[k.boost(a,pair[1:]/pair[0]) for a in daughters]])
    beta=initial[1:]/initial[0];lab=np.array([k.boost(a,beta) for a in cm])
    checks=k.verify(lab,initial)
    pair_back=cm[1:].sum(axis=0);mass_back=math.sqrt(pair_back[0]**2-float(pair_back[1:]@pair_back[1:]))
    checks['intermediate_invariant_mass_residual_MeV']=abs(mass_back-pair_mass)
    if checks['intermediate_invariant_mass_residual_MeV']>1e-8:raise ValueError('pair mass failure')
    return dict(status='CONDITIONAL_KINEMATICS_ONLY',source_distribution_calibrated=False,
        event_probability=None,event_weight=None,E_proton_LAB_MeV=E,pair_relative_MeV=r,channel=channel,
        initial_four_vector_LAB_MeV=initial.tolist(),alpha_four_vectors_LAB_MeV=lab.tolist(),
        alpha_four_vectors_CM_MeV=cm.tolist(),pair_four_vector_CM_MeV=pair.tolist(),
        primary_direction_CM=u.tolist(),secondary_direction_pair_rest=v.tolist(),
        mass_derived_Q_MeV=Q,compound_invariant_mass_MeV=W,checks=checks,
        identical_particle_amplitude_symmetrization='REQUIRED_IN_SOURCE_MODEL; NOT_PERFORMED_BY_COORDINATE_MAP')

def require_calibrated_source():
    raise ValueError('No calibrated amplitude supplied: require sourced line shape, coherent l1/l3 mixture, identical-alpha symmetrization, population/alignment, uncertainty and response validation')
