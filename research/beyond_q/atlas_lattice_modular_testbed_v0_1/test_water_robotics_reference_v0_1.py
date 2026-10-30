import unittest
from water_robotics_reference_v0_1 import Config, simulate

class SimulationTests(unittest.TestCase):
    def test_water_balance(self):
        m=simulate()["metrics"]
        self.assertAlmostEqual(m["water_served_m3"],m["water_recovered_m3"]+m["makeup_water_m3"],places=4)
    def test_no_outages_short_run(self):
        m=simulate(Config(days=10))["metrics"]
        self.assertEqual(m["unserved_demand_m3"],0)
        self.assertEqual(m["repair_events"],0)
    def test_repair_is_triggered(self):
        m=simulate(Config(days=20,daily_degradation=0.05,inspection_every_days=2))["metrics"]
        self.assertGreater(m["repair_events"],0)
        self.assertGreater(m["unserved_demand_m3"],0)
    def test_missing_spares(self):
        r=simulate(Config(days=12,daily_degradation=0.1,inspection_every_days=1,initial_spares=0))
        self.assertIn("unrepaired_fault_no_qualified_spare",[e["event"] for e in r["events"]])
    def test_invalid_parameters(self):
        with self.assertRaises(ValueError): simulate(Config(nominal_recovery_fraction=1.5))

if __name__ == "__main__": unittest.main()
