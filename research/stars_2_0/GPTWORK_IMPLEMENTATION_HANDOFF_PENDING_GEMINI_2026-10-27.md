> **GEMINI v0.5 PROPOSAL TRIAGE (2026-10-27):** [Read v0.5 audit: relativistic invariants, scattering A/B, cryogenic scope](reviews/GEMINI_V05_PROPOSAL_RELATIVISTIC_SCATTERING_AND_CRYOGENIC_SCOPE_AUDIT_2026-10-27.md). Adopt exact-mass 4-vector sequential-decay refactor, and test layer-specific angular scattering OFF vs ON without assuming 3–7° or thickness-optimum direction. Gemini's W expression as supplied is frame/dimension ambiguous: implement s=(P_p+P_B)^2 and W=sqrt(s) from physical input four-vectors. LNG/desal cryogenic cascade is a separate speculative future systems option, not WP-B v0.5 scientific gate. **No new engine has been coded or independently validated from this proposal.**

> **INDEPENDENT EXECUTION UPDATE — 2026-10-27:** Actual Gemini v0.4 source has now been received and executed independently in this conversation: 2/2 original bundled tests pass, all five CSVs generated. **Important A/B discrepancies:** collector optimum 7.0 μm on full 16-point grid vs previously reported 6.0 μm; Newman phases produce crest 5.12, not 3.62 (3.62 comes from different phase sequence); lower max crest can increase occupancy above 2.2× RMS; original code uses toy effective B mass/internal momentum units, hard-coded spectral quadrature for main sweep and BN stopping for foreign backing materials; source needs NumPy+SciPy despite header claiming no dependencies; zero-sigma null passed but zero-output CV becomes NaN. Read the [complete independent execution and A/B report](reviews/GEMINI_V04_INDEPENDENT_EXECUTION_AND_AB_REGRESSION_GATES_2026-10-27.md) before coding. This **supersedes the earlier 'code not received' status** but does not mean physics-calibrated, scientifically frozen, or GitHub source committed. The project-lead contract freeze remains pending after reconciliation. Original file/outputs are downloadable from originating ChatGPT conversation, not yet committed as complete runnable source to GitHub.

> **GEMINI FINAL REVIEW STATUS UPDATE — 2026-10-27 EVENING:** Gemini Argon delivered a **text-only v0.4 result report** (received and critically reviewed), but the claimed full Python suite and five CSV outputs remain unavailable. [Read the source-attributed Gemini v0.4 review](reviews/GEMINI_ARGON_V04_REPORTED_RESULTS_HARMONIC_CREST_FACTOR_AND_REPRODUCIBILITY_AUDIT_2026-10-27.md). Treat the review phase as *partially received*; **do not freeze the implementation contract until actual code/CSV artifacts are retrieved and the project lead approves the reconciliation**. The original heading below reflects the state at initial handoff and is preserved for provenance.

# STARS 2.0 — GPTWork Implementation Handoff / Implementation Contract Candidate
**Atlas Lattice / ORCS | Prepared 2026-10-27 | Project lead: Atlas Lattice**
**HANDOFF STATE: REVIEW PENDING — GEMINI ARGON FINAL REVIEW NOT YET INGESTED**
**Audience:** GPTWork / ChatGPT Work (software implementation, repository QA, reproducible artifacts, independent computational reviews), future research collaborators.
**Source of truth:** https://github.com/atlaslattice/open-regenerative-compute-standard

> **HARD START CONDITION:** Do not interpret this document as authorization to freeze scientific acceptance criteria or begin a blinded G0-B prediction release. Gemini Argon's final contribution is **incoming and not yet incorporated**. After the project lead provides it, append a separately attributed response, reconcile disagreements, then publish a frozen versioned implementation contract approved by the project lead. Routine repository discovery and planning can precede the freeze. This document is a deliberate pre-handoff scaffold, not a claim that the code has already been built.

## 0. Required discovery steps for GPTWork (DO NOT SKIP)
On starting the task:
1. Read this document from the GitHub repository default branch, then verify the latest commit. Do **not** work from a memory excerpt or assume older paper summaries are complete.
2. Read [v0.9 scientific synthesis](whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md), [artifact ledger](ARTIFACT_MANIFEST_2026-10-27.md), [researcher metadata and discovery gateway](RESEARCHER_DISCOVERY_AND_REPRODUCIBILITY_README.md), [original EXFOR dataset](wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv) and [source-meaning audit](reviews/DEEPSEEK_POST_EXFOR_REVIEW_AND_TEST_ANCHOR_CORRECTIONS_2026-10-27.md).
3. Read [Copilot final preflight](reviews/COPILOT_FINAL_PREFLIGHT_ZERO_PHYSICS_ZERO_MAGIC_2026-10-27.md), [DeepSeek source/safeguards](reviews/EXFOR_C2973_PRIMARY_DATA_RECOVERY_AND_DEEPSEEK_FINAL_SAFEGUARDS_2026-10-27.md), [Gemini pasted-module code audit](reviews/GEMINI_V03_PASTED_MODULE_CODE_AUDIT_2026-10-27.md), [G0-B experimental protocol](protocols/G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md), and [lockfile scaffold](protocols/g0_b_lock/README.md).
4. Look for a later "**Gemini Argon final review**" artifact and a project-lead-approved frozen contract. **If neither exists, STOP before claiming implementation is scientifically frozen.** Surface the missing review as a blocker, do not invent its findings.
5. Run all existing tests first, record environment and failures, and preserve legacy prototype results untouched. Do not silently overwrite old model source, CSV, null results, scientific assumptions or model limitations.

## 1. Agreed order of operations

```text
Gemini Argon final review (PENDING)
  ↓
Cross-model synthesis (Gemini Argon + Copilot + DeepSeek + ChatGPT/Tidal Lantern)
  ↓
Reconcile contradictions; sign-off and FREEZE versioned implementation contract
  ↓
GPTWork creates a development branch, implements reusable framework and STARS-specific configuration
  ↓
Zero-physics / analytic-limit verification suite
  ↓
Original EXFOR source-record reproduction and observable-semantics tests
  ↓
Nuclear kinematics, stopping, detector and statistical-model calibration
  ↓
Publish reproducible source, fixtures, error receipts, dependency locks and negative findings
  ↓
Independent code/research review and versioned open-source release
  ↓
Only then: freeze G0-B experimental predictions under independently reviewed blind protocol
```

Do not reverse this order merely to produce attractive plots or a positive fusion number.

## 2. Two independent, useful deliverables

**Deliverable A — Generic, portable, tested nuclear charged-particle simulation methodology.**
Reaction registry and typed nuclear observables; EXFOR/raw-source import and snapshot/hash manifest; mass/Q/frames; channel-aware sequential decay; conservation tests; material/particle stopping interfaces; forward detector modeling; uncertainty types and nuisance parameters; reproducibility; statistical blind controls; provenance and failure receipts. Another researcher should be able to swap reaction, material, detector, data source, or stopping model without rewriting the whole system.

**Deliverable B — STARS 2.0 p–¹¹B research configuration.**
Physically justified proton-source distribution and ^11B catcher, target stack/front/rear/side geometry, 3-alpha event channels, EXFOR source mapping and correct multiplicity, shot-state uncertainties and acoustic experimental controls, optional calibrated alpha collector and whole-system power accounting. Explicitly label unverified acoustic/catcher/collector branches as hypotheses; do not assume a thickness optimum or electrical energy gain.

Documentation, unit tests, machine-readable datasets and null outputs are first-class artifacts, not afterthoughts. The framework's scientific value does **not** depend on proving acoustic gain or net-electric fusion.

## 3. Immutable research constraints / evidence types

- **Quantity kind is typed and protected.** `ALPHA_PRODUCTION_DETECTED_WINDOW`, `ALPHA_PRODUCTION_EXTRAPOLATED_TOTAL`, `FUSION_EVENT_CROSS_SECTION`, `EXCLUSIVE_CHANNEL_CROSS_SECTION`, `DIFFERENTIAL_ALPHA_CROSS_SECTION`. Never convert by implicit factor three. Spraker EXFOR C2973002 is not automatically a fusion reaction-event cross section; Sikora–Weller's restricted-window extrapolation and event conversion require explicit independent treatment.
- **Always track original source metadata:** EXFOR entry, subentry, pointer, reaction notation, gamma/alpha channel, instrument, detector angular and energy window, energy in laboratory versus center-of-mass, units, statistical error, correlated systematic, paper DOI, retrieval URL, raw source SHA/file hash, and transformation history.
- **Nuclear LAB/CM convention:** 675 keV *incident proton LAB* ≈618 keV CM on stationary ^11B. For a full stationary-target p–¹¹B →3α event, total output kinetic energy **LAB ≈ Q + E_p,lab ≈ 9.35 MeV** at 675 keV LAB; **CM ≈Q + E_CM≈9.30 MeV**, using consistent precise masses. Do not impose fixed 3.76/2.74/2.74 MeV alpha energies. Require 3 correlated alpha momenta per event through ^8Be sequential channel decay, with energy/four-momentum closure.
- **Stopping/material:** do not fit entire BN stopping power `S(E)` to one quoted 2.5 MeV range. The 57 µm point requires a traceable exact primary-paper or SRIM configuration receipt. Check multiple energies, local stopping and range inversion; include geometry, areal ^11B atom density, density, phase, film/support and straggling. Distinguish static accelerator catcher from laser-driven hot target and assess time dependence only when relevant/measured.
- **Detector:** forward-fold spectra and noise into detector-space observables. G0-B accelerator and laser EMP contexts differ. Use silicon particle-ID as baseline comparator; diamond/SiC/fiber-optic readout optional subject to actual qualification.
- **Statistics:** fit background to instrument-matched blanks, detector/EMP controls where applicable, test overdispersion; Bayesian or frequentist decision thresholds must be preregistered and calibrated. `BF10>10` is not a universal proof standard.
- **Acoustics:** randomized REFERENCE (hardware absent), OFF, SHAM and ON arms, measured mediator/timing, independent negative controls; no artificial `ON_gain` parameter passed off as observed mechanism. Distinguish mean escaping alpha energy, distribution/jitter, qualified shot fraction and cost per qualified experiment. Null effect is publishable.
- **Collection and energy ledger:** alpha birth → alpha exit → collector acceptance → gross electrical → local auxiliary → whole wall-plug; source and collector benchmarks must use same phase space and energy units. No current evidence for net electric fusion.
- **Evidence stages:** REPORTED → CODE-SPOT-CHECKED → SOURCE-TRACED → SOURCE-REPRODUCED → CALIBRATED → BLIND-VALIDATED. No stage promotion without receipts. Missing scientific data in a run declared calibrated must **fail closed**; optional surrogate research runs must have explicit non-calibrated mode.
- **Preserve original artifacts, all failed tests and superseded hypotheses** with append-only research lineage and source hashes. A model agreement produced by compensating errors is not validation.

## 4. Copilot proposed preflight tests (IMPLEMENT; DO NOT REPORT PASSED UNTIL ACTUALLY RUN)

```text
N0 EXFOR importer: exact entry/subentry/pointer/observable/units/LAB frame/ERR-S plus common systematic
N1 Alpha-count observable-vs-event-cross-section typed distinction and explicit valid conversion
N2 Held-out cross-section point prediction with prespecified error/coverage
K0 Four-momentum energy & momentum conservation per correlated 3-alpha event in CM and LAB
K1 Two-stage ^12C*→alpha+^8Be*→3alpha kinematics, channel-aware correlated spectra
S0 BN proton range point only after exact source/methods receipt; otherwise BLOCKED
S1 Local stopping S(E) at multiple incident and depth-degraded energies; source-specific tolerance
S2 Numerical CSDA range integral/inverse consistency, bounded energy-domain handling
T0 Analytic slab alpha escape probability vs MC at uniform births and fixed range
T1 Zero stopping / constant source: correct analytical reaction depths and unchanged exit energies
T2 Infinite alpha range: every geometrically exiting alpha retains birth energy
T3 Front/rear symmetry for a symmetric slab and symmetric alpha source
D0 Forward detector response on independently known injected particle distributions
D1 Held-out blank/control background spectra and count/waveform likelihood calibration
C0 Catcher/collector energy ledger closure with explicit deposited, escaping and omitted terms
Z0 ZERO PHYSICS → ZERO MAGIC: sigma=0 yields exactly zero fusion births, exactly zero fusion Q and alpha products, while nonfusion backgrounds and input power remain separately accounted
```

For constant isotropic alpha births over slab thickness L and fixed alpha path range R, ideal two-face escape probability is:
```text
P_escape = 1 - L/(2R),  R >= L
P_escape = R/(2L),      R <= L
```
under declared ideal planar assumptions; each face half by symmetry. This is a geometry fixture, not a measured BN transport prediction.

The tests themselves have a versioned source/assumption registry, expected output, exact tolerance justification and pass/fail machine report. Tests use analytic fixtures, original source data and independent numerical reference solutions; do not “tune for green” by mutating expected values.

## 5. Implementation structure proposal (GPTWork may adjust only with documented reasons)

```text
research/stars_2_0/
  README.md or RESEARCHER_DISCOVERY_AND_REPRODUCIBILITY_README.md
  contracts/
    STARS_2_0_WPB_V04_FROZEN_IMPLEMENTATION_CONTRACT_[date].md    # CREATE ONLY AFTER GEMINI+SIGNOFF
  engine/                       # future portable source
    nuclear_sources/
    observables/
    reaction_registry/
    kinematics/
    stopping/
    material_stacks/
    detectors/
    stats/
    experiments/
    ledgers/
    provenance/
  configurations/
    pb11_stars/
  tests/
    fixtures/
    test_nuclear_sources.*
    test_observable_types.*
    test_kinematics_conservation.*
    test_stopping_and_ranges.*
    test_slab_analytic_nulls.*
    test_detector_response.*
    test_energy_ledger.*
  reports/
    verification_runs/
    failures/
    release_receipts/
  whitepapers/                   # preserve versioned originals
  wp_b/original/                 # DO NOT overwrite
```

Preferred implementation language Python with a reproducible dependency lockfile, deterministic seeds, unit-dimension testing and CI. Specify actual dependency versions only after execution in the target environment; do not invent passing CI badges or versions.

## 6. GPTWork execution discipline

1. Build in a fresh development branch where possible; make small, reviewable commits, not one opaque rewrite.
2. Run tests and record exact invocation, environment, package versions, raw source hashes, seed, code commit and a complete failure summary. If environment cannot run them, leave status NOT RUN, not PASS.
3. If source data is missing, document and open an issue or source-request ticket as appropriate; do not fabricate EXFOR, BN stopping, alpha spectra, instrument calibration, or measured acoustic effects.
4. If an external finding disagrees with published science, preserve the discrepancy, check units/observable/frame/detector, seek independent replication and do not assume either side is right without evidence.
5. Publish a human-readable report, machine-readable outcomes and reproducible files; invite adversarial forks and preserve null results.

## 7. Stop/go decision

**GO NOW for:** source discovery, code architecture planning, data parser reproduction, analytic null fixtures and conservation test specifications, after authorized task kickoff.

**NO-GO without Gemini reconciliation and frozen contract:** declare WP-B v0.4 scientifically accepted, change numerical source anchors silently, release final blind G0-B predictions, claim positive acoustic/nuclear gain, claim a working high-voltage collector or net electricity.

**Project-lead request to GPTWork after freeze:**
> Read the root repository pointer and this handoff, ingest the final Gemini review and signed-off frozen implementation contract, implement the portable research framework and STARS p–¹¹B configuration, run strict physics verification tests and source reproduction before fitting, keep full failure receipts, and publish a versioned open-source software release. Do not publish blind G0-B predictions until validated source meaning, stopping, detector and held-out calibration gates are passed.

## 8. Credit, philosophy and source pointers

- Project origin and direction: Atlas Lattice project lead.
- AI model contributions: Gemini Argon, Copilot Researcher, DeepSeek and ChatGPT/Tidal Lantern; attribution records analyses and proposal authorship, not independent empirical validation.
- **Copilot:** “Zero physics produces zero magic”; “Wrong observable, wrong wizardry”; “Conservation before celebration”; “Release the code, preserve the failures, and let the forks begin.”
- Atlas research ethic: **“Reality may defeat a wizard, but it cannot delete their commit history.”**
- These are research-team mottos / design invariants, **not** changes to canonical Aluminum OS numbered invariants.
- OpenAI harmonic analysis / ETH / constructive-QCD announcement: research-method leads only; no assumption that they establish acoustic fusion gains.

**This handoff is deliberately pending Gemini Argon's final response. Nothing in it is evidence that Work has run yet.**
