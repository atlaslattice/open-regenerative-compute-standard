import csv,json,unittest
from pathlib import Path
from design_extensions import schedule_comparison,recovery_incentive,management_cost,integrated_outputs
ROOT=Path(__file__).parent
class DesignTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.inputs=json.loads((ROOT/'inputs.json').read_text());cls.outputs=integrated_outputs(cls.inputs,ROOT)
 def test_marine_is_counted_once(self):
  rows=self.outputs['disjoint_historical_cost_groups']
  self.assertEqual(sum(r['estimate_2025_usd'] for r in rows),997289133)
  self.assertEqual(next(r['estimate_2025_usd'] for r in rows if r['category']=='nonmarine_other_physical'),522809432)
 def test_other_works_detail_reconciles(self):
  with (ROOT/'other_physical_works_detail.csv').open() as f:r=list(csv.DictReader(f))
  self.assertEqual(sum(int(x['estimate_2025_usd']) for x in r),674303247)
 def test_2026_hierarchy_reconciles(self):
  rows=self.outputs['corpus_2026_cost_detail']
  for parent in ['treatment','construction','project']:
   expected=int(next(x['estimate_usd'] for x in rows if x['category']==parent))
   self.assertEqual(sum(int(x['estimate_usd']) for x in rows if x['parent_category']==parent),expected)
 def test_salary_unknown_not_free(self):
  self.assertIsNone(management_cost(self.inputs['management_policy']))
  self.assertEqual(self.outputs['management_policy_summary']['spend_linked_fee_rate'],0)
  self.assertIsNone(self.outputs['management_policy_summary']['total_management_cost_usd'])
 def test_salary_duration_and_employer_cost(self):
  p=dict(self.inputs['management_policy'],salary_usd_year=100,employer_burden_usd_year=20,management_fte=2,management_duration_years=3,verified_reimbursable_costs_usd=10)
  self.assertEqual(management_cost(p),730)
 def test_twice_duration_is_not_total_project(self):
  r=schedule_comparison(10,2);self.assertEqual(r['proposed_construction_months'],20);self.assertIsNone(r['total_project_months'])
  self.assertEqual(schedule_comparison(10,2,5,3)['total_project_months'],28)
 def test_no_double_sold_consumed(self):
  with self.assertRaises(ValueError):recovery_incentive(6,5,10,100,100,0,0,.1,100,True)
 def test_negative_value_no_bonus(self):
  self.assertEqual(recovery_incentive(10,0,10,10,0,110,0,.1,100,True)['incentive_usd'],0)
 def test_bonus_is_net_incremental_capped(self):
  r=recovery_incentive(5,5,10,100,80,100,100,.2,100,True)
  self.assertEqual(r['incremental_net_value_usd'],700);self.assertEqual(r['incentive_usd'],100)
 def test_unresolved_gate_blocks_award(self):
  for gate in [False,None]:self.assertIsNone(recovery_incentive(10,0,10,100,0,0,0,.1,100,gate)['incentive_usd'])
 def test_missing_rate_blocks_award(self):
  self.assertIsNone(recovery_incentive(10,0,10,100,0,0,0,None,100,True)['incentive_usd'])
 def test_redesign_has_no_priced_total(self):
  for row in self.outputs['redesign_sensitivity']:
   self.assertIsNone(row['net_alternative_total_usd']);self.assertEqual(row['marine_saving_usd'],0)
 def test_existing_reuse_not_credited(self):
  self.assertIsNone(self.inputs['wastewater_integration']['firm_reuse_at_required_quality_mgd'])
 def test_historical_management_not_erased(self):
  rows=self.outputs['corpus_2026_cost_detail']
  self.assertEqual(int(next(x['estimate_usd'] for x in rows if x['category']=='general_conditions')),71560000)
if __name__=='__main__':unittest.main()
