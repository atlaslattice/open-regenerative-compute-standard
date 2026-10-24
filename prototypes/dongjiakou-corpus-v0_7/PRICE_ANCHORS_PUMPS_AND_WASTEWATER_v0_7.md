# USD component references, pumping and wastewater boundaries

Version 0.7, October 24, 2026. Screening model. Passing software tests validates bookkeeping, not treatment performance.

## Side-by-side comparison requested

`results/component_price_comparison.csv` compares the same named components and units across three columns:

1. DeepSeek USD reference, converted at an explicitly assumed CNY 7.25/USD.
2. An initially identical Atlas Lattice provisional USD reference. This copies the proposed component reference; it is not a supplier selection or installed quotation. Pump/ERD configuration remains pending clarification.
3. Corpus matched component USD price. This remains null unless a documented like-for-like component, quantity, unit, duty and supply scope match is confirmed. A published whole-plant or combined piping/equipment budget cannot fill a membrane-element or pump-package price.

Ranges remain low/high without invented midpoints. Equipment prices, package budgets, OPEX and product sale prices have distinct classifications and must not be summed. All actual quotations and actual Atlas installed costs remain null. Historical Corpus estimates are preserved separately.

The component ledger now has `china_equipment_anchor_usd`, low/high range columns, anchor IDs, source status and `actual_quotation_usd`. Its alternative cost slots also cross-reference the new wastewater and biological modules instead of leaving them only in inputs.json.

## Source status and price examples

All 27 newly supplied records are labeled **NEEDS SOURCING URLS**, attributed to the user-supplied DeepSeek response of October 24. No missing URLs were invented. Original currency, units, claimed services, date where given and limitations remain visible. This label is a verification task, not confirmation that the price or performance has been substantiated. No new reference enters the priced baseline automatically.

| Attributed reference | USD at assumed FX | Scope still needed |
|---|---:|---|
| Chinese SWRO membrane commercial listing | $275.86/element | Exact model, tax, freight, services |
| Chinese pilot ceiling, Longmo | $539.31/element | Source notice, comparable duty and services |
| Chinese pilot ceiling, OriginWater | $628.28/element | Source notice, comparable duty and services |
| Tangshan NF pumping package | $1.447 million | NF is not automatically SWRO; counts/duties |
| Tangshan RO pumping package | $2.445 million | Phase, pump duties, motors/drives, metallurgy |
| Harbin ERD reference | $270,344.83/unit | Whether capacity refers to feed, reject or product |
| Small industrial MVR project budget | $1.620 million | 5.5 t/hour duty; equipment versus project scope |
| Struvite package range | $117,241–303,448/package | 100–500 m3/day side-stream feed and chemistry |
| Chinese struvite comparison mean | $154,482.76/package | Claimed 200 m3/day comparison needs original evidence |
| Imported struvite comparison mean | $285,517.24/package | Not a Chinese-manufacture price; same-scope test needed |
| Ammonia stripping package | $24,828–38,621/package | Capacity, capture scope, storage and handling excluded/unknown |
| Food-waste digestion, claimed 2025 capacity rate | $8,000 per tonne/day of capacity | Different feed from municipal sludge |

These are reference scopes, not interchangeable installed systems. Membrane vessels remain separately unpriced. The cited domestic/imported membrane and struvite figures are China-market comparisons, not a US-versus-China installed-price test. Exact product purity, domestic-content and time-trend claims remain leads awaiting their original evidence.

The sludge figure CNY 180,000 per tonne retains an **unclear capacity denominator**; it cannot be multiplied by daily sludge production until the source establishes whether it means cost per tonne/day of capacity. Digester volume in m3 is not feed capacity in m3/day.

Ammonia stripping/recovery is a separate cost slot from ammonia storage, handling and dosing. Purchasing ammonia does not require a stripping unit; recovering ammonia does require its own feed and capture design.

## MVR correction

Using DeepSeek's stated budget and assuming 5.5 tonnes/hour is applicable treatment capacity over 24 hours:

- CNY 11.745 million / 132 tonnes/day = approximately CNY 88,977 per tonne/day capacity.
- Linear application to 153,643 tonnes/day gives approximately **CNY 13.67 billion**, or **USD 1.886 billion** at the assumed FX.

This is an arithmetic exposure illustration, **not a lower bound, upper bound or feasibility verdict**. The small project's capacity may describe evaporation rather than feed flow. The feed/evaporation distinction, salinity, preconcentration, crystallization, redundancy, availability, reagent balance and economy of scale require engineering. Mineral removal does not automatically remove residual water or evaporation duty. Do not apply an equipment budget as a guaranteed turnkey ZLD price.

## Can one pump handle wastewater and ocean water?

Potentially the same qualified pump design or family can cover multiple duties, but fluid name alone is insufficient. Required flow/head curves, metallurgy, seals, solids/rags, viscosity, temperature, oxygen, chloride, abrasives, suction conditions, efficiency range and cleaning determine suitability. The cited Xylem paper and seawater-pump tutorial support media-specific materials selection; neither approves a universal dual-service pump.

- A seawater intake pump and raw-sewage/sludge pump usually need different hydraulic and materials checks. Raw sewage may require non-clog solids passage; seawater imposes corrosion demands. A clean-feed high-pressure RO pump is a different duty again.
- A tee on one discharge can serve multiple compatible users of the **same fluid**, after flow/head/control analysis. It does not let the same wet end move seawater and sewage independently at the same time.
- A switched shared standby might be engineered if the manufacturer approves both services and isolation, flushing, contamination control, downtime and reserve capacity are acceptable. No such approval exists in this model.
- More plausible initial standardization is shared pump houses, maintenance, tested pump families, spares and control-system design while retaining separate wet ends and fluid circuits. Each circuit still needs suitable drives/protection; shared infrastructure is not automatically cost-free.
- Treated reuse-water RO and SWRO have different salinity/pressure duties. Do not assume operating a lower-pressure reuse train through SWRO high-pressure equipment is economical.

Pump prices and ERD prices are not interchangeable. ERDs recover pressure from the relevant high-pressure stream, often concentrate. A device described as 10,000 m3/day cannot be counted from finished-water output until its rating basis is established. There is no justified eleven–twelve-unit procurement or sharing saving in the baseline.

## How much Corpus wastewater, including industry?

The city's undated wastewater-service/pretreatment document reports **28 MGD average across six municipal plants**. It explicitly covers residential, commercial and industrial wastewater entering the city system. Therefore industrial sewer flow is already inside that figure; it must not be added again.

This does not establish the total for industrial facilities treating and discharging their own process water outside the municipal system. A TCEQ CITGO package illustrates a 3.5 MGD daily-average permit figure, but a permit/application flow is not an actual measured flow and cannot be added to 28 MGD. Industrial use, wastewater discharge, internal recirculation, once-through cooling and stormwater are different quantities.

The required regional calculation is municipal measured flow plus distinct directly managed industrial actual flow, minus any overlap, using a consistent year and geographic boundary. Both direct-industrial actuals and overlap are unknown here, so the regional combined total remains null. No actual unallocated recoverable volume is established.

The 16 MGD announced reuse program is a use of wastewater, not a separate additional source to be added to municipal 28 MGD. Existing Valero allocations and other contracts remain in the counterfactual. Actual recovery requires flow time series, quality, rights, existing uses and end-user specifications.

## Review findings now foregrounded

The final-effluent struvite case demonstrates low ammonium **at that sampling location**; 42 kg/day is not Greenwood's plant-wide nutrient-recovery potential. Existing side-stream scenarios remain hypothetical. Actual side-stream composition and flow are null. External ammonia is optional; it is not proven necessary for an upstream recovery design.

Existing digester-dependent biogas/centrate routes require reconciliation with the city's planned elimination of anaerobic digestion. Other biological modules do not all depend on that existing asset. New digestion or third-party nutrient sources require separate design, cost and inventory. Bioreactors remain a central design layer, not a claim of an available municipal digester.

The concise nutrient summary leads the review; the complete 54-row ammonia grid remains available. New physical-flow modules and reference prices do not establish installed cost savings. The quantity table remains a template, not engineering takeoff evidence. Both raw-water/desal budgets and additional lattice costs remain distinct. Environmental gates and actual import displacement are unchanged.

## Current status

86 bookkeeping tests pass. Reference-column equality, explicit FX, no midpoint fabrication, match-or-null Corpus rules, non-additive price types, MVR arithmetic, wastewater overlap and no automatic shared-pump credit are tested. Actual installed cost, current regional wastewater total, source URLs for new price claims, vendor duties, footprint and physical performance remain unresolved.


## Follow-up: independent process blocks and train scenarios

DeepSeek's latest pump response supports investigating separate seawater and advanced-reuse blocks divided into parallel trains. We adopt this as an architecture candidate, not a confirmed two-30MGD procurement. The actual reuse block capacity remains null. No large-project pump package is reclassified as an upper bound.

At30MGDfinishedwater and assumed47.5%ROrecovery, the seawaterROfeed is63.16MGD. A separate30MGDreuseproduct block at assumed90%recovery needs33.33MGDfeed. These are different hydraulic and pressure duties, not two identical30MGDpumps. With pressure-exchanger arrangements, the main high-pressure pump may carry only part ofROfeed; its actual duty stays unknown. The city's reported28MGDmunicipalaverage does not establish33.33MGDavailable feed. Separate industrial actuals may add sources, but remain unquantified.

Scenarios include8/16/30MGDreuseproduct blocks,3/4duty trains perblock and0/1complete sparetrain. Three equal-duty trains with no spare lose one-third of output when one is down. A complete standby train is different from merely providing a spare pump. Shared power/intake/header/control failures still require reliability analysis.

The Danfossmanufacturer page confirms a wastewaterAPPWHCfamily up to120bar and parallel coupling. This supports multi-application platform families, not automatic approval of the same pump across rawsewage and seawater, nor its suitability as one giant municipalpump. DeepSeek's specificCarlsbad/Tianjinpumpcounts,87%efficiency and124barvariant claims still need sourcing URLs. A shared same-fluid header remains a scenario; its net reliability depends on backup and isolation rather than being universally worse.
