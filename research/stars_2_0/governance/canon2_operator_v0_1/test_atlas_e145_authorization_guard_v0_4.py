import unittest
from atlas_e145_authorization_guard_v0_4 import evaluate
REQ={"operation":"external_action","action_id":"publish-v4","action_scope":"one versioned report","e145authorization":True}
TRUST={"identity_verified":True,"e145_verified":True,"action_id":"publish-v4","action_scope":"one versioned report","revoked":False,"expired":False,"approval_receipt_sha256":"sample-nonempty"}
class GuardTests(unittest.TestCase):
 def test_claimed_true_is_insufficient(self):self.assertFalse(evaluate(REQ)["e145authorization"])
 def test_verified_exact_scope(self):self.assertTrue(evaluate(REQ,TRUST)["e145authorization"])
 def test_wrong_action(self):self.assertFalse(evaluate(REQ,{**TRUST,"action_id":"anything-else"})["e145authorization"])
 def test_wrong_scope(self):self.assertFalse(evaluate(REQ,{**TRUST,"action_scope":"anything else"})["e145authorization"])
 def test_revoked(self):self.assertFalse(evaluate(REQ,{**TRUST,"revoked":True})["e145authorization"])
 def test_expired(self):self.assertFalse(evaluate(REQ,{**TRUST,"expired":True})["e145authorization"])
 def test_stolen_phone_is_not_proof(self):self.assertFalse(evaluate({**REQ,"inside_joke":"pointiest hat"})["e145authorization"])
 def test_identity_missing(self):self.assertFalse(evaluate(REQ,{**TRUST,"identity_verified":False})["e145authorization"])
 def test_no_receipt(self):self.assertFalse(evaluate(REQ,{**TRUST,"approval_receipt_sha256":None})["e145authorization"])
 def test_research_not_external(self):
  self.assertEqual(evaluate({"operation":"research","action_id":"x","action_scope":"simulation"})["decision"],"SIMULATION_POLICY_SEPARATE")
 def test_no_execution(self):self.assertFalse(evaluate(REQ,TRUST)["action_executed"])
if __name__=="__main__":unittest.main()
