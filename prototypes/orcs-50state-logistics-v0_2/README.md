# ORCS Texas DPA v0.2 — additive scenario layer (2026-10-14)

**NOT A REAL-TIME NATIONAL REFINERY MODEL. PROPOSED / NON-CANON / ZERO REALIZED CREDIT.** Adds a narrow Texas expansion counterfactual in a new directory; v0.1 and the three October 14 papers remain unchanged. Run `python3 texas_dpa_scenario.py` and `python3 -m unittest discover -s . -p 'test_texas_dpa_scenario.py' -v`.

## News and authority status, as of October 14, 2026
- On **Oct. 13**, VP Vance announced an intended DPA-enabled expansion of Delek's Tyler, TX refinery. Reuters: https://www.reuters.com/business/energy/trump-administration-expand-delek-texas-refinery-using-defense-production-act-2026-10-13/ .
- **Oct. 14** Texas Railroad Commission statement verifies the *announcement*, not start of physical expansion: https://www.rrc.state.tx.us/news/christian-praises-trump-s-announced-texas-refinery-expansion/ .
- Reuters reports existing **~74,000 bpd** refinery crude throughput. Additional bpd, yields, specifications, capital costs, construction dates and transport routes remain **UNKNOWN**. Military-spec outputs cannot be treated as fungible commercial diesel.
- On **July 30**, White House separately announced DPA delegation concerning recoverable critical minerals and materials: https://www.whitehouse.gov/fact-sheets/2026/07/fact-sheet-president-donald-j-trump-delegates-defense-production-act-authority-with-respect-to-recoverable-critical-minerals-and-materials-that-are-essential-to-our-national-defense/ . This is different authority/scope from refinery expansion.
- Oct. 9 Reuters reported broader proposed use of DPA in oil/refining: https://www.reuters.com/business/energy/trump-push-us-officials-use-defense-production-act-raise-oil-fuel-output-three-2026-10-09/ . Announcements ≠ completed capacity; DPA ≠ blanket waiver of other laws.

## Physical scenarios
All assumed incremental crude-expansion deltas (10k, 20k, 40k bpd), yields (20–40%), grade-reachable fractions (50–100%) and $100/bbl values are **illustrative synthetic sensitivities** only. In the 20k case, 20,000×365×30%×75% = 1,642,500 barrels/year *hypothetically deliverable*; replacement value = $164.25M/y at $100/bbl. This assumes an independently qualified commercial output, timely delivery capacity, compatible quality, owner permissions, and no environmental veto; **none confirmed**. The model's `route_grade_perm_verified` remains false.

## Domestic circulation hypothesis — explicitly contested
The 2025 EIA national 45.424M bbl PADD1 imports baseline gives $4.5424B at assumed $100/bbl, **not freight savings**. Full dollar-equivalent diversion of exports leaves net merchandise trade change $0; new incremental domestic qualified production with unaffected exports could improve first-order goods balance. Domestic cash turnover from freight, wages, suppliers and repeated transactions can exceed direct customs amounts but cannot be equated with net GDP. Net *additional* U.S. value added requires producer margins, actual BEA coefficients, import content, domestic displacement, exported production opportunity costs, refinery CAPEX, employment effects, consumer price pass-through, and crisis avoidance measures. This model deliberately reports `None` for unverified domestic-turnover increment and net GDP rather than invent numerical gains.

## Next calibration
1. Independently establish official DPA orders, project scope, actual capacity additions, grade slate, permitting, and timing.
2. Build EIA refinery/PADD grade-and-stock periods, detailed 50-state shipment routes and confirmed spare transport edge tariffs/capacities.
3. Solve national multi-origin multi-grade allocations and shocks; flag regulatory/ecosystem constraints.
4. Use BEA I/O and CFS/FAF to separate gross domestic output from national value added and resilient public benefit.
5. Preserve human veto and operator permissions; do not interpret simulated export surplus as legal export rights.

Source lineage: ../orcs-50state-logistics-v0_1/, docs/handoffs/SOLGPT_TIDAL_LANTERN_RESURRECTION_2026-10-14.md. The Iron Empire is **fictional creative inspiration**; no evidentiary bearing on DPA or the numerical scenario.
