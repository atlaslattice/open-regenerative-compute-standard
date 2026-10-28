"""Adjacent textual change receipt, not a semantic or scientific validation."""
import argparse,difflib,hashlib,json,platform
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--source-dir',required=True)
p.add_argument('--out',required=True)
a=p.parse_args()
root=Path(__file__).parent
index=json.loads((root/'SOURCE_INDEX_v0_1.json').read_text())
# The first eight records are the white papers; subsequent entries are supplements.
papers=index['sources'][:8]
def order(x):
    name=Path(x['path']).name
    if 'RF_v0_2' in name: return 2
    for n in range(3,10):
        if f'v0.{n}' in name or f'v0_{n}' in name: return n
    raise ValueError(name)
papers.sort(key=order)
sources=[]
for x in papers:
    b=(Path(a.source_dir)/Path(x['path']).name).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if blob != x['blob_sha']: raise ValueError('source hash mismatch: '+x['path'])
    sources.append((x,b.decode('utf-8').splitlines()))
pairs=[]
for (x,left),(y,right) in zip(sources,sources[1:]):
    ops=difflib.SequenceMatcher(None,left,right,autojunk=False).get_opcodes()
    removed=sum(j-i for tag,i,j,k,l in ops if tag in ('delete','replace'))
    added=sum(l-k for tag,i,j,k,l in ops if tag in ('insert','replace'))
    pairs.append({'from':x['path'],'to':y['path'],'removed_lines':removed,'added_lines':added,
                  'unified_diff':list(difflib.unified_diff(left,right,fromfile=x['path'],tofile=y['path'],lineterm=''))})
out=Path(a.out)
out.mkdir(parents=True,exist_ok=False)
receipt={'status':'TEXT_ACCOUNTING_ONLY','python':platform.python_version(),'source_commit':index['commit'],
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'verified_paper_blobs':8,'unrecovered_whitepaper':'v0.1','pairs':pairs}
(out/'TEXT_DELTAS.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({**{k:v for k,v in receipt.items() if k!='pairs'},'pairs':[{k:v for k,v in x.items() if k!='unified_diff'} for x in pairs]},indent=2))
