# ORCS v2.5 — Four-way desal comparison, combined membrane/LNG cold cascade, and Delek Tyler suitability
2026-10-15 | ADDITIVE RESEARCH · NOT COMMISSIONED · ZERO REALIZED CREDIT

## Four mutually explicit alternatives, identical feed/outlet specifications
A. Caofeidian-type ultrafiltration and nanofiltration (remove Ca/Mg scaling salts), then staged reverse osmosis to concentrate reject and recover water. Real Sanyou industrial trial; not verified freeze.
B. Reverse osmosis with electrically-driven freezing/ice washing/melting of residual brine, then conditional mineral recovery; no imported LNG cold assumed.
C. RO brine with LNG receiving-terminal regasification cold-assisted ice crystallization, wash, melt, mineral liquor separation; thermal availability and safeguards unverified.
D. Hybrid: Caofeidian UF/NF selective Ca/Mg stream isolation + staged RO water recovery, then freeze-concentrate RO reject using usable LNG *subzero* cold, and separately allocate warmer remaining cold to data-center cooling, with server waste heat potentially supplying ice melting. Do NOT physically force ice crystallization after an already-warmed data-center chilled-air loop. If cooling the data center first is required by location/process, the freeze block needs a separately reserved cold branch, cold thermal storage, or powered refrigeration. The warmed CDU return cannot be assumed < freezing-point brine.

## Thermal architecture
LNG receiving/regasification -158C -> segregated engineered indirect heat exchangers, controlled chemical/gas safe distances
 cold branch A: cryogenic ASU/possible ORC as justified by measured temp and economics
 cold branch B: isolated freezer coolant below actual ice-onset freezing-point and exchanger approach -> crystallization, ice washing; concentrated mother liquor -> brine ion assay -> Mg/gypsum/K/Br/NaCl grade-specific offtake
 cold branch C: warmer residual cooling -> data center chilled-water/CDU HVAC where co-located and thermally/electrically feasible
 data-center heat or refinery waste heat if appropriately integrated -> ice-melting or feedwater heat transfer, not cryogenic freezing.
Energy balance MUST allocate each kWh thermal cold by temperature/exergy grade and account for storage, intervals, temperature pinch, line losses, refrigeration backup, pump/fan energy, corrosion and chemical contamination. In reality some configurations may use separate *parallel* branches because demands and exchanger thermodynamics conflict.

## Evidence
- Sanyou Caofeidian Chinese May 2026 reporting: membrane UF/NF hardness removal, four-stage RO, not documented freezing. Source: https://finance.sina.com.cn/jjxw/2026-05-07/doc-inhwzfcv5433395.shtml
- Prior physical engineering narrative preserved at docs/notion-mirrors/2026-10-12-dongjiakou-lng-cascade-v05.md; Chinese LNG ORC power/HVAC and proposed ASU actually separate projects; freeze brine not commissioned.
- Peer-reviewed simulation LNG regas cold + data center, not plant measurements: https://www.sciencedirect.com/science/article/pii/S0360544223018753
- 2026 LNG/multigeneration freeze desal study: https://www.sciencedirect.com/science/article/abs/pii/S0196890426004413
- Real freeze desal/washing study: https://www.sciencedirect.com/science/article/pii/S0043135416304845
- Recent LNG cold energy technical review: https://www.sciencedirect.com/science/article/pii/S0360544226016269

## Delek Tyler refinery - no identified preexisting LNG cold resource
Delek US 2024 10-K reports Tyler a light/sweet crude processing refinery, main processes crude/vacuum distillation, naphtha reforming, diesel/naphtha hydrotreating, FCC, alkylation and delayed coking. Its product mix includes gasoline, distillates, LPG and coke. Official published infrastructure does NOT identify an LNG import/regasification cryogenic cold stream. A normal natural-gas feed pipeline transports gas, NOT regasifying LNG; refinery propane refrigeration if present is an energy CONSUMER, not free LNG cold.
- SEC 2024 report: https://www.sec.gov/Archives/edgar/data/1694426/000169442624000028/dk-20231231.htm
- Official Delek assets https://www.delekus.com/business-operations/refining/refining-overview/default.aspx
- 2026 Oct 13 announced DPA-linked refinery expansion reports do NOT include LNG regas/cold integration nor final added barrels/day https://www.reuters.com/business/energy/trump-administration-expand-delek-texas-refinery-using-defense-production-act-2026-10-13/
Recommendation: Tyler priority could be waste-HEAT capture, steam/cooling loop optimization, sulfur recovery/acid reuse assessment, refinery wastewater/reuse, refinery throughput and delivered-fuel logistics. Brine mining at Tyler requires measured saline reject, a proven desalination plant and market, all unverified. An LNG cold cascade at Tyler would require building/importing costly cold infrastructure or separate mechanical refrigeration; characterize as NEW PROJECT not EASY RETROFIT.
Do not confuse Tyler CITY refinery with unrelated 'Tyler County' cryogenic gas-processing plant; no geographic thermal connection is implied.

## Experimental comparison metrics
Same 1000m3 incoming reject per test, same salt concentration/chemistry, product water salinity, residual discharge and availability requirements. Compare A, B, C, D: incoming brine m3, usable recovered water, outlet dissolved/solid minerals by ion and proper exclusive mass balance, qualified products, pump kWh, cold duty MWth/quality/availability, electricity kWh, heat recovery, capex annuity + OPEX + discharge costs, environmental effect, contracted offtake and revenue net of logistics. Count cold twice only as loss; never double-credit data-center chiller savings and ice freeze cold from same thermal stream. Run cold-unavailable season and backup power cases.
## Gate
Freeze module design only applicable to a genuine LNG receiving/regas terminal or other proven deep-cold source. U.S. export/liquefaction terminals *consume* refrigeration. Tyler refinery does not qualify as an obvious cold source based on documented plant units. Revisit if a real cryogenic stream, stable cold duty, and physical integration contract emerges.