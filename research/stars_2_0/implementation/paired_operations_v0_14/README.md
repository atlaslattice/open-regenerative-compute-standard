# Stellar Forge paired evidence and potential v0.14

2026-10-29. Additive research release. Previous versions and all nonsuperseded apparatus modules remain intact. No merge, scientific freeze, or physical control.

Acoustic preparation is modeled primarily as a potential change to readiness, firing success, physical target/source overlap, and variability. Energy output is downstream of those mechanisms, not an unexplained nuclear multiplier. This release provides a runnable accounting/extrapolation lane and published source-stability benchmark, not a complete Stars yield or burn calculation.

## Delivered

- Recovered selected numerical experimental data from Streeter et al.2025, DOI10.1038/s41467-025-56248-4, Zenodo10.5281/zenodo.14236097 (CC-BY4.0). Reproduced dose, beam-divergence and centroid summaries from the source analysis window without executing the external notebook.
- Two figures: EVIDENCE_CONSTRAINED (reproduced source observations) and EXPLORATORY_POTENTIAL (detector extrapolation and hypothetical stability/throughput pathways). Both are regenerated from source JSON.
- A 7.5MeV Langau-location estimate derived from two published high-energy branch anchors with three alternate extrapolation models. Location-only, not a full track-response distribution or efficiency.
- All-attempt probability and energy accounting: readiness, firing given readiness, physical success given firing, nonzero output on unsuccessful fired pulses, preparation costs, time overhead, and missing-value propagation. Diagnostic qualification is separate and never creates a physical energy gain.
- Energy-gap register and audited news additions: EXL-50U, hollow-sphere PIC/FLUKA and Borealis PRISM. These are distinct research lanes, not imported gains.

## Run from this directory

```bash
python -m pip install -r requirements.txt
# Optional original-source recovery (~small selected ranges, not the full923MB ZIP):
python prepare_sources.py --out sources
python recover_stability.py --sources sources --out receipts/stability_replay
# Bundled derived experimental data supports a fully offline calculation:
python run.py --stability receipts/stability001/STABILITY_DATA.json --out receipts/new_run
python plot.py --stability receipts/stability001/STABILITY_DATA.json --run receipts/new_run
python -m unittest -v test_model
```

`run.py` refuses existing output directories. No RNG/seeds. All important input roles and limitations are in EVIDENCE_INPUTS.json; original source pins and member checksums are in SOURCE_LOCK.json. Source notebook/Pandas data are downloaded, CRC/SHA checked, and loaded only through restricted numeric constructors. Do not substitute arbitrary untrusted pickle files. No source notebook is executed.

13 tests pass. Repeat outputs and isolated replay are byte-identical; original-data replay reproduces the published notebook summaries to printed precision. Source acquisition uses ordinary public HTTP ranges, not authentication or a restricted-content bypass. Full ZIP MD5 was not verified because the full archive was not downloaded. No complete source-code/PIC reproduction is claimed.

See REPORT.md for numbers, NEWS_RECONCILIATION.md for new source distinctions, and ENERGY_GAPS.json for missing flows. A separate conditional nuclear transport engine remains available in previous releases; this operational overlay does not silently apply an unqualified experimental source or detector curve to it.
