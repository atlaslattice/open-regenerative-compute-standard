# Stellar Forge — October 30 evidence and model-impact review v0.1

2026-10-30, America/Chicago. New source-traced review; no prior code, configuration, numerical result, apparatus identity or evidence status is overwritten. No numerical parameter has been changed and no external code incorporated in this review.

## Finding

Today's Git aggregation contains material **model-development leads**, especially the centrifugal-shear proposal and target/plasma-state effects. It does not yet supply a recovered, runnable, independently reproduced replacement for the current handoff calculation. Prioritize a multi-species distribution/collision/drive ledger as a comparison lane for A and B. Preserve original STARS as C and the current PR44 interface benchmark as an independently versioned numerical control.

The most similar lead located in the published index is the **continuous-flow bi-ionic centrifugal-shear proposal**, linked to Technical Disclosure Commons record 11795. The underlying disclosure, associated source-code repository and software license were **not recovered or verified in this review**. Do not call this a completed open-source incorporation assessment, attribute a numerical flaw to unseen code, or assume this is definitely the codebase the project lead meant. Its public-disclosure link does not by itself establish a reusable implementation.

## What was inspected

Pinned ORCS default-branch snapshot: `22bd49ceecdd5fbaafc0a42a3fa842e954708a9b`. Reviewed today's default-branch commit list, updated open PR list, recursive tree, master evidence index, p-boron appendix, convergence audit, FLiBe/fusion supply note, two digital-twin notes, two-day brief, full-stack synthesis and Gemini-commentary reconciliation. The last three documents were checked for additional code/repository references. Manus-artifacts returned no default-branch commits after local midnight in the reviewed window. These are scoped searches, not a complete audit of every repository, historical commit or branch.

The aggregation date is not the date of every underlying finding: its H-mode article is identified as June 2026, the shear proposal as September, and the accepted muon paper as October. Source-type labels in the master index describe the kind of evidence, not automatic correctness, applicability or independent replication.

RETRIEVAL_RECORD.json preserves the six principal project documents and direct-retrieval outcomes. Project summaries were accessible. The web search service repeatedly returned an error with no content; direct primary-page requests returned HTTP 403 for the disclosure and APS accepted paper, and a challenge page rather than the PMC article. No access-control bypass was attempted. The previous council audit's source classifications are attributed below; **this pass has not independently reverified the unavailable primary papers**.

## Model-impact matrix

| Lead in today's aggregation | Evidence actually available to this review | Proposed model action | A/B/C routing |
|---|---|---|---|
| Centrifugal-shear non-equilibrium proposal | Project source audit identifies defensive publication at https://www.tdcommons.org/dpubs_series/11795/ ; full methods/code/license unavailable here | Recover original equations and code; independently reproduce before integrating. Compare species-resolved flow, collision relaxation, rotation/torque, electron heating, radiation and sustaining power | Named A transport/confinement comparator; may inform B. Preserve current PRISM definition of A and unchanged C |
| EXL-50U H-mode | Project audit attributes a measured confinement-regime observation to https://pmc.ncbi.nlm.nih.gov/articles/PMC13343428/ ; current retrieval did not return article text | Add a separate source/confinement-state benchmark once diagnostic and discharge inputs are recovered; do not copy a confinement-time ratio to a different geometry | ENN-informed A source/plasma module and B; no automatic H-mode factor or hardware import into C |
| Transient beam–target plasma: reported 1.48× / 1.75× yield | Today's appendix explicitly says these particular studies are not independently verified in its source audit | Recover exact papers, raw/binned data, source normalization and target conditions; compare changing stopping, target state and source delivery | Separate C target-state experiment or B variant where appropriate. Does not demonstrate mechanical-acoustic causality |
| Muon-catalyzed p–11B | Project audit identifies theoretical accepted PRC work, https://journals.aps.org/prc/accepted/10.1103/2p5j-2m53 ; methods unavailable in this pass | Optional separately named catalyst reaction lane, including production/injection/capture, losses, recycling and energy cost; recover numerical model before use | Exploratory variant, not silently inserted into ordinary p–B A/B/C kernels |
| Physics/surrogate digital twins | Project notes link CFS, Imperial/AMPERA and Saltworks announcements | Independent solver-comparison and fault-injection harness; retain out-of-domain flags, source logs and human review. Retrieve actual software before any reuse assessment | Shared research/verification infrastructure, not a physical fusion-yield gain |
| Quantum FLiBe chemistry / supply-chain news | Separate Beyond Q source note; fragment and full-system errors distinguished | Keep chemistry-to-fuel-cycle coupling separately qualified; procurement state and delivery dates may inform cost/schedule scenarios | Beyond Q extension and optional facility research; does not calibrate p–B reactions or remove PR44 source-domain limits |

## Consequential engineering priorities

1. **Retain full distributions.** A proton cutoff or energy interval is not a measured energy/angle/position/time distribution. Source capture, relative collision energy, target overlap and losses must share the same normalization.
2. **Make target state explicit.** Current PR44 supports cold elemental B11 only. A transient or hot plasma needs its own stopping/collision/charge-state and evolving-density adapter. Do not treat the cold model's refusal as evidence that an actual hot-target experiment fails.
3. **Track sustaining power.** For any shear/rotation/confinement model, audit drive work, drag, collision-driven relaxation, electron/ion exchange, radiation, escaping species and alpha energy partition. A favorable conditional reaction rate is not enough to establish net electrical output.
4. **Test mechanisms separately and jointly.** Reproduce the external model unchanged, then switch collision/drive assumptions under disclosed controls, repeat step/domain refinement, and examine adverse coupling. Do not multiply its reported enhancement by a mirror toy gain, acoustic reliability factor and collector efficiency without a coupled model.
5. **Keep acoustic endpoints physical.** Preparation may change target state, readiness, productive firing probability or source jitter. Those require source/target transfer data and all-attempt denominators. H-mode, transient plasma and muon theory are different mechanisms and do not themselves measure acoustic effects.

A/B/C labels refer to the three **p–B apparatus configurations** in PR43. They are not Beyond Q's reactor A/B labels or the older 525 MW scaling study. Today's master index explicitly protects the separate Beyond Q 1.13 GW D–T / hypothetical 20 MW primary D–D reference. No one system's normalization is transferred into another's ledger.

## External-code incorporation contract

For the centrifugal-shear lead, recover:

- Exact title/author/version and disclosure source; associated GitHub/GitLab/Zenodo release or original code archive.
- Software license and separate permissions/terms for data, figures and bundled dependencies.
- Exact source commit/hash, environment and dependency lock, launch command, configuration, seeds and output files.
- Distribution functions, geometry and boundary conditions; collision, source/drive, radiation and transport definitions; particle/energy accounting.
- A reproduction receipt at original inputs, followed by negative controls, numerical convergence checks and independent comparison with an appropriate conventional solver.

If recovered code is useful, preserve it as an external named baseline and build an adapter around its particle, phase-space, time and energy outputs. Use separate scenario IDs for our changes. A result that reproduces its own assumptions but fails a physical accounting test remains a preserved result, not an approved gain. Missing code or an unresolved license blocks code incorporation, not continued independent model development.

## Immediate decision

**Change implementation priority:** add a scoped multi-species plasma-state/collision and drive-power comparison lane before relying on scalar PRISM-like retention gains. Continue finite source acceptance and correlated-alpha coupling already planned after PR44. No new architecture is silently substituted, and no current numerical output changes on the strength of the news summaries alone.

The remaining source-recovery item is the actual repository/release for the similarly structured external work. Only the disclosure link was located in the inspected project materials. A precise repository URL would let the next step be a code-and-license audit rather than guessing which project was intended.
