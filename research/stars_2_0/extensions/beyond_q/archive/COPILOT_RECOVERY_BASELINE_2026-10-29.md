# BEYOND Q

## D-D / D-T ARC Delta Recovery White Paper

**Recovered research handoff for Git-based continuation • 29 October 2026**

**STATUS: RECOVERED WORKING RECORD — NOT VALIDATED ENGINEERING DESIGN**

## Executive recovery note

This document reconstructs the D-D / D-T ARC work recoverable from the prior “Beyond Q” conversation.

It is deliberately a delta ledger rather than a claim of independent verification.

Numerical statements below are separated into:

1. published-source anchors reported in the recovered thread;
2. cross-model derived estimates; and
3. explicit author/editorial decisions.

The purpose is to give a Git-capable collaborator a compact, auditable starting point without silently promoting estimates into facts.

## 1. Recovered architecture

The recovered work converged on a paired-reactor concept:

- an ARC-family D-T power unit; plus
- an ARC-derived D-D isotope/refinery unit.

Earlier discussion also treated D-D as a refinery that can produce tritium and helium-3, with the tritium potentially feeding the D-T side.

The D-D neutron branch was discussed as a possible secondary lithium-breeding enhancement, but explicitly as optional and engineering-dependent rather than free output.

## 2. High-confidence editorial deltas

### Remove dual-DT comparator as a core paper section

**Recovered direction:** The author explicitly judged the dual-DT comparison not relevant to the paper. Retain only if useful as an appendix/sensitivity benchmark.

**Status:** DECISION

### Use campus CAPEX directly

**Recovered direction:** Shift effort toward verifying the integrated D-D/D-T campus CAPEX with citations instead of building the narrative around a conventional dual-DT comparison.

**Status:** DECISION

### Retain hyperscaler use case

**Recovered direction:** Keep the point that Microsoft/Google-scale users could retain a large fraction of isotope production for campus needs and other applications rather than assuming all product is sold into today's specialty market.

**Status:** DECISION

### Reframe genre

**Recovered direction:** The author observed that the work was evolving toward a pitch/engineering proposition rather than a conventional research paper because the remaining central hypothetical was whether the architecture raises the ceiling for quantum computing.

**Status:** DECISION

### Do not use $1B as the adaptation delta

**Recovered direction:** The recovered cross-model analysis explicitly rejected a $1B “retrofit/module swap” interpretation and proposed a much smaller incremental D-D adaptation range.

This still requires source reproduction before promotion.

**Status:** DERIVED / VERIFY

## 3. ARC commonality and modularity delta

A recovered cross-model synthesis tied the paired-reactor concept to Sorbom et al. (2015), citing ARC demountable magnets and removable vacuum-vessel architecture as the engineering basis for substantial platform commonality.

The thread labeled:

**~85–90% plant-level commonality**

as **DERIVED** rather than a published D-D study result.

It separately reported that:

- more than 95% of the Fusion Power Core cost/mass was permanent shared hardware; and
- the replaceable inner vacuum-vessel cartridge accounted for under 3%.

These percentages must be reproduced from the cited cost/mass table before being used as established values.

## 4. Recovered D-D adaptation cost stack

### Replaceable inner VV + divertor cartridge

**Recovered scope:**

- approximately 65–90 t;
- Inconel 718;
- Be multiplier;
- W divertor;
- custom D-D exhaust baffling.

**Recovered estimate:** $35M–$75M per cartridge

**Evidence state:** Cross-model derivation attributed to Sorbom §6.3/Table 11; verify.

### Auxiliary RF heating/current drive

**Recovered scope:**

Retuned ICRF plus proposed +30–50 MW LHCD/ECRH for sub-ignited D-D control.

**Recovered estimate:** +$90M–$175M

**Evidence state:** Benchmark-derived; source reproduction required.

### Divertor cryopumps/exhaust

**Recovered scope:** Higher-conductance helium/hydrogen handling.

**Recovered estimate:** Recovered thread truncated before complete figure.

**Evidence state:** UNRESOLVED

### Overall incremental D-D adaptation

**Recovered scope:**

Bundle of:

- cartridge;
- heating;
- exhaust; and
- isotope-handling changes.

**Recovered estimate:** ~$50M–$350M stated range

**Evidence state:** DERIVED; do not treat as validated.

### Important correction

The recovered conversation itself recognizes that the isotope-extraction allowance may be undervalued.

A Git continuation should therefore expose isotope-separation CAPEX as an independent sensitivity variable, not bury it inside the retrofit delta.

## 5. Recovered campus financial model

### D-T Unit B

**Recovered value:** 525 MW fusion; ~200 MWe net baseline used in model.

**Classification:** Reported as foundational ARC baseline; verify exact net-electric basis.

### D-D Unit A

**Recovered value:** 25 MW D-D fusion / 105 MWth / about -40 MWe net.

**Classification:** Scenario assumption / derived model.

### Integrated campus net export

**Recovered value:** ~160 MWe

**Classification:** Derived from scenario.

### D-T chassis assumption

**Recovered value:** $2.8B

**Classification:** Model assumption / citation required.

### D-D chassis assumption

**Recovered value:** $2.8B

**Classification:** Common-platform assumption.

### D-D adaptation

**Recovered value:** +$150M in the tabulated scenario.

**Classification:** Scenario point inside broader recovered range.

### Turbine downsizing credit

**Recovered value:** -$200M

**Classification:** Scenario assumption; verify.

### Dedicated isotope separation

**Recovered value:** +$120M

**Classification:** Scenario assumption; author suspected possible undervaluation.

### Integrated initial capital

**Recovered value:** $5.87B

**Classification:** Derived table total.

### Premium vs two $2.8B units

**Recovered value:** +$270M

**Classification:** Comparator arithmetic from recovered scenario; comparator removed from core narrative.

## 6. Fuel-cycle deltas from the preceding work

### D-D as “tritium refinery”

D-D was not merely a He-3 farm in the working architecture.

Direct D-D branches were treated as producing T and He-3 coproducts.

**Status:** ARCHITECTURE

### Feed tritium to D-T

Recovered discussion proposed routing D-D-produced T back to the D-T reactor.

**Status:** HYPOTHESIS / SYSTEM DESIGN

### Lithium blanket decoupling

A stronger version proposed reducing/removing dependence on D-T in-situ lithium breeding if refinery supply is adequate.

This is not demonstrated and must be modeled with:

- inventory;
- losses;
- reserve; and
- startup requirements.

**Status:** HIGH-RISK CLAIM / TEST

### D-D neutron “pays rent”

2.45 MeV-class D-D neutrons were discussed as potentially feeding 6Li(n,t) breeding.

The thread itself cautioned that practical contribution depends on:

- moderation;
- enrichment;
- geometry; and
- recovery.

**Status:** OPTIONAL ENHANCEMENT

### 7Li contribution

The thread contained conflicting/nuanced threshold discussion and should not be promoted without original nuclear-data verification.

**Status:** OPEN

## 7. Product-value and quantum-compute framing

The thread moved away from treating today's helium-3 specialty market as the sole economic justification.

Earlier analysis warned that large production could swamp the existing market.

The later Beyond Q direction instead emphasized strategic internal consumption by hyperscalers and other applications.

The recovered author decision was to keep this internal-use framing.

Any economic model should therefore distinguish:

1. external sales;
2. internal avoided-cost/value;
3. inventory stockpiling; and
4. unpriced strategic uses.

It should not assign all isotope births current spot value.

## 8. Evidence-control rules for the Git handoff

Apply the project-wide four-gate evidence standard already adopted by Atlas Lattice:

**SOURCE-TRACED → SOURCE-REPRODUCED → CALIBRATED → VALIDATED**

Model changes made after blinded results require a new blind validation.

For this recovered D-D/D-T work, nearly all cost, performance and isotope-recovery numbers should enter Git as candidate/derived until their primary sources are reproduced.

### ARC modularity/removable VV

**Provenance:** Sorbom et al. 2015 citation reported in thread.

**Current gate:** SOURCE-TRACED candidate

**Next artifact:** Recover exact passages/table rows.

### 85–90% plant commonality

**Provenance:** Derived from ARC component structure.

**Current gate:** DERIVED

**Next artifact:** Publish calculation notebook + assumptions.

### >95% FPC shared / <3% VV

**Provenance:** Reported derivation.

**Current gate:** DERIVED

**Next artifact:** Reproduce from Table 11.

### $35–75M cartridge

**Provenance:** Reported derivation.

**Current gate:** DERIVED

**Next artifact:** Rebuild cost escalation/fabrication multiplier.

### $90–175M RF/CD

**Provenance:** Benchmark-derived.

**Current gate:** DERIVED

**Next artifact:** Identify primary benchmark sources.

### $120M isotope separation

**Provenance:** Scenario assumption.

**Current gate:** UNSOURCED / sensitivity.

**Next artifact:** Build bottom-up separation-train estimate.

### 25 MW DD / 105 MWth / -40 MWe

**Provenance:** Scenario operating point.

**Current gate:** MODEL

**Next artifact:** Freeze plasma/wall-plug assumptions.

### $5.87B campus

**Provenance:** Arithmetic scenario result.

**Current gate:** MODEL

**Next artifact:** Version inputs and sensitivity ranges.

## 9. Suggested Git artifact structure

- `research/beyond_q/README.md`
  - architecture, scope and status

- `research/beyond_q/deltas/DT_DD_ARC_DELTA_LEDGER_v0_1.md`
  - recovery ledger in machine-friendly prose

- `research/beyond_q/models/campus_capex_v0_1.csv`
  - every CAPEX line item, low/base/high, units, source ID and evidence gate

- `research/beyond_q/models/isotope_mass_balance_v0_1.csv`
  - D input, branch yields, T/He-3 birth, recovery, inventory and losses

- `research/beyond_q/evidence/ARC_SOURCE_MAP_v0_1.md`
  - exact page/section/table identifiers and values

- `research/beyond_q/tests/`
  - reproducible checks for arithmetic, units, stoichiometry and sensitivity

- `research/beyond_q/whitepapers/BEYOND_Q_DT_DD_ARC_v0_1.md`
  - narrative white paper built only from gated entries

## 10. Priority unresolved questions

1. What D-D plasma operating point can an ARC-derived machine actually sustain, and at what wall-plug power?

2. What fraction of born T and He-3 is recoverable at required purity and inventory latency?

3. Does D-D operation truly extend replaceable-vessel lifetime relative to the D-T duty cycle assumed in the recovered model?

4. What isotope-separation train is required and what is its realistic CAPEX/OPEX?

5. How much D-T blanket functionality can safely be reduced, if any, after startup/reserve/failure cases are included?

6. What is the minimum useful D-D refinery size when optimized for T supply, He-3 production and electricity consumption rather than symmetric reactor scale?

7. What internal helium-3 demand cases for quantum computing are technically defensible without assuming future market size?

## 11. Source/provenance pointers recovered from the thread

Primary citation named in the recovered conversation:

B. N. Sorbom et al.,
“ARC: A compact, high-field, fusion nuclear science facility and demonstration power plant with demountable magnets,”
Fusion Engineering and Design 100 (2015) 378–405.

DOI reported in thread:

`10.1016/j.fusengdes.2015.07.008`

Open-access preprint reported as:

`arXiv:1409.3540v2`

The thread pointed specifically to:

- Section 2 / Figure 3; and
- Sections 6.1–6.5 / Table 11.

This recovery document itself did not independently reproduce those passages.

## Conversation provenance

Recovered from the prior Beyond Q Copilot thread on 29 October 2026.

This recovery intentionally preserves the distinction between:

- what the author decided;
- what other models proposed; and
- what published literature was said to contain.

## Handoff instruction to GPT / Git maintainer

Treat this document as an archaeological recovery packet, not canonical truth.

Preserve every recovered value with its evidence state.

Do not overwrite prior versions.

For each quantitative claim, create a source receipt and a reproducible calculation before promotion.

Where the recovered thread is truncated, mark the field **UNKNOWN** rather than filling it by inference.
