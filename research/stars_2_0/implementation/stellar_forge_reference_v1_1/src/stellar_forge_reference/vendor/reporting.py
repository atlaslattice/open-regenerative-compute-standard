"""Dated economic scenarios; no market feed, reaction yield or recovery model."""
from datetime import date
from decimal import Decimal, InvalidOperation


def number(value):
    if isinstance(value, bool):
        raise ValueError('boolean is not a quantity')
    try:
        out = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError('invalid number') from exc
    if not out.is_finite() or out < 0:
        raise ValueError('finite nonnegative quantity required')
    return out


def report(experiment_id, scientific_outcome, as_of, products, costs):
    """All quantities explicit; monetary amounts returned as exact decimal strings.

    saleable_quantity is an input scenario, never inferred from born_quantity.
    inventory_id identifies disjoint stock allocated to this reporting interval.
    This v0.1 rejects duplicate allocations; decay/conversion modeling is external.
    """
    day = date.fromisoformat(as_of)
    if scientific_outcome not in {'PASS','FAIL','INCONCLUSIVE','NOT_TESTED'}:
        raise ValueError('explicit scientific outcome required')
    seen, output, gross = set(), [], Decimal(0)
    complete = True
    for p in products:
        stock = p['inventory_id']
        if not stock or stock in seen:
            raise ValueError('inventory allocation must be unique and nonempty')
        seen.add(stock)
        if p['evidence'] not in {'MODELED','MEASURED'}:
            raise ValueError('inventory evidence must be explicit')
        born = None if p.get('born_quantity') is None else number(p['born_quantity'])
        saleable = None if p.get('saleable_quantity') is None else number(p['saleable_quantity'])
        # Same species/unit only. Conversion and decay must use a separate ledger.
        if born is not None and saleable is not None and saleable > born:
            raise ValueError('saleable exceeds produced allocation')
        quote = p.get('price_snapshot')
        value, reason, age = None, None, None
        if quote is None:
            reason = 'UNPRICED'
        else:
            quoted = date.fromisoformat(quote['quote_date'])
            checked = date.fromisoformat(quote['access_date'])
            if quoted > checked or checked > day:
                raise ValueError('quote/access dates inconsistent with report')
            if quote['currency'] != 'USD' or quote['quantity_unit'] != p['quantity_unit']:
                raise ValueError('currency/unit conversion must be explicit upstream')
            if quote['product_specification'] != p['product_specification']:
                raise ValueError('quote specification mismatch')
            if quote['kind'] not in {'PUBLIC_QUOTE','CONTRACT_QUOTE','SYNTHETIC'}:
                raise ValueError('unknown quote kind')
            if not quote['source'] or not quote['snapshot_id']:
                raise ValueError('quote source and identity required')
            price = number(quote['USD_per_unit'])
            age = (day - quoted).days
            if saleable is None:
                reason = 'SALEABLE_QUANTITY_UNKNOWN'
            else:
                value = saleable * price
                gross += value
        if value is None:
            complete = False
        output.append({**p, 'potential_gross_USD': None if value is None else str(value),
                       'valuation_gap': reason, 'quote_age_days': age})
    known_cost = Decimal(0)
    missing_costs=[]
    required={'electricity','extraction','purification','storage','transport','capital_allocation','other_operations'}
    if set(costs) != required:
        raise ValueError('explicit complete cost-category set required')
    for key, amount in costs.items():
        if amount is None:
            missing_costs.append(key)
        else:
            known_cost += number(amount)
    net = gross-known_cost if complete and not missing_costs else None
    return {'experiment_id':experiment_id,'scientific_outcome':scientific_outcome,
            'economic_as_of':as_of,'currency':'USD','products':output,
            'priced_subset_potential_gross_USD':str(gross),
            'all_products_valued':complete,'known_cost_USD':str(known_cost),
            'missing_cost_categories':missing_costs,'costs_USD':costs,
            'potential_net_USD':None if net is None else str(net),
            'realized_revenue_USD':None,
            'realized_revenue_status':'NOT_RECORDED_BY_SCENARIO_MODULE',
            'energy_credit':'NONE; heat is not automatically electricity',
            'scope':'ONE declared experiment interval; no live market or inventory dynamics'}


def footer(r):
    gaps = ', '.join(r['missing_cost_categories']) or 'none declared'
    specs = '; '.join(f"{p['product_id']}: {p['valuation_gap'] or p['price_snapshot']['kind']}"
                      + (f" (quote {p['price_snapshot']['quote_date']}, age {p['quote_age_days']} days)"
                         if p.get('price_snapshot') else '') for p in r['products']) or 'no products declared'
    return (f"Scientific outcome: {r['scientific_outcome']}. Economic snapshot: {r['economic_as_of']} (USD).\n"
            f"Products: {specs}. Priced-subset potential gross: ${r['priced_subset_potential_gross_USD']}; "
            f"all products valued: {r['all_products_valued']}.\n"
            f"Potential net: {r['potential_net_USD'] if r['potential_net_USD'] is not None else 'UNRESOLVED'}; "
            f"missing cost categories: {gaps}. Realized revenue: NOT RECORDED.\n")
