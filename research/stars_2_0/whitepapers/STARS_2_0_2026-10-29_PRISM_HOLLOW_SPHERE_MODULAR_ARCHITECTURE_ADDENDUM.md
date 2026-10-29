# STARS 2.0 — PRISM, Hollow-Sphere and Stacked-Hybrid Comparative Architecture Addendum
**Date:** 2026-10-29  
**Status:** RESEARCH ADDENDUM / PROPOSED INTEGRATION, NOT EXPERIMENTAL VALIDATION OR APPROVED APPARATUS MODIFICATION  
**Project:** Atlas Lattice / Stars 2.0  
**Repository baseline reviewed:** atlaslattice/open-regenerative-compute-standard commit 4512e9bb8505591ea207d28c2f0689ab5aecae9f  
**Method:** Source-traced findings; keep independently tested and derived/potential-derived outcomes separate. Append only; preserve previous artifacts, failed tests and scope boundaries.

## Executive decision
**Do not construct an automatic PRISM + hollow sphere + Stars physical Frankenstein.** Compare (A) Stars stacked pulsed laser/pitcher/boron-catcher hybrid, (B) independent hollow-sphere pulsed target geometry, and (C) independent PRISM-like tandem-mirror continuous plasma concept. Share code for cross sections, particle diagnostics, alpha spectra, uncertainties and whole-system accounting; treat all proposed hardware couplings as optional research branches subject to boundary compatibility, incremental utility, and experimental validation. Redundant physical modules should be *replaced or omitted* when benchmarked incumbent functions already exist. Do not discard a Stars module solely because another geometry has a superficially similar purpose.

The detailed latest stacked-hybrid apparatus/parameter lockfile has NOT been confirmed by this GitHub audit. The present description is based on published Stars scope, manifest and handoff, and must be reconciled against newest Work artifact before freezing topology.

## 1. External evidence, with careful claims
1. **Borealis PRISM, public 2026-10-15:** Borealis describes a pB11 Rotating Ion Separation Mirror (PRISM), derived from tandem magnetic mirrors: central cell, end cells and open-field exhaust to preferentially remove helium ash while retaining fuel. The design seeks to address bremsstrahlung/ash losses and high-beta confinement; the company explicitly says simultaneous power-plant-condition performance is not yet shown. SOURCES: https://borealisfusion.com/technology/ ; https://borealisfusion.com/introducing-borealis-fusion/
2. **ENN EXL-50U peer-reviewed H-mode:** p–11B plasma H-mode reported, including roughly 16 to 40 ms energy-confinement-time change for the specified discharge. It is *not* proof of energy gain or of Stars laser-target response. SOURCE: https://doi.org/10.1016/j.xinn.2026.101458
3. **ENN boron pellet fueling:** preliminary pellet-injection experimental verification of boron-fuel replenishment (not standalone confinement gain). SOURCE: https://doi.org/10.1088/2058-6272/ae715e
4. **ENN electron temperature:** >8.6 keV central electron temperature reported in a particular ECRH-only spherical torus discharge. Do not conflate with a separate reported p–11B alpha reaction flux or NBI proton distribution. SOURCE: https://arxiv.org/abs/2610.14684
5. **Alpha channeling research:** Qin and Fisch 2026 ion-Bernstein-wave pole-resonance theory offers an interesting transfer mechanism in an idealized example; its quoted near-total transfer is NOT validated for Stars nor PRISM. SOURCE: https://arxiv.org/abs/2609.07732
6. **Hollow-sphere laser target 2026-10-27 claim:** User-supplied report asserts rear-opening hollow spherical target PIC simulation, 39 MeV planar versus 53 MeV hollow-sphere cutoff, ~20 MeV alpha energies and ~10^11 flux. A matching 2026 primary article/DOI and units/normalization have NOT been independently verified in this audit. **Status: UNVERIFIED REPORTED, NOT CALIBRATION INPUT.** Older hollow-target proton acceleration literature exists but is not confirmation of this specific report. Require publisher article, full methods, figures, energy/angle spectra, PIC input deck and normalization before quantitative adoption.
7. **ENN September 2026 ~10^8/s reaction/alpha-flux report:** maintain as a separately reported news claim pending primary diagnostic methodology; distinguish alpha flux from fusion-event counts, angular detector coverage and reaction Q.

## 2. Architectural comparison
| Dimension | A: Stars stacked hybrid (project hypothesis) | B: Hollow-sphere pulsed target (reported proposal) | C: Borealis PRISM (company design) |
|---|---|---|---|
| Primary regime | Pulsed laser proton pitcher, multiple boron catcher/target stages, optional field transport | Pulsed laser irradiating shaped hollow spherical target | Continuous / sustained magnetized multi-ion plasma tandem mirror |
| Main improvement sought | Qualified shot probability, proton-to-boron interactions, controlled alpha escape/recovery | Acceleration and angular shaping by target/sheath geometry | Fuel retention with alpha-ash discrimination and controllable exhaust |
| Hardest bottleneck | Stopping and beam transport between stages; substrate loss; shot-to-shot jitter; wall power | Can increased max proton energy yield more resonance-weighted pB11 reactions? Field transient and alpha diagnosis | Bremsstrahlung and ash; maintaining fast proton tail, fuel separation and viable recirculating power |
| Suitable source evidence | EXFOR typed observables, measured stopping/beam/detector data | Peer-reviewed PIC deck, experimental laser geometry/particle spectra | Company engineering paper and independent magnetic confinement / ash physics studies |
| Present physical proof | No demonstrated net power / acoustic gain | Specific new numerical claim unverified; no hybrid net power | Integrated reactor performance not demonstrated |
| Initial decision | Retain as baseline | Standalone competing target/source configuration; test optional pitcher/catcher substitution | Standalone alternative confinement architecture; borrow data/methods first |

**Different dynamical regimes:** one cannot infer pulsed target and continuous mirror simultaneously operate as the same reactor merely because both involve p–11B or charged alphas. A physical interface requires overlap in density, temperature, timing, ion distribution, magnetic field, contamination, thermal and electromagnetic boundaries.

## 3. Module-by-module redundancy / adoption disposition
| Stars module | PRISM overlap | Hollow-sphere overlap | Proposed decision |
|---|---|---|---|
| 10s acoustic pretreatment, sustained modulation, OFF/SHAM controls | No demonstrated counterpart | Possible alternative target-shaping route | **KEEP experimental branch**, never assign gain without randomized evidence |
| Laser proton pitcher | PRISM instead uses plasma heating / fast ions | Hollow target may itself generate protons | **COMPARE / OPTIONAL REPLACE**, not two proton sources by default |
| Serial boron catcher stages | PRISM distributes boron in plasma; not directly equivalent | Sphere may be reactive target, pitcher, or both | **KEEP A baseline; B standalone**, compare reaction probability per wall joule |
| Magnetic/electrostatic recirculation | Functional overlap with mirror confinement | Transient laser sheath is not long-term mirror | **COMPARE / REPLACE IF DUPLICATIVE**; don't sum retention probabilities |
| Controlled helium ash removal | Central PRISM purpose | Rear aperture may redirect escaped alphas, not sustained ash management | **ADOPT as accounting/design requirement**; hardware only when validated |
| Alpha direct energy conversion | Distinct from PRISM fuel retention; alpha channeling may compete with it | Escaping alpha spectrum affects acceptance | **KEEP OPTIONAL**, allocate each alpha's energy once: channeling OR collection OR heat/loss |
| Detector/spectrometer forward model | Shared diagnostics | Shared diagnostics | **SHARE COMMON SOFTWARE**, qualified to regime and EMP |
| Wave and materials solver | Magnetized-plasma waves different from solid target acoustics | Laser sheath / solid-target dynamics | **SHARE interfaces, NOT uncalibrated physics operators** |
| Whole-plant wall-plug ledger | Essential | Essential | **UNIFY measurement definitions, separate per-architecture power inputs** |

## 4. Evidence tiers and output schema
**LAB-MEASURED:** measured quantity in its actual instrument/operating conditions, original uncertainty and window.  
**VERIFIED-DERIVED:** arithmetic/physics derived from qualified measured or source-reproduced inputs, within supported conditions, documented transformations and uncertainty. It does NOT imply the hybrid output was measured.  
**POTENTIAL-DERIVED:** physically constrained extrapolation to untested geometry/scale, with transparent assumptions, model discrepancies, sensitivity/uncertainty intervals and failure/null outcomes.  
**UNRESOLVED:** source, units, model identifiability or calibration insufficient; output NULL rather than arbitrary number.

Each metric should include architecture_id, scenario_id, metric, unit, evidence_tier, original source, measurement context, input hashes, uncertainty type, calibration domain, extrapolation flags, and wall-plug boundary. Never use percentage multipliers to count the same confinement, target acceleration or alpha recovery effect twice.

## 5. Energy and particle balance requirements
Use typed distinctions: alpha-production detector/window cross section vs exclusive fusion-event cross section. EXFOR C2973002 recovered 41 rows are source-reproduced numerical data, not automatically a validated event-rate kernel.
For stage i: p_i = 1-exp[-integral n_B(z) sigma(E_cm(z)) dz] on surviving protons, under appropriate thin/independent-scattering assumptions; update particle energy/angular/charge state and losses after each stage. Do NOT multiply independent stage success-rate gains. Every fusion reaction consumes a proton; all three alphas must share correlated event four-momentum.
Split born-alpha energy into escaped/collected, energy channeled back to ions, deposited heat and other losses. Do not claim direct conversion and alpha channeling from the same alpha energy. Include drive laser, RF/NBI, cryogenic/vacuum, magnets, acoustic, collector bias and auxiliary loads in each regime's respective wall boundary.

## 6. Proposed fair comparative campaign (not yet run)
**Campaign A — independent physics:** source-traced EXFOR reaction typing, kinematics and stopping benchmarks; B standalone hollow geometry once original article available; C mirror ash-loss/confinement using source-qualified models.  
**Campaign B — fair engineering:** per attempted shot, delivered joule, operation hour, and facility wall joule; compare like-for-like metrics only and specify pulsed duty cycle versus continuous assumptions.  
**Campaign C — redundancy ablation:** A minus acoustic, minus mirror transport, minus second catcher, minus collector; B versus A's pitcher at matched power and B11 areal density; C PRISM-like baseline versus alternative fuel/ash transport.  
**Campaign D — conditional interfaces:** only if measurements support physical compatibility, study hollow-source → staged catcher, staged catcher → external mirror, alpha channeling → collector residual, keeping interface losses explicit.  
**Campaign E — reliability:** pre-registered REFERENCE/OFF/SHAM/ON with 10-second pretreatment and sustained modulation, *all randomized shots*, shot success/jitter, mediators, observed alpha spectra, and energy per attempted shot. No optimization on blind holdout data.

## 7. Software integration request
Retain immutable old source; add candidate modules: typed nuclear observable registry; source-qualified proton-energy distributions; staged-transport and depletion; laser-target PIC import; mirror loss-cone/ash transport; mutually exclusive alpha energy partition; per-architecture scenario schema; dual-evidence report; external invariant/negative-control suite. Mark proposed modules as NOT IMPLEMENTED until code and tests exist.

## 8. Release decisions and blockers
- **APPROVE research integration and competing-architecture benchmarking.**
- **DEFER physical assembly of PRISM+Sphere+Stars pending independent evidence of viable interfaces and measurable nonredundant value.**
- **HOLD** hollow-sphere 39/53 MeV/20 MeV/10^11 as unverified until DOI and underlying figures/input deck are recovered.
- **HOLD** global net-electric performance extrapolation until collector acceptance, full energy boundary and recirculating loads are qualified.
- **HOLD** blinded G0-B prediction freeze pending current project-approved contract and external calibration.
- **PRESERVE** October 28 Stars physics-only boundary with SHUGS/Element-145 separate; no speculative operator can modify physical reaction yield.

## 9. Recommended decision rule
Adopt a component only if (a) it addresses a defined deficiency, (b) improves an independently measured or bounded metric relative to the simplest alternative, (c) its net benefit survives uncertainty and new auxiliary loads, and (d) its physical operating regime is compatible. Otherwise **omit it, substitute it, or publish it as an independent competing apparatus**. The simplest defensible machine wins, even if that means discontinuing some original Stars modules.

*Authorship/provenance: Atlas Lattice-directed research; source and architecture synthesis by ChatGPT, 2026-10-29. This addendum is a literature comparison and research decision record, not a test report, validated experiment or claim of net energy production.*
