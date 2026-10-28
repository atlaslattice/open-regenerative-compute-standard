# STARS 2.0 — Copilot Final Preflight and Analytic Nulls
**2026-10-27 | User-supplied Copilot review; preserved and independently qualified by ChatGPT/Tidal Lantern**
**Status:** reviewer-proposed gates / not a run log / not a frozen G0-B protocol amendment / not a Canon invariant.
**Research motto (Copilot):** **“Zero physics produces zero magic.”** Specifically: when reaction cross section is zero, code must produce zero reaction births, zero nuclear Q release, and zero alpha products attributable to the reaction. The phrase is a reviewer mnemonic, NOT a renumbered constitutional invariant.

## Executive triage
Copilot: **three green lights, four amber lights and two consequential numerical corrections**. The review recommends executing *verification tests now* while blocking G0-B prediction freeze. New principal correction: `sum T_alpha,LAB = Q + T_proton,LAB` for stationary target and full three-alpha final state. At incident proton energy 675 keV LAB, approximately **9.35 MeV in laboratory**, **9.30 MeV in CM** (Q≈8.68 and E_CM≈0.618), using consistent masses. Check total four-momentum rather than only a rounded sum.

### Physical-source reference notes
- Spraker et al. (2012) original experiment (DOI https://doi.org/10.1007/s10894-011-9473-5) is represented in [EXFOR C2973 original](https://github.com/IAEA-NDS/exfor_master/blob/main/exforall/C29/C2973.x4), with original experiment counts/energy boundaries, angular distributions, and statistical plus systematic uncertainty.
- Sikora and Weller (2016), https://doi.org/10.1007/s10894-016-0069-y, reevaluate alpha yield using energy-window extrapolation, then divide total alpha yield by three to infer fusion-event reaction rates. This is **not** permission to divide the original restricted-energy Spraker table by three. Every data column must declare its *observable semantics*.
- Diamond detectors can be useful but do not replace calibrated G0-B silicon alpha/proton identification. EMI/EMP extra controls matter chiefly in laser-driven lanes; G0-B accelerator beam and laser pitcher must not be conflated.
- An exact primary source/location for the 2.5 MeV proton → 57 μm BN range claim is still needed. Never calibrate S(E) from a single R(E0) scalar, since many stopping functions can integrate to the same range.

## Observable semantics: mandatory typed quantity kind
1. `ALPHA_PRODUCTION_DETECTED_WINDOW`
2. `ALPHA_PRODUCTION_EXTRAPOLATED_TOTAL`
3. `FUSION_EVENT_CROSS_SECTION`
4. `EXCLUSIVE_CHANNEL_CROSS_SECTION`
5. `DIFFERENTIAL_ALPHA_CROSS_SECTION`

Required fields: EXFOR entry/subentry/pointer; projectile, target, product channel; incident laboratory/CM energy and exact frame; angular acceptance; alpha-energy window; detector solid angle/efficiency; particle multiplicity/branch definition; extrapolation method; source-versus-derived provenance; statistical and correlated systematic errors. Reject accidental type coercion. A detector-count cross section already incorporating multiplicity must not be multiplied by three again.

## Copilot preflight gate matrix, sourced to supplied review
| Gate | Unit/integration test | Pass predicate / provenance |
|---|---|---|
| N0 | Original EXFOR importer | Exact entry/subentry/pointer, units, observable, frame, reported uncertainty within conversion precision |
| N1 | Count vs event semantics | A detected-window alpha observable cannot be used as a fusion event cross section without an explicit validated transformation |
| N2 | Withheld nuclear points | Predict withheld source data under preregistered residual/uncertainty criterion, no post hoc percent tolerance |
| K0 | Event four-momentum | Conserved per event, strict numerical tolerance determined by method and machine precision |
| K1 | Two-step ^8Be breakup | One reaction generates three linked alphas; sequential recoil/angle correlations retained in CM→LAB transforms |
| S0 | Proton endpoint range | 57 μm BN anchor remains source-unverified; enforce only once primary methods/conditions located |
| S1 | Local stopping curve | Verify S(E) at multiple points, including near 162 and 675 keV LAB and 1, 1.5, 2.5 MeV |
| S2 | Range inversion | R^-1[R(E0)-x] matches independently integrated stopping solution |
| T0 | Analytic slab limit | Constant sigma/S and isotropic escape compare with analytic/higher precision reference |
| T1 | Zero stopping | No unphysical energy losses; distribute valid fusion birth depths correctly |
| T2 | Infinite alpha range | All geometrically escaping alphas retain their birth energy |
| T3 | Mirror symmetry | Symmetric slab + source yield equal front and rear exit expectations within Monte Carlo uncertainty |
| D0 | Detector forward folding | Frozen reference response reproduces known injected spectra |
| D1 | Background inference | Blank/electronics/particle-blocked channels and held-out controls reproduced by justified likelihood |
| C0 | System ledger | p energy + Q accounted for among alphas, material deposition, and explicit remaining physics terms; measured load separate |
| Z0 | Zero-cross-section conservation null | No nuclear events, zero nuclear alpha births and zero nuclear Q energy; unrelated backgrounds unchanged |

## Additional recommended anti-bug analytic limits

**Null Z0: “zero physics equals zero magic”** — set all p–^11B event reaction cross sections to exactly zero, verify zero generated p–^11B reactions and alpha products, while the *non-fusion* charged particle/EMP backgrounds may still be nonzero. Clarify that an electric/optical input remains real even if zero fusion reaction energy appears. This protects the downstream ledgers against rogue Q additions.

**T0: analytic uniform-depth slab escape** — for uniform alpha births, isotropic emission, fixed physical range R and slab thickness L, compute per-face escape analytically/with high-precision quadrature under explicit surface and finite-path conditions. A useful strict benchmark for a uniform stopping length and no scattering is the fixed-range probability over *both faces*, for slab thickness L, 
`P_escape = ∫_0^L [max(0, 1-x/R) + max(0, 1-(L-x)/R)]/(2L) dx`.
This equals `1 - L/(2R)` for `R>=L`, and `R/(2L)` for `R<=L` (continuous at R=L). Each face receives half under symmetric setup. Geometry check, not a full energy-loss spectrum.

**K0: analytic sequential two-body kinematics** — begin with exact masses in each declared state and energy frame; generate primary alpha + ^8Be* and then alpha + alpha in ^8Be rest frame; transform daughters into reaction CM and LAB, monitor event-level 4-vector closure. Use channel-specific measured branching/angular distributions only when available; isotropic decay is a labeled null fixture not a validated universal distribution.

**N2: held-out source interpolation** — raw source points are SOURCE-REPRODUCED at first, not CALIBRATED merely by fitting their own observations. Preserve original 41-point imported table and reject interpolation outside bounds unless an explicit source-qualified extrapolation policy is chosen.

## Statistics and diagnostics
Copilot properly declines to freeze BF10>10 or a Poisson–Gaussian likelihood without dark/blank evidence. Suggested preregistration fields: `likelihood_model`, `likelihood_justification`, `background_dataset_hash`, `prior_definition`, `prior_predictive_check`, `simulation_based_calibration`, `decision_statistic`, `decision_threshold`, `frequentist_operating_characteristics`. Laser and accelerator diagnostics differ. For repeatedly used targets, track delivered fluence, spatial profile, integrated charge, pulse duration, pulse repetition, target position, shot history, deposited energy, temperature, vacuum environment, damage/film changes; randomize position and target-age order to avoid confounding.

## Recommendation
**Execute N0/N1/K0/Z0/T0–T3 and provisional S2 now**, and build the source-type validator, correlated generator and detector-forward-model scaffolding next. **Do not freeze experimental G0-B predictions** until primary nuclear observable conventions, exact BN stopping references, kinematics, detector and background calibrations meet their own acceptance gates.

An independently reproducible, adaptable verification suite is a valuable project output whether the acoustic hypothesis passes or fails. No result in this review demonstrates acoustic fusion gain or net-electric performance.

## Research lineage
Prior [v0.9 white paper](../whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md), [post-EXFOR DeepSeek review](DEEPSEEK_POST_EXFOR_REVIEW_AND_TEST_ANCHOR_CORRECTIONS_2026-10-27.md), [discovery README](../RESEARCHER_DISCOVERY_AND_REPRODUCIBILITY_README.md), and [main manifest](../ARTIFACT_MANIFEST_2026-10-27.md). Full original Copilot text in originating conversation attachment dated 2026-10-27 local evening / filename 20261028-010923. This is an **attributed synopsis**, not a verbatim archived original or a tool-run receipt.
