import unittest
from atlas_canon2_operator_v0_3_e145_quarantine import decide,QUARANTINE_CONFLICT_IDS
S={'git_blob':'sha','sha256':'sha'}
Q={'sha256':'quarantine_sha','record':{'status':'QUARANTINED_PENDING_COUNCIL_REVIEW'}}
BASE={'operation':'research','operator':'H01.S01.N01','simulation':True,'external_effect':False,
 'claim_status':'CANDIDATE','source_receipts':[{'source':'source/path','sha256':'a'*64}]}
class TestE145Quarantine(unittest.TestCase):
 def run_policy(self,**kwargs):return decide({**BASE,**kwargs},S,Q)
 def test_research_proceeds(self):self.assertEqual(self.run_policy()['status'],'ALLOW_SIMULATION_ONLY')
 def test_debate_proceeds(self):self.assertEqual(self.run_policy(operation='council_debate')['status'],'ALLOW_SIMULATION_ONLY')
 def test_quarantine_is_disclosed(self):self.assertEqual(set(self.run_policy()['quarantined_conflicts']),QUARANTINE_CONFLICT_IDS)
 def test_e145_scope(self):self.assertEqual(self.run_policy()['e145_project_final_authority'],'USER_CONVENOR')
 def test_e145_not_identity_authenticated(self):self.assertFalse(self.run_policy()['e145_identity_verified'])
 def test_no_unsafe_research(self):self.assertEqual(self.run_policy(external_effect=True)['status'],'DENY')
 def test_no_unsimulated_research(self):self.assertEqual(self.run_policy(simulation=False)['status'],'DENY')
 def test_no_missing_source(self):self.assertEqual(self.run_policy(source_receipts=[])['status'],'DENY')
 def test_no_invalid_address(self):self.assertEqual(self.run_policy(operator='H13.S01.N01')['status'],'DENY')
 def test_promotion_no_auth(self):self.assertEqual(self.run_policy(operation='canon_promotion')['status'],'DENY')
 def test_promotion_with_reciepts_still_review(self):
  x=self.run_policy(operation='canon_promotion',human_authorized=True,human_authorization_receipt='x',human_ratification_receipt='y')
  self.assertEqual(x['status'],'REVIEW_REQUIRED');self.assertFalse(x['canon_promoted'])
 def test_deployment_still_review(self):
  self.assertEqual(self.run_policy(operation='deployment',simulation=False,human_authorized=True,human_authorization_receipt='x')['status'],'REVIEW_REQUIRED')
 def test_external_action_still_review(self):
  self.assertEqual(self.run_policy(operation='external_action',simulation=False,human_authorized=True,human_authorization_receipt='x')['status'],'REVIEW_REQUIRED')
 def test_resolved_flag_not_bypass(self):
  self.assertEqual(self.run_policy(operation='deployment',simulation=False,human_authorized=True,human_authorization_receipt='x',resolved=True)['status'],'REVIEW_REQUIRED')
 def test_no_effect(self):self.assertFalse(self.run_policy()['action_executed'])
 def test_no_canon_mutation(self):self.assertFalse(self.run_policy()['historical_canon_amended'])
if __name__=='__main__':unittest.main()
