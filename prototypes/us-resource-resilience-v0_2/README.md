# US Resource & Resilience prototype v0.2

2026-10-12 America/Chicago. **Public, forkable early-stage modeling; NON-CANON / ZERO REALIZED CREDIT.** Preserves v0.1 and all upstream China originals.

Download `index.html` and open it in a modern browser. It bundles the national ledger, historical series, simulator, access registry and existing manual Earth & Space adapters. No account is required for local simulation. No operational monitoring or export authority is conferred. Browser rendering and optional live-feed acceptance remain NOT_TESTED.

## Simulator

Select one of 23 national material records. Set an explicit 1–100-year horizon, demand/production growth, additional qualified recovery output capacity and ramp, assumed initial usable stock, annual stock loss, reserve build horizon, one-year production/recovery shock and optional annual import cap. Run a baseline-without-additional-recovery comparison and download annual CSV. Material units are displayed; rows with missing physical baselines remain UNKNOWN. Regional values remain UNKNOWN unless supplied through local unverified JSON.

Default future growth and additional recovery are zero. Initial stock defaults to an explicitly hypothetical zero, not an inventory finding. The proposed reserve target remains 20% of each year's consumption. Demand is served first; remaining supply replenishes reserves. If imports are capped, reserves may be drawn to cover demand and unmet demand is reported. Surplus after reserve allocation is separately accounted. An export candidate requires demand served and modeled end-stock at target; actual export authorization always remains false.

Historical growth is opt-in: five material histories (copper, aluminum, potash, phosphate rock and refined zinc), each with 2021–2025 observations, mapped to compatible ledger units. These are reviewed transcriptions of archived original USGS MCS2026 tables; current federal byte equivalence remains unverified. Reported commercial inventories are retained as observations and never automatically treated as strategic reserves. A four-year CAGR is descriptive and extrapolating it is a sensitivity, not a forecast. The simulator does not automatically convert hazard observations into losses.

Physical and reserve stock equations are tested. Additional recovery is a hypothetical output-capacity assumption, not demonstrated eligible waste mass. Grade compatibility, upstream inputs, technical yields, environmental permits, coast-to-coast logistics, capacity/capital limits, commodity prices and jobs/GDP feedback remain unresolved. No calibrated century-scale prediction or automatic compounding wealth claim is made. EIA cases through 2050 are identified for future ingestion, not currently wired.

## Data access and credentialed forks

[DATA_SOURCES.md](DATA_SOURCES.md) and `source_registry.json` list 75 source entries: 29 US-focused sources and 46 inherited DragonSeek candidates. This is the identified modeling-source inventory, not every possible provider. Access class, evidence, integration gap, local connection and server probe result are separate.

Four anonymous server JSON samples succeeded (USGS, NOAA SWPC, NWS point metadata, OpenFEMA). These snapshots and hashes are in `receipts/` and `public_feed_probe_receipts.json`; successful server access does not establish browser CORS or a simulator connection. Direct USGS PDF returned 403. A Census HS query returned a Missing Key HTML page and was rejected as data. EIA API requires a registered key, while documented bulk downloads do not. Approved-user Space-Track data has transfer restrictions requiring explicit review.

Credentials belong in an authorized private backend. Never commit keys, session tokens, personal records or restricted operational records into this public fork. Publish only permitted snapshots with provenance. Unknown requirements are labeled for review; failed public access does not imply government-only access. See the registry for remaining sources and account gaps.

## Reproduce and validate

From this folder:

```
python3 build_history.py
node test-ledger.js
node test-simulator.js
python3 probe_public_feeds.py
```

History generation verifies source-table numeric tokens and ledger endpoints; row mapping was manually reviewed. Probe execution refreshes raw snapshots and its receipt, not simulator inputs or the bundled HTML. Review changed vintages and update registry evidence deliberately. `index.html` is the self-contained distribution with inlined copies: when modules/data change, update bundled copies too.

Tests cover arithmetic, UNKNOWN handling, no fabricated regional fallback, invalid FIPS prefixes, wording/citation patterns, 30-year flow/stock conservation, recovery import comparison, shock behavior and shortages with capped imports. All five embedded JavaScript blocks passed syntax checks and HTML IDs were unique. Browser visual QA remains pending.

## Reuse and attribution

New research and adaptations follow ORCS CC BY-SA 4.0. Retain complete Atlas-Intelligence MIT license and attribution principle in `upstream/ATLAS_LICENSE.txt`; its notice is also bundled in the HTML. The inherited wording checker checks a few patterns and citation presence, not truth. `provenance.json` pins DragonSeek and Atlas-Intelligence source commits. Firebase, external AI dispatch and operational aviation/pathogen/orbit systems remain unconnected.

This public demonstration is intended to help independent teams evaluate and improve domestic supply resilience, circular recovery and abundance economics. Earlier modeling is preserved; modeled impacts are never credited as realized national accomplishments.
