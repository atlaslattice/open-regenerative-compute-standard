import json
import unittest
from pathlib import Path
from fetch_public import validate,collect_one
from exposure import distance_km,proximity_candidates
from policy_scenarios import candidate_exports
HERE=Path(__file__).resolve().parent
FEEDS=json.loads((HERE/'sources.json').read_text())['feeds']
class Tests(unittest.TestCase):
    def test_registry(self):
        self.assertEqual(13,len(FEEDS))
        self.assertEqual(13,len(set(f['id'] for f in FEEDS)))
    def test_four_prior(self):
        self.assertEqual(4,sum(bool(f.get('prior_snapshot_2026_10_13')) for f in FEEDS))
    def test_geojson(self):
        self.assertTrue(validate({'format':'geojson'},{'type':'FeatureCollection','features':[]}))
        self.assertFalse(validate({'format':'geojson'},{'type':'Point'}))
    def test_array(self):
        self.assertTrue(validate({'format':'array'},[]))
    def test_fema(self):
        self.assertTrue(validate({'format':'fema'},{'DisasterDeclarationsSummaries':[]}))
    def test_stub(self):
        self.assertEqual('NOT_FETCHED_ACCESS_REVIEW',collect_one({'id':'x','access':'owner_authorization','url':None})['status'])
    def test_near(self):
        self.assertEqual(1,len(proximity_candidates([{'id':'e','lat':29.75,'lon':-95.36}],[{'id':'a','lat':29.8,'lon':-95.4}],50)))
    def test_far(self):
        self.assertEqual([],proximity_candidates([{'id':'e','lat':29.75,'lon':-95.36}],[{'id':'a','lat':40.7,'lon':-74.0}],50))
    def test_no_closure(self):
        r=proximity_candidates([{'id':'e','lat':29.75,'lon':-95.36}],[{'id':'a','lat':29.8,'lon':-95.4}],50)[0]
        self.assertFalse(r['closure_verified'])
        self.assertFalse(r['route_impairment_verified'])
    def test_price_unknown(self):
        self.assertIsNone(candidate_exports(100,300,0,20)['price_threshold_met'])
        self.assertEqual(0,candidate_exports(100,300,0,20)['candidate_export_bbl'])
    def test_affordable(self):
        self.assertEqual(180,candidate_exports(100,300,0,20,2.99)['candidate_export_bbl'])
    def test_expensive(self):
        self.assertEqual(0,candidate_exports(100,300,0,20,3.2)['candidate_export_bbl'])
    def test_reserve_short(self):
        self.assertEqual(0,candidate_exports(100,100,0,20,2.99)['candidate_export_bbl'])
    def test_no_rights(self):
        self.assertFalse(candidate_exports(100,300,0,20,2.99)['export_authorized'])
if __name__=='__main__':unittest.main()
