# Physical sequential kinematics and uncertainty recovery v0.7

2026-10-29 America/Chicago. Additive draft stacked on measured calibration v0.6 / PR#28. Historical source files and research remain unchanged. No merge, scientific freeze or blinded prediction.

## Implemented

`sequential.py` repairs the sequential **kinematic map**: p+B11 forms a compound state with invariant mass fixed by its incident four-vector; that state splits into alpha+an explicit alpha-pair invariant mass; the pair splits into two alphas. Exact Lorentz boosts connect the pair rest frame, compound CM and laboratory frame. Physical masses and their source provenance are hash-pinned from v0.5, including its explicitly older NIST B11 mass snapshot and uncertainty qualification. Q is derived from those masses.

For given input directions and pair relative energy, the map returns all birth four-vectors and checks total four-momentum, alpha mass shells and intermediate invariant mass. Pair relative energy means `invariant(pair)-2*m_alpha`, not Be8 excitation energy. Directions are expressed on rotationless boost axes parallel to the CM Cartesian axes. Output particle indices label a coordinate chart; they do not identify an experimentally observable decay history.

Angular-momentum, parity and identical-alpha **pair** selection rules are enforced. A pure2-minus parent cannot decay through ground-state0-plus Be8; a3-minus parent can do so with primary l=3. These checks do not replace the required coherent symmetrization of the full three-alpha source amplitude.

**The map is runnable; a calibrated probability distribution is not yet supplied.** There is no default98.5/1.5 branching, constant-width Cauchy draw, assumed angular law, synthetic detector efficiency or acoustic gain. Building a physical source requires selecting and implementing a sourced amplitude, its uncertainty and its measurement-response boundary. `require_calibrated_source()` rejects promotion until that exists. The previous phase-space null and original Gemini surrogate remain available unchanged as separate controls.

## Numerical verification

Fourteen checks pass. The seeded map verification covers800 conditional events, incident proton LAB energies0.162/0.675/1/2.64/3.8MeV and an explicit grid spanning the allowed pair energy. Seed20261029, NumPy default_rng/PCG64. The input fractions and random directions are **numerical verification fixtures**, not sampled physical source parameters.

Maximum residuals from the run:

| Check | Maximum |
|---|---:|
| Four-momentum | 3.638e-12MeV in c=1 units |
| LAB kinetic-energy sum | 3.055e-12MeV |
| Intermediate invariant mass | 1.819e-12MeV |
| Relative alpha mass shell | 8.045e-16 |

The suite includes inverse-frame reconstruction, forbidden-channel rejection, output permutation conservation, a deliberately broken Galilean-boost mutation, malformed inputs, repeatability, data censoring, error-column mutation and source-observable guards. Correct permutation bookkeeping is not claimed as an amplitude-symmetry test. These numerical tests do not validate a source spectrum, material transport, cross section or net energy prediction. The original v0.4 physical-mass failures are preserved in the hash-pinned v0.6 receipt rather than overwritten or retested against its own approximate mass conventions.

## Newly recovered experimental data

`MAZZUCCONI2025_TABLE2.json` transcribes all28 published rows directly from Table2 on PDF page10 of Mazzucconi et al., EPJA61(2025)114, [DOI10.1140/epja/s10050-025-01589-3](https://doi.org/10.1140/epja/s10050-025-01589-3). The original rendered table was visually checked. Both reported energy and differential-quantity errors are retained; the smallest-energy alpha0 entry remains an upper limit, not zero. Explicit source warnings about possible Al-support alpha contributions are flagged, without treating unflagged rows as background-free.

The source calls this a differential cross section at60degrees LAB and defines it using alpha Counts/(Nt Np dOmega). Event-multiplicity normalization is left unresolved; no automatic division by3, multiplication by4pi, angular transformation or pooling with the 2016 event table is performed. The full article is not a complete raw-event/covariance dataset.

See [UNCERTAINTY_REVIEW.md](UNCERTAINTY_REVIEW.md) for what newer publications can close and what still requires data recovery or experiment-specific calibration. The source disagreement is retained: implementing the older pure-l3 ansatz as settled physics would miss relevant later exclusive data. `PARAMETER_REGISTER.json` distinguishes constants, published model/fit parameters, numerical controls and unresolved inputs. None of the recovered fit percentages or formal R-matrix energies is silently installed as a universal source parameter.

## Reproduce

Keep this directory beside the previous implementation directories on the stacked branch. Dependency hashes are checked at import.

```bash
python -m pip install -r sequential_kinematics_v0_7/requirements.txt
python sequential_kinematics_v0_7/verify_sequential.py --out sequential_kinematics_v0_7/receipts/new_kinematics_run
python -m unittest discover -s sequential_kinematics_v0_7 -v
```

To independently reconstruct the new table from its source, install Poppler and run:

```bash
python sequential_kinematics_v0_7/extract_2025.py --download --pdf sequential_kinematics_v0_7/sources/Mazzucconi2025.pdf --out sequential_kinematics_v0_7/receipts/new_extraction.json
```

The PDF is downloaded only if missing and must match its pinned SHA256. The source PDFs are not bundled. `SOURCE_INDEX.json` records source URLs, hashes and locators. New output paths are required; no previous receipt is overwritten. A repeat extraction was compared byte-for-byte with the bundled fixture. The independent waveform/acoustic/UI modules are retained without being promoted into this source calibration.

## Next gate

Complete a documented, symmetrized amplitude implementation and qualify its input conventions before fitting spectra. Reconcile the published count-normalized quantities, incident-energy response, target/backing transport and detector acceptance, then fit and assess on separate experimental campaigns. The current advance removes kinematic errors and recovers real numerical uncertainty information; it does not establish the complete apparatus yield or net electrical gain.
