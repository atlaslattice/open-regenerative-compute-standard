"""Reconcile published case figures; no Oahu forecast, exchange rate or vendor quote."""
import csv
import json
from pathlib import Path
P=Path(__file__).parent
products=[
 ('rockwool',50000,3000),('bricks',30000,500),('washed_ash',20000,100),
 ('sodium_salt',17250.38,200),('potassium_salt',2870,1600),('calcium_sulfate',17650,400)]
feed=60000;fee=1200;cost=209000000
revenues={n:t*p for n,t,p in products}
item_products=sum(revenues.values());reported_low_total=254554600
reported_high_total=339554600
r={
 'status':'RECONCILIATION OF SUPPLIER-REPORTED CASE/PROJECTIONS, NOT AUDITED OPERATING RESULTS OR HAWAII ECONOMICS',
 'currency':'CNY at source nominal basis; no USD conversion or inflation adjustment',
 'case_feed_tpy':feed,'listed_output_tpy':sum(t for _,t,_ in products),
 'output_to_feed_ratio_if_all_same_boundary':sum(t for _,t,_ in products)/feed,
 'mass_balance_warning':'Outputs exceed listed ash feed. Additional feed/additives, intermediate re-counting or different phase scopes must be resolved. No negative waste or recovery yield inferred.',
 'reported_total_capex_cny':700000000,'reported_phase1_capex_cny':300000000,'reported_phase2_capex_cny':400000000,
 'reported_annual_cost_cny':cost,'reported_cost_per_feed_t_cny':cost/feed,
 'reported_energy_COST_cny_per_feed_t':41510000/feed,
 'energy_kwh_per_feed_t':None,
 'line_item_product_revenues_cny':revenues,
 'line_item_total_product_revenue_cny':item_products,
 'reported_treatment_fee_cny_per_feed_t':fee,'reported_annual_treatment_fee_revenue_cny':feed*fee,
 'reported_low_total_revenue_cny':reported_low_total,
 'reported_high_total_revenue_cny':reported_high_total,
 'discrepancy_low_total_minus_itemized_including_fees_cny':reported_low_total-item_products-feed*fee,
 'annual_balance_using_reported_low_total_cny':reported_low_total-cost,
 'annual_balance_low_total_WITHOUT_treatment_fees_cny':reported_low_total-feed*fee-cost,
 'fee_per_t_needed_to_match_reported_cost_at_low_total_products_cny':max(0,(cost-(reported_low_total-feed*fee))/feed),
 'annual_balance_using_itemized_products_AND_fees_cny':item_products+feed*fee-cost,
 'annual_balance_using_itemized_products_WITHOUT_fees_cny':item_products-cost,
 'fee_per_t_needed_to_match_cost_at_itemized_products_cny':max(0,(cost-item_products)/feed),
 'cost_scope_warning':'Do not add another annualized capex/finance charge without confirming depreciation/financial cost already included. Costs/revenues may reflect planned complete project rather than commissioned phase.',
 'oahu_cost':None,'realized_profit':None,'payback':None,'oahu_residual_yield_changed':False,
 'source':'https://www.ceett.org.cn/kjcg/jscg/698776837681221.shtml'}
assert abs(sum(revenues.values())-182102076)<1e-6
assert r['discrepancy_low_total_minus_itemized_including_fees_cny']==452524
assert r['annual_balance_using_itemized_products_WITHOUT_fees_cny']<0
assert r['annual_balance_using_itemized_products_AND_fees_cny']>0
(P/'reconciliation.json').write_text(json.dumps(r,indent=2)+'\n')
# Generic electricity-cost sensitivity: these intensities/prices are NOT measurements.
rows=[]
for intensity in [100,500,1000]:
 for price in [.1,.3,.5]:
  rows.append({'energy_intensity_ASSUMED_kwh_per_actual_feed_t':intensity,
   'electricity_price_ASSUMED_usd_per_kwh':price,
   'electricity_only_usd_per_feed_t':intensity*price})
with (P/'electricity_sensitivity.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps({k:r[k] for k in ['listed_output_tpy','reported_cost_per_feed_t_cny',
 'discrepancy_low_total_minus_itemized_including_fees_cny','annual_balance_using_itemized_products_WITHOUT_fees_cny',
 'annual_balance_using_itemized_products_AND_fees_cny']},indent=2))
