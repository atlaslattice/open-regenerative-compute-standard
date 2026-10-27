# Stars 2.0 v0.4 — Modular Proton–Boron Interaction and Charged-Product Energy Conversion
**Atlas Lattice / ORCS | Expanded research white paper | 2026-10-27 | Status: exploratory, noncanonical, falsification-first**

## Executive summary
Stars 2.0 is proposed as a **modular research architecture**, not an established fusion reactor: a proton pitcher and boron-11 catcher; optional acoustofluidic target shaping, nuclear-spin preparation and plasma-wave modulation; charged-fusion-product transport; direct energy conversion; and electrical storage or recirculation. The principal research question is whether these subsystems can increase *net recovered electrical energy per unit wall-plug input* relative to matched controls. The design does not claim to stabilize a bound proton–boron intermediate, achieve ignition, or produce net power.

**Foundational engineering principle:** Treat every apparent waste stream as an energy or material flow to account for and, where physically possible, recover. This is an optimization objective, **not** a claim that entropy or irreversible losses can be eliminated.

## 1. Scope and physical boundaries
The primary reaction is p + ¹¹B → 3 α + ~8.68 MeV. Each fusion event consumes a proton and a boron-11 nucleus and produces energetic helium-4 nuclei. Unsuccessful approaches do not release nuclear binding energy. The proposed pitcher–catcher module is a *fusion interaction apparatus*: it prepares and brings reactants into contact; it is not a demonstrated confinement reactor, nor does it store a stabilized proton–boron compound for subsequent ignition. A power plant would additionally require fuel throughput, product handling, cooling, radiation protection, energy conversion, power conditioning and demonstrated net electricity.

**Hydrogen fuel-cell analogy, carefully bounded:** A fuel cell converts chemical free energy via electrochemistry and electron current. Here, a charged-particle converter would decelerate energetic alphas and produce electrical work; capacitors, batteries or other storage would hold the resulting electricity. Alphas are not hydrogen-like electrochemical fuel. Thermalized helium is primarily a product to collect or exhaust. Electrostatic direct conversion, if feasible, acts before thermalization. Recovered electricity may feed later pulses; doing so reduces net exported power.

## 2. Modular architecture and timing
**M1 — Fuel and target preparation.** Produce an isotopically characterized ¹¹B catcher and a protium-rich pitcher. Optional acoustic droplet/jet positioning and surface-acoustic-wave modulation are tested against geometrically and thermally matched controls. Isotope additives (²⁸Si, ¹³C, optional ⁶Li diagnostic witness) are separate hypotheses, not prerequisites.

**M2 — Ion generation and injection.** A high-contrast laser or accelerator creates a characterized proton spectrum. A rotating-wall Penning–Malmberg device may serve as a proton source/buncher; its nonneutral-plasma density limit prevents assuming it is a bulk fusion chamber. Electron-free operation must not be presumed superior in the target plasma.

**M3 — Fusion interaction.** A proton beam intersects a boron-11 target or plasma. Record the energy spectrum, angular spread, charge state, spot size, target areal density and shot-to-shot variability. The often-discussed ~675 keV p–¹¹B resonance is in **center-of-mass** energy; for protons on stationary ¹¹B, the corresponding laboratory proton energy is approximately 736 keV. A laser-generated beam is not assumed monoenergetic.

**M4 — Mechanical/acoustic track.** Investigate acoustic droplet ejection, standing surface acoustic waves, resonant target vibration and phononic isolation. These alter target geometry, density, uniformity or laser coupling; they do **not** directly sculpt femtometer-scale nuclear configurations or change the strong force. Mechanical acoustic waves need matter; they do not propagate through vacuum.

**M5 — Plasma-wave track.** Investigate laser-driven ion-acoustic waves, including stimulated Brillouin scattering where applicable. Verify actual wave amplitude, frequency, phase velocity and coupling. A wave's existence does not establish reduced proton stopping, increased nuclear yield or alpha channeling. Those are separate measured endpoints.

**M6 — Optional nuclear-spin track.** Measure actual ¹¹B and proton polarization before claiming cross-section enhancement or alpha anisotropy. ²⁸Si spin-zero host and ¹³C dynamic nuclear polarization are candidate materials routes, not demonstrated solid-state transfer chains to ¹¹B and ¹H under laser-shot conditions. Any claimed 30–60% enhancement is a hypothesis pending primary-source and experimental verification.

**M7 — Alpha diagnostics, transport and conversion.** Measure primary fusion yield and escaping alpha spectra separately. Use complementary diagnostics (e.g., CR-39 and a calibrated spectrometer) with backgrounds, shielding, species discrimination and detector acceptance quantified. Magnetic steering, spin-related angular anisotropy and wave-mediated alpha channeling are distinct mechanisms. A multistage electrostatic converter is a proposed subsystem whose acceptance, space charge, energy spread, secondary electrons, grid interception and high-voltage insulation must be modeled and measured. No assumed 65–75% system conversion efficiency.

**M8 — Electrical conditioning and storage.** Capture converter output as measurable electrical work at a defined load. Condition and store it (e.g., capacitive storage) or feed subsequent shots. Explicitly separate recovered gross energy, reinvested energy and exported net energy. Product helium management is not equivalent to electricity storage.

## 3. Three noninterchangeable energy-management layers
**Layer A: Unreacted-particle energy retention.** In-field recirculation avoids an extraction/reacceleration cycle, but faces stopping, scattering, transport, electron drag and radiation losses. Recovery-and-reinjection may instead use an electrostatic decelerator plus accelerator; each transfer introduces inefficiency. Repeated encounters are not automatically independent, identical or indefinitely possible.

**Layer B: Whole-system energy management.** Track target heating, conductive/convective transport, bremsstrahlung, scattered laser light, escaping ions and radiation. Some streams may be recovered only as low-grade heat, not high-grade electrical work. Bremsstrahlung recovery is especially difficult: interception of photons does not imply efficient reconversion to energetic protons or electricity. Respect entropy and conversion limits.

**Layer C: Fusion-product management.** Successful reactions create alpha kinetic energy. Channeling may redistribute it to waves or energetic protons; direct conversion may export it as electricity; thermalization may supply heat. **The same alpha joule cannot be credited to more than one pathway.** Removing fusion ash also matters for plasma composition and radiation losses.

## 4. Nuclear-yield model: do not assume a compound multiplier
For an incident proton distribution f(E,θ,t), fusion probability depends on the measured target distribution, stopping, transport and energy-dependent cross section. A simplified thin-target expectation is
Y_f ≈ N_p ∫ f(E) [∫ n_B(x) σ_pB(E(x)) dx] dE,
subject to geometry and attenuation corrections. Primary alpha birth count is ~3Y_f; detected alpha count is modified by escape, energy acceptance and detector response. These are not interchangeable.

The proposed R_Y = f_acoustic × f_resonance × f_spin × f_wave is **not an established physical law**. These factors may interact, overlap or oppose one another. Numerical ranges previously floated (acoustic 2–4×; resonance 3–10×; spin 1.3–1.6×; wave 1.1–1.5×) are illustrative research prompts, not validated gains or independent multipliers. Model main effects and interactions explicitly.

## 5. Complete energy ledger
Define time-integrated electrical energy at the grid boundary:
E_net = E_direct,out + E_thermal-electric,out + E_other,out − E_laser-wall − E_RF-wall − E_acoustic-wall − E_DNP-wall − E_magnet-wall − E_vacuum-wall − E_cooling-wall − E_fuel-prep − E_controls − E_other-aux.
If laser optical energy is given as E_laser,opt, then E_laser-wall = E_laser,opt / η_laser-wall; **do not subtract both**. The converter output is actual delivered electrical energy, not alpha kinetic energy multiplied by an unmeasured ideal efficiency. Account for staging cryostat and offline target preparation on a per-shot or per-unit-fuel basis. Distinguish stored electrical energy from electricity delivered externally. For a pulsed experiment, report energy/shot, time-averaged power at stated repetition rate, duty cycle and uncertainty.

A simplified encounter screening condition, not a reactor equation, is
η_f E_f > E_0 + [(1−p)/p] E_loss + E_aux/p,
for independent, identical encounters with probability p and eventual success. Real beams require finite escape probability, changing energy distributions, and loss correlations. This equation must not substitute for the full ledger.

**Illustrative, not predictive:** At η_f=0.70, useful fusion energy is 6.076 MeV per success before other costs. If 1,000 failures precede one success, the entire available allowance is 6.076 keV per failure, leaving zero for other costs. Such numbers do not establish achievable collision counts.

## 6. Evidence tiers and claim registry
**Demonstrated in relevant disciplines, not integrated here:** Laser-driven p–¹¹B reactions; electrostatic particle deceleration principles; acoustic target handling and elastic-wave bandgaps in other settings; plasma-wave physics; particle spectroscopy.

**Theoretically supported / model-dependent:** Alpha-channeling benefits; spin-polarization cross-section effects; recovery-assisted reduction in confinement requirements; coupling of tailored waves to energetic particle distributions.

**Proposed and not demonstrated for Stars 2.0:** Solid-target ¹³C→¹¹B/¹H polarization chain surviving shot conditions; acoustic enhancement of normalized p–¹¹B yield; SBS-enabled useful alpha extraction in this geometry; integrated net-positive electrical output; −80 dB phononic isolation in the specified target chamber; efficient direct conversion of the actual broad alpha spectrum.

**Specific literature leads requiring direct paper inspection:** arXiv:2609.07732 (reported 99.96% coherent proton response in a modeled LAPD configuration; **not** reactor electrical efficiency); arXiv:2210.08076 (reported confinement-time improvements under assumed energy recovery; **not** demonstrated bremsstrahlung-to-electricity conversion); September 2026 continuously replenished water-sheet / boron-nitride alpha-source report (claimed 10 Hz and 18,000 shots; verify experimental methods); SPIN2025 polarized p–¹¹B discussion; 2025 optical-pumping proposal. Numerical values should remain unverified until original source and applicability are checked. A 5 T proton Brillouin density estimate ~6.6×10^16 m⁻³ is an order-of-magnitude injector constraint, not a universal limit for all confinement geometries.

## 7. Orthogonal experiments and gates
**G0: Provenance and physics.** Retrieve primary papers, cross-section datasets, laser energy definitions, polarization diagnostics and realistic efficiency bounds. Freeze hypotheses and endpoints before testing.

**G1: Acoustic target handling.** Compare laser shots with acoustics OFF, acoustics ON, and power/thermal/geometry-matched SHAM. Predefine primary outcome as fusion reactions per incident proton (or alpha yield normalized to proton spectrum and boron areal density), and secondary outcome as proton production per wall-plug joule. Confirm that target thickness, alignment, shot timing and background are measured. Randomize shot order and replicate.

**G2: Spin preparation.** Establish actual polarization and lifetime in the relevant material under shot conditions; compare polarized/unpolarized controls with matched target composition and laser conditions. Test angular anisotropy separately from total fusion yield.

**G3: Plasma waves.** Demonstrate the intended wave and measure its amplitude and phase; compare resonant, off-resonant and absent waves. Measure stopping, alpha escape and energy costs, not just alpha counts.

**G4: Interactions.** For three binary factors (acoustic, spin, wave), use a full 2³=8-condition factorial design, with independent sham validations, randomized repetitions and uncertainty. A six-run screening matrix cannot identify all interactions. Evaluate direct-converter bias separately to avoid conflating collection efficiency with fusion birth rate.

**G5: Engineering energy ledger.** Measure converter voltage/current versus time at a known load, laser and RF wall-plug power, cooling, target manufacture, duty cycle, stored energy and net output. Require positive E_net with uncertainty and sustained repeatability before any net-power claim.

Stop/go decisions: Failure to demonstrate a controlled yield benefit should retire or revise that subsystem without invalidating the others. A positive G1 yield result is not G5 energy gain.

## 8. Open questions
1. Does acoustic modulation improve target thickness, density uniformity or absorption at fixed laser energy?
2. Does any acoustic benefit survive normalization to incident proton number and energy spectrum?
3. Can a proton distribution near the p–¹¹B resonance be produced with acceptable laser wall-plug cost?
4. What target areal density optimizes fusion probability versus stopping and damage?
5. Can unreacted protons be recirculated at lower loss than fresh injection?
6. What are the quantitative radiation, electron drag and transport losses for each geometry?
7. Can meaningful ¹¹B and proton nuclear polarization be achieved and maintained through the shot?
8. Does polarization change total yield, angular emission, or neither?
9. Can an SBS/ion-acoustic grating be independently verified and controlled during the relevant interaction?
10. Does wave coupling improve useful alpha energy extraction after its own drive cost?
11. What fraction of broad-spectrum alphas can be transported into an electrostatic converter without neutralization or interception?
12. What are converter space-charge limits, grid losses, insulation constraints and actual DC-load output?
13. Is any bremsstrahlung recovery route thermodynamically and economically credible?
14. How should fusion ash and other charged species be removed without large parasitic losses?
15. Which subsystems improve *net electrical* yield rather than only detector counts?
16. Can shot-to-shot reliability and repetition rate support a positive time-averaged energy balance?
17. How do material costs, isotopic purification and component lifetime change economics?
18. Which result would falsify the entire energy-positive architecture versus merely a specific enhancement hypothesis?

## 9. Proposed immediate work packages
**WP-A: Evidence audit.** Validate the primary-source numbers and classify every claim as demonstrated, theoretical, simulated or proposed.
**WP-B: Open numerical model.** Calculate energy-dependent beam–target fusion probability with measured stopping and energy distributions; sweep acoustic improvement, polarization, wave effects and converter efficiency independently; include uncertainty and nonmultiplicative interactions.
**WP-C: G1 experimental protocol.** Specify target geometry, drive frequencies, sham hardware, shot count/power, diagnostic calibration, preregistered endpoints and stop criteria.
**WP-D: Direct-conversion feasibility.** Analyze realistic alpha spectrum and converter acceptance; compare electrical extraction with heat recovery and reinvestment.

## 10. Conclusion
Stars 2.0 should be evaluated as a **modular nonthermal fusion-interaction and energy-management testbed**. The near-term falsifiable goal is a normalized acoustic-target improvement under controlled laser conditions; the long-term goal is an experimentally supported, complete energy ledger for a larger system. Neither a stabilized p–¹¹B intermediate nor a self-sustaining power reactor has been demonstrated. Positive alpha yield, alpha channeling and net electricity are separate milestones.

**Research ethic:** Preserve negative results, provenance, uncertainty and sham controls. Every claimed recovered joule must have an identifiable source and an exclusive destination.


---

# v0.4 Research Extension — Electroacoustic Chemistry, Alpha-State Questions and Coherent Energy Recovery

**Change log:** v0.4 retains the complete v0.3 conceptual architecture and experimental gates. It adds an explicit electroacoustic hypothesis registry, clarifies what an alpha nuclear state is, and proposes an independent alpha-beam recovery experiment. All new performance claims remain unverified.

## 11. Interpret the electroacoustic proposal precisely
“Electroacoustic chemistry” can refer to electrically excited acoustic phenomena in liquids and solids, including acoustofluidics, piezoelectric actuation, sonochemistry and acoustically assisted material preparation. In Stars 2.0, these processes could organize a fuel-bearing droplet, surface, interface or nanostructure before the fusion event. They are not themselves evidence of control over nuclear forces or alpha-particle nuclear states.

Three different hypotheses must remain distinct:

**H-EA1: Target-state engineering (highest near-term readiness).** Acoustic and electroacoustic actuation changes fuel geometry, areal density, microstructure, surface texture, material distribution or laser coupling. Compare matched targets with and without excitation. Primary endpoints: measured target state, incident proton spectrum, normalized fusion birth yield and auxiliary energy per shot.

**H-EA2: Plasma-wave-mediated alpha energy transfer (theoretical research track).** A characterized collective plasma mode, perhaps laser-driven, couples to energetic alpha motion and transfers a measurable fraction of alpha kinetic energy into a specified wave or particle population. Required evidence: alpha energy decrement, destination energy increment, mode characterization, and net extracted work after drive cost. Ion-acoustic waves, stimulated Brillouin scattering, and resonant alpha channeling are not synonyms; frequency, wave vector, phase velocity, resonance condition, geometry and distribution functions must be specified.

**H-EA3: Alpha quantum-state preparation/preservation (speculative and currently unsupported).** Alpha particles are helium-4 nuclei with a stable spin-zero ground state. The value targeted for harvesting is predominantly their kinetic energy and phase-space distribution, not a metastable alpha internal state. Isotopically enriched ²⁸Si has nuclear spin zero and ¹³C can participate in spin-polarization experiments, but neither is established as a means of preserving the internal nuclear state of newly created MeV alphas. Any proposal to alter the reaction branching or alpha angular distribution via reactant spin polarization requires a reaction-specific spin-dependent cross-section calculation and experimental validation. Do not describe ²⁸Si as an absolute 'spin vacuum'.

## 12. Four different control knobs
**Before interaction:** acousto-optical and electroacoustic target preparation; spatially patterned boron loading; controlled laser temporal profile. These influence the incoming conditions.

**At interaction:** proton energy spectrum, target density, nuclear spin orientation if demonstrated, and plasma distributions. These may influence fusion probability and the outgoing alpha energy/angular distributions.

**After birth:** magnetic/electric guiding fields and collective plasma waves may modify charged-particle trajectories or redistribute alpha kinetic energy. Static magnetic fields bend trajectories but do not themselves perform work on particles; electric fields and time-dependent collective fields can exchange energy.

**After energy transfer:** high-voltage DC conversion, RF rectification or other measured electrical recovery, then capacitive/battery storage and possible pulse-to-pulse reinvestment. A coherent wave with increased energy is not yet recovered electricity until its output is measured at a load.

## 13. Direct-versus-wave recovery comparison
Compare three hypotheses under the same injected alpha-beam distribution and an explicitly defined boundary:

**C1 — Guided direct conversion.** Transport escaping alphas toward an electrostatic decelerator. Record capture acceptance, charge exchange, secondary-electron losses, grid interception, load output and auxiliary power. Static magnetic guidance may be used but its coil power and material requirements count in the ledger.

**C2 — Coherent wave-mediated transfer.** Drive and diagnose a plasma wave, pass a known alpha distribution through it, and measure alpha energy loss alongside energy gained by a specific wave or proton population. Then quantify whether that gained energy can be extracted electrically. Control for collisional stopping and ordinary heating.

**C3 — Hybrid acousto-optical preparation plus wave/electrostatic recovery.** Use acoustic target shaping upstream and a separately characterized alpha recovery method downstream. Do not attribute a compound gain to 'synergy' without factorial interaction estimates.

**Crucial comparison:** A low wave-drive cost and a high alpha energy transfer fraction are both necessary but insufficient. The recovered energy must reach a load with higher net value than the reference recovery scheme. A plasma wave that accelerates alphas using laser energy is an energy input, not alpha-energy harvesting.

## 14. New gate G3-A — Controlled alpha-beam energy-transfer experiment
This gate can be tested independently of p–¹¹B fusion using a characterized helium-ion/alpha source and appropriate safety protocols.

1. Specify incoming alpha charge state, flux, kinetic-energy spectrum, angular spread and beam duration.
2. Characterize the plasma or wave-supporting medium, electron density and temperature, background stopping, wave frequency, wave number, phase velocity, amplitude and coherence time.
3. Record baseline alpha output spectra with no drive, off-resonant drive and resonant drive. Match deposited drive energy and thermal state where practicable.
4. Measure energy deposited in electrons, ions, radiation, collective modes and escaping species. Distinguish wave energy gain from irreversible plasma heating.
5. Attach a calibrated extraction circuit to the intended recovered mode; measure time-integrated electrical output at the load.
6. Compare wave-mediated and electrostatic extraction on a common injected alpha-energy basis and a common wall-plug basis.
7. Replicate with randomized control order, blinded diagnostics where practical, and uncertainty intervals. Report null results.

**Primary endpoints:**
- Alpha kinetic-energy change: ΔE_α = E_α,in − E_α,out, corrected for particle loss and acceptance.
- Useful transfer fraction: η_transfer = E_mode,attributable-to-alpha / E_α,in.
- Electrical extraction fraction: η_extract = E_load,attributable-to-alpha / E_mode,attributable-to-alpha, when measurable.
- Incremental net recovery: ΔE_net = (E_load,on − E_load,sham) − (E_wall,on − E_wall,sham), with matched beam input and all auxiliary differences included.

If the numerator in η_extract cannot be separately identified from external drive power, report it as *unresolved*, not as positive recovery. Calorimetry and full species diagnostics may be needed to close the balance.

**Failure conditions:** No reproducible alpha-to-wave energy transfer; transfer attributable only to ordinary stopping/heating; no useful output at a load; or wave-drive/auxiliary energy consistently exceeds incremental recovery. Failure of G3-A does not falsify G1 acoustic target preparation.

## 15. Alpha collection and electron-interference constraints
Alpha particles carry +2e when fully ionized; charge exchange and recombination can alter charge state downstream. Their kinetic energy is distributed over a broad, reaction-specific spectrum. Magnetic guidance can reduce interception and steer some particles, but collection is limited by source geometry, gyroradius, pitch-angle distribution and field topology. Electron removal is not a universal benefit: electrons may be essential to quasineutrality and to the intended plasma-wave dynamics. Positive-ion space charge can limit unneutralized beams and converters. The goal is controlled electron coupling, not an electron-free fusion environment by decree.

**Illustrative electrostatic scale:** A +2e alpha traversing a retarding potential difference of 1 MV can surrender up to 2 MeV of kinetic energy, provided it traverses the field without being reflected or intercepted. This is an ideal single-particle statement, not a measured converter efficiency. Direct conversion is not a hydrogen fuel cell; electrical energy is harvested from particle motion, then stored separately.

## 16. Refined ledger and conservation checkpoints
For an alpha-beam test define E_α,in = E_α,out + E_electrons + E_ions + E_wave + E_radiation + E_walls + ΔE_fields + E_unresolved, with sign conventions, measurement uncertainties and external wave-drive contributions explicitly identified. A time-dependent wave may return energy to the beam or receive energy from it. Do not assign all wave energy to alphas if the laser or RF drive also feeds that wave.

For a complete fusion pulse, retain the v0.3 electrical boundary ledger and add:
- Acoustic driver and its real wall-plug efficiency, including pulsed power.
- Laser pump and wave-generation wall-plug costs.
- Target preparation, isotopic purification and cryogenic spin-preparation energy amortized per shot.
- Magnetic coil, vacuum and charged-particle handling costs.
- Converter output measured at a specified load and storage losses.
- Unrecovered kinetic energy, heat and radiation as explicitly separate destinations.

**No double-counting:** Alpha energy sent to wave-mediated proton heating cannot also be credited to direct DC recovery; electrical energy reinvested in subsequent shots is not exported output.

## 17. Experiment prioritization and literature requests for independent reviewers
**Near term:** G0 source audit; G1 acoustic target preparation with normalized proton and alpha yields; independent electrostatic alpha-beam collection and conversion characterization.

**Medium term:** G3-A coherent alpha-beam wave-transfer measurements; demonstrate actual recoverable mode energy and compare against direct conversion. Only then combine acoustic preparation with recovery.

**Long term:** G2 reactant spin polarization under real shot conditions; G4 factorial interactions; G5 full net-electric ledger and repeatability.

**Questions for Gemini and DeepSeek:**
1. Identify peer-reviewed experiments where an externally driven plasma wave extracted *measurable net electrical work attributable to energetic alpha particles*, not merely shifted their spectrum.
2. Supply the precise alpha-wave resonance condition and accessible wave phase velocities for MeV alphas in the proposed geometry.
3. Quantify wave damping, electron heating and laser/RF drive cost relative to extracted alpha power.
4. Provide any direct evidence of ²⁸Si/¹³C target hosts preserving nuclear polarization of ¹¹B or ¹H through picosecond laser interactions.
5. Distinguish changes in alpha birth angular distribution from post-birth electromagnetic steering.
6. Propose a practical G3-A diagnostic and sham scheme that separates alpha-origin wave energy from externally injected wave energy.
7. Compare electrostatic, inductive/RF and hybrid recovery using identical alpha phase-space inputs, including space-charge and charge-exchange losses.
8. Explain whether an electroacoustic material structure can survive the relevant laser and plasma environment or must remain in an upstream preparation stage.
9. Provide uncertainty-bounded performance ranges with direct primary sources, not illustrative multipliers.
10. Identify a decisive negative result that would retire wave-mediated recovery while preserving other Stars 2.0 research tracks.

## 18. v0.4 conclusion
Electroacoustic preparation and coherent alpha-energy management are **complementary but physically distinct**. It is reasonable to test whether structured material, laser and plasma waves improve proton production, fusion yield, or alpha-energy routing. It is not established that a ²⁸Si/¹³C metamaterial preserves a special alpha nuclear state or that acoustic excitation can directly shape nuclear fusion products. The immediate goal is measurable, independently reproducible energy transfer with closed accounting—not a presupposed gain.

**Reviewer note:** This extension is a hypothesis and experimental-design synthesis. It does not claim independent verification of the literature leads in Sections 6 or 17.
