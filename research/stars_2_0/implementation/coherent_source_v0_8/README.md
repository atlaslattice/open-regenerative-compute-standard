# Stellar Forge Reference — coherent source v0.8

This additive candidate prioritizes coherent l=1/l=3 mixing and Bose symmetrization for the isolated unpolarized 2-minus proton–boron resonance. Pure-wave and incoherent alternatives remain controls. It changes conditional three-alpha source shapes, not the reaction cross-section normalization. It does not establish apparatus yield, acoustic enhancement, sustained burn, ignition, or net power.

The calculation uses the sequential amplitude structure in [Kuhlwein et al.](https://doi.org/10.1016/j.physletb.2021.136857): angular-momentum coupling, Coulomb penetrability/shift/phase, a single Be8(2+) level, and coherent summation of the three primary/pair partitions before squaring. Parent magnetic substates are averaged incoherently. Event four-vectors obey relativistic kinematics; radial R-matrix factors use nonrelativistic channel energies. This hybrid is explicit. No final-state-interaction correction is implemented.

The physical inputs and their qualifications are in `PARAMETER_PROVENANCE.json`; source URLs and downloaded identities are in `SOURCE_INDEX.json`. The primary channel radius is a generic literature convention. The published mixing coefficients are adapted to the raw amplitude basis: exact paper basis normalization and Coulomb phase conventions have not been independently reconciled. These are **exploratory literature-informed shapes, not a calibrated reproduction of the published fit**. `CALIBRATED` is rejected.

## Numerical correction and preserved failure

An 80-point comparison found GSL2.7.1 Coulomb discrepancies as large as 3.082% in penetrability and 0.03230 absolute in shift function. A 40-decimal mpmath1.3.0 calculation independently supports the archive-pinned Michel CPC backend: maximum relative penetrability error 5.92e-10 and absolute shift error 3.85e-9 on this grid. The unchanged gate is 1e-7 for both. Passing the Wronskian alone did not detect the GSL discrepancy.

Production uses Michel CPC, not GSL Coulomb. GSL remains for tested small-integer Wigner3j coefficients. This finding concerns the tested version/domain; no claim is made about every GSL version or a corresponding percentage change in fusion yield. The original failed comparison and original GSL shape outputs remain in `receipts/coulomb_run001` and `receipts/shapes_run001`; they are rejected as production outputs. The original GSL implementation is `gsl_reference.py`; the exact original runner is `receipts/gsl_baseline/run_shapes_original.py`. Preferred results are `receipts/shapes_run002`. Repeat runs reproduced those shape and receipt bytes.

## Reproduction

Use the stacked repository with the adjacent hash-pinned `coupled_reference_v0_5` dependency. Python3.12.14, NumPy2.3.5, SciPy1.17.0, mpmath1.3.0, GNU GSL shared library2.7.1, C++ compiler13.3.0 and Poppler26.05 were used. Compiler-specific shared-library bytes need not match across environments; the numerical gate must pass.

```sh
cd research/stars_2_0/implementation/coherent_source_v0_8
python -m pip install -r requirements.txt
python prepare_cpc.py --download --archive sources/ORM-v1.zip --out build
python -m unittest -v test_coherent
python verify_precision.py --out receipts/new_precision_run
python run_shapes.py --config CANDIDATE_CONFIG.json --samples 2048 --seed 20261029 --out receipts/new_shape_run
python run_sensitivity.py --help
python extract_munch.py --download --pdf sources/Munch2019v1.pdf --out receipts/new_Munch_table.json
```

Build and run destinations must be new. The production loader defaults to `build/libcpc.so`; `STELLAR_CPC_LIBRARY` selects another built library. `prepare_cpc.py` verifies the upstream archive SHA256 and records compiler, wrapper, source and library identities. Upstream ORM/CPC files remain under their original GPL3-or-later archive notices; they are downloaded, not relicensed or redistributed here. No full ORM or simX reproduction is claimed.

The common proposal is constant-matrix-element invariant phase space, used only for importance sampling. Candidate amplitudes determine the weighted shape. Each conditional event contributes three alphas; histograms sum to three. Raw amplitude scale is arbitrary and is not an event rate. The 2048-proposal runs at 0.675MeV LAB and their effective sample sizes are exploratory numerical diagnostics, not experimental uncertainty estimates.

## Recovered real data and remaining calibration

`MUNCH_PREPRINT_V1_TABLE1.json` preserves 45 alpha0 channel cross-section entries from [arXiv1908.04064v1](https://arxiv.org/abs/1908.04064). Rendered Table1 contains duplicated labels at 950keV and 1900keV. All four affected entries are preserved and excluded from automatic fitting. Neither guessed energy corrections nor deduplication are applied. The extraction has not been verified against the journal table and is not a full three-alpha differential dataset. No fit has been run.

`RESOLUTION_LOG.md` separates recovered facts, numerical corrections and remaining gaps. Next calibration needs compatible exclusive data with detector acceptance, exact amplitude conventions, correlated parameter treatment and model-discrepancy validation. Alpha stopping in actual target materials and hot-target transport remain separate blockers to apparatus predictions. Earlier stopping calibration and all nonsuperseded module versions remain preserved in the stack.
