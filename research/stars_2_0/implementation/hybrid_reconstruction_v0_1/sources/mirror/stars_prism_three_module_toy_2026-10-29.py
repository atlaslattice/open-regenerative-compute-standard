"""STARS PRISM centrifugal three-module toy, 2026-10-29.
All numerical inputs are illustrative; this is not a plasma solver nor PRISM calibration.
Modules: rotation barrier (potential energy), loss-cone transport, full-orbit correction.
"""
import numpy as np
import pandas as pd

def escape_probability(Rm, E_keV, barrier_keV, orbit_multiplier=1.0):
    # Isotropic pitch angles. Loss-cone threshold after a positive end barrier:
    # E_parallel >= E*(1-1/Rm)+barrier; for loss-cone directional cosine mu:
    # E*mu^2 >= E*(1-1/Rm)+barrier
    # A mirror-only isotropic two-ended loss-cone fraction: 1-sqrt(1-1/Rm).
    threshold=1-1/Rm+barrier_keV/E_keV
    nominal=1-np.sqrt(np.clip(threshold,0,1))
    return np.clip(nominal*orbit_multiplier,0,1)

def case(label, Rm, barrier_p_keV, barrier_alpha_keV, capture, orbit=1.0, attempts=10, p_reaction=1e-5):
    source=1e10; useful=0.05
    admitted=source*useful*capture
    # Deliberately one-use protons, independent passes conditional on prior survival.
    escape_p=escape_probability(Rm, 200, barrier_p_keV,orbit)
    escape_a=escape_probability(Rm, 2900, barrier_alpha_keV,orbit)
    surviving=admitted; births=0
    for _ in range(attempts):
        reactions=surviving*p_reaction
        births+=reactions
        surviving=(surviving-reactions)*(1-escape_p)
    return dict(scenario=label,mirror_ratio=Rm,proton_barrier_keV=barrier_p_keV,
      alpha_barrier_keV=barrier_alpha_keV,capture_assumed=capture,orbit_loss_multiplier=orbit,
      proton_escape_fraction=escape_p,alpha_escape_fraction=escape_a,
      alpha_to_proton_escape_ratio=(escape_a/escape_p if escape_p else np.nan),
      fusion_events_per_pulse=round(births,3),
      fusion_energy_uJ=births*8.68*1.602176634e-13*1e6,
      evidence="POTENTIAL_DERIVED_TOY_NOT_CALIBRATED")

cases=[
case("single_pass_no_mirror",2,0,0,1,1,1),
case("coupled_R2_no_barrier",2,0,0,.3,1),
case("coupled_R5_no_barrier",5,0,0,.3,1),
case("coupled_R5_p_barrier",5,30,0,.3,1),
case("coupled_R5_differential_p30_a0",5,30,0,.3,1.5),
case("coupled_R5_both_barrier",5,30,300,.3,1.5),
case("coupled_R5_differential_high_capture",5,30,0,.6,1.5),
case("coupled_R5_differential_low_capture",5,30,0,.1,1.5)]
df=pd.DataFrame(cases)
df.to_csv("/mnt/data/stars_prism_three_module_toy_2026-10-29.csv",index=False)
print(df[["scenario","proton_escape_fraction","alpha_escape_fraction","fusion_events_per_pulse","fusion_energy_uJ"]].to_string(index=False))
