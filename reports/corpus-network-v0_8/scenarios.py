"""Atlas Corpus retrofit / 100 MW / 500 MW screening. No external packages.

All MW compute ratings are IT nameplate, not total site load. Outputs are
arithmetic scenarios, not supplier guarantees. Unknown costs remain null.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GALLONS_PER_M3 = 264.1720523581484
M3_PER_MG = 1_000_000 / GALLONS_PER_M3


def evaluate(p):
    out = {}
    water = []
    for feed in p['wastewater_feed_cases_mgd']:
        for fraction in p['fraction_sent_to_ro']:
            ro_feed = feed * fraction
            reject = ro_feed * (1 - p['reuse_ro_recovery'])
            water.append(dict(feed_mgd=feed, ro_fraction=fraction,
                ro_product_mgd=ro_feed-reject, qualified_direct_reuse_mgd=feed-ro_feed,
                combined_water_product_mgd=feed-reject, membrane_reject_mgd=reject,
                qualification='ASSUMED; direct-use chemistry and module losses unresolved',
                incremental_atlas_water_credit_mgd=None, installed_cost_usd=None))
    out['retrofit_water_scenarios'] = water
    desal_product = p['desal_product_mgd'] * M3_PER_MG
    intake = desal_product / p['whole_plant_recovery']
    ro_feed = desal_product / p['swro_recovery']
    residual = intake-desal_product
    out['desal_balance'] = [dict(product_mgd=p['desal_product_mgd'],
        product_m3_d_online=desal_product, intake_m3_d_online=intake,
        ro_feed_m3_d_online=ro_feed, ro_reject_m3_d_online=ro_feed-desal_product,
        pretreatment_residual_m3_d_online=intake-ro_feed,
        combined_residual_m3_d_online=residual,
        feed_salt_t_d_online=intake*p['seawater_tds_kg_m3']/1000,
        ro_feed_salt_t_d_online=ro_feed*p['seawater_tds_kg_m3']/1000,
        annual_water_m3=desal_product*365*p['water_availability'],
        residual_fate='UNRESOLVED; no routine marine process-liquid release',
        all_in_capital_usd=None)]
    compute=[]; wue=[]; heat=[]; hp=[]
    for it in p['compute_it_nameplate_mw']:
        avg_it = it*p['compute_average_load_fraction']
        avg_site = avg_it*p['pue']
        kwh = avg_site*1000*8760
        captured = avg_it*p['recoverable_it_heat_fraction']
        for tariff in p['electricity_tariff_usd_kwh']:
            compute.append(dict(it_nameplate_mw=it, average_it_mw=avg_it,
                pue=p['pue'], peak_compute_site_mw=it*p['pue'],
                average_compute_site_mw=avg_site, annual_compute_gwh=kwh/1e6,
                assumed_tariff_usd_kwh=tariff, compute_electricity_usd_y=kwh*tariff,
                recoverable_low_grade_heat_mw_average=captured,
                compute_capex_usd=None, useful_compute_revenue_usd_y=None,
                net_environmental_credit=None))
        for consumption_wue in p['consumptive_wue_l_per_it_kwh']:
            consumed_l_d=avg_it*1000*24*consumption_wue
            for coc in p['cooling_cycles_of_concentration']:
                evaporation=consumed_l_d/1000
                blowdown=evaporation/(coc-1) if evaporation else 0
                makeup=evaporation+blowdown
                wue.append(dict(it_nameplate_mw=it,
                    assumed_consumptive_wue_l_it_kwh=consumption_wue,
                    cycles_of_concentration=coc,
                    cooling_consumption_mgd=evaporation/M3_PER_MG,
                    blowdown_mgd=blowdown/M3_PER_MG,
                    makeup_with_blowdown_mgd=makeup/M3_PER_MG,
                    boundary='Analyst evaporative envelope; drift and domestic uses excluded; WUE0 is dry-heat-rejection case'))
        for source_temp in p['heat_source_temperature_c']:
            duty_temp=source_temp-p['heat_exchanger_approach_c']
            latent_kwh_d=captured*1000*24
            latent_m3_d=latent_kwh_d/p['illustrative_latent_duty_kwh_m3']
            heat.append(dict(it_nameplate_mw=it, source_temperature_c=source_temp,
                exchanger_approach_c=p['heat_exchanger_approach_c'],
                max_sink_supply_temperature_c=duty_temp,
                captured_heat_mw_average=captured,
                ideal_single_effect_latent_equivalent_m3_d=latent_m3_d,
                ideal_latent_equivalent_fraction_of_avg_desal_residual=latent_m3_d/(residual*p['water_availability']),
                basis='Energy-only ceiling for stated duty, not predicted evaporation; no MVR electricity saving credited',
                mvr_electricity_saving_kwh=None))
        for cop in p['hypothetical_heat_pump_heating_cop']:
            power=captured/(cop-1)
            hp.append(dict(it_nameplate_mw=it, assumed_heating_cop=cop,
                source_heat_mw=captured, added_compressor_electricity_mw=power,
                delivered_heat_mw=captured+power,
                status='Algebraic sensitivity only; COP depends on lift and actual machine; not MVR saving'))
    out['compute_energy_cost']=compute
    out['cooling_water_envelope']=wue
    out['heat_matching']=heat
    out['heat_pump_sensitivity']=hp
    out['desal_energy']=[dict(sec_kwh_m3=sec, annual_gwh=desal_product*365*p['water_availability']*sec/1e6,
        average_mw=desal_product*p['water_availability']*sec/24000,
        annual_electricity_usd_at_010=desal_product*365*p['water_availability']*sec*.1,
        scope='Water-production boundary only; not mineral recovery, residual closure or conveyance')
        for sec in p['desal_sec_kwh_m3']]
    n=[]
    for flow in p['side_stream_cases_m3_d']:
        P=flow*p['side_stream_p_mg_l']/1000
        N=flow*p['side_stream_nh4_n_mg_l']/1000
        p_recovered=min(P*p['phosphorus_capture'], N*30.973762/14.0067)
        struvite=p_recovered*245.406/30.973762
        n.append(dict(side_stream_m3_d=flow, assumed_reactive_p_mg_l=p['side_stream_p_mg_l'],
            assumed_ammonium_n_mg_l=p['side_stream_nh4_n_mg_l'],
            recovered_p_kg_d=p_recovered, pure_struvite_kg_d=struvite,
            magnesium_required_kg_d=p_recovered*24.305/30.973762,
            gross_product_value_low_usd_d=struvite/1000*(2800/7.25),
            gross_product_value_high_usd_d=struvite/1000*(3500/7.25),
            status='ASSUMED FEED and NEEDS SOURCING URLS product prices; not Greenwood yield',
            net_margin_usd=None, actual_side_stream_flow_m3_d=None))
    out['nutrient_sidecar_scenarios']=n
    # Whole RO feed inventory, not double-counted RO reject plus seawater feed.
    minerals=[]
    for name, c in p['illustrative_seawater_ions_mg_l'].items():
        minerals.append(dict(species=name, feed_concentration_mg_l=c,
            ro_feed_inventory_t_d_online=ro_feed*c/1e6,
            basis='Representative assumed feed; not assay, recovery or product',
            actual_qualified_product_t_d=None, actual_net_revenue_usd_y=0))
    out['mineral_inventory']=minerals
    campaign=[];streams=[]
    for rate in p['landfill_screen_nominal_t_h']:
        feed=rate*p['landfill_shift_hours']*p['landfill_effective_availability']
        campaign.append(dict(screen_nominal_t_h=rate, campaign_day_feed_metric_t=feed,
            campaign_days_y=p['landfill_campaign_days_y'], annual_feed_metric_t=feed*p['landfill_campaign_days_y'],
            complete_line_sustained_t_h=None, net_landfill_airspace_recovered_m3=None,
            mineral_qualified_output_t=None, installed_cost_usd=None,
            status='Screen-only planning sensitivity; neither guaranteed complete-line rate nor net diversion'))
        for name,fraction in p['landfill_illustrative_feed_fractions'].items():
            streams.append(dict(screen_nominal_t_h=rate, feed_fraction=fraction,
                stream=name, stream_metric_t_campaign_day=feed*fraction,
                qualified_recovered_product_t_d=None, final_disposal_t_d=None,
                status='Hypothetical composition, not Corpus assay; no assumed diversion fraction'))
    out['landfill_campaigns']=campaign
    out['landfill_stream_envelopes']=streams
    return out


def write_outputs(out):
    target=ROOT/'results';target.mkdir(exist_ok=True)
    for name,rows in out.items():
        with (target/(name+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (target/'summary.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    write_outputs(evaluate(json.loads((ROOT/'inputs.json').read_text())))
    print('Scenario exports updated; unknown costs and actual performance remain unresolved.')
