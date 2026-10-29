# Beyond Q v2.3 — Model-check receipts and limitations
**Version:** 2026-10-29. **Source:** [screening Python code](source/beyond_q_physics_v23.py), especially assertions in `checks()`; [reported check output](source/model_checks.txt).

The code contains **seven assertions summarized in six PASS labels**. No current output gives per-check numerical residuals or a frozen machine/runtime identity. The tolerances shown below are extracted from the published code, not separately rerun in this update.

| Reported category | Check and input | Pass logic / tolerance | Observed status | What it does NOT prove |
|---|---|---|---|---|
| Electrical net identity | Derived gross electricity and auxiliary draw | `abs(DD_net - (gross_e-aux)) < 1e-9` MW | PASS reported | Correct real auxiliary equipment sizing |
| Nuclear Q bookkeeping | Parametric DD, secondary DT, Li6 nuclear terms | `abs(nuclear_q - sum(nuclear terms)) < 1e-9` MW | PASS reported | Valid neutron source, blanket heat, or measured Q terms |
| Facility-boundary algebra | Derived net electricity, modeled local/unconverted energy, nuclear Q | `abs(DD_net + unconverted_and_local - nuclear_q) < 1e-8` MW | PASS reported | Verified location of waste heat or plasma transport |
| Isotope recovered no more than born | Reported T and He3 birth and recovery flow | **Two assertions:** `0 <= T_recovered <= T_born`; `0 <= He3_recovered <= He3_born` | PASS reported | Real purity, separation feasibility, isotope residence/burn |
| Tritium bank conservation | 20y constant deposited T, active inventory + decayed mass | `abs(active + decayed - annual_deposit*years) < 1e-8` kg | PASS reported | Accurate physical capture/recovery or radioactive handling systems |
| Decay-He3 cumulative monotonicity | 20-year computed He3 decay series | Each new cumulative value ≥ preceding cumulative value (no numeric tolerance) | PASS reported | Actual recovered He3 gas, quality, market demand |

**Critical limitations:** All checks are deterministic algebraic assertions at hypothetical operating inputs. There is no measured DD plasma confinement point, no neutron transport simulation, no empirical RF absorption verification, no cryostat wall-plug measurement, no statistical uncertainty coverage, and no 20-year C1–C4 ROI/NPV/IRR calculation. Absence of these is **UNRESOLVED**, not a passed gate.

**Reproduction:** See the [Python program](source/beyond_q_physics_v23.py), [assumptions.csv](source/assumptions.csv), [screening_results.json](source/screening_results.json), [tritium_bank_20y.csv](source/tritium_bank_20y.csv), and [original run receipt](source/model_checks.txt). Execute the model in an ordinary Python 3 environment, then compare each assertion with the source. Numerical tests alone are insufficient for a full physical validation.
