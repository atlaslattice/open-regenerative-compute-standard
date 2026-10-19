# Maui ORCS v1.2 — verified runnable research prototype

Built 2026-10-19. Original v1.1 package preserved separately. This version adds execution evidence, dispatch corrections and dated public-feed receipts.

## Start

Python 3.10 or newer; standard library only. Extract this ZIP and open a terminal in this folder.

```sh
python server.py
```

Open http://127.0.0.1:8765 on that computer. Select a scenario or change sliders to recalculate. The server is local and read-only. No credentials are required for offline use.

```sh
python -m unittest discover -s tests -v
python verify.py
python model.py --scenario storm_outage --output storm.json
python live_feeds.py
python model.py --scenario hybrid_compute --weather-file live/latest.json --output weather_run.json
```

`verify.py` regenerates all 11 offline scenarios and local HTTP checks. Feed refresh is a separate explicit command, with no scheduled background service. The attached feed snapshot will age; the dashboard recomputes freshness on read and refreshes its status display every minute. Rerun a scenario after a successful feed refresh to use that forecast.

## What works

- 30 annual model years, 2026–2055; eleven scenario choices.
- 168-hour advisory electrical dispatch with PV, biogas and battery losses.
- Fresh forecast irradiance, where accepted by timestamp/schema/unit checks. Any remaining hours are explicitly synthetic.
- Separate critical and flexible shortfalls; no grid import/export when islanded.
- Five public-feed adapters retrieved data in this session; raw responses and SHA-256 receipts are in `live/raw/`. These are dated snapshots, not continuous monitoring.
- Local dashboard controls, JSON exports, scenario comparison, public-feed status and independently unverified ecological/community gates.

## Evidence and limits

Read `VERIFICATION_v1_2.md` first. `results/` contains all scenario JSON files, comparison CSV, HTTP response checks and input/code hashes. `data/sample_simulation.json` is regenerated with v1.2.

Only forecast irradiance drives the dispatch engine. Alerts, tides, earthquakes and space weather are context feeds. No hurricane/wildfire damage or tsunami impact is inferred automatically from those feeds. Scenario hazard factors are hypothetical.

NPV is an incomplete screening calculation: annual power netting is optimistic and desal-specific capital costs, financing, insurance, tax and terminal value remain unresolved. Current economics cannot establish commercial viability. Feedstock, process yields, siting, climate ensembles, ecological performance and resident outcomes require calibration.

The HTML dashboard needs the local Python server. It is not a public hosted website or a native phone app. Browser rendering was not verified in this environment; HTTP endpoints and JavaScript syntax were checked.

## Preserved context

`INTEGRATION_HANDOFF_v1_1.md`, `WORK_DISPATCH.md`, `EVIDENCE_REGISTER.md`, `prior/` and `docs/README_v1_1_original.md` are inherited planning/research context. Their statements about failed network access describe the previous environment. This release's dated receipts supersede those access-status notes only; external research claims have not been independently re-audited here.

Next engineering priorities: calibrated 8760-hour power cost accounting; explicit technology capital and O&M breakdown; source-backed GIS alternatives and rights-of-way; actual feedstock/WWTP/utility measurements; weather-history ensembles; validated water and pollutant mass balances; independent cultural/ecological review.
