# ORCS Addendum v1.1 — Full Export-Stream Capture and Distributed Fiber Inventory
Date: 2026-10-30. Companion to docs/whitepapers/ORCS_RECOVERED_PAPER_DOMESTIC_CAPACITY_REDIRECTION_WP_v1_0_2026-10-30.md.

## User's operating thesis
Do not constrain recovered-paper collection to this year's paper-mill idle capacity. Capture the broader export stream where economically competitive, place grade-separated recoverable fiber in permitted regional reserves, and use those stocks to reduce feedstock-related downtime. Prioritize dispatch to existing domestic mills, then brownfield conversions, other paper grades and contracted finished-product exports. This is a proposed operating model, not an instruction to divert existing contractual shipments unilaterally.

## The inventory identity that must close
Closing inventory (tonnes) = opening inventory + receipts + domestic recovered-fiber purchases diverted from exports - mill feedstock withdrawals - contracted fiber sales/exports - contamination/rejection losses.
Mill finished product output <= verified compatible annual throughput and confirmed demand; a fiber reserve can smooth short-term interruptions, but does NOT change the physical maximum production rate of mills.

## Two distinct national cases
**India-bound tranche**: ~2.108 million metric tonnes/y, ~2.324 million US short tons feedstock; at assumed 90% yield ~2.091 million short tons finished board. Numerically below ~3.182 million short tons of 2025-based theoretical containerboard headroom, conditional on mill compatibility and demand.
**All destinations**: ~12.4 million metric tonnes/y, ~13.6687 million short tons feedstock; at assumed 90% yield ~12.302 million short tons output equivalent. Existing 2025-based theoretical idle containerboard output ~3.182 million short tons/y. If that entire stream is collected and none is sent to other grades, sold onward, or converted at new facilities, a notional ~9.12 million short tons/year finished-equivalent backlog accumulates (roughly 10.13 million short tons actual feedstock at 90% yield). Physical reserves must be evaluated in *feedstock tonnes* and realistic storage duration, not output equivalents. Other grades, mill conversions, customer contracts, and product exports are candidate additional outlets.

## Separate downtime causes
- Fiber shortages: strategic local reserves can potentially recover production.
- Maintenance/unplanned failure: additional fiber cannot prevent mechanical downtime.
- Lack of demand / price: additional fiber cannot create customers.
- Grade incompatibility: fiber cannot be fed without appropriate processing or conversion.
- 100% theoretical capacity utilization is not an appropriate operational guarantee; usable maximum requires mill-level reliability factors and scheduled downtime.

## Operational policy candidate
1. Establish 7-, 14-, and 30-day rolling feedstock reserves where safe, contractually supported and financially rational.
2. Optimize grade-specific route assignments by actual 2026 mill demand, spare compatible feedstock intake, rail/truck costs, capacity constraints and inventory deterioration.
3. Keep separate balances for (a) incoming fiber; (b) finished goods; (c) available annual processing capacity.
4. Model storage carrying costs, moisture/fire safety, rejects, degradation and site permit limits.
5. If national annual captures exceed permanent processing and offtake, forecast backlog explicitly and add capacity or preserve an export release valve. Do not assume indefinitely growing stockpiles remain economically feasible.
6. Reserve activation may support higher *realized* utilization up to reliable mill capacity but not capacity beyond it.

## Dashboard fields
capture_feedstock_metric_t_y; diverted_from_india_t_y; diverted_from_other_exports_t_y; eligible_spare_mill_intake_t_y; mill_available_hours_y; feedstock_downtime_hours_y; maintenance_downtime_hours_y; demand_downtime_hours_y; inventory_feedstock_t; days_of_cover; processing_feedstock_t_y; expected_backlog_t_y; reserve_storage_cost_usd_y; realized_incremental_value_added_usd_y; grade; source_timestamp; evidence_grade.

**Evidence gate:** Published 2024 exports and 2025 annual capacity figures provide a national screening baseline only. Collect mill-by-mill 2026 throughput, material grades, sale contracts and actual supply-related downtime before projecting avoided downtime or manufacturing benefits.
