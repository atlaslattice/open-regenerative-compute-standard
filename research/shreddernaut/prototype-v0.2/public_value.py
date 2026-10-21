"""Separate operator cash, physical outcomes and illustrative public-value accounts.
Run: python3 public_value.py --output public-value-results.json
"""
import argparse
import json
import math
from pathlib import Path
from five_year import calculate
from model import run, finite_number

ROOT=Path(__file__).resolve().parent


def evaluate(a,b,v):
    years=finite_number(v['years'],'years',1)
    days=finite_number(v['operating_days_year'],'days',1,365)
    totaldays=days*years
    assert years==5 and days==a['operating_days_year'], 'This version reconciles five full v0.4 operating years.'
    assert all(0<=x<=1 for x in v['additionality_and_virgin_displacement_cases'])
    site=run(b)
    site_emissions=(site['electricity_kwh_day']*v['incremental_site_grid_kgco2e_kwh']
                    +site['mobile_equipment_diesel_l_day']*v['incremental_site_diesel_kgco2e_l'])*totaldays/1000
    output=[]
    for location,kwargs in [('mainland',{}),('maui_illustrative',{
            'extra_capital':100000,'extra_fixed_annual':50000,'extra_freight_recovered_t':250})]:
        finance=calculate(a,b,**kwargs)
        for feedname,feed in a['feed_scenarios'].items():
            accepted={m:a['intake_t_day']*feed['fractions'][m]*feed['capture']*feed['buyer_acceptance']*totaldays for m in a['metals']}
            finished={m:q*a['metals'][m]['refinery_recovery'] for m,q in accepted.items()}
            financial=next(x for x in finance if x['feed']==feedname and x['route']=='toll' and x['service_fee_usd_input_t']==0)
            investment=financial['initial_investment_excluding_working_cash_usd']
            market_net=financial['five_year_net_cash_after_initial_investment_usd']
            gross_credit=sum(accepted[m]/v['metric_t_per_short_t']*v['warm_recycling_credit_tco2e_per_short_t'][m] for m in accepted)
            energy=sum(accepted[m]/v['metric_t_per_short_t']*v['warm_energy_credit_mmbtu_per_short_t'][m] for m in accepted)
            extra_emissions=site_emissions
            if location=='maui_illustrative':
                extra_emissions+=(site['electricity_kwh_day']*v['maui_extra_grid_kgco2e_kwh']*totaldays
                    +sum(accepted.values())*v['maui_extra_shipping_km']*v['maui_extra_shipping_kgco2e_t_km'])/1000
            for alpha in v['additionality_and_virgin_displacement_cases']:
                netghg=gross_credit*alpha-extra_emissions
                nf=(finished['aluminum']+finished['copper'])*alpha
                for carbon in v['shadow_carbon_usd_tco2e_cases']:
                    climate=netghg*carbon
                    for resilience in v['resilience_shadow_usd_finished_nonferrous_t_cases']:
                        security=nf*resilience
                        expanded=market_net+climate+security
                        output.append({'location':location,'feed':feedname,'additionality_and_virgin_displacement_fraction':alpha,
                            'shadow_carbon_usd_tco2e':carbon,'resilience_shadow_usd_finished_nonferrous_t':resilience,
                            'accepted_metal_input_t_5yr':accepted,'finished_metal_output_t_5yr':finished,
                            'qualified_additional_nonferrous_t_5yr':nf,
                            'upstream_energy_saving_proxy_gwh_equivalent_before_extra_site_energy':energy*alpha*0.00029307107,
                            'net_ghg_saving_proxy_tco2e_5yr':netghg,
                            'copper_ore_equivalent_t_5yr':finished['copper']*alpha/(v['copper_ore_grade_fraction']*v['copper_mine_recovery_fraction']),
                            'bauxite_equivalent_t_5yr_range':[finished['aluminum']*alpha*x for x in v['bauxite_t_per_primary_aluminum_t_range']],
                            'iron_ore_equivalent_t_5yr':accepted['ferrous']*alpha*v['iron_ore_avoided_t_per_steel_scrap_t'],
                            'gross_import_purchase_equivalent_usd_5yr_not_additive':sum(finished[m]*a['metals'][m]['finished_usd_t'] for m in ['aluminum','copper'])*alpha,
                            'initial_investment_usd':investment,
                            'operator_net_cash_no_service_fee_usd_5yr':market_net,
                            'operator_roi_percent_no_service_fee':financial['five_year_simple_roi_percent'],
                            'illustrative_climate_public_value_usd':climate,
                            'illustrative_resilience_public_value_usd':security,
                            'expanded_net_value_proxy_usd_5yr':expanded,
                            'expanded_return_proxy_percent_NOT_financial_roi':100*expanded/investment,
                            'remaining_unpriced_public_benefit_needed_for_system_break_even_usd_input_t':max(0,-expanded)/(a['intake_t_day']*totaldays)})
    # Accounting: these public values do not change operator cash, and import values
    # are never included in the expanded net value (would duplicate metal receipts).
    for r in output:
        assert math.isclose(r['expanded_net_value_proxy_usd_5yr'],r['operator_net_cash_no_service_fee_usd_5yr']+r['illustrative_climate_public_value_usd']+r['illustrative_resilience_public_value_usd'])
        assert all(r['finished_metal_output_t_5yr'][m]<=r['accepted_metal_input_t_5yr'][m] for m in a['metals'])
    return {'status':v['status'],'method':'Screening market-value-minus-cost proxy plus explicit carbon and resilience shadow sensitivities; not formal social cost-benefit appraisal, certified LCA, monetized reserve value or credit revenue.',
            'unpriced_outcomes':['Water savings','Tailings/toxicity/biodiversity effects','Site remediation/land value','Methane release or avoided release','Verified shortage-loss avoidance'],
            'assumptions':v,'rows':output}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result=evaluate(*[json.loads((ROOT/n).read_text()) for n in ['payback-assumptions.json','example.json','public-value-assumptions.json']])
    s=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.output:args.output.write_text(s)
    else:print(s,end='')


if __name__=='__main__':main()
