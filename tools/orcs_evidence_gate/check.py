"""Offline ORCS evidence gate. A PASS validates ledger consistency, not physical claims."""
import json, sys
from pathlib import Path

STATES = ('authority','funding','construction','commissioning','operation','measured_output','delivered_benefit')
VALUES = {'UNKNOWN','NOT_APPLICABLE','PROPOSED','DOCUMENTED','VERIFIED'}

def _unique_pairs(pairs):
    """Reject overwritten JSON fields at any nesting depth."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result

def loads_strict(text):
    """Reject ambiguous duplicate keys and nonstandard nonfinite JSON values."""
    return json.loads(text, object_pairs_hook=_unique_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(
                          ValueError(f'nonfinite JSON constant: {value}')))

def validate(data):
    errors=[]
    if not isinstance(data,dict) or not isinstance(data.get('claims'),list):
        return ['claims must be a list']
    ids=set()
    for n,claim in enumerate(data['claims']):
        p=f'claims[{n}]'
        if not isinstance(claim,dict): errors.append(f'{p}: object required');continue
        cid=claim.get('id')
        if not isinstance(cid,str) or not cid.strip():
            errors.append(f'{p}: unique nonempty id required')
        elif cid in ids:
            errors.append(f'{p}: unique nonempty id required')
        else:
            ids.add(cid)
        for key in ('subject','scope','observed_at','source_url'):
            if not isinstance(claim.get(key),str) or not claim[key].strip(): errors.append(f'{p}: missing {key}')
        states=claim.get('states')
        if not isinstance(states,dict):errors.append(f'{p}: states object required');continue
        for key in STATES:
            s=states.get(key)
            if not isinstance(s,dict) or not isinstance(s.get('status'),str) or s['status'] not in VALUES: errors.append(f'{p}: invalid {key} state');continue
            if s['status']=='VERIFIED' and any(
                not isinstance(s.get(field), str) or not s[field].strip()
                for field in ('evidence_ref', 'observation')
            ):
                errors.append(f'{p}: VERIFIED {key} requires evidence_ref and observation')
        if claim.get('reserve_days') is not None:
            errors.append(f'{p}: reserve_days must be derived in a separate region/product-specific calculation')
    return errors

def main():
    if len(sys.argv)!=2:print('usage: python check.py ledger.json',file=sys.stderr);return 2
    try: data=loads_strict(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError,ValueError) as e: print(f'INVALID INPUT: {e}',file=sys.stderr);return 2
    errors=validate(data)
    print(json.dumps({'status':'PASS_LEDGER_SCHEMA_ONLY' if not errors else 'FAIL','claim_count':len(data['claims']) if isinstance(data,dict) and isinstance(data.get('claims'),list) else None,'errors':errors},indent=2))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
