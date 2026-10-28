"""Necessary energy feasibility screen; no reaction kinetics or ignition solver."""
import math

def finite(x, low=0, high=None):
    if isinstance(x,bool) or not math.isfinite(x) or x<low or (high is not None and x>high):
        raise ValueError('invalid physical input')
    return x

def screen(mode, startup_wall_J, sustaining_wall_J, auxiliary_wall_J,
           fusion_J, alpha_self_heat_fraction, alpha_collection_fraction,
           conversion_efficiency, duration_s):
    if mode not in {'SINGLE_PASS_DRIVEN','CONTINUOUSLY_DRIVEN','STARTUP_THEN_BURN_HYPOTHESIS'}:
        raise ValueError('explicit operating mode required')
    for x in [startup_wall_J,sustaining_wall_J,auxiliary_wall_J,fusion_J,duration_s]:finite(x)
    if duration_s<=0:raise ValueError('positive declared cycle duration required')
    for x in [alpha_self_heat_fraction,alpha_collection_fraction,conversion_efficiency]:finite(x,high=1)
    if alpha_self_heat_fraction+alpha_collection_fraction>1:raise ValueError('alpha energy double counted')
    if mode=='STARTUP_THEN_BURN_HYPOTHESIS' and sustaining_wall_J!=0:
        raise ValueError('startup-only hypothesis cannot hide sustaining drive')
    incoming=startup_wall_J+sustaining_wall_J+auxiliary_wall_J
    fraction=alpha_collection_fraction*conversion_efficiency
    gross=fusion_J*fraction
    return {'mode':mode,'cycle_duration_s':duration_s,'fusion_energy_input_assumption_J':fusion_J,
            'startup_wall_J':startup_wall_J,'sustaining_wall_J':sustaining_wall_J,
            'auxiliary_wall_J':auxiliary_wall_J,'alpha_self_heat_J':fusion_J*alpha_self_heat_fraction,
            'alpha_unallocated_J':fusion_J*(1-alpha_self_heat_fraction-alpha_collection_fraction),
            'collector_loss_J':fusion_J*alpha_collection_fraction*(1-conversion_efficiency),
            'gross_electric_J':gross,'wall_input_J':incoming,'net_electric_J':gross-incoming,
            'cycle_average_net_W':(gross-incoming)/duration_s,
            'fusion_J_required_for_electric_breakeven':incoming/fraction if fraction>0 else None,
            'ignition_status':'NOT_EVALUATED_REQUIRES_TIME_DEPENDENT_PHYSICS',
            'physical_status':'SYNTHETIC_OR_EXTERNALLY_SUPPLIED_INPUTS_ONLY',
            'heat_credit_J':0,'stored_energy_change_status':'NOT_MODELED_CYCLE_RESET_REQUIRED'}
