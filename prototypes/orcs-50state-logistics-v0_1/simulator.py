"""ORCS 50-state route/reserve skeleton v0.1. Not calibrated. Standard library only."""
import argparse
import heapq
import json
from pathlib import Path

STATES = 'AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY'.split()


def check_network(data):
    nodes = data.get('states', [])
    if len(nodes) != 50 or len(set(nodes)) != 50 or set(nodes) != set(STATES):
        raise ValueError('Geography must contain exactly the 50 US states')
    for edge in data.get('edges', []):
        if edge['from'] not in STATES or edge['to'] not in STATES or edge['from'] == edge['to']:
            raise ValueError('Invalid state edge')
        for key in ('capacity_bbl', 'cost_usd_per_bbl', 'time_days'):
            if edge.get(key) is not None and edge[key] < 0:
                raise ValueError('Negative ' + key)
        if not edge.get('grade'):
            raise ValueError('Grade must be explicit')
    return True


def optimize(data, origin, destination, grade, volume_bbl, max_days=None, disabled_edges=()):
    """Least-cost path for ONE whole shipment; no competing-flow capacity allocation."""
    check_network(data)
    if origin not in STATES or destination not in STATES or volume_bbl < 0:
        raise ValueError('Invalid shipment')
    if volume_bbl == 0:
        return {'status': 'NO_SHIPMENT', 'volume_bbl': 0}
    graph = {s: [] for s in STATES}
    excluded_unknown = 0
    for i, e in enumerate(data.get('edges', [])):
        if i in disabled_edges or e['grade'] != grade or not e.get('permitted', False) or not e.get('safe', False):
            continue
        if any(e.get(k) is None for k in ('capacity_bbl', 'cost_usd_per_bbl', 'time_days')):
            excluded_unknown += 1
            continue
        if e['capacity_bbl'] < volume_bbl:
            continue
        graph[e['from']].append((e['to'], i, e['cost_usd_per_bbl'], e['time_days']))
    pq = [(0.0, 0.0, origin, [])]
    labels = {s: [] for s in STATES}
    while pq:
        cost, elapsed, at, path = heapq.heappop(pq)
        if any(c <= cost and t <= elapsed for c, t in labels[at]):
            continue
        labels[at] = [(c,t) for c,t in labels[at] if not (cost <= c and elapsed <= t)] + [(cost,elapsed)]
        if at == destination:
            return {'status': 'FEASIBLE_SCENARIO', 'grade': grade, 'volume_bbl': volume_bbl,
                    'path': [origin] + [data['edges'][i]['to'] for i in path], 'edge_indices': path,
                    'cost_usd': cost * volume_bbl, 'time_days': elapsed,
                    'note': 'Scenario feasibility only, independently validate each edge.'}
        for nxt, idx, unit_cost, days in graph[at]:
            t = elapsed + days
            if max_days is None or t <= max_days:
                heapq.heappush(pq, (cost + unit_cost, t, nxt, path + [idx]))
    return {'status': 'UNVERIFIED_OR_INFEASIBLE', 'volume_bbl': volume_bbl,
            'unknown_edges_excluded': excluded_unknown,
            'note': 'No demonstrable route; missing data do not prove physical infeasibility.'}


def reserve_gate(demand_bbl, usable_stock_bbl, supply_bbl, target_days=90, period_days=365):
    """Proposed total-use reserve test, not IEA net-import requirement."""
    if min(demand_bbl, usable_stock_bbl, supply_bbl, target_days, period_days) < 0 or period_days == 0:
        raise ValueError('Invalid reserve input')
    target = demand_bbl * target_days / period_days
    supply_to_demand = min(demand_bbl, supply_bbl)
    stock_draw = min(usable_stock_bbl, demand_bbl - supply_to_demand)
    stock_remaining = usable_stock_bbl - stock_draw
    available_supply = supply_bbl - supply_to_demand
    reserve_add = min(available_supply, max(0., target - stock_remaining))
    final_stock = stock_remaining + reserve_add
    demand_served = supply_to_demand + stock_draw
    return {'demand_served_bbl': demand_served,
            'unmet_demand_bbl': demand_bbl - demand_served,
            'ending_stock_bbl': final_stock, 'target_stock_bbl': target,
            'reserve_days_at_demand_rate': None if demand_bbl == 0 else final_stock * period_days / demand_bbl,
            'export_candidate_bbl': max(0., available_supply - reserve_add)
                if final_stock >= target and demand_served == demand_bbl else 0.,
            'export_authorized': False, 'reserve_target_status': 'PROPOSED_TOTAL_USE'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--network', default=str(Path(__file__).with_name('network.json')))
    p.add_argument('--from-state', dest='origin', default='TX')
    p.add_argument('--to-state', dest='destination', default='NY')
    p.add_argument('--grade', default='distillate_compatible_EXAMPLE')
    p.add_argument('--barrels', type=float, default=100)
    args = p.parse_args()
    data = json.loads(Path(args.network).read_text())
    print(json.dumps(optimize(data,args.origin,args.destination,args.grade,args.barrels),indent=2))


if __name__ == '__main__':
    main()
