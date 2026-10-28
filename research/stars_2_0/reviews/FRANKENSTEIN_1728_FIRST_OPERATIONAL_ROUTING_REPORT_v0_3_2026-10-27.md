# Frankenstein 1728 — First Operational Routing Simulation v0.3

**Run status:** EXECUTED, five/five internal toy checks PASS. **Scientific status:** exploratory graph network, not full historical TCSS/Path B, membrane, actual packet network or nuclear validation. New append-only report. Prior first-ignition v0.2 receipts remain intact.

## Test setup

Three **1728-node** graph candidates share the same periodic nearest-neighbor 12×12×12 torus. Packet routes are minimum unweighted hop counts using SciPy sparse Dijkstra. Same **240 fixed seed-20261028 source/destination attempts** per model in three scenarios: no failure, **86 randomly removed nodes** (~5%), and **17 highest-degree nodes removed per individual graph** (~1%). Total nine model-scenario cells.

1. **Pure torus:** 5,184 undirected edges, six per node.
2. **SHUGS-enriched:** 11,448 edges, adding 6,264 source-HSUF-derived undirected intra-slice shortcuts.
3. **Element145-enriched:** 11,112 edges, adding 5,928 source-HSUF-derived shortcuts.

Shortcut rule: for each original 144-state HSUF matrix, create up to **four strongest nonzero off-diagonal absolute-coupling neighbor selections per node** and union the edges, repeated over 12 slices; no extra administrator node. **This is a novel graph rule, not the actual spectral operator or physical stiffness.** Formula source: `atlaslattice/element-145/shugs/shugs_core.py` and `atlaslattice/element-145/element145/shugs/operator.py`; reconstructed code with original lineage. The full TCSS Path B chiral/Hxp terms remain unrecovered.

| Model | Normal delivered | Mean hops | P95 hops | Random 5% delivered | Targeted 1% delivered |
|---|---:|---:|---:|---:|---:|
| Torus | 240/240 | 8.7833 | 14 | 219/240 | 236/240 |
| SHUGS hybrid | 240/240 | 5.4125 | 8 | 219/240 | 234/240 |
| Element145 hybrid | 240/240 | 5.6292 | 9 | 219/240 | 237/240 |

All nine network states remained in one connected component. All failures to deliver were caused by removal of a source or destination: for example, 21/240 requests in the 5% random-failure scenario had dead endpoints. **No packet with both endpoints alive became unroutable.** The targeted node sets differ by model (degree-based ranking); do not interpret delivery fractions as strictly paired under identical failures.

## Machine gates

- Packet accounting: delivered + dead-endpoint + unroutable-live-endpoint = attempted, **PASS**.
- Base torus degree exactly six, **PASS**.
- Same attempted packet pairs per model/scenario, **PASS**.
- No mandatory administrative node, **PASS** for this simulation topology only.
- No assertion that novel shortcut graph equals historical source operator, **PASS** in metadata.
- **5/5 aggregate toy checks PASS**; not five independent experimental validations.

## Interpretation and immediate next experiment

**The shortest-hop advantage is confounded by edge budget**: SHUGS and Element145 models use about 2.2x as many edges as torus. There is not yet credible evidence of unique spectral-routing improvement, network throughput, delay, fault tolerance improvement, or physical stability. The simulation has **no contention, queueing, capacity, bandwidth, time-varying traffic, energy accounting, actual control-plane votes, authentication, packet transmission, or sensor measurement**. The third lattice dimension is numerical, not mapped to physical depth.

The next necessary experimental control is **equal-edge-budget comparison** against randomly placed and conventional geometry-aware shortcut graphs, with multiple seeds and confidence intervals. After that add routing congestion, vertex/edge failures, heterogeneous packet loads, centralized-admin baseline and a decentralized quorum/failover policy. Keep all 1,728 peer states. Recover exact historical full TCSS matrices before attributing any effect to full Path B.

## Source and receipt availability

The executable source `frankenstein_1728_operational_v03.py` and machine receipt `FRANKENSTEIN_1728_OPERATIONAL_RECEIPT_v0_3.json` are generated in the originating conversation at `/mnt/data`; not asserted to be committed or CI-reproduced in GitHub. Existing STARS draft PRs remain unchanged.

**The doctor found the switch; the numerical creature routed packets; the scientist still wants an edge-matched control.** ☕⚡🧙‍♂️