"""ORCS real-data controls: fixed negative fixtures, not measured Maui resource flows.

Run from repository root:
  python -m unittest discover -s tests -p 'test_orcs_evidence_guard_v01.py' -v
"""
import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from orcs_evidence_guard_v01 import validate_evidence, validate_allocations, arithmetic


class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.real_ledger = json.loads(
            (ROOT / 'research' / 'maui_mycoprotein_evidence_ledger_v05.json').read_text(encoding='utf8')
        )

    def test_existing_research_ledger(self):
        self.assertEqual([], validate_evidence(self.real_ledger))

    def test_crossyear_must_not_be_measured(self):
        data = copy.deepcopy(self.real_ledger)
        record = next(x for x in data['records'] if x['id'] == 'wcs_crossyear_food_estimate')
        record['evidence'] = 'MEASURED/ADMINISTRATIVE'
        self.assertIn('promoted', ' '.join(validate_evidence(data)))

    def test_calculated_record_must_reconcile(self):
        data = copy.deepcopy(self.real_ledger)
        record = next(x for x in data['records'] if x['id'] == 'wcs_crossyear_food_estimate')
        record['value'] += 100
        self.assertIn('reconcile', ' '.join(validate_evidence(data)))

    def test_source_must_be_traceable(self):
        data = copy.deepcopy(self.real_ledger)
        data['records'][0]['source'] = 'citation missing'
        self.assertIn('https URL', ' '.join(validate_evidence(data)))

    def test_external_experiment_is_not_maui_output(self):
        data = copy.deepcopy(self.real_ledger)
        record = next(x for x in data['records'] if x['id'] == 'fusarium_expired_drink_titer')
        record['scope'] = 'Maui operational production'
        self.assertIn('external study', ' '.join(validate_evidence(data)))

    def test_formula_never_evaluates_code(self):
        with self.assertRaises(ValueError):
            arithmetic('__import__("os").system("id")')


class PhysicalAllocationTests(unittest.TestCase):
    """Lot below is a synthetic unit-test fixture, NOT an existing farm contract."""

    def alloc(self):
        return {'schema':'orcs.resource-allocation.v1',
                'source_lots':[{
                    'lot_id':'test-lot',
                    'source_category':'preconsumer_food_processor',
                    'provenance':'SYNTHETIC TEST ONLY; no actual lot',
                    'verified_food_grade':True
                }],
                'allocations':[
                    {'allocation_id':'a','lot_id':'test-lot','source_fraction':.6,
                     'destination':'food_grade_recovered_carbohydrate',
                     'food_grade_product':True,'downstream_media_food_grade_verified':True,
                     'strain_and_product_regulatory_review':True,'realized_credit':0},
                    {'allocation_id':'b','lot_id':'test-lot','source_fraction':.4,
                     'destination':'compost','realized_credit':0}
                ]}

    def test_allocation_partition_is_conserved(self):
        self.assertEqual([], validate_allocations(self.alloc()))

    def test_overallocated_same_source_lot_rejected(self):
        d = self.alloc()
        d['allocations'][1]['source_fraction'] = .8
        self.assertIn('double-counted', ' '.join(validate_allocations(d)))

    def test_duplicate_allocation_id_rejected(self):
        d = self.alloc()
        d['allocations'][1]['allocation_id'] = 'a'
        self.assertIn('duplicate', ' '.join(validate_allocations(d)))

    def test_restricted_material_rejected_for_food(self):
        for material in ('biosolids','municipal_mixed','industrial_brine'):
            with self.subTest(category=material):
                d = self.alloc()
                d['source_lots'][0]['source_category'] = material
                self.assertIn('restricted source', ' '.join(validate_allocations(d)))

    def test_recovery_does_not_automatically_qualify_as_food(self):
        d = self.alloc()
        d['allocations'][0]['downstream_media_food_grade_verified'] = False
        self.assertIn('food-grade source', ' '.join(validate_allocations(d)))

    def test_missing_audited_credit_receipt_rejected(self):
        d = self.alloc()
        d['allocations'][0]['realized_credit'] = 100
        self.assertIn('observed and audited', ' '.join(validate_allocations(d)))

    def test_unknown_provenance_rejected(self):
        d = self.alloc()
        d['source_lots'][0]['provenance'] = ''
        self.assertIn('provenance UNKNOWN', ' '.join(validate_allocations(d)))


if __name__ == '__main__':
    unittest.main()
