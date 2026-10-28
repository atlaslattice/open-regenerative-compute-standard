# ⚡ Frankenstein 1728 — Edge-Matched A/B Routing Experiment v0.4

**Status:** Executed, exploratory toy simulation; 6/6 aggregate software/numerical checks passed. **Scientific status:** negative result for shortcut superiority in this test, not a physical/network/TCSS validation. **Lineage:** append-only successor to first operational routing report v0.3, without modifying historical operators or prior receipts.

## Method and fairness controls
- 1,728 nodes arranged as 12×12×12 periodic torus; base undirected edges = 5,184.
- SHUGS-derived shortcut candidate: **11,448 total undirected edges**. E145-derived: **11,112 edges**.
- For *each* source family, construct a random within-12×12-slice shortcut network and a geometry-aware graph-distance-2–4 shortcut network with the **exact same total edge count** as the corresponding source-derived model. The control edge sets are generated once with fixed seeds for each budget, then held constant across traffic/failure draws.
- Eight paired traffic/failure seeds (20261029–20261036), 240 source-destination requests each, 86 uniformly randomly removed vertices in failure scenario (~5%).
- Route by unweighted SciPy Dijkstra shortest paths, deterministic predecessor tie-breaking. Compute hop count and a **peak edge-use count** (how many of 240 paths traverse busiest edge). This is NOT packet capacity/queueing/congestion/delay.
- All source-derived shortcuts are **new graph-embedding rules using absolute SHUGS/HSUF magnitudes and strongest neighbors**, not the original spectral Hamiltonians; full TCSS Hxp/Lz/Xz Path B **NOT RUN**.

## Key results: normal traffic, 8-seed mean

| Model | Total edges | Mean hops | P95 hops | Mean maximum edge-use count |
|---|---:|---:|---:|---:|
| Base torus | 5,184 | 8.9245 | 14.000 | 6.375 |
| SHUGS-derived | 11,448 | 5.4156 | 8.381 | 4.750 |
| Same-edge random SHUGS control | 11,448 | **4.7927** | **7.131** | **4.375** |
| Same-edge geometric SHUGS control | 11,448 | **5.0313** | **8.000** | **4.500** |
| E145-derived | 11,112 | 5.5922 | 9.000 | 5.250 |
| Same-edge random E145 control | 11,112 | **4.7990** | **7.125** | **4.250** |
| Same-edge geometric E145 control | 11,112 | **5.0651** | **8.000** | **4.625** |

The **negative result**: despite shorter hops than plain torus, source-derived top-four-absolute-weight shortcuts do NOT beat either equal-edge-budget conventional control in this setup. This establishes no intrinsic deficit of original SHUGS/TCSS spectral operators, since their original dynamics were **not** evaluated.

## Failure and bookkeeping
- All seven graphs remained connected under each of the eight 5%-random-vertex removal draws.
- All sampled traffic with surviving source/destination was routable (zero unreachable live-endpoint pairs); failure deliveries averaged 214.375 out of 240 attempts, the remainder being dead endpoint attempts. All models share the same removed set and attempted pair draws in each seed.
- Six checks: equal edge counts within each family, packet accounting, connectivity, common traffic/failure seed control, no mandatory admin node, explicit graph-versus-operator distinction: PASS.
- No 1%-targeted-attack scenario in v0.4: that remains for a versioned next experiment.

## Essential limitations
1. **Topology ensemble:** eight paired seeds resample *traffic and node removal only*; each random/geometric shortcut topology is one fixed seeded draw. Next rerun independent multiple topology seeds and confidence intervals, not merely traffic resampling.
2. **Edge fairness:** same undirected edge count and same 12×12-slice restriction, but **not** same edge lengths, embedding costs, degree distribution, wiring distance or construction overhead; graph-distance-2–4 geometric control explicitly favors shorter links. A physical-network cost ledger remains necessary.
3. No bandwidth, capacity, queueing, stochastic service, dynamic failover, authentication, packets on actual machines, independent control-plane simulation, energy measurement, or physical foil dynamics. Peak path edge-use count is a descriptive proxy **not actual measured congestion**.
4. Shortest-path tie-breaking can alter maximum edge load. Replication should vary tie-break policy and include congestion-aware routing.
5. The source-derived constructions depend on local SHUGS/HSUF index ordering and top-four threshold. Real operator spectra, chiral TCSS terms and mode shapes have not been implemented in this routing test.
6. The work does not claim a reduction of national or distributed computing latency, a physical membrane benefit, or fusion gain.

## Executable / audit provenance
The corrected **standalone** local implementation is `/mnt/data/frankenstein_1728_edge_matched_v04.py`, SHA-256:
`18d06cc8f603b1b93fe93fe448236a32f21bbeafd2cd4f8281e044de888ddf9a`.

Machine-readable result in originating conversation: `/mnt/data/FRANKENSTEIN_1728_EDGE_MATCHED_RECEIPT_v0_4.json`, SHA-256:
`53ff00264bac3b42a6c7b04df3ed5d5fd19d2c3736b8a28eaaa197438881a1fe`.

Environment: NumPy 2.3.5, SciPy 1.17.0; results reproduced by corrected standalone rerun. **Local executable and full receipt have not yet been committed to GitHub**, so this report is **not** a GitHub CI reproduction. An earlier local draft imported v0.3, causing the old module's receipt-output side effect; corrected standalone v0.4 uses an inlined source-derived graph constructor without importing the old runner. Existing historical files preserved.

## Next version specification
1. Multiple independently seeded graph topology draws at equal edge and link-cost budgets.
2. Discrete-time packets with bounded per-edge link capacity, deterministic queueing, per-packet timestamps, end-to-end latency, drop rate, bytes moved and power/cost assumption ledger.
3. Same random and targeted vertex/edge failure sets, with explicit optional observer versus unilateral controller scenarios and fallback.
4. Separate source-faithful TCSS Hxp/Lz/Xz mathematical reconstruction, spectral transfer and measured membrane tests: **do not count this shortcut-routing toy as testing full TCSS**.
5. Preserve any outcome where random shortcuts win; never force a hybrid advantage.

**Verdict:** Igorian alchemy delivered the most valuable sort of receipt: one that tells us where the wizardry did *not* win. ☕⚡🧙‍♂️