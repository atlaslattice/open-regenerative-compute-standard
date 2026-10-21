"""Verify accounting invariants and failure behavior; not physical validation."""
import copy
import json
import math
from pathlib import Path
from model import run

base = json.loads(Path(__file__).with_name('example.json').read_text())
r = run(base)
assert abs(r['mass_balance_error_t_day']) < 1e-9
assert math.isclose(r['accepted_product_t_day'], 0.576)
assert math.isclose(r['electricity_kwh_day'], 203.6)
assert r['capacity_feasible_under_assumed_stage_ratings']
# Service fee calculated by model closes the annual cash/capital balance.
c = copy.deepcopy(base)
c['economics']['contracted_service_fee_usd_t'] = r['break_even_service_fee_usd_input_t']
assert abs(run(c)['annual_surplus_after_capital_charge_usd']) < 1e-6
# Rejection eliminates sales without losing mass or residual costs.
c = copy.deepcopy(base)
for m in c['materials']:
    m['buyer_acceptance'] = 0
z = run(c)
assert z['accepted_product_t_day'] == z['product_sales_usd_day'] == 0
assert math.isclose(sum(m['managed_residual_t_day'] for m in z['streams']), 20)
assert z['residual_management_usd_day'] > r['residual_management_usd_day']
# Doubling achieved throughput exceeds unchanged full-feed stage capacity.
c = copy.deepcopy(base)
c['intake_t_day'] = 40
assert not run(c)['capacity_feasible_under_assumed_stage_ratings']
# Fractions, prices and nonfinite data cannot silently corrupt outputs.
for key, value in [('fraction', 1.1), ('fraction', -0.1),
                   ('buyer_acceptance', 2), ('net_price_usd_t', float('nan'))]:
    c = copy.deepcopy(base)
    c['materials'][0][key] = value
    try:
        run(c)
    except ValueError:
        pass
    else:
        raise AssertionError(f'Invalid input accepted: {key}')
print('PASS: mass balance, acceptance/rejection, break-even fee, capacity, invalid inputs')
