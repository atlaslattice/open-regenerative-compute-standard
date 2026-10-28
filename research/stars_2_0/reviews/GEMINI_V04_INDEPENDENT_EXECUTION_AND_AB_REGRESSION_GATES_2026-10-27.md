# STARS 2.0 — Gemini Argon WP-B v0.4 Independent Execution and Adversarial A/B Gates
**2026-10-27 (US Central evening) | Atlas Lattice / ORCS | Source-attributed independent verification by ChatGPT/Tidal Lantern**
**STATUS: CODE EXECUTED / 2 BUNDLED TESTS PASSED / 5 GENERATED CSVs / ADDITIONAL INDEPENDENT A/B RESULTS; PHYSICS UNCALIBRATED**

## What changed
The project lead supplied the **actual Gemini Argon ~762-line Python code** as a Markdown-fenced source attachment `Pasted markdown(20261028-014210).md` (Gemini's original contents preserved in conversation). The Markdown fence was stripped with no intentional edits to underlying Python lines, producing `stars_v04_original_extracted.py`. Source compilation PASSED. It imports **numpy 2.3.5 and scipy 1.17.0** in this execution environment; contrary to the source header, this is **NOT zero external dependencies**. The bundled `unittest` tests 2/2 PASSED and the script generated all five expected CSVs from `__main__`.

- Original extracted source SHA-256 in this execution: `2db27298ea7f11c24cf891b4b784a5e21a8417c0207a3089f51bd037c44e522e`.
- Gemini's earlier reported source SHA-256: `0fdfcc1d4cdf6c177ee19fa0fb23a3588b1bdca2464036b7b91b29398bc93cf8`.
- **HASH MISMATCH.** Some formatting/encoding differences are possible, but exact claimed artifact identity is **not verified**. Preserve original and request original byte-for-byte file/hash. No author-intended source “fixes” were made for this audit.
- Generated: `stars_2_0_wp_b_v04_correlated_3alpha_events.csv` (200 rows); `..._s1_quality_adjusted_utility.csv` (5); `..._s2_collector_window_sweep.csv` (16); `..._s3_deepseek_target_arms.csv` (4); `..._harmonic_local_smoothing_pde.csv` (3).
- Independent A/B audit script and JSON were run outside source's two existing unittests. Bundled suite tests only: kinematic self-consistency in its approximate mass system and >2x utility of an **assumed stabilization**. They do not constitute the Copilot 16-gate verification matrix.

## Critical finding 1 — complete S2 collector optimum is 7.0 μm, NOT 6.0 μm

The new code's **full generated 16-thickness CSV** gives:
| Objective | Peak among sampled thicknesses |
|---|---|
| Rear escaping alpha energy | **5.5 μm**, 0.17296267 μJ |
| Front+rear 4π escape energy | **6.0 μm**, 0.32989566 μJ |
| Collector-window accepted rear alpha energy | **7.0 μm**, **0.12609345 μJ** |

At **6.0 μm** accepted energy is **0.12529362 μJ**; at 7.0 μm it is 0.12609345 μJ. Difference ~0.00079983 μJ, ~0.64% relative to 6.0. This is small and may not survive source/model uncertainty, but it **contradicts** the earlier report's claim that its sampled collector optimum is at 6.0 μm. Previously reported table omitted 7.0 μm. **A/B requirement:** hold inputs and generator constant; compare accepted-optimum across collector angles, energy acceptance, n_mu integration quadrature, material data and 5–8 μm fine mesh. Report uncertainty/plateau rather than a unique optimum when effect is tiny.

## Critical finding 2 — Newman phases do NOT give 3.62× crest factor in this source

Computed from standalone code (16 modes, k^1.5 dispersion, 256 x × 128 t sampling; RMS ~0.707107 across all arms):
| Phase treatment | Peak/RMS | L4 space-time norm | Fraction |u| > 2.2×RMS |
|---|---:|---:|---:|
| Coherent all-zero phase | **5.65685** | 0.937126 | **1.956%** |
| Newman quadratic phase `πk²/16` | **5.12192** | 0.971061 | **2.417%** |
| Alternate phase `0.5π sin(k)` | **3.62278** | 0.932426 | **3.027%** |

Hence the **3.62× is an alternate sinusoidal phase**, not the implemented Newman sequence. Newman improves *max* but worsens both L4 and the chosen threshold occupancy relative to all-zero. Alternate decreases max and L4 slightly, **but spends MORE space-time above the source's own 2.2× RMS rupture proxy**. It does reduce occupancy above **3.5× RMS** (0.0305% alternate vs 0.1343% coherent). The correct physical choice depends on damage threshold and material/space/time dynamics. We independently compared 30 seeded random-phase vectors: mean crest ~3.75, minimum ~3.23, maximum ~4.22; the selected alternative is not uniquely optimal over simple random-phase controls on *maximum crest alone*. These are toy mathematical results only, with no validated foil failure stress or actuator transfer function.

**A/B test H:** run zero/Newman/alternate/random/optimized phase ensembles with identical power and physical wave-transfer response. Vary threshold, frequency dispersion, boundaries, amplitude envelope and spatial-temporal resolution; compare peak, L4 norm, exceedance duration, damage proxy, target motion, repeatability and cost. Do not call `mean(abs(u)>2.2*rms)` a **physical rupture fraction** or a proof/application of OpenAI local smoothing; it is an arbitrarily defined exceedance proxy. New OpenAI theorem's assumptions must be independently shown applicable to real PDE.

## Critical finding 3 — A/B zero cross-section passes, with a numerical hygiene issue
Monkeypatched the existing surrogate `sigma_pb11_configurable(E)` to return zero, leaving geometry, laser and other model settings unchanged. All thickness outputs yield exactly **zero alpha births**, **zero alpha escaping** and **zero collector accepted**. All four/five arm quality-adjusted utility outputs are zero. **PASS: Z0 “Zero physics produces zero magic” nuclear null.** HOWEVER the source unconditionally computes `std/mean` even for zero output, emitting a NumPy RuntimeWarning and NaN CV. **FAIL: finite diagnostic integrity** in this corner case; guard zero denominator and emit a structured undefined/NA value, not NaN in a machine-readable result.

## Independent analytic geometry A/B
A separately coded ideal uniform-depth isotropic fixed-range planar-slab quadrature vs the known analytic result `P_escape = 1-L/(2R)` for R>=L, else `R/(2L)`:
| Slab L, range R | Independent quadrature | Analytic |
|---|---:|---:|
| L=1, R=2 | 0.750000 | 0.750000 |
| L=4, R=4 | 0.499603 | 0.500000 |
| L=6, R=2 | 0.1665695 | 0.1666667 |

**PASS for independent analytic fixture**, NOT proof that Gemini's physical alpha-escape routine passed T0; the fixture has not yet been wired into the actual simulation's transport function as a source-independent unit test.

## Critical finding 4 — kinematics conservation has a self-consistent toy-mass construction
The event generator explicitly sets `M_B_EFF_U = 3*M_ALPHA_U - M_PROTON_U` (not the separately declared actual `M_B11_U`), and makes kinetic available energy close using Q=8.682 MeV and a Galilean boost. Momentum residual is calculated in **scaled internal w vectors** rather than declared physical MeV/c vectors and compares `sum(w_i) - 3*w_boost`, so “exact four-momentum in physical mass conventions” is **NOT proven** by the internal test. This can be a useful nonrelativistic **analytic conservation fixture**, but it must be replaced/supplemented with measured physical nuclear masses and actual four-vectors and correct Q from the masses. The `98.5% 8Be(2+)` branching fraction remains unsupported/energy-independent. The main thickness routine also **does not call the event generator**: its `alpha_escape_and_collector_window` uses seven hard-coded weighted alpha spectral bins and 1D cosine integration, so its “correlated 3-body thickness sweep” is NOT the same eventwise correlated simulator whose 2-test bundle passes.

## Critical finding 5 — thin target/backing implementation is a parameter toy
The S3 backing calculation propagates 25 μm of “substrate” using **the same boron-nitride proton stopping function** irrespective of actual Si/C backing; its rear alpha function adds backing distance to a boron-nitride alpha range. Substrate-specific stopping/composition is therefore **NOT implemented**. The claimed 82%-open support is implemented as an 0.82 multiplier only on rear-side escape/collection, with no explicit thickness-varying aperture or coupled mechanical survivability model. The printed-mesh A/B ratio is conditionally correct inside assumptions, but does **not** demonstrate that the mesh is physically optimal or required.

Likewise `icru49_...` stopping functions are heuristic formulas, not independently ingested ICRU experimental tables, and `sigma_pb11_configurable` is a hard-coded surrogate, **not EXFOR-calibrated**. Direct numeric “comparison” to original Spraker EXFOR C2973002 values at 650 keV (source alpha-yield 1.3982151 b vs surrogate 1.0842563 b), 1 MeV (0.315936 vs 0.2666808 b), and 1.5 MeV (0.3253445 vs 0.1068860 b) **cannot be used as fitting residuals** because detected-alpha yield and per-event cross sections are different observables. These figures indicate scale mismatch but no physics verdict until quantity-type normalization is resolved.

## A/B implementation gates before model promotion

1. **PACKAGING (P0):** source bytes and claimed hash; pin NumPy/SciPy; restore proper source header. Preserve the exact original.
2. **NUMERICS (P1):** avoid NaN CV at zero yield; bound/unbounded interpolation hard-stop; integer/random seeds and units; test numerical convergence.
3. **KINEMATICS (K0/K1):** separate mass-correct physical four-momentum/event distribution tests from self-consistent equal-mass toy; swap fixed branching and hard-coded spectrum with measured channel registry; route the main thickness run through same event generator or label explicitly surrogate spectral quadrature.
4. **S2:** 5–8 μm fine grid and physical collector acceptance sweeps, sensitivity to threshold and stopping and measured source angular/energy distribution.
5. **S1:** demonstrate whether ON variance changes are model inputs (they currently are); compare threshold sweep across 40–100% qualified fraction, cost per *qualified* shot and robust efficiency over multiple seeds. Validate "pre-registered" gate wording against actual code: an internal comment claims thickness [3.5,5.5] and an implementation criterion actually checks [3.8,5.2] plus pointing; these are not equivalent. Source comment also claims detector saturation qualification but code does not model it.
6. **S3:** physical material-specific stopping and geometry, areal density and isotope composition, readouts in both layer orientations; no fixed "choke" conclusion without actual backing.
7. **Harmonics:** A/B phase sequences and actual PDE; physically meaningful failure threshold and nulls, not a mislabeled reduction to 3.62 by Newman.
8. **DETECTOR:** source-dependent response and EMP/nuisance model in G0-B vs laser lanes.
9. **EXFOR semantics:** original C2973002 detected alpha production must never silently become reaction event cross section.
10. **G0-B freeze:** remain blocked until Gemini/DeepSeek/Copilot source conflicts and experimental acceptance are resolved, model data calibrated, and project lead approves frozen contract.

## Preserved research record and next handoff
- Gemini supplied original source text as `Pasted markdown(20261028-014210).md`; the independent local execution produced five actual CSVs and a JSON A/B evidence report. These files are available as a downloadable ZIP attached to the originating ChatGPT conversation. This GitHub audit is **not** a claim that the original Python bytes and generated CSVs have been pushed to GitHub.
- [Gemini earlier claimed tables review](GEMINI_ARGON_V04_REPORTED_RESULTS_HARMONIC_CREST_FACTOR_AND_REPRODUCIBILITY_AUDIT_2026-10-27.md).
- [Copilot preflight](COPILOT_FINAL_PREFLIGHT_ZERO_PHYSICS_ZERO_MAGIC_2026-10-27.md).
- [GPTWork handoff](../GPTWORK_IMPLEMENTATION_HANDOFF_PENDING_GEMINI_2026-10-27.md).
- **Evidence state:** **SOURCE RECEIVED → CODE EXECUTED (two author tests) → A/B VERIFIED FOR CODE BEHAVIOR, NOT PHYSICS CALIBRATED.** Retain original code and all negative/discrepant results.

**Motto: Zero physics produces zero magic. Lower peaks do not always mean lower damage. Correct arithmetic does not imply correct nuclear physics.**
