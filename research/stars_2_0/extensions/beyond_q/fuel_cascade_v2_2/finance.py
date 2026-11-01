"""Conditional product allocation and reactor-only cash ledger. No GPU/QPU value."""
from collections import defaultdict
from kernel import L_PER_KG,MEV

def annuity(capital,rate,years):
    if capital<0 or rate<0 or years<=0:raise ValueError('invalid loan')
    return capital/years if rate==0 else capital*rate/(1-(1+rate)**(-years))

def connected_financials(rows,p,recovery):
    if not 0<=recovery<=1:raise ValueError('recovery')
    if not 0<=p['debt_fraction']<=1:raise ValueError('debt fraction')
    for key in ['He3_price_USD_per_STP_L','T_price_USD_per_gram','He3_market_cap_STP_L_per_year_fleet',
                'electricity_import_USD_per_kWh','historical_two_chassis_USD','adaptation_USD',
                'A_housing_site_USD','B_housing_site_USD','shared_site_USD','annual_operating_USD_per_module',
                'replacement_cost_USD_each_reactor','construction_interest_fees_USD_per_module',
                'decommissioning_reserve_USD_per_module_year']:
        if p[key] is not None and p[key]<0:raise ValueError(key)
    result=[]; grouped=defaultdict(list); helium_bank=0.
    for row in rows:grouped[row['year']].append(row)
    required=['A_housing_site_USD','B_housing_site_USD','shared_site_USD',
        'annual_operating_USD_per_module','replacement_cost_USD_each_reactor',
        'construction_interest_fees_USD_per_module','decommissioning_reserve_USD_per_module_year']
    costs_complete=all(p[k] is not None for k in required) and p['housing_not_in_chassis_verified']
    priced_energy=p['electricity_export_USD_per_kWh'] is not None
    capital_lower=p['historical_two_chassis_USD']+p['adaptation_USD']
    capital=capital_lower+sum(p[k] or 0. for k in ['A_housing_site_USD','B_housing_site_USD','shared_site_USD','construction_interest_fees_USD_per_module'])
    for year,yr in sorted(grouped.items()):
        total=lambda key:sum(r[key] for r in yr)
        active=int(sum(r['operating_age_years']>0 for r in yr))
        borrowing=int(sum(0<r['operating_age_years']<=p['debt_years'] for r in yr))
        recovered=total('he3_pipeline_exit')*recovery*L_PER_KG
        retained=recovered*p['He3_retained_fraction']
        bank_start=helium_bank
        helium_bank+=recovered-retained
        cap=p['He3_market_cap_STP_L_per_year_fleet']
        sales=helium_bank if cap is None else min(helium_bank,cap)
        helium_bank-=sales
        debt=borrowing*annuity(capital*p['debt_fraction'],p['debt_interest'],p['debt_years'])
        he_revenue=sales*p['He3_price_USD_per_STP_L']; t_revenue=total('exports')*1000*p['T_price_USD_per_gram']
        imports=total('import_MWh')*1000*p['electricity_import_USD_per_kWh']
        exports_revenue=total('export_MWh')*1000*(p['electricity_export_USD_per_kWh'] or 0.)
        opex=active*(p['annual_operating_USD_per_module'] or 0.)
        replacements=(total('A_replacements')+total('B_replacements'))*(p['replacement_cost_USD_each_reactor'] or 0.)
        decommissioning=active*(p['decommissioning_reserve_USD_per_module_year'] or 0.)
        starts=sum(0<r['operating_age_years']<=1 for r in yr)
        equity=starts*capital*(1-p['debt_fraction'])
        cash=he_revenue+t_revenue+exports_revenue-imports-debt-opex-replacements-decommissioning-equity
        fusion=total('DD_fusion_J')+total('A_DT_fusion_J')+total('B_DT_fusion_J')
        neutron=total('primary_DD_neutrons')*2.45*MEV+total('DT_neutrons')*14.1*MEV
        residual=total('T_start_kg')+total('dd_birth')+total('b_birth')+total('fuel_received')-total('fuel_sent')-total('a_burn')-total('b_burn')-total('decay')-total('permeation')-total('process_loss')-total('exports')-total('T_end_kg')
        result.append(dict(fleet_modules=yr[0]['fleet_modules'],year=year,He3_overall_recovery_assumed=recovery,
            price_case=p.get('price_case','requested_prices'),He3_price_USD_per_STP_L=p['He3_price_USD_per_STP_L'],T_price_USD_per_gram=p['T_price_USD_per_gram'],
            offtake_case=p.get('offtake_case','fleet_cap_stress'),He3_market_cap_STP_L_per_year_fleet=cap,
            active_modules=active,modules_with_initial_debt=borrowing,
            He3_born_STP_L=total('he3_born')*L_PER_KG,
            He3_product_candidate_STP_L=recovered,He3_lumped_loss_STP_L=total('he3_pipeline_exit')*(1-recovery)*L_PER_KG,
            He3_retained_STP_L=retained,He3_sale_candidate_STP_L=sales,
            He3_unsold_bank_start_STP_L=bank_start,He3_unsold_bank_end_STP_L=helium_bank,
            T_external_export_scenario_kg=total('exports'),T_predecessor_fuel_sent_kg=total('fuel_sent'),T_predecessor_fuel_received_kg=total('fuel_received'),T_stock_end_kg=total('T_end_kg'),T_balance_residual_kg=residual,
            T_B_burn_kg=total('b_burn'),T_B_gross_breeding_kg=total('b_birth'),T_unserved_kg=total('b_unserved'),
            deuterium_consumed_kg=(4*total('dd_birth')+total('a_burn')+total('b_burn'))/.00301604928*.00201410177812,
            Li6_equivalent_consumed_if_all_breeding_Li6_kg=total('b_birth')/.00301604928*.0060151228874,
            He4_product_candidate_kg=total('he4_pipeline_exit')*p['He4_overall_recovery_assumed'],
            He4_blanket_birth_unavailable_kg=total('b_birth')/.00301604928*.00400260325413,
            electricity_net_MWh=total('net_MWh'),electricity_export_MWh=total('export_MWh'),electricity_import_MWh=total('import_MWh'),
            fusion_energy_J=fusion,fusion_neutron_energy_J=neutron,fusion_charged_energy_J=fusion-neutron,
            blanket_reaction_Q_assumed_J=total('assumed_blanket_Q_J'),qualified_deposited_heat_J=None,
            conditional_He3_revenue_USD=he_revenue,conditional_T_revenue_USD=t_revenue,
            conditional_electricity_revenue_USD=exports_revenue if priced_energy else None,
            electricity_import_cost_USD=imports,
            debt_service_USD_if_capital_incomplete_is_partial=debt,
            annual_OPEX_USD=opex if p['annual_operating_USD_per_module'] is not None else None,
            replacements_USD=replacements if p['replacement_cost_USD_each_reactor'] is not None else None,
            revenue_less_known_charges_USD=cash,
            conditional_cash_flow_before_tax_USD=cash if costs_complete and priced_energy else None,
            actual_profit_USD=None,physical_validation=False,capital_scope_complete=costs_complete,
            actual_qualified_sales_USD=None))
    return result
