"""Read-only public feed snapshotter; no scheduler or live dashboard."""
import hashlib
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent

def validate(feed, value):
    kind=feed.get('format')
    if kind=='array':
        return isinstance(value,list)
    if kind=='geojson':
        return isinstance(value,dict) and value.get('type')=='FeatureCollection' and isinstance(value.get('features'),list)
    if kind=='nws_point':
        return isinstance(value,dict) and isinstance(value.get('properties'),dict)
    if kind=='fema':
        return isinstance(value,dict) and isinstance(value.get('DisasterDeclarationsSummaries'),list)
    raise ValueError('Unknown parser type')

def collect_one(feed, timeout=8):
    if not feed.get('url') or not feed.get('access','').startswith('public'):
        return {'id':feed['id'],'status':'NOT_FETCHED_ACCESS_REVIEW'}
    req=urllib.request.Request(feed['url'],headers={'User-Agent':'ORCS-research-snapshot/0.3 (nonoperational)'})
    try:
        with urllib.request.urlopen(req,timeout=timeout) as response:
            raw=response.read(4_000_001)
            if len(raw)>4_000_000:
                return {'id':feed['id'],'status':'REJECTED_TOO_LARGE'}
            parsed=json.loads(raw.decode('utf8'))
            if not validate(feed,parsed):
                return {'id':feed['id'],'status':'REJECTED_SCHEMA'}
            return {'id':feed['id'],'status':'FETCHED_JSON_SNAPSHOT','sha256':hashlib.sha256(raw).hexdigest(),
                    'bytes':len(raw),'retrieved_utc':datetime.now(timezone.utc).isoformat(),'sample':parsed}
    except (OSError,ValueError,UnicodeError,json.JSONDecodeError) as exc:
        return {'id':feed['id'],'status':'FETCH_FAILED','error_type':type(exc).__name__}

def main():
    feeds=json.loads((HERE/'sources.json').read_text())['feeds']
    receipts=[]
    target=HERE/'snapshots';target.mkdir(exist_ok=True)
    for feed in feeds:
        response=collect_one(feed)
        payload=response.pop('sample',None)
        if payload is not None:
            (target/(feed['id']+'.json')).write_text(json.dumps(payload,indent=2))
        receipts.append(response)
    (target/'fetch_receipt.json').write_text(json.dumps(receipts,indent=2))
    print(json.dumps({'receipt':str(target/'fetch_receipt.json'),'counts':{s:sum(r['status']==s for r in receipts) for s in set(r['status'] for r in receipts)}},indent=2))

if __name__=='__main__':
    main()
