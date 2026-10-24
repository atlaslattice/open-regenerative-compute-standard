"""Atlas Lattice screening model. Standard library only; no site forecast."""
import csv
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
M3_PER_MGAL = 3785.411784


def water_balance(product_mgd, plant_recovery, ro_recovery, feed_salt_kg_m3=35):
    if not 0 < plant_recovery <= ro_recovery < 1:
        raise ValueError('Require 0 < plant recovery <= RO recovery < 1')
    if product_mgd <= 0 or feed_salt_kg_m3 < 0:
        raise ValueError('Invalid flow or salinity')
    p = product_mgd * M3_PER_MGAL
    f = p / plant_recovery
    rf = p / ro_recovery
    pre = f - rf
    reject = rf - p
    # Idealized complete salt rejection, no reagents, volume-additive flows.
    # This conservatively inventories dissolved feed salt; not an assay.
    return dict(product_m3_d=p, intake_m3_d=f, ro_feed_m3_d=rf,
                pretreatment_residual_m3_d=pre, ro_concentrate_m3_d=reject,
                combined_residual_m3_d=f-p,
                pretreatment_salt_t_d=pre*feed_salt_kg_m3/1000,
                ro_concentrate_salt_t_d=rf*feed_salt_kg_m3/1000,
                total_feed_salt_t_d=f*feed_salt_kg_m3/1000,
                ro_concentrate_salt_kg_m3=rf*feed_salt_kg_m3/reject)


def residual_envelope(balance, additional_water_fraction):
    """Volume/salt screening envelope, NOT membrane/evaporator engineering."""
    if not 0 <= additional_water_fraction <= 1:
        raise ValueError('Invalid additional recovery')
    q = balance['combined_residual_m3_d']
    remaining = q*(1-additional_water_fraction)
    recovered = q-remaining
    salt = balance['total_feed_salt_t_d']
    return dict(additional_water_fraction=additional_water_fraction,
                additional_water_m3_d=recovered, remaining_liquid_m3_d=remaining,
                conserved_salt_inventory_t_d=salt,
                apparent_salt_kg_m3=None if remaining == 0 else salt*1000/remaining,
                overall_volume_recovery=(balance['product_m3_d']+recovered)/balance['intake_m3_d'],
                interpretation='At high concentrations crystallization/phase separation is required; no solubility or treatment-performance prediction',
                treatment_energy_kwh_d=None, capex_usd=None, accepted_products_t_d=0,
                realized_ocean_discharge_avoidance_m3_d=0)


def complete_total(costs):
    missing = [k for k, v in costs.items() if v is None]
    return dict(total=None if missing else sum(costs.values()), missing=missing,
                known_subtotal=sum(v for v in costs.values() if v is not None))


def crf(rate, years):
    if rate < 0 or years <= 0:
        raise ValueError('Invalid finance assumptions')
    return 1/years if rate == 0 else rate*(1+rate)**years/((1+rate)**years-1)


def domestic_component_share(domestic, foreign, final_assembly_labor=0):
    # Final-product assembly is excluded from the component-cost denominator.
    # Classification and agency eligibility remain outside this arithmetic.
    if domestic < 0 or foreign < 0 or domestic+foreign <= 0:
        raise ValueError('Invalid component costs')
    return domestic/(domestic+foreign)


def heat_match(source_c, sink_supply_c, approach_c=5):
    return source_c >= sink_supply_c + approach_c


def fate_gate(streams):
    """A transferred waste stream retains its downstream disposal obligation."""
    if not streams:
        return 'UNRESOLVED'
    if any(s.get('routine_marine_release') is True for s in streams):
        return 'FAIL'
    if any(s.get('routine_marine_release') is not False or
           not s.get('permitted') or not s.get('final_fate_verified') for s in streams):
        return 'UNRESOLVED'
    return 'PASS_WITHIN_DECLARED_STREAM_BOUNDARY'


def allocate_minerals(ro_feed_m3_d, ions_mg_l, capture_fraction,
                      magnesium_product='MgOH2', calcium_product='gypsum'):
    """Disjoint ion allocation; theoretical mass, not extraction or qualification.

    Product bound water and externally supplied hydroxide/carbonate are not
    seawater salt. No claim of precipitation feasibility or product purity.
    """
    if ro_feed_m3_d <= 0 or not 0 <= capture_fraction <= 1:
        raise ValueError('Invalid mineral assumptions')
    if magnesium_product not in ['MgOH2', 'MgCl2'] or calcium_product not in ['gypsum', 'CaCO3']:
        raise ValueError('Unsupported competing allocation')
    initial = {k: v*ro_feed_m3_d/1e6 for k,v in ions_mg_l.items()}
    remaining = initial.copy()
    products=[]

    def take(name, requirements, target, mw, external='none'):
        # kmol/day; atomic/molecular weights numerically kg/kmol.
        kmol=min([target]+[remaining[k]*1000/w for k,w in requirements.items()])
        used={k:kmol*w/1000 for k,w in requirements.items()}
        for k,v in used.items():
            remaining[k]-=v
        products.append(dict(product=name, theoretical_t_d=kmol*mw/1000,
                             consumed_feed_ions_t_d=used,
                             external_or_bound_material=external,
                             accepted_t_d=0, realized_revenue_usd_d=0))

    mg=initial['Mg']*1000/24.305*capture_fraction
    if magnesium_product=='MgOH2':
        take('Mg(OH)2', {'Mg':24.305}, mg,58.319,'hydroxide supplied externally; reagent and water balance excluded')
    else:
        take('MgCl2 anhydrous equivalent', {'Mg':24.305,'Cl':70.906},mg,95.211,'hydration state and drying energy unspecified')
    ca=initial['Ca']*1000/40.078*capture_fraction
    if calcium_product=='gypsum':
        take('gypsum',{'Ca':40.078,'SO4':96.06},ca,172.17,'bound water; purity and precipitation unspecified')
    else:
        take('CaCO3',{'Ca':40.078},ca,100.086,'carbonate supplied externally; embodied input not free recovery')
    take('KCl',{'K':39.098,'Cl':35.453},initial['K']*1000/39.098*capture_fraction,74.551)
    take('NaCl',{'Na':22.99,'Cl':35.453},initial['Na']*1000/22.99*capture_fraction,58.443)
    take('bromine elemental equivalent',{'Br':79.904},initial['Br']*1000/79.904*capture_fraction,79.904,
         'speciation, oxidant, containment and process yield unspecified')
    return dict(basis=f'Idealized RO reject only; {capture_fraction:.0%} capture is an assumption, not technology performance',
                initial_ions_t_d=initial,products=products,remaining_ions_t_d=remaining,
                accepted_products_t_d=0, realized_revenue_usd_d=0,
                note='Ion consumption conserves each listed inventory; product mass may include reagents/bound water. Other unlisted ions, suspended solids, chemicals and water require separate balances.')


def landed_cost(customs_value_usd, section_301_rate, other_duties_rate,
                freight_usd, integration_usd):
    """Assumed ad-valorem scenario, not a customs assessment.

    Freight is separate from declared customs value. Actual valuation, tariff
    stacking, exemptions and non-ad-valorem charges require broker review.
    """
    args=[customs_value_usd,section_301_rate,other_duties_rate,freight_usd,integration_usd]
    if any(v is None for v in args):
        return None
    if any(v < 0 for v in args):
        raise ValueError('Negative landed-cost assumption')
    return customs_value_usd*(1+section_301_rate+other_duties_rate)+freight_usd+integration_usd


def baba_screen(applicable, us_manufacturing, domestic, foreign):
    """Only the general manufactured-product arithmetic, not eligibility."""
    if applicable is False:
        return 'NOT_APPLICABLE_AS_DECLARED'
    if applicable is True and us_manufacturing is False:
        return 'ARITHMETIC_FAIL'
    if applicable is None or us_manufacturing is None or domestic is None or foreign is None:
        return 'UNRESOLVED'
    share=domestic_component_share(domestic,foreign)
    return 'ARITHMETIC_PASS_ONLY' if us_manufacturing and share > .55 else 'ARITHMETIC_FAIL'


def coupled_residual(feed_m3_d, additional_water_fraction, energy_kwh_per_m3_feed):
    """Explicit process inputs; ion recovery alone implies no water removal."""
    if feed_m3_d < 0 or (additional_water_fraction is not None and not 0 <= additional_water_fraction <= 1):
        raise ValueError('Invalid coupled-volume assumption')
    if energy_kwh_per_m3_feed is not None and energy_kwh_per_m3_feed < 0:
        raise ValueError('Invalid coupled-energy assumption')
    return dict(remaining_liquid_m3_d=None if additional_water_fraction is None else feed_m3_d*(1-additional_water_fraction),
                incremental_energy_kwh_d=None if energy_kwh_per_m3_feed is None else feed_m3_d*energy_kwh_per_m3_feed,
                status='Unmeasured independent process inputs; no salt or chemistry closure inferred')


def portfolio_support(annual_tonnes, net_contribution_usd_t, annual_residual_m3, years, discount_rate):
    """Maximum shared-residual budget supported by an assumed product margin.

    Margin must already deduct allocated mineral CAPEX/OPEX/logistics. This is
    not product price or demonstrated profit. No escalation, ramp or downtime
    beyond the caller's annual output; no terminal value.
    """
    if annual_tonnes < 0 or annual_residual_m3 <= 0:
        raise ValueError('Invalid portfolio volume')
    annual=annual_tonnes*net_contribution_usd_t
    return dict(annual_product_contribution_usd=annual,
                max_shared_residual_budget_usd_m3=annual/annual_residual_m3,
                nominal_horizon_contribution_usd=annual*years,
                present_value_before_shared_residual_cost_usd=annual/crf(discount_rate,years),
                status='Illustrative break-even support; no accepted sales or actual residual costs established')


def ai_net_savings(gross_savings_usd_y, compute_cost_usd_y, capital_usd, annual_costs, rate=.06, years=10):
    if capital_usd is None or any(v is None for v in annual_costs):
        return None
    return gross_savings_usd_y-compute_cost_usd_y-capital_usd*crf(rate,years)-sum(annual_costs)


def equipment_leverage(equipment_cost, total_cost, equipment_reduction):
    if not 0 <= equipment_cost <= total_cost or total_cost <= 0 or not 0 <= equipment_reduction <= 1:
        raise ValueError('Invalid equipment comparison')
    return dict(equipment_share=equipment_cost/total_cost,
                assumed_equipment_reduction=equipment_reduction,
                total_capital_reduction_fraction=equipment_reduction*equipment_cost/total_cost,
                savings_usd=equipment_cost*equipment_reduction)


def mineral_break_even(capex, fixed_opex_y, variable_cost_t, sold_t_y,
                       rate, years, shared_residual_cost_y=0, coproduct_contribution_y=0):
    values=[capex,fixed_opex_y,variable_cost_t,sold_t_y,shared_residual_cost_y,coproduct_contribution_y]
    if any(v is None for v in values):
        return None
    if any(v < 0 for v in values):
        raise ValueError('Negative break-even input')
    if sold_t_y == 0:
        return None
    return variable_cost_t+(capex*crf(rate,years)+fixed_opex_y+shared_residual_cost_y-coproduct_contribution_y)/sold_t_y


def required_sold_tonnes(price_t, variable_cost_t, annual_fixed_and_capital):
    if price_t <= variable_cost_t:
        return None  # No finite volume pays positive fixed costs at nonpositive margin.
    return annual_fixed_and_capital/(price_t-variable_cost_t)


def sourcing_savings(equipment_cost,total_cost,price_reduction,sourceable_fraction):
    if sourceable_fraction is None:
        return None
    if not 0 <= sourceable_fraction <= 1:
        raise ValueError('Invalid sourceable fraction')
    return equipment_leverage(equipment_cost,total_cost,price_reduction)['savings_usd']*sourceable_fraction


def chloride_tables(cases):
    routes=[];summaries=[]
    for name,case in cases.items():
        routes.extend(dict(scenario=name,**p) for p in case['products'])
        summaries.append(dict(scenario=name,initial_cl_t_d=case['initial_remaining_cl_t_d'],
            total_consumed_cl_t_d=sum(p['consumed_cl_t_d'] for p in case['products']),
            unallocated_cl_t_d=case['unallocated_cl_t_d'],returned_cl_t_d=case['returned_cl_t_d'],
            final_residual_cl_t_d=case['final_residual_cl_t_d'],scope='One row per scenario; route-level consumption is in separate table'))
    return routes,summaries


def usd_bbl_to_m3(value):
    if value < 0:
        raise ValueError('Negative fee')
    return value/(42*3.785411784/1000)


def chloride_meq_l_to_mg_l(value):
    if value < 0:
        raise ValueError('Negative concentration')
    return value*35.453


def chloride_use_gate(measured, maximum, units, specification_units, spec_verified, other_tests_pass):
    """Use-specific chloride criterion; no universal limit or product approval."""
    if not spec_verified or measured is None or maximum is None or not units or units != specification_units:
        return 'UNRESOLVED'
    if measured < 0 or maximum < 0:
        raise ValueError('Negative analytical concentration')
    if measured > maximum or other_tests_pass is False:
        return 'FAIL'
    return 'DECLARED_CRITERIA_PASS_ONLY' if other_tests_pass is True else 'UNRESOLVED'


def chloride_allocation(remaining_ions, route_fractions, acid_return_fraction=0):
    """Disjoint alternatives on leftover Na/Cl; theoretical pure-active masses.

    No water-removal claim. BMED and chlor-alkali also require water/electricity;
    output solutions, purification, purges and other ions are not resolved.
    Acid returned after internal neutralization remains in the residual ledger.
    """
    if set(route_fractions)-{'nacl','bmed','chloralkali'}:
        raise ValueError('Unknown chloride route')
    if any(v < 0 for v in route_fractions.values()) or sum(route_fractions.values()) > 1+1e-12:
        raise ValueError('Routes compete for one chloride inventory')
    if not 0 <= acid_return_fraction <= 1:
        raise ValueError('Invalid acid return fraction')
    cl=remaining_ions['Cl'];na=remaining_ions['Na'];initial_cl=cl;initial_na=na
    if cl < 0 or na < 0:
        raise ValueError('Negative ion inventory')
    products=[];returned_cl=0
    for route,fraction in route_fractions.items():
        use_cl=max(0,min(initial_cl*fraction,cl,na*35.453/22.99))
        use_na=use_cl*22.99/35.453
        cl-=use_cl;na-=use_na
        if route=='nacl':
            product=use_cl*58.443/35.453;co_naoh=0;h2=0;water=0
        elif route=='bmed':
            product=use_cl*36.461/35.453;co_naoh=use_cl*39.997/35.453;h2=0;water=use_cl*18.015/35.453
            returned_cl+=use_cl*acid_return_fraction
        else:
            product=use_cl;co_naoh=use_cl*39.997/35.453;h2=use_cl*1.008/35.453;water=use_cl*18.015/35.453
        products.append(dict(route=route,consumed_cl_t_d=use_cl,consumed_na_t_d=use_na,
                             theoretical_main_product_t_d=product,theoretical_naoh_coproduct_t_d=co_naoh,
                             theoretical_h2_coproduct_t_d=h2,stoichiometric_water_consumed_t_d=water,
                             accepted_product_t_d=0,realized_revenue_usd_d=0))
    return dict(initial_remaining_cl_t_d=initial_cl,initial_remaining_na_t_d=initial_na,
                products=products,unallocated_cl_t_d=cl,unallocated_na_t_d=na,
                returned_cl_t_d=returned_cl,final_residual_cl_t_d=cl+returned_cl,
                allocated_cl_not_returned_t_d=initial_cl-cl-returned_cl,
                water_recovery_m3_d=None,incremental_energy_kwh_d=None,
                scope='Theoretical stage inventory only; no qualification, market, net-water or energy proof. Returned acid counterions unresolved; coproducts are gross production, not simultaneous sales/internal reuse.')


def run(inputs):
    a = inputs['corpus_assumptions']
    balances = []
    for mgd, recovery in itertools.product([30, 50, 100], [.40, .425, .45]):
        b = water_balance(mgd, recovery, a['ro_recovery'], a['feed_salinity_kg_m3'])
        b.update(product_mgd=mgd, plant_recovery=recovery,
                 annual_product_m3=b['product_m3_d']*365*a['availability'],
                 interpretation='Nameplate online-day envelope; annual availability applied once; no daily storage simulation')
        balances.append(b)
    base = water_balance(a['product_mgd'], a['plant_recovery'], a['ro_recovery'],a['feed_salinity_kg_m3'])
    annual = base['product_m3_d']*365*a['availability']
    capital = []
    for cny, fx, escalation, localization in itertools.product(
            [450e6, 650e6], [7.0, 7.25, 7.5], [1.0, 1.3, 1.6], [2, 3, 5]):
        scaled = cny/fx * base['product_m3_d']/100000
        adapted = scaled*escalation*localization
        capital.append(dict(reference_cny=cny, assumed_cny_per_usd=fx,
                            assumed_escalation=escalation, assumed_localization=localization,
                            scaled_reference_usd=scaled, adapted_reference_usd=adapted,
                            budget_headroom_vs_corpus_usd=978770000-adapted,
                            scope='Multiplier sensitivity only; not installed-cost estimate; missing scope not priced'))
    energy = []
    for sec, tariff, it_kw, improvement in itertools.product(
            [2.2, 3.0, 3.52, 4.32], [.07, .10, .15], [0, 100, 1000], [0, .05, .10]):
        gross = annual*sec
        saving = gross*improvement
        compute = it_kw*1.15*8760
        ai=inputs['ai_lifecycle_costs']
        energy.append(dict(water_sec_kwh_m3=sec, tariff_usd_kwh=tariff,
                           additional_compute_it_kw=it_kw, assumed_water_energy_saving=improvement,
                           water_energy_kwh_y=gross, compute_energy_kwh_y=compute,
                           assumed_saving_kwh_y=saving, combined_energy_kwh_y=gross-saving+compute,
                           incremental_energy_vs_water_only_kwh_y=compute-saving,
                           annual_electricity_usd=(gross-saving+compute)*tariff,
                           incremental_ai_lifecycle_net_savings_usd_y=ai_net_savings(
                               saving*tariff,compute*tariff,
                               ai['incremental_sensor_and_integration_capex_usd'],
                               [ai[k] for k in ['storage_and_software_usd_year','cyber_and_training_usd_year','maintenance_and_replacement_usd_year']]),
                           interpretation='Energy-only sensitivity, no demonstrated AI improvement or heat credit; savings exclude additional residual treatment'))
    ro = inputs['reference_procurements'][0]
    replacement = [dict(life_years=life, annual_cny=ro['cost_cny_including_tax']/life,
                        annual_usd_at_assumed_fx=ro['cost_cny_including_tax']/life/7.25,
                        usd_m3_at_assumed_fx=ro['cost_cny_including_tax']/life/7.25/annual,
                        scope='One first-stage RO replacement lot only; no claim of complete membrane inventory or life')
                   for life in [5, 7, 10]]
    finance = [dict(hypothetical_installed_capex_usd=cap,
                    capital_charge_usd_m3=cap*crf(.06, 30)/annual,
                    scope='Capital-only, assumed 6%/30 years/90% availability; excludes OPEX and financing fees')
               for cap in [150e6, 250e6, 500e6, 978770000]]
    mineral_cases={s['name']:allocate_minerals(
        base['ro_feed_m3_d'],inputs['representative_ions_mg_l'],
        s['capture_fraction'],s['magnesium_product'],s['calcium_product'])
        for s in inputs['mineral_scenarios']}
    mg=next(p['theoretical_t_d'] for p in mineral_cases['hydroxide_gypsum']['products'] if p['product']=='Mg(OH)2')
    ps=inputs['portfolio_sensitivity']
    support=[]
    for margin in ps['net_contribution_usd_t']:
        row=portfolio_support(mg*365*a['availability'],margin,
                              base['combined_residual_m3_d']*365*a['availability'],
                              ps['horizon_years'],ps['discount_rate'])
        row.update(assumed_net_margin_usd_t=margin,assumed_sales_t_y=mg*365*a['availability'])
        support.append(row)
    imp=inputs['import_compliance']
    be=inputs['mineral_break_even_actual']
    be_grid=[]
    for sales_fraction,shared_cost in itertools.product([.25,.5,.75,1],[0,10e6,25e6]):
        sold=mg*365*a['availability']*sales_fraction
        be_grid.append(dict(assumed_sales_fraction=sales_fraction,sold_t_y=sold,
            assumed_module_capex_usd=50e6,assumed_fixed_opex_usd_y=5e6,assumed_variable_cost_usd_t=400,
            assumed_shared_residual_cost_usd_y=shared_cost,
            break_even_product_price_usd_t=mineral_break_even(50e6,5e6,400,sold,.06,20,shared_cost),
            scope='Illustrative inputs, not quotes; 50% feed capture and90% plant availability already applied; sales fraction is an additional market/run-rate constraint'))
    cc=inputs['historical_cost_leverage']
    leverage=[]
    for total,label in [(cc['construction_total_usd'],'2025 construction'),
                        (cc['construction_total_usd']+cc['engineering_admin_usd'],'2025 construction plus planning/design/admin')]:
        row=equipment_leverage(cc['process_equipment_usd'],total,.5)
        row.update(denominator_label=label,denominator_usd=total,
                   scope='Dated2025 line-item purchase-price-only sensitivity; no claim this captures every sourceable item or design/civil optimization; not2026 GMP')
        leverage.append(row)
    chloride_cases={s['name']:chloride_allocation(mineral_cases['hydroxide_gypsum']['remaining_ions_t_d'],
                    s['fractions'],s['acid_return_fraction']) for s in inputs['chloride_scenarios']}
    discount_grid=[]
    price_bridge=inputs['conditional_price_bridge']
    bridge_be=mineral_break_even(price_bridge['module_capex_usd'],price_bridge['fixed_opex_usd_y'],
         price_bridge['variable_cost_usd_t'],mg*365*a['availability'],price_bridge['discount_rate'],
         price_bridge['life_years'],price_bridge['shared_residual_cost_usd_y'])
    for rate,years in itertools.product([.03,.06,.10],[10,20,30]):
        row=portfolio_support(mg*365*a['availability'],150,
                  base['combined_residual_m3_d']*365*a['availability'],years,rate)
        row.update(assumed_discount_rate=rate,horizon_years=years,assumed_net_margin_usd_t=150,
                   implied_selling_price_usd_t=bridge_be+150,
                   conditional_break_even_basis_usd_t=bridge_be,
                   price_basis='Conditional bridge to full-sales50mCAPEX/5mfixed/400variable/6%20yr case; not unique implied price or quote; shared residual cost excluded')
        discount_grid.append(row)
    sourcing=[]
    eq=inputs['equipment_sourcing']
    for fraction in eq['scenario_fractions']:
        savings=sourcing_savings(cc['process_equipment_usd'],cc['construction_total_usd'],
                                eq['assumed_net_price_reduction'],fraction)
        sourcing.append(dict(internationally_sourceable_fraction=fraction,fraction_status='ASSUMED scenario, not proven sourceability',
            assumed_net_price_reduction=eq['assumed_net_price_reduction'],savings_usd=savings,
            construction_reduction_fraction=savings/cc['construction_total_usd'],scope='One historical process-equipment line; excludes other hardware/design changes'))
    for row in leverage:
        row['internationally_sourceable_fraction']=eq['internationally_sourceable_fraction']
        row['actual_achievable_savings_usd']=sourcing_savings(cc['process_equipment_usd'],row['denominator_usd'],
                  eq['assumed_net_price_reduction'],eq['internationally_sourceable_fraction'])
    groups=[dict(group=k,cost_usd=v,share_of_2025_construction=v/cc['construction_total_usd'],
                 source='CC25DETAIL grouped by analyst; installed categories; pure labor/admin split unavailable')
            for k,v in inputs['historical_construction_groups'].items()]
    benchmark_rows=[]
    for b in inputs['external_disposal_benchmarks']:
        benchmark_rows.append(dict(id=b['id'],source=b['source'],source_price_year=b['source_price_year'],
            source_usd_per_bbl_low=b['source_usd_per_bbl_low'],source_usd_per_bbl_high=b['source_usd_per_bbl_high'],
            external_benchmark_usd_m3_low=usd_bbl_to_m3(b['source_usd_per_bbl_low']),
            external_benchmark_usd_m3_high=usd_bbl_to_m3(b['source_usd_per_bbl_high']),
            stream=b['stream'],transferable_to_project=b['transferable_to_project'],
            scope=b['note']))
    route_table,scenario_table=chloride_tables(chloride_cases)
    return dict(status='SIMULATED screening; zero realized benefit; no total installed cost or water tariff established',
                base=base, annual_product_m3=annual,
                water_scenarios=balances, capital_sensitivity=capital,
                energy_sensitivity=energy, ro_replacement_sensitivity=replacement,
                capital_charge_sensitivity=finance,
                residual_scenarios=[residual_envelope(base, r) for r in [0, .5, .8, 1]],
                mineral_allocations=mineral_cases,
                coupling_scenarios=[dict(name=c['name'],**coupled_residual(
                    base['ro_concentrate_m3_d'],c['additional_water_fraction'],
                    c['incremental_energy_kwh_per_m3_ro_reject'])) for c in inputs['mineral_water_energy_couplings']],
                portfolio_support_sensitivity=support,
                equipment_leverage=leverage,
                historical_construction_groups=groups,
                equipment_sourcing_sensitivity=sourcing,
                external_disposal_benchmarks=benchmark_rows,
                chloride_route_detail=route_table,chloride_scenario_summary=scenario_table,
                mineral_break_even_actual_usd_t=mineral_break_even(
                    be['capex_usd'],be['fixed_opex_usd_y'],be['variable_cost_usd_t'],be['sold_t_y'],
                    be['discount_rate'],be['life_years'],be['allocated_residual_cost_usd_y']),
                mineral_break_even_sensitivity=be_grid,
                discount_horizon_sensitivity=discount_grid,
                chloride_allocations=chloride_cases,
                fallback_quote_status='NO CONFIRMED QUOTE; actual facilities/capacity/fees remain unknown',
                import_compliance_screen=dict(
                    actual_landed_cost_usd=landed_cost(imp['customs_value_usd'],imp['section_301_rate'],
                        imp['other_duties_rate'],imp['freight_and_insurance_usd'],imp['certification_integration_usd']),
                    baba_status=baba_screen(imp['baba_component_test_applicable'],imp['us_manufacturing_confirmed'],
                                            imp['domestic_component_cost_usd'],imp['foreign_component_cost_usd']),
                    section_301_rates_are_scenarios=imp['section_301_sensitivity_rates'],
                    duty_only_per_million_usd_customs_value=[dict(assumed_rate=r,section_301_only_usd=1e6*r,scope='Normalized hypothetical duty exposure; other duties/freight/certification excluded; not an applied rate') for r in imp['section_301_sensitivity_rates']]),
                environmental_clearance=fate_gate(inputs.get('residual_streams', [])),
                reported_reference_chemical_cost=dict(
                    cny_m3_reported_less_than=.15,
                    illustrative_annual_cny_at_boundary=annual*.15,
                    illustrative_usd_m3_at_assumed_fx=.15/7.25,
                    scope='MIIT reference bound only; not a Corpus quote, mineral reagent cost, or complete OPEX'),
                all_in_cost=complete_total(inputs['corpus_cost_slots_usd']),
                reference_normalization=dict(
                    fx_is_assumed_not_market_quote=7.25,
                    dongjiakou_450m_cny_usd_per_m3_d=450e6/7.25/100000,
                    corpus_usd_per_m3_d=978770000/base['product_m3_d'],
                    raw_ratio_450m=(978770000/base['product_m3_d'])/(450e6/7.25/100000),
                    raw_ratio_650m=(978770000/base['product_m3_d'])/(650e6/7.25/100000),
                    note='Unadjusted mixed-date/scope comparison, not proven savings'),
                realized_credits=dict(water_m3=0, mineral_revenue_usd=0,
                                      avoided_landfill_usd=0, ecological_benefit=0,
                                      imported_materials_displaced_t=0))


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


if __name__ == '__main__':
    inputs=json.loads((ROOT/'inputs.json').read_text())
    result=run(inputs)
    out=ROOT/'results';out.mkdir(exist_ok=True)
    (out/'summary.json').write_text(json.dumps(result, indent=2)+'\n')
    for name in ['water_scenarios','capital_sensitivity','energy_sensitivity',
                 'ro_replacement_sensitivity','capital_charge_sensitivity','residual_scenarios',
                 'portfolio_support_sensitivity','coupling_scenarios']:
        write_csv(out/(name+'.csv'), result[name])
    for name in ['equipment_leverage','mineral_break_even_sensitivity','discount_horizon_sensitivity',
                 'historical_construction_groups','equipment_sourcing_sensitivity','external_disposal_benchmarks',
                 'chloride_scenario_summary']:
        write_csv(out/(name+'.csv'),result[name])
    write_csv(out/'chloride_allocation_sensitivity.csv',result['chloride_route_detail'])
    print(json.dumps({k:result[k] for k in ['base','annual_product_m3','reference_normalization','all_in_cost']}, indent=2))
