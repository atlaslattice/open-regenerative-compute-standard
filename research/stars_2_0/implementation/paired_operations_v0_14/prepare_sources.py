"""Recover only the pinned public ZIP members required by this benchmark."""
import argparse,hashlib,json
from pathlib import Path
from archive_member import recover_member,recover_block

def prepare(out):
    root=Path(__file__).parent;out=Path(out);out.mkdir(parents=True,exist_ok=True)
    lock=json.loads((root/'SOURCE_LOCK.json').read_text())
    for key,name in [('notebook','low_div_stability_figure.ipynb'),('secondary','ProtonSpatial_secondary.pkl')]:
        meta=lock[key];p=out/name
        if not p.exists():
            result=recover_member(meta,p)
            Path(str(p)+'.receipt.json').write_text(json.dumps(result,indent=2)+'\n')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=meta['sha256']:raise ValueError('Source member mismatch')
        receipt=Path(str(p)+'.receipt.json')
        if not receipt.exists():receipt.write_text(json.dumps(meta,indent=2)+'\n')
    fits=out/'beam_fits';metas=lock['beam_fits']['members']
    if not all((fits/Path(m['name']).name).exists() for m in metas):recover_block(metas,fits)
    for m in metas:
        if hashlib.sha256((fits/Path(m['name']).name).read_bytes()).hexdigest()!=m['sha256']:raise ValueError('Beam member mismatch')
    if not (fits/'MEMBER_RECEIPTS.json').exists():(fits/'MEMBER_RECEIPTS.json').write_text(json.dumps(lock['beam_fits'],indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',default='sources');a=p.parse_args();prepare(a.out)
