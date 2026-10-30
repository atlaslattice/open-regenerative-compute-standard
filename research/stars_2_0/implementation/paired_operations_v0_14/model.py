"""Evidence-tagged extrapolation and all-attempt acoustic reliability accounting.

No direct acoustic fusion multiplier, lab control, or ignition model.
"""
import math

def bounded(value, name):
    if isinstance(value,bool) or not isinstance(value,(float,int)) or not math.isfinite(value) or not 0<=value<=1:
        raise ValueError(name+' must be a probability/fraction in [0,1]')
    return value

def overlap_probability(sigma, half_window, bias=0.):
    """Centered/biased one-dimensional Gaussian physical-overlap scenario.

    Units must match. This is NOT a measured acoustic response or a detector cut.
    """
    if any(isinstance(x,bool) or not math.isfinite(x) for x in [sigma,half_window,bias]) or sigma<0 or half_window<=0:
        raise ValueError('finite sigma>=0, half_window>0 required')
    if sigma==0:return float(abs(bias)<=half_window)
    return .5*(math.erf((half_window-bias)/(math.sqrt(2)*sigma))-math.erf((-half_window-bias)/(math.sqrt(2)*sigma)))

def attempt_accounting(*,ready_probability,fire_given_ready,physical_success_given_fired,
                       failed_fired_energy_fraction=0.,attempt_rate_Hz=None,
                       success_energy_J=None,prep_wall_J=None,laser_wall_J_per_fired=None,
                       allocated_aux_wall_J=None,load_J_per_success=None,
                       load_J_per_failed_fired=None):
    """Probabilities are conditional stages, not assumed independent marginals.

    success_energy_J has a declared upstream boundary (e.g. fusion Q); never
    silently equate that energy to load electricity. Failures may still react.
    Preparation cost is per attempted preparation, including timeouts/aborts.
    Any laser energy consumed by misfires must be allocated upstream explicitly.
    """
    r=bounded(ready_probability,'ready');f=bounded(fire_given_ready,'fire');s=bounded(physical_success_given_fired,'success')
    bad=bounded(failed_fired_energy_fraction,'failed-fired relative energy')
    vals=[attempt_rate_Hz,success_energy_J,prep_wall_J,laser_wall_J_per_fired,allocated_aux_wall_J,load_J_per_success,load_J_per_failed_fired]
    if any(v is not None and (isinstance(v,bool) or not math.isfinite(v) or v<0) for v in vals):raise ValueError('nonnegative finite supplied quantities required')
    fired=r*f;good=fired*s;poor=fired*(1-s);not_fired=1-fired
    effective=fired*(s+(1-s)*bad)
    known_wall_subtotal=sum(v for v in [prep_wall_J,allocated_aux_wall_J] if v is not None)+(fired*laser_wall_J_per_fired if laser_wall_J_per_fired is not None else 0)
    wall=known_wall_subtotal if all(v is not None for v in [prep_wall_J,laser_wall_J_per_fired,allocated_aux_wall_J]) else None
    energy=None if success_energy_J is None else effective*success_energy_J
    load=None if load_J_per_success is None or load_J_per_failed_fired is None else good*load_J_per_success+poor*load_J_per_failed_fired
    return dict(ready_fraction=r,timeout_or_not_ready_fraction=1-r,
                no_fire_given_ready_fraction=r*(1-f),fired_fraction=fired,
                physical_success_per_attempt=good,unsuccessful_fired_per_attempt=poor,
                not_fired_per_attempt=not_fired,
                normalized_energy_per_attempt=effective,
                normalization='energy per physically successful pulse held fixed; unsuccessful fired pulse energy fraction supplied separately',
                energy_J_per_attempt=energy,
                energy_power_W=None if energy is None or attempt_rate_Hz is None else energy*attempt_rate_Hz,
                attempt_rate_Hz=attempt_rate_Hz,
                known_wall_subtotal_J_per_attempt=known_wall_subtotal,wall_J_per_attempt=wall,
                load_J_per_attempt=load,
                net_electrical_J_per_attempt=None if load is None or wall is None else load-wall,
                conditional_success_pulse_energy_J=success_energy_J,
                measured_nuclear_yield_multiplier=None)

def tail_models(energy_MeV, x0=2.25,y0=.639,x1=4.52,y1=.611):
    """Three analyst-selected two-point descending-branch models.

    y is source Langau location in um, NOT mean or full response. No model
    probability or uncertainty CI follows from fitting two anchors exactly.
    """
    if not math.isfinite(energy_MeV) or energy_MeV<x0 or energy_MeV>8:
        raise ValueError('This documented exploratory lane supports 2.25..8 MeV only')
    if not (0<x0<x1 and y0>0 and y1>0):raise ValueError('positive ordered anchors required')
    slope=(y1-y0)/(x1-x0)
    out=dict(linear=y1+slope*(energy_MeV-x1),
             exponential=y1*math.exp(math.log(y1/y0)/(x1-x0)*(energy_MeV-x1)),
             power_law=y1*(energy_MeV/x1)**(math.log(y1/y0)/math.log(x1/x0)))
    if any(v<=0 for v in out.values()):raise ValueError('nonpositive extrapolation rejected')
    return out

def full_detector_response(*args,**kwargs):
    raise ValueError('Location-only extrapolation: full response width/tails/efficiency unresolved')
