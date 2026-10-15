"""Numerical tests only. Fixture values are NOT field or mineral measurements."""
import unittest
from allocation import assess,source_inventory

def fixture():
    return dict(site_id="TEST_ONLY",batch_source_url="https://example.org/test-fixture",
        observation_date="TEST_DATE",status="MEASURED_QUALIFIED",
        certificate_reference="TEST_CERTIFICATE_NOT_REAL",qualified_tonnes=100,
        soil_product_approved=True,acid_process_verified=True,
        allocation_tonnes={"agriculture":30,"sulfuric_acid":40,"industrial":10,"resilience_reserve":10})

class Tests(unittest.TestCase):
    def test_source_catalog(self):self.assertEqual(5,len(source_inventory()["sources"]))
    def test_site_is_proposed(self):self.assertEqual("THEORETICAL_COMPOSITION_CEILING",source_inventory()["prior_model_ceiling"][0]["quality"])
    def test_not_operational(self):
        x=fixture();x["status"]="THEORETICAL_COMPOSITION_CEILING"
        self.assertEqual("UNKNOWN_UNQUALIFIED_GYPSUM",assess(x)["status"])
    def test_mass_pass(self):self.assertEqual("MASS_BALANCE_ONLY",assess(fixture())["status"])
    def test_unallocated(self):self.assertEqual(10,assess(fixture())["unallocated_t"])
    def test_double_count(self):
        x=fixture();x["allocation_tonnes"]["agriculture"]=90
        self.assertEqual("REJECTED_DOUBLE_COUNT",assess(x)["status"])
    def test_no_crop_safety(self):
        x=fixture();x["soil_product_approved"]=False
        self.assertEqual("UNKNOWN_AGRONOMIC_SAFETY",assess(x)["status"])
    def test_no_acid_process(self):
        x=fixture();x["acid_process_verified"]=False
        self.assertEqual("UNKNOWN_ACID_PROCESS",assess(x)["status"])
    def test_unknown_source(self):
        x=fixture();x["batch_source_url"]=""
        self.assertEqual("UNKNOWN_SOURCE",assess(x)["status"])
    def test_no_export_authority(self):self.assertFalse(assess(fixture())["export_authorized"])
if __name__=="__main__":unittest.main()
