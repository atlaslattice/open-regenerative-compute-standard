# Gemini Argon WP-B v0.2 — Preliminary Independent Code Audit
**2026-10-27 | Atlas Lattice / ORCS | Review: ChatGPT / Tidal Lantern**
**Provenance:** code displayed in user's message; Gemini Argon results report separately archived verbatim. **Do not conflate this review with an executed test suite**: the full revised script has not yet been received as a standalone machine-readable file in the workspace and has not been rerun independently. The revised source should be archived separately and reproduced before acceptance.

## Strong improvements evident in supplied source
- Proton laboratory-to-center-of-mass relation correctly labeled nonrelativistic.
- Explicit front/back alpha escape counts and energy flows rather than a single total escape fraction.
- Reacted proton depletion and separation of unreacted outgoing protons from target-deposited heat.
- Fixed-thickness acoustic/spin/wave scenario contrasts with separately labeled sham simulations.
- Multi-boundary energy accounting and programmatic assertions.
- Simultaneous sensitivity sweeps for front-only, rear-only and dual-collector objectives; v0.1 stopping retained as alternate for comparison.

## Critical review findings
1. **Calibration claims are not established.** The new proton stopping function is a newly parameterized harmonic surrogate. Numerical spot checks confirm that its coefficients return **93.73 keV/µm at 75 keV, 41.99 at 736.8 keV, 35.76 at 1 MeV and 23.84 at 2 MeV**, but matching declared anchor numbers is not evidence that those are independent ICRU/SRIM-validated boron-nitride values. No provenance CSV, fitting residuals, range-energy benchmarks or uncertainty band accompanies the supplied text. Do not describe it as validated or 'fixed' until checked against underlying data.
2. **Energy closure is necessary, not sufficient.** The proton, alpha and converter identities are algebraically constructed to balance. Their assertions catch bookkeeping and programming errors but do not validate the source spectra, cross sections, stopping powers, angular distributions or converter efficiencies. At small values, tests with rel_tol only may need explicit absolute tolerances.
3. **Converter is not yet acceptance-weighted phase-space integration.** Function `evaluate_multistage_electrostatic_converter` accepts only aggregate rear/front alpha energies and a mean rear alpha energy (unused). It applies fixed scalar front/rear acceptance and a stage-efficiency formula, plus assumed grid/secondary-electron/space-charge losses. No actual `A(E,theta)` or `eta_DEC(E,theta)` integration, Child–Langmuir solution, pulsed current model or angle-dependent phase space is implemented, despite the description.
4. **Acoustic model remains hypothetical.** The 0.85 ripple response, 0.22 sheath factor, ~715 keV spectral bump and laser-to-proton gains are assumed phenomenological coefficients, not measured acoustically prepared pitcher response. Calling it 'physics based' must not suggest independent calibration to specific experiments.
5. **The cross section remains a phenomenological surrogate.** It is still a sum of modified Breit–Wigner and baseline terms with empirical caps and a `1+0.48P²` spin boost. No interpolated EXFOR or evaluated differential/total dataset was installed.
6. **Alpha stopping and correlations remain simplified.** Two fixed representative energy groups, a constant residual-energy exponent 0.65 and isotropic individual emission do not implement energy-dependent helium stopping tables or correlated three-body decay.
7. **Fixed thickness improves the factorial design but does not guarantee orthogonality of the physical mechanisms.** Acoustic ON changes proton-production spectrum and efficiency by assumption (could be a physical mediator); wave ON changes proton stopping; spin interactions are prescribed. This is a hypothesis-driven simulation factorial, not experimentally verified independent causal effects.
8. **Potential low-energy stopping artifact:** protons with residual energy <=10 keV are assigned to target deposition at the end of the simulated slab, including particles that could simply exit its rear at low energy. Verify physical stopping versus numerical threshold termination.
9. **No quantified source/collector timing, space-charge, charge exchange, lateral leakage, electrical breakdown or measured beam current**, so detailed WP-D feasibility cannot be inferred.
10. **Unverified runtime:** Gemini's claim '3/3 unit tests pass' is a *reported result* until we independently run its exact code. Prefer tests against independent reference arrays, not only internal consistency.

## Highest-value next actions
- Obtain and preserve the *complete standalone revised Python file*, plus generated CSVs and plot as original Gemini Argon artifacts, **without overwriting v0.1**.
- Independently execute tests and replicate the 5, 6 and 7 µm maxima and the comparison of 4.5 versus 5 µm rear energy.
- Acquire licensed/tabulated proton and alpha stopping in the actual BN material, proton–¹¹B cross-section tables and uncertainty bands. ICRU 49 gives proton and alpha stopping methods; it is not by itself a BN-specific imported numerical table.
- Replace scalar converter acceptance by per-energy/per-angle distributions; benchmark against real charged-particle tests.
- Preserve a strict status hierarchy: **reported by Gemini** → **reproduced from its code** → **cross-checked against reference data** → **supported by experiments**.

## Additional contextual sources
- NePTUN repeatable pitcher and depth-sensitive BN alphas: https://arxiv.org/abs/2609.33483 .
- ENN low-parameter direct-conversion unit: https://doi.org/10.1088/2058-6272/ae445a .
- Prior paper and provenance manifest: [Stars 2.0 artifact manifest](../ARTIFACT_MANIFEST_2026-10-27.md).

**Bottom line:** Substantial accounting and organization progress. Do not treat the new 'calibrated' label, source/collector scalar formulas or reported tests as numerical validation of a real fusion system.
