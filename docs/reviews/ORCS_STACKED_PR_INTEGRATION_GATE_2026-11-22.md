# ORCS stacked PR integration gate — 2026-11-22

Status: **REVIEW CANDIDATE / NOT MERGED / NOT PHYSICALLY VALIDATED**. This document does not alter scientific models, authorization, CANON, or deployed systems.

## Observed live PR chain
| PR | Head SHA | Base | Draft | Scope |
|---|---|---|---|---|
| [#64](https://github.com/atlaslattice/open-regenerative-compute-standard/pull/64) | `a080438ab6ff3321f13d8f8b29fcb00ec32c7f70` | `gptwork/collector-evidence-v0-1` | yes | source-to-facility conditional pipeline |
| [#67](https://github.com/atlaslattice/open-regenerative-compute-standard/pull/67) | `604158962fada3c5605339ce67539432ec94b2a7` | `gptwork/facility-integration-v0-1` | yes | hollow-sphere CAD/mesh |
| [#68](https://github.com/atlaslattice/open-regenerative-compute-standard/pull/68) | `ae75e78aa0e2d8e615c0cb96afc26d958a1cbbae` | `gptwork/hollow-sphere-solvers-v0-1` | yes | wall-plug/containment accounting |

These are **stacked**, not three independent changes against main. #64 itself depends on #61. Do not merge out of order or infer a clean main-branch integration from branch-local mergeability.

## Required evidence before any merge
1. Capture fresh branch SHA, base SHA, diff and CI status; detect drift since this snapshot.
2. Resolve the ancestor chain through #61 and confirm whether any upstream branch is already merged, superseded or conflicted.
3. Execute tests from a clean checkout at each exact SHA with pinned dependencies. Preserve commands, environment, stdout, exit codes, artifact digests and negative tests. PR-body self-reports are not fresh independent verification.
4. Verify physical claims remain scoped: #64 reports approximately 5.983e-6 J modeled nuclear release per 1 J proton input, **not** net electric gain. #67's mesh checks do not validate downstream FEM/plasma physics. #68's assumed 10% x 10% chain implies approximately 100 J electric input per 1 J beam and a large deficit under its stated recovery scenario.
5. Run a preservation diff against main for existing A/B reactor identities, all 26 C inventory entries, acoustic controls and historical reports. No silent replacement of old data.
6. Rebase/merge bottom-up in an isolated integration branch, rerun tests at the combined SHA, then obtain explicit human approval before changing main or removing drafts.
7. Separate modelled, simulated, calibrated, measured, independently reproduced, and deployed evidence. Keep all absent quantities UNKNOWN, especially actual apparatus net power.

## Adjacent backlog
- [#7](https://github.com/atlaslattice/open-regenerative-compute-standard/pull/7): 50-state logistics draft; unknown edges must not become zero physical capacity, and reserve targets are scenarios rather than established federal policy.
- [Issue #2](https://github.com/atlaslattice/open-regenerative-compute-standard/issues/2): reusable cross-site ORCS simulator, not closed by a draft logistics skeleton.
- [Issue #4](https://github.com/atlaslattice/open-regenerative-compute-standard/issues/4): normalize Dongjiakou/Corpus Christi desal evidence; permit, construction, output, zero-liquid-discharge and marine outcomes are separate.
- [Issue #69](https://github.com/atlaslattice/open-regenerative-compute-standard/issues/69): Somalia nutrition sovereignty open review; do not infer endorsement or verified field deployment.

## Decision
**HOLD merges and issue closures** until the above gates are evidenced. This is a source-linked integration work order, not a completed test run.
