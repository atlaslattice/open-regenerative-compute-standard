# Beyond Q v2.2 — fuel-supported rollout execution report

2026-11-01. Originator: Dave / Atlas Lattice. Computational implementation: GPT Work. Earlier documented GPT-6, DeepSeek and Gemini Argon analytical contributions remain credited in white paper v2.1. No institutional endorsement or experimental validation is implied.

## What changed

This is a new version, implementing the checkpoint at `../white_paper_v2_1_2026_11_01/`. The default He3 retained fraction is now zero. A/B source and fuel-cycle assumptions remain inherited. The copied kernel adds commissioning and fuel-accounting hooks without modifying prior releases; its no-controller output reproduces the parent source, burn, stock and energy regression.

A successor has independent recipient financing, not a requirement for donor cash to pay its capital. Before project authorization, eligible donors must meet a trailing 365.25-day positive NET-energy screen, have no trailing unserved B burn and have matured B operation over that window. This is a numerical screen, not continuous islanding or validated financial sustainability. The separate financing and fuel-qualification permissions are explicitly assumed in conditional cases.

Each donor keeps the same startup/operating stock floor, about 71.654 kg T: one uninterrupted FPY of B burn plus 10 kg. Uncommitted stock above the floor is pooled proportionally across eligible predecessors. Reserved mass is physically removed from donor B storage; it remains in separate custody throughout construction and shipping. The recipient cannot use it early, and the donor cannot export or promise it again. Transfers are added as donor/recipient terms in each campus balance. A separate custody identity accounts for reserved and in-transit stock, radioactive decay and transport loss.

The assumed lead time is three years construction plus seven days transport, with 0.1% transport loss and a small safety allowance. Initial reservation is about 85.090 kg per project so receipt remains approximately 71.726 kg after these losses. Donor after-reservation floors and recipient arrival thresholds are checked. These are research policy inputs, not measured logistics or reactor project timelines. The combined escrow compartment does not simulate individual physical transport equipment or qualified container capacity. A derived custody table shows scheduled dispatch versus actual simulated reservation and receipt.

## Readiness policies — do not conflate them

| Case | Meaning |
|---|---|
| `strict_unresolved` | First bootstrap campus operates as a research scenario; expansion is blocked because complete-cost and physical/fuel qualification evidence is missing |
| `sequential_predecessors` | Conditional qualification/financing permissions; campus k waits for ALL earlier campuses to qualify, then their surplus can fuel it |
| `eligible_pool` | Relaxed conditional sensitivity: currently mature donors can authorize multiple separately financed projects without waiting for every earlier project ID to mature |
| `fixed_calendar` | Earlier one-project-per-0.1-year control; no intercampus transfer |
| `synchronized_seeded_control` | All campuses commissioned together with explicit initial T in each; not a bootstrap or fuel-pooling result; outages remain independent/common as configured |

The sequential interpretation is the baseline in inputs.json, honoring the stated campus1→2, campuses1+2→3 example. The relaxed pool alternative is not silently substituted for it. In the sequential run, actual campus3 project reservations include donors1 and2, and campus4 includes1,2,3. In the relaxed pool run, early additional projects can be supplied by campus1 while campus2 is still building; it therefore answers a different concurrency question.

## Executed results

Five 60-year scenarios with capacity50 were run using Python3.12 / NumPy2.3.5, seed119, dt0.25day. The new zero-retention financial adapter produces 3,600 annual scenario/recovery/price/offtake rows. Separate four-year financing-denied and no-DD-source controls were also run.

| Policy | Operating campuses at year60 | First successor commissioned | 50th campus |
|---|---:|---:|---:|
| Strict unresolved evidence | 1 | Blocked | Not reached |
| Sequential qualified predecessors | 15 | About year4.826 | Not reached |
| Relaxed eligible pool | 50 | About year4.826 | About year42.280 |
| Fixed calendar control | 50 | Scheduled independently of fuel pool | By scheduled year4.9, followed by local B startup |
| Simultaneous/preseeded control | 50 | Initial condition | Initial condition |

The sequential run has a sixteenth campus in construction at the horizon. Its campus3 authorization occurs around year5.832 from donors1+2. The relaxed pool commissions50 with no waiting/building projects left at the horizon. These are finite policy-sensitivity results, NOT commissioning forecasts or proof of exponential growth.

The supply-feedback mechanism is represented: more mature campuses can contribute startup fuel. However, making every immediate predecessor mature before the next authorization imposes a roughly four-year serial construction-plus-qualification cadence under these inputs. The relaxed pool removes that serialization but still faces a four-project construction queue. Therefore the results do not establish unconstrained exponential growth; qualification, concurrency and construction policy determine much of the pace.

## Conservation and adverse evidence

The sequential run reserves/sends 1,276.354 kg, receives 1,004.159 kg and ends with 76.687 kg in combined escrow/transit. Escrow/transport radioactive decay is 194.503 kg and routing loss1.005 kg. The relaxed pool reserves/sends4,169.424 kg, receives3,514.556 kg, ends with no escrow stock, loses651.350 kg to decay and3.518 kg to routing loss. These sums independently reconcile in summarize.py.

Maximum pool residual is below6.6e-11kg. No donor reserve-floor violation occurs. Maximum per-campus T balance residual is below4.6e-9kg in the executed60-year scenarios. No scheduled B burn shortage occurs after allowed startups under the selected baseline physics. A zero-source control also has no served or scheduled B operation; its zero shortage must not be mistaken for a working reactor.

Finance denied for successors causes no shipments or additional commissioning. Zero DD source causes no T production, no B startup and no successor. Unknown strict-mode full costs block expansion rather than being silently treated as zero costs or approved financing. New isolated tests demonstrate both donors1+2 supply campus3, each receipt occurs once, reservation prevents double spending, donor floors remain protected, and unfavorable trailing energy prevents donor eligibility.

Ten new automated tests pass, including parent-kernel regression. This does not supersede or reinterpret earlier16+5 checks, and it does not establish physical qualification.

A five-year / three-slot sequential refinement at0.25 versus0.125day preserves the first successor commissioning day1762.75 and the reserved mass85.090kg. Final campus T differs by approximately0.084%. This checks one coupled scheduling realization, not all discontinuous readiness boundaries or a physical uncertainty interval; exact values are in refinement.json.

## Financial boundary

Recipient project authorizations record separate external financing permissions and a historical hardware-subtotal commitment; donor capital contribution is zero. This is a conditional permission, not a real loan agreement or modeled bank credit decision. Debt service begins in the recipient's operating years. Construction interest/fees, full installed buildings/site, operating and replacement costs remain unresolved. Reserved early fuel can incur substantial decay; custody and radiological-storage costs are not yet priced.

Zero mandatory He3 retention is active in this version. Recovery cases37.5/75/90%, price cases$1,500 and$500 per respective L/g units and capped/full-He3-offtake sensitivities remain explicit. All He3 sellable-quantity and receipt projections assume qualification; actual profit/qualified sales remain null. GPU/QPU configuration, financing and revenues are excluded.

The price/offtake financial sensitivities reuse each physical rollout; they do not feed back into donor eligibility. Conditional donor financial sustainability is an explicit permission override, not derived complete-cost profitability. In particular, a negative capped-sales financial sensitivity must not be described as passing a computed financial sustainability gate. Strict evidence mode blocks expansion while complete costs/qualification remain unknown. Connecting fully specified project cash flows to readiness is further work once those inputs exist.

External T sales are calculated only on donor-bounded terminal withdrawals AFTER fuel reservations. The same stock is not also sold when reserved for a successor. The event log reports an illustrative gross external-sale value forgone on reserved mass. That is NOT simultaneously booked as an extra expense and lost sales, nor a transfer cash receipt. Intercampus sale/grant/loan pricing and ownership contracts remain unresolved, so actual transfer receipts are null. Parent-campus cash is never required to fund the recipient's hardware in the controller.

The model is reactor-only finance. Full-offtake at constant prices over60 years is a sensitivity, not guaranteed market absorption. The fleet sales cap is a stress input, not measured global demand. Annual positive energy and conditional revenue headroom do not close physical energy-autonomy or full-cost profitability gates.

## Limits and next work

- No new DD plasma validation, OpenMC transport or mechanistic pump/purification calculation. He3 overall recovery is still a lumped assumed bound, not a measured equipment yield.
- One seeded synthetic daily outage pattern is not an uncertainty distribution or calibrated repair-duration model. Source duties and availability are inherited assumptions.
- No recipient project cancellation after reservation, fuel return, shipping-container limits, storage capacity limits, contractual internal price or shared external-finance limit has yet been modeled. Finance readiness is a per-project permission and can have independent timing inputs.
- The default sequential qualification rule may be more restrictive than the originator ultimately intends for parallel rollout. It is preserved alongside the relaxed case so that any later decision is explicit.
- Initial bootstrap campus is permitted as the research seed; strict evidence mode blocks successors, not that initial research scenario. The simultaneous control explicitly injects initial T into every campus and cannot be presented as deuterium-only bootstrap.
- Current full-cost readiness remains unresolved. In strict mode a positive incomplete financial screen is not substituted for missing evidence.

Next useful steps are parameter sensitivity over build duration/parallel capacity/qualification window, repeated seeds, transport and cancellation/return controls, and evidence-based physical/installed-cost improvements. Do not fit a favorable exponential curve and call it validation.

## Provenance and sources

Scientific and equipment bibliography: [white paper v2.1](../white_paper_v2_1_2026_11_01/WHITE_PAPER.md), including CFS ARC, Meschini et al. fuel-cycle precedent, ASIPP pump announcement, patents, primary market announcements and their transfer limits. No external measured input was invented for this release. PARENT_PROVENANCE.json pins the inherited kernel source hash. Source/code/input hashes and resolved per-case overrides are recorded with execution. Earlier releases remain unchanged.

Research labels: SOURCE-TRACED for that prior evidence; VERIFIED-DERIVED for arithmetic and conservation checks; POTENTIAL-DERIVED for conditional rollout; UNRESOLVED for physical sustainability, qualified product, financing offers, complete profit and general growth laws. All physical G1–G5 remain OPEN.
