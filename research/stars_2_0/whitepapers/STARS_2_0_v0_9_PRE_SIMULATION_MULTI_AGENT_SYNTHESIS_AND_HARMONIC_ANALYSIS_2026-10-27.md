# STARS 2.0 v0.9 — Pre-Simulation Research White Paper
## Proton–Boron-11, Correlated Alpha Transport, Acoustic Quality Control, Collectors, and the New Harmonic-Analysis Research Lead

**Atlas Lattice / Open Regenerative Compute Standard (ORCS)**  
**Date:** 2026-10-27  
**Project origin/direction:** Atlas Lattice project lead  
**Research collaboration and source-attributed contributions:** Gemini Argon, Copilot Researcher, DeepSeek, ChatGPT / Tidal Lantern.  
**Status:** PRE-SIMULATION RESEARCH CANDIDATE. NOT peer-reviewed as one unified paper. NOT a validated nuclear-data model, observed acoustic fusion gain, successful independent simulation of WP-B v0.3, or net-electric fusion demonstration.

> **Scope and hypothesis.** Test whether a characterized laser-driven proton source, calibrated ^11B-bearing catcher, correlated three-alpha transport, and rigorously controlled acoustic preparation produce more **useful, detector-qualified, potentially collectible alpha output** than well-matched baseline conditions. Separate proton–boron nuclear physics, transport, causal acoustic effects, collector engineering, operational quality and complete wall-plug energy economics. An apparent pattern or simulated advantage is a lead until independently measured.

## Executive synthesis — what is strongest today

1. The **most actionable near-term experiment is G0-B**: blind predictions for incident/transmitted protons and front/rear/side alpha spectra using independently calibrated beam, material, cross-section and detector data. Model failures must be preserved.
2. The **few-micrometre target optimum** is a recurrent *surrogate-model structural prediction*, not a measured optimum. Different model versions have shifted its value and absolute scale. There are different optimum definitions: rear-face escaping energy, both-face exit, accepted detector counts, *collector-reachable* kinetic energy, and qualified shots per cost.
3. **Gemini Argon's v0.3 simulation is not independently reproduced**: the pasted Python is a partial stopping/cross-section/collector parameter module, not the claimed correlated event, OFAT, four-arm acoustic and detector simulation. Its numeric spot checks are internally consistent only.
4. **DeepSeek's target fabrication distinction is valuable:** pitcher, reaction layer, holder and downstream collector are serial subsystems; a printed holder is not a printed dense 4–6 μm BN reaction foil. Compare substrate/film layouts at the same measured ^11B *areal atom density*.
5. **Copilot's intervention is foundational:** classify the ~675 keV feature as **incident proton LAB** (about 618.4 keV center of mass for stationary ^11B), distinguish nuclear-channel assignments, demand correlated alpha kinematics, detector forward folding, pre-registered blind acceptance and an unambiguous energy ledger.
6. **ChatGPT/Tidal Lantern's independent addition** is a staged causal/engineering interface: physics gate before acoustic gate; total effect and mediators separately; quality-adjusted throughput separate from energetic gain; calibration/pre-registration/source status and research ancestry with no erased failures.
7. **OpenAI's 2026-10-26 mathematics claim is a methodological research lead**: harmonic-analysis local smoothing and a new auxiliary PDE may suggest *proof or algorithmic techniques* for suitable linear/dispersive wave models. Applicability to a solid target, driven nonlinear plasma, boundaries, finite pulses and noisy actuators has **not** been shown. QCD/Yang–Mills and ETH claims merit scoped tracking, **not** insertion as experimental fusion gain.
8. **New synthesis worth testing:** optimize expected *qualified collector-input per total cost*, with explicit shot failure/saturation rates and uncertainties, rather than optimizing an idealized total-born-alpha scalar. This could find economically relevant improvements even when the ON–OFF mean change is small, but needs real data.
9. Wall-plug-positive fusion is **not supported** by current reported parameter magnitudes.

## 1. Contributor and provenance register

| Contributor/source | Attributed contributions | Verified boundary |
|---|---|---|
| **Gemini Argon** | Initial executable WP-B v0.1 catcher/alpha-escape surrogate and preserved CSVs; reported subsequent v0.2 and v0.3 OFAT, resonance, stopping, correlated-alpha, acoustic and collector scenarios; 4π vs rear optimum distinction. | v0.1 archive is preserved; v0.3 pasted file lacks claimed full simulation. Numeric claims are **reported**, not experimentally calibrated or end-to-end reproduced. |
| **Copilot Researcher** | Nuclear frame/source critique, need for three-alpha correlated kinematics, detector response, discriminating collector-interface accounting, cross-review; concrete G0-B blinded proton-transmission/alpha-escape protocol and validation lockfile. | Protocol is DRAFT, not preregistered or experimentally executed. Some original Copilot OneDrive spreadsheet sources unavailable. |
| **DeepSeek** | Acoustic timing and target preparation, isotope/lifecycle critiques, silicon/diamond/SiC detector branches, deposition vs printing, supported film comparisons, tungsten/DEC, spin and Bayesian tuning with hard caveats; support-orientation and ^11B areal-atom-matching controls. | Attributed review/digest and literature leads, not instrument qualification or observed effect. Not all underlying review prose retained verbatim in repository. |
| **ChatGPT / Tidal Lantern** | Source/reference checking, 675-keV LAB convention reconciliation, static/numeric v0.3 code audit, governance of source grades, randomized reference/OFF/SHAM/ON causal design, boundary-by-boundary uncertainty and energy ledger, preservation/lineage protocol; cross-domain synthesis in this paper. | No claim that missing model modules or unavailable EXFOR/BN calibration tables were magically executed or received. |
| **OpenAI, 2026-10-26 announcement** | Claims AI-produced local-smoothing proof all dimensions (with released text and Lean artifact), ETH refutation (with released text and Lean artifact), and QCD/Yang–Mills-related constructive existence results (physics workgroup shepherding, AI artifacts held pending interpretation). | These are statements in OpenAI's primary announcement; independent academic assessment, proof applicability and physical consequences require further work. They are **not** Stars contributors or evidence of acoustic/nuclear gain. |

Primary previous version: [v0.8](STARS_2_0_v0_8_REFERENCE_DATA_CALIBRATION_AND_INTERFACE_VALIDATION_2026-10-27.md). Reference preservation: [artifact manifest](../ARTIFACT_MANIFEST_2026-10-27.md). Original collaborator views must remain separately attributed.

## 2. Physics scope, conventions and source gates

Fundamental channel: ^1H (bare incident proton) + ^11B → 3 ^4He, **Q ≈ 8.68 MeV**. Neither a deuteron-beam reaction nor an acoustic change to the strong nuclear force is proposed.

**Laboratory-to-CM** for stationary ^11B:
\[
E_{\mathrm{CM}}=E_{p,\mathrm{lab}}\frac{m_{^{11}B}}{m_{^{11}B}+m_p}\simeq 0.91616E_{p,\mathrm{lab}}.
\]
The **675 keV LAB feature ≈618.4 keV CM**. Do not reassign the literature's 675 keV LAB feature to 675 keV CM (~736.8 keV LAB). Nuclear spin/parity and entrance-/exit-channel partial waves must be cited to exact source and level/channel, independently checked before embedding in generator code.

Scientific anchors: Stave et al. (2011) https://doi.org/10.1016/j.physletb.2010.12.015 ; Sikora & Weller (2016) https://doi.org/10.1007/s10894-016-0069-y ; Mazzucconi et al. (2025) https://doi.org/10.1140/epja/s10050-025-01589-3 ; 2026 experimental preprint https://arxiv.org/abs/2609.33483 . All source-derived resonance amplitudes, branches and cross sections require traceable original data rather than a guessed Lorentzian.

**Prerequisite source acquisition:**
- Nuclear differential and integrated reaction observables, threshold/resonance data, uncertainties, energy frame and experiment IDs from IAEA [EXFOR](https://github.com/IAEA-NDS/exfor_master) or equivalent primary measurements.
- ^11B isotopic enrichment; BN/B/B4C density, porosity, actual surface chemistry, layer orientation, support thickness; cross-validated stopping and straggling for *real material states*, not a smooth function merely named “ICRU49.”
- Incident proton energy–angle–time distribution with covariance, laser energy, source stability and shot IDs.
- Independently measured detector efficiency, angle, threshold, species recognition, dead layers, EMP artifacts and pileup.
- Experimental fitting training/holdout separation; a version-pinned source registry and a machine-readable provenance lock.

A Python [EXFOR integration scaffold](../wp_b/revised/iaea_exfor_pipeline/README.md) exists, but **live source-data calibration remains unverified**.

## 3. Four Gemini Argon v0.3 reported OFAT corrections — explicitly UNREPRODUCED

User-supplied round-four report (not full runnable code) gives these *model-reported* rear-face thickness maxima:

| Stage | Proposed change from earlier stage | Reported rear-optimal thickness | Reported rear escaping energy |
|---|---|---:|---:|
| 0 | Archival surrogate | 4.5 μm | 0.403059 μJ |
| 1 | LAB resonance correction | 4.5 μm | 0.412364 μJ |
| 2 | High-energy cross-section background damping | 4.0 μm | 0.131427 μJ |
| 3 | Smooth stopping/CSDA revision | 4.5 μm | 0.140252 μJ |
| 4 | Claimed correlated alpha CM→LAB kinematics | **5.5 μm** | **0.172942 μJ** |

Stage 4 separately reports total two-face optimum at **6 μm**, 0.335129 μJ. The report claims an altered front/rear asymmetry; *that is particularly sensitive to source anisotropy, correlated three-alpha momentum, detector acceptance, layer placement and substrate orientation*. The reported rear/front ratio at 4.5 μm rose from 0.851 to 1.155. Do not interpret as experimental asymmetry.

**Important mathematical issue:** the three alphas originate from a constrained **single nuclear event**, potentially via excited ^12C and sequential ^8Be decay channels. Independently sampling three isotropic energies can break event-level momentum conservation and angle-energy correlation. Require per-event four-momentum residual with explicit numerical tolerances, conserved baryon number/charge, sampled channel probabilities and frame transformations, plus test fixtures.

**Code audit result:** [v0.3 pasted-module audit](../reviews/GEMINI_V03_PASTED_MODULE_CODE_AUDIT_2026-10-27.md) independently recovered spot values for its formulas (e.g., 675 keV LAB → 618.406 keV CM and reported stopping/range numbers) but identified missing event-generator, OFAT, detector and acoustic Monte Carlo implementations. **CODE-SPOT-CHECKED / NOT REPRODUCED / NOT CALIBRATED / NOT VALIDATED**.

## 4. DeepSeek's manufacturable G0 target comparison

Keep the laser **pitcher**, boron-rich **catcher reaction film**, and **holder/substrate** distinct. Compare three prospective arms at measured matched areal ^11B atoms/cm²:

A. Free-standing/minimally supported film or foil, with unavoidable supports still characterized.
B. Deposited film on a thick dense substrate; account for alpha attenuation and transmission of the incoming proton beam and explicitly reverse/record film orientation.
C. Printed holder/frame/membrane plus separately fabricated deposited film; distinguish obstructed exit cones, batch reproducibility and survivability.

Optional D: a graded/porous structure only after A–C baseline data exist, with fixed areal atom counts and physically characterized density profile.

**New derived cross-check:** comparisons based on geometric micrometres alone conflate isotope inventory, stopping, support shielding and void fraction. Source-normalized alpha exit **per ^11B areal atom**, with actual beam transport and spectra, is more informative; retaining a separate source-energy normalization prevents apparent efficiency from selective detector acceptance. All are denominators, not arbitrary correction multipliers.

DeepSeek's detector proposals: diamond and SiC compared against particle-identifying silicon ΔE–E, CR-39, TPS, calibrated proton diagnostics, and live EMP qualification. Spin/polarization, tungsten high-voltage grids, isotope transmutation and Bayesian tuning stay parallel exploratory branches until hardware-grounded.

DeepSeek docs: [engineering audit](../reviews/DEEPSEEK_V08_CROSS_DOMAIN_ENGINEERING_AUDIT_2026-10-27.md), [hybrid fabrication follow-up](../reviews/DEEPSEEK_V08_HYBRID_BORON_TARGET_FABRICATION_FOLLOWUP_2026-10-27.md), [three-target protocol](../reviews/DEEPSEEK_G0B_THREE_TARGET_SUBSTRATE_COMPARISON_PROTOCOL_2026-10-27.md).

## 5. Acoustic intervention: causal experimental design, not hidden physics multiplier

Four preregistered, randomized and blocked arms:
- **REFERENCE:** no actuator installed; captures physical geometry difference.
- **OFF:** actuator hardware installed but no drive; isolates mechanical assembly effect.
- **SHAM:** equivalent electrical/heating/EMP actuation without target-relevant coherent phase shaping, empirically verify sham contrast.
- **ON:** specified frequency–phase–amplitude–delay actuation, measured at target.

Record mediator distributions (geometry, acoustic displacement, thermal state, prepulse/plasma state, proton E/angle/timing). **First estimate total ON vs OFF/SHAM effect**. Then investigate mediators with appropriately qualified conditional or mechanistic designs; do not match on post-treatment variables and present it as an unbiased total effect.

Gemini's illustrative Monte Carlo claims, N=250/arm with seed 20261027, at 4.5 μm: OFF 0.1700 μJ mean rear escaping energy (CV 18.6%), SHAM 0.1678 μJ (CV ~19%), ON 0.2761 μJ (CV 5%), actuator 15 mJ per SHAM/ON shot. **These differences are programmed into an unverified model and cannot be treated as experimental evidence**. Their magnitude and precision require the full execution path and mechanism-backed actuation parameters.

Two separate scoreboards:
1. **Physics**: escaping/collector-accepted alpha kinetic energy per measured incoming proton distribution; measured causal mean difference and uncertainty; measured dispersion/jitter.
2. **Operations/value**: fraction of *qualified* shots, detector usable/saturation limits, statistical confidence per facility hour, diagnostic repeatability, target survivability, material throughput, downtime and **cost per qualified shot**. A reduction in variability can have substantial non-energy benefits even if mean alpha energy is unchanged. The 15 mJ acoustic input must still be in the whole-system electrical ledger for any electricity claim.

## 6. G3 collectors and falsifiable system ledger

For every event/shot distinguish:
\[
E_{\alpha,\mathrm{born}}\to E_{\alpha,\mathrm{escaping}}\to E_{\alpha,\mathrm{accepted}}\to E_{\mathrm{load,gross}}\to E_{\mathrm{load,net}}.
\]
Do not equate born particles, measured detector counts, rear-exit energy or alpha collection with recovered electricity.

Gemini's reported **100 mJ separate alpha beam** benchmark (assumed portfolio parameters; NOT measured):
| Architecture | Assumed capture | Assumed conversion of captured | Gross from 100 mJ | Local auxiliary | Local net |
|---|---:|---:|---:|---:|---:|
| C1 electrostatic | 78% | 68.5% | 53.43 mJ | 4.20 mJ | 49.23 mJ |
| C2 ion-Bernstein/wave | 42% | 38% | 15.96 mJ | 14.00 mJ | 1.96 mJ |
| C3 hybrid | 78% | 73% | 56.94 mJ | 6.80 mJ | 50.14 mJ |
| C4 inductive | 64% | 44% | 28.16 mJ | 31.50 mJ | −3.34 mJ |

These local margins **do not transfer** to the reported ~0.172942 μJ rear catcher energy at fixed auxiliaries. For example, C1's assumed gross fraction 0.5343 yields ~0.0924 μJ gross per reported rear-energy event, still **many orders of magnitude below** 4.2 mJ local auxiliary if that per-shot charge applies. Duty-cycle amortization and collector physical scaling must be explicitly measured, not guessed.

Whole-system illustrative laser ledger: if 0.6 J optical laser energy with assumed 8% laser efficiency, laser wall input is 7.5 J. Adding assumed services 0.85 J and ON actuation 0.015 J yields **8.365 J wall input** before other costs. No current model output approaches positive wall-plug balance. **Never substitute a 100 mJ benchmark beam for the sub-microjoule modeled Stars alpha plume**.

C1 electrostatic, C2 ion-wave, C3 hybrid and C4 inductive should be experimentally tested on calibrated alpha/ion sources with space-charge, electron suppression, breakdown, plume divergence, energy spread, hardware durability and full auxiliaries. Down-select by *measured useful output and uncertainty*, not assumed percentage rank.

## 7. NEW 2026-10-26 OpenAI scientific announcement: precise relationship

Primary source: [Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities/), OpenAI, October 26, 2026. **These are OpenAI's reported model results undergoing a range of expert follow-up and different release strategies, not independent verification performed by this team.**

### 7.1 Harmonic analysis — local smoothing, Kakeya, Stein restriction

OpenAI reports a model-produced proof of the **local smoothing conjecture in every dimension**, with a novel auxiliary PDE, and says natural-language output and a Lean proof have been released. It describes exceptional wave focusing as short-lived relative to typical-time behavior; implications include Kakeya and Stein restriction problems. *Mathematical local smoothing* is not synonymous with **material acoustics**, radio-frequency ion cyclotron dynamics, laser pulse propagation, or the colloquial sense of musical harmonics.

**Candidate mathematical bridge (our synthesis, not OpenAI's claim):**
- First identify an actual wave equation and geometry in a relevant Stars subsystem: e.g., linearized elastic surface wave in a support or small-amplitude acoustics in a characterized pre-shot material.
- Prove or numerically verify the equation's assumptions (linearity, dispersion, boundary conditions, anisotropy, coefficients, dimensions, regularity). Determine whether local-smoothing inequalities for the source problem even apply.
- Test time-integrated concentration and peak-versus-typical intensity using independent high-bandwidth displacement and phase measurements; compare with conventional energy estimates and numerical simulation baselines.
- Only if a valid bound/model arises, ask whether it constrains actuator parameter sweeps, transient hot spots, sensitivity or shot stability. There is **no direct inference** from the announced proof to an increase in p–^11B reaction rate.

**Failure criteria:** no applicable PDE class; no measurable wave-field link to the source/catcher; estimated bounds noninformative; simpler wave analysis performs equally well; effect disappears under sham control.

### 7.2 Complexity theory — ETH

The same announcement reports an AI-generated **refutation of the Exponential Time Hypothesis (ETH)** with released natural-language and Lean artifacts and an external expert working group. This is **not P≠NP or P=NP** and does not make combinatorial design spaces computationally easy by itself. Track whether later constructive algorithms improve optimization or proof search; do not change computational complexity assumptions in G0/G1 planning on a headline alone.

### 7.3 QCD/Yang–Mills mathematical existence

OpenAI reports model-produced constructive existence proofs in four-dimensional quantum field theory, including QCD/Yang–Mills-related results, now being handled by a group led by David Gross. The announcement says the **physics AI artifacts are initially withheld** at the working group's request. This is a **foundational, long-horizon theory watch**, not a reaction-specific evaluated cross section or empirical detector spectrum. Nothing reported permits substituting a universal-QCD proof for EXFOR records, detailed ^12C/^8Be nuclear spectroscopy, or experiment.

**Source-status note:** A Lean formalization supports checking a theorem relative to its definitions, axioms and trusted formal system, but it does not automatically supply the physical relevance, claimed empirical consequences or independent explanatory understanding. Treat all three announcement tracks as **lead sources with differing accessibility and verification status**.

## 8. New cross-model synthesis: where the genuinely high-value hypotheses are

### S1 — Quality-adjusted alpha interface, not peak counts
Define an endpoint that does not hide failure rates:
\[
U = \frac{\sum_{s\in\mathcal{Q}}E_{\alpha,\mathrm{collector-accepted},s}}
{\sum_{s\in\mathrm{all}} C_{\mathrm{facility},s}},
\]
where \(\mathcal{Q}\) is a **pre-specified** set of qualified shots and the cost denominator includes all attempted shots, failures, diagnostics and actuation. Report *also* unconditional mean exit energy, not just selected successful shots. Use the same frozen qualification criteria for all arms. This could reveal a valuable increase in reproducibility without falsely claiming nuclear yield enhancement.

### S2 — Geometry × correlated spectra × collector acceptance interaction
The thickness optimum can shift when maximizing **accepted** rather than **escaping** alpha energy: the collector has a real energy-angle-charge-phase-space window. Integrate the same correlated 3-alpha events through material, detector, and acceptance; independently calibrate collector on its actually received distribution. **Prediction to falsify:** an apparent two-face exit maximum need not maximize collector acceptance, and a lower-output but narrower-spectrum geometry can win on usable output.

### S3 — Matched boron inventory and support topology
With the **same incident proton distribution and total ^11B atoms/cm²**, compare support-free, dense-backed and supported-film layouts, including both orientations. Require one fixed model to predict all configurations *before unblinding*. This disentangles a geometric “micron optimum” from practical fabrication and hidden shielding effects.

### S4 — Frequency-domain preparation and causal timing
If actuated catcher preparation is real, mechanism should appear **before** changes in fusion outcome: measure actuator phase/target displacement, temperature, morphology or proton source mediator at appropriate timestamps. Design negative-control frequencies, phase scrambling and matched electrical load. If ON effects occur with no corresponding measured physical mediator, treat as anomaly needing diagnostic review rather than a claim of nuclear-force resonance.

### S5 — Alpha source uncertainty allocation before ambitious hardware investment
Use sensitivity analysis for nuclear cross sections/branches, beam E-angle distributions, stopping, straggling, support obstruction and detector response. Fund/source-check the highest **decision-changing uncertainty**, not the most glamorous collector first. A cross-model agreement among agents reusing assumptions is not independent evidence.

### S6 — Proof-aware scientific Alexandria link, future lane
Index each external proof claim by theorem statement, hypothesis, proof artifact/hash, verifier status, expert review, and relationship to a physically validated governing equation. Separate **mathematical proof**, **numerical prediction**, **experimental observation**, and **engineering performance** as non-substitutable evidence types. SHUGS/HSN is a research index candidate, **not** proof that a twelvefold physical symmetry governs p–^11B.

## 9. Pre-simulation freeze contract

Before an independently labeled **WP-B v0.4 reproducible run**, require:
1. Full Python source that actually calls OFAT, correlated event generation, detector forward model, acoustic controls and collector score; dependency lock and source/file hashes.
2. Measured/source-identified p–^11B cross sections and level/branch tables with energy reference frame, uncertainty, and source status. Retain a separate **surrogate-only run** if primary-data import is still unavailable.
3. Source-qualified proton/He transport in specific material stacks; energy conservation tests and event-by-event 3-alpha momentum conservation.
4. Common initial incident proton ensembles for controlled OFAT/arm comparisons; deterministic seeds, unit tests and checksums.
5. Thickness scan including both faces and detector-normalized spectra, transmitted protons, uncertainty bands and threshold/geometry variation.
6. Four-arm REFERENCE/OFF/SHAM/ON simulations with **explicit hypothesized mechanism** and energy/time cost, not arbitrary ON output multipliers masquerading as evidence.
7. G3 calibrated source-matching test and full wall-power ledger with explicit allocation of pulsed vs standby utilities.
8. G0-B blind experimental lockfile after independent instrument calibration, predicted acceptance criteria and external custodians; **simulation is not experiment**.
9. Null models: no resonance correction, independent isotropic alpha strawman, no acoustic effect, support-only substrate, shuffled phases and no collector. A method that fails to beat a simple null is not promoted.
10. Append-only ancestry: freeze the prior incorrect-frame, incorrect-stop or null-effect runs as negative findings rather than silently overwriting them.

**Evidence grade ladder:** REPORTED → CODE-SPOT-CHECKED → SOURCE-TRACED → SOURCE-REPRODUCED → CALIBRATED → BLIND-VALIDATED. These are distinct gates, not merely incremental confidence adjectives.

### Simulation output checklist
- Machine-readable *per shot and per event* records, frozen scripts and dependency environment, SHA-256 digest manifest.
- Plot/table A: nuclear cross-section by exact original LAB and CM labels + source uncertainty.
- B: incident/transmitted protons, stopping/range and layer stack.
- C: 3-alpha correlated birth and four-momentum residual histograms.
- D: front/rear/side exit spectra, detector-folded counts vs corrected inference.
- E: sensitivity of optima to thickness, isotope/areal inventory, support and collection acceptance.
- F: randomized ON/OFF/SHAM/reference contrasts for mean, variance and qualified-shot yield.
- G: optical→laser electrical→aux→alpha exit→captured→load full energy/accounting ledger.
- H: model failures, negative controls and unresolved source mismatches.

## 10. Explicit stop signs and authorial conclusion

STOP if full source cannot regenerate the stated tables; if imported reference records lack provenance; if momentum or energy residual exceeds locked tolerances; if detector calibration fails; if sham cannot be differentiated from ON; if target state cannot be characterized; if positive collected net energy is inferred by omitting the laser/actuator/services; or if a post-hoc tuned optimum is promoted to blind validation.

**Scientific conclusion:** Stars 2.0 is at a potentially valuable *model-calibration and discriminating experiment* stage. The strongest actionable synergies combine Copilot's frame/event/detector disciplines, DeepSeek's practical support/fabrication and diagnostics, Gemini's falsifiable thickness/collector/acoustic surrogates, and ChatGPT's causal design, independent audits, scoreboards, and source lineage. OpenAI's October 26 harmonic-analysis announcement justifies a sharply bounded wave-PDE methods watch—not a fusion success claim. There is no demonstrated net-electric return and no verified acoustic enhancement yet.

**Research ethic:** Reality may defeat a wizard, but it cannot delete their commit history.

## 11. Linked source and review shelf

- [v0.8 integrated reference/calibration white paper](STARS_2_0_v0_8_REFERENCE_DATA_CALIBRATION_AND_INTERFACE_VALIDATION_2026-10-27.md)
- [v0.3 partial-module numerical audit](../reviews/GEMINI_V03_PASTED_MODULE_CODE_AUDIT_2026-10-27.md)
- [DeepSeek v0.8 independent engineering review](../reviews/DEEPSEEK_V08_CROSS_DOMAIN_ENGINEERING_AUDIT_2026-10-27.md)
- [DeepSeek hybrid boron fabrication](../reviews/DEEPSEEK_V08_HYBRID_BORON_TARGET_FABRICATION_FOLLOWUP_2026-10-27.md)
- [DeepSeek blinded three-target proposal](../reviews/DEEPSEEK_G0B_THREE_TARGET_SUBSTRATE_COMPARISON_PROTOCOL_2026-10-27.md)
- [Copilot-inspired G0-B blind protocol](../protocols/G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md)
- [G0-B lockfile README](../protocols/g0_b_lock/README.md)
- [Atlas source/lineage README](../../lineage/README.md)
- [OpenAI October 26, 2026 announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/)
- [IAEA EXFOR master](https://github.com/IAEA-NDS/exfor_master)
- [Primary experimental refs: Stave](https://doi.org/10.1016/j.physletb.2010.12.015), [Sikora–Weller](https://doi.org/10.1007/s10894-016-0069-y), [Mazzucconi](https://doi.org/10.1140/epja/s10050-025-01589-3)

---
**End v0.9. Next phase: reproduce and audit a complete simulation before interpreting improvements.**
