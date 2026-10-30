"""Recover selected members of the public Zenodo ZIP, without executing them."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import urllib.request
import zlib

URL='https://zenodo.org/api/records/14236097/files/LowDivergenceProtons_paper_data.zip/content'

def recover_member(meta,out):
    out=Path(out)
    # Local header plus exact filename length; no ZIP64 members selected here.
    start=meta['offset'];end=start+30+len(meta['name'].encode())+4096+meta['compressed_size']-1
    req=urllib.request.Request(URL,headers={'Range':f'bytes={start}-{end}','User-Agent':'StellarForgeResearch/0.14'})
    with urllib.request.urlopen(req,timeout=45) as r:
        if r.status!=206 or not r.headers.get('Content-Range','').startswith(f'bytes {start}-'):raise ValueError('Wrong HTTP range')
        data=r.read(end-start+2)
    h=struct.unpack_from('<4s5H3I2H',data)
    if h[0]!=b'PK\x03\x04' or h[3]!=meta['method']:raise ValueError('ZIP header mismatch')
    name=data[30:30+h[9]].decode()
    if name!=meta['name']:raise ValueError('Wrong archive member')
    offset=30+h[9]+h[10]
    packed=data[offset:offset+meta['compressed_size']]
    raw=zlib.decompress(packed,-15) if meta['method']==8 else packed
    if len(raw)!=meta['size'] or zlib.crc32(raw)!=meta['crc']:raise ValueError('ZIP member CRC/length mismatch')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(raw)
    return dict(**meta,sha256=hashlib.sha256(raw).hexdigest(),url=URL,
                member_crc_verified=True,full_archive_md5_verified=False)

def recover_block(selection,out):
    """One HTTP range for nearby beam-fit members; never extract arbitrary paths."""
    start=min(m['offset'] for m in selection)
    end=max(m['offset']+30+len(m['name'].encode())+m['compressed_size']+4096 for m in selection)
    req=urllib.request.Request(URL,headers={'Range':f'bytes={start}-{end}','User-Agent':'StellarForgeResearch/0.14'})
    with urllib.request.urlopen(req,timeout=45) as r:
        if r.status!=206 or not r.headers.get('Content-Range','').startswith(f'bytes {start}-'):raise ValueError('Wrong HTTP range')
        data=r.read(end-start+2)
    out=Path(out);out.mkdir(parents=True,exist_ok=True);receipts=[]
    for m in selection:
        loc=m['offset']-start;h=struct.unpack_from('<4s5H3I2H',data,loc)
        name=data[loc+30:loc+30+h[9]].decode()
        if h[0]!=b'PK\x03\x04' or name!=m['name'] or h[3]!=8:raise ValueError('Wrong member')
        off=loc+30+h[9]+h[10]
        raw=zlib.decompress(data[off:off+m['compressed_size']],-15)
        if len(raw)!=m['size'] or zlib.crc32(raw)!=m['crc']:raise ValueError('Bad member CRC')
        target=out/Path(name).name;target.write_bytes(raw)
        receipts.append(dict(**m,sha256=hashlib.sha256(raw).hexdigest(),member_crc_verified=True))
    (out/'MEMBER_RECEIPTS.json').write_text(json.dumps(dict(url=URL,full_archive_md5_verified=False,members=receipts),indent=2)+'\n')
    return receipts

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('inventory');p.add_argument('name');p.add_argument('out');a=p.parse_args()
    meta=next(f for f in json.loads(Path(a.inventory).read_text()) if f['name']==a.name)
    result=recover_member(meta,a.out);Path(a.out+'.receipt.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
