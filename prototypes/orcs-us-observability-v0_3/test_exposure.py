import unittest
from exposure import distance_km,proximity_candidates

class ExposureTests(unittest.TestCase):
    def test_same_site(self):
        self.assertEqual(distance_km({'lat':0,'lon':0},{'lat':0,'lon':0}),0)
    def test_near_hazard(self):
        a=[{'id':'a','lat':29.8,'lon':-95.4}]
        e=[{'id':'e','lat':29.75,'lon':-95.36}]
        x=proximity_candidates(e,a,50)
        self.assertEqual(len(x),1)
        self.assertFalse(x[0]['closure_verified'])
    def test_far_hazard(self):
        self.assertEqual([],proximity_candidates([{'id':'e','lat':29.75,'lon':-95.36}],[{'id':'a','lat':40.7,'lon':-74.0}],50))
    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError): distance_km({'lat':120,'lon':0},{'lat':0,'lon':0})
