# STARS 2.0 — G0-B Protocol v0.1
## Preregistered proton-transmission and front/rear alpha-spectrum validation across boron catcher thickness
**Atlas Lattice / ORCS | 27 October 2026**
**Status:** DESIGN DRAFT — **NOT preregistered in a third-party registry, NOT yet funded, run, blinded, calibrated or passed.** This version must be frozen and independently reviewed **before** experiment data acquisition.
**Project direction:** Dave Sheldon / Atlas Lattice.
**Design contributors:** Copilot Researcher (2026-10-27 v0.8 critique: wedge, proton transmission, full-spectrum scoring, data partitions, leakage rules, collector reference source), DeepSeek (three-target substrate-comparison scheme, printed-frame/deposited-film distinction), Gemini Argon (WP-B preliminary target-thickness escape model), ChatGPT/Tidal Lantern (synthesis, analysis plan, controls, source requirements and archival editing).
**Basis:** [STARS 2.0 v0.8](../whitepapers/STARS_2_0_v0_8_REFERENCE_DATA_CALIBRATION_AND_INTERFACE_VALIDATION_2026-10-27.md); [DeepSeek substrate G0-B/G0-F](../reviews/DEEPSEEK_G0B_THREE_TARGET_SUBSTRATE_COMPARISON_PROTOCOL_2026-10-27.md); [IAEA EXFOR acquisition](../wp_b/revised/iaea_exfor_pipeline/README.md).

> **Purpose:** A conventional, measured incident-proton beam probes characterized boron-bearing target layers. Independently qualified diagnostics record transmitted/scattered protons and the *two* alpha-exit hemispheres across thickness and support designs. A model trained only on approved earlier data must predict **full measured spectra with a fixed parameter set and frozen instrument-response model**. No re-fitting at each thickness, film or substrate is permitted on the blinded validation set.

## 0. Evidence maturity and source discipline
Four mutually exclusive statuses:
1. **SOURCE-TRACED** — source record ID/version/entry/subentry/pointer, DOI or instrument record is retained.
2. **SOURCE-REPRODUCED** — a deterministic, independently rerun parser reproduces the original published data and units/frame with recorded hashes.
3. **CALIBRATED** — a frozen model predicts truly withheld *external*, independently measured calibration datasets within preregistered uncertainty criteria.
4. **VALIDATED** — a frozen model passes the preregistered, blinded, *newly acquired* G0-B dataset with its originally stated error tolerances and no post-hoc repairs.

For every nuclear input, preserve **source_energy_label_verbatim** along with energy_value, energy_unit, energy_frame, projectile, isotope, reaction channel/observable, source_entry, source_subentry and source_revision. Distinguish a cross-section for **reaction events** from alpha multiplicity and partial-channel measurements. The prominent ~675-keV **incident proton laboratory** resonance convention must be source-verified. **Do not promote a particular J^π label until an authoritative ENSDF/level/channel mapping has been checked and recorded.** Copilot's corrected spreadsheet is a reported *remapped candidate*, not an evaluation. All current 4–6 µm optima are scenario-generated, not verified physical values.

## 1. Scientific hypotheses

- **H1 birth:** Across at least part of the selected incident proton spectrum and test range, the *latent* reaction-birth integral may grow with B-11 areal thickness. Because birth counts are **not directly observed**, test through a joint, response-corrected inference with explicitly propagated nuclear and detector assumptions, not a claimed directly counted birth total.
- **H2 exit:** For a specified proton source, measured material stack and diagnostic acceptance, alpha escaping energy may have an interior maximum or statistically distinguishable plateau vs catcher B-11 areal column. The precise thickness of this feature **is not predetermined**.
- **H3 sidedness:** Vacuum-facing and opposite-side exit energies/spectra vary differently with thickness. Always identify faces by **beam-upstream, beam-downstream, and substrate-facing** direction, not informal front/rear alone.
- **H4 spectrum evolution (new, Copilot):** Normalized and absolute alpha energy–angle distributions change with catcher thickness, beyond a change in integrated yield alone. Compare both the **distribution shape** and normalization, and test differential detector artifacts.
- **H5 stopping isolation:** The same frozen proton-stopping model must predict the transmitted proton energy/angle spectrum vs material thickness **without using alpha data to tune proton loss**.
- **H6 substrate:** At matched *B-11 atoms/cm²*, structural backing and support geometry alter the measured transmitted-proton and escaping-alpha distributions in a manner predictable from a recorded multilayer stack.

These hypotheses can fail independently. Numerical confirmation of the old Gemini curve without experimental sources is not a pass.

## 2. Experimental object, interfaces and arms

### G0-B is NOT the full laser experiment
Use an independently characterized conventional proton beam, with a specified distribution in energy, angle, time, spot and flux. No acoustic drive, water-leaf pitcher, pulsed laser EMP, reactor collector or nuclear-spin polarization is introduced in the initial beam-to-target physics test. Their integration is conditional on passing the interfaces below.

### Material arms / controls (DeepSeek)
- **A — free-standing/minimally supported reference:** Characterized boron/BN foil, with all actual windows or sparse frames included in the layer-stack model (even an ultrathin Si₃N₄ window is not zero stopping).
- **B — thick-substrate control:** B-bearing film with matched B-11 areal atom density, on independently characterized Si/Al or other solid backing. Run a separate **bare-substrate** control and document irradiation direction relative to the layer order. Fully blocked downstream alphas behind a thick substrate are a *hypothesis to model/measure* based on actual particle energy, not an assumption used for normalization.
- **C — deposited film + printed open-aperture holder:** B-bearing functional layer supported by a DISH/AM-inspired frame or mesh, comparing support occlusion, reproducibility, target survival and transport on matched B-11 areal inventory.
- **D — optional exploratory graded/porous architecture:** only after A–C and source qualification; record actual three-dimensional density, isotope fraction and film roughness, not just nominal thickness.

**Thickness set:** provisional central nominal active B-bearing thickness targets 2, 3, 4, 5, 6, 8, 10, 15, 25 and 50 µm, **subject to fabrication feasibility, transmitted proton ranges, stopping uncertainties, and safety/instrument capability**. Do not force every material route to match this set; define shared comparable **B-11 areal column** points. Preserve a limited independent foil series even if using a same-batch graded wedge.

**Wedge/step add-on:** a carefully mapped BN wedge or step target is a *within-batch systematic-error control*, not a substitute for independent fabricated targets. Raster the beam to pre-mapped, non-overlapping spots; log lateral beam gradients, beam energy/current, local film thickness/density/composition, angle, drift and irradiation damage. Randomize raster order; remeasure drift, wear and contamination. If raster position and dose history alias thickness, wedge data are excluded from primary causal claims.

## 3. Independent source and material calibration inputs

### R-N nuclear data
Source-archived EXFOR raw records and per-observable tables; experimental energy frame, reaction channel, σ statistical/systematic uncertainties and covariances, angular differential information, sequential three-alpha decay data, branching ratios and level assignments with provenance. Never take a scalar 3α cross section and synthesize three independent 2.9 MeV alpha tracks as though validated.

### R-S material stopping
Per-target measured B-11 areal atomic density (with traceable uncertainty), composition, isotope ratio, surface topography, total material thickness, density/porosity, substrate and holder layer stacks. Source-qualified proton and helium stopping and range straggling at relevant energy/angle; multiple scattering and attenuation. If only theoretical SRIM/TRIM calculations are available, carry as simulation inputs with version/run cards and calibration uncertainty, not as measured BN material properties.

### R-P beam source
Measure beam incident at target (including shot-to-shot and raster gradients): d³N_p/(dE_lab dΩ dt), current/charge integration, energy spread, spot and incidence angle. Independent post-target proton spectrometer measures transmitted E/angle and any proton contamination in alpha detectors. Distinguish laboratory beam current from laser TNSA predictions in later G2.

### R-D detector qualification
Qualify detector response with known particle sources **before blinding**. Include calibrated silicon ΔE–E telescopes, diamond/SiC as optional active instruments, CR-39/TPS as independent checks where feasible. Document solid angle, filters, dead layers, ion species misclassification, alpha/proton/electron/secondary backgrounds, thresholds, time response, nonlinear saturation, live-time, pile-up, digitizer/EMP artifacts and geometrical acceptance. Diamond and SiC are *candidates*, not inherently EMP-immune or automatically particle-resolving.

## 4. G0-D must pass BEFORE G0-B blind data are used
Using independently known mixed-particle calibration sources and geometry, freeze detector forward response R_det(E,Ω,species,t,channel), response covariance and detector-calibration dataset IDs.

Instrument acceptance criteria must be **numerically specified by the experimenters from instrument calibration, before acquiring the G0-B blind set**; this paper intentionally does not invent a percentage, event-count or signal-to-noise threshold without facility evidence. Fail G0-D if reconstructed known calibration spectra systematically fall outside the predetermined recovery/coverage criteria. A failed detector response invalidates interpretive G0-B scoring, not the existence of physical counts. Retain raw data.

## 5. Data partitions, freeze sequence and leakage control
Declare datasets and immutable hashes/DOIs before fitting:
- **TRAIN:** allowed nuclear cross-section, stopping, alpha-decay and historical accelerator data for fitting model choices.
- **CALIBRATION:** separate measured beams/targets/diagnostics used to set uncertainty and validate instrument/model interfaces (may include G0-D).
- **VALIDATION_PUBLIC:** publicly accessible experiments **never used in optimization, feature/physics selection or threshold choice** once assigned validation role; timestamp selection and record any prior exposure.
- **VALIDATION_BLIND:** independent prospective G0-B shots acquired and access-escrowed under protocol. Hash raw data prior to unblinding and prevent model authors from viewing outcomes, response-corrected plots or statistics.

Freeze code commit hash, fitted model parameters and priors, nuclear/stopping dataset versions, instrument response, random seed, input beam distribution and uncertainty, target sample characterization, predicted distributions, scoring code and criteria **before the blind outcomes are opened**. Facility must hold secure blind data and independent custodian must sign data-access log.

**A model changed after inspecting blind outcomes receives a new version; any earlier blind failure remains reported and the changed model requires a new independently blinded validation experiment.** A previously used dataset cannot be renamed 'blind' again. Publish negative findings.

## 6. Primary joint measured observables
All normalization constants (incident proton number, detector acceptance, live-time, aperture fraction, illuminated B-11 areal mass and collection angle) must be source-qualified.

1. Incident proton distribution as a control, E/Ω/t.
2. **Transmitted/scattered proton** distribution E/Ω/t and energy loss conditional on target/sample.
3. Vacuum/upstream alpha E/Ω spectrum and species-ID confidence.
4. Opposite/downstream alpha E/Ω spectrum and species-ID confidence.
5. Front/rear alpha energy partition, shape, relative normalization and angular yield.
6. Thickness-dependent *source-normalized* alpha flux, energy per incident proton and derivative/plateau.
7. Observational backgrounds from blank substrate, no boron, no beam and detector dark runs.
8. Full neutron/gamma/secondary/other particle channels, if relevant to the actual apparatus and source, as independently budgeted backgrounds.
9. Target dose, irradiated location, sample and batch ID, film wear, and instrument/beam drift.

**Do not claim direct simultaneous detection of all three alpha products from every event** without a real coincidence apparatus and its acceptance model. Record events with a latent reaction_id in Monte Carlo, distinct from measured hit IDs. Spectral output should be provided **both** raw counts and detector-folded predictions, with carefully labeled response-corrected inference.

## 7. Forward model / blind predictions
Let theta be a single global frozen physical parameter vector. Model predictions are detector-forward-folded distributions conditional on the **measured incident** proton source and **recorded material stack**:
p(D_p,out, D_alpha,up, D_alpha,down | incident p(E,Ω,t), sample/material, theta, R_det).
No independently adjusted alpha yield, stopping/range exponent, resonance shift, angle scale, backing attenuation or detector efficiency for each thickness is allowed at validation.

Use either a preregistered statistical generative model with counting/statistical backgrounds and covariance, or an equivalently reproducible multivariate scoring approach. Parameter uncertainty may be marginalized **using a frozen prior/posterior**, never fitted to revealed blind endpoints.

**Proposed primary pass/fail family (precise thresholds to be preregistered in facility appendix):**
- proton-transmission spectral agreement across thickness/material;
- alpha upstream/downstream energy spectra including both shape and absolute normalization;
- alpha front/rear partition;
- thickness-dependent trend (H2) and spectrum evolution (H4).

Compare confidence/predictive bands or proper scoring rules; account for overdispersion, detector threshold and background. Require jointly acceptable coverage across the selected hypotheses and thicknesses, using a prespecified multiplicity/correlation policy. No single metric, such as total microjoules, may compensate for a major failure in proton transmission, front/rear partition or energy distribution. Preregister which measures are primary and which exploratory to avoid shifting success criteria.

**Mechanistic fault isolation:** if transmitted proton spectrum fails, prioritize material/proton source/stopping/model geometry corrections, **not retuning nuclear cross section**. If proton passes but alpha fails, investigate channel physics, correlated decay, helium stopping, solid-angle or instrument response—with G0-D separately tested. If support-specific arms fail, investigate multilayer acceptance/backing geometry. These are diagnostic leads, not conclusive identification of a single wrong mechanism.

## 8. Exact energy and particle ledgers
For a shot/beam pulse, define all material-domain energies in joules and charged-particle kinetic energies at explicit boundaries. Source-experimental proton kinetic input plus **nuclear mass-defect Q for verified reactions** plus explicitly modeled other input channels equals output transmitted/scattered protons, escaped alpha energy by face and side angle, all deposited target/substrate energy, gamma/neutron/other particles, recoil, secondary electrons/radiation and **unresolved residual** within measurement uncertainty.

Do NOT credit transmitted proton energy as recoverable heat. Do NOT credit a theoretical fusion Q per **detected alpha count** without response-corrected event multiplicity. Note alpha kinetic birth energy includes incident reaction proton energy and Q, with exact reaction kinematics and recoils. Detector-system electrical draw and accelerator beam generation electricity are **research energy/cost metrics**, not required to claim G0-B physics success; G0-B does not prove an electrical fusion reactor.

Explicit residual and measurement covariance:
E_residual = E_total_known_inputs+E_Q_inferred − sum(observable/scored exits+deposits+other channels).
A residual may be uncertain; do not hide it as target heat.

## 9. Acoustic branch: sequential falsification, not G0-B confound
Separate G1-A liquid pitcher arms geometry-reference / actuator OFF / powered SHAM / ON with randomized blocks and wall-power log.
- A0: actuator delivers calibrated intended mechanical field.
- A1: target shape/reproducibility changes measurably.
- A2: resulting measured proton phase space changes (mean and/or variability).
- A3: downstream alpha-interface energy changes after known G0-B catcher transport.
- A4: recoverable electrical load work improves after actuation power and full plant inputs.

No access to A3/A4 success claim if A0/A1/A2 have not passed corresponding causal tests. A2 can show real beneficial variance reduction even if mean unchanged; do not call that reactor energy gain. Bayesian tuning happens only *after* controlled randomized reference tests with prospective holdout shots and no validation leakage.

## 10. Collector comparator: STARS Alpha Exhaust Benchmark v1 (later gate)
After independently characterized source-to-catcher outputs establish alpha flux Phi_alpha(E,Ω,t,q), freeze and publicly release an appropriately uncertainty-banded, reference-source **measured** benchmark distribution. Every collector C1 electrostatic, C2 ion-Bernstein-wave, C3 hybrid, C4 inductive receives **the same** source distribution or explicitly propagates its mismatch. Before measurement, release only **SIMULATED BENCHMARK**, never label as actual plasma exhaust.

Collector score:
W_net,Ci = W_load,Ci − W_local_aux,Ci,
with identical particle-energy denominator, accepted solid angle, time window, charge-state data and uncertainty. Whole-plant net additionally subtracts proton/laser generation, target recycling and all upstream energy.

**C4 magnetic/inductive specific caution:** A pickup-coil voltage spike is not recovered fusion electricity. Account for Delta U_B = 0.5 L I_f²−0.5 L I_i² along with bank charge/discharge, switches, resistive coil losses, plasma preparation and power conditioning; verify closed-cycle load work.

## 11. Information gained per joule (optional scheduling policy)
Prioritize high-information, low-complexity source/detector/transport calibration over fully integrated laser+acoustic+collector shots. Optional resource metric is expected discrimination among preregistered models per facility joule, dollar and hour, not a claim about energy-balance physics. Record actual operational costs; do not invent them. A G0-B accelerator study independently constrains several interfaces in a way a full integrated experiment may not.

## 12. Facility preregistration appendix: REQUIRED BLANKS BEFORE FREEZE
**Do not declare this draft preregistered until the following slots are filled and the exact protocol hash is escrowed/registered:**
- Facility, beam species/spectra/current, flux and beam-time allocation;
- Sample manufacturer/fabrication recipe and target batch map, foil/film isotope ratios and local areal-density uncertainties;
- Actual subset of material arms and thickness/areal-density bins; independent vs wedge/raster replication and randomization;
- Detector configurations, response qualification source/calibration results and G0-D numeric passing rules;
- Formal primary/endpoints and treatment of side-angle escape; covariance and denominator;
- Sample size / power or precision argument accounting for shot/batch effects, physical damage and adaptive-stopping bias;
- Prospective numerical agreement bands, statistical multiplicity handling, scoring-code commit and conditional model-failure rule;
- A fully operational blinding/escrow custodian and timestamp/hash of hidden raw results;
- Definition of fatal vs recoverable instrument failure and excluded data rules set before reveal;
- Planned readout/analysis timeline and independent review board sign-off;
- File structure, repository/snapshot license and sensitive proprietary-data exceptions.

## 13. Minimal example machine schema (illustrative, NOT actual observations)
\`\`\`text
shot_id,run_id,randomization_block,facility_beam_id,sample_id,spot_xy,
sample_batch,material_arm,layer_stack_id,
boron11_areal_atoms_cm2,areal_density_unc,upstream_face_id,substrate_facing_id,
incident_proton_response_id,transmitted_proton_response_id,
alpha_upstream_detector_id,alpha_downstream_detector_id,
beam_frame,source_energy_label_verbatim,EXFOR_entry,subentry,pointer,
detector_response_version,raw_data_sha256,blind_split,model_commit,
prediction_commit,random_seed,measurement_status
\`\`\`
Measured particle hit events and simulated source reaction events MUST be separate tables with separate identifiers. Use null for unavailable columns rather than guessed constants. Every published comparison states data class and source hash.

## 14. Review questions before v0.2
1. Can a known accelerator beam and detector ensemble actually discriminate the proposed full-spectrum hypotheses at the expected low event rates? Perform pre-study power/precision and background calculations before scheduling beam time.
2. Can G0-D produce identifiable proton-vs-alpha response with documented angular acceptance and side losses?
3. Does the wedge improve statistical sensitivity after beam spot/damage/history controls, or create confounding?
4. What thickness/boron areal-column set is physically manufacturable under the relevant incoming proton range?
5. Which directly identified EXFOR measurements and helium stopping benchmarks close the nuclear-data source gate?
6. Can the full transport model make honest pre-shot predictions, or do unmeasured parameter correlations make the protocol currently untestable?

**Publication rule:** Protocol failures are evidence and remain published. Model revisions can learn from failures, but a new blind dataset is then required.

## Primary literature and source registers
- IAEA EXFOR master source: https://github.com/IAEA-NDS/exfor_master
- IAEA pointwise experimental tables: https://github.com/IAEA-NDS/exfortables_py
- IAEA Data Explorer: https://nds.iaea.org/dataexplorer/
- Stave et al. (2011): https://doi.org/10.1016/j.physletb.2010.12.015
- Sikora & Weller (2016): https://doi.org/10.1007/s10894-016-0069-y
- Copilot review text supplied by user in ChatGPT on 2026-10-27 (archival attribution, not independent experimental proof).
- [STARS v0.8](../whitepapers/STARS_2_0_v0_8_REFERENCE_DATA_CALIBRATION_AND_INTERFACE_VALIDATION_2026-10-27.md)

**Receipts in the front. Wizards in the back.**
