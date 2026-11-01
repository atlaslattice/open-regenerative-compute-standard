# Beyond Q v2.0.1 — independent review reconciliation

2026-11-01. Review provenance: DeepSeek critique supplied by Dave; GPT Work source-code/data reconciliation. This adds disclosure and display outputs; v2.0 model.py, finance.py and inputs.json remain unchanged. No physics was tuned to make the review pass.

## Findings

| Review claim | Source check and disposition |
|---|---|
| There is no DT stage or DT consumption in the data | Incorrect for the implementation. The raw module ledger contains a_burn, b_burn, b_birth, a_transfer, b_recirculated and independent A/B schedules. The old aggregate dashboard hides much of this. ACCEPT presentation gap; add explicit reactor-stage rows and a two-reactor display. |
| Equal B breeding and B burn means A is not a factory | Incorrect inference. B gross TBR=1 is an explicitly requested replacement scenario; A's direct DD source is separate. Recovered B fuel is less than gross births when losses occur. Gross TBR1 never establishes operational self-sufficiency. |
| The flat export cap is an unmodeled source | Incorrect. Actual withdrawals are min(available B storage above reserve, module cap), then limited by fleet cap. Withdrawals are subtracted from storage and included as sinks in conservation. A saturated cap can be flat without being a manufactured source. |
| He3:T co-production ratio is 7:1 | Wrong denominator. The critique compares direct He3 births in A to blanket T births in B, during B's partial startup year. Equal-DD-branch comparison is He3_A_birth versus T_A_DD_birth. Their atom ratio is 1; their mass ratio differs only by isotope molar masses. No factor-seven unit correction is warranted. |
| T decay is absent, and stocks are fiction | Incorrect for model and raw CSV; accepted aggregate disclosure gap. Decay is advanced in each T compartment with ln(2)/(12.32*365.25) per day. Year-one decay is 2.964505 kg. Add aggregate T_decay_kg and a visible balance. |
| A must have T_consumed=0 | Incorrect whenever modeled secondary DT is enabled. A's born T can burn internally; this creates He4 and a DT neutron, and cannot also be delivered. The improved stage view displays this consumption explicitly. |
| Fleet must equal 50 times the single trajectory | Incorrect for this scenario. Fleet commissioning, independent permissions, correlated outages, replacements, per-module stocks and a shared 100 kg/year T export cap differ from the single trajectory. A separate synchronized-identical control would be needed for a multiplication identity. |
| Large unsold He3 inventory is hidden | ACCEPT. At 75% recovery / requested prices / capped offtake / 50 modules, year-60 bank is 890,924,155 STP L. This deserves a visible metric. It is not evidence of measured global demand: 350k L is a chosen fleet-wide stress cap. |
| Market absorbs only 0.03% | Not supported by matched rows. At 75% / year60, 350k divided by 31.787 million L total candidate is ~1.10%; after the 50% internal allocation it is ~2.20% of that year's available sale allocation. At 37.5%, the corresponding shares are ~2.20% and ~4.40%. Banked stock can also supply sales, so annual cap/output is not itself an annual stock-flow identity. |
| Delivered dashboard was truncated | Not reproduced for generated file. The original complete dashboard contains 1,440 closed JSON records and its JavaScript parses. A copied/pasted version may have been truncated externally; do not infer source corruption from a partial transfer. |

## Year-one source reconciliation, one module

All quantities below are kg of the named isotope, unless stated otherwise:

- A DD tritium births: 121.04130904279312 kg T.
- A DD He3 births: 121.04050800401671 kg He3.
- He3:T DD atom-birth ratio: 0.9999999999999988 (roundoff from the assumed equal branches).
- A secondary T consumption: 6.314544339169696 kg T.
- B DT consumption: 17.13050154709158 kg T.
- B gross blanket births: 17.13050154709158 kg T (assumed gross TBR=1).
- A to B storage transfer: 108.44753454564972 kg T (internal flow; not another source).
- T decay: 2.964505424555794 kg.
- Processing losses: 5.763100943699317 kg.
- Permeation: 0.0000139944224765 kg.
- Conditional terminal exports: 20 kg, debited from storage.
- Final campus T inventory: 85.99914434094279 kg, starting from zero.

Thus 0 + A births + B births - A burn - B burn - decay - processing loss - permeation - exports = final inventory. B gross birth/burn cancellation does not eliminate A's direct production.

## Changes made

`audit.py` reads the unchanged v2.0 physical module CSVs and product/financial CSV. It produces an enriched annual CSV exposing A DD births, A secondary consumption, A→B transfer, decay, loss, stock change, correct DD atom ratio, B gross TBR and separate A/B plasma He4 births. It also produces per-reactor stage rows with explicit stage role, direct and blanket birth, burn and internal transfers. Per-reactor loss allocation is not exported in the parent raw data; it remains null rather than being invented or assumed zero.

The stage electrical screen is reconstructed from actual B burns and on-time, A on-time, existing prescribed loads and the unchanged inputs. A/B stage nets plus the separately allocated shared processing load reproduce parent module net MWh. These remain prescribed electrical sensitivities, not reactor heat-conversion validation.

The new self-contained dashboard exposes fleet, recovery, price AND offtake selectors; all four actually filter the data. It has a high-DPI canvas, year inspection, banked inventory, gross imports, decay and the two-reactor flow table. Missing profit remains unresolved. It distinguishes conditional sale allocation from actual sales. It does not include the review's proposed false unit-error alarms or replace B breeding with A production when the latter is unavailable.

## Rejected code fallbacks

Do not use `T_gross_birth_kg ?? T_B_gross_breeding_kg` to check DD coproducts; those sources are physically different. Do not call birth-minus-burn-minus-export a full surplus while omitting decay, processing/permeation and inventory boundaries. Do not label the stock line decay-free. The supplied replacement HTML also initializes RAW as an empty placeholder and its filtered() function ignores the price/offtake selects despite wiring change events. The corrected dashboard embeds the actual data and filters every selector.

## Reproduction and limits

From `module_fleet_v2_0`: `python run.py`. Then from this directory: `python audit.py` and `python -m unittest test_audit -v`. Outputs are `annual_reconciled.csv`, `reactor_stages.csv`, `checks.json` and `dashboard.html`. Parent hashes are recorded so the reconciliation can be checked without asserting that unchanged arithmetic validates the physics.

The review strengthens the interface and the market-cap stress test. It does not establish a new physical failure of DD coproduct accounting. All G1–G5 remain OPEN; all original source, recovery, outage, qualification, energy and cost caveats still apply. No new experimental or transport result is claimed. Dave/Atlas Lattice retains research-direction credit; DeepSeek is credited for the independent review and useful display recommendations, GPT Work for verification and implementation, and earlier GPT-6/Gemini Argon analytical credits remain in v2.0.
