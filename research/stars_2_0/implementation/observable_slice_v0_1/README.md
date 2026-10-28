# Source/observable and identifiability slice v0.1

Exploratory implementation of the explicitly authorized **v0.3 A1/A2 + early synthetic identifiability scope**. Project lead authorized this scope after Tidal Lantern's review with “Yeah lets run it!!”. This is not authorization to merge, freeze scientific assumptions, accept empirical calibration or release blinded G0-B predictions.

Parent: `research/stars_2_0/contracts/GPTWORK_IMPLEMENTATION_CONTRACT_CANDIDATE_v0_3.md` at commit `9bfe5e6bace4e7cc1bc9b64962ab99325ebd462f`. All files in this directory are new. Existing sources, contracts and receipts remain unchanged.

## Implemented behavior

- Typed source identity, quantity, frame, acceptance/interpretation, source hash, evidence identity and license-status metadata.
- Exact Decimal source values and explicit transformation records; incident-energy uncertainty survives normalization and JSON serialization. Unreported uncertainty remains null with `not_reported`, distinct from a reported zero.
- A strict adapter for the archived cross-section CSV. No implicit LAB/CM conversion or alpha-to-event division. The generic `sigma_b` heading is retained as source syntax, not treated as evidence of fusion-event semantics.
- Named common-nuisance loadings produce shared covariance, including across sources. Registry identity conflicts and duplicate evidence rows are rejected. Evidence IDs must be curated: byte hashes cannot reveal all overlapping or derived publications.
- Measured zero, missing, censored and invalid outcomes are distinct. Undefined ratios serialize as null with a reason; JSON NaN is prohibited. This outcome helper is not a complete all-shot causal ledger.
- Local linear sensitivities are scaled by declared parameter scales and whitened with the full covariance. SVD exposes weak/null directions. Rank-deficient fits refuse unique point estimates. Singular covariance is rejected rather than silently regularized.
- An exploratory synthetic harness checks recovery, interval coverage, discrepancy and prior sensitivity against an independent scalar regression oracle. Generative shared noise uses a separate construction from the fit's covariance whitening.

## Source receipt and a newly detected format defect

The first strict import failed because the archived CSV writes `11B(p,a)8Be` without CSV quoting: the comma creates an extra field. We preserved the original bytes. The adapter repairs only the exact SHA-256-qualified legacy file, checks the precise split-field structure, and records that repair in every normalized observation. It does not guess how to repair arbitrary malformed CSVs.

`receipts/run_001` preserves the initial failure and the pre-repair importer. `receipts/run_002` is the successful implementation receipt. The original importer elsewhere in the repository remains unchanged.

Independent fixed-width extraction from the original EXFOR C2973002 table reproduces all **41 rows / 123 numerical cells** exactly after MB-to-barn conversion using Decimal. This validates numerical transcription, not event normalization or the full experimental likelihood. The source table supplies no incident-energy error column; the synthetic regression fixture verifies that nonzero errors survive when supplied.

Source locators:
- Archived CSV: `research/stars_2_0/wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv`, parent commit above; Git blob `a288d4a3631c60b07565a22a587ef3b26e5d7153`.
- Original EXFOR: https://github.com/IAEA-NDS/exfor_master/blob/main/exforall/C29/C2973.x4
- Original publication: DOI `10.1007/s10894-011-9473-5`.

Input SHA-256:
- CSV: `e56d240ea05fb8663debbb42cef99a93ef466d309eec3dbeb239f77509a6d089`
- EXFOR: `e6bb8289bf67c485af9a97c212d5604421dae7ab5aad91bbf7064618277d0efb`

The EXFOR URL is a retrieval locator; the hash identifies the required bytes. A changed upstream file must be separately qualified. External raw EXFOR bytes are not vendored here. Preserve upstream attribution and establish data reuse terms for a distribution; the repository's code/document license does not relicense third-party data.

## Reproduction

Tested with Python 3.12.14 and NumPy 2.3.5. No network calls occur in the implementation. From this directory in a repository checkout:

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python -m unittest discover -s . -p test_slice.py -v
OPENBLAS_NUM_THREADS=1 python run_slice.py \
  --csv ../../wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv \
  --exfor /path/to/C2973.x4 \
  --out /path/to/new_run_directory
```

Acquire the original EXFOR file using the source locator above; the runner checks its SHA-256. Output paths must be new: the runner refuses an existing output directory. Preserve failed runs. Unit tests require no external data; the full run additionally requires both verified source files.

The run produces normalized observations, covariance, synthetic findings, test log and a run receipt with code/input/output hashes. Test timing in the log can vary; numerical last digits can vary across BLAS/platforms. The synthetic seed is 20261028 and repetitions are 2,000. Requirements pin the single nonstandard runtime dependency; this is not a containerized, hash-locked supply-chain release.

## Executed findings

All **15 unit tests passed**, alongside the source reconciliation check. Tests include input/schema mutations, dropped-uncertainty regression, incorrect shared-error averaging, duplicate evidence, singular covariance, structural degeneracy and coordinate/unit invariance. These are software and synthetic checks, not fifteen empirical validations.

| Synthetic result | Value |
|---|---:|
| Independent oracle estimate maximum absolute difference | 1.33e-15 |
| Nominal 95% interval coverage, intercept / slope | 95.45% / 95.45% |
| Coverage with omitted quadratic discrepancy, intercept / slope | 83.8% / 95.45% |
| Wide-design slope standard deviation | 0.05164 |
| Narrow-design slope standard deviation | 51.64 |

Both wide and narrow designs have full rank and nine assumed unit-cost measurements. Their slope uncertainties differ by a factor of 1,000. The design variable and parameters are dimensionless; they are not a calibrated proton/alpha measurement model. Coverage has binomial standard error approximately 0.00487 near 95%; tests use declared five-standard-error Monte Carlo sanity bounds, not facility acceptance criteria.

A further useful result: incorrectly treating the common offset as independent makes the intercept uncertainty too small (0.0745 instead of 0.2028), while making slope uncertainty too large (0.1155 instead of 0.0516). Correlation is direction-dependent information, not simply an uncertainty multiplier. This motivates calibration-aware measurement design rather than optimizing raw shot counts alone. It is a standard statistical consequence, not a new physical effect.

## Boundaries and next work

This is a narrow first vertical slice, not completion of every v0.3 acceptance gate. Statistical errors and the 3.6% target normalization are interpreted as independent statistical standard deviations and one linear unit-variance common nuisance for this working covariance model. Their distributions/correlations require source qualification before empirical inference. Energy errors are preserved, but an errors-in-variables likelihood is not implemented. No interpolation, nonlinear detector response, transport, kinematics, energy recovery or full experimental causal estimator is supplied.

The independent oracle covers a symmetric linear model; it does not validate nonlinear nuclear inference. Profile likelihoods, empirical grouped holdouts, correlated nuisance groups, facility intervention costs and a qualified proton-transmission/alpha-spectrum forward model remain subsequent work. Prior sensitivity is a disclosed Gaussian slope-prior toy with an unregularized intercept and noiseless weak-design observation, not a recommended physical prior.

The next spectral experiments remain as recommended by Tidal: a bounded physical plate/membrane comparator, frequency-dependent transfer and sensor/actuator placement, and deliberate boundary/edge mutations. They are separate from this source slice. The full TCSS/Path B operator and any membrane-control or fusion benefit remain unvalidated. Later Gemini v0.4 repository ingestion/hash reconciliation/local reproduction remains outstanding.
