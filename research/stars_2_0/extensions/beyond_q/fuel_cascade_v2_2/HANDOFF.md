# Beyond Q v2.2 continuation

Implemented after white paper v2.1 (commit15df944). Prior releases preserved. New code is in fuel_cascade_v2_2, on a new branch/draft PR stacked on #65.

## Critical policy preserved

- A=1.10GW PRIMARY DD, B=1.10GW DT default; explicit1.13GW B option. Historical A+20MWe NET is unvalidated, never20MW fusion. Executed A draw100MWe is ASSUMED.
- Isotope-first module; no GPU/QPU configuration, finance or compute revenue.
- Mandatory He3 retention=0. Overall assumed recovery37.5/75/90%; prices$1500/L He3,$1500/gT with pressure cases.
- Each new campus has independent external financing permission. Donors do NOT pay successor hardware capital. Donors supply only mobile T above their own reserve, reserved/debited once; shipments cannot also earn external sales.

## What was executed

60years, capacity50, seed119, dt0.25day; five comparisons. Strict evidence mode keeps the first research bootstrap module only while full costs and physical qualification are unknown. Conditional sequential predecessor baseline reaches15 operating campuses and has16building atyear60. Conditional relaxed eligible-pool case reaches50 aroundyear42.28. Fixed-calendar and simultaneous seeded controls also supplied. Explicit zero-source and financing-denied controls do not expand.

Three-year construction, one-year trailing operating screen, four concurrent projects and7day transport are ASSUMED. The strict sequential baseline requires every previous campus to qualify before authorizing the next: campus3 draws from1+2 as requested. The relaxed pool can authorize more than one project from currently mature donors before all previous project IDs mature; early campus3 there can draw only fromcampus1. This is an explicit alternative, not silent compliance with the stricter example.

No exponential growth law is validated. Greater fuel-producing capacity works as feedback, while construction, concurrency and maturation set the pace in these cases. Do not report these dates as project forecasts.

## Accounting and tests

Fuel escrow is outside reactor stock, decays during construction/transit, incurs loss once on receipt and then is credited once to the recipient. Per-module T balances include sent/received terms; a separate pool identity closes reservations, receipts, remaining inventory, decay and transport loss. No donor floor violations. Maximum pool residual<6.6e-11kg, per-campus residual<4.6e-9kg. Ten new tests pass; dashboard filter/null harness passes. Parent kernel regression passes when controller disabled. Five-year dt0.25/.125 check keeps first successor date unchanged, with~0.084% finalT difference.

The opportunity value recorded for reserved T is not extra booked revenue or an automatically double-counted expense. Actual transfer contract, ownership and payment are unknown. Finance-denied prevents reservations. No project cancellation/return has yet been modeled.

## Financial limits — essential

Recipient financing gates are conditional permissions, NOT bank offers. Complete installed housing/site, OPEX, replacement, construction interest and decommissioning costs remain unknown; actualprofit remainsnull. Financial price/offtake rows are postprocessed sensitivities, NOT feedback to donor financial eligibility. Conditional donor sustainability is an explicit assumed permission; strict mode blocks unknown evidence. Do not call capped-sales losses financially sustainable.

The simultaneous control injects71.654kg initialT into EACH of50modules. It is not a zero-external-T cascade. Outages remain independent/common, so simultaneously commissioned does not mean identical stochastic operation.

## Reproduce and next work

python -m unittest test_cascade -v; python run.py; python summarize.py; node test_dashboard.js. plot.py optionally uses matplotlib. Full CSVs/events/dashboard regenerate; compact execution and financial/custody/project evidence are committed. Prior source remains in module_fleet_v2_0 and is required for one regression test.

Next: vary construction duration/concurrency/qualification windows WITHOUT conflating the sequential and relaxed rules; repeat seeds; add cancellation/fuel-return and finite storage/transport constraints. Connect actual fully specified project finance to eligibility when evidence supports it. Highest physical priorities remain full DD operating point, transport-qualified breeding/deposited heat, mechanistic recovery/buyer specs and installed/lifetime costs. No new WarpX/OpenMC execution. All physical G1–G5 OPEN.
