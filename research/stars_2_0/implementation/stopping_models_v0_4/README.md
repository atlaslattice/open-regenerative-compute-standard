# Cold proton/alpha stopping-model replay v0.4

Additive research version, 2026-10-28 America/Chicago. Earlier measured-data and implementation versions remain unchanged. This release makes calculated proton and alpha stopping/finite transport runnable in elemental B11 and a BN mixture, while keeping measurement, isotope transfer and compound assumptions visible. It does not claim an independently calibrated BN/alpha table or full fusion yield.

## Recovered numerical model inputs

Upstream: ir2-lab/libdedx, commit f20ddde3063bbad4f3528b11a279146707620df0, https://github.com/ir2-lab/libdedx/tree/f20ddde3063bbad4f3528b11a279146707620df0 . This is a different project from APTG/libdedx. Its author documentation identifies electronic-stopping tables for SRIM 1996 and SRIM 2013. SRIM96 tables derive from published code; SRIM13 tables derive from SR_module.exe output generated upstream. We recovered four generated C arrays plus their energy grid and extracted B/N target columns for proton/helium projectiles: eight tables, 121 energies each, 968 stopping values.

All eight tables were compiled from the recovered upstream C arrays and read through ctypes. The independent text extractor reproduces all 968 selected C float stopping values and 121 energy nodes exactly. It preserves binary32 round-trip values. UPSTREAM_LOCK pins source bytes; TABLE_LOCK pins exported tables. The original SR_module.exe and full SRIM transport simulation were NOT regenerated or run. This is replay of versioned calculated tables, not new measured stopping data.

The source grid is keV/u, not total projectile keV. Stopping is 1e-15 eV cm2 per target atom. Total incident energy is converted using the explicitly supplied approximate atomic mass of the projectile. The generator's SRIM13 source confirms multiplication by projectile mass when preparing total energies for SR_module. The model does not use those approximate atomic masses as event-generator rest-mass constants.

The upstream MIT notice is retained in UPSTREAM_LICENSE.txt. This does not assert new licensing rights over the original SRIM executable. Downloaded C sources and binaries are not bundled in this addition. Upstream software and source-file hashes are recoverable from UPSTREAM_LOCK.

## Electronic and nuclear stopping remain separate

Electronic stopping uses log-log interpolation of the source table with no extrapolation. Nuclear stopping uses the standard screened-collision ZBL mean formula. The default follows the SIMNRA 7.04 documentation's reduced-stopping coefficient 0.01321 and energy prefactor 32.53. A named Geant4 10.7.4 variant uses 0.01312 and 32.536, as found in that exact source version. The variation is recorded rather than silently conflated. NUCLEAR_METHODS.json identifies both primary sources. No Geant4 or SIMNRA executable was run, and no stochastic straggling was sampled.

Total stopping = electronic + nuclear, with both components and mass-stopping conversion returned explicitly. The atomic stopping unit is NOT mass stopping or stopping per BN formula unit. Energy loss of the incident particle is NOT automatically recoverable heat. Density is not needed when using an explicit atomic areal inventory.

## Material transfer and BN assumptions

Three explicit materials are available: B11, OVERLEY_B10_ENRICHED (95.96% B10 and 4.04% B11), and BN_B11_N14 (equimolar B11/N14). Electronic isotope transfer assumes equal-velocity elemental stopping per atom. Nuclear stopping uses each isotope's mass. The conversion to stopping per gram also uses the chosen isotope inventory. This is an explicit model of transfer, not a relabeling of the old measured curve as B11 data.

BN uses Bragg atomic-fraction additivity, Se(BN average atom) = [Se(B)+Se(N)]/2, multiplied by an explicitly supplied electronic correction factor. The nuclear terms are averaged separately. No BN measurement fixes that factor in this release. The nominal factor 1 means additive model; 0.8 and 1.2 are deliberately chosen sensitivities. They are not BN-specific confidence bounds. The SIMNRA author manual discusses order-10–20% departures in some compounds, particularly near maxima; that is not proof that this bracket covers every BN phase and energy. The upstream elemental nitrogen phase/default generation settings have not been independently reconstructed. hBN versus cBN, bonding, crystallographic orientation, porosity, temperature and irradiation evolution are not resolved.

The scenarios compare E_p=0.65 MeV or E_alpha=3 MeV at a fixed ASSUMED boron inventory of 1e18 atoms/cm2. Elemental B has 1e18 total atoms/cm2; equimolar BN has 2e18 total atoms/cm2. This avoids an accidental factor-of-two boron normalization error. Neither inventory is a proposed apparatus specification. The alpha calculation is a single-particle transport example, not a fusion birth spectrum or correlated three-alpha event.

## Historical measurement comparison, without fitting

The recovered 27-point Overley curve is imported with its previous artifact hash and original DOI 10.7907/XZP6-5P63. The model is evaluated for the source's actual enriched-boron composition. With zero fitted parameters:

| Electronic model + default ZBL | Mean fractional discrepancy | Maximum absolute fractional discrepancy |
| --- | ---: | ---: |
| SRIM96 table replay | -2.730% | 6.517% |
| SRIM13 table replay | -6.835% | 8.632% |

These are model-minus-digitized-measurement ratios, not uncertainty-standardized residuals. The source reports 4% total probable error; digitization has separate working allowances. We do not invent a complete covariance, convert probable error to Gaussian sigma or tune a normalization to manufacture agreement. SRIM may share ancestry with historical measurements, so this is NOT a grouped experimental holdout or independent validation. The model versions are retained separately and are not averaged into an asserted best curve.

## Runnable finite transport

The solver integrates reciprocal total stopping over a refined energy grid and inverts each piecewise-linear segment analytically. Nominal refinement is 16 subdivisions per source interval; the runner compares with 32 and requires <1e-6 MeV change. The maximum observed change across the sixteen scenarios is 1.774e-7 MeV. These are numerical tolerances, not physical accuracy claims.

The lower source grid is positive: about 1.008 keV for protons and 4.003 keV for alphas with the chosen mass parameters. If a particle would cross below that limit, output energy and stopped status become null with an explicit model-boundary result. No tail to zero energy or complete stopping range is invented. No scattering, straggling, target motion, hot-plasma stopping, laser-plasma coupling or acoustic gain is supplied.

This version deliberately does not export a full CSDA RangeTable to the earlier engine: that interface expects an absolute range to zero, which these bounded inputs do not establish. The model API is available for a later bounded-domain integration. The main Stellar Forge UI and all-shot runner are not modified by this sidecar release.

## Reproduce

Python >=3.11, standard library only for the bundled-table replay, comparison, transport and twelve tests:

```bash
python run_models.py --out receipts/NEW_RUN
python -m unittest -v test_models
```

To reacquire the pinned upstream inputs and reproduce extraction (network needed once):

```bash
python extract_tables.py --download --upstream upstream --out receipts/NEW_EXTRACTION --native-check
```

The optional native comparison requires a C compiler with shared-library support on Linux. Without --native-check the extractor uses the standard library and no compiler. Existing source files and output directories are not overwritten. The recorded native check used GCC 13.3.0. Receipts include exact source hashes, C-float verification, all 54 comparison rows, sixteen transport cases, source discrepancy summary, nuclear variants, tests, parameters and a preserved refinement failure. No RNG is used.

The first coarse refinement failed the same 1e-6 MeV gate for alpha transport in BN. Resolution was increased; the acceptance threshold was retained. FAILED_REFINEMENT001.json records the outcome. Final repeated calculations are byte-identical in the recorded environment.

## Scientific status and next integration

Original numerical alpha measurements remain unacquired. The model makes alpha/B11/BN sensitivity work executable while that evidence gap remains open. Next: compare to measured alpha energy-loss data and independently characterized B11/BN transmission, qualify compound corrections over energy, integrate bounded stopping results with the correlated event source and detector response, and test grouped experimental holdouts. Those steps precede apparatus calibration acceptance. All nonsuperseded physical modules remain in scope. Scientific freeze remains pending; no merge is requested.
