# ORCS v0.4 — Empirical-only U.S. Data and Asset Admissibility Gate
**2026-10-14 · ADDITIVE DRAFT · NO SYNTHETIC INFRASTRUCTURE OR HAZARDS · ZERO REALIZED CREDIT**

## Binding policy for further ORCS empirical work
User requires **real-world references and datasets only**. No invented refinery, terminal, pipeline, hazard, outage, freight corridor, capacity, or price observation may enter the empirical national logistics or hazard model. Prior v0.3 synthetically geolocated sample demonstrations are classified **TEST FIXTURES ONLY**; they must not appear as factual scenario evidence, operational exposure, or national policy projections. Keep prior artifacts append-only and preserve fictional *Iron Empire* independently.

### Known existing public evidence
- EIA 2025 annual distillate in the October 14 research: Gulf PADD3 exports **411.180 million bbl** vs East PADD1 imports **45.424 million bbl**. These are regional trade totals, **not a validated TX→NY lane, available domestic freight, individual refinery grade slate or deliverable spare capacity**.
- Four **actual Oct 13 source requests** were previously successful and their original bytes and hashes preserved under `prototypes/us-resource-resilience-v0_2/receipts/` and `public_feed_probe_receipts.json`: USGS all-hour quake GeoJSON, NOAA SWPC planetary K-index, NWS Austin point metadata, FEMA disaster declarations. **Historical snapshots only**; not evidence of currently functioning runtime sync.
- USGS public GeoJSON/API: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
- NOAA NWS official alerts endpoint: https://api.weather.gov/alerts/active?area=TX ; documentation https://www.weather.gov/documentation/services-web-alerts
- PHMSA National Pipeline Mapping System Public Map Viewer: https://www.npms.phmsa.dot.gov/AboutPublicViewer.aspx . **Viewer only** with access/scale limitations; public pipeline maps and downloadable vector routes are NOT interchangeable, and more detailed PIMMA data are restricted.
- BTS Freight Analysis Framework (FAF): https://www.bts.gov/faf . OD flows do not show available unused corridor capacity, grades, rates or contractual rights.
- EIA national energy dataset and energy atlas https://www.eia.gov/opendata/ ; refinery and import/export totals must retain period, unit and location method. The bulk-download route may be usable without a registered key, whereas EIA API access has key requirements.
- Additional candidate sources (untested by new runtime): NASA EONET wildfire and public orbital elements from CelesTrak. Orbital catalog is not a verified collision-avoidance event. Deep-Earth resonance lacks a verified standardized nationwide prediction feed; no unverified earthquake predictions.

### Data admissibility record contract
Every operationally relevant observation must have:
`source_agency`, `url`, `retrieved_at_utc`, `observation_time_utc`, `source_record_id`, `physical_quantity`, `unit`, `geography`, `quality_status`, `sha256_snapshot`, `rights_access_class`.
Reject/mark UNKNOWN missing key fields. Site and route geometry require published source and explicit rights; no reverse-engineering of restricted pipelines or sensitive infrastructure. Quake points, warning polygons, and utility outages are different event types and not interchangeable. Hazards only produce human-reviewed **potential exposure**, not closure.

### Priority implementation
1. **Import the four real archived snapshots** and validate each according to its source-specific schema; prefer exact original timestamps and source IDs, not fabricated examples.
2. Build an **actual asset registry** from public, attributable source locations at permitted granularity (EIA refinery facilities, BTS modal nodes, NOAA ports), with dataset releases and versions. Do not silently geocode ambiguous names or place a synthetic facility.
3. Join observed hazard footprints to source-based facility geography using quality/freshness gates; publish counts and provenance, not fictional closures.
4. Leave route edges null until an independently documented publicly disclosable route, commodity grade, transport capacity, tariff, and permission exists. Public NPMS is not a downloadable comprehensive pipeline routing layer.
5. Calibrate existing PADD3→PADD1 petroleum substitution first with **physical feasibility still UNKNOWN**; DPA expansion is a separate additive supply pathway.
6. Maintain scenario-specific proposed American domestic-service → grade-/region-specific reserve → affordability export gate; this never grants operational export authority and must handle legal constraints and possible unintended shortages.

**No government, utility, airline, defense organization or corporation has been shown to deploy ORCS.** All changes should undergo human review before merge. Fictional Iron Empire bug swarm is creative-only and must not contaminate empirical observations.
