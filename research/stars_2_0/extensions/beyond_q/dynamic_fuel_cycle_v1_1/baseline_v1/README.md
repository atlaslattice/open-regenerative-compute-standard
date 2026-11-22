# Dual-reactor tritium self-sufficiency audit — research release v1.0
**Standalone peer-reviewable arithmetic / not validated reactor performance.**
- [White paper](WHITE_PAPER.md) — complete reconciled logic, defined A0/A1/A2, corrections, gates
- [Citation / provenance appendix](APPENDIX_SOURCES_AND_PROVENANCE.md) — primary research bibliography, audit trail, role of GPT-6, DeepSeek, Gemini Argon
- [Python reproducibility script](tritium_ledger.py) — deterministic simple annual balance; no neutron transport
- [Scenario table](SCENARIOS.csv) — gross TBR × ultimate recovery sweeps
- [Metadata](research_metadata.json) — search/discovery
**Quick check:** `python3 tritium_ledger.py`; repeat with `--efficiency .85`. Both assume A 3.65 kg/FPY **actually available**, although currently only a speculative pre-processing estimate. The white paper deliberately reports operational self-sufficiency as UNRESOLVED.
