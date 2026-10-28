# STARS 2.0 — DeepSeek post-EXFOR review: reproducibility, target anchors and corrected acceptance gates
**Date:** 2026-10-27 | **Origin:** user-supplied DeepSeek critique; primary-paper checks and integration by ChatGPT/Tidal Lantern | **Status:** review/design update; not executable WP-B v0.4 or empirical G0-B result.

## Summary
DeepSeek independently praised source provenance, multiplicity-aware alpha kinematics, 57-μm proton range, EMP-aware diamond detection, low-count Bayesian inference, and target beam-dose history. These are valuable constraints for a **portable research protocol** beyond p–11B. Several **specific proposed constants/interpretations are not interchangeable with validated executable unit tests**; the corrections below are required.

### 1. Original Spraker 2012 yields are alpha-particle count observables
Primary [Spraker journal article](https://doi.org/10.1007/s10894-011-9473-5) defines `X = Counts / (N_target × N_protons × dΩ)`, with cross-section-like units, explicitly **without dividing by particle multiplicity**. The authors report that for an alpha-1 peak energy window, ~**2.1** alphas/reaction contribute near **675 keV LAB** versus ~**1.5** near **2.64 MeV**. That is **energy-dependent accepted multiplicity**, not a fixed correction factor 3. EXFOR integrated C2973002 is tied to C2973003 angular distributions and restricted alpha-1 region. Do not use `sigma_b` from our original 41-row normalized CSV as a nuclear *reaction event* cross section or multiply by 3 without a separately validated reconciliation.

**Recommended test A:** exact reproducibility of the C2973002 41 numbers, units and ERR-S from original IAEA master; at **1.0 MeV LAB** the original tabulated observable is **315.936±10.9008 millibarns statistical**, separate correlated target-thickness 3.6% systematic. Then independently derive an accepted-alpha rate from the source's angular/energy acceptance, and only derive reaction probability from an independent reaction-total normalization. Earlier derived CSV remains preserved with legacy `sigma_b` label and a discoverable semantic warning.

### 2. Three-alpha kinematics
The complete p+^11B → 3 alpha breakup has three outgoing alpha particles, but branch-resolved alpha energies vary with event channel and emission angles; illustrative **3.76, 2.74, 2.74 MeV** must not be imposed universally. At **675 keV LAB** the stationary-B target CM energy is ~**618 keV**, so *CM-frame* total final kinetic energy is ~**8.68+0.618=9.30 MeV**, not simply ~8.68 MeV. LAB has an additional incoming total momentum contribution. Implement primary alpha + ^8Be recoil and two-alpha daughter decay with each branch's actual masses/excitation and per-event four-momentum/charge/baryon conservation.

**Recommended test B:** event-by-event energy/momentum invariants in specified frame, CM↔LAB Lorentz/low-energy transformation precision, correct particle multiplicity and branch-dependent spectra. The desired numerical tolerance must be explicitly defined in code from solver precision; “<0.1%” is a *proposed* numerical threshold, not a measurement.

### 3. BN proton range in NePTUN
DeepSeek cites **57 μm range at 2.5 MeV** for protons in BN at ~2.1 g/cm³. A technical summary of [Popper et al. preprint](https://arxiv.org/abs/2609.33483) attributes ~57 μm to SRIM. The arXiv abstract verifies the BN-converter experimental context but **does not expose the full SRIM run card, density and uncertainties**; therefore treat this as **PUBLISHED/SECONDARY-REPORTED BENCHMARK — NOT YET STRICT SOURCE-REPRODUCED**. Confirm primary-paper text and SRIM configuration, actual phase/composition/density, and ensure the stopping integral agrees across energies. A single range check within ±5% **cannot qualify** the entire BN stopping law.

**Recommended test C:** validate one point (2.5 MeV, density and SRIM conditions locked) and additional reference energies, material stacks, alpha stopping and sensitivity to uncertainties before source-calibrated runs. A 4–6 μm BN film is thinner than a 57 μm nominal range but **this does not imply negligible proton energy loss** when cross section changes sharply.

### 4. Diamond detector and EMP
[Salvadori et al. 2021](https://doi.org/10.1038/s41598-021-82655-w) report 5.486 MeV ^241Am single-alpha detection with ~0.8 ns offline timing in a diamond detector. EMP shielding/cabling are still critical. Single-crystal diamond and fiber-optic transport are high-quality comparator options **not mandatory demonstrated specifications for every setup**. Use matched instrument baseline, particle-blocked and blank shots, EMP dummy channels, signal recovery tests, separate laser and actuator pickup controls, and species confusion tests. A Faraday cage can change detection geometry; establish particle acceptance independently.

### 5. Bayesian low-count calibration
Preregister count likelihoods including background exposure, alpha detector efficiency, EMP transients, shot variability and detector noise; choose Poisson, hierarchical count, compound/overdispersed or mixed distributions **from measured blank-shot residuals**. A Poisson–Gaussian mixture is a **candidate**, not inherently universal. BF10 >10 is one prospective decision threshold requiring calibration and prior sensitivity, not guaranteed evidence against p-hacking. Cross-check posterior predictive and held-out validation. A blank-target dark shot may itself change laser-target EMP generation; compare appropriate blank/support-only configurations instead of assuming identical electronic background.

### 6. Beam repetition/dose/target damage
For separately positioned catcher, record delivered ion dose, proton current, beam duration, repetition, temperature, sputtering, backing damage, morphology and target changes. First-pass static solid remains reasonable for appropriately characterized conditions; dynamic modeling becomes necessary when measured state changes. **Nuclear B11 depletion is not established** at current model yields. Model degradation penalty and maintenance economics only after measured dose/lifetime and acceptance criteria.

## Researcher-facing acceptance statuses
| Gate | Current status |
|---|---|
| Source EXFOR 41 C2973002 values | Imported from original IAEA GitHub master, with statistical and common systematic uncertainties |
| Conversion to *fusion reaction* cross section | **BLOCKED**, requires multiplicity/acceptance reconciliation |
| Three-alpha generator + invariant tests | **SPECIFIED, NOT CODED/RUN** |
| SRIM BN 57 μm reference | **SECONDARY-REPORTED, EXACT CONDITIONS UNVERIFIED** |
| EMP hardened, particle-identifying diamond diagnostic | **PROPOSED, NOT BENCH-QUALIFIED** |
| Bayesian/preregistered G0-B acceptance | **DESIGN, NOT FROZEN OR RUN** |

## Reuse outside STARS
These gates are intended as generic research modules: quantity-kind-aware nuclear data, exact source units/frames, transport reference conditions, event conservation, blinded detector response, causal actuation controls, null-result retention, and cost/energy system boundaries. To claim a **reproducible completed framework**, the open-source program still needs runnable code, test fixtures, dependency versions, deterministic seeds and reproductions by another team. A documented protocol and dataset alone are an important foundation but not a completed validated implementation.

Researcher discovery: [metadata gateway](../RESEARCHER_DISCOVERY_AND_REPRODUCIBILITY_README.md), [machine metadata](../RESEARCH_METADATA_STARS_2_0_2026-10-27.json).
