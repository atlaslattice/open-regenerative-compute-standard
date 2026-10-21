"""Convert conditional national metal outputs to consumption-equivalent coverage.
2025 estimated USGS baselines held constant; not grade-specific dispatch modeling.
"""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
r=json.loads((p/'national-summary.json').read_text())
annual={'copper':2200000,'aluminum':5700000,'ferrous':95000000}
rows=[]
for case in r['rows']:
    if case['program'] not in ['targeted_metal_rich_conditional','mixed_program_unfunded'] or case['additionality_fraction']!=1:
        continue
    for metal,consumption in annual.items():
        stock=case['five_year_finished_metal_t'][metal]
        y5=case['annual'][-1]['finished_metal_t'][metal]
        rows.append({'case':case['program'],'metal':metal,'baseline_2025_consumption_t_year':consumption,
            'five_year_output_t':stock,'gross_stockpile_days_at_full_national_consumption':stock/consumption*365,
            'attributable_days_at_50pct_additionality':stock/consumption*365*0.5,
            'year5_output_t_year':y5,'year5_fraction_of_annual_consumption':y5/consumption,
            'year5_consumption_equivalent_days_produced_per_year':y5/consumption*365})
case=next(x for x in r['rows'] if x['program']=='targeted_metal_rich_conditional' and x['additionality_fraction']==1)
a=json.loads((p/'payback-assumptions.json').read_text())
gross=sum(case['five_year_finished_metal_t'][m]*a['metals'][m]['finished_usd_t'] for m in annual)
netreceipts=sum(x['net_product_receipts_usd'] for x in case['annual'])
downstream=gross-netreceipts
local=sum(x['local_cash_operating_cost_usd']+x['shared_operations_allowance_usd'] for x in case['annual'])
cost=case['initial_investment_usd']+local+downstream
coproducts=sum(case['five_year_finished_metal_t'][m]*a['metals'][m]['finished_usd_t'] for m in ['aluminum','ferrous'])
result={'status':'CONDITIONAL ESTIMATE; ALL OUTPUT STORED, NO WITHDRAWALS; VAULT ACCEPTANCE NOT ESTABLISHED',
    'consumption_basis':'2025 USGS estimates; copper apparent primary refined + old scrap; aluminum apparent excluding new scrap; steel mill product apparent consumption. Different material bases; conversion into qualified grades assumed, not verified.',
    'coverage_rows':rows,'reported_vault_shipment_copper_t':12000,
    'reported_shipment_days_at_broad_copper_consumption':12000/annual['copper']*365,
    'modeled_copper_output_divided_by_reported_shipment':case['five_year_finished_metal_t']['copper']/12000,
    'modeled_gross_finished_output_value_usd':gross,
    'modeled_total_resource_cash_cost_usd':cost,
    'modeled_co_product_credit_usd':coproducts,
    'modeled_copper_cost_after_coproduct_credits_usd_t':(cost-coproducts)/case['five_year_finished_metal_t']['copper'],
    'cost_limitations':'Synthetic prices/yields/fees; co-product credits require sales so cannot also stockpile all coproducts while claiming their cash receipts. Cost excludes financing/tax/reserve holding, extra refinery construction and site-specific changes. $500m Mercuria commitment is not the 12000t shipment purchase price.'}
assert abs(gross-cost-case['operator_net_after_initial_investment_usd'])<0.001
assert all(x['gross_stockpile_days_at_full_national_consumption']>x['year5_consumption_equivalent_days_produced_per_year'] for x in rows)
(p/'reserve-coverage-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
