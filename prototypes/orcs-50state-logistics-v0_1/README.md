# ORCS 50-state logistics/resilience skeleton v0.1 (2026-10-14)

**PUBLIC / PROPOSED / NON-CANON / ZERO REALIZED CREDIT.** Independently additive to the October 14 resurrection packet, three white papers, GPTBrain archives and existing 23-material prototype. No prior versions modified.

Runnable standard-library-only 50-state node registry and conservative single-shipment route finder; **not a calibrated real-time national logistics simulator**. All 50 state codes are enumerated. There are **zero validated network edges**, so the default output is `UNVERIFIED_OR_INFEASIBLE`, not fabricated transport or savings. No operational permission is granted.

Run `python3 simulator.py` and `python3 -m unittest discover -v` in this directory. Tests use synthetic edges only. For illustrative routing, copy network.json and add explicitly hypothetical records with from/to state, grade, capacity_bbl, cost_usd_per_bbl, time_days, permitted and safe. The solver selects the lowest unit-cost *single shipment* through edges with enough capacity, grade match, time compliance and human-provided safety/permission flags; edges can be disabled for shocks. It does not perform system-wide multi-commodity flow allocation.

The separate `reserve_gate()` function tests a one-period domestic-demand-first, reserve-first, candidate-surplus accounting rule. The 90-day total-use target is PROPOSED and is **not** the IEA 90-day net-import requirement. Candidate surplus never equals authorized exports.

**UNKNOWN:** State-grade supply/demand/stocks; owner-confirmed available pipeline/rail/truck/marine capacities and tariffs; grade equivalence; operator permissions; emission and risk characteristics; accessible reserve inventories; verified labor and value-added impacts. Absent information is not zero and cannot imply physical route infeasibility. Future work is multimodal, multi-commodity flow with ledger reconciliation, source snapshots and credible route/grade/shock engineering validation.

Lineage: [Resurrection 2026-10-14](../../docs/handoffs/SOLGPT_TIDAL_LANTERN_RESURRECTION_2026-10-14.md); [national white paper v1.2](../../docs/whitepapers/ORCS_US_NATIONAL_ABUNDANCE_WP_v1_2_2026-10-14.md); [pilot v1.1](../../docs/ORCS_NATIONAL_FUEL_ROUTING_RESERVES_AND_CHINA_BENCHMARK_v1_1_2026-10-14.md). Iron Empire / The Last Conquest are **fictional inspiration**, not engineering evidence.
