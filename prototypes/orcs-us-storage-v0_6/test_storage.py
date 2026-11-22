"""All figures below are mathematical TEST FIXTURES, not grid observations."""
import unittest
from storage_screen import screen_charge

def record():
    return dict(observed_source_id="TEST_FIXTURE_ONLY",observed_curtailed_mwh=100,
                available_storage_headroom_mwh=80,authorized_charge_mw=20,charging_hours=4,
                charge_efficiency=.8,discharge_efficiency=.9,stored_soc_mwh=5,
                protected_emergency_reserve_mwh=30,authorized_discharge_mw=10,
                discharge_hours=2,reachable_domestic_load_mwh=25,transfer_limit_mwh=14,
                owner_and_operator_authorized=True)

class TestScreen(unittest.TestCase):
    def test_charge(self):self.assertEqual(80,screen_charge(record())['input_charged_mwh'])
    def test_storage(self):self.assertEqual(64,screen_charge(record())['energy_stored_mwh'])
    def test_delivery(self):self.assertEqual(14,screen_charge(record())['potential_domestic_delivery_mwh'])
    def test_no_auto_dispatch(self):self.assertFalse(screen_charge(record())['real_dispatch_authorized'])
    def test_missing_source(self):
        x=record();x.pop('observed_source_id')
        self.assertEqual('UNKNOWN_NO_SOURCE',screen_charge(x)['status'])
    def test_unknown_curtailment(self):
        x=record();x['observed_curtailed_mwh']=None
        self.assertEqual('UNKNOWN_INCOMPLETE',screen_charge(x)['status'])
    def test_authority(self):
        x=record();x['owner_and_operator_authorized']=False
        self.assertEqual('NOT_AUTHORIZED',screen_charge(x)['status'])
    def test_negative(self):
        x=record();x['observed_curtailed_mwh']=-1
        with self.assertRaises(ValueError):screen_charge(x)
    def test_reserve(self):
        x=record();x['protected_emergency_reserve_mwh']=100
        self.assertEqual(0,screen_charge(x)['potential_domestic_delivery_mwh'])
    def test_transfer(self):
        x=record();x['transfer_limit_mwh']=3
        self.assertEqual(3,screen_charge(x)['potential_domestic_delivery_mwh'])
if __name__=="__main__":unittest.main()
