"""v0.8: EPA 2018-based five-year flow scenarios, with finite fleet capacity.
Run: python3 incoming_waste.py. All masses metric tonnes unless labeled.
No annual baseline is represented as an observed 2026 quantity.
"""
import json
from pathlib import Path
from math import isclose
P = Path(__file__).resolve().parent
ST_TO_T = 0.90718474
SOURCE = {
    'year': 2018,
    'msw_generated_million_short_t_per_year': 292.36,
    'msw_landfill_million_short_t_per_year': 146.12,
    'cd_generated_million_short_t_per_year': 600.33,
    'cd_landfill_million_short_t_per_year': 143.78,
    'msw_landfill_metals_million_short_t_per_year': {'ferrous': 10.53, 'aluminum': 2.66, 'other_nonferrous': 0.74},
    'cd_landfill_materials_rounded_million_short_t_per_year': {
        'concrete': 71.2, 'wood': 29.6, 'gypsum_drywall': 13.2,
        'ferrous_proxy_for_reported_metal': 1.1, 'brick_clay': 10.8,
        'asphalt_shingles': 13.0, 'asphalt_pavement': 4.9},
    'sources': [
        'https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials',
        'https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material',
        'https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1019BN2.TXT'],
}
RAMP = [0.10, 0.25, 0.50, 0.75, 1.0]
TARGET = 5000
ANNUAL_UNIT_T = 20 * 300
CAPTURE, ACCEPTANCE = 0.8, 0.9
YIELDS = {'ferrous': .95, 'aluminum': .95, 'copper': .97}
CONSUMPTION = {'ferrous': 95000000, 'aluminum': 5700000, 'copper': 2200000}
ALLOCATIONS = {
    'legacy_only': {'legacy': 1.0, 'fresh_msw': 0, 'fresh_cd': 0},
    'illustrative_integrated_40_30_30': {'legacy': .4, 'fresh_msw': .3, 'fresh_cd': .3},
    'fresh_only_50_50': {'legacy': 0, 'fresh_msw': .5, 'fresh_cd': .5},
}

def project(growth):
    annual = []
    for y in range(5):
        factor = (1 + growth) ** y
        row = {'year': y + 1, 'baseline_multiplier': factor}
        for stream in ['msw', 'cd']:
            for route in ['generated', 'landfill']:
                row[f'{stream}_{route}_t'] = SOURCE[f'{stream}_{route}_million_short_t_per_year'] * 1e6 * ST_TO_T * factor
        annual.append(row)
    totals = {key: sum(r[key] for r in annual) for key in ['msw_generated_t', 'msw_landfill_t', 'cd_generated_t', 'cd_landfill_t']}
    totals['combined_generated_t'] = totals['msw_generated_t'] + totals['cd_generated_t']
    totals['combined_landfill_t'] = totals['msw_landfill_t'] + totals['cd_landfill_t']
    return {'annual_growth': growth, 'annual': annual, 'five_year': totals,
            'five_year_landfill_t_per_state_equal_split': totals['combined_landfill_t'] / 50}

# C&D Table 8 rounded details sum to 143.8; normalize shares to exact 143.78 summary.
cd_details = SOURCE['cd_landfill_materials_rounded_million_short_t_per_year']
cd_detail_total = sum(cd_details.values())
msw_metals = SOURCE['msw_landfill_metals_million_short_t_per_year']

def operate(allocation, copper_share):
    shares = ALLOCATIONS[allocation]
    assert isclose(sum(shares.values()), 1)
    compositions = {
        'legacy': {'ferrous': .03, 'aluminum': .007, 'copper': .003},
        'fresh_msw': {'ferrous': msw_metals['ferrous']/146.12,
                      'aluminum': msw_metals['aluminum']/146.12,
                      'copper': msw_metals['other_nonferrous']/146.12*copper_share},
        # Unknown C&D Al/Cu are omitted, not asserted to be physically absent.
        'fresh_cd': {'ferrous': cd_details['ferrous_proxy_for_reported_metal']/cd_detail_total},
    }
    years = []
    for y, ramp in enumerate(RAMP):
        capacity = TARGET * ramp * ANNUAL_UNIT_T
        streams = {}
        for stream, share in shares.items():
            intake = capacity * share
            accepted = {m: intake * f * CAPTURE * ACCEPTANCE for m, f in compositions[stream].items()}
            finished = {m: accepted[m] * YIELDS[m] for m in accepted}
            front_residue = intake - sum(accepted.values())
            conversion_loss = sum(accepted.values()) - sum(finished.values())
            assert isclose(intake, sum(finished.values()) + front_residue + conversion_loss)
            streams[stream] = {'intake_t': intake, 'accepted_metal_t': accepted,
                               'finished_metal_t': finished,
                               'front_residue_t': front_residue,
                               'conversion_loss_t': conversion_loss}
        assert isclose(sum(v['intake_t'] for v in streams.values()), capacity)
        years.append({'year': y+1, 'intake_capacity_t': capacity, 'streams': streams})
    finished = {m: sum(r['streams'][s]['finished_metal_t'].get(m, 0) for r in years for s in shares) for m in YIELDS}
    intake = {s: sum(r['streams'][s]['intake_t'] for r in years) for s in shares}
    fresh_products = sum(sum(r['streams'][s]['finished_metal_t'].values()) for r in years for s in ['fresh_msw', 'fresh_cd'])
    legacy_products = sum(sum(r['streams']['legacy']['finished_metal_t'].values()) for r in years)
    flat = project(0)['five_year']
    # All uncredited mass assumed landfilled, including conversion losses.
    # This is a deliberately closed, metal-only mass ledger, not a real disposal forecast.
    residuals = sum(r['streams'][s]['front_residue_t'] + r['streams'][s]['conversion_loss_t'] for r in years for s in shares)
    assert isclose(sum(intake.values()), sum(finished.values()) + residuals)
    assert intake['fresh_msw'] <= flat['msw_landfill_t']
    assert intake['fresh_cd'] <= flat['cd_landfill_t']
    return {'allocation': allocation, 'shares': shares,
            'assumed_copper_share_of_msw_other_nonferrous': copper_share,
            'annual': years, 'five_year_intake_by_stream_t': intake,
            'five_year_finished_metal_t': finished,
            'gross_consumption_equivalent_stock_days': {m: t/CONSUMPTION[m]*365 for m,t in finished.items()},
            'fresh_finished_product_diversion_t': fresh_products,
            'legacy_finished_product_removed_t': legacy_products,
            'uncredited_residual_plus_conversion_loss_t': residuals,
            'fresh_landfill_addition_after_product_diversion_t': flat['combined_landfill_t']-fresh_products,
            'net_addition_to_buried_mass_after_legacy_product_removal_t': flat['combined_landfill_t']-fresh_products-legacy_products,
            'financial_roi': None}

projections = [project(g) for g in [0, .01, .02]]
flat_multiplier = 5e6 * ST_TO_T
pools = {'msw': {m: v*flat_multiplier for m,v in msw_metals.items()},
         'cd': {m: v/cd_detail_total*143.78*flat_multiplier for m,v in cd_details.items()}}
cases = [operate(a,c) for a in ALLOCATIONS for c in [0, .25, .5]]
assert isclose(projections[0]['five_year']['combined_landfill_t'], (146.12+143.78)*flat_multiplier)
assert isclose(sum(pools['cd'].values()), projections[0]['five_year']['cd_landfill_t'])
for case in cases:
    assert isclose(sum(case['five_year_intake_by_stream_t'].values()), 78000000)
    for metal in YIELDS:
        available = (pools['msw'].get(metal, 0) if metal!='copper'
                     else pools['msw']['other_nonferrous']*case['assumed_copper_share_of_msw_other_nonferrous'])
        recovered = sum(r['streams']['fresh_msw']['finished_metal_t'].get(metal,0) for r in case['annual'])
        assert recovered <= available + 1e-8
result = {
    'status': 'ILLUSTRATIVE FLOW AND CAPACITY MODEL; NOT A 2026 WASTE FORECAST, RESERVE OR PERFORMANCE GUARANTEE',
    'source_data': SOURCE,
    'projection_convention': 'Planning years 1-5 use the 2018 annual rate times (1+g)^(year-1). No growth from 2018 to a claimed 2026 level is assumed. Disposal shares and composition held constant.',
    'assumptions': {'target_units': TARGET, 'states': 50, 'annual_unit_intake_t': ANNUAL_UNIT_T,
                    'ramp': RAMP, 'capture': CAPTURE, 'buyer_acceptance': ACCEPTANCE,
                    'refinery_yields': YIELDS, 'consumption_t_year_from_v07': CONSUMPTION},
    'projections': projections,
    'five_year_flat_landfill_material_pools_t_before_capture': pools,
    'cases': cases,
    'limitations': [
        'C&D Al/Cu and MSW copper are not separately quantified in these tables. Copper shares 0/25/50% are sensitivities, not measured estimates; zero means no credit.',
        'C&D reported metal is modeled as ferrous using the steel generation category as a proxy; material characterization is required.',
        'Existing recovery and next-use tonnage excluded from incremental feed; no displacement/additionality audit has been performed.',
        'Legacy fractions and all capture/yields remain synthetic. Average national disposal composition is not a site assay.',
        'The 20t/day capacity is carried over as an assumption. C&D handling and crushing capability are not demonstrated; regional partners need independent capacity and cost verification.',
        'No mineral, plastic, wood or organic product credited; gross mineral inventory is not saleable aggregate or refinery feed.',
        'Residues and refining losses all assumed landfilled for the closed mass ledger. Actual treatment, soil management, oxidation and routing may differ.',
        'Legacy C&D stock unknown; prior 10bn tonne legacy assumption is not a verified combined MSW+C&D inventory.',
        'No automatic transfer of prior ROI, avoided-mining or carbon totals to these changed feed mixes. Fresh collection, preprocessing, residual treatment and partner economics need a new cost model.',
        'Consumption-equivalent days assume all modeled finished output is retained domestically, qualifies for use, and is stored without withdrawals; Vault eligibility and demand by grade are unverified.',
        'Industrial process wastes, wastewater sludge, mine tailings, vehicles and separate sector streams are not comprehensively included. Equal state splits are arithmetic only.'
    ]}
(P/'incoming-waste-results.json').write_text(json.dumps(result,indent=2)+'\n')
summary = {k:v for k,v in result.items() if k!='cases'}
summary['cases'] = [{k:v for k,v in c.items() if k!='annual'} for c in cases]
(P/'incoming-waste-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({'projections':[x['five_year'] for x in projections], 'pools':pools, 'integrated':[c for c in summary['cases'] if c['allocation']=='illustrative_integrated_40_30_30']},indent=2))
