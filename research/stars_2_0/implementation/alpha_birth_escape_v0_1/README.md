# Stellar Forge — conditional alpha birth and escape v0.1

2026-10-31. Additive numerical research release, downstream of draft PR55 at `ccd944f4496ae98c68c916269edc4fdd8dfed01a`. No historical files replaced; no merge or scientific freeze. **Net wall-plug power remains unevaluated.**

## What ran

The saved field-on target handoff supplies 16 local proton-energy cells, expected reaction weights, and the actual incoming beam direction. For each cell we generate correlated relativistic three-alpha proposals, apply five conditional source-weight models, rotate momenta into the receiving laboratory direction, and propagate each alpha through a cold elemental-11B infinite slab. Each model is normalized separately to the SAME receiver event count: 0.01628033146332977 weighted expected reactions. The small absolute count is a numerical fixture, not a predicted laboratory pulse.

Source controls: constant-matrix-element Lorentz-invariant phase space; exploratory coherent l=1+l=3; incoherent ablation; pure-l=1; pure-l=3. The coherent model is the inherited unpolarized 2-minus candidate, with mix coefficient 0.76 and phase 0.67*2*pi in the declared RAW basis. These are not verified branch fractions. Extending that candidate to every local receiver energy is exploratory; amplitude conventions, final-state interactions and other parent-state contributions remain unresolved. This release tests a conditional transport interface, not an absolute cross-section prediction or an exact Kuhlwein reproduction.

All variants preserve the upstream reaction count and alpha birth energy; no extra fusion multiplier is introduced. The phase-space null is a control, not a physical reaction fit.

## Results and checks

| Run | Proposals/cell | Seed | Stopping grids | Outcome |
|---|---:|---:|---|---|
| run001 | 128 | 20261031 | 2048 / 4096 | 29/30 checks; refinement FAILED at 4.189 eV |
| run002 | 128 | 20261031 | 8192 / 16384 | 30/30; maximum refinement difference 0.251 eV |
| run003 | 256 | 20261101 | 8192 / 16384 | 30/30; maximum refinement difference 0.292 eV |
| run004 | 128 | 20261031 | 8192 / 16384 | 30/30; exact scientific replay of run002 |

The stopping gate stayed at 1 eV. Original coarse code, log, result and event bank remain preserved. `transport_v002.py` also explicitly handles a zero-material-path boundary case below the stopping floor; the earlier transport implementation is retained. This branch does not alter sampled interior-cell results.

Thirteen transport/rotation unit tests and 78 bank audits pass. The bank audits need NumPy only, not the compiled Coulomb backend. Same-seed replay compares every array and all result fields except elapsed runtime; it does not infer identity from archive timestamps. Maximum event four-momentum residual is 5.46e-12 MeV, conditional on inherited nominal masses.

| Source | Escaping energy run002 (weighted MeV) | run003 (weighted MeV) |
|---|---:|---:|
| Phase-space null | 0.1490420364 | 0.1490551134 |
| Coherent l1+l3 | 0.1489518841 | 0.1490032470 |
| Incoherent ablation | 0.1489304491 | 0.1490702243 |
| Pure l1 | 0.1489233203 | 0.1490869535 |
| Pure l3 | 0.1489534730 | 0.1489912617 |

Birth kinetic energy is 0.1522944597 weighted MeV in every variant. This includes reacting-proton kinetic energy as well as nuclear release, so it must not be relabeled Q alone. The ordering changes with sampling; **no best-model claim is supported**. The second seed also doubles sample count: this is sensitivity, not an isolated convergence rate, uncertainty interval, or independent experimental validation. Finite importance-sampling ESS is reported per cell. Source/model and physical uncertainties have not been propagated.

## Material and geometry boundaries

Normal 11B column is 1e18 atoms/cm2. Birth depths use the upstream midpoint-cell quadrature. The slab is laterally infinite; it does not represent the finite printed pocket, porous scaffold, supports, mirrors, scattering/straggling, hot target, or material evolution. Material is cold ELEMENTAL 11B, not BN or B4C. Stopping uses the inherited calculated SRIM13 electronic tables and ZBL_SIMNRA_7_04 nuclear model; these are not newly measured stopping data. Provenance and original references remain in `stopping_models_v0_4/README.md`, TABLE_LOCK and upstream license/lock files.

The alpha stopping table has a positive lower energy floor of 0.004002603 MeV. Crossing it is UNRESOLVED, never silently “stopped.” Per alpha:

`birth kinetic = resolved escaping kinetic + material transfer lower bound + unresolved kinetic budget`.

When the floor is reached, the remaining floor energy is retained as an unresolved budget. Conditional escaping-energy bounds are [resolved escape, resolved escape + unresolved budget]. These bound the missing tail within the assumed model; they are not comprehensive physical confidence intervals. Grazing trajectories are unresolved because no finite lateral boundary is defined. A zero-column post-birth control is vacuum propagation, not a nuclear zero-target test. No stopping extrapolation above the grid is allowed.

## Reproduction

Keep sibling implementation versions in their original relative layout from the stacked PR55 branch. Python 3.12.14 / NumPy 2.3.5 were used; SciPy and the inherited archive-pinned Michel CPC shared library are needed for full source regeneration. Consult `coherent_source_v0_8/prepare_cpc.py` and its original build/precision receipts. The compiled GPL backend is not redistributed here. The source archive hash, license and original download instructions remain upstream; its local compiled-library hash is in each receipt. WarpX is not rerun by this alpha postprocessor: its receiving source is the hash-pinned PR55 result.

```
python alpha_birth_escape_v0_1/unpack_banks.py
python alpha_birth_escape_v0_1/audit_banks.py
python -m unittest discover -s alpha_birth_escape_v0_1 -v
python alpha_birth_escape_v0_1/reproduce.py --receiver warpx_target_handoff_v0_2/run001/RESULTS.json --models . --samples-per-cell 128 --seed 20261031 --out alpha_birth_escape_v0_1/fresh_run
```

`reproduce.py` checks the inherited dependency hashes before launching the refined runner. Output directory must not already exist. Use the numerical fixture values only to reproduce this control. Source conventions and provenance are pinned in `coherent_source_v0_8/SOURCE_INDEX.json`, PARAMETER_PROVENANCE and CANDIDATE_CONFIG. The Kuhlwein source is DOI [10.1016/j.physletb.2021.136857](https://doi.org/10.1016/j.physletb.2021.136857); no new exclusive data or acceptance calibration was recovered in this release. Nominal physical masses and mass uncertainty caveats are inherited unchanged from `coupled_reference_v0_5/MASS_SOURCE.json`.

## Next boundary

Resolve finite target geometry, material identity/density, birth/exit positions and times, and uncertainty before injecting alpha trajectories into a collector or magnetic map. Then test a declared collector field and recoverable electrical work, with electrode losses and particle/energy conservation. Full wall-plug assessment additionally needs measured source normalization and efficiency, acoustic and magnetic power, duty cycle, cooling, target replacement and startup/steady-state accounting. A/B/C apparatus comparisons remain separate and incomplete. None of the numbers here demonstrates sustained burn, net positive electricity, or acoustic improvement.
