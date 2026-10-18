"""Reproducible screening model, not a project forecast. Python standard library only."""
from pathlib import Path
import json, csv

ROOT = Path(__file__).resolve().parent

def payment(p, r, n=30):
    return p/n if r == 0 else p*r/(1-(1+r)**(-n))

def run(base, cfg):
    s = next(x for x in base['scenarios'] if x['capture_fraction'] == cfg['capture'])
    c = s['county_financing_cases'][cfg['county_budget_index']]
    w = s['state_WW_financing_cases'][2]
    m = s['manure_national_unallocated']; b = s['macro']
    def component(name, capital, margin, income):
        net = margin + payment(capital, .05)
        income = max(net, 0) if income is None else income
        return dict(name=name, base_capital=capital, income=income, cost=income-net)
    components = [
        component('County food/yard/wood',c['capex_usd'],c['annual_margin_after_debt_usd'],c['annual_product_energy_receipts_assumed_usd']+c['annual_gate_receipts_assumed_usd']),
        component('Local manure',m['capex_usd'],m['annual_margin_after_debt_usd'],m['annual_product_receipts_assumed_usd']),
        component('State wastewater nutrients',w['capex_usd'],w['annual_margin_after_debt_usd'],w['annual_nutrient_receipts_assumed_usd']),
        component('Three-plant full ZLD',b['brine_full_ZLD_30y_option_capex_usd'],b['brine_full_ZLD_30y_option_margin_usd'],None),
        component('Industrial food floor',b['industrial_food_capex_floor_usd'],b['industrial_food_finance_floor_margin_usd'],s['industrial_food']['nutrient_receipts_assumed_usd']+s['industrial_food']['power_heat_receipts_assumed_usd'])]
    capital = sum(x['base_capital'] for x in components) * cfg['capital_factor']
    income = sum(x['income'] for x in components); cost = sum(x['cost'] for x in components)
    cohorts=[]
    powers=[s['municipal_county_streams']['food']['net_power_MWh'],m['net_power_MWh'],0,0,s['industrial_food']['net_power_MWh']]
    nutrients=[{k:sum(s['municipal_county_streams'][x]['nutrients']['incremental_first_season_t_assumed'][k] for x in ['food','yard']) for k in ['N','P','K2O']},m['nutrients']['incremental_first_season_t_assumed'],dict(N=0,P=0,K2O=0),dict(N=0,P=0,K2O=0),s['industrial_food']['nutrients']['incremental_first_season_t_assumed']]
    for j,comp in enumerate(components):
        # The three-plant brine option is procured upfront; other portfolios stage draws.
        fractions=[1.] if j==3 else cfg['draw_fractions']
        for i,f in enumerate(fractions):
            principal=comp['base_capital']*cfg['capital_factor']*f
            cohorts.append(dict(component_index=j,draw_year=i+1,commissioned_year=i+1+cfg['component_lags_years'][j],fraction=f,
                                principal=principal,balance=0.,debt_payment=payment(principal,cfg['interest_rate']),
                                income=comp['income']*f,cost=comp['cost']*f,power=powers[j]*f,
                                nutrients={k:nutrients[j][k]*f for k in ['N','P','K2O']}))
    assert abs(sum(x['principal'] for x in cohorts)-capital)<.01
    annual=[]; cumulative=0.; pv=0.
    last_debt_year = max(x['draw_year']+29 for x in cohorts)
    for year in range(1,last_debt_year+1):
        for x in cohorts:x['activation']=1 if year>x['commissioned_year'] else .5 if year==x['commissioned_year'] else 0
        active=sum(x['principal']*x['activation'] for x in cohorts)/capital
        commissioned=sum(x['principal'] for x in cohorts if year>=x['commissioned_year'])/capital
        draws=sum(x['principal'] for x in cohorts if year==x['draw_year'])
        debt=interest=principal=0.
        for x in cohorts:
            if year==x['draw_year']: x['balance']=x['principal']
            if x['draw_year']<=year<=x['draw_year']+29:
                i=x['balance']*cfg['interest_rate']; p=min(x['balance'],max(0,x['debt_payment']-i))
                debt+=i+p;interest+=i;principal+=p;x['balance']=max(0,x['balance']-p)
        under_construction=sum(x['principal'] for x in cohorts if x['draw_year']<=year<x['commissioned_year'])
        carrying=under_construction*cfg['construction_carry_rate']
        receipts=sum(x['income']*x['activation'] for x in cohorts); operating=sum(x['cost']*x['activation'] for x in cohorts); cash=receipts-operating-carrying-debt
        support=max(0,-cash); cumulative+=cash
        if year<=30: pv+=support/(1+cfg['fiscal_discount_rate'])**year
        annual.append(dict(year=year,calendar_year=2026+year,within_30_year_window=year<=30,
                           capital_draw=draws,commissioned_fraction=commissioned,operating_fraction=active,
                           modeled_receipts=receipts,operating_costs_and_reserves=operating,construction_carry=carrying,
                           debt_service=debt,interest=interest,principal_repaid=principal,outstanding_principal=sum(x['balance'] for x in cohorts),
                           net_cash=cash,required_public_support=support,cumulative_net_cash=cumulative,
                           new_net_power_MWh=sum(x['power']*x['activation'] for x in cohorts),
                           new_N_first_season_t=sum(x['nutrients']['N']*x['activation'] for x in cohorts),
                           new_P_first_season_t=sum(x['nutrients']['P']*x['activation'] for x in cohorts),
                           new_K2O_first_season_t=sum(x['nutrients']['K2O']*x['activation'] for x in cohorts)))
    first30=annual[:30]
    product_proxy=(c['annual_product_energy_receipts_assumed_usd']+m['annual_product_receipts_assumed_usd']+w['annual_nutrient_receipts_assumed_usd']+s['industrial_food']['nutrient_receipts_assumed_usd']+s['industrial_food']['power_heat_receipts_assumed_usd'])
    summary=dict(id=cfg['id'],name=cfg['name'],capture=cfg['capture'],interest_rate=cfg['interest_rate'],
                 installed_capital_with_planning_allowance=capital,base_installed_capital=capital/cfg['capital_factor'],
                 county_portfolio_last_commissioning_year=max(x['commissioned_year'] for x in cohorts if x['component_index']==0),
                 last_capital_draw_year=max(x['draw_year'] for x in cohorts),last_commissioning_year=max(x['commissioned_year'] for x in cohorts),
                 first_year_at_least_half_commissioned=next(x['year'] for x in annual if x['commissioned_fraction']>=.5),
                 steady_annual_cash_with_all_tranche_debt=income-cost-payment(capital,cfg['interest_rate']),
                 public_support_first_30_years=sum(x['required_public_support'] for x in first30),
                 public_support_PV_5pct_first30=pv,peak_annual_public_support_first30=max(x['required_public_support'] for x in first30),
                 outstanding_principal_end_year30=first30[-1]['outstanding_principal'],
                 debt_payments_after_year30=sum(x['debt_service'] for x in annual[30:]),
                 final_debt_payment_year=last_debt_year,
                 priced_product_energy_sales_proxy_steady=product_proxy,
                 new_power_TWh_steady=b['new_food_manure_net_power_MWh']/1e6,
                 new_first_season_nutrients_t=b['additional_first_season_nutrients_t_assumed'],
                 construction_labor_budget_jobyears_low=capital*.20/140000,
                 construction_labor_budget_jobyears_high=capital*.35/90000,
                 county_reactors_required=3144,county_benefit_gate='REQUIRED; NONE VERIFIED BY THIS MODEL',
                 inflation_assumption='0%; flat nominal planning dollars, not an inflation forecast',
                 actual_import_displacement_t=None,net_GDP_effect_usd=None,net_trade_balance_effect_usd=None)
    return dict(config=cfg,components=components,summary=summary,annual=annual)

def main():
    base=json.loads((ROOT/'base-network-results.json').read_text())
    config=json.loads((ROOT/'scenario-inputs.json').read_text())
    results=[run(base,c) for c in config['scenarios']]
    output=dict(version='0.1',status='SIMULATED / PROPOSED / NO REALIZED CREDIT',method=config['method'],scenarios=results)
    (ROOT/'abc-results.json').write_text(json.dumps(output,indent=2)+'\n')
    with (ROOT/'abc-summary.csv').open('w',newline='') as f:
        rows=[x['summary'] for x in results];w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (ROOT/'abc-annual.csv').open('w',newline='') as f:
        fields=['scenario']+list(results[0]['annual'][0]);w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in results:
            for a in r['annual']:w.writerow(dict(scenario=r['summary']['id'],**a))
    print(json.dumps([r['summary'] for r in results],indent=2))

if __name__=='__main__':main()
