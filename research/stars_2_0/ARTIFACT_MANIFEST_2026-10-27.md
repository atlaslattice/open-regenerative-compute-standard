# Stars 2.0 — Artifact Manifest and Preservation Ledger
**Atlas Lattice / ORCS | 2026-10-27 | Maintainer-led, source-attributed, falsification-first**

This is a **preservation manifest**, not a claim that every file mentioned historically has been recovered. Original contributions are kept separate from later scientific corrections. Gemini Argon, DeepSeek, Copilot, and ChatGPT/Tidal Lantern are credited for their respective research, proposals, reviews and editing; project initiation and direction belong to Atlas Lattice.

## In-repository artifacts verified by commit in this conversation

### White papers
- [v0.2 Markdown — original paper](whitepapers/STARS_2_0_RF_v0_2_updated_whitepaper.md), committed 2ba3af6c4c918ce14a205ffcbc781f1ba1694088.
- [v0.3 architecture](../stars-2-0-modular-pb11-acousto-optical-energy-conversion-whitepaper-v0.3-2026-10-27.md), committed 1dac8054bc80b136122c3512bd0c2249c8c91ee0.
- [v0.4 electroacoustic and alpha recovery](../stars-2-0-modular-pb11-electroacoustic-alpha-recovery-whitepaper-v0.4-2026-10-27.md), committed b0af48ff2d9301908fb21433407249d8cc60c6ee.
- [v0.5 evidence integration and experimental roadmap](../stars-2-0-v0.5-evidence-integration-2026-10-27.md), committed 36d7207710e824e9524518bcb88157fdcbd8c488.

### Provenance and peer critique
- [Multi-agent provenance and Gemini Argon/DeepSeek source audit](../provenance/STARS_2_0_MULTI_AGENT_PROVENANCE_AND_GEMINI_ARGON_AUDIT_2026-10-27.md), committed 2cc4e7a6fec147f45709cb63da8b76414e393e2d.
- [Copilot review synthesis with reproducibility checks](../provenance/STARS_2_0_COPILOT_WP_B_CODE_REVIEW_2026-10-27.md), committed af9007642b8a61b17a9f3623e806b794b1e1845c.
- [Full supplied Copilot review text](reviews/COPILOT_WP_B_FULL_REVIEW_2026-10-27.txt), committed d5123f62d68f424eecebad5996cefad39c1ddb7c.

### WP-B original baseline — preserve unchanged
- [Gemini Argon original Python simulator](wp_b/original/stars_2_0_wp_b_gemini_argon_original.py), commit 396900a402f7212d131f8af8c500da98f7a8f358.
- [Gemini Argon original as-received paste](wp_b/original/GEMINI_ARGON_AS_RECEIVED_2026-10-27.md), commit 3c7d181dd205448df0fafe983ce1e34d8d78fcf0.
- [Original thickness-sweep CSV](wp_b/original/stars_2_0_wp_b_thickness_sweep.csv), commit 76461a1495ce650ef16d9a6b39dd4e670d68fe00.
- [Original bundled-factorial CSV](wp_b/original/stars_2_0_wp_b_factorial_results.csv), commit b2530537fcda724becfd15b75b1eef239d6677d4.
- [Original alpha recovery scenario CSV](wp_b/original/stars_2_0_wp_b_g3a_recovery_comparison.csv), commit a0ddac4b07780a02879f9bb94e7040708878d26a.

## Status legend
**Original / archival**: a faithful preservation of user-supplied source, with no implied endorsement.
**Reviewed**: criticisms and issue list recorded, not necessarily fixed.
**Validated**: independently benchmarked against original numerical/experimental sources (not yet achieved for WP-B).
**Exploratory**: model settings are hypotheses; comparisons conditional on their assumptions.
**Net-electric proof**: requires measured complete positive energy balance with uncertainties (not achieved).

## Known gaps and planned repairs
- The formatted v0.2 DOCX exists as a conversation artifact but is **not in this GitHub manifest as a binary commit**; the Markdown content is saved. GitHub connector available here supports text files; original Word file can be handled separately.
- A separately generated Gemini markdown numerical report beyond the supplied code/CSV is **not currently verified as a complete original file**. No imaginary artifact or report is claimed uploaded.
- The **entire original DeepSeek Chinese transcript(s)** are not yet committed verbatim, but are attributed and summarized in the source audit and whitepapers. The archival record contains the review claims and their provenance, not all original messages.
- The original source and CSVs are not physics-calibrated. Copilot found surrogate cross-section, stopping-law calibration, two-face alpha escape vs downstream collection, confounded factorial factors, thermal ledger allocation and hardcoded conversion scenario deficiencies.
- A **repaired WP-B v0.2 code version** must be kept separate from the untouched Gemini baseline. Required tests include cross section dataset provenance, proton and helium stopping/range, front/rear escape, all particle/thermal flow boundaries, factorial independence, uncertainty and conservative converter stage input accounting.
- Underlying v0.1 historical white paper is referenced in earlier research but not independently verified as committed in this manifest.

## Suggested directory layout
```
research/stars_2_0/
  ARTIFACT_MANIFEST_2026-10-27.md
  whitepapers/STARS_2_0_RF_v0_2_updated_whitepaper.md
  reviews/COPILOT_WP_B_FULL_REVIEW_2026-10-27.txt
  wp_b/original/{Gemini code, as-received paste, three CSVs}
  wp_b/revised/ [future repaired code and tests, NOT overwrite]
```

**No-harvest, no-overwrite research policy:** preserve original artifacts, publish provenance, mark superseded assumptions as superseded, and add corrected versions without silently revising the originals.

## New checkpoint — Stars 2.0 v0.6
- [v0.6 integrated white paper: WP-B audit, conservation corrections, and reviewer questions](whitepapers/STARS_2_0_v0_6_WP_B_AUDIT_AND_INTEGRATED_RESEARCH_WHITEPAPER_2026-10-27.md), committed a306bf804e8fff912f6ad96a4764921a8d5f4b49 on 2026-10-27.
- This adds new analysis only. Original Gemini Argon code and three generated CSVs remain unmodified; Copilot's supplied full text and DeepSeek/Gemini attribution remain separately archived.
- The WP-B audited replacement code is **planned, not yet committed**. Do not interpret this new white paper as a replacement for validated transport data or as a physical net-power claim.

## New review: DeepSeek on v0.6
- [DeepSeek v0.6 review and source-correction register](reviews/DEEPSEEK_V0_6_REVIEW_2026-10-27.md), commit afd1823cbd92ef9e4fc3476c03480de6e7a9a558. Preserves timing and target-preparation suggestions, DEC concerns, natural ¹¹B abundance qualification, ICRU 49/73 correction, and specific questions awaiting primary-method verification. This file is an attributed digest, not a verbatim review.

## Gemini Argon WP-B revised-model checkpoint (October 27, later review)
- [Gemini's complete user-supplied results report](reviews/GEMINI_ARGON_WP_B_V02_RESULTS_AS_RECEIVED_2026-10-27.txt), commit 81b7738718eea824f1ea1dbc630f65a5ef45ba56.
- [Preliminary review of revised model source shown in chat](reviews/GEMINI_ARGON_WP_B_V02_PRELIMINARY_CODE_AUDIT_2026-10-27.md), commit 5ba8c3bd16265b202c43225506b2c2f1b82dd038.
- The *complete revised v0.2 .py source file and its newly generated CSV outputs* have **not yet been committed as standalone originals**. The code appeared as text in chat; do not assert full independent execution or experimental validation until received as files and rerun. v0.1 model remains preserved separately.

## Stars 2.0 v0.7 synthesis checkpoint
- [Complete v0.7 white paper — acoustic A/B, alpha escape, converter reality and multi-agent falsification](whitepapers/STARS_2_0_v0_7_ACOUSTIC_AB_EVIDENCE_AND_INTEGRATED_REVIEW_2026-10-27.md), commit a41a60765b68b4af8d4d0ac0cb9c21b672444e85.
- Includes new acoustic ON/OFF/SHAM causal design, source-boundary evidence table, Copilot/DeepSeek/Gemini reviewer disagreements, pending resonance-reference reconciliation, independent ChatGPT/Tidal Lantern analysis and numbered reviewer challenges.
- Does NOT claim verified v0.2 revised Python runtime, experimental acoustic gain, a unique BN thickness optimum, or net electrical fusion.

## DeepSeek v0.7 and boron isotope pathway review
- [DeepSeek v0.7 source/data/acoustic/DEC review and B-10→B-11 transmutation-vs-enrichment audit](reviews/DEEPSEEK_V07_REVIEW_BORON_ISOTOPE_PATHWAYS_2026-10-27.md), commit f4ba7906b8fcdcf5daad0f1d99f9196584780427.
- Retains source-claim boundaries: natural ¹¹B vs enrichment economics, ¹⁰B(p,γ)¹¹C→¹¹B isotope production, ¹⁰B(n,α)⁷Li competing pathway, 2026 boric-acid extraction demonstration, and independent acoustic OFF/SHAM/ON controls.
- Review is an attributed digest and verification supplement; latest original DeepSeek prose remains in the chat rather than a separately committed verbatim transcript.

## Gemini Argon reported cross-section/stopping table (late Oct 27)
- [Source-claim and resonance-frame audit](wp_b/revised/GEMINI_ARGON_REFERENCE_TABLE_CLAIMS_AND_RESONANCE_HOLD_2026-10-27.md), commit d0d02993cdff5e8708feef57788380704612bac9.
- [Eight-row reported thickness excerpt, **NOT** source table](wp_b/revised/data/GEMINI_REPORTED_EIGHT_ROW_THICKNESS_EXCERPT_NOT_REFERENCE_TABLE_2026-10-27.csv), commit db583387f742aa2e5e3ea3d561cb56d9a1473c6a.
- The named original `stars_2_0_reference_nuclear_stopping_tables.csv` with purported 125 rows was **NOT RECEIVED**. No claim of independent execution or validated EXFOR/SRIM calibration. The proposed 675 keV CM = 736.8 keV lab feature conflicts with Stave et al.'s **675 keV incident lab** resonance and requires source-frame and spin/channel reconciliation before promotion.

## Copilot OneDrive spreadsheet links (unretrieved)
- [Original reference CSV and corrected spreadsheet bundle — exact OneDrive links, source-status warning](wp_b/revised/ONEDRIVE_COPILOT_SPREADSHEET_SOURCE_POINTERS_2026-10-27.md), commit 5abd323589a0d9142221796e7b51ac1876ecf10c.
- Both OneDrive links were preserved exactly but **neither spreadsheet's bytes have been retrieved, inspected, or verified**. No source CSV is claimed archived.

## IAEA EXFOR primary-data interface — 2026-10-27
- [Runnable Python EXFOR acquisition / experimental-table normalizer](wp_b/revised/iaea_exfor_pipeline/exfor_pipeline.py), commit d74aed7dc2a31351133ba3cc30045fc492c3aa36.
- [Data registry, API usage, reproduction instructions and limitations](wp_b/revised/iaea_exfor_pipeline/README.md), commit 6619ce490ad491d8b90cbd86cd69d1a91a36d50c.
- Status: **SOURCE INTEGRATION SCAFFOLD PUBLISHED; NOT YET LIVE VERIFIED**. Local fixture tests were run on a related prototype; live IAEA endpoint could not be reached, and no real p–¹¹B data were downloaded or validated. EXFOR reaction channel/energy-frame selection and material-specific BN stopping remain mandatory gates.

## Stars 2.0 v0.8 — authoritative nuclear data and next peer-review round
- [v0.8 complete integrated whitepaper: calibration gates, nuclear-data interface, acoustic randomized controls and reviewer challenge packet](whitepapers/STARS_2_0_v0_8_REFERENCE_DATA_CALIBRATION_AND_INTERFACE_VALIDATION_2026-10-27.md), commit cef6240ffdfbafbe9d1168610dd81a28e10c881c.
- Explicit data requests: EXFOR nuclear-channel source IDs/uncertainties, BN proton/He stopping/straggling, front/rear detector response, target acoustic metrology, beam-to-load converter tests. Twelve named Gemini Argon, Copilot, DeepSeek, ChatGPT reviewer challenges included.
- **Not calibrated/validated yet:** IAEA live API import unverified; original purported 125-row Gemini table and revised executable unavailable; few-micrometre plateau and converter recovery remain model-reported, not measured.

## DeepSeek cross-domain engineering review of Stars v0.8
- [Source-checked engineering integration: diamond/SiC detectors, printed BN vs deposited film, tungsten grids, spin, Bayesian optimization and B-10 activation](reviews/DEEPSEEK_V08_CROSS_DOMAIN_ENGINEERING_AUDIT_2026-10-27.md), commit 269430a3c07dcc858de78d676894baeb917dded9.
- Technical boundaries: DISH ~19 µm photopolymer resolution is not a demonstrated 4–6 µm BN catcher; B-10(p,gamma)→C-11→B-11 is real but no meaningful same-shot enrichment; spin enhancement and tungsten collector performance not yet experimentally validated in Stars.
- Review integrated as sourced **v0.9 candidate branches**, not a revised v0.8 calibration or fully verified model.

## DeepSeek hybrid target manufacturing clarification
- [DeepSeek hybrid BN catcher follow-up and substrate/interface audit](reviews/DEEPSEEK_V08_HYBRID_BORON_TARGET_FABRICATION_FOLLOWUP_2026-10-27.md), commit 845a26c78fdb143ca9d5bd4f5971f584a32d71a9.
- Preserve liquid pitcher, deposited active boron layer, and DISH/ceramic-printed frame as distinct serial subsystems. Explicitly account for substrate alpha attenuation and match boron-11 areal atomic density in comparator studies. Not experimental proof.

## DeepSeek third review: G0-B three-target substrate comparison
- [G0-B / G0-F three-target blinded comparison and support orientation controls](reviews/DEEPSEEK_G0B_THREE_TARGET_SUBSTRATE_COMPARISON_PROTOCOL_2026-10-27.md), commit 9d68591c4eb3f32730a5e590f2f9670113c64a6b.
- Free-standing/minimally supported boron foil, matched-B11-areal-density thick-substrate deposition, and printed-holder/deposited-film architecture are independent catcher **fabrication** arms; liquid pitcher remains a separate serial subsystem. Define upstream/downstream and substrate-facing orientations explicitly. Status: prospective experimental design, not measured.

## Copilot v0.8 critique → G0-B preregistration design
- [G0-B Protocol v0.1 — source-reproduction ladder, detector qualification, transmitted proton + paired alpha spectra, blinded validation, wedge/material arms and source-to-collector benchmark](protocols/G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md), commit 959bba447ab1411524b957530061c521a938f051.
- Source attribution: Copilot Researcher review provided by the user on Oct 27, 2026; integration with DeepSeek target fabrication comparisons and prior Gemini WP-B research. This protocol is a prospective design, **not yet formally preregistered or experimentally run**. Numeric facility acceptance thresholds, beam specification, instrument response, sample-size/power, and independent blind-custodian signatures remain required before freeze.
- Distinguish energy-frame confidence from pending nuclear-level J^π source mapping. Four evidence grades are SOURCE-TRACED → SOURCE-REPRODUCED → CALIBRATED → VALIDATED. New spectral-evolution H4, proton-transmission H5, layer/substrate H6. A frozen model that fails blinded testing must remain a recorded failure; revising it requires a new blind dataset.

## Copilot review: G0-B Validation Lockfile v0.1
- [Lockfile lifecycle and limitations](protocols/g0_b_lock/README.md), commit 26f9611f9ac660c9f8a7e72407591c26bff614ea.
- [Machine-readable JSON template](protocols/g0_b_lock/G0_B_VALIDATION_LOCKFILE_TEMPLATE_v0_1.json), commit 113524e33de724ac5ec80823d356c4ef6d8daa7e.
- [Conservative completeness checker](protocols/g0_b_lock/check_g0_b_lock.py), commit 2c2aaca873649eef89872d21d7d1457eb6d97bbd.
- **Template is deliberately incomplete; NOT a frozen or formally preregistered experiment.** Blind raw-data hash is generated and committed independently **after acquisition, before unblinding**; do not retroactively alter frozen predictions or reuse revealed data as newly blind.

## Atlas Research Ancestry prototype — INV0-WIZ alias, not constitutional renumbering
- [Research lineage README and canonical INV-0 reconciliation](../lineage/README.md), commit 474ae74f0763dce0ece2dab094d15989f596a2b0.
- [Source-traced research ancestry JSON graph](../lineage/atlas_research_lineage_v0_1.json), commit 9cbf475f6e0c1c1984a90d38a64b2841a6b99715 — six archived nodes, zero experimental receipts.
- [Append-only structural lineage validator](../lineage/validate_lineage.py), commit aae007e3d004b45b0123538a0ad13c1a5f0998cf.
- [Static HTML ancestry browser prototype](../lineage/lineage_viewer.html), commit a8d7740d39f41a9ea5d63589079b48fdfbfb73a2 (source view on GitHub; download/serve as HTML for interaction).
- Research subtext approved: **Reality may defeat a wizard, but it cannot delete their commit history.** Canon note: Aluminum OS INV-0 is System Integrity; historical ORCS `inv0_cleared` dual-use usage conflicts with that label. Existing INV-17 Zero Erasure and INV-19 Audit Immutability overlap this policy. This is not a formal Canon amendment or experimental validation.

## Stars 2.0 v0.9 pre-simulation synthesis — 2026-10-27
- [v0.9 pre-simulation integrated white paper: Gemini Argon, Copilot, DeepSeek, ChatGPT/Tidal Lantern and October 26 OpenAI harmonic analysis/QCD/ETH research leads](whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md), commit 3847de8b9d5540916a882ef6a01a0d11fc7b240f.
- Explicit source-attribution table, reported Gemini v0.3 OFAT results, unreproduced-code warning, DeepSeek three-material-stack comparison, Copilot preregistration and detector/kinematics requirements, two acoustic value scoreboards, local and whole-plant collector ledger.
- Newly proposed synthesis: qualified collector-accepted energy per total facility cost; collector acceptance can change optimal target thickness; wave-PDE/ETH/QCD tracking as *methods leads* only. No new complete simulation run, validated EXFOR calibration, experimental acoustic gain, or net-electric claim.

## Primary EXFOR nuclear-data recovery and DeepSeek v0.9 safeguard audit — 2026-10-27
- [Original EXFOR C2973002 41-point Spraker 2012 p-B11 cross sections with statistical uncertainties and 3.6% correlated systematic field](wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv), commit dadb9473c993cff31461f2584ad2edcf1520aae0. Source IAEA-NDS/exfor_master/C2973 original BIB & DATA retrieved through public GitHub. This supersedes the prior EXFOR live-ingest blocker for **this one reaction cross-section channel only**.
- [DeepSeek five safeguards fully adjudicated and EXFOR ingestion/source uncertainty review](reviews/EXFOR_C2973_PRIMARY_DATA_RECOVERY_AND_DEEPSEEK_FINAL_SAFEGUARDS_2026-10-27.md), commit 0974244230500cbe1411b7f5e1c2fd372bb51289. Bayesian count prior/BF, shot-time state, EMP detector, held-out optimizer and repeat-shot target lifetime integrated **as design requirements only**, not yet implemented code or actual G0-B preregistration. Report remains fail-closed and preserves nulls.

## Researcher discovery/metadata and DeepSeek post-EXFOR final anchor audit
- [Public researcher discovery README, field synonyms, data semantics and portability interface](RESEARCHER_DISCOVERY_AND_REPRODUCIBILITY_README.md), commit d1d095c9c496948fe8c34ae93b154651a19391d9.
- [Machine-readable STARS research keywords, topic recommendations, source IDs, evidence grades](RESEARCH_METADATA_STARS_2_0_2026-10-27.json), commit 3073a63287ea08bdca689c5833109347759bf1dd. GitHub repository topics **were not changed** (no available topic-edit action); recommendations are documented only.
- [DeepSeek post-EXFOR scientific audit of alpha-count semantics, 57 um BN range benchmark, kinematics, diamond detector, Bayesian and degradation gates](reviews/DEEPSEEK_POST_EXFOR_REVIEW_AND_TEST_ANCHOR_CORRECTIONS_2026-10-27.md), commit 8e5de931709a5f119708f63c7a657f222915739d.
- Corrective warning: C2973002 source `SIG` values can be integrated alpha-yield observables as Spraker counts/luminosity, **not automatically per-event reaction cross sections**; preserve the original 41 rows and require explicit observable-kind transformation. No new WP-B v0.4 source execution or formal G0-B preregistration has occurred.

## Copilot final v0.4 preflight — zero physics equals zero magic
- [Copilot source-attributed final audit, physical-observable typing, strict LAB/CM kinetic ledger, 16-gate verification matrix and analytic nulls](reviews/COPILOT_FINAL_PREFLIGHT_ZERO_PHYSICS_ZERO_MAGIC_2026-10-27.md), commit df6d88ceaca9fdf09de55ad790beb9b8e69ddb3c.
- Reviewer mnemonic **“Zero physics produces zero magic”** is a test slogan, not a ratified Canon invariant. Zero cross section must imply no fusion reactions and no nuclear Q energy; non-fusion backgrounds and input electrical energy remain separately accounted.
- **Design-only**: audit/verification matrix published; WP-B v0.4 code and its full passing test log have not been produced or executed in this action. Do not freeze blind G0-B predictions yet.

## GPTWork implementation handoff (pending Gemini Argon final reviewer response)
- [Top-level GPTWork START HERE pointer](../../GPTWORK_START_HERE_STARS_2_0.md), commit d05366b09820c7926c7d239f5ea46e23d4963806.
- [Full implementation handoff, two deliverables, physics/data invariants, 16 verification gates, freeze dependencies and planned build structure](GPTWORK_IMPLEMENTATION_HANDOFF_PENDING_GEMINI_2026-10-27.md), commit 8b8a4ef1e98d1f72b4ac9a68a12d9185f1548fff.
- This is a discoverable implementation **candidate**, not the frozen contract; Gemini final review pending, GPTWork has NOT run, and G0-B predictions not authorized for freeze.

## Gemini Argon v0.4 text report received — code and CSV still outstanding
- [Critical review of Gemini's claimed 1,000-event conservation, S1 quality/2.60x utility, S2 5.5→6.0 um optimum, S3 supported targets, and Newman/Rudin-Shapiro crest reduction](reviews/GEMINI_ARGON_V04_REPORTED_RESULTS_HARMONIC_CREST_FACTOR_AND_REPRODUCIBILITY_AUDIT_2026-10-27.md), commit e531ecfd238a2e4a9a778d902d37217df106aa76.
- Full claimed v0.4 `.py` and five CSV artifacts **not received, hash unverified, no independent end-to-end execution**; OpenAI local smoothing theorem applicability still unproven. GPTWork implementation contract remains **not frozen** despite report receipt.

## Gemini v0.4 independent execution and A/B test checkpoint
- [Original source externally executed, 2/2 author tests passed, all five CSV artifacts regenerated, plus critical independent A/B test discrepancies and required changes](reviews/GEMINI_V04_INDEPENDENT_EXECUTION_AND_AB_REGRESSION_GATES_2026-10-27.md), commit 81d9bb4d8d4189c42c30b29c1adf3aade031b0cc.
- **Status update:** actual Python source is now present in this conversation and did execute under NumPy 2.3.5/SciPy 1.17.0; it is **not yet published to repository with all generated CSVs**. Previous 'code absent' blocker for local execution is resolved, but original hash does not match claimed Gemini digest.
- A/B FAIL or research holds: whole-grid accepted optimum 7 μm instead of reported 6 μm; Newman crest 5.12 vs claimed 3.62 (alternative non-Newman phases generate 3.62); lower peak has higher occupancy above chosen 2.2×RMS damage proxy; foreign substrate is modeled with BN stopping, not substrate-specific stopping; toy equal-mass generator and hard-coded alpha spectra remain disconnected; no EXFOR calibrated quantity types.
- A/B PASS: independent sigma=0 null yields no fusion born/escaping/collector energies; independent ideal planar slab analytic quadrature matches closed form (but has not yet been run against Gemini physical transport routine). Zero sigma also exposes NaN-CV edge error. **Full Copilot 16-gate suite remains unimplemented.**
