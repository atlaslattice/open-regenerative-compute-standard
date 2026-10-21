"""Compare scrap vs toll processing; standard library; no market-price API.
Run: python3 payback.py --output payback-results.json
Requires model.py, example.json, payback-assumptions.json beside this file.
"""
import argparse
import copy
import json
import math
from pathlib import Path
from model import run, finite_number

ROOT = Path(__file__).resolve().parent


def compare(a, base):
    for k in ('intake_t_day', 'operating_days_year', 'installed_capital_usd',
              'one_time_development_usd', 'initial_cash_reserve_usd',
              'refinery_settlement_days', 'toll_outbound_freight_usd_recovered_t',
              'toll_assay_usd_recovered_t', 'budget_contingency_fraction'):
        finite_number(a[k], k)
    finite_number(a['toll_selling_fraction'], 'selling fraction', 0, 1)
    if a['intake_t_day'] <= 0 or not 0 < a['operating_days_year'] <= 365:
        raise ValueError('Positive intake and 1–365 operating days required')
    for fee in a['service_fee_usd_t_cases']:
        finite_number(fee, 'service fee')
    for metal in a['metals'].values():
        for k in ['scrap_net_usd_t', 'finished_usd_t', 'conversion_usd_recovered_t']:
            finite_number(metal[k], k)
        finite_number(metal['refinery_recovery'], 'refinery recovery', 0, 1)
    rows = []
    invested = a['installed_capital_usd'] + a['one_time_development_usd']
    for feedname, feed in a['feed_scenarios'].items():
        c = copy.deepcopy(base)
        c['intake_t_day'] = a['intake_t_day']
        c['operating_days'] = a['operating_days_year']
        c['economics']['purchased_capital_usd'] = a['installed_capital_usd']
        c['materials'] = []
        for name, fraction in feed['fractions'].items():
            ismetal = name in a['metals']
            c['materials'].append({
                'name': name, 'fraction': fraction,
                'capture': feed['capture'] if ismetal else 0,
                'buyer_acceptance': feed['buyer_acceptance'] if ismetal else 0,
                'net_price_usd_t': a['metals'][name]['scrap_net_usd_t'] if ismetal else 0,
                'residual_management_usd_t': 400 if name == 'hazard_quarantine' else 40 if name == 'fines' else 50})
        result = run(c)
        if not result['capacity_feasible_under_assumed_stage_ratings']:
            raise ValueError('Configuration exceeds assumed stage capacity')
        cash_opex = result['residual_management_usd_day'] + result['other_operating_usd_day']
        recovered = result['accepted_product_t_day']
        gross, conversion, finished = 0, 0, 0
        for stream in result['streams']:
            if stream['name'] not in a['metals']:
                continue
            metal = a['metals'][stream['name']]
            tonnes = stream['accepted_t_day']
            finished += tonnes * metal['refinery_recovery']
            gross += tonnes * metal['refinery_recovery'] * metal['finished_usd_t']
            conversion += tonnes * metal['conversion_usd_recovered_t']
        # Fees assessed on recovered feed, gross sales fee on actual finished value.
        toll_net = (gross * (1-a['toll_selling_fraction']) - conversion
                    - recovered*(a['toll_outbound_freight_usd_recovered_t']+a['toll_assay_usd_recovered_t']))
        for route, net in [('scrap', result['product_sales_usd_day']), ('toll', toll_net)]:
            for fee in a['service_fee_usd_t_cases']:
                surplus = net + a['intake_t_day']*fee - cash_opex
                days = invested/surplus if surplus > 0 else None
                rows.append({
                    'feed': feedname, 'route': route, 'service_fee_usd_input_t': fee,
                    'accepted_metal_t_day': recovered,
                    'finished_metal_t_day': finished if route == 'toll' else None,
                    'net_product_receipts_usd_day': net,
                    'cash_operating_cost_usd_day': cash_opex,
                    'cash_surplus_usd_operating_day': surplus,
                    'cash_surplus_usd_year': surplus*a['operating_days_year'],
                    'break_even_service_fee_usd_input_t': max(0, (cash_opex-net)/a['intake_t_day']),
                    'simple_payback_operating_days': days,
                    'simple_payback_years_at_assumed_days': days/a['operating_days_year'] if days else None,
                    # Conservative calendar funding allowance, service fees also assumed delayed.
                    'settlement_cash_bridge_usd': cash_opex*a['refinery_settlement_days'] if route == 'toll' else None,
                    'mass_balance_error_t_day': result['mass_balance_error_t_day']})
    low = sum(v[0] for v in a['budget_allowances_usd'].values())*(1+a['budget_contingency_fraction'])
    high = sum(v[1] for v in a['budget_allowances_usd'].values())*(1+a['budget_contingency_fraction'])
    return {'status': a['status'],
            'installed_budget_allowance_range_usd': [low, high],
            'central_nonrecoverable_initial_investment_usd': invested,
            'central_cash_envelope_usd_with_initial_reserve': invested+a['initial_cash_reserve_usd'],
            'payback_definition': 'Initial installed capital + development divided by positive cash surplus; unlevered, pre-tax, no capital charge or grants. Cash reserve excluded from payback denominator; settlement bridge is timing allowance, not additional recurring expense.',
            'rows': rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--assumptions', type=Path, default=ROOT/'payback-assumptions.json')
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    a = json.loads(args.assumptions.read_text())
    base = json.loads((ROOT/'example.json').read_text())
    out = json.dumps(compare(a, base), indent=2, allow_nan=False)+'\n'
    if args.output:
        args.output.write_text(out)
    else:
        print(out, end='')


if __name__ == '__main__':
    main()
