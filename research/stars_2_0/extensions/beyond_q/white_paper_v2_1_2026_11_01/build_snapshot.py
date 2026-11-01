"""Reproduce the checkpoint's financial recalculation from unchanged v2.0 output.
No new physical simulation; no qualification or actual sales inferred.
"""
from pathlib import Path
import csv,json,hashlib
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'module_fleet_v2_0'

def main():
    source=BASE/'outputs/annual_products_finance.csv'
    records=list(csv.DictReader(source.open()))
    rows=[]
    for recovery in [.375,.75,.9]:
        for year in [1,2]:
            r=next(x for x in records if float(x['fleet_modules'])==1 and float(x['year'])==year and
                float(x['He3_overall_recovery_assumed'])==recovery and x['price_case']=='requested_prices' and
                x['offtake_case']=='He3_full_offtake_sensitivity')
            liters=float(r['He3_product_candidate_STP_L'])
            t=float(r['T_external_export_scenario_kg'])
            debt=float(r['debt_service_USD_if_capital_incomplete_is_partial'])
            imports=float(r['electricity_import_cost_USD'])
            headroom=liters*1500+t*1.5e6-debt-imports
            rows.append(dict(year=year,He3_overall_recovery_assumed=recovery,mandatory_He3_retention=0.,
                He3_product_candidate_STP_L=liters,
                assumed_full_qualified_He3_sale_receipts_USD=liters*1500,
                conditional_T_export_kg=t,conditional_T_receipts_USD=t*1.5e6,
                partial_scope_debt_service_USD=debt,electricity_import_cost_USD=imports,
                remaining_before_unknown_costs_USD=headroom,
                remaining_if_He3_sales_capped_350000_L_USD=min(liters,350000)*1500+t*1.5e6-debt-imports,
                actual_profit_USD=None,actual_qualified_sales_USD=None))
    assert abs(rows[0]['remaining_before_unknown_costs_USD']-87006328.81375093)<.01
    assert abs(rows[1]['remaining_before_unknown_costs_USD']-135798600.5077737)<.01
    execution=json.loads((BASE/'outputs/execution.json').read_text())
    hashes={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [source,BASE/'model.py',BASE/'finance.py',BASE/'inputs.json']}
    result=dict(paper_version='2.1',date='2026-11-01',implementation_base_commit='971a94300d91d4ff514061a4918e44684277e78b',
        new_physical_execution=False,zero_retention_financial_recalculation=True,
        saved_physical_inputs_still_use_retention_fraction=.5,
        facts=dict(startup_threshold_kg=execution['checks'][0]['startup_B_threshold_kg'],
            years=execution['inputs']['years'],fixed_calendar_commissioning_interval_years=.1,
            predecessor_fuel_controller_executed=False,all_physical_gates='G1-G5 OPEN'),
        recalculation=rows,source_sha256=hashes)
    (ROOT/'NUMERICAL_SNAPSHOT.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Verified six recovery/year recalculations; no physical inputs changed.')
if __name__=='__main__':main()
