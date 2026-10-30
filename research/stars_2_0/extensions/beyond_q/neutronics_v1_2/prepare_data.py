"""Download official evaluated ACE data and convert to OpenMC HDF5.

Records every source/converted hash. No invented cross sections, NJOY run,
temperature broadening or unreported library substitution. Data cache lives
outside source tree. Conversion requires installed OpenMC Python API/h5py.
"""
import argparse,hashlib,json,time,urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--download-only',action='store_true');args=ap.parse_args()
    cfg=json.loads((ROOT/'inputs/nuclear_data_sources.json').read_text())
    args.cache.mkdir(parents=True,exist_ok=True)
    def get(name):
        path=args.cache/name;url=cfg['base_url']+name
        if not path.exists():
            for attempt in range(3):
                try:
                    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
                    with urllib.request.urlopen(req,timeout=60) as r:raw=r.read()
                    if len(raw)<1000 or b'<html' in raw[:300].lower():raise ValueError('not ACE nuclear data')
                    path.write_bytes(raw);break
                except Exception:
                    if attempt==2:raise
                    time.sleep(1)
        return dict(file=name,url=url,bytes=path.stat().st_size,ace_sha256=sha(path),
                    header=path.open().readline().strip())
    with ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(get,cfg['files']))
    lock=ROOT/'outputs/nuclear_data_manifest.json'
    if lock.exists():
        expected={r['file']:r['ace_sha256'] for r in json.loads(lock.read_text())['files']}
        if any(expected.get(r['file'])!=r['ace_sha256'] for r in records):
            raise ValueError('Official ACE bytes differ from the published lock; review before accepting a new library')
    manifest=dict(library=cfg['library'],official_index=cfg['official_index'],
        processed_repository_commit=cfg['processed_repository_commit'],temperature_K=cfg['temperature_K'],files=records)
    (args.cache/'ace_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('Downloaded/verified',len(records),'ACE files',flush=True)
    if args.download_only:return
    import openmc,openmc.data,h5py
    converted=args.cache/'hdf5';converted.mkdir(exist_ok=True)
    library=openmc.data.DataLibrary()
    for rec in records:
        data=openmc.data.IncidentNeutron.from_ace(args.cache/rec['file'])
        path=converted/(data.name+'.h5')
        if path.exists():
            try:
                with h5py.File(path,'r') as h:pass
            except OSError:
                rec['replaced_invalid_cache_sha256']=sha(path);path.unlink()
        if not path.exists():data.export_to_hdf5(path)
        library.register_file(path)
        rec.update(nuclide=data.name,hdf5_file=path.name,hdf5_sha256=sha(path),
                   temperatures=list(data.temperatures),reaction_MTs=sorted(int(x) for x in data.reactions))
    library.export_to_xml(converted/'cross_sections.xml')
    manifest.update(openmc_version=openmc.__version__,cross_sections_sha256=sha(converted/'cross_sections.xml'))
    (converted/'data_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(converted/'cross_sections.xml')

if __name__=='__main__':main()
