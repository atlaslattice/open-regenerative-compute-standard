"""Illustrative financing only; Python standard library; USD nominal, annual payments.
Run: python calculate.py. This does not change the reactor simulation.
"""
import json
from pathlib import Path

def annual_payment(principal, rate=.05, years=30):
    if principal < 0 or rate < 0 or years <= 0:
        raise ValueError('Invalid financing input')
    return principal / years if rate == 0 else principal * rate / (1-(1+rate)**(-years))

def calculate():
    debt = []
    for capital in [5.67e9, 5.9e9, 8e9, 12e9]:
        payment = annual_payment(capital)
        balance = capital
        for _ in range(30):
            balance = balance * 1.05 - payment
        assert abs(balance) < .001
        debt.append(dict(financed_USD=capital, annual_debt_service_USD=payment,
                         total_payments_USD=payment*30, total_interest_USD=payment*30-capital))
    assert annual_payment(300, 0, 30) == 10
    cases = []
    for sold_liters in [175000, 350000]:
        for export_kg in [0, 5, 20]:
            he_revenue = sold_liters*1500
            t_revenue = export_kg*1000*1500
            cases.append(dict(He3_qualified_sold_STP_L=sold_liters,
                T_qualified_export_kg=export_kg, He3_revenue_USD=he_revenue,
                T_revenue_USD=t_revenue, gross_isotope_revenue_USD=he_revenue+t_revenue,
                revenue_less_5_67B_debt_before_all_other_costs_USD=he_revenue+t_revenue-debt[0]['annual_debt_service_USD'],
                net_profit_USD=None))
    return dict(status='POTENTIAL-DERIVED scenarios; VERIFIED-DERIVED arithmetic only',
        rates_assumed=dict(annual_interest=.05, years=30, debt_fraction=1,
            He3_USD_per_STP_L=1500, T_USD_per_gram=1500),
        capital_recovery_factor=annual_payment(1), financing=debt, isotope_cases=cases,
        physical_validation=False, operating_cost_USD=None, GPU_margin_USD=None,
        notes=['Sales quantities are hypothetical qualified exports, not simulated saleable surplus.',
          '5.67B is the corrected historical ledger, not a CFS quote; 5.9B=two assumed 2.8B chassis plus 0.3B gross adaptation, without turbine savings. Alternative scopes, never additive.',
          '8B and 12B are cost stress cases, not estimates. Interest during construction, fees, taxes, working capital, replacement and OPEX are excluded.',
          'Debt ends after year 30 only if fully amortized and no refinancing/new debt. Replacement and decommissioning obligations remain.'])

if __name__ == '__main__':
    result = calculate()
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
