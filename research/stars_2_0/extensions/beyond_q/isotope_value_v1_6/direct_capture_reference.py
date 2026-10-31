"""Direct DD coproduct reference, no He3 decay credit or blanket breeding.
500MW is a reconstruction of the older scale, not a replacement power lock.
Volumes distinguish He3 atoms from molecular T2 at 0C/1atm (22.414 L/mol).
"""
import csv
import account as a
from fuelcycle.physics import dd_source,dt_events,FPY_S,AVOGADRO

def evaluate(label,power_a,power_b,availability,recovery):
    t=dd_source(power_a)['t_atoms_s']*FPY_S*availability*recovery
    he=dd_source(power_a)['n_atoms_s']*FPY_S*availability*recovery
    consumption=dt_events(power_b)*FPY_S*availability*a.T_KG_PER_ATOM
    return dict(case=label,A_primary_DD_MW=power_a,B_DT_MW=power_b,availability=availability,assumed_capture_fraction=recovery,
      direct_captured_He3_kg=he*a.HE3_KG_PER_ATOM,direct_captured_T_kg=t*a.T_KG_PER_ATOM,
      He3_STP_L=he/AVOGADRO*22.414,T_atom_equivalent_STP_L=t/AVOGADRO*22.414,T2_molecular_STP_L=t/AVOGADRO*22.414/2,
      B_T_burn_kg=consumption,direct_T_balance_before_internal_burn_delays_losses_reserves_kg=t*a.T_KG_PER_ATOM-consumption,
      decay_He3_credit_kg=0,blanket_T_credit_kg=0,
      status='POTENTIAL-DERIVED source screen; no secondary T/He3 burn, decay, processing delays or qualified plant operation')

def main():
    rows=[evaluate('older_500MW_scale_reconstruction',500,500,.85,.8),evaluate('current_1100MW_ideal_90percent_capture',1100,1100,1,.9)]
    a.write('direct_capture_reference.csv',rows)
    for r in rows:print(r)
if __name__=='__main__':main()
