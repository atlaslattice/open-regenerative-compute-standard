import unittest
from spore_hypothesis_exchange_v0_2 import Spore,invitational_propagate
S=Spore("H01.S01.N01","Moss can inspire caching",("source:abc",),"tentative",ttl=2,budget=2)
G={"H01.S01.N01":["H01.S01.N02","H01.S01.N03"],"H01.S01.N02":["H02.S01.N01"]}
class Tests(unittest.TestCase):
 def test_bounded(self):self.assertLessEqual(len(invitational_propagate(S,G,{})["invited"]),2)
 def test_blocked(self):self.assertNotIn("H01.S01.N03",invitational_propagate(S,G,{},{"H01.S01.N03"})["invited"])
 def test_zero_ttl(self):self.assertEqual(invitational_propagate(Spore("H01.S01.N01","x",("s",),"u",ttl=0),G,{})["invited"],[])
 def test_no_source(self):
  with self.assertRaises(ValueError):Spore("H01.S01.N01","x",(),"u").validate()
 def test_no_canon_spoof(self):
  with self.assertRaises(ValueError):Spore("H01.S01.N01","x",("s",),"u",kind="CANON").validate()
 def test_no_external_action(self):self.assertFalse(invitational_propagate(S,G,{})["external_action_executed"])
 def test_no_e145_authorization(self):self.assertFalse(invitational_propagate(S,G,{})["e145authorization"])
 def test_no_promotion(self):self.assertFalse(invitational_propagate(S,G,{})["canon_promoted"])
 def test_determinism(self):self.assertEqual(invitational_propagate(S,G,{}),invitational_propagate(S,G,{}))
if __name__=="__main__":unittest.main()
