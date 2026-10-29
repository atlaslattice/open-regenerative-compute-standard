"""Installed capital inventory only; no financing or unsupported cost scaling."""
from decimal import Decimal

def installed_capex(components):
    seen=set();known=Decimal(0);missing=[]
    for c in components:
        if not c['asset_id'] or c['asset_id'] in seen:raise ValueError('duplicate physical asset')
        seen.add(c['asset_id'])
        if c['currency']!='USD':raise ValueError('explicit upstream currency conversion required')
        if c['installed_cost_USD'] is None:missing.append(c['asset_id']);continue
        if not c.get('cost_date') or not c.get('source'):raise ValueError('dated source required')
        value=Decimal(str(c['installed_cost_USD']))
        if not value.is_finite() or value<0:raise ValueError('invalid cost')
        known+=value
    return {'known_installed_capex_USD':str(known),'missing_assets':missing,
            'total_installed_capex_USD':None if missing else str(known),
            'financing_and_replacement_costs':'NOT_CALCULATED'}
