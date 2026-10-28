# Stopping-source qualification and aluminum reference check v0.1

STATUS: CANDIDATE DATA AUDIT; PHYSICAL CALIBRATION NOT RUN  
Date: 2026-10-28. Conventional G0-B physics scope only.

## Concrete result

Recovered a pinned, explicitly headed PSTAR aluminum table from a scientific-code repository and exercised the preceding G0-B transport kernel with it. This is reference-table use rather than another artificial constant-stopping example. It remains a **third-party mirror candidate**, with primary-source byte identity and experimental validation unresolved.

- 132 source rows pass strict header/unit/monotonicity checks.
- Every row's electronic+nuclear stopping sum agrees with total stopping within a budget derived from its printed decimal precision.
- Projected range and detour factor agree with CSDA range within printed-rounding bounds. Projected range is retained as a distinct quantity, never substituted for CSDA.
- Six adapter/integration tests pass, including semantic mutations with recomputed hashes, so hash checking alone cannot hide a wrong projectile, material, header or column meaning.
- Twelve transmission cases compare the existing range-inversion kernel against independent integration of the source's total stopping column.
- Largest residual-energy formulation difference in these cases is **0.002450083874 MeV = 2.450083874 keV**. This is an interpolation/formulation sensitivity, not a measured uncertainty or calibration pass.

The boron mirror contains **77 records in four groups: A=27, B=17, C=15, D=18**. The numeric file has no unit headings or reference mapping. It is parsed only for an inventory and explicitly quarantined; no standard-unit range table or BN transport input is generated from it.

## Source identity

Repository: `dedx-erpa/dedx`, pinned revision `83e2babc0612dbac733705c02973418ef87e210e`.

| Candidate | Path | Git blob | SHA-256 |
|---|---|---|---|
| PSTAR aluminum mirror | `data/Al/pstar.txt` | `5799d82300c78411c8fb2cfbd8a55629e58bd378` | `3fe6459ec4abde6052bcb63f427ea856bbc35dd8506014191145b4eb9253db5e` |
| Boron electronic mirror | `data/iaea/B.txt` | `0e9b5db1d1f870e025d7fb060d3d0066c052c0ad` | `ab93971d116d0ef37ce64fa0f83153daf771ab46eba98ee72510dd84b16a7c97` |

[Pinned aluminum input](https://github.com/dedx-erpa/dedx/blob/83e2babc0612dbac733705c02973418ef87e210e/data/Al/pstar.txt), [pinned boron candidate](https://github.com/dedx-erpa/dedx/blob/83e2babc0612dbac733705c02973418ef87e210e/data/iaea/B.txt).

The same boron file occurs under `data/iaea/SCSData/01H/B.txt` with the **same Git blob**. These are aliases of one source, not two independent datasets. The external repository also contains calculated stopping/range outputs; those were not relabeled as experimental data or substituted here. No upstream program was executed or copied into this implementation.

Raw inputs remain external and retain upstream attribution/rights. This companion does not vendor or relicense the upstream code, raw archive or entire tables. A mirror hash establishes identity of this recovered copy, not equality to a current NIST/IAEA release.

## Numerical comparison

For each case, method A uses the existing piecewise-linear range table and its inverse. Method B interpolates total mass stopping linearly in energy and integrates its reciprocal analytically segment by segment. It finds residual energy by bracketed bisection. Method B never uses the tabulated range column or the range-inversion implementation.

Within a linear stopping segment S(E)=S0+a(E-E0), the segment mass range is log(S1/S0)/a, or delta_E/S0 when a=0. Both routes use the same source; their agreement is **internal numerical consistency**, not an independent physical benchmark.

The cases have E_in = 0.5, 0.675, 1.0, 2.0 MeV and normal areal masses 0.0001, 0.0005, 0.001 g/cm2 at normal incidence. These are model comparison settings, not characterized physical foils. No density or micrometre conversion is invented. All residuals stay within the source's energy domain; neither method supplies a low-energy tail.

| E_in (MeV) | Areal mass (g/cm2) | Range-column E_out (MeV) | Stopping-integral E_out (MeV) | Difference (keV) |
|---:|---:|---:|---:|---:|
| 0.5 | 0.001 | 0.197420334 | 0.197310920 | 0.109413 |
| 0.675 | 0.001 | 0.433149171 | 0.433010056 | 0.139115 |
| 1.0 | 0.001 | 0.817248062 | 0.817532851 | 0.284789 |
| 2.0 | 0.001 | 1.885740402 | 1.888190486 | 2.450084 |

No numerical threshold was selected to declare physical agreement. Future instrument uncertainty and required predictive precision must determine whether interpolation refinement is necessary. Neither route is designated experimental truth. Source rounding, interpolation grids and common provenance limit what this check can establish.

## Reproduction

Requires Python 3.12.14 (tested), standard library, the two exact external inputs above and the previous transport source:

`research/stars_2_0/implementation/g0b_transport_reference_v0_1/transport.py` at draft PR #11 commit `872c3322ec5d91dab341c357468977eb92e1444c`; SHA-256 `f3a43e6781da00bdc47b9f31605817e11fe28a5ae12149538f2787e5a8d6439e`.

```bash
python stopping_source_check_v0_1.py \
  --al-mirror /path/to/data/Al/pstar.txt \
  --b-mirror /path/to/data/iaea/B.txt \
  --transport-file /path/to/g0b_transport_reference_v0_1/transport.py \
  --out /path/to/NEW_DIRECTORY
```

The runner checks source hashes before use/import and refuses an existing output directory. `receipts/run_002` is authoritative for the published root script. `run_001` preserves the earlier successful four-test run and its source snapshot; the later version adds semantic-mutation tests and passes six tests. Both preserve the same numerical comparison outcomes. No random sampling occurs.

## Physical-data decision

Read [source acquisition and benchmark register](SOURCE_ACQUISITION_REGISTER_v0_1.md). The aluminum reference is a useful support/filter-material interface check. It is not a boron substitution. The next required gate is primary-file reconciliation plus an independent, sufficiently characterized transmission measurement in the applicable energy/material regime. The full physical G0-B prediction remains uncalibrated.
