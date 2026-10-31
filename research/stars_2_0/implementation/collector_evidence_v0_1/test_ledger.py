import unittest
from terminal_ledger import terminal_ledger
class Tests(unittest.TestCase):
 def test_tmx_signed_terminals(self):
  r=terminal_ledger([{'id':'collector','voltage_V':565.,'net_positive_charge_current_into_electrode_A':.14},{'id':'suppressor','voltage_V':-500.,'net_positive_charge_current_into_electrode_A':.025}],139.5)
  self.assertAlmostEqual(r['terminal_gross_out_W'],79.1);self.assertAlmostEqual(r['terminal_external_draw_W'],12.5);self.assertAlmostEqual(r['net_terminal_out_W'],66.6)
 def test_electron_current_reduces_output(self):
  r=terminal_ledger([{'id':'collector','voltage_V':1000.,'net_positive_charge_current_into_electrode_A':-.01}],1.)
  self.assertEqual(r['net_terminal_out_W'],-10.);self.assertEqual(r['net_fraction_of_declared_incident_power'],-10.)
 def test_missing_is_not_zero_efficiency(self):self.assertIsNone(terminal_ledger([],None)['net_fraction_of_declared_incident_power'])
 def test_zero_incident_ratio_undefined(self):self.assertIsNone(terminal_ledger([],0.)['net_fraction_of_declared_incident_power'])
 def test_negative_voltage_negative_current_delivers(self):self.assertEqual(terminal_ledger([{'id':'negative','voltage_V':-2.,'net_positive_charge_current_into_electrode_A':-3.}])['net_terminal_out_W'],6.)
 def test_duplicate_is_rejected(self):
  t={'id':'x','voltage_V':1.,'net_positive_charge_current_into_electrode_A':1.}
  with self.assertRaises(ValueError):terminal_ledger([t,t])
 def test_bad_inputs(self):
  for value in [True,float('nan'),float('inf')]:
   with self.assertRaises(ValueError):terminal_ledger([{'id':'x','voltage_V':value,'net_positive_charge_current_into_electrode_A':1.}])
 def test_no_facility_promotion(self):self.assertIsNone(terminal_ledger([],1.)['wall_plug_net_power_W'])
if __name__=='__main__':unittest.main()
