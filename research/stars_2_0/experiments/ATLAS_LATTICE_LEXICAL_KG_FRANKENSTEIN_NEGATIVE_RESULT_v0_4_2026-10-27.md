# ⚡ Atlas Lattice v0.4 — Lexical + Graph Frankenstein; honest negative result

**Status:** EXECUTED EXPLORATORY BENCHMARK • NON-CANON • NO LIVE INDEPENDENT LLM COUNCIL • NO VERIFIED COGNITIVE BENEFIT. Date: 2026-10-27. This is a **new version**; all earlier source/operator artifacts remain untouched.

## Research question
Can ordinary lexical evidence retrieval and speculative cross-domain knowledge-graph routing be combined under **the same source-document selection budget**, retaining source correctness while exposing surprising connections?

## Reproduction
Exact source Python and per-question JSON receipt are bundled with the originating ChatGPT conversation as:
- `/mnt/data/atlas_cognitive_v04/atlas_hybrid_lexical_graph_v04.py`
- `/mnt/data/atlas_cognitive_v04/ATLAS_HYBRID_LEXICAL_GRAPH_RECEIPT_v0_4.json`

The v0.4 program imports unchanged v0.3 fixture `atlas_real_corpus_eval_v03.py`, itself based on real GitHub-extracted but **hand-selected and shortened** source passages. Re-run command from environment with NumPy and scikit-learn:

```bash
python atlas_hybrid_lexical_graph_v04.py
```

**Important**: The stand-alone script expects the v0.3 directory beside v0.4; script/JSON are conversation files, not claimed to be committed here or run in GitHub CI. Reports are not executable substitutes.

Corpus: **eight** real Atlas Lattice documents, ten hand-written questions, two hand-identified required evidence sources per task, ten manually curated graph edges. The graph is not an original recovered TCSS/SHUGS spectral operator. All five policies share identical TF-IDF similarities and document budgets.

Policies: lexical-only top-K; graph-first; reserve top 1, 2, or 3 lexical documents then spend remaining selection slots on graph neighbor documents. Graphs: curated; node-label shuffled negative control; 50% dropped; 100%-additional-spurious-edge; combined noisy. One hundred independently seeded graph perturbations per noise condition; **NOT 100 independent tasks**.

## Executed results on original curated graph

| Method | Exact evidence source recall @2 (of 10) | @3 | @4 |
|---|---:|---:|---:|
| Lexical only | **5** | **8** | **9** |
| Graph first | 4 | 5 | 6 |
| Lexical reserve 1 then graph | 4 | 5 | 6 |
| Lexical reserve 2 then graph | 4 | 7 | 7 |
| Lexical reserve 3 then graph | 4 | 7 | 8 |

Six of six implementation checks passed: exactly 1728 address slots, fixture size, identical per-policy selection budget, lexical graph-invariant, top-K−1 lexical preservation for guarded variant, and explicit zero live LLM agents.

For 100 independently perturbed **graphs** with 50% link deletion and 50% new random-link insertion, average **@4** complete-evidence counts:
- Lexical: **9.00/10**
- Graph-first: **6.27/10**
- Lexical reserve 1: **6.27/10**
- Lexical reserve 2: **7.48/10**
- Lexical reserve 3: **8.51/10**

The graph perturbations do not constitute independent answer sets, and a higher average over noise graphs is not a confidence interval on task generalization.

## Interpretation

**Negative result:** no graph-invitation policy outperformed plain lexical document ranking under an identical tight retrieval budget. Protecting direct evidence reduced but did not remove the loss. The graph is a shallow manually linked citation-document network and does not represent true domain-level cross-concept relations. Given the small N and fixture authoring bias, this establishes only an engineering failure mode, **not that lexical is intrinsically superior to all graph retrieval or all spectral methods**.

## Frankenstein redesign, not yet validated

Model **evidence retrieval** and **discovery exploration** as **separate, accounted budgets**. First gather `K_e` ranked source passages; separately allocate `K_x` exploratory invitations using KG/spectral/ontology/random/diversity candidates, without displacing the evidence-backed baseline. Every candidate innovation includes a provenance receipt, independent support/contradiction ledger and independent verifier. Claim improvement only if external graded answer correctness or verified useful cross-domain solutions improve under **matched combined budgets** `K_e + K_x` and model-token/tool-call limits.

Crucial control: compare against lexical using the **same combined budget**, not an unfair lexical K=K_e vs hybrid K=K_e+K_x comparison. Also compare a random-exploration control and shuffled graph, and require blinded held-out questions, independently authored graphs, and live separately-instantiated language model candidates for cognitive claims.

## Scientific boundaries

- No new Canon promotions; human root required.
- 1728 are addresses only; no 1728 independent reasoning jobs were run.
- Current experiment measures document retrieval, not response correctness, creative hypotheses, debate or external verification.
- No recovered complete TCSS H_B or E145/SHUGS source-faithful cognitive routing was tested. Spectral-gap/GUE scores are not evidence of inference quality.
- Distinguish a knowledge-operator HSN address from an industrial/physical site accounting node.

**Conclusion:** the ordinary librarian wins again. Do not silence the speculative wizards; give them an evidence-preserving, independently costed exploration lane and demand receipts before promoting their proposals.

*Wizards in the back. Receipts in the front. The spores can explore, but may not evict the books.*
