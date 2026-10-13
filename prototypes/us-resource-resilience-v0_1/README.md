# US Resource & Resilience prototype v0.1

Published 2026-10-12 (America/Chicago). Public, versioned, forkable early-stage abundance-economics modeling. **CANDIDATE / NON-CANON; zero realized national-impact credit.**

Download `index.html` and open it in a modern browser. Supply-security calculations work locally without an account. Earth & Space observation buttons optionally request public upstream data; browser/network behavior has not been acceptance-tested. No deployment, government authority or operational monitoring is claimed.

## What is included

- An additive US adaptation of DragonSeek v1.6.1: English default; contiguous US, Alaska and Hawaii regions; original China comparison retained.
- Twenty-three national physical material-consumption/production records from ORCS v0.6. These are screening proxies, not a complete raw-material trade census.
- A proposed reserve target of 20% of annual domestic consumption, recovery sensitivity and physical-gap import backstop. Actual grades, deliverability, reserves and export authorization remain unverified. Blank reserve data stays UNKNOWN, rather than zero. Imports may cover production and reserve gaps.
- State and county selection with local JSON imports. National totals are never apportioned into invented regional records. Coast-to-coast transport, regional costs, jobs, wages and certified reserves remain UNKNOWN.
- Original synthetic storage/PV resilience model; manual earthquake, space-weather and optional fire observations. Broader weather/pathogen/aviation/orbital adapters are explicitly NOT_CONNECTED. No air traffic control, collision avoidance or public-health decision system.
- A local JavaScript port of the actual Atlas-Intelligence claim checker. It detects a few wording patterns and citation presence; a passing check does **not** establish truth. Houses appear as context tags, not a functioning semantic router. No Firebase, autonomous agents or external AI providers are connected.

## Arithmetic and interpretation

For compatible units and an assumed qualified additional recovery `W`, modeled annual supply is `P + W`. Reserve target is `0.2 * C`; reserve gap is `max(target - assumed usable stock, 0)`. For build horizon `H` years, imports needed are `max(C + reserve_gap/H - supply, 0)`.

An export candidate is computed only when assumed stock meets the target; it is a simulation, not lawful authorization. Actual authorization is always false. Stock decay, surge demand, grade conversion, seasonal flows, logistics and environmental permitting require subsequent evidence. Production and consumption proxies may have mismatched transformation boundaries. This prototype does not override those limitations.

Repeated payment transactions, GDP, employment and environmental outcomes remain distinct. The existing v0.7 throughput scenarios are linked, not promoted into forecasts. This is an inspectable demonstration of a proposed domestic supply-security approach; it does not establish that either country's national abundance economics has been empirically demonstrated.

## Reuse and source lineage

Fork this public repository; preserve source attribution, provenance and prior versions. New research and adaptations follow the repository's CC BY-SA 4.0 license. The Atlas-Intelligence component retains its complete upstream MIT license and attribution principle in `upstream/ATLAS_LICENSE.txt`. Do not remove those notices from extracted or bundled copies. Source commits and paths are pinned in `provenance.json`; original upstream projects remain unchanged.

DragonSeek source: atlaslattice/manus-artifacts, commit `34c8e681b0f0b12a8422ca0439db2fceb8fc355e`, `research/dragonseek_1_6_1/index.html`. Broad adapter catalog: commit `9188383d18704fa70fbb93dd7cd8b3556bd692fe`. Atlas-Intelligence: commit `c17a50f3bd3f4f01e0ee22273aaf4fe18f1bc349`, `src/lib/verifier.ts`.

`index.html` is the self-contained distribution and contains copies of the calculation module, claim checker and national data. When editing separate source modules or data, update their inlined copies too. `test-ledger.js` checks module behavior; it is not browser acceptance testing.

## Regional JSON format

Import an array of records. Required fields: `id`, `unit`, `geo_level` (`state` or `county`), two-digit `state_fips`, five-digit matching `county_fips` for counties, `annual_consumption` and `domestic_output_or_proxy` (nonnegative numbers or JSON `null`). Include source/year/grade metadata where available. Local imports are explicitly UNVERIFIED. Upload limits: 5 MB and 10,000 records. FIPS checks validate syntax and prefix, not existence in an authoritative geography registry.

## Validation receipt

`node test-ledger.js` verifies balance arithmetic, UNKNOWN propagation, no national fallback for regional gaps, matching FIPS, input constraints and the claim checker's citation/overclaim behavior. JavaScript syntax checks passed for all three embedded script blocks. Browser rendering, optional upstream feed fetches and official regional data acceptance: NOT_TESTED / UNKNOWN. These checks confer no empirical-impact credit.
