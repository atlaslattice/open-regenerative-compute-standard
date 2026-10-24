import json
import unittest
from scenarios import ROOT, evaluate, M3_PER_MG

class ConservationAndBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.p=json.loads((ROOT/'inputs.json').read_text());self.o=evaluate(self.p)

    def test_water_conservation(self):
        for r in self.o['retrofit_water_scenarios']:
            self.assertAlmostEqual(r['feed_mgd'],r['combined_water_product_mgd']+r['membrane_reject_mgd'])
            self.assertIsNone(r['incremental_atlas_water_credit_mgd'])

    def test_desal_distinct_recoveries(self):
        r=self.o['desal_balance'][0]
        self.assertAlmostEqual(r['intake_m3_d_online'],r['product_m3_d_online']+r['combined_residual_m3_d_online'])
        self.assertAlmostEqual(r['combined_residual_m3_d_online'],r['ro_reject_m3_d_online']+r['pretreatment_residual_m3_d_online'])

    def test_no_heat_free_electricity(self):
        for r in self.o['heat_matching']:self.assertIsNone(r['mvr_electricity_saving_kwh'])
        for r in self.o['heat_pump_sensitivity']:
            self.assertGreaterEqual(r['added_compressor_electricity_mw'],0)
            self.assertAlmostEqual(r['delivered_heat_mw'],r['source_heat_mw']+r['added_compressor_electricity_mw'])

    def test_fivefold_compute_comparison(self):
        rows=self.o['compute_energy_cost']
        a=next(r for r in rows if r['it_nameplate_mw']==100 and r['assumed_tariff_usd_kwh']==.1)
        b=next(r for r in rows if r['it_nameplate_mw']==500 and r['assumed_tariff_usd_kwh']==.1)
        self.assertAlmostEqual(b['annual_compute_gwh'],5*a['annual_compute_gwh'])
        self.assertAlmostEqual(a['annual_compute_gwh'],906.66)

    def test_cooling_evaporation_not_recoverable(self):
        for r in self.o['cooling_water_envelope']:
            self.assertAlmostEqual(r['makeup_with_blowdown_mgd'],r['cooling_consumption_mgd']+r['blowdown_mgd'])

    def test_nutrient_inventory(self):
        for r in self.o['nutrient_sidecar_scenarios']:
            self.assertLessEqual(r['recovered_p_kg_d'],r['side_stream_m3_d']*self.p['side_stream_p_mg_l']/1000)
            self.assertIsNone(r['net_margin_usd'])

    def test_missing_costs_not_zero(self):
        self.assertIsNone(self.o['desal_balance'][0]['all_in_capital_usd'])
        for r in self.o['compute_energy_cost']:self.assertIsNone(r['compute_capex_usd'])

    def test_inventory_is_not_recovery(self):
        for r in self.o['mineral_inventory']:
            self.assertIsNone(r['actual_qualified_product_t_d'])
            self.assertEqual(r['actual_net_revenue_usd_y'],0)

    def test_landfill_streams_conserve_feed(self):
        for r in self.o['landfill_campaigns']:
            rows=[x for x in self.o['landfill_stream_envelopes'] if x['screen_nominal_t_h']==r['screen_nominal_t_h']]
            self.assertAlmostEqual(sum(x['stream_metric_t_campaign_day'] for x in rows),r['campaign_day_feed_metric_t'])
            self.assertIsNone(r['net_landfill_airspace_recovered_m3'])

if __name__=='__main__':unittest.main()
