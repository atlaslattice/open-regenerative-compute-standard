import unittest
from decimal import Decimal
from check_anchors import atomic_to_mass_stopping,check,NA

class Tests(unittest.TestCase):
    def test_dimensions_against_per_atom_accounting(self):
        e=Decimal('2.72e-15');m=Decimal('10.05')
        # Independent reference: one gram contains NA/m atoms; eV to MeV.
        expected=(NA/m)*e/Decimal(1000000)
        self.assertLess(abs(atomic_to_mass_stopping(e,m)-expected),Decimal('1e-24'))
    def test_mass_dependence(self):
        self.assertEqual(atomic_to_mass_stopping(1,2),atomic_to_mass_stopping(1,1)/2)
    def test_invalid_values(self):
        for e,m in [(1,0),(-1,2),('NaN',2),(1,'Infinity')]:
            with self.assertRaises(ValueError):atomic_to_mass_stopping(e,m)
    def test_no_material_promotion(self):
        r=check();self.assertEqual(len(r['anchors']),2)
        self.assertIn('B10 enriched',r['restrictions'][0]);self.assertFalse(r['primary_pdf_hash_verified'])

if __name__=='__main__':unittest.main()
