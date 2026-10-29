# Stellar Forge Reference — integration contract candidate v1.1

2026-10-28 America/Chicago. Candidate for council gap review; not a final scientific freeze. Supersedes implementation details only where explicitly stated below. Prior source artifacts and versions remain unchanged. User supplied DeepSeek/Copilot review is the input, not evidence that proposed numerical gates have passed.

## Disposition

Adopt four evidence gates (SOURCE_TRACED, SOURCE_REPRODUCED, CALIBRATED, VALIDATED) as separately scoped metadata, plus orthogonal quantity provenance. Input maturity never establishes a derived model's validation. Dependency metadata identifies the assumptions influencing a specific result. Unrelated measurements are not downgraded. Source enums in the original modules remain unchanged; the new dependency layer supplements them instead of retroactively changing historical labels.

Adopt explicit source/reaction/transport/detector/collector/system domains. No reaction inherits reactor maturity or loses measured reaction evidence merely because a power plant is absent. D–He-3 should not be declared inherently parametric; its actual imported data status must be checked. No new reaction engine is supplied in v1.1.

Allow scenario energy ledgers below calibration with visible assumptions and dependencies. Missing physical inputs block physical predictions; a supplied exploratory assumption permits only its stated scenario. Only VERIFICATION_DEMO is executable in this release; broader scenario-mode execution remains a subsequent gate, not an implied permission to extrapolate data.

Adopt BORN → EXIT → ACCEPTED → DELIVERABLE → REALIZED as separate quantities. Detector acceptance is not collector acceptance. The primary event generator, calibrated collector and time-dependent inventory/recovery stages are still absent. Do not manufacture those columns from existing ray fixtures. Realized revenue stays unknown without a transaction record; zero realized accounting credit is a policy, not an assertion that no sales occurred.

Retain nuclear resonance mapping, particle–wave resonance and mechanical/acoustic response as three research lanes with distinct equations/data. Do not require every reaction curve to contain a discrete resonance peak. Never insert a generic resonance gain multiplier. Nuclear-state/channel fitting, wave damping/coupling and measured modal transfer functions need independent tests.

Do not freeze 10% Spraker agreement, a 57 µm BN range, universal relative four-momentum tolerance or universal Qwall=1e-7. Use original observable semantics, source uncertainty, scale-aware component residuals and documented calibration domains. The old unsupported anchors remain blocked. A zero-reaction null produces zero reaction-attributable Q/products, not necessarily strictly negative output if all inputs are zero or stored energy is released; complete boundary/storage accounting is required.

Adopt structured failure codes, source/code/output hashes, deterministic fixtures, convergence layers and failures with receipts. v1.1 implements source missing, invalid input, unsupported calibration, out-of-domain range and acoustic convergence classifications; the full proposed catalog is not yet implemented. Exact-bit repeatability is tested in this environment; cross-platform tolerances remain to be specified, not presumed universal.

## Acoustic interface and UI

The local UI edits location, control arm, waveform, carrier frequency, frequency deviation/modulation, phase, acceleration amplitude, timing/duration, mode frequency/damping, sample count and declared driver wall energy. Tone, sinusoidal frequency modulation and linear chirp are supported by a synthetic single-mode ODE. REFERENCE/OFF/SHAM/ON are distinct recorded arms. OFF/REFERENCE have zero intended drive; SHAM has zero intended coherent forcing but may carry wall cost. This does not validate a laboratory sham or model thermal/EM confounding.

Location is metadata until a real component's geometry, M/C/K operators or measured transfer function are supplied. The benchmark predicts synthetic displacement/velocity, not local stress, fatigue or nuclear gain. Mode parameters and driver acceleration are not measured defaults. Driver wall cost must fit within the separately declared auxiliary total; no hidden cost duplication. A measured actuation→target-state→beam/transport link is required before acoustic settings alter physical outputs. These are future adapter requirements, not a disabled hidden effect.

UI export is reproducible configuration, not an in-browser fusion calculation. The CLI runs the same Python modules and produces a report for reloading into the UI. Never treat a UI preview as a calibrated simulation. Static precomputed public examples remain preferable to an unrestricted hosted API initially; no public site is deployed here. Market geography, quantity tiers, absorption caps, precision estimates and quotation qualification remain open fields for later economic schema expansion.

## Integration boundary

All currently available non-superseded executable production slices are incorporated or explicitly referenced in MODULE_INTEGRATION_v1_1.json. Historical audit scripts and raw source archives remain evidence, not runtime simulation engines. Superseded buggy implementations and external SHUGS/TCSS probes are not imported. Missing Gemini source/physical modules cannot be integrated by assumption. The next review must inspect source/kinematics recovery, full uncertainty propagation, grouped holdouts, all-shot causal inference, acoustic calibration and full energy/inventory closure before expanding physical run classes.
