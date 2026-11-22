"""ORCS v0.2 Texas DPA planning sensitivities, not a capacity forecast.
All outputs are scenario math with unknown grade and transport permissions.
"""
import json
import argparse
from dataclasses import asdict, dataclass

TYLER_REPORTED_CRUDE_THROUGHPUT_BPD = 74000.0
EAST_COAST_DISTILLATE_IMPORTS_2025_MBBL = 45.424

@dataclass(frozen=True)
class Case:
    name: str
    expansion_crude_bpd: float
    incremental_qualified_distillate_yield: float
    reachable_fraction: float
    import_displacement_fraction: float
    diverted_exports_fraction: float
    illustrative_import_value_usd_per_bbl: float = 100.0
    illustrative_export_value_usd_per_bbl: float = 100.0
    domestic_freight_usd_per_bbl: float = 6.0
    domestic_freight_value_added_fraction: float = 0.8

def simulate(case: Case):
    for field in ('expansion_crude_bpd','incremental_qualified_distillate_yield','reachable_fraction',
                  'import_displacement_fraction','diverted_exports_fraction',
                  'illustrative_import_value_usd_per_bbl','illustrative_export_value_usd_per_bbl',
                  'domestic_freight_usd_per_bbl','domestic_freight_value_added_fraction'):
        val=getattr(case,field)
        if val < 0:
            raise ValueError(f'Negative input: {field}')
    for field in ('incremental_qualified_distillate_yield','reachable_fraction',
                  'import_displacement_fraction','diverted_exports_fraction','domestic_freight_value_added_fraction'):
        if getattr(case,field)>1:
            raise ValueError(f'Fraction above unity: {field}')
    incremental=case.expansion_crude_bpd*365*case.incremental_qualified_distillate_yield
    deliverable=incremental*case.reachable_fraction
    displaced=min(EAST_COAST_DISTILLATE_IMPORTS_2025_MBBL*1e6,
                  deliverable*case.import_displacement_fraction)
    forgone=displaced*case.diverted_exports_fraction
    gross_imports_avoided=displaced*case.illustrative_import_value_usd_per_bbl
    exports_forgone=forgone*case.illustrative_export_value_usd_per_bbl
    freight_spend=displaced*case.domestic_freight_usd_per_bbl
    return {
        'name':case.name,
        'status':'HYPOTHETICAL_UNCALIBRATED',
        'existing_Tyler_throughput_bpd_context_only':TYLER_REPORTED_CRUDE_THROUGHPUT_BPD,
        'incremental_qualified_distillate_bbl_y':incremental,
        'hypothetical_deliverable_bbl_y':deliverable,
        'import_displacement_bbl_y':displaced,
        'gross_import_goods_value_avoided_usd_y':gross_imports_avoided,
        'export_goods_value_forgone_usd_y':exports_forgone,
        'first_order_merchandise_balance_change_usd_y':gross_imports_avoided-exports_forgone,
        'gross_domestic_freight_receipts_usd_y':freight_spend,
        'potential_direct_freight_value_added_before_displacement_usd_y':freight_spend*case.domestic_freight_value_added_fraction,
        'total_domestic_turnover_increment_usd_y':None,
        'net_incremental_gdp_usd_y':None,
        'avoided_emergency_losses_usd_y':None,
        'export_authorization':False,
        'route_grade_perm_verified':False,
        'notes':['Synthetic scenario assumptions; no evidence of actual DPA capacity or route.',
                 'Freight receipts are part of turnover, not an additive GDP or net benefit estimate.',
                 'Opportunity costs, refinery capital, imported intermediates, domestic displacement, wage effects and consumer surplus are UNKNOWN.']
    }

def cases():
    # 74,000 bpd is pre-expansion throughput. Expansion delta is UNKNOWN; below are invented sensitivities only.
    return [Case('counterfactual_no_expansion',0,0.25,0.0,1.0,0.0),
            Case('hypothetical_10k_expansion_low',10000,0.2,0.5,1,0),
            Case('hypothetical_20k_expansion_base',20000,0.3,0.75,1,0),
            Case('hypothetical_40k_expansion_high',40000,0.4,1,1,0),
            Case('hypothetical_20k_all_export_diversion',20000,0.3,0.75,1,1)]

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--compact',action='store_true')
    args=parser.parse_args()
    print(json.dumps({'model':'ORCS_TX_DPA_v0.2','results':[simulate(c) for c in cases()]},
                     indent=None if args.compact else 2))
