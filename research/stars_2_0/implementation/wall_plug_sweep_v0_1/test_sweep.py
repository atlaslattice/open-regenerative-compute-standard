import unittest
from run import scenario, control
from containment import pulsed_coil,steady_coil

class SweepTests(unittest.TestCase):
    def test_pinned_ratio(self): self.assertAlmostEqual(control()[0]['nuclear_release_J'],5.983277924531208e-6,places=16)
    def test_optical_chain(self):
        r=scenario(.1,.1,0.,1.);self.assertAlmostEqual(r['main_laser_wall_J_per_fired'],100.)
        self.assertAlmostEqual(r['net_electric_W'],-99.+r['nuclear_J_per_fired'])
    def test_no_nuclear_no_free_energy(self):
        # Perfect refunds expose ONLY the nuclear term; no duplicated beam credit.
        r=scenario(.1,.1,1.,1.);self.assertAlmostEqual(r['net_electric_W'],r['nuclear_J_per_fired'],places=12)
    def test_coil_cost(self):
        r=scenario(.1,.1,0.,1.,coil_optical_J=500.,coil_eta=.1)
        self.assertEqual(r['containment_wall_J_per_fired'],5000.)
        self.assertAlmostEqual(r['net_electric_W'],-5099.+r['nuclear_J_per_fired'])
        self.assertGreater(r['required_source_remainder_refund_if_downstream_perfect'],1.)
    def test_continuous_hold_rate(self):
        a=scenario(.1,.1,0.,1.,rate=.1,hold_W=1000.)
        b=scenario(.1,.1,0.,1.,rate=10.,hold_W=1000.)
        self.assertAlmostEqual(a['net_electric_W']-.1*(-99.+a['nuclear_J_per_fired']),-1000.)
        self.assertAlmostEqual(b['net_electric_W']-10*(-99.+b['nuclear_J_per_fired']),-1000.)
    def test_all_attempt_cost(self):
        r=scenario(.1,.1,0.,1.,fired=.5,hold_W=1000.)
        self.assertAlmostEqual(r['gross_wall_W'],1050.)
    def test_zero_efficiency_rejected(self):
        with self.assertRaises(ValueError): scenario(0.,.1,0.,1.)
    def test_duplicate_containment_rejected(self):
        with self.assertRaises(ValueError): scenario(.1,.1,0.,1.,hold_W=1000.,coil_optical_J=500.)
    def test_pulsed_recovery(self):
        # Numerical circuit fixture, not a coil specification.
        r=pulsed_coil(2.,3.,4.,5.,.5);self.assertEqual(r['peak_field_inventory_J'],9.);self.assertEqual(r['electric_J_per_pulse'],184.5)
    def test_steady_storage_not_power(self):
        r=steady_coil(2.,3.,0.,7.);self.assertEqual(r['startup_field_inventory_J'],9.);self.assertEqual(r['steady_wall_W'],7.)

if __name__=='__main__': unittest.main()
