# ⚡ Atlas Lattice Cognitive v0.3 — Real-Source Evidence Retrieval Benchmark

**Executed:** October 27, 2026. **Status:** exploratory, non-canon, no independent LLM agents. **Result: ordinary lexical retrieval wins.** New append-only artifact; cognitive ignition v0.1/v0.2 unmodified.

## Why this is different
Earlier v0.2 created its own graph and sampled expert-pair answers from that same graph. Here the **evidence passages come from real fetched Atlas Lattice GitHub documents**. The questions and source-required answer keys are still **hand-authored from those passages**; the benchmark is an internally curated document-evidence retrieval test, **not independently held-out cognitive QA**.

The eight input document excerpts are sourced from:
- `atlaslattice/manus-artifacts/docs/LATTICE_HYPERCUBE_12x12x12.md` (HSN/12D/Canon)
- `atlaslattice/atlas-lattice-providers/docs/SWARM_RECEIPTS.md` (identity, attribution, dissent)
- `atlaslattice/manus-artifacts/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/lattice/NODE_TEMPLATE.md` (accounting nodes and evidence gates)
- `atlaslattice/element-145/element145/shugs/operator.py` (145-admin historical variant)
- `atlaslattice/open-regenerative-compute-standard/research/stars_2_0/experiments/ATLAS_LATTICE_COGNITIVE_IGNITION_v0_2_2026-10-27.md` (synthetic invitation test)
- `atlaslattice/manus-artifacts/archive/research/math/tcss/TCSS_121212_WORKING_BASELINE_v1_1_2026-05-21.md` (historical TCSS source)
- `atlaslattice/open-regenerative-compute-standard/research/stars_2_0/implementation/observable_slice_v0_1/README.md` (draft PR #9 source, not default-branch Canon)
- `atlaslattice/open-regenerative-compute-standard/research/stars_2_0/design/ATLAS_LATTICE_COGNITIVE_SPECTRAL_RECONSTRUCTION_CANDIDATE_v0_1_2026-10-27.md` (new, non-canon synthesis)

Each excerpt carries its exact fetched Git blob SHA (source version, not necessarily exact quote of full document), repo and path. Excerpts are hand-selected and condensed, not full-corpus ingestion. Source contains 8 curated documents, 10 question/evidence pairs, and 10 hand-curated undirected inter-document links (not recovered original KG links).

## Tests, budgets, and measured quantity

For each question, choose 2, 3, or 4 evidence documents using TF-IDF cosine similarity (word+bigram), unique-source diversity, random, first-neighbor graph exploration, shuffled node-label graph negative control, and post-hoc baseline-preserving exploratory variants. Same document budget in each comparison.

**Correctness metric:** whether the selected document IDs include *all* hand-identified required evidence sources (two per task). No model-generated final answers were scored, no human judges, no 1728 spawned reasoning models and no creative hypotheses verified.

| Policy | Complete evidence @2 /10 | @3 /10 | @4 /10 |
|---|---:|---:|---:|
| Lexical TF-IDF | **5** | **8** | **9** |
| Source-diverse lexical | 5 | 8 | 8 |
| Random | 0 | 2 | 1 |
| Curated graph-first | 4 | 5 | 6 |
| Shuffled-label graph | 4 | 4 | 5 |
| Post-hoc top-two lexical reserve + curated graph | 5 | 5 | 7 |
| Post-hoc top-two reserve + shuffled graph | 5 | 6 | 6 |

**Outcome: no evidence of KG retrieval advantage** on this particular hand-curated task set. In fact, the graph-first policy sacrifices some directly relevant documents to neighbors. The shuffled graph is sometimes competitive, signaling noise and small-sample limitations. Adding a lexical evidence reserve helps only partly. The latter modification is post-hoc and cannot be treated as independent evaluation.

Six implementation checks passed: 1728 conceptual slot count; unique source IDs; every answer key supported by fixture sources; exact per-policy document-selection budget; shuffled graph degree multiset preserved; no false claim of live LLM agents.

## Critical epistemic limitations

1. **Human-authored answer keys and links:** source selection and edge mapping are not independently blind. Some source excerpts are condensed, not the full documents, and the evaluation is subject to author bias.
2. **Very small N:** 8 excerpts and 10 tasks; accuracy rates are descriptive, not statistically robust.
3. **No 1,728 cognitive runs:** all slots are conceptual addresses. No actual independent agent invitations, debates, disagreements, synthesis, idea generation, executive adjudication or cross-domain verification.
4. **No implemented full spectral operator:** this evaluates TF-IDF and curated neighbors, not the TCSS Path B `H_xp,L_z,X_zL_z` or original SHUGS HSUF dynamics.
5. **No external QA score:** complete-evidence-source recall is a proxy for groundwork, not response factual correctness or useful novelty.
6. **Subsequent A/B requires** a larger external or blind source corpus, complete source extraction, protected benchmark construction and separate question/graph authors; matching inference budgets, actual independently instantiated agents (when available), real disagreement receipts, calibrated correctness, novel verified hypothesis yield, and candidate versus ratified claim statuses.

## Receipts

Local executed standalone Python script: `atlas_real_corpus_eval_v03.py` SHA-256 `a753a3d3fdad5d7747dc3eba50aac009235de329f9a60529b7e9744168b46a80`.
Machine receipt: `ATLAS_REAL_CORPUS_EVAL_RECEIPT_v0_3.json` SHA-256 `54ad4092c7c5034e978fbf773d71b9445b5f2f1567d7c5dc756b8ba2cbc7426e`.
Environment Python and sklearn/NumPy; source and detailed per-question selections in local artifacts provided in originating conversation. Not GitHub CI reproduced unless files subsequently committed and CI run.

**Conclusion:** The librarian has legitimate source fragments. The wizard invitations need better calibration. **The most accurate local method remains ordinary lexical retrieval.** Do not optimize the conclusion away.

*Wizards in the back. Receipts in the front. The ordinary librarian wins round one.* 🍄🧙‍♂️⚡
