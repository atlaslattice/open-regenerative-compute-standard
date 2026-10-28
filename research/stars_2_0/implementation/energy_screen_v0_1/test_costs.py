import unittest
from costs import installed_capex
class Costs(unittest.TestCase):
    def test_unknown_not_free(self):
        r=installed_capex([dict(asset_id='laser',currency='USD',installed_cost_USD=None)])
        self.assertIsNone(r['total_installed_capex_USD'])
    def test_shared_asset_not_twice(self):
        c=dict(asset_id='cooling',currency='USD',installed_cost_USD=None)
        with self.assertRaises(ValueError):installed_capex([c,c])
    def test_dated_synthetic_costs(self):
        r=installed_capex([dict(asset_id='fixture',currency='USD',installed_cost_USD='12.50',cost_date='2026-10-28',source='SYNTHETIC')])
        self.assertEqual(r['total_installed_capex_USD'],'12.50')
