# STARS 2.0 v0.7 — Acoustic A/B, Alpha Escape, Converter Reality and Multi-Agent Falsification
## An Integrated Pitcher–Catcher–Collector Research White Paper
**Atlas Lattice / Open Regenerative Compute Standard (ORCS) | 27 October 2026**

**Research status:** Exploratory, noncanonical, and explicitly NOT a demonstrated net-electric p–¹¹B reactor.
**Motto:** *Receipts in the front, wizards in the back.*
**Project direction:** Dave Sheldon / Atlas Lattice.
**Contribution and review provenance:** Gemini Argon (cross-domain hypothesis generation, original and revised WP-B modeling and its reported outputs); DeepSeek (literature synthesis, engineering sequencing, target lifecycle and reviewer questions); Copilot Researcher Mode (adversarial transport/collection/software audit, surrogate sensitivity and converter-evidence scrutiny); ChatGPT / Tidal Lantern (integrated physics/evidence analysis, causal A/B protocol, conservation boundaries, source-claim qualifications, archival synthesis). Attribution describes roles, not independent confirmation or formal coauthorship. All claims of numerical validation refer to particular named tests only.

**Prior papers / archive:** [v0.2](STARS_2_0_RF_v0_2_updated_whitepaper.md); [v0.3](../../stars-2-0-modular-pb11-acousto-optical-energy-conversion-whitepaper-v0.3-2026-10-27.md); [v0.4](../../stars-2-0-modular-pb11-electroacoustic-alpha-recovery-whitepaper-v0.4-2026-10-27.md); [v0.5](../../stars-2-0-v0.5-evidence-integration-2026-10-27.md); [v0.6](STARS_2_0_v0_6_WP_B_AUDIT_AND_INTEGRATED_RESEARCH_WHITEPAPER_2026-10-27.md); [artifact manifest](../ARTIFACT_MANIFEST_2026-10-27.md). This document adds evidence and experimental design without replacing earlier records.

---

# Executive findings (read before hypotheses)

**E1 — Demonstration is not reactor gain.** The p + ¹¹B → 3 α reaction releases ~8.68 MeV Q per event. Recent experiments demonstrate repeatable laser-driven proton-boron alpha sources and geometry sensitivity, not electrically self-sustaining fusion.

**E2 — Target escape is central.** Fusion reactions deep in a solid catcher can produce alphas that deposit their kinetic energy in that catcher rather than reach an external converter. Target thickness, reaction-depth profile, angular distribution, alpha stopping and collection topology must therefore be optimized jointly. Maximizing fusion births is not equivalent to maximizing electrical output.

**E3 — A single 5 µm optimum is not established.** Gemini Argon's WP-B v0.1 surrogate sampled a two-face escaping-energy maximum at 5 µm. Its reported v0.2 model yields 5 µm rear-energy and 6 µm two-face energy maxima under revised *assumed* stopping and other parameters. Copilot's adversarial surrogate test instead found broad, collector-dependent spans: approximately 3.25–6.75 µm for its dual-face 5th–95th percentile stress bracket, and 2.50–5.25 µm rear-only. These are **not statistical confidence intervals, experimentally measured peaks or independently validated transport predictions**.

**E4 — Acoustic shaping remains a central, testable hypothesis.** Acoustic or electroacoustic methods might reproducibly set droplet/sheet thickness, local target shape, roughness, alignment, surface modulation or source consistency **before** picosecond laser arrival. There is presently no demonstrated p–¹¹B yield or net-electric enhancement specifically attributable to this method in this architecture. Neither enthusiasm nor skepticism should be substituted for the necessary randomized **acoustic OFF / SHAM / ON** experiment. The total acoustic benefit can be *mediated by a changed proton spectrum*. Conditioning on that spectrum may remove a residual direct effect **without negating a real total benefit**.

**E5 — Converter transferability is unresolved.** ENN's >80% direct electrostatic conversion demonstration concerns a controlled low-energy charged-particle apparatus, not broad MeV fusion alpha exhaust. Copilot's source-specific review reports roughly 390 eV argon, near 20 mA and ~82% under a measured beam-power denominator; verify these particulars in the complete primary methods before setting simulator parameters. Collection acceptance, pulse current, space charge, electron neutralization, grid losses and power-conditioning are distinct from single-unit efficiency.

**E6 — IBW is not SBS and wave power is not electrical power.** Qin–Fisch's 99.96% is an idealized linear kinetic-model partition of alpha-energy loss into coherent proton ion-Bernstein-wave response, **not** recovery at a load; it is not an ordinary acoustic or laser-SBS ion-acoustic result. Independently test alpha-origin energy transfer and its eventual electrical outlet using matched beam/RF controls.

**E7 — The current audited code is still a surrogate.** A reported Gemini WP-B v0.2 revision includes front/rear escape and conservation identities, but retains phenomenological cross sections, fitted stopping, surrogate alpha decay, and assumed scalar converter acceptance. Passing built-in balance equations does not validate the physics. Original v0.1 code and CSVs are preserved; the v0.2 revised source was displayed in chat but **has not been independently executed as a preserved standalone GitHub script** at this checkpoint.

**E8 — Total energy and material cost are the gate.** A wall-to-load calculation must include laser, acoustic driver, ion/source preparation, magnets, vacuum, cooling, target feed, isotopic processing if used, controls, failed shots, power conditioning and maintenance. Embodied lifecycle energy is a separate disclosed boundary to avoid confusing it with facility wall-plug input. Natural boron is ~80.1% ¹¹B, so enriched-boron assumptions require explicit justification.

# 1. Explicit architecture and physical boundaries

The research program tests:

```text
 PRE-SHOT TARGET STATE  [Acoustic OFF | SHAM | ON]  ← G1-A
      | measured thickness/roughness/position/phase
      v
 CHARACTERIZED LASER / PROTON PITCHER              ← G1-P
      | d²N_p / dE dΩ ; energy/pulse
      v
 BORON-11 CATCHER  [thickness, phase, composition]  ← WP-B / G1-B
      | fusion births and proton passage
      +--> Unreacted protons [out / thermalized / recovered]
      +--> Alpha born at depth x: d³Nα / dE dΩ dx
                 | alpha slowing and attenuation
                 +--> front escape  +--> rear escape  +--> lateral exit
                 +--> deposited target heat
                          |
                TRANSPORT / SEPARATION               ← WP-D
                          |
                 DEC / hybrid / IBW experiments      ← G3-A
                          |
                    ELECTRICAL LOAD
                          |
                 storage / reuse / export             ← G5
```

The reaction is (^{1}H^+ + ^{11}B \to 3 ^{4}He^{2+}\), with fusion Q approximately 8.68 MeV. The reaction is a sequence of nuclear processes including ¹²C* resonances and ⁸Be channels; three equal monoenergetic alphas is an incorrect transport source. Incoming proton kinetic energy also contributes to outgoing product energy; full lab-frame distributions are needed, not only Q.

The **magnetic** force can change alpha direction but a static magnetic field does not perform work on its moving charge. Electrostatic retardation or time-dependent collective wave interactions can exchange kinetic energy. An ionized alpha's spin-zero nuclear ground state is not a useful protected quantum-energy store. Hypothetical ²⁸Si/¹³C DNP preparation of polarized ¹¹B and/or ¹H remains a separate, unverified research lane, distinct from collecting alpha kinetic energy.

No module is entitled to multiply independent gains of (f_{acoustic} f_{spin} f_{wave} f_{resonance}) without an experimentally measured interaction model. Measured efficiency requires an explicit denominator and source boundary.

# 2. Primary-source register, and issues not yet reconciled

| Evidence | What it supports | What it does **not** prove |
|---|---|---|
| Popper et al. (2026), arXiv:2609.33483 | Replenishable water-leaf laser proton pitcher; 10 Hz for 18,000 shots; boron nitride catcher; alpha spectra affected by depth-dependent reaction/stopping | Continuous catcher renewal, high alpha electrical recovery or power-positive fusion |
| Mazzucconi et al. (2025), EPJ A 61:114 | Experimental energy-dependent cross-section and alpha spectra with silicon-telescope particle identification | That a single-angle differential cross section is a total cross section, or that the WP-B Lorentzian fit is validated |
| Sikora and Weller (2016) evaluation | Experimental/evaluated p–¹¹B data and resonance structure | Literal agreement with arbitrary WP-B penetrability caps and spin multiplier |
| LFEX confined-geometry experiment | Spherical versus planar target changes measured filtered alpha spectral yield; largest ~100× occurs through thick filtering | Universal 100× change in total births or recoverable alpha energy |
| Kong et al. (2026), ENN DEC | >80% under a specified fundamental low-parameter charged-particle test | >80% collection × conversion of high-current, broad, MeV p–¹¹B alphas or net electricity |
| Qin and Fisch (2026), arXiv:2609.07732 | Ion Bernstein wave alpha-cyclotron pole mechanism in idealized plasma and coherent proton response | Electricity, useful thermal heat or measured gain from laser-SBS |
| Ochs et al. (2022), Phys. Rev. E 106, 055215 | Power-balance advantages of prescribed alpha-energy channeling | Demonstrated reactor confinement or net power |
| Gemini Argon WP-B v0.1/v0.2 | Transparent sensitivity prototypes and suggested tests | Calibrated cross sections/stopping/collector efficiencies or experiments |
| Copilot Researcher stress review | Shows possible wide sensitivity of optimum to assumed source and collection face | Experimental uncertainty intervals or validated thickness |
| DeepSeek v0.6 review | Acoustic temporal sequencing, material preparation and cost cautions | Measured acoustic fusion gain or exact ENN ion species without checking methods |

**Reference URLs:**
- https://arxiv.org/abs/2609.33483
- https://link.springer.com/article/10.1140/epja/s10050-025-01589-3
- https://doi.org/10.1007/s10894-016-0069-y
- https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/hydrogen-boron-fusion-in-confined-geometries/D273DDE00ABB65D29D2053845A22A887
- https://doi.org/10.1088/2058-6272/ae445a
- https://arxiv.org/abs/2609.07732
- https://doi.org/10.1103/PhysRevE.106.055215
- https://www.iaea.org/resources/databases/experimental-nuclear-reaction-data
- https://www.nist.gov/pml/stopping-power-range-tables-electrons-protons-and-helium-ions

## 2.1 Important unresolved p–¹¹B resonance-label discrepancy
Earlier Stars papers described a major resonance near **675 keV center-of-mass**, estimating ~736 keV incident laboratory proton energy for stationary boron. Copilot's latest review flags nuclear sources describing a broad prominent feature near **612 keV center-of-mass**, suggesting roughly 668 keV laboratory. The 2025 Mazzucconi paper's abstract says '0.675 MeV resonance peak' without unambiguously establishing the *frame in that isolated sentence*; other papers refer to proton accelerator incident energies. The physically correct conversion remains (E_{cm}\simeq E_{lab}m_B/(m_B+m_p)\simeq 0.916 E_{lab}), but **source conventions and whether different channels/features are being compared must be verified before declaring 736 keV the universal resonance target**.

**Hold point:** Import published nuclear-energy tables with original lab/CM metadata and channel-specific cross sections, display both energy axes, mark peaks *as observed* and reconcile with R-matrix evaluations. Until completed, present 'approximately 675 keV CM / 736 keV lab' as the **earlier working premise subject to audit**, not a finalized design setting. Do not silently substitute a different resonance. The proton pitcher should be assessed over a broad spectrum regardless.

# 3. Independent modeling audit: WP-B v0.1 to reported v0.2

## 3.1 Original v0.1 model and observations
The preserved v0.1 Gemini Argon script generated:
- a depth-resolved but surrogate p–¹¹B birth integral;
- two-component alpha representative energies and a (E_{res}=E_0(1-s/R_0)^{0.65}) stopping approximation;
- a 14-point BN thickness sweep showing a sampled **5 µm** total two-face escaped-energy maximum at approximately **0.7456 µJ**, with **6 µm** highest sampled escaped alpha count;
- a *bundled architecture* acoustic/spin/wave matrix, where acoustic ON changed thickness, efficiency and source spectrum simultaneously; and
- C1/C2/C3 assumed conversion outcomes, **not predictions from field/plasma particle calculations**.

The stopping approximation's own comment claimed ~36 keV/µm at 1 MeV. Independent direct function execution yielded **52.89 keV/µm**. At 75 keV, the code yielded ~90.4 keV/µm. This proves documentation-versus-calculation disagreement, not which number is accurate experimentally.

## 3.2 Gemini Argon reported v0.2 changes
In code supplied in conversation, Gemini added (i) a reparameterized stopping function labeled 'v02 calibrated'; (ii) separate alpha front/rear escape; (iii) proton reactant depletion and explicit birth Q plus proton kinetic energy; (iv) multiple conservation assertions; (v) fixed-thickness factorial scenarios and independent shams; and (vi) a parameterized acoustic-source and electrostatic-collector routine.

Gemini reported sample maxima: rear-only escaped alpha energy at **5.0 µm**, two-face energy at **6.0 µm**, and two-face particle count at **7.0 µm** for its new assumed stopping and source inputs. Those values have **not been reproduced from a standalone WP-B v0.2 committed executable**, and the new stopping formula has no traceable numeric proton/helium BN dataset or published fitting residuals presented in this conversation.

**Independent analysis:** The supplied 'physics-linked' acoustic model still sets empirical ripple/sheath response factors (including assumed gain coefficient 0.85 and sheath factor 0.22), rather than deriving them from measured G1 shots. The supplied 'acceptance weighted' converter **does not actually integrate energy and angle bins**; it applies aggregate alpha-front/rear energy with fixed scalar acceptance and grid loss percentages. Its mean rear alpha energy input is unused. Internal energy-conservation assertions are necessary but **not sufficient** to establish correct reaction probabilities, real alpha phase space, stopping, or engineering performance.

## 3.3 Copilot's adversarial review (latest round)
Copilot Researcher Mode reviewed v0.6 and reported:
- 5 versus 6 µm was only ~1.1% different in original escaped-energy output, consistent with a shallow peak.
- a surrogate stress sweep generated a **dual-face median ~4.62 µm** (5th–95th stress span 3.25–6.75 µm), **rear-only median ~3.75 µm** (2.50–5.25 µm) and **front-only median ~14.75 µm**, the last censored by the chosen upper test boundary. These are *stress distributions*, **not probability-based uncertainty intervals or measurement**.
- data gaps include differential three-body alpha spectra, solid versus hot-target proton/helium transport, collector charge-state and pulse acceptance, source-laser phase space and actual per-shot electricity.
- the LFEX ~100× headline is selective energy-filtered detection rather than total yield.
- an ordinary accelerator proton beam and BN thickness series, with simultaneous front/rear energy-angle spectroscopy, would isolate nuclear transport **before** laser and acoustic confounders.
- acoustic modulation in this architecture lacks a demonstrated fusion-yield causal gain; the appropriate response is blinded randomized ON/OFF matched controls, **not suppressing the experimental branch**.

**Independent corrective analysis of Copilot:** Its proposed rule to 'retire acoustics' whenever the outcome loses a residual effect after conditioning on measured proton spectrum is **too strict as a test of total acoustic value**. Acoustic shaping might change laser coupling or pitcher phase space, leading to more fusion births *entirely through those measured intermediate changes*. Adjusting for the mediator could remove the apparent acoustic coefficient even when the treatment has a physically useful total effect. Register total effect, mediated pathway and residual direct effect separately. Retire an implementation if randomized total effects and physically measured first-stage target/spectrum response fail meaningfully under specified operating conditions and uncertainty bounds.

# 4. Primary design decision — acoustic A/B plus sham, with no foregone outcome

**Hypothesis H-A:** Pre-shot acoustic/electroacoustic excitation produces a reproducible change in the target state at the laser-arrival instant, which may change proton fluence/energy/angular distribution, fusion-born yield, escaped alpha kinetic-energy distribution and possibly converter-delivered electrical work.

**Null:** No reproducible improvement in target state or in relevant normalized system endpoints beyond sham/control variability, with sufficient measurement precision.

### 4.1 Exactly what is randomized
Primary factor **A**: acoustic OFF, acoustic ON, matched acoustic SHAM (matched wall power or electrical/thermal disturbance but without intended coherent mechanical shaping). Record actuator input, physical acoustic power, phase, amplitude, frequency, target-shaping delay, temperature and mechanical jitter. A SHAM is an experimental control, **not** a guaranteed copy of every perturbation; validate that its unintended mechanical effects differ from ON but nonmechanical backgrounds match.

**Geometry G**: planar / spherical / liquid sheet or droplets, with geometry appropriate to each source. Do not pretend that all are interchangeable at an identical areal density without metrology. Nested geometry-by-acoustic comparisons should match *nominal thickness/composition/laser dose*, then measure achieved geometry as an outcome.

**Independent catcher thickness T**: predetermined discrete thicknesses, e.g. a coarse 1–12 µm series, refined only after preregistered primary analysis. Maintain fixed thickness within an initial acoustic A/B block.

**Pitcher and collector BOUNDARIES:** A deployed acoustic system might shape *pitcher*, *catcher* or both; record which, and test independently. Initial easiest claim likely concerns replenished pitcher/droplet preparation, not real-time acoustic modulation of nuclear interactions in a heated catcher.

### 4.2 Sequence and synchronism
```text
target feed established
   → acoustic actuation / target preconditioning
   → independently measured phase + amplitude + target-shape readiness
   → trigger delay Δt (and measured jitter)
   → picosecond laser pulse at t=0
   → time/energy/angular diagnostics of protons and alphas
   → charged-particle acceptance and electrical load integration
   → material/energy accounting + randomized next shot
```
Mechanical acoustic preparation can occur on ns–ms dependent on device, but **the relevant observable is the prepared material state at laser incidence**. Do not assume that a macroscopic sound wave can directly rearrange nuclei during the picosecond fusion event; plasma ion-acoustic or ion Bernstein waves are separate *post-ionization* mechanisms.

### 4.3 Primary and secondary endpoints — causality aware
- **Primary A/B total engineering endpoint:** difference in escaping **alpha energy into the declared collector interface** per measured incident optical laser energy, at fixed catcher geometry and proton-source protocol. This avoids claiming a working electrical converter prematurely.
- **Primary scientific target endpoint:** measured target geometry and proton phase-space response at laser incidence and after pitcher interaction, with uncertainty.
- **Secondary nuclear endpoint:** fusion reactions per incident proton, conditioned on measured energy/angular distributions, to separate interactions from source improvement.
- **Ultimate G5 endpoint:** actual measured **net exported electrical energy** per wall-plug joule including incremental acoustic actuation.
- **Mechanism mediation:** acoustic → morphology/alignment → proton spectrum → depth-resolved fusion births → alpha escape → collector work. Report total randomized contrast **before** and **after** conditioning on the measured proton distribution. Differences describe mediation but do not by themselves uniquely prove each causal link.

Keep reported ON/OFF/SHAM data for each stage, **including null and negative results**. Never encode an assumed 2.8%→4.8% pitcher efficiency change as if a trial measured it. Report actual acoustic amplifier wall power and timing overhead.

### 4.4 Sample experimental design
At a fixed catcher thickness/geometry, use randomly ordered repeated shots in three arms (OFF, ON, SHAM). Record laser pulse fluence/contrast and alignment. Run target-only imaging with no fusion irradiation first. Compare pitcher-only acoustic influence and catcher-only acoustic influence if both use shaping. Measure shot-to-shot drift, target survival and effective target delivery rate. Use synchronized optical profilometry/interferometry, calibrated proton spectrometers, particle-discriminating alpha spectroscopy and actual detector solid-angle calibration. Plan blinded detector analyses where practical.

A physically successful acoustic stage **may**:
- improve target reproducibility or reduce thickness/position variance without increasing mean proton yield;
- increase proton production/shift resonance-window occupancy;
- alter angular distribution or escape energy without increasing *birth* rate;
- fail to produce useful incremental electricity after accounting for transducer power;
- reduce performance. Negative results must be retained.

# 5. Independent nonacoustic control: beam–catcher calibration

A non-laser accelerator beam through a thickness-controlled BN wedge/series is an efficient, clean precursor, **not an alternative that supersedes acoustic testing**. It measures the transport kernel: input proton spectrum/fluence, front and rear alpha differential spectra, surviving proton kinetic energy, target calorimetry and detector efficiencies. A fixed particle beam disentangles stopping/escape from laser variance, then its measurements constrain both acoustic-ON and OFF branches. Experimental uncertainties must cover BN density, porosity, crystalline structure, impurity/isotope mix, non-normal incidence, radiation damage and hot-plasma deviations in later laser shots.

**Source data audit:** Obtain legally reusable data for ¹¹B(p,α) cross sections, channel-specific distributions and proton + helium stopping in actual boron-nitride material. SRIM/TRIM and ICRU references are useful but a comment 'ICRU/SRIM calibrated' without actual tables, fitting residuals, density/composition and license metadata **does not constitute calibration**. NIST PSTAR/ASTAR supports listed materials and may not natively include BN. Use actual traceable imported arrays or documented surrogate uncertainty envelopes. An assertion with residual tolerance 1e−9 on internally balanced arithmetic cannot substitute for external experimental calibration.

# 6. The integrated coupled particle-energy simulator: required WP-B v0.3 contract

Propose a new **audit-ready simulator** (not yet constructed, not claimed to run here). Inputs:
```text
laser E, repetition, measured proton spectrum and its covariance
target acoustic phase/amplitude/timing/metrology at shot
pitcher and catcher geometry; thickness, boron isotope fraction and density
nuclear cross section per lab/CM energy and differential alpha decay distribution
proton + alpha stopping and straggling in BN or actual materials
front/rear/side boundary geometry and measured field topology
collector energy-angle-charge-time acceptance, power electronics
facility and optional embodied preparation/transport/replacement costs
```

**Birth integral (thin-reaction limit):**
```math
N_f ≈ ∫dE₀dΩ₀ [d²N_p/(dE₀dΩ₀)]
           ∫_path n_B(x) σ_pB(E_cm(E_p(x))) dx.
```
For finite reaction probabilities include survival/depletion and competing energy loss. Reaction Q and projectile energy must appear **once** in species-resolved energy conservation.

**Escaping alpha phase space:** Sample conditional three-body (d³N_{α,born}/(dE_α dΩ_α dx)); integrate actual material path lengths and stopping to obtain *separate* front/rear/side exit (Phi_α(E,Ω,t,q)). No fixed three equal-energy alpha assumption; no binary single 9 µm escape cutoff.

**Converter work:**
```math
E_{DC,load} = ∫dt dE dΩ Φ_α(E,Ω,t,q) A(E,Ω,t,q) η_{DEC}(E,Ω,t,q) E .
```
Scalar A_rear=0.82 and eta_stage formula in Gemini v0.2 are **scenario parameters** pending actual WP-D field/beam calibration. Space charge, co-moving electrons, charge exchange, grid field penetration, breakdown and RF feedback may determine viability.

**Shot-level conservation:**
```text
proton + nuclear Q → alphas + surviving outgoing protons
  + target and collector heat + secondary electrons + radiation
  + escaped energetic particles + field energy changes + unresolved
```
Apply species/charge and energy consistency at catcher and converter separately. Distinguish true recoverable heat from target/beamline/chamber deposits outside a designed heat exchanger.

**Electrical export:**
```math
E_net,export = E_load_DC + E_other_export
   - E_laser_wall - E_acoustic_wall - E_RF_wall
   - E_spin_prep_wall - E_magnet/vacuum/cooling/control_wall
   - E_target_op_wall - E_other_aux_wall .
```
Add separately a **life-cycle/embodied-energy** accounting column (fabrication, isotopic separation when selected, target feedstock and disposal, material transport) and declare which pieces already appear as measured facility electricity so they are never counted twice. Account for failed shots and repetition rate. Internal energy reused in later shots may offset future draws but is not simultaneous **export**.

**Comparative output table (each acoustic arm × thickness × collector topology):**
```text
shot_id, protocol_id, acoustic_condition, actual_target_state,
laser_wall_J, acoustic_wall_J, N_protons, proton_spectrum,
N_fusion, alpha_birth_E_J, alpha_exit_front_E_J,
alpha_exit_rear_E_J, alpha_accepted_E_J, DC_load_E_J,
recoverable_heat_J, uncollected_E_J, net_export_J,
uncertainty, data_provenance, model_version
```

# 7. Branches retained without artificial multipliers

## G3-A direct electrostatic conversion
Start with an independently measured charged-particle beam and separately measured electrical load. Compare C1 electrostatic, C2 wave, C3 hybrid **on identical alpha energy/angle/time distributions**. The ENN low-energy unit result is a calibration *lead*, not an efficiency input for MeV broad beams until geometry and operating regime match. Beam-test gains must report alpha injector/accelerator costs separately if a system-level claim is contemplated.

## G3-A IBW / coherent recovery
Qin–Fisch's pole resonance couples alpha dynamics to coherent proton IBW in idealized magnetized plasma; the original model's 99.96% number is not a usable conversion efficiency. Optical SBS, ion-acoustic density waves, and magnetized ion Bernstein waves must not be conflated. In any experiment separate externally injected seed energy, reflected RF/impedance changes, coherent alpha-origin response, electron heating and actual load electricity. A zero-seed experiment is useful but background plasma/beam energy other than alpha must still be audited.

## P0–P5 spin and materials
Retain nuclear-spin ideas in a distinct roadmap: original spin-dependent reaction theory; actual polarization of boron/protons; material construction and lifetime; survival under pre-pulse and irradiation; measured angular/energy-resolved yield; integration only if validated. Stable ²⁸Si or ¹³C NMR coherence in other hosts does not prove ¹¹B/¹H polarization survives relevant laser events.

# 8. Decision gates: named negative results

| Gate | Positive observation needed | Clear negative/downgrade |
|---|---|---|
| C0 nuclear/transport | Measured thickness-resolved front/rear alpha spectra match predeclared transport model within uncertainty | No pre-registered stopping/escape kernel reproduces data |
| A1 acoustic material | Reproducible change in material state at laser arrival, beyond sham | No measurable target-state change at meaningful amplitude/timing |
| A2 acoustic proton | Stable total proton yield/spectrum improvement or useful reduction in jitter at equal laser power | No overall response after appropriate randomized trials |
| A3 acoustic alpha | Measured alpha-interface energy improves on OFF/SHAM with consistent causal measurements | No improvement within engineering cost/reliability bounds |
| A4 acoustic electricity | Incremental electricity at load > incremental acoustic cost under comparable boundary | Extra acoustic energy exceeds recovered gain |
| DEC | Measured pulsed He²⁺ collector efficiency and stable fields at actual particle phase-space | Required acceptance×conversion or electrical stability not reached |
| IBW | Alpha-specific wave transfer and real incremental load output after drive | No attributable mode/load energy within measurement resolution |
| Spin | Measured ¹¹B/proton target polarization survives shot and changes normalized nuclear observable | Depolarization or no measurable channel-dependent yield |
| G5 plant | Reproducible positive net electrical output with uncertainty and full auxiliaries | Negative net balance under credible optimized operating envelope |

**Retirement must name its tested design, diagnostic sensitivity and parameter region.** A failed acoustic actuator at one frequency does not disprove the general existence of target shaping. A failed wave mechanism in one magnetized regime does not disprove all collective plasma effects. Conversely, repeated unvalidated scenario gains are not evidence that a positive result exists.

# 9. Reviewer-specific requests for round 4

### DeepSeek — engineering and data sourcing
1. Identify original datasets or permissible exports for BN proton and helium stopping, with state/density/charge, experimental-vs-derived labels and error estimates.
2. Audit acoustic pre-shot shaping (SAW/ultrasound, water-leaf or droplet devices): attainable profile amplitude, frequency, phase stability, timing, heat, transducer lifetime, shot-level evidence.
3. Trace isotope separation and target preparation/fuel lifecycle at natural (~80% ¹¹B) versus 99% enriched boron under liquid, sheet and solid catchers.
4. Check LFEX diagnostic response and ENN test beam species/energy/efficiency from primary full methods.

### Gemini Argon — simulation refactor and mechanisms
5. Supply complete **WP-B v0.2 .py** and generated tables as versioned standalone files with verified reproduction command, plus actual BN data sources for stopping calibration.
6. Replace scalar DEC acceptance with energy-angle-time-charge bins and measured/reference acceptance boundaries.
7. Run acoustic OFF / ON / SHAM **with measured-input columns** and explicit ranges for unverified ripple and preplasma coefficients; present scenario uncertainty without claiming empirical gain.
8. Resolve reported rear/dual optimum differences across v0.1, v0.2 and Copilot stress cases using identical inputs and geometry.
9. Specify plasma conditions enabling IBW coupling for a realistic pulsed alpha phase space; report whether it produces extra electricity, not just coherent proton response.

### Copilot Researcher — adversarial verification
10. Independently check resonance metadata: which papers specify 612 keV CM versus 675 keV, and which provide explicit lab-beam proton energies or channel-specific peaks?
11. Review total-versus-mediated acoustic benefit; propose controls that cannot falsely reject acoustic improvement operating via modified proton production.
12. Provide versioned stress-test code/seeds and uncertainty *semantics* for its 3.25–6.75 µm dual-face and 2.50–5.25 µm rear-face spans.
13. Prioritize realistic sequential alpha decay + helium stopping / range-energy curve replacement and quantify impact on face-specific optimum.
14. Independently audit the claimed ENN argon 390 eV / 20 mA / ~82% apparatus, exact efficiency denominator and extrapolation limits.

### Joint challenge
15. Each reviewer supplies **one source-backed independent success, one strongest contrary result, one unmeasured parameter that could flip the conclusion, and one preregisterable test**. Preserve dissent rather than merging all reviews into a consensus that does not exist.

# 10. Evidence and artifact preservation policy

1. **Immutable originals:** original Gemini WP-B v0.1 code and three CSVs remain separately archived; later code gets new paths, no overwrite.
2. **Attribution and original wording:** reviewer transcripts supplied by the user are archived as-is when feasible, with separately authored digest or corrections; the full latest Copilot text was supplied in the conversation but may not yet be separately committed as an original artifact.
3. **Source traceability:** publication URLs/DOIs and dataset version/license accompany every calibrated table and plot; corrections state what previous version they supersede.
4. **Model outputs have grades:** external observation; reproduced code output; independently calibrated model; parametric assumption; unsupported claim. A code unit test is *not* a measurement.
5. **No reward for agreeable answers:** optimistic and skeptical hypotheses both receive tests; null findings are not erased.
6. **Energy provenance:** every joule gets one source and one destination. Experimental recovered energy, theoretical channeling and exported load electricity remain separate categories.

# 11. Conclusion

Stars 2.0's most defensible near-term achievement is an **auditable experimental architecture**, not a high-efficiency fusion reactor. Replenished targets, shape-dependent laser/alpha behavior, p–¹¹B spectra, and charged-particle direct conversion each have external experimental precedents at **different system boundaries**. The remaining scientific task is integrating them without misattributing a model assumption to measurement or a particle-beam success to complete reactor gain.

**The highest-value new contribution of this review is to keep acoustic target pre-shaping as an explicit mechanistic A/B program while accepting Copilot's demand for strict confounder, collection and stopping audits.** Acoustics can be physically important by improving the *initial* target and proton source, even if it cannot directly manipulate nuclear interactions in a picosecond burning plasma. Its merit must be judged by measured ON/OFF/SHAM outcome and its electrical cost, not by ideology, skepticism or cross-agent enthusiasm.

The work therefore divides into three immediately actionable branches: **(1) clean beam–BN transport calibration; (2) acoustic pre-shot G1 target/proton A/B; (3) characterized collector G3-A on real phase-space beams.** They can proceed in parallel as resources permit. Combined WP-B+WP-D modeling then tests whether any demonstrated benefits survive whole-system electrical accounting.

**Receipts in the front. Wizards in the back. Every negative result stays in the archive.**

---
**End of v0.7.** The review team is invited to respond with section citations, numerical reproduction or primary sources, exact energy/measurement boundaries and predeclared falsification criteria.
