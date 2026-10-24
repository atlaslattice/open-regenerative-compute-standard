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
    print(json.dumps({k:result[k] for k in ['base','annual_product_m3','reference_normalization','all_in_cost']}, indent=2))
