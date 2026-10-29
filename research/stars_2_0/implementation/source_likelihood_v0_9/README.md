# Stellar Forge Reference — source likelihood v0.9

This additive release makes the coherent v0.8 source usable in a conditional event likelihood and evaluates which ideal observables retain information about its raw mixing coefficient and relative phase. It uses the cited physical candidate unchanged. No experimental source fit, calibrated detector fold, net-energy prediction or acoustic gain is claimed.

## Calculation

For every phase-space proposal, retain four real basis terms: the two pure-wave intensities and the real/imaginary cross term, averaged over the five parent substates. For a basis kernel `(a,b,c,d)`, intensity is

`w = k*a + (1-k)*b + 2*sqrt(k*(1-k))*(c*cos(delta)-d*sin(delta))`.

Analytic derivatives include the derivative of total normalization. The conditional probability is `p_i=w_i/sum(w)`, and the categorical Fisher information per event is `sum_i (dp_i dp_i^T)/p_i`. This is a local model-information calculation in coordinates `(raw k, phase in radians)`. Condition numbers depend on coordinates. No apparatus noise, measurement covariance, model discrepancy or exposure is invented; these are not experimental uncertainty bounds.

`likelihood.py` provides coherent kernels, derivatives, conditional multinomial negative log likelihood, explicit response folding and basis transformations. It requires integer event counts. Missing counts raise an error; a genuine all-zero count vector contributes zero shape information. Unknown detector outcomes must not be filled with zeros. Positive counts in a zero-probability bin give infinite negative log likelihood. No optimizer or experimental fit has been run.

A supplied response matrix must be nonnegative, with columns summing to at most one. The caller explicitly chooses whether to append a missed-outcome bin. Conditioning on detected events renormalizes the retained distribution; it must not be confused with knowing the number of unobserved reactions. The API assumes a parameter-independent response. Real acceptance depending on unrepresented directions or parent alignment cannot be supplied as a guessed universal matrix. No detector response is silently selected.

## Information experiment

At0.675MeV proton LAB, compare: (1) each reaction's sorted triple of energy-fraction bins, (2) one uniformly randomly selected alpha from that reaction, (3) count-only collapse, and (4) a proposal-point upper diagnostic. The triple retains energy correlations; the single-alpha projection is an exact stochastic coarsening. All three alphas contribute to its marginal probabilities with weight1/3. They are not treated as three independent reaction events.

Each alpha energy is divided by the total CM kinetic energy and put into12 equal bins. Sorted bin triples define exclusive categories; no measured detector segmentation or resolution is asserted. The unbinned quantity uses the discrete integration proposals, not experimental events. The matrix differences `F_unbinned-F_exclusive` and `F_exclusive-F_random_alpha` must be positive semidefinite. Total counts carry zero conditional mixing information when source reaction normalization is separate; this does not assert a universal lack of rate sensitivity in other physical models.

The raw coefficient and phase use the v0.8 literature-informed evaluation point, not newly fitted values. Pure coefficient endpoints need another coordinate chart and are explicitly rejected by this derivative API. All earlier pure-wave controls remain available in v0.8.

Rescaling basis amplitudes by `(a,b)` requires `k'=(k/a²)/(k/a²+(1-k)/b²)`. This preserves every normalized probability. The test with scales2 and0.5 maps k0.76 to0.1652173913 while changing probabilities by less than1e-15. These arbitrary scales are an algebraic test, not physical input. A freely fitted coefficient can absorb constant normalization choices; it does not resolve energy-dependent phases or physical model inadequacy.

## Reproduction

Use the adjacent hash-pinned v0.8 and its prepared Michel CPC backend; follow its README for compiler/GSL and dependency setup. Python3.12.14, NumPy2.3.5 and SciPy1.17.0 were used.

```sh
cd research/stars_2_0/implementation/source_likelihood_v0_9
python -m unittest -v test_likelihood
python run_information.py --samples 8192 --seed 20261030 --bins 12 --out receipts/new_run
```

Run destinations must be new. Run001 uses8192 proposals, run002 uses8192 with an independent seed20261031, and run003 refines run001 to32768 proposals with the same seed. Seeds/grid sizes are numerical integration settings, not synthetic physical calibration parameters. See `receipts/INTEGRATION_COMPARISON.json` for finite-integration sensitivity. No convergence tolerance was retrofitted to manufacture acceptance. Tests use explicit algebraic counterexamples and count fixtures; those are not laboratory measurements.

`SOURCE_AUDIT.md` records this turn's primary-source checks and unsuccessful retrievals. `CALIBRATION_GATES.json` identifies exactly what is still required before fitting or promoting the model. No historical file is modified or deleted; this draft is stacked on PR30.
