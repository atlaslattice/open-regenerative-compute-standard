# ⚡ Atlas Lattice Cognitive Ignition v0.2 — Council Invitation / Provenance Smoke Test

**Status:** EXECUTED SYNTHETIC BENCHMARK • NON-CANON • NO LIVE LLM COUNCIL • NO SCIENTIFIC ADVANTAGE CLAIM.  
**Date:** October 27, 2026. **Update policy:** new version, v0.1 untouched.  
**Parent proposed mathematical specification:** `research/stars_2_0/design/ATLAS_LATTICE_COGNITIVE_SPECTRAL_RECONSTRUCTION_CANDIDATE_v0_1_2026-10-27.md`.

## Purpose

Test whether 1,728 fixed H.S.N knowledge-operator **address slots** can support selective query councils, independent invitee records, cross-house serendipity retrieval and dissent preservation **without adding 12 house +144 sphere operators**. This is an algorithmic demonstration, **not 1,728 independently operating models**.

## Setup

- 12 Houses × 12 Spheres per House × 12 Nodes per Sphere = 1,728 total address slots.
- 1,200 independently generated toy tasks, fixed synthetic undirected knowledge graph with **three generated cross-house links per node** (plus incoming links), one obvious primary specialist and one obscure specialist selected from primary specialist's KG neighbors.
- All five policies recruit exactly **12** slots per task: random, highest relevance, diverse-house relevance, 9 highest relevance +3 graph leads, and an identical graph-lead policy operating on a **node-label-permuted graph** as negative control. All policies receive the same relevance scores, but only graph strategies inspect graph edges.
- Missing evidence partner is specifically sampled from the same knowledge graph that a retrieval policy can traverse: **the experiment is designed to give the correct KG mechanism a discoverable path**. The result does not independently establish superior accuracy/creativity on real problems.
- Scores are synthetic, not embedding or empirical relevance measurements. Selection is algorithmic; no language model calls. Graph permutation changes mapping but preserves its edge topology/degree distribution. The toy result measures retrieval of a stipulated pair, not quality of generated hypotheses.

## Independent executed v0.2 results

| Policy | Both experts recovered | Primary expert recall | Hidden cross-house recall | Avg houses invited |
|---|---:|---:|---:|---:|
| Random | 0 / 1200 = 0.00% | 0.92% | 0.83% | 7.83 |
| Relevance only | 25 / 1200 = 2.08% | 100% | 2.08% | 3.49 |
| House-diverse | 65 / 1200 = 5.42% | 99.92% | 5.42% | 12.00 |
| Graph-guided exploration | **603 / 1200 = 50.25%** | 100% | 50.25% | 4.68 |
| Node-label-shuffled graph | 20 / 1200 = 1.67% | 100% | 1.67% | 4.44 |

**Interpretation:** meaningful graph-encoded cross-house links are much more effective in *this synthetic task generator* than a label-shuffled graph, under the same 12-slot budget. This is a mechanism smoke test, not fair third-party benchmark of actual cognitive discovery. Link correctness is effectively the answer source by construction. The historical TCSS/Path B and SHUGS physical/numerical spectral operators are **not used or validated here**.

## Five checks passed

1. Exactly 1,728 addressable slots.
2. All strategies use 12 invitations ×1,200 tasks =14,400 selections.
3. No extra House/Sphere thinkers added.
4. All complete-pair recoveries bounded by either expert recall.
5. Minority specialist receipt is always counted when invited.

## Execution details and limits

Python + NumPy v2.3.5, fixed seed `20261027`. Generated standalone scripts and machine receipts in originating conversation:

- `atlas_lattice_cognitive_ignition_v01.py`, `ATLAS_COGNITIVE_IGNITION_RECEIPT_v0_1.json`, earlier unshuffled comparator, preserved.
- `atlas_lattice_cognitive_ignition_v02.py`, `ATLAS_COGNITIVE_IGNITION_RECEIPT_v0_2.json`, **current negative-control run**.
- Source and machine receipts are conversation downloadable artifacts **not asserted to be committed to GitHub or run on GitHub CI**. This Markdown report is the new GitHub artifact.

**Limitations:** Not actual 1,728 model instances; not evidence of independent hypotheses or creative output; no corpus ingestion, embeddings, actual source citations, calibrated accuracy, judge adjudication, executive deliberation, latency/energy ledger, hierarchical adaptation, topology holdouts or test-set separation. Scoring and task graph intentionally share a relationship. One fixed graph and seed; replication under graph noise and independent seeds is outstanding.

## Next gates

- Real grounded corpus queries with external answer keys; blind multiple models, flat councils, HSN councils and graph exploration under matched inference budgets.
- Typed KG edge provenance, false-positive/false-negative links; stale/missing/hostile edges, negative controls, time-based holdouts, and minority correctness.
- An executable Atlas Prime librarian interface retrieving immutable Canon/source receipts, plus E145 executive as optional, audited action proposal; no automatic Canon promotion.
- Full TCSS/SHUGS source-faithful operator testing separately. If a spectral affinity policy is proposed, compare to standard knowledge graphs/embeddings and ablate the actual operator.

**Wizard motto:** The spores were invited because a real map showed the path. The map still owes us independent evidence that its paths matter.
