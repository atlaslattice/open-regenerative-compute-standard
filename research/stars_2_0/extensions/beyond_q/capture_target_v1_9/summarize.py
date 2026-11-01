"""Reference table and independent atom/molecule volume normalization."""
import json
import run as r
from dispatchcycle.physics import dt_events,FPY_S,T_KG_PER_ATOM

def main():
    liters=350000.;moles=liters/22.414
    ref=dict(STP='0C,1atm;22.414 L/mol',target_He3_STP_L=liters,He3_target_kg=moles*.0030160293201,
      T_atom_equivalent_target_kg=moles*.00301604928,T2_molecular_350kL_target_kg=2*moles*.00301604928,
      B_1100MW_burn_full_FPY_kg=dt_events(1100)*FPY_S*T_KG_PER_ATOM,
      B_burn_365_25day_clock_at_15_over_16_duty_kg=dt_events(1100)*FPY_S*T_KG_PER_ATOM*15/16)
    (r.OUT/'mass_reference.json').write_text(json.dumps(ref,indent=2)+'\n')
    rows=[x for x in r.paired.readcsv(r.OUT/'annual_dispatch.csv') if x['policy']=='captured350k_atom_equivalent' and float(x['B_gross_TBR_assumed'])==1 and int(x['year'])>0]
    r.write('reference_350k.csv',rows)
    print(json.dumps(ref,indent=2))
if __name__=='__main__':main()
