# Stellar Forge - published experimental figure benchmarks v0.13

Additive research release, 2026-10-29. Previous packages remain unchanged.

This release recovers four experimental CR-39 helium histograms from Schollmeier et al.2023 Supplement Figure S3 and six PDF vector traces from Kuhlwein et al.2022 Figure3. Published experimental observations are legitimate calibration/benchmark evidence. The limited claim is what our recovery actually preserves, not whether the experiment is respectable.

## Result

- Four helium examples: 0.23 +/-0.05, 0.56 +/-0.06, 2.25 +/-0.06, 4.52 +/-0.11 MeV. Preserve the source interval labels without interpreting them as Gaussian SDs. The last histogram includes a sputtered-ion population.
- 118 visible approximate display bins out of 184 candidate bins. Other bins are unresolved, not zero. Full histogram totals/means and absolute efficiency remain unknown.
- Kuhlwein black experimental trace repeated in three panels; these are one dataset, not three independent replications. Orange curves are the published models, not newly generated Stellar Forge predictions. Figure3 projects the Figure2 Dalitz fits; no new fit was performed in the paper for those projections.
- Area-normalized descriptive shape distance (total variation over the recovered display interval): pure l=1 0.133265; pure l=3 0.096926; coherent mixture 0.047560. This metric prefers the published mixture among these three published curves. It is not a reproduction of the Dalitz likelihood, chi-square, mixing coefficient fit, physical acceptance, or event rate.
- Source formula/location discrepancy remains unresolved. No 7.5 MeV alpha calibration, acoustic yield gain, ignition, apparatus validation, or net-electric result is established.

## Reproduce

```bash
python -m pip install -r requirements.txt
python recover.py --download --sources sources --out receipts/new_run
python -m unittest -v test_recovery
python verify_render.py --pdf sources/Kuhlwein2022.pdf --run receipts/new_run
python plot_recovery.py --run receipts/new_run
```

Requires Poppler `pdftoppm` for the independent raster cross-check. Outputs are JSON plus two regenerated PNG plots. Pinned source PDFs are downloaded and hash-checked, not bundled. The extraction works offline once these PDFs are available. Ten source-backed tests ran without skips; repeated extraction bytes and isolated-layout replay match. No random sampling, fitting, or seeds are used.

`receipts/run002` is the current complete result. `SOURCE_INDEX.json` contains original source URLs and hashes. `REPORT.md` explains results, limitations and next decisions. `receipts/VERIFICATION.json` records integrity checks. Tests validate recovery/software behavior, not apparatus physics.

## Policy

OFF reference receives zero additional unmeasured acoustic enhancement credit. Unqualified ON effect and costs remain unknown. Acoustic evidence status is revisable; no permanent zero-effect label. No existing apparatus module was removed or modified, and no scientific contract is frozen.
