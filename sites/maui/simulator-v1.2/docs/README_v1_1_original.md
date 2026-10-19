# MAUI ATLAS LATTICE / ORCS — v1.1 runnable research handoff

**2026-10-19 · PROPOSED / NON-CANON · no field deployment · no realized impact credit**

This package preserves the earlier Maui v0.8, v0.9 and checklist v1.0 documents, adds dated research and **a small, executable research prototype** with a local HTML dashboard, 30-year deterministic scenario comparisons, an illustrative 168-hour microgrid dispatch and five read-only public-feed adapters. It **does not** claim a live operational plant, calibrated weather-to-grid forecast, grid interconnection, land approval, proven 30-year net-positive outcome, or verified production economics.

## Run it

Requires **Python 3.10+**, using only the Python standard library. Extract the ZIP. In the extracted directory:

```bash
python server.py
```

Open **http://127.0.0.1:8765/** on the **same computer**. The dashboard loads built-in synthetic scenarios with no internet connection.

```bash
python model.py --scenario hybrid_compute --output trial.json
python model.py --scenario storm_outage --mode hourly --output storm.json
python model.py --scenario hybrid_compute --set solar_mw=35 --set desal_mgd=1 --output alternative.json
python -m unittest discover -s tests -v
```

To **attempt** live public feed connections, on a machine with internet access:

```bash
python live_feeds.py
```

The program writes `live/latest.json`, marking each feed LIVE_RETRIEVED, STALE_CACHE or UNAVAILABLE. Reload the browser to view status. A successful, fresh Open-Meteo 7-day forecast may supply hourly irradiance to the 168-hour dispatch; no forecast is projected directly through 30 years. If any provider is unreachable, the dashboard identifies the unavailable feed rather than inventing readings. API terms, traffic limits and commercial permissions must be reviewed before persistent deployment.

**Current environment limitation:** external HTTPS calls from this execution container failed DNS resolution. Therefore **no live data pulls were validated and no feeds are claimed live now**. Test the adapters in GPT Work's internet-enabled environment and capture response receipts before promoting status.

## Files

- `dashboard.html`: read-only local dashboard, metrics, scenario comparison, 30-year trend, 168-hour dispatch, data health, four regional site plans and protective gates.
- `server.py`: HTTP service bound to `127.0.0.1`; GET-only JSON endpoints `/api/catalog`, `/api/annual`, `/api/dispatch`, `/api/compare`, `/api/live`.
- `model.py`: deterministic mass, fuel, heat, electrical and financial calculations; configurable 30-year and 168-hour scenarios.
- `live_feeds.py`: opt-in weather, Hawaii alerts, Kahului tide level, regional earthquakes and space weather ingestion.
- `data/assumptions.json`: explicitly provisional inputs (units named), not approved engineering data.
- `data/scenarios.json`: 11 scenarios, including drought, cyclone/outage, fuel shortage, wildfire, low commodity prices and underperforming conversion.
- `data/feed_inventory.json`: 30 cross-domain source interfaces with implementation vs planned status.
- `data/sample_simulation.json`: sample results from a deterministic offline run, no field measurements.
- `tests/test_model.py`: reproducibility, conservation, no double counting, non-certification and outage gates.
- `INTEGRATION_HANDOFF_v1_1.md`: extended complete Maui technical, research and dashboard requirements.
- `EVIDENCE_REGISTER.md`: new 2026 sources, limitations and evidence classifications.
- `WORK_DISPATCH.md`: ready-to-paste parallel GPT Work assignment and independent acceptance gates.
- `prior/`: unchanged prior Maui project files.

## Prototype lineage (reconciliation required)

1. Existing China reference: https://github.com/atlaslattice/manus-artifacts/tree/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build — Dongjiakou pilot simulator, evidence appendix, validator concept, with no live plant-control authority. The simulator file is discoverable as `public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/simulator.py`.
2. Other China reference in prior handoff: `dashboard/dragonseek_1_0_standalone.html`, `engine/dragonseek_v1.py` (168-hour synthetic demo), and 26 weather/ocean/disaster adapter candidates in `evidence/weather_ocean_disaster_adapter_inventory.json`. **These precise paths were reported in a prior portable archive but were not independently retrieved in the current GitHub lookup; do not claim verified default-branch source availability.**
3. US reference: https://github.com/atlaslattice/open-regenerative-compute-standard with a 50-state resource and agricultural resilience framework at `research/us-agricultural-resilience/2026-10-17/50-state-orcs-agricultural-resilience-framework-v0.1.md`. The Maui implementation is a separate local alpha and is **not** a merge of the original codebases.
4. Reuse the governance/evidence contract: MEASURED, ESTIMATED, FORECAST, SIMULATED, PROPOSED, QUARANTINED and RECEIPTS, preserving boundaries, timestamps, units, source licenses, checksums and human approval.

## What a passing run proves—and does not prove

Passing tests proves the offline equations execute and basic contractual invariants hold. It does not prove yields, local feedstock volume, net positive 30-year economics, utility export eligibility, Native Hawaiian or community acceptance, favorable ecology, code compliance, sanitary safety, fuel certification, source feed uptime, or industrial suitability.

**Default hybrid_compute sample result:** Financial NPV is negative under deliberately provisional assumptions; this is a screening result, not a Maui investment valuation. No grant revenue, uncertified HTL fuel sale, uncontracted grid export, or unpriced social benefit is counted as cash.

**Safety:** Read-only. Never connect these routes to power, wastewater, ocean, fuel or emergency actuators. Public alerts are informational and must be verified with authorities before any safety-critical action.
