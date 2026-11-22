# ORCS v0.5: National electricity and microgrid-resilience ledger

**PROPOSED / EMPIRICAL-SOURCES ONLY / NOT LIVE / ZERO REALIZED CREDIT — 2026-10-14.** Independent additive energy layer. No fictional facilities, observations, current margins, or blackout predictions are used.

Includes an official-source registry, strict UNKNOWN-preserving energy accounting diagnostics, and a site-level *proposed* microgrid endurance evaluation. Electricity is modelled by **balancing authority** and by **state** with separate time resolutions; no unverified mapping between those geographic systems. Grid accounting checks never interpret generation minus demand as physically deliverable surplus.

Public source inventory includes EIA-860/923/930/861, DOE-417, PNNL outage history and DOE microgrid methods. Source *documentation* has been verified, but **live data ingestion is not connected** in this package. EIA final 2025 state historical tables were released October 7, 2026; 2024 U.S. electric generation was about 4.309 billion MWh, an older verified baseline, not current annual generation.

Operational access and reliability limits: Net interstate generation is not freely dispatchable without network/security/transmission/market data; missing reserve margin and generator outages are UNKNOWN. Microgrid theoretical storage sufficiency is not black-start, switchgear, protection, duration, weather availability, islandability or deployment approval. No actual site is assumed to have a microgrid.

Run `python3 -m unittest discover -s . -v` and `python3 energy_model.py`.

Next tasks: download and archive EIA final 2025 plant/state generation by source; pull EIA-930 balancing authority data with time-zone and interchange sign convention checks; obtain operator-public regional reserve margin forecasts; import PNNL outage history for historical reliability associations; calibrate proposals using actual site electricity and verified engineering permissions. No automatic utility operations, emergency orders, or exports.
