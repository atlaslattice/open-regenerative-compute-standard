import unittest
from atlas_canon2_operator_v0_1 import decide, APPLICABLE, CONFLICTS
FAKE={'git_blob':'pinned_blob','sha256':'pinned_sha'}
BASE={'operation':'research','operator':'H01.S01.N01','simulation':True,'external_effect':False,
 'source_receipts':[{'source':'repo/path','sha256':'a'*64}], 'claim_status':'CANDIDATE'}
class Canon2Tests(unittest.TestCase):
 def invoke(self,**changes):return decide({**BASE,**changes},FAKE)
 def test_address_count(self):self.assertEqual(12**3,1728)
 def test_research(self):self.assertEqual(self.invoke()['status'],'ALLOW_SIMULATION_ONLY')
 def test_bad_address(self):self.assertEqual(self.invoke(operator='H00.S01.N01')['status'],'DENY')
 def test_out_of_range_address(self):self.assertEqual(self.invoke(operator='H13.S01.N01')['status'],'DENY')
 def test_missing_source(self):self.assertEqual(self.invoke(source_receipts=[])['status'],'DENY')
 def test_external_effect(self):self.assertEqual(self.invoke(external_effect=True)['status'],'DENY')
 def test_unsimulated_research(self):self.assertEqual(self.invoke(simulation=False)['status'],'DENY')
 def test_canon_overclaim(self):self.assertEqual(self.invoke(claim_status='CANON')['status'],'DENY')
 def test_canon_missing_ratification(self):self.assertEqual(self.invoke(operation='canon_promotion',human_authorized=True,human_authorization_receipt='x')['status'],'DENY')
 def test_canon_receipted_still_review(self):
  x=self.invoke(operation='canon_promotion',human_authorized=True,human_authorization_receipt='x',human_ratification_receipt='y')
  self.assertEqual(x['status'],'REVIEW_REQUIRED');self.assertIn('CON-05',x['conflict_ids'])
 def test_deploy_without_auth(self):self.assertEqual(self.invoke(operation='deployment')['status'],'DENY')
 def test_deploy_with_auth_still_review(self):
  x=self.invoke(operation='deployment',human_authorized=True,human_authorization_receipt='x',simulation=False)
  self.assertEqual(x['status'],'REVIEW_REQUIRED');self.assertIn('CON-01',x['conflict_ids'])
 def test_fake_resolution(self):
  x=self.invoke(operation='deployment',human_authorized=True,human_authorization_receipt='x',simulation=False,resolved=True)
  self.assertEqual(x['status'],'REVIEW_REQUIRED')
 def test_majority_cannot_promote(self):
  x=self.invoke(operation='council_debate',votes_for=1728)
  self.assertFalse(x['canon_promoted'])
 def test_unsupported_operation(self):self.assertEqual(self.invoke(operation='delete_history')['status'],'DENY')
 def test_all_families(self):self.assertEqual(len(set(sum((list(v) for v in APPLICABLE.values()),[]))),12)
 def test_conflicts(self):self.assertEqual(len(CONFLICTS),5)
 def test_no_action_claim(self):self.assertFalse(self.invoke()['action_executed'])
if __name__=='__main__':unittest.main()
