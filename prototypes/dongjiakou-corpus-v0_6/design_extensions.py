"""Proposed delivery/incentive alternatives. Not quotations or contract advice."""
import csv
from pathlib import Path


def schedule_comparison(reference_months, multiplier, prerequisites_months=None,
                        acceptance_months=None):
    if reference_months <= 0 or multiplier < 1:
        raise ValueError('Invalid schedule assumption')
    construction=reference_months*multiplier
    return dict(reference_construction_months=reference_months,
                allowance_multiplier=multiplier, proposed_construction_months=construction,
                prerequisites_months=prerequisites_months, acceptance_months=acceptance_months,
                total_project_months=None if prerequisites_months is None or acceptance_months is None
                  else prerequisites_months+construction+acceptance_months,
                status='SCENARIO construction clock only; no time-to-commission guarantee')


def recovery_incentive(sold_t, consumed_t, qualified_available_t,
                       sales_unit_value, substitute_unit_value, attributable_cost,
                       baseline_net_value, share, cap, gates_verified):
    """Sold and consumed are exclusive; net value after attributable lifecycle cost.

    Attributable costs include recovery CAPEX charge, OPEX, qualification, logistics,
    final residual allocation and third-party selling fees. Exclude this award itself.
    A baseline is required to avoid claiming existing operations as new performance.
    """
    required=[sold_t,consumed_t,qualified_available_t,sales_unit_value,
              substitute_unit_value,attributable_cost,baseline_net_value,share,cap]
    if any(x is None for x in required) or gates_verified is not True:
        return dict(incremental_net_value_usd=None, incentive_usd=None,
                    status='UNRESOLVED; no award recognized')
    if any(x < 0 for x in required) or share > 1:
        raise ValueError('Invalid award input')
    if sold_t+consumed_t > qualified_available_t+1e-9:
        raise ValueError('Sold plus consumed exceeds qualified inventory')
    gross=sold_t*sales_unit_value+consumed_t*substitute_unit_value
    net=gross-attributable_cost-baseline_net_value
    award=min(cap,share*max(0,net))
    return dict(incremental_net_value_usd=net,incentive_usd=award,
                status='SCENARIO only; independent verification and contract terms required')


def management_cost(policy):
    salary=policy['salary_usd_year'];fte=policy['management_fte']
    years=policy['management_duration_years'];burden=policy['employer_burden_usd_year']
    expense=policy['verified_reimbursable_costs_usd']
    values=[salary,fte,years,burden,expense]
    if any(x is None for x in values):return None
    if any(x < 0 for x in values):raise ValueError('Negative management cost')
    return (salary+burden)*fte*years+expense


def integrated_outputs(inputs, root):
    total=inputs['historical_cost_leverage']['construction_total_usd']
    groups=inputs['historical_construction_groups']
    marine=151493815
    disjoint=dict(named_process_equipment=groups['process_equipment'],
      nonmarine_other_physical=groups['other_physical_works']-marine,
      marine=marine, indirect_allowances=groups['escalation_contingency_insurance_general_conditions'])
    group_rows=[dict(category=k,estimate_2025_usd=v,share_of_construction=v/total,
                    scope='Disjoint installed-cost groups; estimates not expenses; not a pure labor split') for k,v in disjoint.items()]
    schedule=inputs['schedule_policy']
    schedules=[dict(name=f'{multiplier:g}x reported construction duration',**schedule_comparison(
        schedule['reference_construction_months'],multiplier,
        schedule['corpus_prereadiness_months'],schedule['corpus_acceptance_after_first_water_months']))
        for multiplier in [1,1.5,schedule['allowance_multiplier'],3]]
    awards=[]
    # Normalized 1m net-value scenarios; no mineral market assumption or actual award.
    for margin in [-100000,0,1000000]:
        for rate in [.05,.1,.2]:
            cost=max(0,1e6-margin)
            r=recovery_incentive(1000,0,1000,1000,0,cost,0,rate,100000,True)
            awards.append(dict(hypothetical_value_before_cost_usd=1e6,
                hypothetical_attributable_cost_usd=cost, assumed_share_rate=rate,
                assumed_cap_usd=100000,**r))
    with (Path(root)/'corpus_2026_cost_detail.csv').open() as f: cc26=list(csv.DictReader(f))
    redesign=[]
    for physical_cut in [0,.1,.2,.4,.5]:
        # Only disjoint nonmarine-other works reduced; no stacked generic range.
        for equip_cut in [0,.5]:
            savings=disjoint['nonmarine_other_physical']*physical_cut+disjoint['named_process_equipment']*equip_cut
            redesign.append(dict(assumed_nonmarine_other_physical_cut=physical_cut,
                assumed_named_equipment_cut=equip_cut, marine_saving_usd=0,
                indirect_saving_usd=0, modeled_gross_savings_usd=savings,
                modeled_reduction_fraction=savings/total,
                replacement_lattice_costs_usd=None, net_alternative_total_usd=None,
                status='ASSUMED disjoint cuts, not generic benchmarks or achieved savings; quantities unknown'))
    reuse=[]
    for q in [0,5,11,16]:
        reuse.append(dict(assumed_equivalent_firm_demand_mgd=30,
            assumed_incremental_qualified_firm_reuse_mgd=q,
            illustrative_desal_gap_mgd=max(0,30-q),
            actual_incremental_qualified_reuse_mgd=inputs['wastewater_integration']['firm_reuse_at_required_quality_mgd'],
            note='Demand substitution illustration only; no automatic subtraction of committed16MGD from30MGD project; demand/quality/drought/reuse return flows require verification'))
    return dict(disjoint_historical_cost_groups=group_rows,schedule_sensitivity=schedules,
                recovery_incentive_sensitivity=awards,corpus_2026_cost_detail=cc26,
                redesign_sensitivity=redesign,reuse_demand_sensitivity=reuse,
                management_policy_summary=dict(spend_linked_fee_rate=inputs['management_policy']['spend_linked_management_fee_rate'],
                    salary_and_verified_expenses_usd=management_cost(inputs['management_policy']),
                    outcome_incentives_usd=None,total_management_cost_usd=None,
                    realized_management_incentives_usd=0,
                    note='No automatic spend-based fee; salary expenses and outcome awards remain TBD costs, not zero. Historical comparators unchanged.'))
