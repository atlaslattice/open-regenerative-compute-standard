"""Formal source normalization from recorded particles; NOT a transport or reactor result."""
from pathlib import Path
import json,csv,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parent

def main():
 r=json.loads((ROOT/'outputs/runs/chain_on/analysis.json').read_text())
 qDT=17.58929696;qDDT=4.032653948;qDDN=3.26891111;MeVJ=1.602176634e-13
 births=r['DD_T_birth_atoms'];ddn=r['DD_n_birth_atoms'];burn=r['DT_burn_atoms'];t=r['elapsed_s']
 dd_q=MeVJ*(births*qDDT+ddn*qDDN)
 scale=20e6/(dd_q/t)
 B_rate_legacy=1130e6/(17.6*MeVJ);B_rate_warpx=1130e6/(qDT*MeVJ)
 totaln=ddn+burn
 source=dict(schema='beyond-q-kinetic-source-1.3',kind='ACTUAL_WARPX_SOURCE_SAMPLE_NOT_TRANSPORT',
  physical_validation=False,stationary_reactor_source_qualified=False,
  source_window_s=t,observed_DD_T_branch_fraction=births/(births+ddn),
  observed_secondary_burn_fraction=burn/births,reference_primary_DD_MW=20,reference_B_DT_MW=1130,
  formal_primary_DD_normalization_factor=scale,
  A_DD_neutrons_s=ddn/t*scale,A_secondary_DT_neutrons_s=burn/t*scale,
  formal_secondary_DT_power_MW=burn/t*scale*qDT*MeVJ/1e6,
  A_primary_T_birth_atoms_s=births/t*scale,A_unconsumed_T_atoms_s=(births-burn)/t*scale,
  B_DT_reactions_s_at_17_6_MeV=B_rate_legacy,B_DT_reactions_s_at_WarpX_Q=B_rate_warpx,
  B_convention_fractional_difference=B_rate_warpx/B_rate_legacy-1,
  normalization_warning='Scaling a2ps dense frozen-particle benchmark to20MW does not establish achievable power or steady-state confinement. No annual qualified surplus.',
  raw_particle_archive_sha256=hashlib.sha256((ROOT/'outputs/baseline_daughter_particles.npz').read_bytes()).hexdigest())
 with (ROOT/'outputs/weighted_spectra.csv').open() as f:rows=list(csv.DictReader(f))
 selected=[]
 for row in rows:
  if row['case']=='chain_on' and row['species'] in ('nDD','nDT'):
   n=float(row['physical_atoms']);selected.append(dict(species=row['species'],energy_low_eV=row['energy_low_eV'],energy_high_eV=row['energy_high_eV'],
      probability_per_all_source_neutrons=n/totaln,probability_given_source_type=n/(ddn if row['species']=='nDD' else burn)))
 with (ROOT/'outputs/normalized_A_source_spectrum.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(selected[0]));w.writeheader();w.writerows(selected)
 (ROOT/'outputs/source_interface.json').write_text(json.dumps(source,indent=2)+'\n')
 print(json.dumps(source,indent=2))
if __name__=='__main__':main()
