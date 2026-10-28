# STARS 2.0 — Gemini Argon v0.5 proposal: relativistic kinematics, scattering, cryogenic thermodynamics

**2026-10-27 | Project: Atlas Lattice / ORCS**  
**Origin:** User-shared Gemini Argon follow-up to independent WP-B v0.4 A/B audit.  
**Status:** independent scientific triage by ChatGPT/Tidal Lantern; proposed engineering change requests, **not implemented, tested or calibrated**.

## Executive outcome

The proposed refactor is warranted, but **do not let Gemini's attractive physical narrative write the test expected values**. A pure four-vector sequential-decay engine is a good next step; scattering needs material/ion-specific validation; the LNG cold-cascade analogy is an optional site-dependent future industrial branch, unrelated to proving the pre-simulation proton-boron physics or acoustic controls.

### 1. Relativistic conservation — ADOPT, but correct the proposed W formula

Gemini proposes `W = sqrt((E_cm_tot/c²+M_12C)²-|p|²)` for the compound invariant mass. This combines ambiguous frame quantities and dimensions. If `E_cm_tot` already represents CM total energy, total momentum is zero there and there is no momentum term to subtract. Instead work in units c=1 with source-defined nuclear masses:

`P_in = (E_p,lab + m_B11, p_p,lab)`, target B11 stationary,  
`s = P_in·P_in = m_p² + m_B11² + 2 m_B11 E_p,lab`,  
`W = sqrt(s)`, `beta_CM = |p_p,lab|/(E_p,lab+m_B11)`.  
`Q = m_p + m_B11 - 3*m_alpha` in consistent bare-nuclear-mass convention; precise nuclear masses/energy should be source qualified. The `^12C*` intermediate has compound invariant mass W, not a separately added arbitrary ground-state 12C plus reaction Q. Generate the sequential `P_in→alpha1 + Be8*`, `Be8*→alpha2 + alpha3`, with source-traced channel mass/width/branching and exact Lorentz boosts. Enforce `P_in = P_a1+P_a2+P_a3` to precise numerical tolerances *in physical MeV and MeV/c units*, rather than the existing w-vector/effective-mass self-closure.

Add tests at lab 162 keV, 675 keV, 1 MeV and >1 MeV; check inverse boosts, invariant masses, zero-boost case, threshold/kinematic impossibility rejection, permutation/identical-alpha consistency, per-event lab kinetic sum `Q+T_p,lab`, CM kinetic sum `W-3*m_alpha`. Strict output tolerances should be tied to stable floating-point calculations (not a magical universal 1e-16).

Scientific reference: [Particle Data Group, Kinematics](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-kinematics.pdf).

### 2. Charged-alpha angular scattering / energy straggling — ADOPT gated test branch

Gemini gives a Highland/Molière-style formula `theta_0≈(13.6 MeV/(beta p c)) z sqrt(x/X0)` and **asserts 3–7°** exit divergence and an optimum shift toward 6 µm. No source-qualified BN/Si/C energy-dependent stopping and angular scattering model, layer thickness, charge-state, projectile distribution, trajectory angle or validated radiation length is given. The formula is a *candidate approximation* with a domain of validity; it is not an automatic benchmark for sub-MeV to few-MeV heavy alpha ions in micrometre targets, especially approaching stopping range. Energy loss, nuclear stopping, angular tails, path length and correlation matter. Source-check and benchmark with validated ion-transport measurements and material-specific TRIM/SRIM-like collision simulations before adopting a distribution.

Implement A/B: identical p–11B event stream, geometry, source and collector window; `SCATTER_OFF` vs `SCATTER_ON_EXPERIMENTAL`, then vary model and thickness/angles. Report full exit (E,theta,phi) distributions, backward scattering, non-Gaussian tails, recoil/deposited energy, collector acceptance with uncertainty. **Never hard-code any scattering-induced outward optimum shift** or narrow 3–7° divergence as fact; observed numerical optimum may move in either direction or disappear after validation.

References: [Particle Data Group, passage through matter](https://pdg.lbl.gov/2023/reviews/rpp2022-rev-passage-particles-matter.pdf); [low-energy ion scattering and energy-loss experimental comparison](https://doi.org/10.1103/PhysRevA.88.032901).

### 3. LNG / desalination cryogenic-cascade analogy — PARK as conditional industrial systems study

Gemini suggests co-locating a hypothetical future fusion testbed and industrial LNG cold recovery if cryogenic hydrogen/deuterium handling becomes useful. STARS is p + **11B**, not a deuterium experiment, and **cryogenic boron targets are not a verified baseline design requirement**. LNG-regasification cold-energy utilization requires suitable geographical/industrial co-location, true temperature-grade matching, safety, regulatory review, contamination isolation, capex, thermal duty, intermittency and full entropy/exergy treatment. It does not automatically *slash* auxiliary power, and is not a reason to complicate WP-B v0.5.

Reserve a future separately financed `industrial_integration/cryogenic_auxiliary_option` proposal; keep outside the physics calibration, acoustic A/B, original alpha energy accounting and experimental G0-B lockfile until real facility loads and cold-source availability are measured.

### 4. The four earlier known engineering issues still block promotion

- **Event→transport coupling:** Gemini v0.4's `generate_correlated_3alpha_events()` is not the event source for `alpha_escape_and_collector_window()`; the main sweep instead uses weighted hard-coded alpha spectra. Coupling must preserve events/angles/energy/depth/detector acceptance.
- **Material identity:** the 25-µm Si/C-like support currently uses BN stopping tables for protons and alphas. Introduce per-material and layered tables with known density, units, version, charge state and energy domain; in any calibrated run fail closed on missing material.
- **Mass consistency:** physical p, B11 and alpha masses, Q and Lorentz-invariant kinematic closure in same declared nuclear convention; independently check exact-energy residual and four-vectors.
- **Blind G0-B:** protocol is **DRAFT**, not actually preregistered. Freeze predictions only after EXFOR observable semantics, material stopping and detector calibration, statistical design and independent custodian review; keep Gemini's simulation claims separate from future measured outcomes.

### 5. Work implementation instructions

Make refactor a *reproducible research branch*, preserve Gemini v0.4 original SHA and outputs unchanged. Prefer narrow acceptance contracts:
- `K-REL`: proper s, W and boosts; event conservation independent of generator internal algebra.
- `MAT-STACK`: material-qualified range & stopping, including support layer ordering.
- `A-B-SCAT`: scattering OFF/ON with no assumed direction of collector optimum.
- `A-B-CREST`: phase method vs multiple physical damage thresholds; crest maximum alone insufficient.
- `BLIND-FREEZE`: explicit not-ready state until G0-B source, response and background gates pass.
- `THERMO-SCOPE`: cryogenics only a separate optional conditional study, not the next core simulator sprint.

**No repaired v0.5 engine exists by virtue of this note. It is a proposal audit and a Work implementation input.**

## Attribution and reproducibility

Gemini Argon proposed the relativistic refactor, scattering correction, LNG cascade analogy and coding next step; Copilot and DeepSeek identified underlying observable/matter/geometry gate issues; ChatGPT/Tidal Lantern independently differentiated supported physics from unsupported numbers and recorded exact acceptance tests. Preserve tests, failures and uncertainties.

**Wizard wall:** Zero physics produces zero magic. Conservation before celebration. Lower peaks do not always mean lower damage. And *a claimed 3–7° scattering correction shall not move an optimum until the particles have actually been simulated.*
