# Beyond Q — November 1, 2026 white-paper checkpoint

- [WHITE_PAPER.md](WHITE_PAPER.md): comprehensive v2.1 synthesis; 30 source entries; equations, evidence, executed results, economics, corrections and research gates.
- [DECISIONS.json](DECISIONS.json): originator-approved architecture and latest reserve/financing/rollout policy.
- [HANDOFF.md](HANDOFF.md): resume instructions and exact stop point for a new thread.
- [NUMERICAL_SNAPSHOT.json](NUMERICAL_SNAPSHOT.json): six zero-He3-retention year/recovery financial recalculations with source hashes.
- [build_snapshot.py](build_snapshot.py): regenerates that snapshot from unchanged parent CSV output; no physical simulation.
- [AUDIT_HISTORY.jsonl](AUDIT_HISTORY.jsonl): append-only checkpoint decisions.
- [CHECKPOINT_MANIFEST.json](CHECKPOINT_MANIFEST.json): file checksums for this document package.

**Do not lose the controlling fleet rule:** each new campus is separately externally financed. Campus1 can fuel2; campuses1+2 can fuel3; eligible operating predecessors pool uncommitted T above their reserves to fuel later startups. The next campus does not have to be purchased with predecessor cash. Transfers reduce donor stock and cannot also be counted as tritium sales.

This rule could accelerate fuel readiness; no exponential growth curve has yet been executed or validated. The saved v2.0 50-module simulation is fixed-calendar, not this cascade. The next version should implement the controller with explicit fuel, donor-sustainability, financing and site/construction gates.

Updated default policy is zero mandatory He3 retention for standalone/GPU-hosted modules. The older saved input remains 50% and is preserved. Tritium operating/startup reserves remain required. GPU/QPU economics remain outside the reactor module. All physical G1–G5 are OPEN.

Publication route: draft PR #65, stacked on #63. No earlier release is overwritten and no merge is implied.
