"""ORCS energy resilience v0.5: observed records only; unknowns preserved."""
from dataclasses import dataclass
from typing import Optional
import json

@dataclass(frozen=True)
class GridHour:
    balancing_authority: str
    period_utc: str
    demand_mw: Optional[float]
    net_generation_mw: Optional[float]
    net_imports_mw: Optional[float] = None
    source_url: str = ''

def accounting_gap(row: GridHour):
    """Diagnostic only; never call generation-load difference spare capacity."""
    if None in (row.demand_mw, row.net_generation_mw, row.net_imports_mw):
        return {'status':'UNKNOWN','accounting_gap_mw':None,'surplus_mw':None,'blackout_risk':None}
    return {'status':'DIAGNOSTIC_ONLY','accounting_gap_mw':round(row.net_generation_mw+row.net_imports_mw-row.demand_mw,3),
            'surplus_mw':None,'blackout_risk':None}

def critical_load_coverage(critical_load_mw, firm_local_generation_mw, usable_storage_mwh, duration_h,
                           islanding_verified=False, equipment_verified=False):
    values=(critical_load_mw,firm_local_generation_mw,usable_storage_mwh,duration_h)
    if any(v is None for v in values):
        return {'status':'UNKNOWN','can_cover':None,'capacity_gap_mwh':None}
    if any(v<0 for v in values):
        raise ValueError('Negative input')
    if duration_h==0:
        return {'status':'ZERO_DURATION','can_cover':None,'capacity_gap_mwh':0}
    shortage=max(0,critical_load_mw-firm_local_generation_mw)*duration_h
    theoretical=usable_storage_mwh>=shortage
    return {'status':'ENGINEERING_VERIFICATION_REQUIRED',
            'can_cover':theoretical if islanding_verified and equipment_verified else None,
            'theoretical_energy_sufficient':theoretical,
            'capacity_gap_mwh':max(0,shortage-usable_storage_mwh),
            'islanding_verified':islanding_verified,'equipment_verified':equipment_verified,
            'note':'Energy balance alone does not verify instantaneous power, black start, protection or operability.'}

if __name__ == '__main__':
    print(json.dumps({'model':'ORCS v0.5','status':'NO_OBSERVED_ROWS_IMPORTED','feeds':'registry.json',
                      'live_balancing_authority_capacity':'UNKNOWN','blackout_probability':'UNKNOWN'},indent=2))
