# Beyond Q — continuation checkpoint, November 1, 2026

Read WHITE_PAPER.md and DECISIONS.json first. This checkpoint is intended to survive a thread/credit limit. Do not restart from historical small-reactor assumptions.

## Controlling architecture

- Two separate ARC-class proposed reactors: A 1,100 MW PRIMARY DD fusion; B default matched 1,100 MW DT, with explicit public-reference 1,130 MW option.
- A's historical +20 MWe NET projection is unvalidated. It is NOT a 20 MW fusion reactor. Executed energy sensitivity assumes A draws 100 MWe; do not promote that assumed draw to physics.
- Isotopes are the primary outputs; available net electricity is secondary. No GPU/QPU design, financing or compute revenue is included. The module can be an addition to an existing host campus or serve external customers.
- B has its own lithium-breeding blanket; gross TBR=1 is a replacement-breeding sensitivity, not a demonstrated recovered self-sufficient cycle. Lithium and deuterium are consumed. A supplies startup/makeup and potential external/expansion fuel.

## Latest originator decisions — do not lose these

1. **NO mandatory He3 reserve for the standalone/GPU-hosted baseline.** Next default retained_fraction=0. Saved v2.0 input is still 0.5 and must remain an independent historical artifact. Optional QPU/strategic allocations can be inputs later; no QPU economics is required.
2. Overall eventual He3 recovery cases: **37.5% conservative potential, 75% planning, 90% optimistic**. All assumed; apply loss once and distinguish pipeline holdup from loss.
3. Prices: **$1,500/STP L He3; $1,500/g T**; 30-year/5% financing. Separate product value from cash receipts and qualification. Housing/site, OPEX and replacement costs are incomplete.
4. **CRITICAL FLEET RULE: separate external financing for EACH new campus; predecessor campuses supply fuel, not the purchase price. Campus 2 receives eligible T from campus 1; campus 3 from campuses 1+2; campus k from eligible predecessors 1..k-1.** Pooled qualified stock above donor reserves accelerates fuel readiness. Do not require predecessor cash to fund successor CAPEX, and do not infer exponential growth has been simulated.
5. Fuel, donor sustainability, recipient finance and engineering/site readiness are separate gates. Reserved/transported fuel is debited and cannot also be sold or pledged twice. Shipment losses, decay, recipient receipt and foregone T sales must be explicit. Intercampus transfer pricing/ownership is unresolved.

## What exists on GitHub

- Repository: atlaslattice/open-regenerative-compute-standard.
- Draft PR #65: https://github.com/atlaslattice/open-regenerative-compute-standard/pull/65 . Branch `research/beyond-q-module-fleet-v2.0`.
- Base of this paper: commit `971a94300d91d4ff514061a4918e44684277e78b`.
- PR #65 is stacked on draft PR #63 / `research/beyond-q-capture-target-v1.9`; preserve dependencies and earlier releases. Do not merge or overwrite old artifacts by inference.
- `module_fleet_v2_0/`: 60-year one/50-module physical ledgers and connected conditional finances; 16 tests pass. NumPy 2.3.5, Python 3.12.14, seed119, dt0.25 day. Full raw CSV and HTML regenerate from run.py; compact execution and summary evidence are committed.
- `review_reconciliation_v2_0_1/`: five passing reconciliation tests plus a dashboard data/filter harness. Explicit A/B sources, transfers, decay and unsold inventory; parent physics unchanged.
- `financing_note_v1_0/`: financing-scope arithmetic/history.
- This directory: comprehensive paper, latest decisions, machine-readable numerical checkpoint and resume instructions. This is documentation/recalculation, not a new physical rollout run.

## Results that must be stated with their assumptions

- Single-module B starts day246 after A accumulates ~71.654kg (one full-power-year burn plus10kg reserve). No modeled B fuel shortages after startup in baseline.
- Annual net electricity: year1 +119,053 MWh; year2 +2,170,561 MWh. Gross imports still occur (629,520 and85,320 MWh). Annual net positive is NOT electrical islanding.
- Fixed-calendar fleet: first year -2.877TWh because10A units operate but only3B units have started; year2 +12.909TWh. This is not evidence of mature modules becoming net negative.
- At37.5% overall recovery, He3 candidate year1 335,841L; year2 332,089L. Separate85% macro availability AND15/16source duty explain why this differs from the earlier939k gross at85%EFFECTIVE exposure.
- With ZERO mandatory He3 retention, full qualified sale at assumed prices,20kg conditional T exports, partial-scope$5.9B hardware debt and priced imports: year1+$87.006M; year2+$135.799M remaining BEFORE unknown costs. Do not call this complete profit or evidence of break-even by midyear2.
- At75%, selling only350kL gives ~$108.245M / $162.665M headroom. Unsold product has illustrative value but not automatic cash receipts.
- The saved50%-retention/fleet350k-sales-cap case gives negative financial stress results. That sales cap is fleet-wide and arbitrary, NOT global measured demand. Full-offtake is a sensitivity, not guaranteed sales.

## Review corrections already settled

DeepSeek's 7:1 error allegation compared A He3 with B blanket T. Actual year1 A DD T=121.041309kg; A He3=121.040508kg; atom ratio1. B breed=burn17.130502kg because selected grossTBR1. Decay2.964505kg is included; stock is not decay-free. A secondaryTburn6.314544kg is included. Terminal20kgTexport is physically withdrawn. A→B108.447535kg is internal, not another source. Final stock85.999144kg closes the full campus ledger.

The review was right to request better display of these terms, market controls and banked inventory. At50modules/75%/capped-sales/year60 unsoldHe3 bank890.924millionL is real within that stress case. Updated dashboard exposes it. Per-reactor losses unavailable in old exports remain null, not fabricated zero.

## Next implementation, AFTER this checkpoint

1. Freeze existing numerical artifacts and use a new version for zero-He3-retention and fuel-supported rollout.
2. Add a discrete expansion controller: eligible donors, reserve floors, committed inventory, fuel shipments/in-transit/receipt, independently financed recipient, construction/maturation queue, startup and failure/blocker logging.
3. Define a sustainability evaluation window explicitly; strict mode cannot set unknown full-cost or physical readiness true. Conditional scenario mode can impose assumptions but must label them.
4. Compare synchronized identical mature modules, the old fixed-calendar fleet and the new gated cascade. Add controls for financing denied, no surplus, transport loss, concurrent claims on fuel, construction delay and correlated outages.
5. Price transferred fuel consistently with foregone external sales; avoid counting donor sales on recipient fuel. New financing does not have to originate from predecessor cash.
6. Continue evidence work: feasible full DD plasma operating point, qualified OpenMC geometry/data/yields and deposited heat, ASIPP pump regeneration data, buyer purity/tritium specs, complete installed costs and long-term replacements.

## Evidence and tools

G1-G5 remain OPEN. No new physical OpenMC/WarpX transport or long-time plasma result was generated today. The source/patent evidence and quantum-market survey are in the paper with limitations. Prior small collision benchmarks are not reactor or laser-device validation.

GitHub connector tools can create a tree, commit and update refs with expected-head leases. Local `repo/` is a reconstructed working directory without a `.git` checkout; do not assume local git push works. Read the live branch head before modifying it. User has authorized routine research implementation and versioned GitHub draft publication; do not repeatedly request permission for ordinary reversible work. No external outreach has been authorized or sent.

Stop point: the comprehensive paper is being logged before implementing the cascade. Next thread should begin with that controller, not rerun birth arithmetic or rewrite the architecture.
