# STARS 2.0 v0.6 — Pitcher–Catcher–Collector: Evidence, WP-B Audit, and Falsifiable Experimental Roadmap
**Atlas Lattice | Open Regenerative Compute Standard (ORCS) | October 27, 2026**

**Status:** Research white paper, exploratory and noncanonical. **Audience:** Gemini Argon, DeepSeek, Copilot Researcher Mode, experimental plasma/nuclear physics reviewers. **Tagline:** *Receipts in the front, wizards in the back.*

**Authors/provenance:** Atlas Lattice project initiation and research direction: Dave Sheldon. Original WP-B model and cross-domain architecture contributions: Gemini Argon (2026-10-27). Technical-literature criticism and experimental prioritization: DeepSeek (2026-10-27). Independent software and physics-model review: Copilot (2026-10-27). Integration, conservation and source-boundary synthesis: ChatGPT / Tidal Lantern (2026-10-27). This is **contribution attribution, not independent institutional coauthorship, verification, or endorsement**.

## Executive abstract
Stars 2.0 is a proposed modular proton–boron-11 **fusion interaction and charged-product energy-management testbed**, not an existing reactor, not a claim of stabilized compound p–B11 fuel, and not evidence of net electric fusion. Its components—laser/beam proton pitcher, boron-rich catcher, optional acoustic/metamaterial target preparation, nuclear-spin preparation, plasma-wave manipulation, escaping-alpha collection, charged-particle electrical conversion, and storage/reinvestment—are tested separately before integrated claims.

Recent externally supplied analyses by Gemini Argon, DeepSeek, and Copilot converged on one **qualitatively sound but quantitatively unvalidated tradeoff**: thick solid boron-nitride targets increase fusion reaction opportunities but stop more newly born alpha particles before an external energy converter can collect them. Gemini's WP-B prototype produced an *assumption-dependent* maximum escaped alpha energy at a sampled catcher thickness of **5 µm (~0.7456 µJ)**, versus peak *escaped alpha count* at **6 µm**, while birth yield continued increasing through **60 µm**. This is not a universal optimum.

Copilot identified multiple material errors or limitations in that model: uncalibrated stopping and cross sections, mixing alpha escape from both sides with one-sided collection, bundled interventions masquerading as an orthogonal experiment, hardcoded recovery efficiencies, and a thermal ledger that treats outgoing particle energy as recoverable heat. Running the script independently confirmed that its **1 MeV proton stopping approximation is 52.89 keV/µm**, while its own comment describes **36 keV/µm**. WP-B must be audited before using its apparent optimum to design hardware.

**Finding:** The right first optimization is neither raw reaction yield nor alpha count, but an angle-, energy- and material-resolved **net electrical energy per wall-plug joule** across a common pitcher–catcher–collector boundary, with uncertainty and experimentally calibrated component models.

## 1. What the design actually is
The proposed primary reaction is
```
¹H⁺ + ¹¹B → 3 × ⁴He²⁺ + ~8.68 MeV
```
A successful encounter consumes one proton and one boron-11 nucleus. Failed encounters do not create fusion energy. The three emitted alpha particles are stable helium-4 nuclei; valuable energy resides primarily in their **kinetic phase-space distribution**, not in an exotic preserved alpha nuclear state. A ²⁸Si spin-zero host, ¹³C nuclear polarization, or phononic/metamaterial lattice has **no demonstrated ability** to hold a special internal nuclear alpha state through and after fusion.

The system chain is:
```
ACOUSTIC/MATERIAL PREPARATION
    ↓
CHARACTERIZED PROTON PITCHER → BORON-11 CATCHER
    ↓                               ↓
UNREACTED PROTON CHANNEL       FUSION-BORN ALPHAS
    ↓                               ↓
OPTIONAL RETENTION/RECYCLE     FRONT/REAR ESCAPE / STOPPING
                                    ↓
                        TRANSPORT & COLLECTION
                                    ↓
                   DIRECT DEC / IBW TEST / HYBRID
                                    ↓
                        LOAD → POWER ELECTRONICS
                                    ↓
                       STORAGE / REUSE / EXPORT
```
The pitcher–catcher need not itself be a thermally self-heated power reactor. However, any claim of net electricity must include **all** auxiliary cost and what happens to ions, electrons, radiation and heat. Static magnetic fields can redirect but do not themselves perform kinetic work on alpha ions. Electrostatic fields or genuinely interacting plasma waves can exchange energy; merely generating a coherent wave is not the same as exporting measured electricity. Hydrogen fuel cells are an analogy only at the power-chain level; alpha-particle kinetic energy conversion is not electrochemistry.

## 2. Evidence matrix — avoid invented multipliers

| Topic | Source-derived fact or model | Current evidence status | Implication |
| --- | --- | --- | --- |
| p–¹¹B resonance | ~675 keV center-of-mass corresponds to ~736 keV lab for proton on stationary ¹¹B | Established kinematics, with cross-section data to be calibrated | Model broad proton distributions and stopping; do not assume monoenergetic pitch |
| Continuous water-leaf pitcher / BN catcher | NePTUN reports 18,000 shots at 10 Hz with downstream BN converter | Published experiment/preprint | Repetition and repeatable target feed are feasible experimentally, not evidence of net fusion |
| Alpha stopping in BN | NePTUN discusses depth-dependent birth and escape; representative 2.9 MeV alpha range ~9.1 µm in BN | Paper-specific transport result | Explicit birth depth, direction and residual-energy distributions are mandatory |
| Spherical versus planar LFEX geometry | Strong alpha yield/spectral changes; ~100× comparison occurs in a high-filter energy selection | Published geometry experiment | Do not treat filtered detector ratio as universal total energy multiplier |
| Acoustic/liquid target shaping | Acoustofluidic and SAW technologies in neighboring disciplines | Demonstrated techniques; specific p–¹¹B yield improvement unverified | G1 uses matched sham and measures target state plus normalized fusion births |
| ²⁸Si/¹³C nuclear spin path | Potential target materials; transfer to ¹¹B/¹H through laser shot unshown | Proposed | Separate P-series research roadmap |
| Alpha-to-proton IBW pole coupling | Qin–Fisch modeled ~99.96% alpha power loss into coherent proton response in an idealized example | Kinetic theory, **not electricity** | G3-A must measure alpha-origin load output |
| Electrostatic direct energy conversion | ENN reported >80% in a fundamental low-parameter charged-particle unit | Specific unit experimental result, not full p–¹¹B collection | Benchmark with characterized broad-spectrum helium beam |
| Gemini 5 µm catcher optimum | WP-B surrogate, 14 sampled thicknesses, fixed assumed source | Unvalidated numerical scenario | Repeat after material/cross-section/escape calibration |
| Gemini G3-A PASS and FAIL | Fixed assigned alpha beam energy, load and driver overheads | Hardcoded assumption ledger | No mechanism is experimentally proven or retired by this table |

### Public papers and source boundaries
- Popper et al. (2026), *Continuous Laser-Driven α Source*, arXiv:2609.33483, https://arxiv.org/abs/2609.33483 . 10 Hz, 18,000 consecutive shots and a replenished laser pitcher plus solid BN catcher; depth-dependent alpha escape is central.
- Qin & Fisch (2026), *Thresholdless IBW Emission and Alpha-to-Thermal-Ion Energy Channeling via Pole Resonance of Fusion-Product Ions*, arXiv:2609.07732, https://arxiv.org/abs/2609.07732 . Ion Bernstein wave (IBW), **not** generic SBS ion-acoustic wave; idealized coherent energy transfer is not electrical recovery.
- *Hydrogen boron fusion in confined geometries*, *High Power Laser Science and Engineering*, https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/hydrogen-boron-fusion-in-confined-geometries/D273DDE00ABB65D29D2053845A22A887 . Report detector-filter-specific comparisons as such.
- Mazzucconi et al. (2025), *European Physical Journal A* 61, 114, DOI https://doi.org/10.1140/epja/s10050-025-01589-3 . Separate *differential* and *total* cross sections and reference-frame conventions.
- Kong et al. (2026), *Plasma Science and Technology* 28(5), 054001, DOI https://doi.org/10.1088/2058-6272/ae445a . >80% in a specific low-parameter electrostatic converter test unit; verify denominator, particle species, spectrum and scaling before extrapolation.
- Ochs et al. (2022), *Physical Review E* 106, 055215, DOI https://doi.org/10.1103/PhysRevE.106.055215 . Conditional confinement-time improvements from modeled alpha-energy distribution and channeling, not a measured plant.

**Evidence rule:** Primary-source verification of a paper's existence or conclusion does not validate new quantitative extrapolations, the scenario code coefficients, or applicability to a different geometry.

## 3. WP-B original prototype — reproducible but not calibrated

### 3.1 What Gemini Argon implemented
The GitHub archival original separates (a) phenomenological p–¹¹B cross-section surrogate, (b) empirical BN proton stopping, (c) 4π angular alpha escape with two discrete representative alpha energies and fixed-range residual-energy scaling, (d) proton distribution and depth integration, (e) bundled '2³' experimental scenarios, (f) sampled BN thickness sweep, and (g) assigned C1/C2/C3 charged-particle converter input/output scenarios. This decomposition is useful software infrastructure.

### 3.2 What its CSVs mean
At **5 µm** under a fixed assumed broadband proton source: approximately **3.231 million alpha births**, **2.294 million escaping alphas**, **71.0% particle escape fraction** and **0.7456 µJ of escaping alpha kinetic energy**. Highest sampled *energy* at 5 µm and highest sampled *count* at 6 µm are different objectives. The model represents alpha emission by two surrogate groups; the 5 µm value must be independently stress-tested against stopping/range data, angular correlations and source distributions. A 5 µm result is **not** established engineering design guidance.

Its G3-A 'C1 pass' assigns a 100 mJ alpha-beam input, 54.5 mJ at a load and 4.2 mJ wall overhead; +50.3 mJ follows from arithmetic, **not** particle transport or a measured power converter. Wave-on modeled cases likewise hardcode transfers and driver costs. A positive beam-test load *conditional on an externally supplied alpha beam* is in any case not a net electric fusion plant: alpha-beam generation belongs to a different boundary.

### 3.3 Directly checked discrepancy
The code labels a harmonic, heuristic BN proton stopping function as SRIM calibrated and comments that at 1 MeV S ~36 keV/µm. Executing that function instead gives **S(1000 keV) ≈52.89 keV/µm**, about **47% higher**. At 75 keV, S≈90.4 keV/µm agrees approximately with the ~92 comment. Copilot spotted the underlying issue; its textual conjecture that the 1 MeV result was below the comment was in the wrong direction, corrected by directly running the function. This is a **code-versus-comment mismatch**, not proof that either number matches measured stopping.

### 3.4 Other mandatory corrections
- The so-called 'relativistic' stationary-target CM conversion uses a **nonrelativistic mass ratio**; reasonable at the modeled energies but label correctly.
- Additive Breit–Wigner cross sections, penetrability caps and spin factors are **surrogates**, not confirmed evaluations of the literature. Provide raw data, interpolation, uncertainties and cross-section residual plots; avoid treating differential cross-section peaks as total values.
- Alpha escape currently reports **both-face escape energy** but applies downstream collection to the entire escape pool via a scalar geometric factor. Compute separate front, rear, oblique, charge-state and energy distributions. Magnetically returned front alphas need explicit demonstrated transport.
- The alpha energy representation (3.76 MeV + two particles at 2.461 MeV) and post-path residual-energy exponent 0.65 are simplifying assumptions. The real sequential decay yields correlated three-body energy/angle distributions and charge-state-dependent stopping.
- Acoustic ON changes thickness **50 → 4 µm**, laser-to-proton energy efficiency **2.8 → 4.8%**, source spectrum and sheath distribution simultaneously. This is a **bundled architecture scenario matrix**, not a causal 2³ test of three independent devices. Wave ON additionally modifies both stopping and converter conversion.
- One all-system sham is not three independently matched sham controls. Distinguish acoustic-only sham, spin/RF sham, wave-only sham, all-system sham and separate converter-bias controls.
- Thermal pool incorrectly assumes all proton beam energy becomes heat despite calculated proton exit energy; it also includes uncaptured alpha and converter-loss energy irrespective of whether it remains inside the declared recoverable thermal boundary.
- Depth/quadrature integration, reaction depletion, stopping/range convergence, sample thickness spacing, alpha angular sampling and uncertainty sensitivity need explicit tests.

## 4. WP-B v0.2 physics specification — **proposal, not yet coded**

### 4.1 Proton–catcher interaction
For incident proton distribution d²N_p/dE₀dΩ₀, target density n_B(x) and stopping rate S_p(E,x), evolve E_p(x) along the path, including angular path length and source straggling where supported. The thin-reaction-probability limit is

```
N_f ≈ ∫ dE₀ dΩ₀ [d²N_p/dE₀dΩ₀]
          ∫_target n_B(x) σ_pB(E_cm(E_p(x))) dx .
```

For probability not negligible, add proton survival and competing interactions. Nuclear alpha birth count ~3N_f. The measured escape spectrum, **not** alpha birth count alone, is the input to the converter model.

### 4.2 Depth-resolved alpha escape
```
dN_alpha,born/(dE_alpha dΩ_alpha dx)
    = reaction_depth_distribution × conditional_alpha_decay_spectrum.
```
Use tabulated helium stopping/range in actual target density/composition, compute directional path length to **each** surface, residual energy at exit and material interception. Record at minimum:
```
E_alpha,birth
E_alpha,exit_front
E_alpha,exit_rear
E_alpha,deposited_target
E_alpha,lateral_escape
E_alpha,unresolved
```
and assert their sum within numerical tolerance. Note fusion Q-energy and initial collision kinetic energy may both enter outgoing product kinetic energy; avoid using 8.68 MeV alone as a universal absolute final-state energy when establishing an exact laboratory-frame energy ledger.

### 4.3 Converter/collector
For alpha phase-space flux Φ_α(E,Ω,t) at the interface and actual acceptance A(E,Ω,t):
```
E_DC,load = ∫ Φ_α(E,Ω,t) A(E,Ω,t) η_DEC(E,Ω,t) E dE dΩ dt
```
subject to collection geometry, space charge, grid interception, secondary electrons, charge exchange and insulation. An ENN single-stage unit efficiency is **not** a full-device acceptance-weighted value for broad alpha spectra. Track front/back collection devices separately, and define which energy is dumped into recoverable structures.

### 4.4 Plasma-wave branch
Keep **IBW cyclotron-pole hypotheses** distinct from conventional laser-SBS ion-acoustic target modulation. The published 99.96% model is idealized coherent **proton-mode** response, not electricity. A wave-on/off experiment must compare the alpha energy loss, mode energy gain and time-integrated **incremental electrical output at a load** after extra wave-drive wall-plug energy. Use alpha-on/off as well as wave-on/off controls and characterize antenna reflection and plasma impedance. Sidebands alone may signal dielectric modulation rather than power transfer.

### 4.5 Net electrical boundary
```
E_net,export =
    E_DC,to_export + E_other_electric,to_export
  - E_laser,wall - E_RF,wall - E_acoustic,wall
  - E_spin_prep,wall - E_magnets - E_vacuum
  - E_cooling - E_materials/prep - E_controls - E_other_aux .
```
Recycled energy used by the next shot is not exported electricity. Do not subtract both optical laser output and wall-plug input for the same laser. Subtract unrecovered kinetic/radiative outputs from any hypothetical heat-to-electric pool. Every joule requires one input source and one destination.

## 5. Energy conservation and sensitivity tests
Required internal assertions:
1. Each incident proton either reacts, exits with remaining energy, is stopped/deposited, or enters a separately named category; nuclear reaction changes particle identities and Q-energy must be applied only when it occurs.
2. Alpha birth energy equals front/rear/side exit, energy deposited in matter/plasma, radiation, and unresolved residuals, with energy and charge-state bins.
3. Converter input equals delivered electricity, deposited collector heat, uncollected exiting particle energy, stored field-energy change and any identified other sink, with power supply included.
4. All experimental performance plots carry error bands or scenario envelopes.
5. Numerical convergence versus energy-bin, angular-bin, depth-step, and target-thickness refinement must be shown; an optimum is defined by named objective and assumptions.

Minimum sensitivity axes:
```
target thickness: coarse 1–60 µm + local refinement
proton source: measured TNSA spectrum + surrogate spectrum envelopes
pB cross sections: evaluated curve(s) and uncertainty
stopping: independently calibrated proton + helium ranges in BN
alpha angular emission: isotropic null plus spin-dependent hypotheses
collector: front-only / rear-only / dual collector
conversion: single/multistage acceptance-weighted transfer
wave: no-wave / measured RF / hypothetical self-excited IBW
spin: unpolarized / measured polarization only
auxiliaries: all real per-shot and continuous service costs
```
**Do not** use a 2³ factorial label for a matrix where an intervention also changes thickness or source. Use a full or fractional independent design, or accurately call it a bundled architecture comparison.

## 6. Near-term falsification gate schedule
**G0: primary references, data licensing and computational calibration.** Fix source metadata and lock the boundaries.

**G1: Geometry × acoustic target preparation.** Cross planar/spherical target geometries with acoustics OFF/ON and per-subsystem sham. Randomize and repeat; measure target thickness, focal position, proton spectrum, fusion-birth-corrected alpha output and electrical acoustic cost. The published LFEX high-energy-filter comparison is not a 100× whole-fusion prior.

**G3-A-DEC: benchmark characterized alpha/helium ion beam collection and direct voltage/current delivery.** The benchmark is independent of nuclear fusion; track beam generation energy in any system-level comparisons.

**G3-A-WAVE: measure wave-mediated alpha-origin energy transfer separately from external drive, with measured electrical load output.** A null effect or negative incremental work retires the tested geometry or regime, not all possible alpha-channeling physics.

**P0–P5 spin roadmap:** separately measure ¹¹B/¹H polarization, lifetime, prep cost and survival through representative laser interaction before integrating spin factor in yield models.

**G4 integration:** only independently characterized interventions qualify for the factorial combination.

**G5 whole-wall-plug:** no net power claim absent repeatable E_net,export >0 with uncertainties, service loads, downtime and fuel/material throughput.

## 7. WP-C and WP-D downstream design implications
**WP-C experimental protocol** should preregister endpoints and sham definitions. Suggested primary endpoint is *fusion birth rate per measured incident proton and energy spectrum*, and separate engineering endpoint *collector-delivered electric energy per wall-plug joule*. Diagnostic CR-39 alone does not automatically reveal full 4π births or original birth angular distribution because escape and acceptance introduce bias.

**WP-D converter design** must take as input the **actual exit phase-space spectrum** produced by the audited WP-B model, rather than three monoenergetic alphas, a fixed 0.78 geometric collection fraction or a scalar conversion efficiency. Include space-charge, longitudinal/transverse spread, grid losses, time structure and separate kinetic energy from output electrical work. Compare only matching beam-input conditions across electrostatic, traveling-wave and hybrid options.

## 8. Questions for the independent review team
### Copilot / numerical verification
1. Can the existing code be refactored into independent physics modules with unit tests, no changing original data?
2. At what BN proton energies does the stopping surrogate differ most from traceable reference data, and how much does it move optimal thickness?
3. What is the smallest energy-accounting schema that closes beam, target, alpha escape, converter and wall-plug boundaries?
4. Which parameter correlations most undermine the existing sampled optimum?
5. Does alpha forward/rear separation alone materially change the 5–6 µm scenario maximum?

### Gemini Argon / plasma and recovery architecture
6. For Qin–Fisch's IBW branch, what resonance condition and alpha phase-space distributions plausibly exist in an actual pulsed pitcher–catcher exit beam?
7. What measurable load interface could convert **alpha-origin** wave power into DC/RF without mistakenly crediting RF seed power?
8. Can an ultrathin boron catcher retain acceptable reaction probability under experimentally measured beam stopping and converter acceptance?
9. What model architectures would link target acoustic state to proton source distributions without assuming a fixed 2.8→4.8% efficiency gain?

### DeepSeek / experimental source audit
10. What total versus filtered LFEX fusion-alpha yields can be backed by original data and diagnostic acceptance?
11. What exact species, incoming spectrum and denominator led to ENN's unit-level >80% DEC result?
12. Which primary data tables for p–¹¹B cross sections, proton stopping in BN and helium stopping in BN can legally be committed or cited?
13. Which spin polarization results survive relevant pulsed irradiation, with quantified measured ¹¹B polarization rather than analogs?

### Joint decision
14. Can each reviewer produce one **strong falsification test**, one **uncertainty-dominant assumption**, and one **independent observation that would overturn their favored mechanism**?
15. Which single physics-data replacement (cross section, stopping or escape) most improves reproducibility at lowest effort?

## 9. Artifact and provenance policy
The preservation ledger is [ARTIFACT_MANIFEST_2026-10-27.md](../ARTIFACT_MANIFEST_2026-10-27.md). It links v0.2–v0.5, original Gemini code plus three CSVs, original/as-received snippets, complete supplied Copilot review, and the DeepSeek/Gemini provenance digest. No overwrite of WP-B originals. Repaired numerical code belongs in **wp_b/revised/** with an explicit changelog, tests and reproduction commands. All external reviews retain origin attribution, original wording when available, and a distinction between audit, model, experiment and extrapolation.

## 10. Prioritized next steps and final position
**Immediate:** WP-B v0.2 calibration and conservation repair. Preserve the original scenario output as a reproducible hypothesis generator. **Next:** WP-D converter collection and accepted alpha phase-space; **then:** WP-C preregistered experiment and G4 integration. Parallel P-series spin work stays independent.

The central substantive result is a sharper question: **At what target geometry, proton spectrum and alpha exit distribution can collected electrical work be maximized after paying for target preparation, beam generation and conversion?** Current evidence supports asking this question; it does **not** establish a working energy-producing machine.

**Research maxim:** *There is no waste unless you waste it*—as an engineering target constrained by measured conservation and thermodynamic irreversibility. *Receipts in the front, wizards in the back.*

---
**Review requested:** Please return corrections with line/section, primary source or reproducible calculation, measurement boundary, and suggested falsifying test. Preserve dissenting reviews rather than silently averaging them into agreement.
