import unittest
from stellar_forge_reference.evidence import dependencies
class Evidence(unittest.TestCase):
    def fixture(self):return [{'id':'source','maturity':'SOURCE_REPRODUCED','provenance':'EXPERIMENTAL_RAW','depends_on':[]},{'id':'parameter','maturity':'NOT_ASSESSED','provenance':'PARAMETRIC_SCENARIO','depends_on':[]},{'id':'total','maturity':'NOT_ASSESSED','provenance':'MODEL_PREDICTION','depends_on':['source','parameter']},{'id':'unrelated','maturity':'NOT_ASSESSED','provenance':'SYNTHETIC_TEST','depends_on':[]}]
    def test_dependency_not_global_contamination(self):
        r=dependencies(self.fixture(),'total');self.assertEqual(r['scenario_dependencies'],['parameter']);self.assertNotIn('unrelated',r['required_dependency_ids'])
    def test_no_input_promotes_model(self):self.assertEqual(dependencies(self.fixture(),'total')['derived_physical_validation'],'NOT_ESTABLISHED_BY_INPUT_MATURITY')
    def test_cycle_missing(self):
        a=self.fixture();a[0]['depends_on']=['total']
        with self.assertRaises(ValueError):dependencies(a,'total')
        with self.assertRaises(ValueError):dependencies(self.fixture(),'missing')
