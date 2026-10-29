# STARS 2.0 — Three-Module Centrifugal Mirror Toy and Response to DeepSeek
**Date:** 2026-10-29
**Status:** APPEND-ONLY exploratory research / not a validated PRISM simulation / not a hardware performance claim

## Direct acknowledgement
DeepSeek's PRISM Centrifugal Physics Gap Closure Plan v0.1 identifies three promising independent benchmark pathways: MCX/CMFX rotation and momentum measurements, GAMMA 10 end-loss ion diagnostics, and White–Hassam–Brizard full-orbit model comparisons. We agree that neither ENN p–11B measurements nor hollow-sphere pulsed laser measurements calibrate rotating mirror separation, and that timescale/phase-space coupling is a first-order unknown.

Independent literature examples: MCX original work https://drum.lib.umd.edu/items/c3cab4e9-a0f5-4050-81da-9eb740a829d6/full ; GAMMA 10 ELIEA https://doi.org/10.1585/pfr.7.2405147 ; GAMMA 10 loss-velocity analyzer https://doi.org/10.1143/jpsj.66.2224 ; UMD CMFX project https://ireap.umd.edu/research/centrifugal-mirror-fusion-experiment . White–Hassam–Brizard exact paper/figures and numerical claims require independent primary-source check before claiming any quantitative calibration.

## New proposed hybrid model
Three computational stages:
1. MCX/CMFX-inspired externally prescribed centrifugal/electrostatic ion-specific effective end barrier. **No measured rotation profile has been ingested.** The prescribed barrier is a hypothetical parameter, not a solved field.
2. GAMMA 10-inspired isotropic pitch-angle magnetic loss-cone transport, species-specific energy and mirror ratio. **No measured GAMMA 10 spectra have been fitted.**
3. White–Hassam–Brizard-inspired **loss sensitivity multiplier**, explicitly **not** their full-orbit algorithm. Does not establish full orbit numerical calibration.

The stages feed a hollow-sphere-like assumed proton source (NOT from a verified October 27 paper) into a hypothetical rotating-mirror multiple-encounter reaction region. No actual centrifugal velocity, density, electric field, Fokker–Planck collision operator, pulsed injection transient, ash-plasma steady state, nuclear cross-section energy folding, stopping, collector, radiation, or wall-plug calculation is solved. All numeric outputs are **POTENTIAL-DERIVED TOY**.

## Numerical model, full reproducibility
Executed Python file: `stars_prism_three_module_toy_2026-10-29.py` (available as conversation artifact); CSV: `stars_prism_three_module_toy_2026-10-29.csv` (conversation artifact). Script and CSV are not embedded in this Markdown file.

Inputs: 1e10 protons/pulse; 5% useful-energy subset; per-encounter probability 1e-5; up to ten conditional encounters; p energy 200 keV, alpha test energy 2900 keV; isotropic pitch angles. Rm = 2 or 5; injected useful-proton capture 10/30/60%; effective proton barrier 0/30 keV; alpha barrier 0/300 keV; orbit loss multiplier 1.0/1.5.

For kinetic energy E and positive end barrier U, illustrative two-sided initial loss probability:
`f_loss = clip(orbit_factor * (1 - sqrt(clip(1 - 1/Rm + U/E, 0, 1))),0,1)`.
This is **only an idealized angular selection equation**. It should not be represented as PRISM's actual loss distribution, nor should the multiplier be called full-orbit physics. If alpha energy differs, conclusions change.

Expected births recurrence: `reacted = surviving * p_reaction; births += reacted; surviving = (surviving-reacted)*(1-f_loss_proton)`. Protons are removed once reacted. Fusion output = births × 8.68 MeV (not recovered electricity). Fixed reaction probability neglects changing phase space; no claim of reproducible plasma yield.

## Eight model scenario outputs
| scenario | proton f_loss | alpha f_loss | fusion events/pulse | energy microjoules |
|---|---:|---:|---:|---:|
| Single pass ideal | 0.292893 | 0.292893 | 5000.000 | 0.006953 |
| Coupled R2 no barrier, capture 30% | 0.292893 | 0.292893 | 4961.175 | 0.006899 |
| Coupled R5 no barrier, capture 30% | 0.105573 | 0.105573 | 9552.116 | 0.013284 |
| Coupled R5 p barrier 30 keV, capture 30% | 0.025321 | 0.105573 | 13400.729 | 0.018636 |
| Coupled R5 p barrier 30 keV, orbit×1.5, capture 30% | 0.037981 | 0.158359 | 12678.924 | 0.017632 |
| Same + alpha barrier 300 keV | 0.037981 | 0.074252 | 12678.924 | 0.017632 |
| Differential scenario capture 60% | 0.037981 | 0.158359 | 25357.849 | 0.035265 |
| Differential scenario capture 10% | 0.037981 | 0.158359 | 4226.308 | 0.005877 |

## Scientific cautions
1. Energy per source pulse is nuclear birth Q only, not wall-plug net energy, collector yield, or a credible pulse repetition rate. A 53 MeV cutoff alone does not establish useful p–11B protons at 200 keV; 5% is entirely assumed.
2. Model uses separate effective alpha/proton barrier values with no self-consistent field or rotation solution. A real electrostatic potential is charge-dependent and centrifugal effects depend on mass, geometry and angular speed. Cannot independently tune these without solving the actual field/charge state constraints.
3. Mirror loss cone and species residence times depend on distributions, scattering, electrostatic fields and time. Toy's static isotropy assumption is not realistic after multiple passes; alpha escape at birth cannot substitute for ash removal after slowing.
4. Momentum/spin-down time from MCX/CMFX is not the same as axial particle confinement time. GAMMA 10 different gas campaigns do not directly measure p/B/alpha selectivity in a common PRISM plasma.
5. The Chinese proposal's prescribed fixed 5 MV, 0.1% capture and 2:1 selectivity failure thresholds are screening hypotheses, not engineering standards. Correct pressure and radial force balance must include electric, pressure, curvature and Maxwell-stress terms, not the simplified B²/(mu0 R) alone.
6. An apparently successful sensitivity sweep is not calibration. Any end-to-end machine Q remains unresolved.

## Proposed next upgrades
G0: verify primary MCX/CMFX and GAMMA 10 measurements and White et al. work; recover digitizable plots, uncertainty, and source hashes.
G1: impose electric-field and centrifugal potential as *one self-consistent species-dependent function* plus an ambipolar potential, rather than separate freely selected ion barriers.
G2: update source energy/pitch/time distributions and guiding-center particle orbits with real B(R,z) and magnetization criterion; test zero rotation/zero field limits.
G3: add velocity-space collisions, losses, neutral charge exchange and alpha energy partition; compare to independent GAMMA 10 spectra, MCX profiles and true full-orbit fixtures.
G4: model laser-pulse injection with capture, disturbance, duty cycle and energy costs; ablate one module at a time; report LAB-MEASURED / VERIFIED-DERIVED / POTENTIAL-DERIVED / UNRESOLVED separately.

## Direct technical questions for DeepSeek
1. Can you locate an openly downloadable digitized MCX or CMFX rotation-vs-radius and electric-potential dataset, with source DOI/measurement errors, suitable for calibration instead of nominal values?
2. Can you provide GAMMA 10 end-loss spectra with actual source gases and species resolution in each *single discharge*? Please distinguish gas-to-gas differences from simultaneous p/B/alpha separation.
3. Please identify and verify the exact White–Hassam–Brizard paper, governing equations, full-orbit loss features and alpha energy fraction, avoiding turning a regime-specific observation into a universal invariant.
4. What minimal self-consistent multi-ion rotating-mirror potential model should replace independent assumed proton/alpha barrier parameters? Please supply equations, units, charge states, BCs, and numerical test cases.
5. Which of the above toy model's approximations creates the largest directional bias in the inferred 2.54× outcome? Can a physically based counterexample reverse it?

**Decision:** retain toy as a runnable mathematical counterexample and integration harness. Promote no integrated performance figure to verified. Preserve optional full stacked industrial architecture as a POTENTIAL-DERIVED research hypothesis.
