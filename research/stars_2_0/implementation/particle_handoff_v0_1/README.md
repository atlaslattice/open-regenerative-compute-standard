# Stellar Forge — particle and energy handoff v0.1

2026-10-30. First executable coupling layer following PR43's A/B/C clarification. Append-only; historical code, results and apparatus identities remain unchanged. This release is a **conditional interface benchmark**, not a complete A, B or C apparatus simulation, recovered full-hybrid execution or net-power prediction.

## Implemented

- Weighted proton packets retain source identity, LAB kinetic energy, direction, source position/time tags and evidence. Fractional weights represent expected populations, not observed reaction counts or independently sampled physical shots.
- A prescribed sequence of cold elemental B11 slabs updates energy and survival through each depth cell using the existing SRIM13 electronic/ZBL nuclear stopping model and typed publication-derived event cross sections.
- Reacted protons are consumed once. Later stages see only survivors at their degraded energies. Target B11 consumption is recorded by physical instance, and inconsistent target inventories or excessive depletion reject the dilute-target approximation.
- Explicit external work and an analytic adiabatic mirror boundary share the same primary-particle energy ledger. The mirror uses each packet's pitch direction; it does not re-isotropize survivors on every visit.
- All supplied attempts remain present. Missing source outcomes are distinct from known zero source. Unknown physical-success outcomes, recovery and facility power remain null.

The existing rate and stopping code is imported without modification. DEPENDENCY_LOCK.json pins the exact tables and source bytes. The event table's observable is `PUBLICATION_MODEL_EXTRAPOLATED_FUSION_EVENT_CROSS_SECTION`, not detected-alpha production. The nominal reaction Q is derived from the earlier MASS_SOURCE.json, rather than replacing the historical mass convention. Source mass uncertainties, stopping uncertainty and nuclear-model uncertainty are not newly propagated.

## Interface and conservation

For each reaction-bearing cell, first transport all incident weight to the cell midpoint, consume the conditional reacted weight there, then transport only survivors to the cell exit. Birth-alpha **total kinetic energy** includes the reacted proton's local kinetic energy plus nuclear Q. It is not Q alone and is not three invented monoenergetic alphas.

\[
N_{p,\mathrm{source}}=N_{\mathrm{reacted}}+N_{p,\mathrm{escaped}}+N_{p,\mathrm{remaining}},\quad
N_{B11,\mathrm{consumed}}=N_{\mathrm{reacted}},\quad
N_{\alpha,\mathrm{born}}=3N_{\mathrm{reacted}}.
\]

\[
K_{p,\mathrm{source}}+Q_{\mathrm{nuclear}}+W_{\mathrm{external}}
=K_{\alpha,\mathrm{birth}}+E_{\mathrm{material\ transfer}}
+K_{p,\mathrm{escaped}}+K_{p,\mathrm{remaining}}.
\]

All ledger terms are weighted MeV, not MeV per particle; source input energies and field-work prescriptions are MeV per proton. One MeV equals 1.602176634×10⁻¹³ J. Material transfer is not automatically recoverable heat. Negative external work is not automatically electricity at load. Facility wall input is distinct from kinetic work on particles; wall input alone cannot determine net output without a conversion/collector model.

Repeated visits require unique visit IDs. Reusing a target physical-instance ID conserves its B11 budget **within an attempt**; repeated targets cannot change their material, column or inventory silently. The current runner explicitly assumes a fresh target each attempt. Target replacement, replenishment, consumed energy and downtime are not free: their apparatus inputs remain missing, and net electrical output remains null. An evolving or persistently reused target needs a separately versioned adapter.

## Scope of the mirror boundary

For mirror ratio R, midplane kinetic energy E and physical midplane-to-throat potential-energy rise V, the adiabatic loss boundary is `cos²(pitch) > 1 − 1/R + V/(R E)`. This is the conditional throat interpretation examined in PR42, based on Kolmes, Ochs & Fisch (2024), DOI [10.1017/S0022377824000205](https://doi.org/10.1017/S0022377824000205), Eqs 2.3–2.4. It is not a recovered PRISM field map or a universal centrifugal potential.

Escaped protons leave at the throat with kinetic energy E−V; the ledger records external field work −V per escaped proton. Reflected protons return to the midplane with unchanged kinetic energy and reversed axial direction. Near-separatrix transit is unresolved and rejected. This idealized endpoint classifier assumes adiabatic motion and a compatible barrier profile; it does not calculate finite orbits, flight time, collisions, instability or capture from a laser source. Both escape and reflection cases are tested.

## Runnable cases and results

Use the full stacked repository branch and Python 3.12.14 with NumPy 2.3.5. No GSL or coherent-decay backend is needed for this layer.

```bash
cd research/stars_2_0/implementation/particle_handoff_v0_1
python -m unittest -v test_handoff
python run.py examples/C_conditional_reference.json --out /tmp/forge-handoff-001
python verify_release.py --out /tmp/forge-handoff-verification-001
```

Output directories must be new. The runner stores exact input bytes, stage records, result hashes, code/dependency identities and environment. The examples originate from the earlier **assumed** v0.10 verification inputs: 0.675 MeV LAB protons, 10¹⁸ B11 atoms/cm² and three attempts containing 10,000, zero and 20,000 protons. Beam area, target reset, cell discretization and source tags are also declared verification assumptions. These are not specifications of the installed original STARS apparatus.

The one-slab example gives approximately **0.0398257582 expected reactions** across those three attempts. The same-depth-grid independent earlier integrator agrees. Two slabs sharing the **same total boron column** give approximately 0.0398257585, a relative difference of 6.84×10⁻⁹ due to numerical discretization. That is a numerical equivalence test, not a measured two-catcher benefit. The reaction-off control gives zero nuclear births while retaining stopping transfer. Missing source data block the all-attempt total. A and C full apparatus profiles retain explicit unresolved inputs and no performance value.

32 regression tests cover particle/energy closure, nuclear-observable semantics, same-column stage splitting, survivor handoff, mirror pitch/barrier conventions, signed field work, target identity/depletion, source frames and units, model-domain bounds and all-attempt missingness. The complete verification harness also reruns the reference and compares result bytes. An isolated minimal repository-layout replay, with the 14 pinned neighboring dependency files and the existing Python/NumPy environment, passes all 32 tests and reproduces the same reference result hash; this is not a clean OS installation. Conservation tolerances and exact-zero numerical residuals concern arithmetic conditional on supplied models, not physical measurement precision.

## Boundaries that remain open

**Geometry and timing:** the stage route is prescribed. Position/time values are carried source tags explicitly marked `SOURCE_TAGS_NOT_PROPAGATED`; they are not predicted current coordinates. No aperture, finite lateral foil, injection acceptance, spatial trajectory, recirculation time or jitter propagation is solved. Areal path through the ideal slab is normal column divided by the absolute direction cosine; grazing paths requiring finite lateral geometry are rejected. Stopping is deterministic CSDA with no scattering or straggling. No claim of full momentum conservation is made for aggregate alpha output; correlated three-alpha four-vectors remain a separate existing source adapter to connect.

**Nuclear domain:** the imported event kernel excludes the narrow low-energy resonance below 0.22 MeV. It is not applied to ENN's reported 162–200 keV population. The stopping/kernel combination also cannot accept a 53 MeV proton merely because a published hollow-sphere calculation reports that cutoff. The full source distribution, applicable reaction channels, frames and qualified kernels remain necessary. Neither source headline is converted into a spectrum or a gain factor.

**Material and energy recovery:** only cold elemental B11 is connected. The model is not measured material-specific stopping and is not transferred to BN, B10-enriched targets, compounds or hot plasma. Alpha outputs are birth count and total kinetic energy; correlated spectra, alpha escape, secondary reactions, collector acceptance, alpha channeling, heat conversion and electrical recovery are not implemented here. No double credit from an unavailable recovery module is introduced.

**Architecture:** A remains hollow sphere + PRISM + the confirmed ENN source/coupling research. C retains the original STARS inventory, and B combines them. The example labels identify the C family and explicitly say `NOT_APPARATUS`; they do not pin or reproduce the complete original installed configuration. No new source is inserted into C, and acoustics is not silently installed in A. Existing modules remain outside the scope of this interface run rather than being removed or assigned calibrated zero effects.

## Next adapter

Connect actual source-phase-space records and finite geometry/field transport, then introduce a reaction kernel covering the selected source regime. Couple the existing correlated-event generator to the local weighted reaction cells within its declared energy/state domain. Follow with alpha transport/recovery and acoustic readiness/firing/timing changes, retaining all-attempt energy and time costs. Assemble the B integration only with explicit shared-field, target-state and hardware reconciliation. These additions need new versions and must preserve this reference and its null cases.
