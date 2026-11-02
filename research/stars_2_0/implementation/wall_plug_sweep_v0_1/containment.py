"""Engineering energy bookkeeping functions; hardware parameters are supplied.
No inference of confinement quality, stability, or actual coil geometry.
"""
import math

def positive(v,zero=False):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or (v<0 if zero else v<=0): raise ValueError('invalid input')
    return v

def pulsed_coil(L_H,I_A,R_ohm,on_s,recovered_field_fraction,supply_efficiency=1.):
    """Rectangular-current approximation, zero field between pulses.
    Startup field inventory is not charged repeatedly as steady-state power.
    Charging/discharging losses use the unrecovered PEAK magnetic inventory;
    ohmic current integral is approximated by I**2*R*on_s.
    """
    positive(L_H);positive(I_A,True);positive(R_ohm,True);positive(on_s,True)
    positive(recovered_field_fraction,True);positive(supply_efficiency)
    if not 0<=recovered_field_fraction<=1 or not 0<supply_efficiency<=1: raise ValueError('fraction')
    U=.5*L_H*I_A**2;ohmic=I_A**2*R_ohm*on_s
    return {'peak_field_inventory_J':U,'resistive_dissipation_J':ohmic,'electric_J_per_pulse':((1-recovered_field_fraction)*U+ohmic)/supply_efficiency}

def steady_coil(L_H,I_A,R_ohm,cryo_and_support_W,supply_efficiency=1.):
    positive(L_H);positive(I_A,True);positive(R_ohm,True);positive(cryo_and_support_W,True)
    positive(supply_efficiency)
    if not 0<supply_efficiency<=1: raise ValueError('fraction')
    return {'startup_field_inventory_J':.5*L_H*I_A**2,'steady_wall_W':I_A**2*R_ohm/supply_efficiency+cryo_and_support_W}
