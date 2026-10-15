# ORCS v2.0a reproducible seawater mining screen — computed results

**2026-10-14. This is NOT the full 91-facility network, not actual brine measurements, and not real recovered mineral production.** Only the named, documented existing **78 MGD seawater finished-product capacities** for Carlsbad CA (50), Tampa FL (25), and Santa Barbara CA (3) were counted. A separate **seven-site 192.8 MGD** scenario includes *four proposed projects* (Harbor Island TX 100, Doheny CA 5, Monterey CA 4.8, Laguna Madre TX 5) and is not current supply. The entire remaining brackish network has unmeasured chemistry and is excluded, not treated as zero.

Inputs and explicit screening assumptions: 90% capacity factor, 50% conversion seawater intake to freshwater, negligible desal ion passage, 50% constituent recovery/qualification (entirely hypothetical). USGS normal seawater concentrations [here](https://pubs.usgs.gov/circ/2003/circ1262/) Mg 1350 mg/L, K 390, Br 67, Ca 410, sulfate 2700, Na 10500, Cl 19000. One US gallon=0.003785411784 m3. Calculate annual feed from annual finished water/0.5 and brine as feed minus finished water. Recovered product equivalents from feed-ion inventory and stoichiometric maxima (Ca-limited gypsum, Na-limited NaCl), not individual plant assay. Reagent/co-product changes, impurities, pretreatment losses and process compatibility **unknown**.

**Three operating named seawater plants (78 MGD):**
- Modeled annual brine **96,993,606 m3/y** (96.99 million), not actual surveyed discharge.
- Gross equivalent **gypsum 341,673 t/y; magnesium oxide equivalent 434,270 t/y; potassium oxide equivalent 91,134 t/y; bromine elemental content 12,997 t/y; salt equivalent 5,177,661 t/y**. These are 100% constituent ceilings in model.
- At hypothetical 50% usable capture: **170,837 t/y gypsum; 217,135 MgO eq; 45,567 K2O eq; 6,499 t Br; 2,588,831 t NaCl eq**. No plant presently known to sell these recovered lots.
- Gross hypothetical **price × captured volume = $197.7–388.0 million/year**, using magnesium *unverified* $250–500/t MgO, gypsum *unverified* $35–65/t, industrial salt *unverified* $35–75/t, 2025 USGS bromine import-value benchmark $3,000/t Br, 2025 USGS potash **K2O eq** mine-gate prices $600/t MOP and $1,200/t all product average. This is **not gross revenue, net value or import savings**. Product-grade and contracted demand ceilings not applied, and low-value salt may saturate markets/transport networks.

**Seven operating + proposed projects (192.8 MGD):** additional projects are not operating.
- Hypothetical annual brine **239,748,298 m3/y** (239.75 million).
- Gross equivalent gypsum **844,546 t/y**; MgO **1,073,425 t/y**; K2O **225,266 t/y**; Br **32,126 t/y**; NaCl **12,798,117 t/y**.
- At hypothetical 50% constituent recovery: gypsum **422,273 t/y**, MgO **536,713**, K2O **112,633**, Br **16,063**, salt **6,399,058**.
- Gross price×captured scenario **$488.7–959.1 million/year**. Not committed projects or probable output.

**USGS 2025 import comparison (U.S. total):** gypsum gross imports 6.8 Mt/y; magnesium compounds ~0.640 Mt/y MgO equivalent; potash **5.6 Mt/y K2O equivalent**, with USGS estimated net import reliance **92%**. Thus operating 50%-recovery screen would equal **~2.5% gypsum imports**, **33.9% MgO-compound gross imports**, **0.81% K2O gross imports** if every tonne of product were actually qualified as like-for-like import replacement. **These are theoretical comparison percentages, not proven offsets**, and require product grade and pricing. 20%-consumption reserve at *new* demand scope is separate one-time stock target (gypsum 8.8Mt, MgO compounds apparent consumption 980kt → reserve 196kt, potash consumption 5.9Mt→ reserve 1.18Mt K2O), not a standing annual export ban.

Bromine: USGS 2025 U.S. is already among major producing nations, domestic production withheld, import unit value about $3/kg Br content; without 2025 gross imports/extracted grade in this source module, **national percentage UNKNOWN**. Lithium, iodine, deuterium and other specialty ions may be present but actual site assays, recovery conversion, U.S. imports and qualified spot prices **UNKNOWN**, so dollar credits **zero/undefined**. Deuterium isotope commercial price *not applied* to raw H2O in brine.

***Important discrepancy against older Harbor Island preliminary calculation:*** this physically-conserved model derives ~**0.438Mt/y gypsum equivalent per proposed Harbor Island 100 MGD** at normal seawater Ca 410 mg/L, 50% finished-water recovery, 90% operation. Prior Harbor Island proposed brief used ~**0.733 Mt/y gypsum equivalent** under different assumed design source volumes/chemistry. **Both must be reconciled to actual intake/reject design and calcium/sulfate assays before promoting either number.** The 0.733Mt/y and 0.438Mt/y outputs are not interchangeable; selecting the larger number solely for valuation is inappropriate.

Data source citations:
- [USGS standard seawater chemistry](https://pubs.usgs.gov/circ/2003/circ1262/)
- [USGS 2026 MCS](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf)
- [USGS 2026 Potash chapter](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-potash.pdf)
- [Existing 91 named sites census](ORCS_NAMED_DESAL_GYPSUM_ACTIVATION_CENSUS_V1_9_2026-10-14.md)
- [Executable screen](../../prototypes/orcs-brine-portfolio-v2_0/portfolio_v2_0a.py)

**No deployment, actual brine mining, actual output, cleared import substitution, validated market price for all grades or economic profit claimed.** Net financial feasibility remains UNKNOWN until CAPEX, OPEX, power, disposal, transport and offtake are known.
