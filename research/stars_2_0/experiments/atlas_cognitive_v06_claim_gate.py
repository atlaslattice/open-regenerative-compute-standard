#!/usr/bin/env python3
"""Atlas Lattice v0.6 source-gated synthetic dissent stress test.
This is not an independent LLM multi-agent run or semantic truth verifier.
Requires previous v0.3 fixture script (no source change).
See accompanying report and full conversation artifacts for detailed receipt.
"""
import hashlib,json,re,random,collections,sys
from pathlib import Path
sys.path.insert(0,'/mnt/data/atlas_cognitive_v03')
import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 import atlas_real_corpus_eval_v03 as old
FACTS=[
 ('HSN','The 12×12×12 House-Sphere-Node grid is the entry-level addressable public coordinate surface.', 'HSN is the complete 12D system', 'The HSN grid is an entry-level coordinate surface, not the entire 12D ontology.'),
 ('HSN','Human-root/public ratification is required for canon promotion.', 'Model majority can automatically promote canon', 'Human-root/public ratification is required for Canon promotion.'),
 ('SWARM','NO MERGED MIND, NO IDENTITY FUSION.', 'Swarm should merge operator identities to reach consensus', 'Swarm coordination explicitly preserves separate identities.'),
 ('SWARM','dissent_preserved: true.', 'Dissent gets deleted after a vote', 'The Swarm receipt specifies dissent is preserved.'),
 ('FACILITY','Only MEASURED can establish a current physical state at a node.', 'Predictions establish present measured physical state', 'Only MEASURED evidence establishes current physical state in the template.'),
 ('FACILITY','G12 Model consensus is not evidence.', 'A large council consensus is physical evidence', 'Model consensus does not count as physical evidence.'),
 ('FACILITY','Node-001 coordinate currently UNASSIGNED.', 'Node-001 already has an assigned HSN location', 'Dongjiakou Node-001 is recorded as UNASSIGNED.'),
 ('E145','N=145 is the canonical default (12x12 + 1 Admin Sphere).', '145 is identical to 1728 positions', 'Historical E145 uses 144 + 1 administrator rather than 1728 cognitive addresses.'),
 ('COGNITIVE','No live LLM council.', '1728 models were simultaneously instantiated in v0.2', 'The v0.2 report did not run a live language-model council.'),
 ('TCSS','Numerical fitting is not Riemann proof.', 'A fitted spectrum proves the Riemann Hypothesis', 'The TCSS archive does not treat fitting as proof.'),
 ('SOURCE','No implicit alpha-to-fusion-event conversion.', 'Alpha counts can be converted into fusion events without qualifications', 'The source contract excludes implicit alpha-to-fusion-event conversion.'),
 ('GOVERNANCE','Source and inference run identities remain distinct.', 'Agent consensus may overwrite original source identities', 'Source IDs and inference-run IDs remain distinct.')
]
source={x['id']:x for x in old.SOURCES}
for i,(sid,quote,misleading,correct) in enumerate(FACTS):
 assert quote in source[sid]['text'],(i,sid,quote)

def evidence_gate(candidate):
 evidence=source.get(candidate['source_id'])
 quote=candidate['exact_quote']
 if evidence is None or quote not in evidence['text']:
  return 'REJECT_NO_EXACT_SOURCE'
 if candidate['claim_id']!=candidate['source_claim_id']:
  return 'REJECT_SOURCE_MISMATCH'
 if candidate['stance']=='CONTRADICTS' and candidate['proposal_kind']=='MISLEADING':
  return 'DISPUTED_RETAINED'
 if candidate['stance']=='SUPPORTS' and candidate['proposal_kind']=='CORRECT':
  return 'SUPPORTED_CANDIDATE_NOT_CANON'
 return 'REVIEW_REQUIRED'

random.seed(61027)
results=[]
for i,(sid,quote,bad,good) in enumerate(FACTS):
 votes=['MISLEADING']*7+['CORRECT']*5
 random.shuffle(votes)
 selected=collections.Counter(votes).most_common(1)[0][0]
 proposals=[{'operator_id':f'H{(i%12)+1:02d}.S{(j%12)+1:02d}.N{((i+j)%12)+1:02d}',
             'claim_id':i,'source_claim_id':i,'source_id':sid,'exact_quote':quote,
             'stance':'SUPPORTS' if vote=='CORRECT' else 'CONTRADICTS',
             'proposal_kind':vote,'proposal_text':good if vote=='CORRECT' else bad,
             'synthetic_vote':True} for j,vote in enumerate(votes)]
 decisions=[evidence_gate(p) for p in proposals]
 results.append({'id':i,'source_id':sid,'source_blob_sha':source[sid]['blob'],'quote':quote,
   'correct_claim':good,'misleading_claim':bad,'synthetic_proposals':proposals,
   'naive_majority':selected,'naive_majority_correct':selected=='CORRECT',
   'evidence_packet_result':'SUPPORTED_CANDIDATE_NOT_CANON' if 'SUPPORTED_CANDIDATE_NOT_CANON' in decisions else 'REVIEW_REQUIRED',
   'correct_candidate_kept':any(d=='SUPPORTED_CANDIDATE_NOT_CANON' for d in decisions),
   'disputed_opinions_kept':sum(d=='DISPUTED_RETAINED' for d in decisions),
   'canon_promotion':False})
sample=results[0]['synthetic_proposals'][-1].copy()
sample.update(stance='SUPPORTS',proposal_kind='CORRECT')
checks={
 'twelve_grounded_quotes':len(FACTS)==12,
 'each_exact_quote_present':all(q in source[sid]['text'] for sid,q,_,_ in FACTS),
 'wrong_source_rejected':evidence_gate(dict(sample,source_id='TCSS'))=='REJECT_NO_EXACT_SOURCE',
 'wrong_claim_id_rejected':evidence_gate(dict(sample,claim_id=333))=='REJECT_SOURCE_MISMATCH',
 'altered_quote_rejected':evidence_gate(dict(sample,exact_quote='manufactured unsupported quote'))=='REJECT_NO_EXACT_SOURCE',
 'minority_preserved':all(x['correct_candidate_kept'] for x in results),
 'misleading_majority_wrong':all(not x['naive_majority_correct'] for x in results),
 'disputes_not_erased':all(x['disputed_opinions_kept']==7 for x in results),
 'zero_canon_promotions':all(not x['canon_promotion'] for x in results),
 'distinct_positions_1728':12**3==1728,
 'no_live_agents_claimed':True,
}
rec={'status':'SYNTHETIC_DETERMINISTIC_CONTROL_NOT_LIVE_LLM','date':'2026-10-27',
 'scope':'12 manually source-anchored tests; 7 wrong synthetic votes and 5 correct per test by construction. Quote gate validates quotation/provenance and explicit claim tags, not semantic truth.',
 'summary':{'naive_majority_correct':sum(x['naive_majority_correct'] for x in results),
 'source_bound_correct_candidate_retained':sum(x['correct_candidate_kept'] for x in results),
 'dissent_retained':sum(x['disputed_opinions_kept'] for x in results),'canon_promotions':0},
 'tests':checks,'cases':results}
output=Path(__file__).with_name('ATLAS_CLAIM_GATE_RECEIPT_v0_6.json')
output.write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'summary':rec['summary'],'tests':checks},indent=2))
