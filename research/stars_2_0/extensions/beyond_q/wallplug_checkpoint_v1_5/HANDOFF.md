# Tomorrow's continuation — wall-plug atomic-factory model

Current package: wallplug_checkpoint_v1_5, stacked on startup_year_v1_4_1 / PR52.
Previous source: v1.4 REPORT.md, SOURCES.md, inputs and eight_hour_summary.csv.
Power correction: ../DUAL_LASER_POWER_BASIS_LOCK_2026-10-30.md.

## Completed

1. Actual prior WarpX collision/drag benchmarks remain separate from assumed
   reactor/laser operation. No new physical-validation claim.
2. Wall-plug adapter now consumes the actual saved eight-hour scenario outputs.
3. DD primary Q and internally consumed-T secondary DT Q are separate. B actual
   burn and scheduled laser budget have different boundaries.
4. Six assumed gain/efficiency cases,162 energy rows and18 price sensitivities.
5. Nine tests covering missing inputs, normalization, electricity identity,
   unfueled scheduled drive, energy allocation and consumed-versus-sold T.
6. Market prices, qualified He3 recovery, campus demand and profit remain null.

## Next bounded work

- Retrieve/source-qualify the actual laser configuration, pulse energy and
  repetition rate, on-target energy and supported target-gain range. Declare
  primary-DD versus total-A gain basis; do not silently swap definitions.
- Connect time-aligned laser diagnostics when available; a no-laser PIC fusion
  test cannot supply laser gain. Record physical volume/window normalization.
- Split A/B electrical auxiliaries, thermal/charged-particle recovery and
  processing loads. Add heat rejection, maintenance, replacement and CAPEX/OPEX.
- Extend the same energy adapter to the staged one-year trajectories. Current
  source-connected electricity results cover8h; one-year economics is not done.
- Add separate He3 birth/capture/purity/storage ledger, actual external demand
  constraints and price provenance. Preserve T internal-use/sales separation.
- Allocate shared costs and electricity opportunity cost once. Distinguish
  imported power bill, internally supplied power cost and displaced export value.
- Produce uncertainty/sensitivity boundaries, then consolidate a methods/results
  white paper. Keep calibration requirements and possible negative outcomes visible.

User direction: Stellar Forge is an atomic-factory research framework, accepting
energy-consuming isotope manufacture as a potential useful outcome. Success
requires measured/supported recoverable output and total costs, not necessarily
net-electric DD operation. The campus electricity requirement remains a separate
constraint. Do not assume electricity expense is trivial before computing it.

Do not confuse this D-D/D-T thread with the parallel p–11B ceramic-pocket work.
Do not restart completed suites without a new code change or unresolved issue.
Keep all current work as draft, preserve earlier artifacts, and continue routine
implementation within the user's existing authorization.
