# Beyond Q v1.1.1 — Benchmark and resilience verification

Research direction: Dave Sheldon / Atlas Lattice. GPT-6 computational work;
DeepSeek and Gemini Argon contributions retained from v1.1. No institutional
endorsement or experimental validation. G1–G5 remain physically OPEN.

## External computational benchmark

Independent Python implementation of the 11-stock Meschini equations in INL
TMAP8 reproduces all 115 rows of its reduced-runtime gold
fixture to a maximum stock error of 4.47e-09 kg.
This is VERIFIED-DERIVED computational reproduction, not physical validation.
Source: Meschini et al., Nuclear Fusion 63 (2023) 126005,
doi:10.1088/1741-4326/acf3fc, via pinned TMAP8 input and gold CSV at commit
7dfbc71378fb243afba23db80a8284cd4b6429a4.

Matching the reference required backward Euler at the published timestamps,
with source forcing evaluated at the preceding accepted step. The upstream
test overrides initial_refinement_time to 17000 seconds; after that it uses
averaged 75% activity. A matrix-exponential continuous-time oracle splits at
each true source jump. Maximum difference between the reproduced gold and
continuous oracle is 0.0136331 kg:
agreement with a solver's recorded output does not remove discretization bias.
At t=0 upstream total_tritium is reported as zero despite 1.14 kg in storage;
we compare the 11 actual stocks, not that initial diagnostic artifact.

This literature fixture uses its own published burn rate, half-life, startup
stock and schedule; it does not replace our reference power configuration.
TMAP8/Matlab executables were not run here. The direct MATLAB CSV is not the
comparison target; this result reproduces INL's computational reference.

## Mapping to the dual-reactor model

The seven-stock Beyond Q model cannot be expected to match the 11-stock case
by changing scalars alone: it lumps cleanup/ISS, omits wall/divertor/HX and
detritiation recovery, uses different A/B sources and fuel-limited B operation.
The published fixture prescribes burn and terminates on exhausted storage.
We therefore reproduce the full fixture separately and retain Beyond Q as a
screening model. Benchmark success does not validate its lumping assumptions.

## Resilience scenarios — POTENTIAL-DERIVED

B remains 1130 MW D-T fusion; A hypothetical 20 MW primary D-D. Horizon 180
days; all requested on except explicit scenario windows. Initial A stock zero;
initial B stock 10 kg. Extraction/processing states are independent of reactor
states. With a failed processor, unburned fuel accumulates in processing,
cannot return to storage, and actual burn and breeding fall when feed runs out.

| Scenario | Final stock kg-T | Unmet B fusion GWh | Conditional startup bracket kg-T |
|---|---:|---:|---:|
| baseline | 12.0482 | 0.0000 | 1.0979–1.0981 |
| extractor_7d | 12.0478 | 0.0000 | 2.0927–2.0929 |
| processor_7d | 12.0346 | 119.0629 | 25.3075–25.3077 |
| processor_30d | 11.9637 | 741.0458 | 105.4428–105.4430 |
| A_off_60d | 11.4639 | 0.0000 | 1.0979–1.0981 |
| B_off_40d | 11.9230 | 0.0000 | 1.0979–1.0981 |
| common_off_30d | 11.6639 | 0.0000 | 1.0979–1.0981 |

Startup brackets use bisection on initial B storage, with a 200 kg upper
search bound, tolerance 1e-8 kg cumulative unmet burn, and 20 iterations.
They are finite-horizon fuel-availability bounds under assumed parameters,
not safe/qualified startup inventories or licensing reserves. No positive
regulatory reserve floor is imposed. Track substep minimum B storage as well
as daily final stocks; bisection width is not physical uncertainty.

## Error budget

Numerical: processor-7-day startup upper bracket changes from
25.578117 kg at step .25 day to
25.127792 kg at .03125 day. See numerical_budget.csv
for all steps, unmet burn and final inventory. Exact single-compartment
updates still have coupling/scheduling discretization error.

Parameter: parameter_budget.csv varies TBR_B, processing residence rate and
pass burn fraction independently at fixed outage windows. These are assumed
input sensitivities, not statistical confidence intervals.

Structure: extraction_comparison.csv contrasts continuous well-mixed turnover
k=epsilon/tau with periodic discrete-pass removal at the same source/loop and
loss rate. Discrete stock has separate pre-pass, post-pass and cycle-mean
values; a continuous steady stock cannot be compared only to its post-pass
minimum. This is a standalone extraction module comparison, not a full
dual-reactor discrete-loop prediction. Full delay/age-structured coupling,
temperature/speciation and empirically calibrated failures remain open.

Independent measured parameter covariance, model discrepancy, transport,
startup qualification and wall-plug energy closure remain missing. No usable
surplus or physical self-sufficiency follows from these tests.
