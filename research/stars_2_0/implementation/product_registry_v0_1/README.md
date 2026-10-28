# Stars multi-reaction product registry v0.1

2026-10-28. Initial source and market-acquisition register; no calibrated multi-reaction simulator or economic result.

Three isotope identities are registered: helium-4, helium-3 and hydrogen-3 (tritium). Five reaction/decay pathway associations are listed. Zero numerical market prices, recovered inventories or processing costs are qualified. JSON null means unknown, never zero. This is a deliberately small seed registry, not a complete activation or impurity network.

## Source receipts and market status

Sources are linked in PRODUCT_REGISTRY_v0_1.json. DIII-D's educational reaction description supports the two D-D product channels; ITER identifies helium and neutron products for D-T; the pinned Stars paper records p–B-11 alpha products. DOE NIDC documents helium-3 recovery from tritium decay. These sources support channel identity only, not energy-dependent cross sections, branching fractions or production performance.

NIDC helium and quote pages were inspected through public search on October 28, 2026. They direct buyers toward quote requests rather than supplying a numerical price usable here. ISOFLEX states that quotes depend on isotope, enrichment, purity, form and quantity. No request was sent to a supplier, no procurement action was taken and no secondary price headline was adopted as today's price.

For tritium and helium-4, no matching qualified numerical product quotation was acquired in this pass. Helium-3 has a supplier-listing lead; it remains unpriced. A price per gas volume needs declared reference temperature/pressure and isotope composition before mass conversion. Analysis-service prices are not isotope sale prices.

## Connection to the economic reporter

This register is an acquisition layer for economic_reporting_v0_1 in draft PR #15. A caller must provide independently justified inventory and saleability, a matching dated price snapshot and explicit processing/operating costs before the reporter can calculate a complete potential net value. Empty product specifications and null snapshots are intentional blockers. No inventory or value is inferred from registry membership.

The shared simulation architecture can eventually compare many experiments using:
qualified reaction channel data → event/source model → material/field transport → diagnostics and product retention → separately qualified recovery/inventory model → dated economic scenarios.

The present engine is not yet a calibrated implementation of all those stages. Adding a registry entry is not adding a working reaction simulator. Rapid surrogate screening should have its own status, while calibrated predictions require reaction-specific validation. Synthetic outputs are predictions, not instrument readings. Product role (primary/coproduct/byproduct) depends on the declared experiment objective.

## Explicit limits and next acquisition work

No branching fractions, decay rates, masses, cross sections, extraction efficiencies or device settings are introduced here. The decay path is an inventory dependency, not an optimization model. Parent sale and future daughter value cannot be credited to the same allocated stock; external atom/time accounting is required.

Prompt neutrons are an experimental output and transport burden, not a stored saleable isotope. Prompt protons, unreacted feedstock and impurities need separate inventories if economically relevant. Secondary activation and material-specific side channels are NOT enumerated; do not label this an all-products balance.

Next: qualify original nuclear data for each experiment, enumerate material-specific channels, obtain specification-matched dated price evidence, and attach measured or explicitly assumed recovery/cost uncertainties. Supplier price is not guaranteed accessible revenue. Preserve scientific outcome separately throughout.
