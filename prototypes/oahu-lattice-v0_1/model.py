#!/usr/bin/env python3
"""Oahu Atlas Lattice v0.1: daily conserved-flow screening sensitivities.

Standard library only. Not a calibrated digital twin or plant-control system.
"""
import argparse
import csv
import json
import math
from pathlib import Path

SHORT_TON_TO_T = 0.90718474
MGD_TO_M3_DAY = 3785.411784


def validate(cfg):
    a = cfg['assumptions']
    fractions = a['feed_fraction']
    assert all(0 <= v <= 1 for v in fractions.values())
    assert math.isclose(sum(fractions.values()), 1, abs_tol=1e-10)
    for key in ['availability', 'metal_recovery', 'metal_buyer_acceptance',
                'conditional_combustible_acceptance', 'conditional_fuel_ash_fraction',
                'conditional_mineral_qualified_fraction', 'conditional_mineral_conversion_yield']:
        assert 0 <= a[key] <= 1, key
    assert 0 < a['future_desal_recovery_fraction'] < 1
    assert 0 <= a['scheduled_shifts'] <= a['days']
    assert all(v > 0 for v in a['screen_tph_cases'])
    for key, value in a.items():
        if isinstance(value, (int, float)):
            assert value >= 0, key


def simulate(cfg, name, tph=0, integrated=False, stress=False, future=False):
    validate(cfg)
    a, p = cfg['assumptions'], cfg['published_anchors']
    days = a['days']
    other_day = p['wgsl_other_2024_us_short_tons']['value'] * SHORT_TON_TO_T / days
    ash_day = p['wgsl_ash_residue_2024_us_short_tons']['value'] * SHORT_TON_TO_T / days
    hwrf_design = p['honouliuli_design_mgd']['value'] * MGD_TO_M3_DAY
    buffer = 0.0
    rows = []
    for day in range(days):
        # Evenly distributed shift calendar; actual feed/outage profiles UNKNOWN.
        scheduled = ((day + 1) * a['scheduled_shifts'] // days >
                     day * a['scheduled_shifts'] // days)
        operating = scheduled and tph > 0
        hpower_out = stress and 150 <= day < 150 + a['stress_hpower_outage_days']
        water_out = stress and 150 <= day < 150 + a['stress_reclaimed_outage_days']
        # No incoming-waste stockpile: any unprocessed current feed is disposed.
        processed = min(other_day, tph * a['shift_hours'] * a['availability']) if operating else 0
        fractions = {k: processed * v for k, v in a['feed_fraction'].items()}
        accepted_metal = {k: fractions[k] * a['metal_recovery'] * a['metal_buyer_acceptance']
                          for k in ['ferrous', 'nonferrous']}
        metal = sum(accepted_metal.values())
        mineral = min(fractions['mineral_fines'] * a['conditional_mineral_qualified_fraction'],
                      a['conditional_manufacturing_capacity_t_per_day']) if integrated else 0
        product = mineral * a['conditional_mineral_conversion_yield']
        # Rejected fuel and manufacturing residues remain on the disposal ledger.
        candidate_fuel = fractions['combustibles'] * a['conditional_combustible_acceptance'] if integrated else 0
        opening_buffer = buffer
        available_fuel = buffer + candidate_fuel
        to_hpower = min(available_fuel, a['conditional_hpower_spare_t_per_day']) if integrated and not hpower_out else 0
        available_fuel -= to_hpower
        buffer = min(available_fuel, a['conditional_fuel_buffer_capacity_t']) if integrated else 0
        fuel_overflow = available_fuel - buffer
        local_residual = processed - metal - product - candidate_fuel + fuel_overflow
        fuel_ash = to_hpower * a['conditional_fuel_ash_fraction']
        fuel_nonash_mass = to_hpower - fuel_ash
        unprocessed = other_day - processed
        disposal = unprocessed + local_residual + fuel_ash + ash_day
        # Avoidance counts only outputs accepted this day, never stored fuel.
        net_avoidance = metal + product + fuel_nonash_mass
        incremental_water = a['conditional_incremental_reclaimed_m3_per_day'] if integrated and not water_out else 0
        assert incremental_water <= hwrf_design
        dust = processed * a['dust_water_m3_per_feed_t']
        reclaimed_dust = min(incremental_water, dust)
        reclaimed_irrigation = min(max(0, incremental_water-reclaimed_dust),
                                   a['conditional_irrigation_demand_m3_per_day']) if integrated else 0
        replacement_water = dust - reclaimed_dust
        # Illustrative agricultural reuse displaces an assumed existing source;
        # no yield, fertilizer, food-import, or ecology benefit is inferred.
        desal_product = p['future_kalaeloa_product_mgd']['value'] * MGD_TO_M3_DAY if future else 0
        desal_feed = desal_product / a['future_desal_recovery_fraction'] if future else 0
        concentrate = desal_feed - desal_product
        revenue = sum(accepted_metal[k] * a['metal_netback_usd_per_metric_t'][k] for k in accepted_metal)
        allowance = a['daily_operating_allowance_usd'] if operating else 0
        train_kwh = a['screen_train_assumed_kw'] * a['shift_hours'] * a['availability'] if operating else 0
        compute_kwh = a['conditional_data_compute_kw'] * 24 if integrated else 0
        mass_error = (other_day + ash_day + opening_buffer -
                      disposal - metal - product - fuel_nonash_mass - buffer)
        assert abs(mass_error) < 1e-7
        assert reclaimed_dust + reclaimed_irrigation <= incremental_water + 1e-9
        assert product <= mineral + 1e-9
        rows.append(dict(day=day+1, scheduled_shift=int(operating), hpower_outage=int(hpower_out),
                         offered_other_t=other_day, incumbent_ash_t=ash_day,
                         processed_t=processed, metal_accepted_t=metal,
                         manufacturing_product_t=product, fuel_to_hpower_t=to_hpower,
                         fuel_ash_t=fuel_ash, fuel_nonash_mass_t=fuel_nonash_mass,
                         fuel_buffer_t=buffer, local_residual_t=local_residual,
                         landfill_disposal_t=disposal, net_disposal_avoidance_t=net_avoidance,
                         dust_water_m3=dust, new_nonreclaimed_water_m3=replacement_water,
                         reclaimed_to_dust_m3=reclaimed_dust,
                         reclaimed_to_irrigation_m3=reclaimed_irrigation,
                         indicative_metal_netback_usd=revenue, operating_allowance_usd=allowance,
                         screen_train_kwh=train_kwh, data_compute_kwh=compute_kwh,
                         future_desal_product_m3=desal_product, future_desal_feed_m3=desal_feed,
                         future_concentrate_m3=concentrate,
                         future_desal_kwh=desal_product*a['future_desal_sec_kwh_per_product_m3'],
                         mass_error_t=mass_error))
    sums = {key: sum(r[key] for r in rows) for key in rows[0] if key not in ['day', 'fuel_buffer_t']}
    baseline = (other_day + ash_day) * days
    # End inventory receives NO diversion credit; reserve its eventual disposal.
    summary = dict(scenario=name, evidence='MODELED ASSUMPTIONS; NOT FORECAST; ZERO REALIZED CREDIT',
                   feed_scope='current other MSW only; no legacy excavation; ash bypass; C&D excluded',
                   screen_tph=tph, baseline_wgsl_t=baseline,
                   processed_t=sums['processed_t'],
                   net_disposal_avoided_t=sums['net_disposal_avoidance_t'],
                   net_disposal_avoided_percent=100*sums['net_disposal_avoidance_t']/baseline,
                   final_fuel_inventory_t=buffer,
                   disposal_plus_inventory_t=sums['landfill_disposal_t']+buffer,
                   accepted_metals_t=sums['metal_accepted_t'],
                   manufactured_product_t=sums['manufacturing_product_t'],
                   assumed_incremental_irrigation_delivery_m3=sums['reclaimed_to_irrigation_m3'],
                   assumed_new_dust_water_m3=sums['new_nonreclaimed_water_m3'],
                   indicative_metal_netback_usd=sums['indicative_metal_netback_usd'],
                   partial_operating_allowance_usd=sums['operating_allowance_usd'],
                   PARTIAL_metal_less_allowance_usd=sums['indicative_metal_netback_usd']-sums['operating_allowance_usd'],
                   screen_train_kwh=sums['screen_train_kwh'], data_compute_kwh=sums['data_compute_kwh'],
                   future_product_water_m3=sums['future_desal_product_m3'],
                   future_concentrate_m3=sums['future_concentrate_m3'],
                   future_desal_kwh=sums['future_desal_kwh'],
                   recovered_brine_product_t=None, agriculture_yield_gain=None,
                   ai_efficiency_gain=None, local_fabrication_downtime_savings=None,
                   lifecycle_co2e=None, capex=None, full_profit=None, roi=None,
                   reclaimed_displacement_credit='conditional counterfactual only; not realized',
                   net_airspace_recovered_m3=None, max_abs_mass_error_t=max(abs(r['mass_error_t']) for r in rows))
    assert math.isclose(summary['disposal_plus_inventory_t']+summary['net_disposal_avoided_t'], baseline, abs_tol=1e-6)
    return rows, summary


def run(cfg):
    cases = [('incumbent_baseline', 0, False, False, False)]
    cases += [(f'screen_{tph}_metals_only', tph, False, False, False) for tph in cfg['assumptions']['screen_tph_cases']]
    cases += [('conditional_integrated_50', 50, True, False, False),
              ('conditional_integrated_200', 200, True, False, False),
              ('conditional_integrated_200_outages', 200, True, True, False),
              ('future_conditional_200_desal_online', 200, True, False, True)]
    return [(name, *simulate(cfg, name, tph, integrated, stress, future))
            for name, tph, integrated, stress, future in cases]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, default=Path(__file__).with_name('inputs.json'))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('results'))
    args = parser.parse_args()
    cfg = json.loads(args.inputs.read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    summaries = []
    for name, rows, summary in run(cfg):
        with (args.output/f'{name}.csv').open('w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
        summaries.append(summary)
    (args.output/'summary.json').write_text(json.dumps(summaries, indent=2)+'\n')
    columns = ['scenario', 'processed_t', 'net_disposal_avoided_t', 'net_disposal_avoided_percent',
               'accepted_metals_t', 'manufactured_product_t', 'final_fuel_inventory_t',
               'assumed_incremental_irrigation_delivery_m3', 'PARTIAL_metal_less_allowance_usd',
               'data_compute_kwh', 'future_concentrate_m3', 'full_profit', 'roi']
    with (args.output/'summary.csv').open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=columns, extrasaction='ignore'); w.writeheader(); w.writerows(summaries)
    print(json.dumps([{k:s[k] for k in ['scenario','processed_t','net_disposal_avoided_percent','full_profit']} for s in summaries], indent=2))


if __name__ == '__main__':
    main()
