# Full p–¹¹B hybrid recovery — reconstruction report v0.1

## Finding and scope

Recovered originals reproduce the historical mirror and scaling numbers and the acoustic preparation models. **There is not yet an authenticated execution package for the latest full integrated hybrid.** This release keeps those two statements separate. It adds evidence to PR #39 without rewriting its historical template or registry.

The reconstruction request names acoustic pretreatment and sustained modulation, laser proton acceleration, hollow-sphere geometry, staged boron catchers, rotating-mirror retention, repeated encounters, helium-ash handling, alpha-energy recovery and industrial integration. Every named module remains in the hybrid identity. A missing transfer model is an explicit open interface, not a reason to discard the module or substitute a zero physical effect.

## Search and provenance

Pinned GitHub main: `876bb375d278e9ccb934638fbfbe64852fbcbfbd`; PR39 head: `b8687d7945fa5ef62362f1c7f15f85e1fa036bf9`. PR39 remains a draft, unmerged. Five October 29 whitepapers were recovered at the main snapshot:

- PRISM / hollow-sphere modular architecture addendum.
- Integration-first industrial stack policy addendum.
- Centrifugal three-module toy and DeepSeek reply.
- Centrifugal-hybrid 525 MW scaling whitepaper.
- Acoustic recovery and T/D/H energy-ledger contract.

Their paths, Git blob SHAs and source URLs are in PROVENANCE.json. The later integration-first policy is the operative clarification: retain full-stack potential-derived exploration and quantify interfaces/adverse coupling. The earlier architecture document's restrictive language is not used to suppress the full hybrid.

All 37 discovered ORCS branch trees were scanned for relevant paths. An initial Stars subtree scan was followed by a whole-tree filename scan for PRISM, centrifugal, 525 MW, pretreatment and Stars/hybrid candidates. These scans did not find the named original toy Python/CSV artifacts in Git at those tips. GitHub code searches across ORCS and manus-artifacts led to the whitepapers; Library searches recovered the scripts and archives. SEARCH_SCOPE.json preserves the branch tips and limitations. This is not a search of every historical blob or a full export of private conversation history. A negative search result cannot establish that an execution never happened.

Library recovery found both copies of the three-module script and both copies of the reduced script. Each pair is byte-identical. All original source IDs, versions where available, file sizes and SHA256 values are preserved. There are 13 ZIP archives and 120 inventoried files including extracted contents and pinned GitHub documents. Prior figures and receipts are preserved locally; archive hashes permit later reconciliation.

## Executed baseline comparison

| Recovered program | Original output | Replay result | Physical scope |
|---|---|---|---|
| prism_sphere_reduced_model.py | 12-row exploratory sweep | CSV byte-identical | Scalar source fraction, capture, return survival and effective passes |
| stars_prism_three_module_toy_2026-10-29.py | Eight mirror/barrier cases | CSV byte-identical | Isotropic loss-cone proxy, assumed orbit multiplier, one-use proton recurrence |
| stars_525mw_gain_scenarios_2026-10-29.py | 18 scaling cases | CSV byte-identical | Arithmetic sensitivity layered on an assumed 525 MW baseline |
| Acoustic v0.6 | arm comparison | CSV byte-identical | Damped oscillator and independent uniform-B test particles |
| Acoustic v0.7 | four-arm spherical comparison | CSV byte-identical | Rigid fluid-cavity radial modes; separate finite-wall particle trajectories |
| Acoustic v0.8 | arms and 14,000 paired shot samples | Both CSVs byte-identical | Assumed target displacement and optical overlap; seed 20261028 |
| Acoustic v0.10 | 84 timing/phase/coupling cases | CSV byte-identical | Envelope, hypothetical material memory and absorbed-optical-energy proxy; seed 20261028 |
| Acoustic v0.11 | 18 duration/arm cases | CSV byte-identical | Euler envelope/history dynamics; nuclear outcomes NOT_MODELED |
| Acoustic v0.12 | 30 duration/arm cases | CSV byte-identical | Analytic long-duration extension through ten seconds; nuclear outcomes NOT_MODELED |

Original dependency versions, launch records and exact source commits were not recovered. This reconstruction used Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0 and Matplotlib 3.10.8. Eleven CSV hash matches establish output reproduction in this environment, not original-environment identity. No random draws occur in the mirror/scaling programs; acoustic v0.8 and v0.10 pin seed 20261028.

An initial replay-wrapper attempt ran eight of nine programs; the scaling script could not find its input CSV beside its staged source because the original upstream toy wrote it to `/mnt/data`. The wrapper was corrected to stage that newly generated CSV in the expected location. No historical source was changed. INITIAL_WRAPPER_FAILURE_RECEIPT.json preserves the failed attempt; REPLAY_RECEIPT.json records the successful nine-program run.

## Historical numbers recovered

| Scenario | Events per pulse, archived rounded output | Relative to full-capture single pass |
|---|---:|---:|
| Ideal single pass | 5,000.000 | 1.000000 |
| R=5, no barrier, capture 0.3 | 9,552.116 | 1.910423 |
| R=5, proton barrier 30 keV, orbit multiplier 1.5, capture 0.3 | 12,678.924 | 2.535785 |
| Same, alpha barrier 300 keV | 12,678.924 | 2.535785 |
| Differential, capture 0.6 | 25,357.849 | 5.071570 |
| Differential, capture 0.1 | 4,226.308 | 0.845262 |

Inputs are illustrative: 10¹⁰ source protons, useful fraction 0.05, per-pass fusion probability 10⁻⁵, ten effective opportunities, 200 keV representative proton energy and 2.9 MeV representative alpha energy. They are not an integrated laser/PIC/stopping calibration. Q=8.68 MeV in this original; the earlier reduced model uses 8.7 MeV. Both are preserved rather than silently reconciled.

The reduced model's capture-0.6 / 30-pass case gives 14,980.837 events (about 2.9962 times its reference). It is a different model with fixed 0.8 return survival. It is not the 25,357.849-event three-module case and not a recovered full industrial hybrid.

The alpha-barrier pair has identical births **by construction**: alpha escape never feeds back to proton populations, fuel dilution, space charge or reaction probability. It cannot establish that ash removal has no effect in an actual plasma.

## Independent audit and new ablations

A separate script reconstructs the particle recurrence, checks a finite-geometric-series solution, closes proton counts, runs zero-reaction/unit-reaction/zero-capture limits and examines a conditional mirror correction. **77 checks pass**, and 32 new factorial scenarios cross mirror ratio, barrier, orbit multiplier, capture and barrier convention. These are new derived audits, not claimed historical hybrid runs.

For admitted protons N, per-pass reaction probability p and post-reaction escape probability l:

\[
N_{k+1}=N_k(1-p)(1-l),\qquad F=\sum_kN_kp.
\]

The independent audit records reacted, lost and remaining protons. No proton reacts twice. The mirror×barrier interaction contrast is +2,900.641 events under the archived convention but −280.392 under the conditional throat-potential convention, holding capture 0.3 and orbit multiplier 1 fixed. Thus even the sign of a toy interaction can depend on a physical definition. These contrasts are not measured apparatus synergy.

### Barrier normalization needs resolution

The original implementation uses

\[
u_c^2=1-1/R+V/E.
\]

If V denotes an actual potential-energy increase from midplane to the field maximum, conservation of magnetic moment and total energy instead yields

\[
E_{\parallel,\rm throat}=E-R E_\perp-V,\qquad
u_c^2=1-1/R+V/(RE).
\]

Here u is the cosine of midplane pitch angle; V is an energy, not a voltage. This derivation assumes adiabatic motion and the effective barrier at the mirror throat. It follows the energy/trapping relations in Kolmes, Ochs & Fisch (2024), *Loss-cone stabilization in rotating mirrors*, DOI [10.1017/S0022377824000205](https://doi.org/10.1017/S0022377824000205), Eqs 2.3–2.4. It does not supply a PRISM geometry or a measured centrifugal barrier.

At R=5 the archived 30 keV parameter would correspond to a 150 keV throat barrier under this interpretation. With every other toy assumption unchanged, the differential capture-0.3 case becomes **8,556.831 events**, a gain of **1.711366** against the ideal 5,000-event reference rather than 2.535785. This conditional correction reduces that case by about 32.51%. If the original V was deliberately a rescaled effective pitch-angle parameter rather than a physical end-to-midplane energy difference, its definition and physical mapping need documenting instead. Neither result is a validated mirror prediction. Historical outputs are unchanged.

A second issue is that an isotropic loss-cone fraction is reapplied after every pass. Collisionless trapped survivors do not automatically re-isotropize each transit; pitch-angle scattering, return timing and the distribution of newly injected particles must justify that hazard. The scalar orbit multiplier also is not a full-orbit calculation.

### Acoustic interpretation retained

Recovered v0.10 has OFF, SHAM, PRE_ONLY, SUSTAIN_ONLY and PRE_PLUS_SUSTAIN with paired noise and phase controls. Under its **assumed** geometry coupling, phase 0 sustained preparation changes mean absorbed optical energy from 0.17993817 J to 0.18555187 J; adding its hypothetical memory pathway gives 0.19286005 J. Disabling both assumed couplings gives the same optical output for every schedule. Those outputs do not represent measured laser absorption or nuclear energy.

The v0.12 ten-second case reproduces amplitude/history values 0.367879441 / 0.804066237 for PRE_ONLY after its 2 ms decay gap, and 1 / 1 for continued drive. It already essentially saturates its **assumed** memory model by 100 ms. That is a property of specified 1 ms/5 ms timescales, not evidence that a real target is ready after 100 ms. Readiness should ultimately use observable target/source stability with logged time to readiness, firing attempts and failures.

The new acoustic ablation table exposes the recovered proxy/null comparisons. The nuclear coupling remains NOT_IMPLEMENTED; this is not a calibrated zero-effect claim. Reduced physical shot failure or jitter can materially change total useful output once its measured or explicitly scenario-based probability model is connected to the source distribution and cycle time.

## Energy and scale reconciliation

The three-module energy column is **reaction Q times expected events**. It does not calculate the full alpha kinetic distribution, incoming proton kinetic contribution, electric field work or usable electrical recovery. At capture 0.3 the admitted 200 keV monoenergetic proxy contains about 4.80653×10⁻⁶ J (4.80653 µJ), while the original differential toy releases about 1.7632×10⁻⁸ J of nuclear Q. This comparison only concerns the specified admitted proxy and its arbitrary per-pass reaction probability; it is not a wall-plug Q or an upper bound on another apparatus.

The 525 MW script independently assumes a 525 MW baseline and multiplies it by toy/illustrative gains. Its net-baseline interpretation gives 3,150 MW at a sixfold factor. Its gross-fusion interpretation assumes 40% conversion, 50 MW fixed auxiliaries and incremental auxiliary demand, giving 1,157.5 MW. These exact CSV numbers reproduce. **No calculation connects the 5,000-event toy normalization to that 525 MW plant baseline.** There is no modeled ignition, sustained burn, source power, plant design or capital estimate establishing either output.

A coupled ledger must separately track source/actuator/RF/magnet power, incoming particle kinetic energy, nuclear Q, external work, stored energy, escaping particles/radiation, deposited heat and electricity at load. Alpha channeling, direct conversion and thermal recovery must partition one energy stream rather than each claim it in full. Repeated encounters require actual surviving particles at their degraded energies, not reuse of a gain factor or consumed protons. Gross recovered heat is not automatically electrical revenue.

## Decision

Retain the full hybrid as an exploratory apparatus with all modules selectable. Preserve the reproduced scripts as the historical baseline. Do not transfer the mirror gains or 525 MW arithmetic into reference apparatus performance. The immediate implementation priority is a source-to-mirror/catcher particle handoff with explicit field work, stopping, survival and all-attempt timing; then connect conditional acoustic readiness effects and collector allocation. Use paired evidence-constrained and exploratory scenarios with clearly stated missing adapters. Quantify incompatibilities rather than declaring the architecture impossible in advance.

The exact later full-hybrid run still needs its entrypoint, configuration, data, numerical outputs and receipt. Until recovered, a new coupled implementation must carry a new run identity and cannot be called reproduction of that reported run.
