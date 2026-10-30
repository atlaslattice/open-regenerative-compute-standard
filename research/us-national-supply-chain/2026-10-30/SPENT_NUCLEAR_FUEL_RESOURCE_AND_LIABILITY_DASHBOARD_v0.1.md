# National Supply-Chain Dashboard — Spent Nuclear Fuel Recovery & Liability (research candidate v0.1)

Date: 2026-10-30. Scope: United States. Status: sourced dashboard-layer proposal, **not** a facility feasibility determination or an assertion that nuclear material can be handled outside regulated channels.

## Separate dashboard ledgers
1. **Physical inventory:** commercial spent nuclear fuel (metric tons heavy metal), annual discharged quantity, site/state counts, age, custody and publicly releasable data only. Baseline >90,000 metric tons; roughly 2,000 metric tons annually (GAO, access 2026-10-30): https://www.gao.gov/nuclear-waste-disposal
2. **Energy-resource potential:** DOE says >90% of *potential nuclear energy* remains after usual reactor life. This is **not** recoverable electricity, recovery yield or present market value: https://www.energy.gov/ne/articles/5-fast-facts-about-spent-nuclear-fuel ; https://www.pnnl.gov/news-media/new-life-used-nuclear-fuel
3. **Nuclear Waste Fund:** FY2025 ending balance ~$51.4B, funded through past utility fees plus interest; not $51.4B new taxpayer spending, and not freely appropriable recovery capital. Use audited DOE FY2025 NWF statements: https://www.energy.gov/sites/default/files/2025-11/DOE-OIG-26-02.pdf ; cross-check https://world-nuclear.org/information-library/country-profiles/countries-t-z/usa-nuclear-fuel-cycle
4. **Delayed-acceptance damages:** $12.2B cumulative paid as of 2025-09-30, distinct from Nuclear Waste Fund. Remaining estimated federal contract liability $38.6B–$44.3B, not cash spent; total estimated liability $50.8B–$56.5B. Source DOE FY2025 NWF audit: https://www.energy.gov/sites/default/files/2025-11/DOE-OIG-26-02.pdf
5. **Recovery options:** conventional direct disposal; interim storage; reprocessing/recycle; advanced fuel cycles; subcritical transmutation (research only). Track separations loss, recoverable fuel yields, safety/security/licensing, residual waste volumes/activity, full lifecycle costs, technology readiness and capital needs; don't assume tipping-fee revenue or disposal savings.

## UI schema candidates
`national_spent_fuel_tHM`, `spent_fuel_increment_tHM_per_year`, `stored_sites_count`, `energy_remaining_fraction_claim`, `energy_recoverable_fraction_model`, `fuel_recovery_yield_t_per_t`, `nwf_balance_usd`, `damages_paid_usd`, `remaining_liability_low_usd`, `remaining_liability_high_usd`, `reprocessing_lifecycle_cost_usd_per_t`, `reference_disposal_cost_usd_per_t`, `avoided_liability_usd_model`, `evidence_grade`, `as_of_date`, `source_url`.

## Constraints
- **NEVER** add NWF balance to damages and claim total taxpayer investment; don't treat a projected liability as paid or cash on hand.
- Material composition and regulatory status vary, and separated uranium is NOT automatically HALEU.
- Recovery reduces neither geological disposal needs nor liabilities without demonstrated and legally accepted outcomes.
- Keep the nuclear resource/recycling dashboard independent of Beyond Q fusion and proposed fission hybrid until supported engineering results exist.

## Next implementation gate
Attach this dataset to the dashboard resource selector as `Nuclear fuel / spent-fuel recovery`, with federal overview and state-level public-data drilldown, uncertainty labels and source/update timestamps; compare direct disposal vs licensed recovery on lifecycle net cost and long-term waste liabilities. **This file is a research specification only; no live UI wiring is claimed.**
