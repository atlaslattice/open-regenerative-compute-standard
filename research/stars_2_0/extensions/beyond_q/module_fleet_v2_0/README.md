# Beyond Q module/fleet v2.0

Isotope-first dual-reactor research model, connected reactor-only financials and staged 1–50-module fleets. Proposed A = 1.10 GW primary D-D; default B = 1.10 GW D-T, with explicit 1.13 GW input option. G1–G5 remain OPEN. No GPU/QPU hardware, financing, revenues or configurations are included.

The 37.5% conservative-potential, 75% planning and 90% optimistic **overall He3 recovery** cases are assumptions, not demonstrated equipment efficiencies. They are applied once to the output of an explicit two-compartment transient pipeline. This is not a mechanistic adsorption or purification simulation. The prior v1.9 target-controlled model remains unchanged. This release uses fixed source availability rather than an annual 350k target controller.

```sh
python -m pip install -r requirements.txt
python -m unittest test_model -v
python run.py
# Shorter run or different module count:
python run.py --years 30 --modules 1 10 50 --out outputs_30y
# Finer integration and edited versioned assumptions:
python run.py --inputs inputs.json --step-days 0.125 --out outputs_fine
```

Open `outputs/dashboard.html` locally. No server or external JavaScript is required. `annual_products_finance.csv` contains annual products, inventories, energy, financing, capped/full-He3-offtake and price-pressure sensitivities. `module_ledger_*.csv` contains each module's physical sources, losses, internal fuel recycle, exports, energy and replacement events. There is no intermodule fuel sharing in this release; enabling it raises an error rather than silently inventing transfers. Daily permissions are synthetic seeded availability, not calibrated outage-duration distributions.

`execution.json` records the exact inputs, versions, runtime and conservation checks. `input_code_hashes.json` records executed input and code hashes. `refinement.json` compares three-year timestep refinements. `REPORT.md` defines boundaries, evidence, results and blockers.

The generated bulk CSVs/dashboard are reproducible outputs. The draft PR carries source code and compact execution evidence; large regenerated files may be distributed separately. Net profit and actual qualified sales remain null when unsupported. Default capital excludes unpriced buildings/site and operating/replacement costs; known-charge headroom is NOT profit.
