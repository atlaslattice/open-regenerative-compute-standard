"""Acquire hash-pinned upstream C tables; extract exact C float values without a compiler."""
import argparse,hashlib,json,re,struct,subprocess,ctypes
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parent

def numbers(s):
    tokens=re.findall(r'[-+]?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?f',s)
    return [struct.unpack('f',struct.pack('f',float(t[:-1])))[0] for t in tokens]

def extract(folder):
    folder=Path(folder);lock=json.loads((ROOT/'UPSTREAM_LOCK.json').read_text())
    for r in lock['files']:
        if hashlib.sha256((folder/r['path']).read_bytes()).hexdigest()!=r['sha256']:
            raise ValueError('upstream source identity mismatch: '+r['path'])
    energy=numbers((folder/'src/generated/erg.c').read_text())
    if len(energy)!=121 or energy[0]!=1 or energy[-1]!=1e6:raise ValueError('energy grid changed')
    out=[]
    for model in ['srim96','srim13']:
        for z in [1,2]:
            text=(folder/f'src/generated/{model}/Z{z:02d}.c').read_text()
            groups=re.findall(r'\{([^{}]*)\}',text)
            if len(groups)!=93 or numbers(groups[0]):raise ValueError('target indexing changed')
            for target in [5,7]:
                values=numbers(groups[target])
                if len(values)!=121 or min(values)<=0:raise ValueError('stopping values invalid')
                out.append(dict(model=model,projectile_Z=z,target_Z=target,energy_keV_u=energy,
                    electronic_stopping_in_1e_minus15_eV_cm2_atom=values))
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--download',action='store_true');p.add_argument('--native-check',action='store_true');a=p.parse_args()
    if a.out.exists():raise FileExistsError('output exists')
    lock=json.loads((ROOT/'UPSTREAM_LOCK.json').read_text())
    if a.download:
        for r in lock['files']:
            path=a.upstream/r['path']
            if path.exists():continue
            u=f"https://raw.githubusercontent.com/{lock['repository']}/{lock['commit']}/{r['path']}"
            raw=urllib.request.urlopen(u,timeout=30).read()
            if hashlib.sha256(raw).hexdigest()!=r['sha256']:raise ValueError('download mismatch')
            path.parent.mkdir(parents=True,exist_ok=True)
            with path.open('xb') as f:f.write(raw)
    rows=extract(a.upstream);a.out.mkdir(parents=True,exist_ok=False)
    for r in rows:
        (a.out/f"{r['model']}_Z{r['projectile_Z']}_T{r['target_Z']}.json").write_text(json.dumps(r,indent=2)+'\n')
    if a.native_check:
        sources=[a.upstream/f'src/generated/{m}/Z{z:02d}.c' for m in ['srim96','srim13'] for z in [1,2]]+[a.upstream/'src/generated/erg.c']
        libpath=a.out/'libselected.so'
        cmd=['cc','-shared','-fPIC',*[str(s) for s in sources],'-o',str(libpath)]
        subprocess.run(cmd,check=True)
        lib=ctypes.CDLL(str(libpath.resolve()));energy=list((ctypes.c_float*121).in_dll(lib,'erg'))
        for r in rows:
            array=((ctypes.c_float*121)*93).in_dll(lib,f"{r['model']}_Z{r['projectile_Z']:02d}_")
            if list(array[r['target_Z']])!=r['electronic_stopping_in_1e_minus15_eV_cm2_atom'] or energy!=r['energy_keV_u']:
                raise ValueError('C-native comparison failed')
        receipt=dict(native_stopping_nodes_exact=968,native_energy_nodes_exact=121,
            compiler_command=cmd,compiler_version=subprocess.run(['cc','--version'],capture_output=True,text=True).stdout.splitlines()[0],
            interpretation='C table replay only; SRIM original executables not regenerated')
        (a.out/'NATIVE_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'tables':len(rows),'selected_stopping_nodes':sum(len(r['energy_keV_u']) for r in rows)}))

if __name__=='__main__':main()
