import copy
import json
import unittest
from pathlib import Path
from model import run, simulate, validate


class ModelChecks(unittest.TestCase):
    def setUp(self):
        self.cfg=json.loads(Path(__file__).with_name('inputs.json').read_text())

    def test_all_scenarios_conserve_mass_and_reserve_inventory(self):
        for _, rows, s in run(self.cfg):
            self.assertEqual(len(rows),365)
            self.assertLess(s['max_abs_mass_error_t'],1e-7)
            self.assertAlmostEqual(s['baseline_wgsl_t'],s['disposal_plus_inventory_t']+s['net_disposal_avoided_t'])
            self.assertIsNone(s['roi'])
            self.assertIsNone(s['recovered_brine_product_t'])

    def test_schedule_has_exactly_300_shifts(self):
        rows,_=simulate(self.cfg,'schedule',50)
        self.assertEqual(sum(r['scheduled_shift'] for r in rows),300)

    def test_no_outlets_no_diversion(self):
        self.cfg['assumptions']['metal_buyer_acceptance']=0
        _,s=simulate(self.cfg,'no buyers',200)
        self.assertEqual(s['net_disposal_avoided_t'],0)

    def test_no_fuel_acceptance_no_fuel_credit(self):
        self.cfg['assumptions']['conditional_combustible_acceptance']=0
        rows,_=simulate(self.cfg,'no fuel',200,True)
        self.assertEqual(sum(r['fuel_nonash_mass_t'] for r in rows),0)

    def test_outage_blocks_hpower_delivery(self):
        rows,_=simulate(self.cfg,'outages',200,True,True)
        self.assertTrue(any(r['fuel_buffer_t']>0 for r in rows))
        self.assertTrue(all(r['fuel_to_hpower_t']==0 for r in rows if r['hpower_outage']))

    def test_stockpile_never_earns_diversion(self):
        self.cfg['assumptions']['conditional_hpower_spare_t_per_day']=0
        rows,s=simulate(self.cfg,'no sink',200,True)
        self.assertGreater(s['final_fuel_inventory_t'],0)
        self.assertEqual(sum(r['fuel_nonash_mass_t'] for r in rows),0)
        self.assertAlmostEqual(s['net_disposal_avoided_t'],s['accepted_metals_t']+s['manufactured_product_t'])

    def test_water_and_manufacturing_are_bounded(self):
        rows,_=simulate(self.cfg,'bounded',200,True,True)
        for r in rows:
            self.assertLessEqual(r['reclaimed_to_dust_m3']+r['reclaimed_to_irrigation_m3'],100+1e-8)
            self.assertLessEqual(r['manufacturing_product_t'],50*.9+1e-8)
            if 151<=r['day']<=160:
                self.assertEqual(r['reclaimed_to_irrigation_m3'],0)

    def test_future_desal_conserves_water(self):
        rows,s=simulate(self.cfg,'future',200,True,False,True)
        for r in rows:
            self.assertAlmostEqual(r['future_desal_feed_m3'],r['future_desal_product_m3']+r['future_concentrate_m3'])
        self.assertGreater(s['future_desal_kwh'],0)
        self.assertIsNone(s['recovered_brine_product_t'])

    def test_invalid_fractions_are_rejected(self):
        self.cfg['assumptions']['feed_fraction']['other']=.9
        with self.assertRaises(AssertionError): validate(self.cfg)


if __name__=='__main__': unittest.main()
