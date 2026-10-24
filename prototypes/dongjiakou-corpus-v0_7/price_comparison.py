"""Reference prices with explicit units; no automatic installed-cost aggregation."""
import csv,math
from pathlib import Path


def cny_to_usd(value,fx):
    if value is None:return None
    if value<0 or fx<=0:raise ValueError('Invalid conversion')
    return value/fx


def matched_component_price(reference,candidate):
    """Only return a cost when documented procurement scope and duty match.

    Actual equality/engineering equivalence requires independent confirmation.
    An aggregate civil/process package is not a membrane-element quotation.
    """
    keys=['component','price_unit','quantity','supply_scope','duty_basis']
    if candidate is None:return None
    if candidate.get('scope_match_confirmed') is not True or not candidate.get('source_url'):return None
    if any(reference.get(k) is None or candidate.get(k) is None or reference[k]!=candidate[k] for k in keys):return None
    value=candidate.get('amount_usd')
    return value if value is not None and value>=0 else None


def regional_total(city_actual,industrial_direct_actual,overlap):
    if any(x is None for x in [city_actual,industrial_direct_actual,overlap]):return None
    if min(city_actual,industrial_direct_actual,overlap)<0 or overlap>min(city_actual,industrial_direct_actual):raise ValueError('Invalid wastewater boundary')
    return city_actual+industrial_direct_actual-overlap


def price_outputs(inputs,root):
    with (Path(root)/'china_price_anchors_needs_sourcing.csv').open() as f:anchors=list(csv.DictReader(f))
    rows=[]
    for a in anchors:
        point=float(a['china_equipment_anchor_usd']) if a['china_equipment_anchor_usd'] else None
        lo=float(a['china_equipment_anchor_usd_low']);hi=float(a['china_equipment_anchor_usd_high'])
        rows.append(dict(anchor_id=a['anchor_id'],component=a['component_slot'],item=a['item'],price_kind=a['anchor_kind'],
            reference_price_unit=a['quoted_unit'].replace('CNY','USD'),
            deepseek_reference_usd=point,deepseek_reference_usd_low=lo,deepseek_reference_usd_high=hi,
            atlas_lattice_reference_usd=point,atlas_lattice_reference_usd_low=lo,atlas_lattice_reference_usd_high=hi,
            atlas_reference_status='Copiedprovisionalreference;NEEDS SOURCING URLS;notinstalledcost',
            corpus_matched_component_usd=matched_component_price({},None),
            corpus_match_status='NULL:no documented like-for-like componentmatch;historicalaggregatesarenotunitquotes',
            pump_clarification_pending=a['component_slot'] in ['high_pressure_pumps','energy_recovery'],
            supply_scope=a['reported_scope'],limits=a['scope_limitation'],source_url=None,
            actual_quotation_usd=None,atlas_installed_cost_usd=None,include_in_total=False))
    # Arithmetic reproduction, not scale economics or a lower/upper bound.
    q=153643.18;capacity=5.5*24;budget=11745000
    mvr=[dict(assumed_residual_t_d_at_density1=q,assumed_small_project_capacity_t_d=capacity,
        reported_small_project_budget_cny=budget,
        linear_extrapolation_cny=q/capacity*budget,
        linear_extrapolation_usd=q/capacity*budget/7.25,
        actual_corpus_zld_cost_usd=None,is_lower_bound=False,is_upper_bound=False,
        note='Arithmeticonly;capacityfeedvs evaporationdutyunknown;phase separations preconcentration and economyofscale unmodeled;notfeasibilitydecision')]
    return dict(component_price_comparison=rows,mvr_linear_exposure=mvr,
                regional_wastewater_summary=dict(city_reported_average_mgd=28,
                    direct_industrial_actual_mgd=None,overlap_mgd=None,
                    combined_actual_mgd=regional_total(28,None,None),
                    note='Cityincludesindustrialsewerflows;notallregionalindustrialoutfalls;28MGDundatedreportedaverage'))


def train_block(product_mgd,recovery,duty_trains,complete_spare_trains):
    if product_mgd<=0 or not 0<recovery<1 or duty_trains<1 or complete_spare_trains<0:
        raise ValueError('Invalid train scenario')
    unit=product_mgd/duty_trains
    return dict(product_mgd=product_mgd,assumed_recovery=recovery,
                ro_feed_mgd=product_mgd/recovery,ro_reject_mgd=product_mgd/recovery-product_mgd,
                duty_trains=duty_trains,assumed_complete_spare_trains=complete_spare_trains,
                installed_complete_trains=duty_trains+complete_spare_trains,
                product_per_train_mgd=unit,
                product_with_one_complete_train_unavailable_mgd=min(duty_trains,duty_trains+complete_spare_trains-1)*unit,
                actual_high_pressure_pump_flow_mgd=None,actual_pressure_bar=None,
                actual_installed_pump_cost_usd=None,
                note='HydraulicROfeednotnecessarilymainHPPflowwithpressureexchanger;completesparetrainnotmerelysparepump;commonfailureandswitchingnotmodeled')


def pump_train_outputs(inputs):
    rows=[]
    for reuse_product in [8,16,30]:
        for n in [3,4]:
            for spare in [0,1]:
                for fluid,product,recovery in [('SWRO',30,.475),('Advancedreuse',reuse_product,.9)]:
                    rows.append(dict(pair_scenario=f'SWRO30_reuse{reuse_product}',fluid=fluid,
                      **train_block(product,recovery,n,spare),
                      reuse_supply_status='30MGDreuseproductrequires33.33MGDfeedat90percent;city28MGDreportedaveragenotunallocated;directindustrialactualunknown',
                      base_case_selection='SCENARIOONLY;actualreusecapacitynotselected'))
    return dict(pump_train_scenarios=rows)
