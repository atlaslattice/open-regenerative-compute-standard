# Beyond Q v2.5 — engineering coverage, gas conventions and qualification gates

This append-only audit follows commit `156d32353c0655e9d8d487c84aebc1a88ba6abb8`. It responds to the consolidated work order without treating previous code execution as physical validation. Earlier releases, outputs and financial projections are unchanged.

## What was already covered, and what this adds

| Work-order item | Existing coverage | v2.5 addition / remaining limit |
|---|---|---|
| Public full-text search | v2.3–v2.4: publisher/ANS inaccessible; 1980 precursor obtained | Wisconsin bibliography examined directly; no 1982 equations obtained |
| Historical70/80% benchmark | Abstract traced; calibration disabled | Parameter availability matrix below; still not reproduced |
| A1100/B1130 reference | Earlier B1130 option exists; executed v2.2 default B1100 | Explicit B1130 comparison and startup arithmetic; no relabeling old runs |
| Complete recovery chain | v2.4 groups pump and purification responses | Separate species-routing interfaces and disjoint stream ledgers; real coefficients unknown |
| 37.5/75/90% cases | Overall assumed cases preserved | Endpoint scenarios separated from observed capture/assay and synthetic stage tests |
| Financial accounting | Candidate versus actual revenue already separated | Explicit gross/recovered/purified/qualified/allocation fields; costs and actual revenue remain unknown |
| Engineering gates | Physical gates open | Machine-readable PASS/FAIL/UNRESOLVED matrix |
| Branch energies and STP | Correct current mapping and T2 distinction already present | Off-midpoint regression and exact ideal-gas comparison |

This adds an interface model and evidence audit, not a calibrated, continuously operating exhaust plant. Missing process data remain null. Unknown efficiencies are never silently replaced by100%.

## Historical evidence and retrieval limits

Greenspan and Miley, *Deuterium-Based Plasmas as a Source for Helium-3*, Nuclear Technology – Fusion2(1),43–54(1982), DOI [10.13182/FST82-A20733](https://doi.org/10.13182/FST82-A20733). The publisher abstract supports approximate70% recoverability in its driven SCD cases, approximate80% in studied ignited cases, and sensitivity to energy balance. It lists radiation, temperature profiles, ion/electron temperature separation, tritium assistance and external heating as considerations. It provides neither reproducible operating points nor downstream plant efficiency. The full journal text remains inaccessible; earlier HTTP403 and retrieval failures are recorded in v2.4. No new full-text success is claimed.

The explicitly requested Wisconsin document is J.C.Crabb, S.W.White, L.P.Wainwright, S.E.Kratz and G.L.Kulcinski, *Fifty Years of Research in Helium-3 Fusion and Helium-3 Resources*, UWFDM-935, December1993, revised May1994. [Official PDF](https://fti.neep.wisc.edu/fti.neep.wisc.edu/pdf/fdm935.pdf). The134-page PDF was downloaded, text searched and bibliography page visually checked. PDFpage66 contains entries111–112 for the1980 precursor and1982 paper. This is bibliographic confirmation, not a reproduction of their plasma calculation. Its report-number typography/OCR for the precursor differs from the downloaded report header; v2.4's DOE identifier remains authoritative for that file. No operating conditions are inferred from a citation list.

| Historical quantity | Available evidence | Benchmark status |
|---|---|---|
| Plasma regime | Ignited and driven semi-catalyzed deuterium described in abstract | SOURCE-TRACED |
| Temperature, density, profiles | Effects named; numerical points unavailable | UNRESOLVED |
| Particle and energy confinement | No reconstructable values obtained | UNRESOLVED |
| Secondary reaction network / tritium assistance | Considered in study; specific case implementation unavailable | UNRESOLVED |
| Helium-removal definition / timescale | Recovery reported; complete boundary unavailable | UNRESOLVED |
| Energy balance |50/70MeV per recovered atom reported; full normalization unavailable | SOURCE-TRACED summary, reproduction UNRESOLVED |
| Industrial pump, separation and qualified-product yield | Not established by abstract | UNRESOLVED |

The separately obtained1980 precursor is retained as such. Its all-internal-tritium-burn illustration and unreconciled74/26 output split are documented in v2.4; neither is imported as the1982 plasma solution. Progress does not depend on obtaining that journal article: mechanistic calibration may instead use another fully specified and appropriate source.

## Canonical comparison and startup accounting

The requested comparison uses **A1100MW primary DD fusion / B1130MW DT fusion**, with B's lithium blanket audited separately. A remains a hypothetical DD operating target; public DT ARC design work does not establish its feasibility. B1100 is retained as the explicitly labeled matched-power sensitivity used by prior v2.2 runs. Old annual and cascade CSVs continue to describe B1100.

With17.6MeV per DT event,365.25-day FPY, Avogadro6.02214076e23/mol and T molar mass0.00301604928kg/mol, derived burn is56.0490733kg/(GW-fusion FPY).

| B power | Uninterrupted T burn kg/FPY | Historical55.8 convention kg/FPY | One FPY plus illustrative10kg reserve |
|---|---:|---:|---:|
|1100MW matched sensitivity |61.653981 |61.38 |71.653981kg |
|1130MW reference |63.335453 |63.054 |73.335453kg |

These are **VERIFIED-DERIVED** under chosen conventions, not startup-system sizing or an annual uptime prediction. Actual startup must also reconcile pipeline fills, extraction delays and independent schedules. Gross blanket TBR1 would produce gross births equal to burn; it does not establish recovered replacement after losses. No B self-sufficiency claim follows from that assumption. T reserve rules remain distinct from the zero mandatory He3 internal allocation policy.

## Explicit complete-chain interfaces

`engineering_inputs.json` enumerates secondary consumption, plasma exhaust, divertor capture, vacuum pumping, hydrogen/helium separation, He3/He4 separation, purification and qualified storage. DD births are the independently normalized source. Every real stage's species routing, service capacity, energy, lifetime and availability are unknown until sourced.

`routing.py` accepts a packet in moles of nuclei of H,D,T,He3,He4. At each processing stage, input is split into **forward, recycle bank, permanent loss and retained** streams:

\[
n_{in,s}=n_{forward,s}+n_{recycle,s}+n_{loss,s}+n_{retained,s}.
\]

All coefficients are conditional on that stage's input. Forwarded material alone enters the next stage. Recycle is banked once and cannot also be product; this batch interface does not invent unlimited repeated-pass recovery. Unprocessed material remains held during a capacity restriction or outage. An optional numerical service capacity is expressed in mol-nuclei/day and requires a molecular-composition model before it can represent a real gas throughput or vacuum pump rating. It is not equivalent to pump L/s.

Secondary D-He3 consumption removes one mole each of He3 and D per mole reacted and produces one mole each of He4 and H. Baryon and nuclear charge balances are checked. Those balances are not an energy balance: nuclear mass defects, reaction-product transport and deposited heat remain outside this batch interface. No synthetic He4 is added to the existing campus totals.

The reproducible demonstration uses a deliberately **synthetic**100molHe3/100molT/1000molD packet,30mol secondary He3 burn, and hypothetical stage fractions. It is not an estimate of ARC or laser exhaust. `synthetic_stage_ledger.csv` supplies35 species-stage rows; downstream candidate material is held in unqualified storage. Total per-species closure is exact at the recorded precision. Other chemical impurities, molecular speciation, adsorption equilibria and tritium decay during residence are not modeled here; the existing integrated inventory model retains its separate decay accounting. None of this determines a physical feed composition.

T contamination is an explicit tracked species. `assay_screen` reports He3/(He3+He4) atom fraction and T atoms per He3 atom. These are not interchangeable with gas-molecule ppm, activity per volume or complete buyer specifications. User-provided criteria can yield a conditional PASS/FAIL; even a computed PASS is not an observed assay and cannot create actual qualified sales. Buyer criteria and measured batch assays remain null. Unknown non-hydrogen impurities are another unresolved qualification requirement.

Equipment energy, replacement intervals and real throughput cannot be inferred from this routing demonstration. Inputs stay null instead of zero. Stage-specific downtime/capacity effects are supported in the interface and tested with synthetic inputs; measured schedules and capacities remain unavailable. A time-resolved, capacity/pressure-coupled process simulation remains a dependency, beyond v2.4's idealized hold-and-release calculation.

## Product and financial boundaries

The37.5%,75% and90% cases remain hypothetical gross-born-to-endpoint-product potentials. They do not become actual qualified product through relabeling. The gross938967.995STPL/year calculation uses1100MW primary DD and85% **effective** exposure, before separate secondary-burn or process calibration. It is not a rerun of the parent85% macro availability ×93.75% duty schedule.

| Overall assumed potential recovery | Potential endpoint STP L/year | Conditional value at assumed$1500/L |
|---|---:|---:|
|37.5% |352113 |$528.169million |
|75% |704226 |$1.056339billion |
|90% |845071 |$1.267607billion |

These **POTENTIAL-DERIVED** steady-throughput valuations assume product qualification and full sale at the illustrative price; they are neither year-one revenue nor profit. Actual measured recovery, qualified saleable quantity, demand-backed revenue and full-cost profit remain null. The output ledger distinguishes gross births, scenario recovery, purified candidate, qualified product and internal allocation. Zero mandatory He3 allocation does not mean zero secondary He3 burn; the latter is unresolved inside the overall assumption. T recovery and T sales are not derived by applying the He3 fraction to T births.

Do not multiply these overall fractions by the explicit stage demonstration again. v2.4's conditional feasibility table still applies: an assumed70% plasma survival cannot produce75% overall, whereas37.5% overall would require53.57% downstream yield. That is a **FAIL for that conditional target combination**, not a universal reactor failure or a validated survival limit. No empirical probability distribution or confidence interval is justified. With wholly unknown stage yields, the physical bound spans zero to source availability; planning sensitivities are not statistical uncertainty bounds.

The historical$300million adaptation allowance, chassis estimates and30-year5% financing remain placeholders. Separating process stages does not justify additional or reduced CAPEX. Purification energy must be reconciled against the existing shared-processing allowance before being added; otherwise costs and power could be counted twice. No new campus profit, break-even date or rollout forecast is claimed.

## Branch-energy and volume audit

Correct rounded DD totals are T+p:4.03MeV and He3+n:3.27MeV. Product kinetic energies must not be mislabeled as total reaction Q. At equal branches, the mean is3.65MeV. With T-branch fraction \(f_T\), use

\[
\bar Q=f_T4.03+(1-f_T)3.27,\quad
N_T=f_TN_{DD},\quad N_{He3}=N_{n,DD}=(1-f_T)N_{DD}.
\]

The reviewed active physics files already use the correct mapping; source hashes are recorded. The prior white paper records an older swapped-label issue; this audit does not silently edit that artifact. At the illustrative archived-sample fraction0.48096, correct meanQ is3.6355296MeV; swapped labels give3.6644704MeV and approximately−0.790% source-rate bias at fixed power. This is an arithmetic sensitivity, not a new kinetic benchmark or a universal branch ratio. Equal-branch tests alone would miss the labeling error.

Parent STP is273.15K,101325Pa,22.414L/mol rounded. The ideal-gas value from \(V_m=RT/P\) and the SI gas constant is22.413969545L/mol. At273.15K and100000Pa it is22.710954641L/mol. We report both without changing earlier outputs. These are gaseous reference volumes, not liquid volume or actual operating-pressure volume.

| Parent-reference quantity | Equivalent |
|---|---:|
|350000He3 STPL |47.096023kgHe3 |
|Equal number of T nuclei |350000T-atom-equivalent STPL;47.096335kgT |
|Same T nuclei as pure T2 gas |175000T2 STPL |
|350000molecularT2 STPL |94.192670kgT |

Mixed HT/DT/T2 exhaust requires molecular speciation; pureT2 conversion cannot be assigned to the whole mixture. Every gas-volume output records reference conditions and nucleus/molecule basis. No factor-two ambiguity is used to claim extra fuel or sales.

## Gate decisions

| Gate / check | Status | Evidence or remaining requirement |
|---|---|---|
| Convention/regression software | PASS | Ten checks; branch labels, STP/T2, species closure, custody and unknown handling |
| Synthetic contamination example under stringent assumed criteria | FAIL | Conditional test only; no claim about real process performance |
|1982 full plasma benchmark reproduction | UNRESOLVED | Full equations and numerical operating points unavailable |
|G1: feasible A DD plasma and coupled secondary reactions | UNRESOLVED | A1100MW target and He3/T residence/burn not established by DT ARC or abstract |
|G2: neutron transport, breeding and shielding | UNRESOLVED | Geometry-qualified yields/data/benchmarks still required; B blanket independently audited |
|G3: extraction, pump and isotope-processing performance | UNRESOLVED | Mixed feed, conductance, capacity, cyclic yield, contamination and assay missing |
|G4: integrated inventory, startup and independent downtime | UNRESOLVED | Conservative accounting exists; measured process constraints and real schedules missing |
|G5: complete energy/thermal boundary | UNRESOLVED | DD drive, deposited heat, separations power and shared-load overlap unclosed |
|ARC-compatible retrofit, geometry and service life | UNRESOLVED | Public DT design does not validate DD retrofit or maintenance envelope |
|Qualified products and full-cost economics | UNRESOLVED | Buyer assay, off-take, validated CAPEX/OPEX and lifetime required |

G1–G5 are all open. PASS applies to stated software/convention checks only. Synthetic FAIL demonstrates a functioning rejection path; it does not establish experimental falsification of Beyond Q.

Full sources and retrieval scope are in `sources.json`. Dave / Atlas Lattice retains credit for the isotope-first direction. GPT Work performed this audit and implementation. Earlier GPT-6/Tidal Lantern, DeepSeek and Gemini Argon contributions retain their documented attribution. Citations and published precedents imply no institutional endorsement.
