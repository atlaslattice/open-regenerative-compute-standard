import unittest
from check import validate,STATES

def record():
    return {'claims':[{'id':'sample','subject':'synthetic diesel shipment','scope':'test only','observed_at':'2026-11-22','source_url':'https://example.org/synthetic','states':{k:{'status':'UNKNOWN'} for k in STATES}}]}
class GateTests(unittest.TestCase):
    def test_unknown_is_valid(self):self.assertEqual(validate(record()),[])
    def test_missing_state_rejected(self):
        r=record();del r['claims'][0]['states']['operation'];self.assertTrue(validate(r))
    def test_verified_without_evidence_rejected(self):
        r=record();r['claims'][0]['states']['operation']={'status':'VERIFIED'};self.assertTrue(validate(r))
    def test_verified_with_evidence(self):
        r=record();r['claims'][0]['states']['operation']={'status':'VERIFIED','evidence_ref':'source:1','observation':'meter read'};self.assertEqual(validate(r),[])
    def test_no_unscoped_reserve_days(self):
        r=record();r['claims'][0]['reserve_days']=90;self.assertTrue(validate(r))
    def test_duplicate_ids(self):
        r=record();r['claims'].append(r['claims'][0].copy());self.assertTrue(validate(r))
    def test_missing_provenance(self):
        r=record();r['claims'][0]['source_url']='';self.assertTrue(validate(r))
    def test_empty_claims(self):self.assertEqual(validate({'claims':[]}),[])
if __name__=='__main__':unittest.main()
