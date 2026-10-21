"""Shreddernaut dry recovery screening model. Python 3, standard library only.
All example inputs are synthetic assumptions, not equipment or site measurements.
Run: python3 model.py example.json
"""
import argparse
import json
import math
from pathlib import Path


def finite_number(value, name, low=0, high=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name}: finite number required")
    if value < low or (high is not None and value > high):
        raise ValueError(f"{name}: outside allowed range")
    return value


def run(c):
    q = finite_number(c['intake_t_day'], 'intake', 0.001)
    days = finite_number(c['operating_days'], 'days', 1, 365)
    hours = finite_number(c['shift_hours'], 'hours', 0.001, 24)
    avail = finite_number(c['within_shift_availability'], 'availability', 0.001, 1)
    mats = c['materials']
    if not mats or len({m['name'] for m in mats}) != len(mats):
        raise ValueError('Nonempty, uniquely named materials required')
    if not math.isclose(sum(finite_number(m['fraction'], 'fraction', 0, 1) for m in mats), 1, abs_tol=1e-9):
        raise ValueError('Material fractions must sum to 1')
    streams, sales, costs, energy, capacities = [], 0, 0, 0, []
    for m in mats:
        for k in ['capture', 'buyer_acceptance']:
            finite_number(m[k], k, 0, 1)
        for k in ['net_price_usd_t', 'residual_management_usd_t']:
            finite_number(m[k], k)
        incoming = q * m['fraction']
        accepted = incoming * m['capture'] * m['buyer_acceptance']
        residual = incoming - accepted
        # Net product price is AFTER offsite freight, refining fees and deductions.
        sales += accepted * m['net_price_usd_t']
        costs += residual * m['residual_management_usd_t']
        streams.append({'name': m['name'], 'input_t_day': incoming,
                        'accepted_t_day': accepted, 'managed_residual_t_day': residual})
    for s in c['stages']:
        for k in ['rated_kw', 'capacity_t_hour']:
            finite_number(s[k], k, 0.001)
        for k in ['load_factor', 'feed_fraction']:
            finite_number(s[k], k, 0, 1)
        energy += s['rated_kw'] * s['load_factor'] * hours
        if s['feed_fraction']:
            capacities.append(s['capacity_t_hour'] * hours * avail / s['feed_fraction'])
    if not capacities:
        raise ValueError('At least one processing stage must receive feed')
    e = c['economics']
    for k, v in e.items():
        finite_number(v, k)
    if e['capital_years'] < 1:
        raise ValueError('capital_years must be >= 1')
    r, n = e['capital_rate'], e['capital_years']
    crf = r * (1+r)**n / ((1+r)**n-1) if r else 1/n
    capital_daily = e['purchased_capital_usd'] * crf / days
    labor = e['crew'] * hours * e['loaded_wage_usd_hour']
    diesel = q * e['diesel_l_t']
    other = (energy * e['electricity_usd_kwh'] + diesel * e['diesel_usd_l']
             + labor + e['rental_usd_day'] + e['other_usd_day']
             + e['fixed_annual_usd']/days + q * e['maintenance_usd_t'])
    total = costs + other + capital_daily
    accepted_total = sum(s['accepted_t_day'] for s in streams)
    closure = q - sum(s['accepted_t_day'] + s['managed_residual_t_day'] for s in streams)
    a = c['national']
    for k, v in a.items():
        finite_number(v, k)
    if not a['target_years'] or not a['states'] or not a['units_per_state']:
        raise ValueError('Positive target_years, states, units_per_state required')
    # Analyst-entered intake is achieved target; reject infeasible configuration.
    feasible = q <= min(capacities) + 1e-9
    annual = q * days
    fleet = a['states'] * a['units_per_state']
    return {
        'status': 'SYNTHETIC SCREENING ONLY; NOT VALIDATED OR CONSTRUCTION READY',
        'capacity_feasible_under_assumed_stage_ratings': feasible,
        'assumed_bottleneck_t_day': min(capacities),
        'mass_balance_error_t_day': closure, 'streams': streams,
        'accepted_product_t_day': accepted_total,
        'accepted_product_fraction': accepted_total/q,
        'electricity_kwh_day': energy, 'electricity_kwh_input_t': energy/q,
        'connected_nameplate_kw_not_inrush': sum(s['rated_kw'] for s in c['stages']),
        'mobile_equipment_diesel_l_day': diesel,
        'product_sales_usd_day': sales, 'residual_management_usd_day': costs,
        'other_operating_usd_day': other, 'capital_recovery_usd_day': capital_daily,
        'total_cost_usd_day': total,
        'break_even_service_fee_usd_input_t': max(0, (total-sales)/q),
        'annual_surplus_after_capital_charge_usd': (sales+q*e['contracted_service_fee_usd_t']-total)*days,
        'national': {
            'stock_t_assumption': a['stock_t'], 'stock_t_per_state_equal_split': a['stock_t']/a['states'],
            'steady_state_fleet': fleet,
            'legacy_processing_years_no_ramp_no_new_waste': a['stock_t']/(fleet*annual),
            'units_for_target_years_no_ramp': math.ceil(a['stock_t']/(a['target_years']*annual)),
            'accepted_product_t_stock_sensitivity': a['stock_t']*accepted_total/q,
            'warning': 'One processing pass is not complete remediation; no downstream capacity, reserve or import substitution claim.'},
        'limitations': ['No thermal processing, washing, pelletizing or moisture loss modeled.',
                       'Residual management price must include lawful treatment/disposal and transport.',
                       'Demand charges belong in fixed annual costs; electrical inrush requires engineering.',
                       'No grants, avoided disposal credits, land value or carbon revenue booked.',
                       'All costs and motor ratings are synthetic scenario inputs.']}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('config', type=Path)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    result = run(json.loads(args.config.read_text()))
    output = json.dumps(result, indent=2, allow_nan=False) + '\n'
    if args.output:
        args.output.write_text(output)
    else:
        print(output, end='')
    if not result['capacity_feasible_under_assumed_stage_ratings']:
        raise SystemExit('Requested intake exceeds assumed stage capacity; results are infeasible.')


if __name__ == '__main__':
    main()
