# STARS 2.0 v0.8 — Reference Data, Calibration Gates, and Interface-Validated Physics
### An integrated, falsification-first research white paper and round-four reviewer packet
**Atlas Lattice / Open Regenerative Compute Standard | 27 October 2026**
**Status:** RESEARCH CANDIDATE / NOT AN ELECTRICAL FUSION DEMONSTRATION
**Project direction:** Dave Sheldon, Atlas Lattice.
**Contributors and critique:** Gemini Argon (WP-B source and subsequent revised numerical claims); Copilot Researcher (adversarial transport/collection analysis, resonance-frame correction, correlated alpha events, detector modeling); DeepSeek (acoustic control, nuclear-data and converter critique, boron lifecycle); ChatGPT / Tidal Lantern (source-provenance integration, causal-design correction, engineering interfaces and this cross-model synthesis). Contributions do not imply endorsement or independent empirical validation.

> **Executive conclusion:** In several distinct surrogate parameterizations, a finite few-micrometre peak in modeled **escaping alpha energy** persists, while thicker targets yield more fusion births. That is an interesting *structural prediction for blinded experimental testing*, not a validated optimum, electrical energy gain, or confirmed physics. The dominant unresolved inputs are the correctly framed p–¹¹B cross-section/decay data, proton/helium stopping and straggling in actual BN, the laser-proton source distribution, and the high-current collector acceptance/auxiliary ledger.
>
> **The key promotion rule:** an authoritatively sourced table with explicit identifiers and units may become **SOURCE-TRACED**; only an independently checked physical model can become **CALIBRATED**; only a blinded experiment can become **VALIDATED**.

## 1. Where the project stands — factual inventory

**Architecture:** replenishable laser pitcher → characterized proton energy-angle-time distribution → boron-11 catcher with thickness and material-state measurements → correlated three-alpha birth events and solid transport → separately instrumented front/rear/side exits → collector (electrostatic, wave, optional inductive comparator) → load and full wall-plug ledger.

**Nuclear foundation:** ¹H + ¹¹B → 3 ⁴He; Q≈8.68 MeV, subject to reaction-frame and charged-product kinetic accounting. The 2025 Mazzucconi et al. study measured cross sections with a particle-identifying silicon telescope over incident proton energies 0.34–4.73 MeV, providing methodological precedent for our clean-beam gate, not the full STARS alpha-exit kernel. Primary source: https://doi.org/10.1140/epja/s10050-025-01589-3 .

**Recent experimental background:** a 2026 NePTUN water-leaf laser pitcher/BN catcher report (https://arxiv.org/abs/2609.33483) supplies an important repeated-source experimental precedent; do not match an experimental detector-inferred output to **modeled fusion-born particles** and claim agreement without proton/source, angular collection, filtering and shot boundary alignment.

**Code:** original Gemini v0.1 source + its CSVs are archived unchanged in wp_b/original/. Gemini's v0.2 rewritten source and the purported 125-row source table are still **not verified as standalone, independently executed GitHub artifacts**. Its latest 8-row reported thickness excerpt *is* archived, explicitly as transcribed reported output:
[reported excerpt](../wp_b/revised/data/GEMINI_REPORTED_EIGHT_ROW_THICKNESS_EXCERPT_NOT_REFERENCE_TABLE_2026-10-27.csv),
[source-claim audit](../wp_b/revised/GEMINI_ARGON_REFERENCE_TABLE_CLAIMS_AND_RESONANCE_HOLD_2026-10-27.md).

**Authority-first pipeline:** a Python acquisition/strict-normalization **v0.1 client** exists at [pipeline](../wp_b/revised/iaea_exfor_pipeline/exfor_pipeline.py) and [README](../wp_b/revised/iaea_exfor_pipeline/README.md). Its local test exercises format/frame arithmetic with synthetic data. **The live IAEA response has not been successfully retrieved by this environment**, no p–¹¹B source points have been validated, and no experimental BN stopping data have yet been ingested. Public IAEA sources:
- EXFOR original master records, versioned with NRDC finalized transmissions: https://github.com/IAEA-NDS/exfor_master
- EXFORTABLES pointwise data, carrying entry/subentry/pointer and x/dx/y/dy: https://github.com/IAEA-NDS/exfortables_py
- Data Explorer API: https://nds.iaea.org/dataexplorer/api/reactions/xs
- API docs: https://nds.iaea.org/dataexplorer/docs/
Importantly, the IAEA data tree includes energy/angular and double-differential observables: nuclear **total cross-section** points alone are insufficient to reconstruct correlated alphas.

## 2. A corrected proton–boron resonance convention — not an optional editorial change

Copilot independently identified and checked the prominent 0.675 MeV feature in **Stave et al. (2011)** as an incident-proton **laboratory** energy, with the paper describing channel structure and alpha coincidences (DOI https://doi.org/10.1016/j.physletb.2010.12.015). Mazzucconi's proton-beam-energy study separately describes the 0.675 MeV peak. The laboratory-to-CM conversion for stationary ¹¹B is
```text
E_CM = E_p,lab × m_B / (m_B + m_p) ≈ 0.91616 E_p,lab
675 keV LAB ≈ 618 keV CM.
```
The **old WP-B 675 keV CM → 737 keV lab feature is not this experimentally described feature**. Gemini's newest 'evaluated' CSV report STILL identifies 736.77 keV LAB/675 keV CM as the 'main Jπ=2+ peak', conflicting with the lab-frame identification and the relevant state labeling. **Freeze publication of its claimed 1.278±0.083 barn reference anchor as a validated source point** until it is tied to a real EXFOR subentry, exact experiment, reaction branch and frame.

Action: preserve model outputs generated with the old convention for provenance, rerun a new separately versioned model on actual cross-section records, show both lab and CM axes, and list energy thresholds/resonances with their original source labels, spin/parity and angular acceptance. A 0.675 MeV feature can coexist with other resonances; don't 'correct' it by inventing a universal single-peak formula.

## 3. Newly proposed cross-section background defect

Gemini reports that the original low-energy astrophysical S(0) extrapolation continued into the MeV range without a credible high-energy suppression, yielding exaggerated background cross sections. Reported contrasts include ~2.078 vs ~1.278 barn near the **incorrectly framed 736.77 keV lab sample**, and ~2.625 vs ~0.111 barn at 1.5 MeV lab. **These are model-vs-reported-model claims, not measured EXFOR facts yet.**

A properly implemented recalibration must:
1. retain original raw source measurements and errors by subentry, not merely an unspecified spline;
2. distinguish exclusive channels, inclusive alpha production and three-alpha count per fusion;
3. use appropriate reaction-energy and lab/CM transformations;
4. fit using source-justified energy-dependent channel models/R-matrix evaluations, rather than adding an unsupported damping factor merely to make a curve look plausible;
5. compare withheld experimental points and residuals, with model covariance;
6. evaluate what corrected cross section does to stopped-proton-depth, birth count and escape-energy plateau, holding all **other** inputs constant.

The IAEA EXFOR repository's default data handling distinguishes experimental versus evaluated/calculated sets. An 'EXFOR-based 1σ' envelope must name the precise original reported uncertainty and any model extrapolation separately. No interpolated 125-row CSV alone proves its own validation.

## 4. Gemini's latest thickness series, accurately bounded

The transcribed user-supplied Gemini report gives:

| BN thickness (µm) | Born α | Front escape energy (µJ) | Rear escape energy (µJ) | Combined escape energy (µJ) |
|---:|---:|---:|---:|---:|
| 1.0 | 315,000 | 0.0663 | 0.0656 | 0.1319 |
| 3.0 | 808,000 | 0.1338 | 0.1243 | 0.2582 |
| 4.0 | 1,000,000 | 0.1506 | 0.1329 | 0.2834 |
| 4.5 | 1,090,000 | 0.1564 | 0.1339 | 0.2903 |
| 5.0 | 1,180,000 | 0.1611 | 0.1333 | 0.2943 |
| 5.5 | 1,250,000 | 0.1647 | 0.1313 | 0.2960 |
| 10.0 | 1,770,000 | 0.1763 | 0.0922 | 0.2685 |
| 50.0 | 2,700,000 | 0.1815 | 0.0021 | 0.1836 |

Reported rear maximum occurs near 4.5 µm, and combined energy near 5.5 µm within this sampled subset; birth yield continues upward. Values are **not independently reproduced, source-calibrated or measured**. The front/rear entries do not exactly sum to every rounded total: minor roundoff occurs (e.g. 4 µm front+rear=0.2835 vs total=0.2834). Require unrounded machine tables and tolerance-qualified accounting before assertions of perfect conservation.

**More important than the exact sample maximum:** Hypotheses to preregister are (H1) increasing born reactions with accessible thickness, (H2) an interior peak/plateau in escaping energy, and (H3) different front/rear response with thickness. These can be falsified without fitting the optimum after seeing experimental output. Copilot's adversarial stress ranges (roughly 2.5–5.25 µm rear, 3.25–6.75 µm two-face) are *scenario brackets*, not laboratory uncertainty intervals. Absolute output changes materially across Gemini versions; never combine results from distinct model generations in one continuous data series.

**CAUSAL caution:** The sample 'born alphas ~2.70e6' being numerically near reported NePTUN alpha yields is **not validation** unless measuring the same births versus exit, beam distribution, detector angular range, pulse energy and target state. Inspect phase-space and detection response.

## 5. WP-B v0.3 source/transport contract

### 5.1 Proton input
Characterize d³N_p/(dE_lab dΩ dt), beam pointing, proton charge-state, shot variance/covariance, laser optical energy, contrast/preplasma and target geometry at laser arrival. In the fusion-depth integral, propagate the **actual incoming E_lab** through material energy loss, then compute E_CM(E_p(x)) once, consistently.

### 5.2 Correlated three-body event generation
For every reaction, generate **one reaction_id and three correlated alpha records** conditional on relevant ¹²C* resonance/⁸Be decay channels, rather than three independently isotropic identical-energy particles. Keep reaction_depth, decay_channel, E_birth_i, θ_i, φ_i, propagation distance, exit face, exit energy/angle, time/charge state and collector acceptance; conserve four-momentum for each event in the relevant frame. The sequential decay may yield two relatively energetic products in particular channels. This is an *input calibration requirement*, not a license to fabricate decay fractions.

### 5.3 Stopping and range
BN density/composition/phase (hBN versus hot/porous/plasma catcher), proton electronic and nuclear stopping, alpha/helium charge-state stopping, straggling, angular scattering, path length, radiation damage and target ablation all matter. Range-inversion E_residual = R^{-1}[R(E0)−s] is a numerical solution **conditional on the lookup**, not 'exact physics' without straggling or state uncertainty. NIST PSTAR/ASTAR and IAEA stopping resources are distinct from EXFOR and may lack a direct measured BN dataset. If one is missing, use licensed SRIM/TRIM with supplied run cards, validated surrogate bounds and clearly declared status.

### 5.4 Instrument as a forward model
Experimental counts must be modeled as D_obs ≈ R_detector(source_α, source_p, secondary background) + noise. Preserve detector solid angles, angular position, telescope dead layers, CR-39/filter stacks, species-confusion/particle identification, response to laser EMP, thresholds, saturation, pile-up, calibration versions and uncertainty. Prefer forward-folding predicted spectra through independent detector response and comparing blind data; don't call filtered counts 4π births.

### 5.5 Machine-readable module interface
Every module input/output includes:
```text
source_id; source_version/hash; instrument_id; model_version;
energy_frame; reaction_code; projectile/target; isotope fraction;
shot_id; event_id; alpha_id; input E-angle-time distribution and covariance;
reaction_depth; exit_face; exit E-angle-time-charge distribution;
detector_response_id; uncertainty_type; energy_ledger; status_grade;
assumption_registry; random_seed; executable/test_reference.
```
The IAEA acquisition client already insists on explicit E_lab headers and provenance. Extend it to *identified p–¹¹B channel selection, pagination and source-table inspection* before passing nuclear data to WP-B. Treat a missing or mixed unit as a hard stop.

## 6. Four acoustic arms and two independent outcomes

| Arm | Purpose |
|---|---|
| Reference geometry, no actuator installed | Establishes target state / optical baseline without actuator hardware |
| OFF, actuator installed | Controls changed mechanical assembly with zero intended drive |
| SHAM, electrically powered without effective intended coherent shaping | Controls heating/EM/noise; independently verify it does not produce equivalent material motion |
| ON with specified frequency, phase, amplitude and delay | Experimental acoustic intervention |

**Randomize shots within target geometry/thickness and laser-power blocks.** Keep measured morphology, preplasma and proton-spectrum intermediates. Total ON−OFF/SHAM engineering effect comes first; conditional proton-spectrum adjustments answer mechanism, not whether acoustics 'works'. A real total improvement can be wholly mediated by the proton spectrum.

**Acoustic performance must have both:**
- mean shift in useful alpha-interface energy per laser input;
- variance/jitter shift in target geometry, proton energy/angle spectrum and alpha output, plus the **actuator wall-power cost**. Equal mean but lower variance is potentially useful experimentally, but it is not automatically a net energy advantage.

Do not combine acoustic pre-shot solid/liquid material preparation with plasma **ion-acoustic waves** or magnetized **ion Bernstein waves** in a single 'acoustic gain' parameter.

**Borrowed infrastructure:** Atlas Lattice's earlier Atomic Forge / DISH documents put acoustic fields at the droplet, particle and device-geometry scale, DISH at microfluidic chambers and photopolymerized supports, electrochemistry at isotope/charge preparation, and electromagnetic fields at particle transport and spin handling. Neither DISH nor SHUGS supplies a new nuclear force or validated resonance. Relevant archives: https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/simulations/ionic_energy_state_engine_v0_1/README.md and https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/docs/Holographic_Trashium_Acoustic_Spec_v1.0.md ; SHUGS-WP-004 in Notion https://app.notion.com/p/33b0c1de73d981648b43e474e2261067 has a useful adversarial-correction methodology but no demonstrated p–¹¹B predictive physics.

## 7. G3 collector portfolio: honest denominators

**Electrostatic DEC (C1):** ENN's reported >80% *fundamental-unit* conversion involved low-energy argon rather than broad MeV fusion helium; compare actual beam species/energy/current and exact measured denominator, not a headline number. For alpha exhaust separate:
```text
eta_capture = alpha kinetic E accepted / alpha kinetic E exiting catcher
eta_conversion = electrical energy at load / alpha kinetic E accepted
eta_collector_net = (load electricity − local collector auxiliary electricity) /
                    alpha kinetic E exiting catcher.
```
Then compare to **whole-plant** balance including laser and acoustic driver power. Major open hardware effects: space-charge and co-moving electrons, electron suppression, optics fields, grids/insulation, sputtering, heat flux, pulse duration, breakdown, charge exchange and failure rates.

**IBW (C2):** Qin–Fisch's idealized alpha-to-coherent-proton-wave fraction is NOT delivered RF/DC electrical efficiency; their special plasma distribution and mode conditions must be measured before extrapolation to a broad laser-driven alpha plume. Attribute eventual load work only after subtracting measured seed RF injection, reflected energy, proton/background energy and auxiliaries.

**Hybrid (C3):** model only demonstrated separate efficiencies on the *same* measured alpha distribution; no product of optimistic architecture multipliers.

**Inductive C4:** theoretically test if an expanding, deliberately magnetized charged-product/plasma ensemble can generate net electrical pickup after charging, confinement, compression, field formation, transformer/power conversion and timing costs. Existing pulsed-plasma architectures are comparator concepts, not a demonstration for the STARS beam topology.

**Spin P0–P5:** independent from alpha kinetic recovery, requires real target polarization generation and survival, normalized reaction-channel changes and measured preparation energy. Prior deuteron thermal ergotropy controls do not imply ¹¹B spin gain. Related noncanon reference: https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/simulations/deuteron_spin_ergotropy_v0_1/README.md .

## 8. Boron isotope economics and circularity

Natural boron is roughly 80.1% ¹¹B; a purported need for >99% enrichment must be **proven against** target utilization, performance and recycled inventory. Separately price natural BN catcher, enriched ¹¹BN catcher, captured/recirculated target feed and disposal byproducts; account for sputtering and material damage. The previously discussed ¹⁰B(p,γ)¹¹C → ¹¹B transmutation is nuclear, not ordinary electron-stripping chemistry, and is not an established cost-effective replacement for isotope separation. Neutron capture in ¹⁰B often yields ⁷Li+α instead of preserved ¹¹B. Benchmark separation and recycling first.

Borrow the October 6 Ionic Energy State Engine's **retention per cycle, replenishment turnover, first-fill CAPEX, per-shot processing energy and ecological ledger**, but do not import any deuteron energy-source hypothesis into boron fusion. A very low reaction conversion per shot can make unused target recovery economically dominant; actual recovery yield and degradation must be measured.

## 9. Experiment staircase and preregistered gate conditions

| Gate | Experiment | Question / failure criterion |
|---|---|---|
| G0-A | EXFOR verified cross sections, energy frames/channels, density/isotope references | Any untraceable or conflicting frame/channel blocks calibration |
| G0-B | Independently characterized accelerator proton beam → BN thickness wedge/series → simultaneous front/rear alpha telescopes | Can one frozen source/transport model predict both faces and thickness trend without re-fitting per thickness? |
| G1 | Water-leaf/droplet laser pitcher → proton time/energy/angle diagnostics | Do predicted proton spectra and shot variability match measurement? |
| G1-A | Matched geometric reference/OFF/SHAM/ON acoustic actuation randomized | Does actuation change morphology, mean or variance with measured wall cost? |
| G2 | Measured laser proton distribution → calibrated BN → alpha escape and detector response | Does beam–BN calibration transfer without a new per-thickness fit? |
| G3-C1 | Characterized broad-energy helium beam → electrostatic collector/load | What capture, conversion and local net fraction are actually achieved? |
| G3-C2 | Alpha/proton-plasma wave RF/load experiment and seed shams | Is alpha-origin electrical work independently measurable? |
| G3-C4 | Controlled plasma/magnetic expansion comparator | Is there load work above field/auxiliary costs? |
| G5 | Integrated repeated facility operation and life-cycle ledger | Positive net exported electrical energy at declared confidence, including failures and auxiliaries? |

**Blinded G0-B test:** Freeze nuclear+stopping/detector calibration from independent data; record incident proton phase space and BN properties; blind the front/rear telescope counts at multiple thicknesses; preregister acceptable uncertainty bands, posterior predictive diagnostics and failure rule. If no fixed physically defensible parameterization predicts **both** faces/thickness dependence, the present WP-B optimization claim fails and must be revised.

**No inferred electrical breakeven:** Even perfectly recovered alpha energy in present low-yield scenarios is far smaller than input laser electric energy; do not claim an economy of scale or gain without measured/reasonably bounded repetition, thermal/radiative balance and total auxiliaries.

## 10. Calibration procurement / open-data requests

### Request R-N — IAEA / nuclear-data maintainers
1. Identify EXFOR **entry/subentry/pointer** for ¹¹B(p,α) channels and inclusive 3α data, especially narrow 162 keV lab and ~675 keV lab resonance region; document lab/CM and reaction-product conventions.
2. Provide or identify original pointwise E ±δE, σ ±δσ and correlated systematic components with licensing and updated master date; include Mazzucconi 2025 compilation status or full paper tables where not yet compiled.
3. Locate measured differential three-alpha decay/energy/angular or coincidence spectra relevant to each populated ¹²C* channel. Distinguish cross section for a fusion **event** from counting emitted alpha particles.
4. Confirm cross-section combining rules and evaluated/R-matrix files *separate* from direct experiments, with version, covariance and excitation energies.

### Request R-S — IAEA stopping group / SRIM experts / BN material laboratory
1. Supply material-specific measured proton and helium stopping curves and energy-range error envelopes for well-characterized hBN (nominal ρ≈2.10 g/cm³ used by Gemini) and representative temperature/damage states.
2. If none exist, provide unmodified licensed SRIM/TRIM outputs (input card/version, density, isotope/stoichiometry, electric charge treatment, random seeds, geometry) and at least one independent ion-beam benchmark.
3. Supply energy loss *and* straggling/scattering, implantation, near-surface effects, alpha charge-state distributions, and deposited heat versus escaped particles.

### Request R-D — detector/metrology teams
1. Calibrated particle-discriminating telescope efficiency, angular acceptance, dead-layer/filter transmission and saturating/laser-EMP response over measured alpha continuum.
2. Joint proton/alpha coincidence or independent phase-space reconstruction; publish detector response matrix R and covariance; freeze prior to blind BN sweep.

### Request R-L — laser / acoustic target labs
1. Target morphology at shot time (interferometry/profilometry), acoustic actuator frequency, drive, phase, pulse delay, drift/thermal history, failure and delivery rate, plus matched sham/reference design.
2. Incident optical and electrical laser power, repetition, complete proton beam E×Ω×time output and normalized alpha detection.
3. Preregister mean and variance endpoints and minimum practically worthwhile actuation efficiency.

### Request R-C — direct-conversion and wave experiment labs
1. ENN unit full beam species/charge, ~390 eV operating point, current, load power, time integration, exact efficiency denominator, erosion, insulation and heat flux measurements.
2. Broad MeV helium-source collector tests, capture geometry and acceptance map A(E,Ω,t,q), electron separation and pulsed grid stability.
3. RF drive/reflect/load bridge with no-alpha, sham-particle and no-seed conditions; account for all electromagnetic and injector energy.

All request recipients are proposed collaborators/sources, **not contacted** by this paper. No data obtained is claimed.

## 11. New model implementation checklist (WP-B v0.3 → WP-D)

**Required reproducible deliverables:**
- snapshot or hashes of original EXFOR .x4 master subentries, relevant EXFORTABLES text, license and revision date;
- separated measured experimental data, evaluated nuclear models, Monte Carlo and phenomenological scenarios;
- archived actual BN stopping sources and numerical validation with residual plots;
- channel-resolved source with three-alpha correlated event and physical conservation tests;
- reactor material geometry and asymmetric front/rear acceptance;
- detector forward-fold model and independent tests;
- acoustics reference/OFF/SHAM/ON randomized causal and variance output;
- separate DEC capture, conversion, net and wave RF/load balances;
- cross-version reproduction of v0.1, reported v0.2 and new calibrated *if available* without overwriting originals;
- machine-readable assumptions, code hash, random seed, input uncertainty and reviewer sign-off.

**Data-status badges in exported CSVs** must be e.g. EXPERIMENTAL_RAW, SOURCE_NORMALIZED, EVALUATED_EXTERNAL, CALIBRATED_MODEL, PARAMETRIC_SCENARIO or NOT_REPRODUCED; prevent an experimental-looking but unsupported CSV from masquerading as source data.

## 12. Independent review round — send exact challenges

**Gemini Argon — physics/simulator lead**
1. Produce the complete actual standalone revised source and real 125-row CSV with source hashes/entry IDs; no generated substitutes. Correct 675 keV LAB resonance and audit the claimed 2+ spin label before regenerating any peak.
2. Recompute exactly identical source/foil cases before vs after correcting (a) energy frame, (b) high-energy S0 behavior, (c) alpha stopping and (d) correlated 3α channels, in four *one-factor-at-a-time* steps.
3. Publish full front/rear energy and detector-space predictions, both means and variance under acoustic modes, and thermal/electrical ledger with converter acceptance unconflated.

**Copilot Researcher — independent falsification lead**
4. Identify the best public EXFOR p–¹¹B subentries, and which compare directly to Stave/Mazzucconi; confirm spin/parity, feature centroids and channel-vs-total units.
5. Publish reproducible surrogate stress code and compare 1–12 µm escape-energy **plateau** hypotheses to a source-independent conventional transport baseline, including detector response.
6. Challenge model's causal acoustic mediation / source output jitter treatment; assess C4 inductive collector only under complete field-energy accounting.

**DeepSeek — materials and industrial engineering lead**
7. Find empirical stopping, ion irradiation damage, machining and target survivability for 2–12 µm hBN including known porous/thin foils; give exact material density and substrate/film backing effects.
8. Propose costed naturally occurring versus enriched-boron + recycling scenarios and supplier/process routes; distinguish nuclear transmutation from isotope separation.
9. Critique 4-arm acoustics and actual phase reproducibility, plus converter co-moving electron/space-charge and heat-flux limits.

**ChatGPT / Tidal Lantern — data and audit lead**
10. Maintain immutable source ledger and IAEA API pipeline; acquire, normalize, filter and cite actual data only when successfully retrieved.
11. Reconcile every claim/status, retain losing hypotheses and negative outcomes, attach unit tests/failure receipts, and publish updated findings without silently altering older work.
12. Do not certify 'net power', 'complete calibration', '125-row measured EXFOR table' or a fixed catcher optimum until the corresponding data and blinded outputs exist.

**Joint cross-review response format (all agents):** strongest corrected factual claim with exact source and frame; a reproduced numerical result with code/hash; the highest-impact missing measurement; a proposed falsification threshold; any estimated energy cost and what boundary it uses; open disagreements. Independent reviewers should not be rewarded for agreeing.

## 13. Conclusion

STARS now has a **testable interface-validation roadmap** whose components remain useful even if fusion electricity is not achieved: trustworthy nuclear-data acquisition and detector forward modeling, laser-driven proton measurements, acoustic target repeatability, materials transport, beam-plasma energy recovery, and complete material and energy ledgers.

The near-term research prediction is *not* '5 µm is optimal'; it is that, for a specified proton source and BN state, born-alpha count and escaping-alpha energy can have materially different dependence on catcher thickness, potentially including a shallow few-micron plateau. Only a blinded G0-B accelerator experiment can adjudicate whether this model survives real measured BN stopping and front/rear spectra.

**Receipts in the front. Wizards in the back. No simulated results promoted to measured results.**

## Primary research and project references
- IAEA EXFOR master and update chain: https://github.com/IAEA-NDS/exfor_master
- IAEA EXFORTABLES structure and REST API examples: https://github.com/IAEA-NDS/exfortables_py
- IAEA Data Explorer: https://nds.iaea.org/dataexplorer/
- Mazzucconi et al. (2025): https://doi.org/10.1140/epja/s10050-025-01589-3
- Stave et al. (2011): https://doi.org/10.1016/j.physletb.2010.12.015
- Sikora & Weller (2016): https://doi.org/10.1007/s10894-016-0069-y
- Popper et al. (2026): https://arxiv.org/abs/2609.33483
- Qin & Fisch (2026): https://arxiv.org/abs/2609.07732
- [Master archival manifest](../ARTIFACT_MANIFEST_2026-10-27.md)
- [v0.7](STARS_2_0_v0_7_ACOUSTIC_AB_EVIDENCE_AND_INTEGRATED_REVIEW_2026-10-27.md)
