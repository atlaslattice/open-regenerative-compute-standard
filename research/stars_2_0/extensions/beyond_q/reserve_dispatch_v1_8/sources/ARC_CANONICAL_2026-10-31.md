# Stellar Forge / Beyond Q — ACTIVE TWO-ARC REACTOR DESIGN LOCK

**2026-10-31 | Owner-corrected active research configuration | PROPOSED, NOT CFS-VALIDATED OR OPERATIONAL**

## The architecture (MUST NOT BE MISSTATED)

**TWO separate ARC-class high-field tokamak reactors, each targeting 1.1 GW of GROSS NUCLEAR FUSION POWER (2.2 GW combined).**

| Distinction | A: D–D ARC isotope refinery | B: D–T ARC power unit |
|---|---|---|
| Fusion-power target | **1,100 MW_fusion** | **1,100 MW_fusion** |
| Nuclear fuel | D + D | D + T |
| Purpose | Helium-3 and tritium production; isotope resource economics | Net electricity, with separately accounted tritium breeding |
| Historical electrical projection | **~20 MW_e NET**, owner-reported estimate, not independently validated | **~400 MW_e NET** design comparator from published ARC D–T at ~1.13 GW_fusion; not demonstrated output or exact for 1.1 GW |

**NEVER interpret the 20 MW_e net electricity estimate as 20 MW D–D fusion power.** Earlier calculations that used 20 MW_fusion as A are an archived, distinct sensitivity, not this owner's full-size reactor design. The October 30 commit [dual-laser power-basis lock](https://github.com/atlaslattice/open-regenerative-compute-standard/commit/674eb174ff935bcfc9829109b57c1187d25dc710) captured two 1.1 GW gross fusion source powers but described **LASER reactors**; subsequent owner clarification specifies **ARC-class tokamak reactors** instead. Laser/pulsed WarpX experimental studies are independent research tools or variants, not automatic replacement of the ARC physical platform.

The full-power D–D conversion is **hypothetical**. ARC D–T design publications do not establish a feasible 1.1 GW D–D operating point, required heating, confinement, wall-plug efficiency, neutron loads, engineering viability or He-3/T separation yield. B is likewise a published design, not a currently operating commercial ARC plant.

## Modularity, mass and PRICE — THREE DISTINCT QUANTITIES

**Known source architecture:** The published ARC design incorporates demountable magnets and a replaceable vacuum vessel, with a roughly 1–2 full-power-year planned replacement interval. This makes modular adaptation a research opportunity, NOT proof of a technically complete D–D retrofit. ARC 2026 physics basis: https://doi.org/10.1017/S0022377826101706 .

**Owner's previously modeled retrofit scope:** about **10–15% of component MASS** modified/replaced when adapting an ARC D–T platform to D–D. **This is NOT a 10–15% cost percentage.** The owner additionally recalls a **~3% modular vessel component reference**; its exact mass/cost denominator is unresolved and must not be presumed to equal total plant cost.

### Recovered earlier detailed retrofit pricing (historical research assumptions, NOT quotes)

| Hardware category | Earlier candidate installed/modification cost |
|---|---:|
| Inner vacuum-vessel and divertor cartridge | $35M–$75M |
| RF heating/current-drive upgrades | $90M–$175M |
| Cryopumps | $25M–$45M |
| Isotope separation plant | $85M–$160M |
| **Gross adaptation subtotal** | **$235M–$455M** |
| Turbine island resizing/downsizing allowance | **−$150M to −$250M**, conditional saving requiring validation |

The historical scenario register separately included **$75M low / $150M base / $350M high NET retrofit additions**; an alternate summary quoted a net $85M–$205M. These are **scenario values / inconsistent scope records**, not three reconciled outcomes from one identical bill of materials. Unpaired endpoints of gross $235M–$455M minus $150M–$250M yield an unconstrained difference interval of **−$15M to +$305M**; that interval is NOT itself a credible financed retrofit forecast. Preserve actual component pairings, engineering interfaces, credits and any avoided turbine costs rather than attributing a universal net value.

**Owner's current approximation of ~$300M:** treat this as **approximate D–D ARC retrofit/modification scope**, NOT the total cost of both new ARC power plants, and not a confirmed current-dollar bid. $300M is within the historical **gross $235M–$455M** subtotal. Need recover the exact prior source to see whether the remembered figure was intended gross or net.

### Historical dual-ARC chassis ledger, separately from retrofit estimate

- A full-size ARC chassis $2.8B (previous illustrative basis); B $2.8B (previous illustrative basis).
- A separate simplified historical ledger used adaptation **+$150M**, turbine change **−$200M**, isotope equipment **+$120M** and thus summed to **$5.67B**, although a prior document wrote **$5.87B**. **$200M inconsistency is unreconciled**.
- The **+$150M** adaptation and **+$120M** isotope line may overlap the detailed retrofit schedule above. **Do not stack** these or convert 10–15% MASS into a 10–15% PRICE uplift.
- $2.8B for each chassis is neither a quote nor an accepted current CFS price. Separate two-reactor acquisition CAPEX, D–D-specific adaptation, turbine change, isotope plant, financing, replacement vessel life-cycle, operating, site and contingency expenses.

**Google/CFS:** Google announced an additional investment in Commonwealth Fusion Systems and a 200-MW electricity purchase agreement for CFS's planned first D–T ARC in June 2025. **Gemini** was a tool used to help explore the owner's candidate component-cost model, not evidence of Google approval, investment or a priced D–D modification. Announcement: https://cfs.energy/news-and-media/google-and-commonwealth-fusion-systems-sign-strategic-partnership/ .

## Correct conditional gross nuclear isotope ledger

Assume hypothetical continuous full-power operation for **1.1 GW primary D–D fusion** at 50:50 T+p and He-3+n branches (mean reaction energy ~3.6508 MeV), **1.1 GW primary D–T fusion** (17.589 MeV/reaction), 365.25 days full-power year and no in-core D–D-born T secondary burn.

| Flow | Gross nuclear accounting, BEFORE losses |
|---|---:|
| A direct helium-3 births | ~148.6 kg/FPY |
| A direct tritium births | ~148.6 kg/FPY |
| B plasma tritium consumption | ~61.7 kg/FPY |
| B helium-4 births | ~81.9 kg/FPY |
| A born tritium / B burn | ~2.41× *gross conditional ratio*, NOT proof of self-sufficient delivery |

At illustrative 85% common calendar availability: He-3 and T born in A ~126.3 kg/year each; B T burn ~52.4 kg/year; B He-4 ~69.6 kg/year. Time-resolved recovery, fuel processing, internal secondary burns, reserve buildup, decay, downtime mismatch, qualified He-3/T product, and B's separate lithium blanket breeding remain OPEN. Only actual qualified surplus after ALL internal consumption may be sold; isotope value or theoretical gross mass is not available cash.

The historical A=20 MW_fusion scenario produces ~2.7 kg of He-3 and T/FPY and **is ~55 times smaller** than the present A source power. Old 20 MW_fusion cost/power/self-sufficiency conclusions **must not be ported** into this configuration without a fresh physical model.

## Validation and handoff rules

1. All new dual-ARC datasets MUST use distinct keys: A.fusion_power_MW=1100, A.projected_net_electric_MW=20, B.fusion_power_MW=1100. Mark A projected net as historical/unvalidated.
2. Model 1.1 GW D–D physics and ARC vessel engineering explicitly, not by assuming D–T physics transfers unchanged.
3. Keep experimental laser/WarpX efforts separate from ARC apparatus definitions while comparing validated reaction-rate or diagnostic outputs when appropriate.
4. Reconcile the full detailed Gemini-derived cost table and the owner's ~$300M recollection, component mass scope and 3% vessel reference; do not silently alter 2026-10-29 historical calculation files.
5. Determine D–D whole-plant NET power from distinct heat sources, electricity conversion, external heating/current drive, cryogenic and auxiliary loads; do not infer +20 MWe from gross source rating.
6. Recompute He-3/T birth, actual recovery, B tritium breeding, demand, reserves and 20/30/50-year finances. Preserve error messages on incompatible power inputs.

**Mandatory one-line handoff:** TWO ARC-class reactors, each 1.1 GW proposed gross fusion; A D–D isotope refinery with historical +20 MWe net projection, B D–T electricity with ~400 MWe published-design comparator; 10–15% is modified MASS not cost; ~$300M is a user-recalled retrofit-scale estimate, not paired-reactor total purchase.
