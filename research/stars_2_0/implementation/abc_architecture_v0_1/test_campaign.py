import copy,json,unittest
from pathlib import Path
from plan_campaign import validate,campaign
R=Path(__file__).resolve().parent
class IdentityTests(unittest.TestCase):
    def setUp(self):self.r=json.loads((R/'ABC_REGISTRY.json').read_text())
    def test_confirmed_three_configurations(self):
        by=validate(self.r)
        self.assertEqual([len(by[k]['research_modules']) for k in 'ABC'],[3,29,26])
        p=campaign(self.r)
        self.assertTrue(all('THIRD_FINDING_NOT_BOUND' not in c['blockers'] for c in p['primary_configurations']))
        self.assertTrue(all(all(v is None for v in c['planned_metrics'].values()) for c in p['primary_configurations']))
    def reject(self,change):
        r=copy.deepcopy(self.r);change(r)
        with self.assertRaises(ValueError):validate(r)
    def test_no_stars_inheritance_in_a(self):self.reject(lambda r:r['configurations'][0]['research_modules'].append('acoustic_preparation'))
    def test_c_cannot_acquire_new_prism(self):self.reject(lambda r:r['configurations'][2]['research_modules'].append('new_prism'))
    def test_c_cannot_drop_an_original_module(self):self.reject(lambda r:r['configurations'][2]['research_modules'].remove('spin_preparation'))
    def test_b_cannot_drop_acoustics(self):self.reject(lambda r:r['configurations'][1]['research_modules'].remove('acoustic_sustain'))
    def test_b_cannot_duplicate_module(self):self.reject(lambda r:r['configurations'][1]['research_modules'].append('collectors'))
    def test_no_unsupported_third_substitution(self):self.reject(lambda r:r['third_finding'].update(selected_source_id='OTHER'))
    def test_confirmed_requires_named_source(self):self.reject(lambda r:r['third_finding'].update(selected_source_id=None))
    def test_no_automatic_historical_retagging(self):self.reject(lambda r:r['legacy_mappings'][1].update(retag_historical_runs=True))
    def test_no_automatic_performance_promotion(self):self.reject(lambda r:r['configurations'][0].update(performance={'gain':2.54}))
if __name__=='__main__':unittest.main()
