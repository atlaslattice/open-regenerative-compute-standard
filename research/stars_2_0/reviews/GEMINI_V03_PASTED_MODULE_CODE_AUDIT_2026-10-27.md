# STARS 2.0 — Gemini Argon WP-B v0.3 pasted-module audit
**2026-10-27 | Atlas Lattice / ORCS | Independent static and numerical spot audit**
**Source:** User-supplied inline Python: `stars_2_0_wp_b_v03_ofat_and_interface.py` (text in originating conversation). This audit DOES NOT claim that code or its unseen CSVs have been installed, run end to end, or retrieved from the claimed artifact bundle.

## Important response to project lead: evaluate acoustics by useful output quality
The 15 mJ per-shot actuator cost is not itself evidence acoustic shaping is worthless: quality, proton shot repeatability, diagnostic acceptance, facility uptime, downstream capture, reduced beam spill, target reliability and per-valid-shot costs can justify expenditures at a **research or value-added product** boundary. Evaluate delivered good shots, variance, sample throughput, lost shots, plant uptime and cost per qualified experiment. For an **eventual net-electric energy product**, cost still belongs in the whole-system energy ledger. A 0.1083 μJ alpha gain against 15 mJ acoustic draw is ~1/138,504 in same-shot additional escape energy. Those two statements coexist.

## What source code actually contains
- `icru49_proton_stopping_bn`: smooth formula composed of two joined fitted electronic-stopping branches and reduced-ZBL-like nuclear term; v01 versus v02 heuristic modes.
- `icru49_alpha_stopping_bn`: similar smooth parameterization, with its own parameters.
- `SP_FINE`, `SA_FINE` and `RP_FINE_UM`, `RA_FINE_UM`: integrated ranges on a half-keV grid, using scipy cumulative_trapezoid.
- `sigma_pb11_configurable`: empirical three-Lorentzian plus S-factor and damping continuum curve, selected energy frames and a `1+0.48 P²` spin multipler.
- `evaluate_g3_collector_portfolio`: four *assumed* capture/conversion/auxiliary efficiencies on a 100 mJ helium beam, and scaled gross electrical energy against **rear-only** catcher exit energy.

**Not present in pasted script:** executable multi-thickness OFAT stages; stochastic correlated three-body decay and individual alpha momenta; CM-to-laboratory transform; detector response/particle counting; four-arm acoustic Monte Carlo; shot energy ledger; generation of the three claimed CSVs; main calls other than `print("WP-B v0.3 module loaded successfully.")`. Thus the supplied text is a **partial module** and *cannot reproduce Gemini's round-four output tables*, nor independently verify claims of event conservation below 1e-9.

## Independent numerical spot-check, evaluating exactly the supplied formulas
Values from independent Python evaluation of copied function definitions (not original unseen binaries):
| Quantity | Computed | Gemini claim |
|---|---:|---:|
| S_p(75 keV), keV/µm | 94.0788 | 94.08 |
| S_p(1000 keV), keV/µm | 35.8409 | 35.84 |
| S_alpha(2900 keV), keV/µm | 245.1658 | 245.2 |
| CSDA R_alpha(2461 keV), µm | 7.3594 | ~7.34 |
| CSDA R_alpha(2900 keV), µm | 9.0868 | ~9.07 |
| CSDA R_alpha(3760 keV), µm | 12.8294 | ~12.81 |
| CSDA R_p(1000 keV), µm | 19.4172 | ~19.36 |
| E_CM(675 keV lab), keV | 618.406 | ~618.41 |

These show good **internal numerical consistency**, not independent stopping/reference-data validation. Values originate from in-code parametric functions, not actual ingested SRIM, ICRU or EXFOR records; naming the functions `icru49_` does not make them an authoritative stopping table. The alpha range inverse would be numerically conditional on that parametrization, not 'exact transport' (straggling, scattering and substrate effects remain).

## Core cross-section and model limitations
- Three resonance widths/amplitudes and `exp(-E_CM / 290)` damping are **hard-coded phenomenological**; no EXFOR ingestion, fitted measurement source list, covariance or out-of-sample evaluation.
- `spin_polarization_P` is a direct assumed `1+0.48 P²` multiplier; no measured polarization at shot time or spin-dependent cross sections.
- Energy conversion uses a fixed approx mass convention `M_B11_U=11.006562`, with `M_PROTON_U` proton nuclear mass; document atom-versus-nucleus convention if seeking sub-keV precision.
- `N_B11_CM3=(2.10/25.016)*N_A*0.99`: BN mass and 99% enrichment assumptions, not characterized film facts.
- `E_FINE_KEV` starts at zero but stopping functions clamp energy to 1 keV; this creates a finite numerical low-energy convention, not measured stopping near zero.
- No actual alpha CM-to-LAB boost is computed in pasted source; Gemini's claimed reversal of rear/front output is currently unverified by this module.
- The G3 evaluator receives rear-only `E_alpha_exit_rear_J` and computes **gross** catcher load, not local-net shot recovery. Fixed 4.2 mJ local auxiliary for C1 must not be silently ignored when evaluating a ~0.173 µJ energy plume; any actual power scaling, duty-cycle amortization or shared plant loads require an explicit physical model. Gross and local net values for a 100 mJ independent alpha benchmark do not imply feasibility on a sub-µJ catcher source.
- `scipy.integrate.cumulative_trapezoid` requires scipy, despite earlier pipeline being standard-library only: module needs a reproducible dependency environment.

## Suggested separate value-creation metric for acoustic control
For a research facility or downstream product `cost_per_accepted_shot = [energy_price × (laser+actuator+aux) + target_materials + staff + wear + downtime] / accepted_shots`. Other objectives: confidence interval width per facility hour, fraction of shots within qualified incident-proton energy/angle envelope, beam-to-catcher interception, instrument saturation/background, repeatability, collector stability and uptime. Do not use only energetic alpha increment to decide whether precision acoustic control is worthwhile. Include randomized reference/OFF/SHAM/ON causal controls; the improved quality/yield has so far only been **reported by simulation**.

## Required next artifact to validate Gemini report
Full runnable code containing `run_ofat_sweep`, correlated 3-alpha generator/CM-to-LAB transform, detector response, acoustic arms and ledger; generated CSVs with hashes; fixed versions of source data; empirical or licensed BN stopping records. Verify conservation **per event**, common seeds/sources and actual randomization; independently reconstruct/fail comparisons and preserve negative results. Do NOT alter the canonical G0-B blind experimental protocol simply to suit this model.

**Status:** CODE-SPOT-CHECKED / NOT REPRODUCED / NOT CALIBRATED / NOT EXPERIMENTALLY VALIDATED.
