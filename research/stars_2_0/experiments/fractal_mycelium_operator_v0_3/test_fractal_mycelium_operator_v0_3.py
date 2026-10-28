import unittest
from fractal_mycelium_operator_v0_3 import *
H=Hypothesis("H01.S01.N01","Test cross-domain reuse",("gamma:fractal","gamma:swarm"),"unvalidated",dissent=("counterclaim",))
G={"H01.S01.N01":["H01.S01.N02","H02.S01.N01"],"H01.S01.N02":["H03.S01.N01"]}
class Integration(unittest.TestCase):
 def test_ledger_hash_chain(self):
  l=WitnessLedger();l.append("HYPOTHESIS",H.id,{"claim":H.claim});l.append("DISSENT",H.id,{"objection":"counterclaim"});self.assertTrue(l.verify());l.records[0]["body"]["claim"]="tampered";self.assertFalse(l.verify())
 def test_sources(self):
  with self.assertRaises(ValueError):Hypothesis(H.origin,H.claim,(),"unsure").validate()
 def test_no_canon_spoof(self):
  with self.assertRaises(ValueError):Hypothesis(H.origin,H.claim,("ref",),"unsure",classification="CANON").validate()
 def test_opt_in(self):
  r=spores(H,G,{},opted_in=["H01.S01.N02"]);self.assertEqual(r["invited"],["H01.S01.N02"])
 def test_budget(self):
  h=Hypothesis(H.origin,H.claim,("a",),"u",max_invites=1);self.assertEqual(len(spores(h,G,{},opted_in=["H01.S01.N02","H02.S01.N01"])["invited"]),1)
 def test_blocked(self):
  self.assertNotIn("H02.S01.N01",spores(H,G,{},blocked=["H02.S01.N01"],opted_in=["H02.S01.N01","H01.S01.N02"])["invited"])
 def test_isolated(self):
  h=Hypothesis(H.origin,H.claim,("a",),"u",consent_scope="isolated-research");self.assertEqual(spores(h,G,{})["status"],"ISOLATED_NO_PROPAGATION")
 def test_consent(self):
  with self.assertRaises(ValueError):Hypothesis(H.origin,H.claim,("a",),"u",consent_scope="private").validate()
 def test_council_flag(self):
  self.assertEqual(council_review(H,{"MANDOG":"FLAG"})["research_decision"],"QUARANTINE_FOR_HUMAN_REVIEW")
 def test_reward_no_unverified_gain(self):
  self.assertEqual(reward_update(0,"VERIFIED_USEFUL",source_verified=False),0)
 def test_reward_bounded(self):
  self.assertEqual(reward_update(3,"VERIFIED_USEFUL",source_verified=True),3)
 def test_reverse_audit(self):
  b=dict(verified_discoveries=1,bytes_sent=1,compute_units=1,unresolved_harms=0,dissent_retained=1)
  a={**b,"verified_discoveries":2,"compute_units":10}
  self.assertTrue(reverse_audit(b,a,{"compute_units":5})["apparent_success_with_drift"])
 def test_no_external_authorization(self):
  r=spores(H,G,{},opted_in=["H01.S01.N02"]);self.assertFalse(r["e145authorization"]);self.assertFalse(r["external_action_executed"])
if __name__=="__main__":unittest.main()
