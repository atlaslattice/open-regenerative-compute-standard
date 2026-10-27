# Stars 2.0 — DeepSeek G0-B three-target substrate comparison protocol
**2026-10-27 | Review integration for v0.9 | Experimental design, not measured results**
**Provenance:** Derived from user-supplied DeepSeek follow-up (not verbatim), with ChatGPT/Tidal Lantern interface and falsification annotations.

## What is already integrated and what remains
DeepSeek's six original cross-domain candidates are covered in [the source-checked engineering audit](DEEPSEEK_V08_CROSS_DOMAIN_ENGINEERING_AUDIT_2026-10-27.md): diamond/SiC G0-D, hybrid target fabrication G0-F, tungsten G3-M, polarized protons/boron G2-P, Bayesian acoustic G1-ML, and trace ¹⁰B activation G0-I. **These are reviewed proposals, not all runnable model components.** The [earlier hybrid fabrication follow-up](DEEPSEEK_V08_HYBRID_BORON_TARGET_FABRICATION_FOLLOWUP_2026-10-27.md) separated water pitcher, boron reaction film and structural support.

## Concrete comparison: G0-B / G0-F

### A — Reference: free-standing/minimally supported B-rich foil
Known ¹¹B enrichment, areal B-11 atom density, thickness distribution, chemistry and porosity, fixed proton source, characterized front/rear detection. If a submicron Si₃N₄ window or mesh is used, **that support must still be included** in the full stopping and detection model: it is not truly free-standing.

### B — Dense-substrate control
Boron-bearing film at **matched B-11 areal atomic density** deposited on a characterized thick Si/Al substrate (DeepSeek example 500 µm silicon). In the simplest full-coverage geometry MeV alphas directed into this substrate will stop before exiting; compute actual stopping and straggling, and measure the surviving output. Incident protons may undergo substrate stopping/backscattering too. A substrate with identical B-film thickness is not equivalent to a standalone foil. Substrate thermomechanical response and pre-shot/shot-time state must be instrumented rather than assumed.

### C — Printed holder + deposited film
Boron-bearing film in an additive-manufactured/DISH-derived **frame, membrane aperture or sparse mesh**. Compare on the same B-11 areal atom budget, proton and optical geometry, film quality, layer composition, target alignment, and detection acceptance. Holder claims are testable: can the support avoid obstructing the alpha-exit cone and improve reproducibility while maintaining integrity? DISH photopolymer printing does not itself produce dense sintered BN at ~5 µm.

### Optional D — graded BN
Only explore after A-C: graded-density/porous ceramic geometries at matched total B-11 atom budget, with 3D geometry and transport modeling; no assumption that nominal micron thickness alone determines nuclear yield or escape.

## Crucial geometry correction
Use beam-frame definitions:
- **incident / upstream** = side proton beam first encounters,
- **transmission / downstream** = opposite side,
- **substrate-facing** = direction blocked by backing layer,
- **vacuum-facing** = exposed direction.

Do not equate substrate-facing with downstream without knowing coating order. For substrate-on-downstream experiments, proton transport into the backing may contaminate diagnostics and change production/deposited energy. For reverse orientation, protons must cross the backing *before reaching boron* and this is a distinct invalid source equivalence without beam measurement. Prescribe a layer-stack diagram in both orientations and keep identical detector positions relative to beam.

## Measurements and scientific acceptance criteria
- Quantify film composition, ¹¹B isotope fraction, boron-11 atoms/cm², morphology, density/porosity, chemistry, supporting substrate thickness/composition and active aperture.
- Independently measure proton incident phase space, transmitted/scattered proton distribution, particle-ID alpha energy and angular response on both sides, background controls, isotope/purity uncertainty.
- Freeze proton/cross-section/stopping/detector inputs before blind prediction; use EXFOR-identified nuclear data and source-qualified stopping.
- Blinded primary endpoint: source-normalized **detector-corrected escaping alpha energy** per incident proton and B-11 areal atom, for both hemispheres; test whether one fixed layer-resolved model predicts A/B/C without re-fitting per sample.
- Secondary: spectra, escaping-alpha counts, shot-to-shot jitter, target breakage/debris, supports' thermal robustness, assembly alignment and per-shot cost.
- Predefine tolerances from instrument calibration; not an invented percent in this planning note. Include no-beam control, support-only beam control, and reference proton beam calibration runs. Replicate fabrication batches.
- Evaluate electrostatic collector compatibility separately; measured alpha escape does not imply captured alpha or DC load output.

## Decision outcomes: conditional, not proof of one single cause
- If A outperforms B and C: investigate substrate attenuation **among other differences** (film microstructure, detector obstruction, beam-source changes), rather than declaring attenuation the sole cause.
- If C approaches A for escape and has better repeatability: support geometry may be valuable and merits durability and multi-shot tests.
- If C matches B or fails: test whether supports obstruct downstream alpha cone or alter target transport, then revise fabrication architecture.
- If an independently fixed transport model cannot predict A/B/C and both exit hemispheres within preregistered uncertainties, G0-B/G0-F calibration fails. Do not 'optimize' a post hoc thickness to repair it.

## Interaction with other cross-domain lanes
- G0-D detector work (diamond/SiC + silicon telescope/TPS + CR-39 controls) supplies response and source confusion calibration.
- G3-M tungsten collector materials should only be tested after transport and accepted plume measurements.
- G2-P polarization remains an independent no-presumed-gain test.
- G1-ML constrained Bayesian acoustic tuning starts after fixed, randomized OFF/SHAM/ON reference phase.
- G0-I proton-capture isotope conversion is a trace activation diagnostic, not an economically meaningful enrichment mechanism under present assumptions.

## Scientific verdict
The proposal is a **reproducible causal comparison of foil geometry and substrates**, with a decisive failure rule. It separates nuclear reaction-layer transport, holder fabrication, proton pitcher behavior and collector electricity. Neither a favorable few-micron thickness nor net fusion electric gain has yet been verified.
