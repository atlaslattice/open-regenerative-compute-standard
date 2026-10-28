# Atlas Lattice Cognitive v0.5 — Dual-Lane Evidence + Exploratory Wizard Council

**Date:** 2026-10-27  
**Status:** EXECUTED SMALL RETRIEVAL EXPERIMENT • NON-CANON • NO LIVE INDEPENDENT THINKERS • NO VERIFIED CREATIVE DISCOVERIES.  
**Preservation:** append-only v0.5; historical v0.1–v0.4 untouched. Human-root Canon approval remains required.

## Research aim

Recover Atlas Prime's librarian/evidence retrieval as a protected channel, while inviting optional cross-domain exploration without silently replacing cited evidence. Compare to **equal aggregate document budgets**, not unfairly to a smaller lexical baseline. The full HSN address set remains **12 Houses ×12 Spheres ×12 Nodes = 1,728 slots total**, **not** 1,728+12+144 operators. Slots do not imply 1,728 actively instantiated agents.

## Executed reproducible fixture

- Imported the *unchanged v0.3 test fixture*: eight excerpted, attributed **real GitHub repository documents** and ten **hand-authored** questions that each require two stipulated source IDs.
- The v0.3 script has import-time printing and rewrites its JSON receipt when imported; v0.5 script was run independently in the model's container.
- Used shared TF-IDF scores, manually selected source-document graph (10 edges; **not** a recovered historical spectral graph), 3 base evidence sources, up to 2 exploratory invitations, lexical 5-source matched-budget comparator. Two independent graph controls: 100 seeded trials each of label shuffling and link dropout/additions.
- The metric `citation_complete` means both required evidence IDs appear among *protected evidence sources*; `candidate_coverage` means they appear in **evidence plus exploration**, not that any novel finding has been scientifically verified.

## Actual results (10 questions)

| Policy | Complete evidence | Required pair present in all retrieved/invited sources | Total documents seen across 10 questions |
|---|---:|---:|---:|
| Lexical top 3 | 8/10 | 8/10 | 30 |
| Lexical top 3 + random exploratory 2 | 8/10 | 8/10 | 50 |
| Lexical top 3 + graph exploration up to 2 | 8/10 | 9/10 | 49 |
| Lexical top 5, matched total budget | **9/10** | **9/10** | 50 |
| Graph exploration displacing 2 of lexical top 3 | 1/10 | 1/10 | 29 |

- **Eight of eight implementation checks passed.**
- 100 graph-noise trials (50% edge-drop probability plus 5 random edge-add attempts): dual-lane graph policy mean complete evidence **8/10** and candidate pair coverage **8.75/10**; average total sources **44.46**. These are repeats of graph perturbations, NOT independent test questions.
- 100 graph label-shuffle trials: same **8/10** evidence, mean candidate pair coverage **8.79/10**; average total sources **45.84**.
- **Negative scientific result**: a graph-assisted exploratory lane did not beat equally funded lexical top-5 retrieval. Shuffled graph matches its candidate coverage under this tiny hand-curated fixture, so the original edge metadata have not demonstrated special information value.

## Interpretations and practical next design

**Engineering success**: keeping a separate evidence channel can preserve the direct citations while exposing additional ideas under a separate budget. This is a software invariant, **not** proof that exploring finds better hypotheses.

**Performance finding**: plain lexical retrieval remains competitive/superior at the same total document budget; neither original topology nor graph-shuffled control shows verified cross-domain cognition.

The candidate architecture therefore tracks two distinct outputs for each query:
1. Atlas Prime **evidence packet**: source IDs, hashes, excerpts, direct/contradictory citation links, unresolved unknowns, audit log.
2. Wizard **hypothesis packet**: independent operator address `H##.S##.N##`, reason for invitation, novelty claim, candidate analogies, critical objections, evidence links, separate verification status. Never overwrite evidence or promote a hypothesis to Canon automatically.

For evaluation, compare full cost of (evidence + exploration + actual reasoning and verification) against the same-resource ordinary retrieval and flat council. Retrieval of a second required document is **not itself creative scientific discovery**.

## Files, hashes, and access

The following executable files were generated and executed as conversation artifacts, but are **not asserted to be committed to GitHub**:
- `/mnt/data/atlas_cognitive_v05/atlas_dual_lane_v05.py` — SHA-256 `7c048d4c55e873bf702b21a91c4da0419be980cbd1376fefa59e1e241a954e74`
- `/mnt/data/atlas_cognitive_v05/ATLAS_DUAL_LANE_RECEIPT_v0_5.json` — SHA-256 `5760d0147355df0aad5627ae09a5701bbd7e4999c7c2ee6c3a163cf37a2897e3`
- Requires unmodified original `/mnt/data/atlas_cognitive_v03/atlas_real_corpus_eval_v03.py` beside the v0.5 directory. Dependencies Python 3, NumPy, scikit-learn.

## Unmet gates

No 1,728 model-agent processes spawned; there is no autonomous agent-debate runtime available in this session. These trials use deterministic algorithmic selectors, real cited **source excerpts**, hand-curated questions, and selected links. No hidden questions, external objective answer graders, nontrivial verified innovative solutions, actual dissent deliberation, independent judges or source-faithful TCSS/SHUGS reruns.

Next candidate work: completely separate **source corpus extraction from task authorship**, hold out sources/time, scale beyond eight documents, add cross-disciplinary problems with outside answer keys, implement candidate hypothesis packets and an external gradeable test harness, then compare at matched token and tool budget when independent agent execution is available. Keep the original TCSS and HSUF as separate mathematical experimental branches until their functional mapping is independently validated.

**Wizard verdict:** Protect the librarian. Invite the spores. Do not equate a candidate connection with a verified discovery. Wizards in the back, receipts in the front.
