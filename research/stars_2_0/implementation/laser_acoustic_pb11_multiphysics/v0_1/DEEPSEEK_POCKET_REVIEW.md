# DeepSeek pocket response — integration review v0.1

2026-10-30. Attributed digest of the user-supplied DeepSeek response and GPTWork
technical assessment. This is new candidate design work, not recovery of the
original pocket. The exact historical specifications remain unresolved.

## Accepted additions

Retain three named candidates: P1 porous boron-bearing ceramic scaffold with a
separately described loaded phase; P2 deposited boron-bearing layer on printed
support; P3 minimally supported ceramic membrane. A loose-particle-bed pocket
remains a fourth unresolved structural possibility, not silently equated to P1.
These are candidate target IDs, not apparatus A/B/C identities. Candidate fields
remain null until a source or explicitly chosen exploratory parameter is supplied.

Keep actual grain/contact physics conditional on material form; measure damping,
impedance, preparation memory, prepulse ejection and repeated-shot target change.
Preserve separate born, escaped, accepted and detected alpha ledgers. Use static
source-controlled comparisons first, then end-to-end source-changing comparisons.

## Required corrections before numerical adoption

| Supplied claim | Integration decision |
|---|---|
| Porosity increases proton path without substantially increasing stopping | Not established. Lower solid fraction changes nuclear target column and stopping together; tortuosity/scattering can increase both and alter escape. Compare full energy-dependent transport at explicitly matched inventory/column. |
| Enrichment increases cross section | Enrichment changes B11 population and mixture reaction rates/stopping, not the intrinsic p+B11 cross section for a fixed state and collision energy. |
| 2–10 µm, 15–40% porosity, 60–85% density, 20 kHz–2 MHz | Uncited proposed search ranges here, not calibrated defaults or constraints recovered from the apparatus. Porosity and relative density are complementary for an otherwise fixed skeleton, not independent knobs. |
| 0.7 J/cm2 laser threshold transferred from monolayer to bulk/coating | Source/conditions unresolved. Require wavelength, pulse duration, fluence definition, environment, sample geometry and damage criterion. No monotonic bulk/coating improvement presumed. |
| Standing surface waves suppress prepulse roughening | Hypothesis only; may instead seed modulation, instability or ejection. Compare phase/timing and surface evolution with sham controls. |
| Acoustic streaming improves cooling | Requires an actual fluid/coupled heat path. Do not assume streaming in vacuum or a solid ceramic; include damping heat and thermal drift. |
| Acoustic waves cannot propagate in plasma | Incorrect as a blanket statement. Plasma supports ion-acoustic and other modes; this does not establish coupling of an external mechanical actuator to the expanding target plasma. |
| Sustained forcing must be restricted to before plasma formation | Too categorical. Ordinary solid elastic response changes as material ionizes; surviving supports, un-ionized fuel and the liquid pitcher can remain mechanically driven. Match domains/time scales and track coupling rather than assert zero or automatic transfer. |
| Flash-X supplies granular/elastic pocket mechanics | Not established by the inspected access page; require actual constitutive/contact modules and benchmarks. Multiphase hydrodynamics is not automatically granular friction or solid elasticity. |
| Geant4 guarantees precise stopping | A candidate transport tool, not a precision guarantee; qualify material, projectile/energy range, selected models and experimental comparison. |
| 2D WarpX compares all P1/P2/P3 and escaping spectra | Only after appropriate solid/compound stopping, target geometry, ionization and product transport are qualified. 2D slab/cylindrical weighting cannot silently represent a 3D granular pocket. Native pB reactions alone are insufficient. |
| At least 100 shots and a 10% effect target | Do not freeze. Use power/precision analysis with measured variance, clustering, failures and missingness. |
| Bayesian Poisson plus Bayes factor is the statistical solution | Conditional option only. Count data may need exposure offsets, efficiency, overdispersion, zero inflation and shared systematics; success is binomial/hierarchical and timing is a separate observable. Bayes factors require explicit priors and are not mandatory. |
| Backward alpha obstruction proves only forward value | Not enough information. Mechanical reliability, total yield, recoverable heat, accessibility and lifecycle cost may also matter; quantify rather than rule out. |

The existing six-cell comparison is retained, rather than replacing it with an
ambiguous four-group REFERENCE/OFF/SHAM/ON design. Reference is a geometry factor;
OFF/SHAM/ON is a treatment factor. No unsupported effect coefficient is inserted.
Reliability remains a contributor to total fusion output, not an unrelated goal.

## Areal-density arithmetic check — illustrative, not a target prescription

For uniform hBN with approximate molar mass 24.82 g/mol,
N11/cm2 = rho[g/cm3] * thickness[um] * 1e-4 * N_A * f11 / 24.82.
Using the response's own proposed input endpoints gives about:
- rho 2.1, thickness 2 µm, f11 .801: 8.16e18 atoms/cm2;
- rho 2.2, thickness 10 µm, f11 .801: 4.28e19 atoms/cm2;
- rho 2.2, thickness 10 µm, f11 .99: 5.28e19 atoms/cm2.
Thus the quoted 2–8e19 range is not the direct full result of those hBN endpoints.
Porosity lowers values at fixed geometric thickness if it reduces bulk density.
Actual isotope-dependent molar masses and B4C/elemental-B composition require
separate calculations. This arithmetic neither validates the endpoint densities
nor justifies adopting them as apparatus measurements.

Primary code cross-check for plasma acoustic terminology: Smilei's
[thermal-expansion benchmark](https://github.com/SmileiPIC/Smilei/blob/61aa917e851e89c64a0a2c17ca869fa71128422d/benchmarks/tst1d_03_thermal_expansion.py)
explicitly uses an ion-acoustic speed. No execution or physical coupling validation
of that benchmark is claimed here.

## New useful falsifiable hypothesis

A pocket may retain a prepared packing state after vibration decays, whereas a
coherently oscillating surface can depend on laser phase at firing. Measure both
packing/geometry persistence and displacement phase versus preparation-to-shot
delay. Include phase-locked, deliberately randomized-phase and sham conditions
only after the actual response is characterized. This is a proposed mechanism
separation experiment, not evidence that either mechanism occurs in this target.
