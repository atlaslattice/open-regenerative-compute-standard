# Maui Regenerative Resilience Simulator — Water, Energy, Waste & Recovery

**Maui, Hawaiʻi · Lahaina · Kahului–Wailuku · Waikapū · Kīhei · North Shore**

A runnable, public research prototype for exploring how Maui could connect **water reuse, organics recovery, solar, batteries, resilient community services and ecological restoration** over 30 years. It brings regional siting proposals, public environmental feeds and scenario calculations into one inspectable package.

**Version 1.2 · October 19, 2026 · research alpha · proposed infrastructure**

[![Tests](https://img.shields.io/badge/local_tests-19_passed-238636)](simulator-v1.2/results/tests.txt)
[![Scenarios](https://img.shields.io/badge/scenarios-11-0969da)](simulator-v1.2/data/scenarios.json)
[![License](https://img.shields.io/badge/license-CC_BY--SA_4.0-blue)](../../LICENSE)

## Start on your phone

You can read the research, results and contribution needs directly on GitHub; no computer, account or installation is needed for public reading.

- **[Download the complete runnable simulator ZIP](https://github.com/atlaslattice/open-regenerative-compute-standard/raw/refs/heads/main/sites/maui/Maui_ORCS_v1_2_Verified_Runnable.zip)** — keep it for when you have a computer.
- **[Read the verified results and limitations](simulator-v1.2/VERIFICATION_v1_2.md)**.
- **[Compare all 11 scenarios](simulator-v1.2/results/scenario_comparison.csv)** — synthetic outcomes, not measured Maui performance.
- **[See where help is needed](CONTRIBUTING.md)** — Maui communities, cultural stewards, water/energy operators, engineers, ecologists, researchers and open-source developers.
- **[Browse the full integration plan](simulator-v1.2/INTEGRATION_HANDOFF_v1_1.md)** — preserved v1.1 design context; v1.2 execution notes take precedence for current software status.

The interactive dashboard runs with Python on a computer. This GitHub publication is not a continuously hosted dashboard.

## Why this matters for Maui

Water security, resident affordability, reliable power, waste handling, island food supply, healthy reefs and native habitats are connected planning problems. This project makes those connections explicit so proposed investments can be compared against existing services, retrofit-first options and distributed alternatives.

The key siting question is whether **existing Central Maui water and power infrastructure, landfill resources, the Waena battery project and planned Waikapū wastewater expansion** can support useful interfaces. Those facilities are not assumed adjacent, connected or available. Lahaina/West Maui, North Shore and Kīhei remain distinct regional candidates for services and disaster redundancy. Kanahā Pond stewardship has a separate ecological scope; it is not an industrial discharge destination.

No affiliation, endorsement, land approval, utility commitment or community consent is implied. Site and project references in the inherited evidence register still require current independent verification.

## What actually runs today

| Component | Verified v1.2 scope |
|---|---|
| Long-term model | 30 annual accounting years, 2026–2055 |
| Short-term model | 168-hour advisory electrical dispatch |
| Alternatives | Status quo; retrofit-first; distributed; HTL/AD; hybrid compute; storm outage; drought; fuel shortage; wildfire; low commodity prices; technology underperformance |
| Public-feed adapters | Weather forecast, Hawaii alerts, Kahului Harbor water levels, regional earthquakes, global space weather |
| Forecast coupling | Accepted forecast irradiance drives hourly solar; remaining hours are labeled synthetic |
| Verification | 19 local tests, 11 scenarios and 11 HTTP checks; dated receipts and hashes included |
| Interface | Local read-only Python server and HTML dashboard, scenario controls and JSON export |

Five public adapters retrieved data during the verification session. These are **dated snapshots**, not an uptime guarantee or continuous monitoring service. Alerts, ocean level, earthquakes and space weather provide context; only forecast irradiance is coupled to dispatch. Public data retain their provider classifications and licensing conditions.

## A useful early finding

The hypothetical storm scenario still has a critical-power deficit. This makes the next engineering questions concrete: verified critical loads, battery reserves, backup generation, fuel storage, water storage, safe load reduction and distributed redundancy.

Financial outputs are **incomplete screening calculations**. Annual electricity netting is optimistic; desal-specific capital costs, finance, insurance, taxes and terminal value are unresolved. Negative default NPV does not establish that an optimized network is infeasible. It also does not support claims of validated profitability. No field benefits or actual import displacement are claimed.

## Run on a computer

Python 3.10+; standard library only.

```sh
cd sites/maui/simulator-v1.2
python -m unittest discover -s tests -v
python verify.py
python server.py
```

Open **http://127.0.0.1:8765** on that same computer. To explicitly refresh public feeds:

```sh
python live_feeds.py
```

The dashboard recomputes cached-data freshness; rerun a scenario after a successful refresh. Read [full instructions](simulator-v1.2/README_START_HERE.md).

## Evidence and safeguards

Measured/observed source inputs, forecasts, simulated outputs, estimates and proposals are distinct. Core assumptions are provisional. The model is not a complete water/pollutant/elemental balance, calibrated 8760-hour utility simulation, approved engineering design, long-term climate ensemble or ecological impact assessment. The 2056 terminal checkpoint remains outstanding. Local HTTP routes were checked; browser rendering was not verified in the build environment.

Ecological, cultural, sanitary, labor and resident-affordability outcomes require independent review. Improving one modeled metric cannot establish success in another. No physical actuation or financial transaction interface is implemented.

## Public research lineage

- [Open Regenerative Compute Standard](../../README.md)
- [Earlier Maui comprehensive handoff](../../research/solgpt-maui-orcs-comprehensive-handoff-2026-10-16.md)
- [Earlier Maui water and biosolar research](../../docs/maui/MAUI_WATER_BIOSOLAR_DESAL_SOIL_RECOVERY_V0_1_2026-10-15.md)
- [Dongjiakou research reference](https://github.com/atlaslattice/manus-artifacts/tree/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build)
- [Current simulator evidence register](simulator-v1.2/EVIDENCE_REGISTER.md)

This is a Maui-specific alpha, not a verified merger of the China and US codebases. Older research paths remain intact.

## Discovery, citation and reuse

[Project metadata](metadata.json) · [CodeMeta](codemeta.json) · [Citation](CITATION.cff) · [Web metadata](index.html) · [Third-party data notice](THIRD_PARTY_DATA.md)

Project-authored material follows the repository's CC BY-SA 4.0 license. Third-party public-feed content retains its original rights and terms. Maintainer attribution: Atlas Lattice project; no personal contact details are included.

### Subject keywords

Maui, Hawaii, Hawaiʻi, Lahaina, West Maui, Kahului, Wailuku, Waikapū, Waikapu, Kīhei, Kihei, North Shore Maui, Mā‘alaea, Maalaea, Kanahā Pond, Kanaha Pond, Olowalu, Kapalua, East Maui, Maui recovery, Lahaina recovery, island resilience, disaster resilience, regenerative infrastructure, circular economy, industrial symbiosis, water security, water reuse, wastewater reclamation, R-1 reclaimed water, desalination, brine recovery, aquifer protection, cesspool remediation, ocean health, reef protection, watershed restoration, wetland restoration, native habitat, solar photovoltaics, biosolar, battery storage, microgrids, critical infrastructure, grid outage, hurricane preparedness, wildfire resilience, drought resilience, food waste, anaerobic digestion, hydrothermal liquefaction, HTL biocrude, compost, nutrient recovery, microplastics, food security, axis deer, resident affordability, workforce housing, community stewardship, 30-year simulation, 168-hour dispatch, scenario modeling, open research, Python simulator, Open-Meteo, NOAA, NWS, USGS, space weather, forecast provenance, data freshness, reproducible research, ORCS, Atlas Lattice, Dongjiakou, DragonSeek, import substitution, microhaulers, GIS siting.
