"""Five-year cash ROI sensitivities. Inputs remain synthetic; not forecasts.
Run: python3 five_year.py --output five-year-results.json
"""
import argparse
import copy
import json
from pathlib import Path
from payback import compare

ROOT=Path(__file__).resolve().parent


def calculate(a,b,days=300,price_factor=1,cost_factor=1,extra_capital=0,
              extra_fixed_annual=0,extra_freight_recovered_t=0,extra_overhaul_year3=0):
    c=copy.deepcopy(a)
    for metal in c['metals'].values():
        metal['finished_usd_t']*=price_factor
        metal['scrap_net_usd_t']*=price_factor
    rows=compare(c,b)['rows']
    e=b['economics']
    # Treat retained crew, rental, other daily overhead and annual fixed costs as
    # committed across the original planned year, even when operating days fall.
    fixed=((e['crew']*b['shift_hours']*e['loaded_wage_usd_hour']
            +e['rental_usd_day']+e['other_usd_day'])*a['operating_days_year']
           +e['fixed_annual_usd'])
    investment=a['installed_capital_usd']+a['one_time_development_usd']+extra_capital
    out=[]
    for row in rows:
        variable=row['cash_operating_cost_usd_day']-fixed/a['operating_days_year']
        receipts=row['net_product_receipts_usd_day']
        if row['route']=='toll':
            receipts-=row['accepted_metal_t_day']*extra_freight_recovered_t
        annual=(receipts+a['intake_t_day']*row['service_fee_usd_input_t'])*days
        annual-=(fixed+variable*days)*cost_factor+extra_fixed_annual
        cash=[annual,annual,annual-extra_overhaul_year3,annual,annual]
        surplus=sum(cash)
        out.append({'feed':row['feed'],'route':row['route'],
                    'service_fee_usd_input_t':row['service_fee_usd_input_t'],
                    'operating_days_per_year':days,
                    'initial_investment_excluding_working_cash_usd':investment,
                    'annual_operating_cash_usd':cash,
                    'five_year_operating_cash_usd':surplus,
                    'five_year_net_cash_after_initial_investment_usd':surplus-investment,
                    'five_year_simple_roi_percent':100*(surplus-investment)/investment,
                    # Assume working cash is returned in full at end of year five.
                    'roi_on_total_initial_funding_with_working_cash_returned_percent':100*(surplus-investment)/(investment+a['initial_cash_reserve_usd'])})
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    a=json.loads((ROOT/'payback-assumptions.json').read_text())
    b=json.loads((ROOT/'example.json').read_text())
    variants={
        'base_300_days':{},
        'downtime_240_days_retained_staff':{'days':240},
        'metal_prices_minus20pct':{'price_factor':0.8},
        'operating_costs_plus15pct':{'cost_factor':1.15},
        'combined_downside_plus_extra_overhaul':{'days':240,'price_factor':0.8,'cost_factor':1.15,'extra_overhaul_year3':100000},
        'maui_illustrative_overlay_NOT_QUOTED':{'extra_capital':100000,'extra_fixed_annual':50000,'extra_freight_recovered_t':250}}
    result={'status':'SYNTHETIC SENSITIVITY, NOT ROI FORECAST OR HARDWARE RELIABILITY EVIDENCE',
            'definition':'ROI=(five-year operating cash minus initial equipment/development investment)/initial investment. Pre-tax, unlevered, undiscounted; no salvage, grants or carbon credits. Working reserve excluded from primary ROI. Five full operating years, no construction delay.',
            'stress_inputs':variants,
            'cases':{name:calculate(a,b,**kw) for name,kw in variants.items()}}
    # Five-year base must reconcile to previously executed daily model.
    for r,previous in zip(result['cases']['base_300_days'],compare(a,b)['rows']):
        assert abs(r['five_year_operating_cash_usd']-previous['cash_surplus_usd_operating_day']*1500)<1e-6
    for r in result['cases']['downtime_240_days_retained_staff']:
        if r['service_fee_usd_input_t']==0 and r['feed']=='enriched_selected_stream' and r['route']=='toll':
            assert r['five_year_simple_roi_percent'] < next(x['five_year_simple_roi_percent'] for x in result['cases']['base_300_days'] if x['feed']==r['feed'] and x['route']==r['route'] and x['service_fee_usd_input_t']==0)
    s=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.output:args.output.write_text(s)
    else:print(s,end='')


if __name__=='__main__':main()
