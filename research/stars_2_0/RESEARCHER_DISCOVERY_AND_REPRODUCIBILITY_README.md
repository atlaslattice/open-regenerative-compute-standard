# STARS 2.0 — Researcher Discovery, Source Registry & Reproducibility Gateway

**Research category:** open computational / experimental nuclear physics methods and engineering research program (candidate)  
**Release status:** proposal + source-ingested primary cross-section data + partial model audit; not a calibrated end-to-end simulator or validated fusion energy system  
**Updated:** 2026-10-27  
**Project:** Atlas Lattice / Open Regenerative Compute Standard (ORCS)

## Search-friendly abstract

STARS 2.0 is an open, provenance-preserving, falsification-first research framework for laser-driven proton–boron-11 (p–11B) reactions, aneutronic-fusion particle production, three-alpha event kinematics, thin catcher targets, alpha-particle escape spectroscopy, charged-particle transport, laser-plasma diagnostics, acoustic target preparation/control, detector-response forward modeling, and direct alpha energy recovery. It proposes blinded accelerator-beam calibration (G0-B), four-arm randomized acoustic controls (REFERENCE/OFF/SHAM/ON), source-specific uncertainties, uncertainty propagation, and wall-plug energy accounting. The framework is intended to be **adaptable to other reactions and experimental geometries** using explicit interfaces, not merely one p–11B concept. It is not a demonstrated net-electric fusion technology.

## Indexed keywords and synonyms

**Nuclear reactions:** proton boron-11; p-B11; p–11B; ^11B(p,alpha)^8Be; B-11(p,a)Be-8; three alpha; triple alpha exit channel (NOT the stellar 3α carbon synthesis process); aneutronic fusion; nuclear resonance; 675 keV laboratory proton resonance; center-of-mass energy; EXFOR; nuclear reaction cross section; alpha-particle yield cross section; reaction multiplicity; angular distributions; Legendre coefficients; branch-specific alpha spectra; ^12C excited states; ^8Be sequential breakup; correlated 3-body kinematics.

**Particle transport and detectors:** boron nitride BN; hBN; B4C; elemental boron thin-film catcher; areal ^11B density; proton stopping power; alpha stopping; CSDA; SRIM/TRIM; FLUKA; straggling; MCNP/Geant4 comparators (future candidates, not implemented); silicon delta-E E telescope; silicon surface barrier detector; diamond detector; SiC detector; CR-39; Thomson parabola; proton transmission; energy-angle distribution; EMP; high-intensity laser diagnostics; particle-identification; forward response.

**Experimental design and reproducibility:** G0-B; blinded prediction; preregistration draft; source provenance; FAIR data; open science; reproducible computational physics; uncertainty propagation; falsification; Bayesian Poisson background; Bayes factor; randomized sham control; negative control; held-out validation; machine-readable metadata; source hashes; GitHub provenance; research ancestry; negative results; causal effect; detector calibration; alpha yield.

**Engineering:** water-leaf laser pitcher; TNSA proton source; boron-rich catcher; thin-film sputter deposition; support attenuation; laser-pulse contrast; acoustic control; vibroacoustics; shot-to-shot jitter; target survivability; repetitively pulsed targets; direct electrostatic alpha conversion; ion Bernstein waves; inductive charged-particle pickup; collector efficiency; wall-plug efficiency; beam-to-load ledger; quality-adjusted throughput.

**Mathematics/research leads (NOT established direct connections):** harmonic analysis; local smoothing conjecture; dispersive PDEs; wave focusing; Bayesian optimization; constructive Yang-Mills; QCD theory watch.

## Recommended entrypoints

1. [v0.9 integrated pre-simulation white paper](whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md).
2. [Current artifact and provenance ledger](ARTIFACT_MANIFEST_2026-10-27.md).
3. [G0-B blinded beam and alpha escape draft experimental protocol](protocols/G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md) and [lockfile validator](protocols/g0_b_lock/README.md).
4. [Original IAEA EXFOR C2973 dataset interpretation and DeepSeek design-gate audit](reviews/EXFOR_C2973_PRIMARY_DATA_RECOVERY_AND_DEEPSEEK_FINAL_SAFEGUARDS_2026-10-27.md).
5. [Source-normalized C2973002 41-row original EXFOR master data](wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv) with the **critical alpha-count interpretation note immediately below**.
6. [Gemini Argon WP-B v0.3 independent partial-code audit](reviews/GEMINI_V03_PASTED_MODULE_CODE_AUDIT_2026-10-27.md).
7. [Existing EXFOR acquisition prototype](wp_b/revised/iaea_exfor_pipeline/README.md).

## Crucial nuclear data semantics — read before fitting

**Spraker et al., DOI 10.1007/s10894-011-9473-5** report an alpha-particle **Counts/Luminosity** observable X, with cross-section units, that has **not been divided by the number of outgoing alphas per reaction**. Depending on energy cuts, branches and angular integration, its value is **not automatically the physical number of fusion reactions per target-proton pair**. The 2012 article discusses ~2.1 alphas in its chosen alpha_1 peak window at 675 keV lab, versus ~1.5 at 2.64 MeV; this demonstrates **energy-window-dependent detection multiplicity**, not a globally fixed 3× conversion. Exactly three alphas are produced in the specified p+^11B → 3α complete breakup reaction, but the alpha observable integrated over a restricted energy region is not simply 3× every channel's total reaction cross section.

The source-normalized CSV uses a legacy column name `sigma_b`, reflecting the EXFOR `(5-B-11(P,A)4-BE-8,,SIG)` label. **Its interpretation for event-level fusion reaction probability is flagged as PROVISIONAL / ALPHA-COUNT-RELATED until matching the exact author's integration, channel and normalization definitions**. Do not silently plug `sigma_b` into a per-reaction birth integral and then multiply by 3. The original IAEA master is authoritative for recorded columns; the paper's count/luminosity discussion is authoritative for its physical interpretation. Use explicit quantity-kind tags in future normalized schemas, with no hidden aliases.

Primary [EXFOR entry C2973](https://github.com/IAEA-NDS/exfor_master/blob/main/exforall/C29/C2973.x4), [Spraker paper](https://doi.org/10.1007/s10894-011-9473-5), [NePTUN/Popper 2026](https://arxiv.org/abs/2609.33483). The master has **ERR-S statistical errors**, plus a correlated **3.6% target-thickness systematic**. The authors discuss a broader overall systematic **≤5%** for the alpha-count observable. Do not independently add these as two unrelated random uncertainties. The flattened exfortables summary dropped errors in some columns.

## Review of proposed DeepSeek final numerical tests

- **Cross-section / yield benchmark:** at 1.0 MeV lab, the EXFOR C2973002 numeric entry is **315.936 millibarns (0.315936 b)** with statistical error **10.9008 mb**, plus source-wide systematic. This is an **EXFOR-labelled integrated alpha yield** requiring event-multiplicity reconciliation before use as a reaction probability. Test exact source-table reproduction with a narrow near-machine-precision tolerance, not a generic ±10% scientific license.
- **BN proton range:** the NePTUN 2026 report is associated with an SRIM-derived approximately **57 μm** proton range benchmark at **2.5 MeV** in BN in contemporaneous secondary technical summaries. The precise SRIM inputs, density, stopping version and source statement should be checked directly before adopting **57 μm ±5%** as a frozen unit-test target. Even a correct range at one energy cannot validate the full energy-dependent stopping curve or alpha scattering. A 4–6 μm film being shorter than the range is not equivalent to negligible energy loss, especially when resonant cross sections are energy sensitive.
- **Three-alpha event physics:** sum of alpha kinetic energy in appropriate **CM frame** is approximately `Q + E_CM`, not merely Q=8.68 MeV; calculate LAB energy with projectile momentum and recoil. Per-event momentum conservation, channel masses, and nuclear four-momentum must be checked; a strict numerical tolerance is a **computational** test, not an experimental measured alpha spectral benchmark. Do not force every event to have 3.76/2.74/2.74 MeV; that is an illustrative channel/geometry approximation.
- **Detector hardware:** diamond is a serious candidate; wide-bandgap/fast recovery does **not** eliminate cabling/EMP, baseline pickup, species confusion or amplifier saturation. Fiber-optic readout is an instrument option, not the only validated architecture.
- **Statistics:** low-count Poisson with background nuisance and continuous EMP/shot noise as separately observed detector-response processes. A Poisson–Gaussian mixture is one candidate, **not universally the correct likelihood**. Select after blank-shot calibration and goodness-of-fit.

## Framework portability contract

To adapt G0-B to another reaction, replace the reaction registry; source nuclear mass and Q values; energy-frame conventions; differential/multiplicity-aware observables; stopping/material composition and geometry; detector forward response; controls and cost/energy interface. Keep frozen: source IDs/hashes, explicit quantity kind, sample inclusion criteria, statistical/model uncertainty categories, blind lockfile, negative-result lineage and full source-to-diagnostic/boundary ledger. Never transplant numeric thresholds from p–11B to a new reaction without calibration.

## Machine-readable discovery

See [research metadata JSON](RESEARCH_METADATA_STARS_2_0_2026-10-27.json). GitHub **repository topics** are a separate repository-settings metadata field: documenting recommended tags here does not imply that topics were updated in GitHub settings. Recommended discoverability topics (subject to GitHub's maximum number): `proton-boron-fusion`, `nuclear-physics`, `aneutronic-fusion`, `exfor`, `reproducible-research`, `laser-plasma`, `particle-transport`, `open-science`, `experimental-design`, `alpha-particles`, `boron-nitride`, `plasma-physics`, `physics-simulation`, `data-provenance`, `fusion-research`.

## Licensing, citations and scope

Respect original EXFOR records and cited authorship; individual paper/source terms may differ from the ORCS repository license. Do not imply that repository data exports convey ownership of the underlying nuclear measurements. Cite original scientific papers, EXFOR entry/subentry and the specific repository commit/path. Authors named in primary papers are **source authors**, not authors of Stars 2.0. Credit project lead and explicitly attributed AI reviewer contributions separately. **No DOI has been minted for this work; no external peer-reviewed approval or registration is claimed.**
