# ⚡ Frankenstein 1728 — Capacity-Limited Packet Routing v0.5

**Status:** independently executed exploratory numerical traffic simulation; 6/6 implementation checks pass. **No physical spectral/membrane/fusion validation.** Append-only successor to v0.4, leaving all prior work unchanged. Approved exploratory 1,728-node research lane.

## Executive result
The source-HSUF-derived shortcut graphs again **lose** to equal-edge-budget random and geometric shortcuts on mean latency under this specified toy load. This is useful negative evidence against claiming their routing superiority from their current *graph reinterpretation*. It says nothing conclusive about the still-unimplemented full original TCSS/Path B spectral operator.

The experiment includes finite per-edge packet capacity, real FIFO queueing **in simulated discrete time**, packet arrival times, and route recomputation on the static post-failure graph. It remains neither packet routing on real computers nor a full dynamic failover protocol.

## Reproducible setup

- 12×12×12 periodic topology, **1,728 nodes**. Baseline: 5,184 undirected torus edges.
- Seven graphs: bare torus; SHUGS-derived at **11,448** edges; SHUGS-budget random and geometric controls at the same **11,448** edges; E145-derived at **11,112** edges and two same-budget controls.
- All extra edges are confined to the corresponding 144-node slice. SHUGS/E145 kernels translated into top-four *absolute-value* shortcut edges, not source spectral operators.
- Three independent graph-control topology seeds `3001,3002,3003` × three paired traffic seeds `4001,4002,4003` × two scenarios (normal and 86 removed random vertices): **126 scenario-model executions**.
- 180 source–destination packet requests per execution, injected in first 12 ticks. Shared undirected edge service capacity **one packet per time slot**, FIFO; all packets routed by hop-minimizing graph Dijkstra computed for each scenario before service; 120-tick horizon.
- No mandated centralized controller, but **no implemented decentralized governance or recovery protocol** either. Failure topology is known before packet release: instantaneous idealized recomputation, not an outage-duration test.

## Normal condition results (mean of 9 matched runs per model)

| Model | Edges | Mean simulated completion latency (slots) | Mean cumulative waiting-edge slots |
|---|---:|---:|---:|
| Pure torus | 5,184 | 9.06 | 20.33 |
| SHUGS derived | 11,448 | 5.54 | 8.00 |
| SHUGS-budget random control | 11,448 | **4.86** | **5.33** |
| SHUGS-budget geometric control | 11,448 | 5.13 | 5.78 |
| Element145 derived | 11,112 | 5.71 | 9.67 |
| Element145-budget random control | 11,112 | **4.91** | **6.78** |
| Element145-budget geometric control | 11,112 | 5.15 | 8.11 |

All 180 packet attempts completed in all 63 normal network-runs. With 86 random dead nodes, average completed attempts were **163.67/180**, with lost attempts entirely due to removed endpoint nodes, not network disconnection. These packet counts do not establish a throughput limit or resilience advantage: offered load is relatively light, and nearly all end-to-end latency reflects hop count rather than queuing.

## Software gates

6/6 PASS: all attempted packets accounted (delivered, endpoint dead, unreachable, or timed out); exact matching edges within each comparison family; no surviving but unreachable requests under tested failure; all graphs connected; completed not greater than possible; all packets completed in no-failure runs.

These are aggregate **software invariants** in toy assumptions, not scientific calibrations.

## Independent cautions and next scientific gates

1. Random/geometric controls resampled over 3 topology seeds; source graphs fixed, so uncertainty needs a family-aware paired analysis. No confidence intervals or statistical victory claims.
2. Edge cost fairness remains untested. Equal number of intra-slice links is not equal geographic distance, hardware budget, electrical use, weight, link capacity or administrative cost.
3. Discrete model has shared undirected FIFO edge capacity, no actual bandwidth, byte sizes, propagation distance, energy cost, synchronized distributed routing, routing protocol convergence time, authentication or queue priorities.
4. The model permits instant recomputation before packet injection on post-failure topology. Must explicitly test *mid-flight* failures with detection/recovery latency before claiming operational failover.
5. **Peak queued packets include packets awaiting ordinary hop service** and are not standalone congestion severity. Cumulative waiting-edge slots is the more explicit measure of capacity contention here. Under this workload, small wait totals show the test has not substantially saturated the network.
6. Next experiment should increase offered load until bottlenecks appear, vary burstiness, model static/centralized/decentralized routing decisions with failure timing, and compare topology cost and queueing under multiple load points.
7. Independently recover exact TCSS `H_xp`, `L_z`, `X_zL_z` definition and compare original operator dynamics; **do not substitute graph shortcut routing as full TCSS.** Separate physical modal `M,C,K` validation and sample-level metrology remain necessary.
8. GUE-KS matching is not evidence for better routing throughput. The source family names are provenance labels, not claims of physical applicability.

## Execution and provenance

Standalone source generated and run in originating conversation:
- `frankenstein_1728_capacity_v05.py`, SHA256 `fdee0ad6c713698a8a4f615c78f041ae8e91e51dec1b271a5e60fa7781baca9a`.
- `FRANKENSTEIN_1728_CAPACITY_RECEIPT_v0_5.json`, SHA256 `9920f638a12c99c3828abf56c0ecb522c5b22adac688162bbc310d48e3321b8f`.
- Python, NumPy 2.3.5 and SciPy 1.17.0; exact environment and 126 model-scenario records stored in JSON.
- Local executable and receipt provided as conversation attachments **not yet committed to GitHub**. No GitHub CI certification asserted.

**Decision:** Progress to capacity-saturation sweeps and mid-flight failure/recovery, not a speculative mathematical victory. Keep source histories intact and project-lead scientific freeze blocked.

**Wizard ledger:** The creature queued packets and kept receipts. The random-control gremlin won this round. ☕⚡🧙‍♂️