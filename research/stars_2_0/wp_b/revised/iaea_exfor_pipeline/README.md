# Stars 2.0 — IAEA EXFOR nuclear-data acquisition v0.1
**Status (2026-10-27):** Provenance-first Python client published. A richer local prototype's fixture tests passed, and the committed version includes a self-test. The live IAEA endpoint was NOT available for a successful request in this environment. **No real p–¹¹B cross-section data have yet been downloaded or validated.**

## Canonical sources
- [IAEA EXFOR master files](https://github.com/IAEA-NDS/exfor_master), original EXFOR .x4 records and history (CC BY 4.0).
- [IAEA exfortables_py](https://github.com/IAEA-NDS/exfortables_py), experimental per-observable pointwise files with EXFOR entry IDs (CC BY-SA 4.0).
- [IAEA Reactions REST API](https://nds.iaea.org/dataexplorer/api/reactions/xs) and [API documentation](https://nds.iaea.org/dataexplorer/docs/).
- [IAEA Stopping Power for Light Ions](https://nucleus.iaea.org/Pages/stopping-power-for-light-ions.aspx): **separate data family** from EXFOR; do not treat it as EXFOR.
- [NIST PSTAR/ASTAR](https://www.nist.gov/pml/radiation-dosimetry-data): protons and helium ion stopping, but not necessarily a native hexagonal BN table.

## Execute
Requires Python ≥3.9 and only the standard library.
```bash
python exfor_pipeline.py test

# API query is an example of the documented parameter style, not yet live verified:
python exfor_pipeline.py fetch \
 --url 'https://nds.iaea.org/dataexplorer/api/reactions/xs?target_elem=B&target_mass=11&table=true&page=1' \
 --out data/exfor/raw

# Or use a source exfortables_py file with explicit E_in_lab(MeV), data(B), SIG:
python exfor_pipeline.py parse-exfortable /path/to/IAEA/table.txt \
 --out data/exfor/normalized
```

## Two independent workflows
1. **API:** `fetch` stores unmodified JSON response and a hash manifest. The API schema, filters, pagination, nuclear observable and reaction must be inspected before extraction. No response is automatically interpreted as a fusion cross section.
2. **GitHub-hosted EXFORTABLES:** Select `p/B-11/.../xs/` or relevant channel. Each source has an entry/subentry/pointer and units header. `parse-exfortable` accepts only labelled **E_in_lab(MeV), data(B)** with `SIG` reaction code. No unsupported frame conversion, invented nuclear uncertainties or silent channel aggregation. Reaction-code specificity still requires manual verification: `SIG` may be a partial channel, not necessarily total 3-alpha production.

## Mandatory scientific gates
- **Energy frame:** The prominent experimental proton resonance described as **E_p(lab) ≈ 675 keV**, corresponding to about 618 keV CM for stationary ¹¹B, is NOT the earlier v0.1/v0.2 675 keV CM surrogate feature. Resolve exact entry/channel and its published convention before fitting.
- **Evidence type:** Experimental points, evaluated cross sections, interpolation and simulations are distinct categories. Never present direct interpolation as an evaluated nuclear standard.
- **Particle channels:** Resolve (p,α)⁸Be, inclusive breakup, state-specific yields and counts per fusion event. Differential alpha spectra are not total cross sections.
- **BN stopping:** Obtain proton/He stopping/range curves from independent stopping repositories or licensed material-specific simulations, with hBN density, material composition, range uncertainties, temperature/state and provenance. Never insert unverified surrogate coefficients as ICRU/SRIM data.
- **Tests:** The `test` command uses one fabricated input solely to check table parser and lab→CM arithmetic; it does not validate physics or confirm live API reachability.
- **Attribution/licenses:** Preserve upstream EXFOR credits, master entry/subentry revision, reference paper and upstream CC license; do not silently relicense upstream table content.

## Expected next work
Confirm exact p–¹¹B reaction filters with live OpenAPI, list returned EXFOR entry and publication IDs, make dated raw snapshot, create curated channel-specific table, add regression checks versus source tables, then feed a separately versioned WP-B model. Keep measured alpha spectra and converter acceptance outside this first acquisition layer.

**Status:** A working *fetch/parse scaffold*, not yet an operational auto-synchronized or independently calibrated nuclear-data service.
