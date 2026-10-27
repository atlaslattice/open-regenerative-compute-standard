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
