"""Five-year national ramp with operator, public transfer and externality accounts.
Run: python3 national_five_year.py --output national-results.json
"""
import argparse
import json
import math
from pathlib import Path
from payback import compare
from public_value import evaluate

ROOT=Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT/name).read_text())


def national(n,a,b,v):
    ramp=n['year_average_active_fraction_of_target']
    assert len(ramp)==5 and all(0<x<=1 for x in ramp)
    assert all(x<=y for x,y in zip(ramp,ramp[1:])) and ramp[-1]==1
    f={r['feed']:r for r in compare(a,b)['rows'] if r['route']=='toll' and r['service_fee_usd_input_t']==0}
    pub=evaluate(a,b,v)['rows']
    results=[]
    for perstate in n['target_units_per_state_cases']:
        fleet=n['states']*perstate
        active=[fleet*x for x in ramp]
        for label,p in n['program_cases'].items():
            share=p['enriched_unit_share']
            weights={'enriched_selected_stream':share,'legacy_sensitivity':1-share}
            investment=fleet*(a['installed_capital_usd']+a['one_time_development_usd'])*(1+n['shared_initial_engineering_fraction_of_unit_capital'])
            yearly=[]
            for year,units in enumerate(active,1):
                totalfeed=units*a['intake_t_day']*a['operating_days_year']
                income=sum(weights[k]*f[k]['net_product_receipts_usd_day'] for k in weights)*units*a['operating_days_year']
                localcost=sum(weights[k]*f[k]['cash_operating_cost_usd_day'] for k in weights)*units*a['operating_days_year']
                overhead=localcost*n['shared_annual_operations_fraction_of_unit_cash_cost']
                service=totalfeed*(1-share)*p['legacy_service_fee_usd_t']
                output={m:sum(weights[k]*a['feed_scenarios'][k]['fractions'][m]*a['feed_scenarios'][k]['capture']*a['feed_scenarios'][k]['buyer_acceptance'] for k in weights)*totalfeed*a['metals'][m]['refinery_recovery'] for m in a['metals']}
                accepted={m:sum(weights[k]*a['feed_scenarios'][k]['fractions'][m]*a['feed_scenarios'][k]['capture']*a['feed_scenarios'][k]['buyer_acceptance'] for k in weights)*totalfeed for m in a['metals']}
                newlycommissioned=units-(active[year-2] if year>1 else 0)
                yearly.append({'year':year,'average_active_units':units,'input_t':totalfeed,
                    'legacy_input_t':totalfeed*(1-share),'selected_enriched_input_t':totalfeed*share,
                    'finished_metal_t':output,'accepted_metal_t':accepted,
                    'net_product_receipts_usd':income,'local_cash_operating_cost_usd':localcost,
                    'shared_operations_allowance_usd':overhead,'service_payment_usd':service,
                    'initial_investment_usd':newlycommissioned/fleet*investment,
                    'operator_cash_after_current_year_investment_usd':income+service-localcost-overhead-newlycommissioned/fleet*investment})
            opnet=sum(y['operator_cash_after_current_year_investment_usd'] for y in yearly)
            transfers=sum(y['service_payment_usd'] for y in yearly)
            systemmarket=opnet-transfers
            outputs={m:sum(y['finished_metal_t'][m] for y in yearly) for m in a['metals']}
            accepted={m:sum(y['accepted_metal_t'][m] for y in yearly) for m in a['metals']}
            feed=sum(y['input_t'] for y in yearly)
            legacy=sum(y['legacy_input_t'] for y in yearly)
            enriched=sum(y['selected_enriched_input_t'] for y in yearly)
            physicalflags=[]
            for field,required in [('annual_available_enriched_feed_t',yearly[-1]['selected_enriched_input_t']),
                    ('annual_domestic_finished_copper_capacity_t',yearly[-1]['finished_metal_t']['copper']),
                    ('annual_domestic_finished_aluminum_capacity_t',yearly[-1]['finished_metal_t']['aluminum'])]:
                supplied=n[field]
                physicalflags.append({'constraint':field,'required_year5_t':required,
                    'capacity_limit_t':supplied,'status':'UNKNOWN' if supplied is None else 'FAIL' if required>supplied else 'PASS'})
            for alpha in n['additionality_cases']:
                benefits={}
                for key in ['net_ghg_saving_proxy_tco2e_5yr','upstream_energy_saving_proxy_gwh_equivalent_before_extra_site_energy','copper_ore_equivalent_t_5yr','iron_ore_equivalent_t_5yr']:
                    benefits[key]=sum(weights[k]*next(r[key] for r in pub if r['location']=='mainland' and r['feed']==k and r['additionality_and_virgin_displacement_fraction']==alpha and r['shadow_carbon_usd_tco2e']==100 and r['resilience_shadow_usd_finished_nonferrous_t']==0) for k in weights)*sum(active)/5
                climate=benefits['net_ghg_saving_proxy_tco2e_5yr']*n['shadow_carbon_usd_tco2e']
                critical=(outputs['copper']+outputs['aluminum'])*alpha*n['domestic_delivery_fraction_assumption']
                resilience=critical*n['resilience_shadow_usd_finished_nonferrous_t']
                expanded=systemmarket+climate+resilience
                imports={m:outputs[m]*alpha*n['domestic_delivery_fraction_assumption']*n['import_replacement_fraction_sensitivity'] for m in ['copper','aluminum']}
                potentialtrade=sum(imports[m]*a['metals'][m]['finished_usd_t'] for m in imports)
                results.append({'program':label,'target_units_per_state':perstate,'target_national_units':fleet,
                    'status':'CONDITIONAL; feed/processing capacity not verified','additionality_fraction':alpha,
                    'five_year_active_unit_years':sum(active),'five_year_input_t':feed,
                    'five_year_legacy_input_t':legacy,'five_year_enriched_input_t':enriched,
                    'legacy_stock_processed_once_percent':100*legacy/n['legacy_stock_t_assumption'],
                    'initial_investment_usd':investment,'working_cash_envelope_at_full_fleet_usd':fleet*a['initial_cash_reserve_usd'],
                    'five_year_finished_metal_t':outputs,'five_year_accepted_metal_t':accepted,
                    'five_year_managed_residual_t':feed-sum(accepted.values()),
                    'operator_net_after_initial_investment_usd':opnet,
                    'operator_roi_percent':100*opnet/investment,
                    'five_year_service_payments_usd':transfers,
                    'net_market_value_after_costs_excluding_transfers_usd':systemmarket,
                    'climate_public_value_proxy_usd':climate,'resilience_shadow_value_usd':resilience,
                    'expanded_net_value_proxy_usd':expanded,'expanded_return_proxy_percent_NOT_financial_roi':100*expanded/investment,
                    'potential_import_replacement_t_NOT_actual':imports,
                    'gross_import_purchase_equivalent_usd_NOT_additive':potentialtrade,
                    'bauxite_equivalent_t_range':[outputs['aluminum']*alpha*x for x in v['bauxite_t_per_primary_aluminum_t_range']],
                    'remaining_public_benefit_needed_usd_legacy_input_t':max(0,-expanded)/legacy if legacy else None,
                    'constraint_checks':physicalflags,'benefit_proxies':benefits,'annual':yearly})
    for r in results:
        assert r['five_year_legacy_input_t'] <= n['legacy_stock_t_assumption']
        assert math.isclose(sum(r['five_year_accepted_metal_t'].values())+r['five_year_managed_residual_t'],r['five_year_input_t'])
        assert math.isclose(r['operator_net_after_initial_investment_usd']-r['five_year_service_payments_usd'],r['net_market_value_after_costs_excluding_transfers_usd'],abs_tol=1e-4)
        assert math.isclose(sum(y['initial_investment_usd'] for y in r['annual']),r['initial_investment_usd'])
    # Service payments must not change physical outputs or expanded system value.
    for r in results:
        if r['program']=='mixed_program_service_contract_sensitivity':
            match=next(x for x in results if x['program']=='mixed_program_unfunded' and x['target_units_per_state']==r['target_units_per_state'] and x['additionality_fraction']==r['additionality_fraction'])
            assert match['five_year_finished_metal_t']==r['five_year_finished_metal_t']
            assert math.isclose(match['expanded_net_value_proxy_usd'],r['expanded_net_value_proxy_usd'],abs_tol=1e-4)
    return {'status':n['status'],'assumptions':n,'executed_case_count':len(results),'rows':results}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    r=national(*[load(s) for s in ['national-assumptions.json','payback-assumptions.json','example.json','public-value-assumptions.json']])
    s=json.dumps(r,indent=2,allow_nan=False)+'\n'
    if args.output:args.output.write_text(s)
    else:print(s,end='')


if __name__=='__main__':main()
