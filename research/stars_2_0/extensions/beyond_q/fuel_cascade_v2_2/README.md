# Beyond Q v2.2 — separately financed, predecessor-fueled rollout

New research version implementing the November 1 white paper's fuel-supported expansion decision. Earlier versions are unchanged. **No reactor-performance, product-qualification, financial-profit or exponential-growth validation is claimed. G1–G5 OPEN.**

## Run

Requires Python 3.12 and NumPy 2.3.5 as recorded in the parent package.

```sh
python -m unittest test_cascade -v
python run.py
python summarize.py
# Shorter experiment:
python run.py --years 10 --modules 5 --cases strict_unresolved sequential_predecessors eligible_pool --out short
```

`run.py` defaults to 60 years / capacity 50 with five policy/control cases. `summarize.py` currently summarizes the default `outputs/` directory. Full outputs regenerate locally; compact execution evidence and summaries are committed.

## Policy boundaries

- A and B remain proposed 1,100 MW fusion each; B=1,130 MW remains an explicit input option. Primary source/reaction assumptions are inherited, not recalibrated.
- Mandatory He3 retention is **zero**. Product value, sale allocation and actual receipts remain different quantities. Prices, qualification and offtake remain assumptions.
- Each successor requires its OWN external financing permission. Donor cash does not pay recipient capital. No real financing offer is represented.
- Eligible donor mobile T must exceed its own one-FPY-plus-10kg floor. Reserving fuel physically removes it from usable donor stock. It cannot be spent or sold again.
- Reserved fuel decays during construction and transport. Shipping loss is debited once on delivery. Recipient receives once, then begins operating from its own storage.
- The custody CSV derives scheduled dispatch dates separately from observed reservation and receipt events; the executed kernel uses one combined reserved/in-transit compartment.
- `sequential_predecessors` is the baseline interpretation of the originator's example: all earlier campuses must qualify before the next project. `eligible_pool` is a distinct relaxed sensitivity that can authorize multiple projects before earlier project IDs mature. Do not conflate them.
- Strict evidence readiness blocks successors while full-cost and physical qualification are missing. Conditional mode explicitly assumes those permissions, while still testing numerical trailing energy, served fuel, reserve and financing gates.

## Outputs

- `module_ledger_*.csv`: per-campus sources, inventory, losses, local recycle, predecessor sent/received flows and energy.
- `events_*.jsonl`: wait reasons, finance/construction permissions, donor reservations, receipts and commissioning.
- `fuel_custody.csv`: independently reconciled shipment sources, remaining escrow, decay and routing loss.
- `project_financing.csv`: separate recipient commitments; donor capital contribution is zero; complete installed costs remain unknown.
- `rollout_comparison.csv`: commissioned counts and timings.
- `annual_finance.csv`: recovery, price and offtake cases; missing costs/actual profit remain null.
- `dashboard.html`: self-contained interactive policy/product/finance display; no GPU/QPU economics.
- `REPORT.md`: results, limitations and continuation instructions.

The fixed-calendar and simultaneously commissioned/preseeded controls do not establish fuel-supported expansion. The preseeded control has explicit initial tritium in every campus, unlike zero-external-T cascade bootstrap. One seeded synthetic outage realization is not a reliability distribution. Three-year construction, one-year qualification window, four concurrent projects and shipping assumptions are scenario inputs, not engineering forecasts.
