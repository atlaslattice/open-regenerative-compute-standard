"""Explicit joint source/SI-field admission; no missing source reconstruction."""
import math
from scipy.constants import c,m_p,e


def finite(x,name,positive=False):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError(name+' must be finite')
    if positive and x<=0:raise ValueError(name+' must be positive')
    return x


def admit(source,field):
    if source.get('jointness')!='JOINT_RECORDS':raise ValueError('marginal spectra do not determine joint phase space')
    if source.get('species')!='proton' or source.get('frame')!='LAB':raise ValueError('explicit LAB proton source required')
    if source.get('units')!={'position':'m','time':'s','kinetic_energy':'MeV','weight':'physical_particles'}:raise ValueError('canonical source units required')
    if source.get('normalization')!='ABSOLUTE_PHYSICAL_PARTICLES_PER_SNAPSHOT':raise ValueError('relative spectrum does not specify particle count')
    ev=source.get('evidence',{})
    if ev.get('kind') not in ['MEASURED_JOINT','SOURCE_REPRODUCED_JOINT','DERIVED_JOINT','NUMERICAL_VERIFICATION']:raise ValueError('explicit evidence kind required')
    if not ev.get('source_ref') or not ev.get('input_sha256'):raise ValueError('source provenance required')
    if field.get('grid_unit_SI')!=1 or field.get('component_unit_SI')!=[1,1,1] or field.get('axis_labels')!=['x','y','z']:raise ValueError('canonical SI XYZ field required; metadata-only conversion rejected')
    if not field.get('map_sha256') or not field.get('source_ref'):raise ValueError('field provenance required')
    lo,hi=field['domain_lo_m'],field['domain_hi_m']
    if len(lo)!=3 or len(hi)!=3:raise ValueError('3D bounds required')
    for a,b in zip(lo,hi):
        finite(a,'lower bound');finite(b,'upper bound')
        if b<=a:raise ValueError('invalid bounds')
    records=source.get('records')
    if records is None:raise ValueError('missing source is not known zero')
    if not isinstance(records,list):raise ValueError('records must be a list')
    snapshot=finite(source['snapshot_time_s'],'snapshot time')
    if snapshot!=0 and field.get('time_dependence')!='STATIC':raise ValueError('time-dependent field needs an explicit clock-preserving restart adapter')
    out=[];ids=set()
    for r in records:
        rid=r['id']
        if not isinstance(rid,str) or not rid or rid in ids:raise ValueError('unique source record IDs required')
        ids.add(rid)
        pos=r['position_m'];direction=r['unit_direction_LAB']
        if len(pos)!=3 or len(direction)!=3:raise ValueError('3D vectors required')
        for q in pos:finite(q,'position')
        for q in direction:finite(q,'direction')
        if abs(math.fsum(q*q for q in direction)-1)>1e-10:raise ValueError('direction must be unit norm, not normalized silently')
        if any(x<a or x>b for x,a,b in zip(pos,lo,hi)):raise ValueError('source outside field/geometry domain')
        time=finite(r['time_s'],'record time')
        if time!=snapshot:raise ValueError('mixed-time injection is not a snapshot')
        weight=finite(r['weight'],'weight');energy=finite(r['kinetic_MeV'],'energy')
        if weight<0 or energy<0:raise ValueError('negative source weight/energy')
        k=energy*1e6*e;delta=k/(m_p*c*c);unorm=math.sqrt(delta*(delta+2))
        out.append(dict(id=rid,weight=weight,position_m=list(pos),source_time_s=time,kinetic_MeV=energy,normalized_u=[unorm*d for d in direction],momentum_kg_m_s=[m_p*c*unorm*d for d in direction]))
    return dict(status='CONDITIONAL_SNAPSHOT_ADMITTED_NOT_APPARATUS_CALIBRATION',evidence=ev,field_source=field['source_ref'],field_sha256=field['map_sha256'],simulation_clock_zero_corresponds_to_source_time_s=snapshot,physical_proton_weight=math.fsum(r['weight'] for r in out),weighted_kinetic_energy_J=math.fsum(r['weight']*r['kinetic_MeV']*1e6*e for r in out),packets=out)


def input_fragment(admitted):
    rows=admitted['packets']
    if not rows:return '# KNOWN_ZERO_SOURCE; caller must retain this attempted shot\n'
    lines=['# Conditional snapshot only; reset clock mapping recorded in admission receipt.','proton.injection_style = MultipleParticles']
    for j,axis in enumerate('xyz'):
        lines.append('proton.multiple_particles_pos_'+axis+' = '+' '.join(format(r['position_m'][j],'.17g') for r in rows))
        lines.append('proton.multiple_particles_u'+axis+' = '+' '.join(format(r['normalized_u'][j],'.17g') for r in rows))
    lines.append('proton.multiple_particles_weight = '+' '.join(format(r['weight'],'.17g') for r in rows))
    return '\n'.join(lines)+'\n'
