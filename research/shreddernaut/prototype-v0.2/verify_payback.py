"""Accounting checks, not engineering or financial validation."""
import copy
import json
import math
from pathlib import Path
from payback import compare
p=Path(__file__).resolve().parent
a=json.loads((p/'payback-assumptions.json').read_text())
b=json.loads((p/'example.json').read_text())
r=compare(a,b)
assert len(r['rows']) == 16
for x in r['rows']:
    assert abs(x['mass_balance_error_t_day']) < 1e-9
    calculated=x['net_product_receipts_usd_day']+20*x['service_fee_usd_input_t']-x['cash_operating_cost_usd_day']
    assert math.isclose(x['cash_surplus_usd_operating_day'],calculated,abs_tol=1e-8)
    d=x['simple_payback_operating_days']
    if calculated <= 0:
        assert d is None
    else:
        assert math.isclose(d*calculated,500000)
    if x['route']=='toll':
        assert x['finished_metal_t_day'] < x['accepted_metal_t_day']
# Grant/capital funding is not fabricated recurring operating income.
c=copy.deepcopy(a);c['installed_capital_usd']=0;c['one_time_development_usd']=0
z=compare(c,b)
for x,y in zip(r['rows'],z['rows']):
    assert x['cash_surplus_usd_operating_day']==y['cash_surplus_usd_operating_day']
# Longer settlement delays increase liquidity allowance, not operating profitability.
c=copy.deepcopy(a);c['refinery_settlement_days']=120
z=compare(c,b)
for x,y in zip(r['rows'],z['rows']):
    assert x['cash_surplus_usd_operating_day']==y['cash_surplus_usd_operating_day']
    if x['route']=='toll':
        assert math.isclose(2*x['settlement_cash_bridge_usd'],y['settlement_cash_bridge_usd'])
# Invalid refinery recovery must fail.
c=copy.deepcopy(a);c['metals']['copper']['refinery_recovery']=1.1
try:
    compare(c,b)
except ValueError:
    pass
else:
    raise AssertionError('Invalid refinery yield accepted')
print('PASS: 16 scenarios; losses, cash payback, refining losses, capital separation, settlement timing, validation')
