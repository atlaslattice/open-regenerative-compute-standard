# Stellar Forge — A/B/C architecture clarification v0.1

2026-10-30. Project-lead correction and confirmation: **“Yeah ENN is third finding.”** New definitions govern future comparison runs. Historical files, PR39, PR42, IDs, results and qualifications remain unchanged.

| Primary configuration | Intended apparatus | STARS inheritance |
|---|---|---|
| **A — New Hybrid** (`SF_A_NEW_HYBRID_V0_1`) | Published hollow-sphere research + PRISM research + ENN EXL-50U suprathermal-proton p–¹¹B result | None automatically |
| **B — Combined Hybrid** (`SF_B_COMBINED_HYBRID_V0_1`) | A integrated with the original STARS acousto-optical, staged-interaction and alpha-management research inventory | Retain C's nonsuperseded modules and explicit alternative branches |
| **C — Original STARS** (`SF_C_ORIGINAL_STARS_V0_1`) | Original STARS reference family, without the newly introduced A components | Preserve the recovered 26-entry inventory |

**Full stacked industrial integration is the B research track.** A and C still need their own complete facility energy and cost accounting for fair comparison. Shared diagnostic, nuclear-data and accounting software does not install STARS physical hardware in A. Original STARS already contains optional particle-field, recirculation and plasma-wave research; their retention in C does not import the new PRISM or ENN configurations.

The recovered inventory contains hardware, software, optional modules and alternative configurations. Retention does not mean installing every alternative at once. B's 29 research entries are a union of three new research ingredients and the 26 C inventory entries; they are not 29 independently additive gains or 29 necessarily separate hardware instances. Physical instance IDs, alternative selection, shared services and redundant equipment must be reconciled during actual configuration assembly. Preserve adverse coupling and interface costs.

## Source binding resolved

The original shared news message grouped three leads: the ENN EXL-50U result, hollow-sphere target geometry and Borealis PRISM. The October 29 architecture addendum also listed H-mode, pellet fueling, electron-temperature and alpha-channeling leads separately, so the third ingredient was initially left unresolved. **The project lead's present confirmation selects the ENN EXL-50U suprathermal-proton result.** It is no longer an unresolved source-selection blocker.

SOURCE_BINDINGS.json records the original news context, prior source-audit paths and the confirmation. The binding does not replace technical evidence: ENN's reported NBI/RF fast-proton population is a source/coupling benchmark lead, not an automatic gain factor or instruction to treat a spherical torus, a pulsed hollow target and a mirror as the same field region. The exact spatial, spectral and temporal interfaces belong to A's physical model. The audit's alpha-rate versus reaction-rate normalization question remains open. Neither the separate H-mode result nor a direct-conversion efficiency is silently substituted for the selected result.

## Historical IDs and numerical outputs

| Historical ID | New relationship | Treatment of old runs |
|---|---|---|
| `STARS_REFERENCE_V1` | C reference-family alias | Preserve original tags and configuration hashes |
| `HYBRID_PB_RESEARCH_V0_1` | Forward full-stack family mapping to B | Do not relabel its historical results; never use it as A's identity |
| `STARS_DESIGN_CANDIDATE_V0_1` | Separate prospective revision | Not automatically A, B or unchanged C |

The earlier registry's broad full-stack scope corresponds to the newly clarified B family. That mapping does not establish that any historical toy executed B. The reduced sphere/mirror toy, three-module mirror toy and 525 MW scaling remain submodels under their original scenario names. The nine-script replay, 11 matching CSVs and 77 audit checks remain valid within the scope stated in PR42. No numerical result is upgraded by the new labels.

## Runnable implementation

ABC_REGISTRY.json encodes the configurations, legacy mappings, retained inventory, confirmed third source and common metrics. ORIGINAL_STARS_MODULE_COVERAGE.json is a separate recovered copy of the inventory at PR39 commit `b8687d7945fa5ef62362f1c7f15f85e1fa036bf9`; the historical file is not edited. Its relative evidence links refer to that original source directory.

```bash
python plan_campaign.py --out /tmp/stellar-forge-abc-plan-001
python -m unittest discover -s . -p 'test_*.py'
```

Run from this directory. The planner checks the mapping and writes a new campaign-plan directory; it does not calculate apparatus performance. The confirmed plan removes the third-finding blocker. Exact executable configurations and integration handoffs remain unpinned. Unknown performance is null, never an unearned zero or ideal efficiency. Historical replays remain runnable in the adjacent hybrid_reconstruction_v0_1 package.

## Comparison and next implementation order

1. Pin exact A and C physical configurations, sources, stages, parameter provenance and operating tracks. Keep C's reference configuration unchanged; changes require a new candidate version.
2. Build A's hollow-source → fast-proton preparation/coupling → mirror/interaction handoffs with explicit alternatives and shared fields. Use the ENN result as a scoped benchmark lead; do not fabricate its full distribution from an energy interval.
3. Compose B with C's selected physical branches. Resolve duplicate sources, fields, collectors and services by physical instance and energy destination. Run adverse-coupling sensitivities as well as favorable cases.
4. Report A vs C, B vs A and B vs C under common wall-energy, source-inventory and time-budget definitions. Keep events, alpha birth/escape energy, useful recovered electricity, shot success, jitter, duty cycle and capex/opex distinct.
5. Run matched module ablations and crossed controls. A/B/C comparisons alone do not identify causal synergy: B−A−C lacks an appropriate common baseline and can double-subtract shared functions. Use a defined common control and factorial interaction contrasts where physically meaningful.

Acoustics belongs to C and B unless a future explicitly named A variant adds it. Its first intended effect remains readiness, firing reliability and jitter, with all attempts and preparation time charged to the ledger. No acoustic nuclear-yield multiplier is introduced here. Configuration identities are resolved; calibrated apparatus performance and net-power operation remain separate research questions.
