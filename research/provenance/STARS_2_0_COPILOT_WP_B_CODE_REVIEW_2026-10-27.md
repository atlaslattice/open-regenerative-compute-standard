# Stars 2.0 — Copilot WP-B Independent Code Review (2026-10-27)

**Provenance:** Review supplied by user from Copilot. Original simulator: Gemini Argon. Verification notes: ChatGPT/Tidal Lantern. Atlas Lattice / ORCS. This is a review digest, not a replacement for the original transcript or an empirical validation.

## Assessment
Copilot considers WP-B a good exploratory software scaffold but *not* a validated numerical baseline. Its source audit and the direct code inspection identify:

1. Lab-to-CM energy conversion is **nonrelativistic**, though reasonable at these energies; correct the documentation.
2. The analytic cross-section is a **surrogate**, with assumed Breit–Wigner amplitudes and modifiers. Benchmark to evaluated data, including uncertainties.
3. The BN proton-stopping interpolation is **not demonstrably SRIM-calibrated**. Independent local execution gives S(75 keV)=90.40 keV/µm and S(1 MeV)=52.89 keV/µm, while a code comment claims ~92 and ~36 keV/µm respectively. Copilot's speculation about the direction of the 1 MeV difference was incorrect, but the calibration discrepancy is real.
4. The escape function integrates **both faces**, while the downstream collection estimate implicitly treats total escaping energy as accessible from one side. Separate front/rear energy and angle distributions.
5. Two mean alpha groups and a 0.65 power-law residual-energy function are approximations, not a correlated three-alpha transport solution.
6. The 8-condition design is a **bundled scenario matrix**: acoustic ON changes thickness, proton spectrum and conversion simultaneously; wave ON changes stopping and collection. It does not isolate independent main effects.
7. A single all-system sham is not equivalent to acoustic-only, spin-only and wave-only matched shams.
8. The electrical/thermal ledger credits escaping proton kinetic energy and non-collected fusion-product energy to recoverable heat. Require explicit energy-conservation terms at each boundary.
9. G3-A converter recovery values are **hardcoded assumptions**, so labels such as PASS are conditional arithmetic outcomes and not demonstrated energetic gain.
10. The 5 µm result is a **sampled optimum**, not an exact optimum; run finer sweeps and uncertainties with explicit objective functions.

## Reproduced Gemini code outputs
CM mass fraction 0.9161569824. Five-µm BN scenario: 3,231,094 alpha particles born, 2,294,336 escaped, escaping fraction 0.71008 and escaped energy 0.745632 µJ. C1 G3-A scenario: 100 mJ input, 54.5 mJ assumed load output and 4.2 mJ assumed overhead produce a *conditional* +50.3 mJ. None of these values has independent experimental calibration.

## Actionable WP-B v0.2 checklist
- Preserve original Gemini Argon script and CSVs unchanged in an explicitly labeled baseline.
- Replace cross-section and stopping surrogates with traceable datasets; unit and range regression tests.
- Separate front/back alpha escape energy, charged-particle acceptance and electrode load output.
- Implement multi-boundary energy conservation with escaped protons and thermal sinks explicitly tracked.
- Decouple target thickness, acoustic modulation, beam spectrum, polarization and wave-drive settings.
- Audit Monte Carlo/quadrature convergence and propagate uncertainty before interpreting any thickness optimum.
- Label hardcoded C1/C2/C3 scenarios *assumption ledgers*, not experimentally passing or failing technologies.

**Next order:** Repair and validate WP-B first; then tackle WP-D converter phase-space acceptance and WP-C preregistered target experiments. Keep DeepSeek, Gemini Argon and Copilot source contributions distinguishable.
