#!/usr/bin/env python3
"""Atlas Intelligence Canon 2.0 candidate governance adapter (not official Canon).
Requires historic merged v0.2 JSON in parent directory. Pure decision function.
No external action, agent spawning, Canon mutation, or semantic truth verification.
"""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
MERGE_NAME='ATLAS_CANON_MERGED_RESURRECTION_CANDIDATE_v0_2_2026-10-27.json'
EXPECTED_GIT_BLOB='b2b42813ebdd98dbe6ed47036193d8bfb82be623'
APPLICABLE={
 'research':('ALC-001','ALC-002','ALC-003','ALC-008','ALC-010','ALC-011'),
 'council_debate':('ALC-001','ALC-002','ALC-003','ALC-006','ALC-009'),
 'canon_promotion':('ALC-001','ALC-002','ALC-003','ALC-007','ALC-009'),
 'deployment':('ALC-001','ALC-003','ALC-004','ALC-005','ALC-006','ALC-007','ALC-008','ALC-009','ALC-010','ALC-011','ALC-012'),
 'external_action':('ALC-001','ALC-003','ALC-005','ALC-006','ALC-009','ALC-010')}
CONFLICTS={
 'CON-01':{'topic':'provider_cap','families':['ALC-006'],'reason':'Provider-cap percentages differ between historical registries.'},
 'CON-02':{'topic':'amendment_threshold','families':['ALC-007','ALC-009'],'reason':'Amendment thresholds and quorum/tie-break rules differ.'},
 'CON-03':{'topic':'ontology_mapping','families':['ALC-011'],'reason':'Legacy 144-sphere vs 1728 cognitive slot mapping requires explicit review.'},
 'CON-04':{'topic':'jurisdiction','families':['ALC-005'],'reason':'Dialect, residency and consent scope remains jurisdiction dependent.'},
 'CON-05':{'topic':'ratification_provenance','families':['ALC-001','ALC-007'],'reason':'Source-claimed ratification has no independently verified signed authority packet.'}}
ADDR=re.compile('^H(?:0[1-9]|1[0-2])[.]S(?:0[1-9]|1[0-2])[.]N(?:0[1-9]|1[0-2])$')

def load_registry(path=None):
 path=Path(path) if path else ROOT/MERGE_NAME
 raw=path.read_bytes()
 blob=hashlib.sha1(('blob '+str(len(raw))+chr(0)).encode()+raw).hexdigest()
 if blob!=EXPECTED_GIT_BLOB: raise ValueError('FAIL_CLOSED_REGISTRY_BLOB_MISMATCH')
 doc=json.loads(raw);groups=doc['groups'];ids=[g['alias'] for g in groups]
 if len(ids)!=12 or len(set(ids))!=12 or doc.get('status')!='CANDIDATE_NON_CANON':
  raise ValueError('FAIL_CLOSED_INVALID_REGISTRY')
 for g in groups:
  if not g.get('sources') or g.get('status')!='MERGE_PROPOSAL_NOT_RATIFIED':
   raise ValueError('FAIL_CLOSED_UNTRACEABLE_OR_OVERCLAIMED_RULE')
 return {'git_blob':blob,'sha256':hashlib.sha256(raw).hexdigest()}

def decide(request,source):
 op=request.get('operation')
 if op not in APPLICABLE:return packet(request,source,'DENY','UNSUPPORTED_OPERATION',[],[])
 applied=list(APPLICABLE[op]);review=[];fail=[]
 research=op in ('research','council_debate')
 if not isinstance(request.get('operator'),str) or not ADDR.fullmatch(request['operator']):
  fail.append('INVALID_HSN_ADDRESS')
 receipts=request.get('source_receipts')
 if not isinstance(receipts,list) or not receipts or not all(isinstance(x,dict) and x.get('source') and x.get('sha256') for x in receipts):
  fail.append('MISSING_SOURCE_RECEIPT')
 if request.get('claim_status')=='CANON' and not request.get('human_ratification_receipt'):
  fail.append('UNAUTHORIZED_CANON_CLAIM')
 if research:
  if request.get('simulation') is not True or request.get('external_effect') is True:
   fail.append('RESEARCH_MUST_BE_ISOLATED_SIMULATION')
 else:
  if request.get('human_authorized') is not True or not request.get('human_authorization_receipt'):
   fail.append('MISSING_HUMAN_AUTHORIZATION')
  if op=='canon_promotion' and not request.get('human_ratification_receipt'):
   fail.append('MISSING_RATIFICATION_RECEIPT')
  if request.get('simulation') is True and op in ('deployment','external_action'):
   fail.append('SIMULATION_CANNOT_AUTHORIZE_REAL_ACTION')
  for cid,c in CONFLICTS.items():
   if set(c['families'])&set(applied):review.append(cid)
 if fail:status='DENY';reason='HARD_GATE_FAILURE'
 elif review:status='REVIEW_REQUIRED';reason='UNRESOLVED_CONSTITUTIONAL_CONFLICT'
 else:status='ALLOW_SIMULATION_ONLY';reason='STRUCTURAL_SIMULATION_GATES_PASSED_NOT_TRUTH_VERIFIED'
 return packet(request,source,status,reason,applied,review,fail)

def packet(request,source,status,reason,applied,review,fail=None):
 fp=hashlib.sha256(json.dumps(request,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 return {'version':'canon2-operator-v0.2','status':status,'reason':reason,
  'request_sha256':fp,'registry_git_blob':source['git_blob'],
  'registry_sha256':source['sha256'],'applied_candidate_families':applied,
  'conflict_ids':review,'conflict_details':{k:CONFLICTS[k] for k in review},
  'failures':fail or [],'canon_promoted':False,'action_executed':False,
  'semantic_truth_verified':False,'historical_canon_amended':False}

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('request_json');p.add_argument('--registry',default=None)
 a=p.parse_args();src=load_registry(a.registry)
 print(json.dumps(decide(json.loads(Path(a.request_json).read_text()),src),indent=2,ensure_ascii=False))
if __name__=='__main__':main()
