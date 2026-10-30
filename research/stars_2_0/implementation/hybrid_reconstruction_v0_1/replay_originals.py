#!/usr/bin/env python3
"""Replay byte-preserved historical scripts. Never overwrite the sources or an old run.
A temporary /mnt/data symlink is required by original hard-coded output paths.
"""
from pathlib import Path
import argparse, csv, hashlib, importlib.metadata, json, math, os, platform, shutil, subprocess, sys
ROOT=Path(__file__).resolve().parent
JOBS=[('mirror','prism_sphere_reduced_model.py'),('mirror','stars_prism_three_module_toy_2026-10-29.py'),('mirror','stars_525mw_gain_scenarios_2026-10-29.py'),('acoustic_v06','run_benchmark.py'),('acoustic_v07','run_spherical.py'),('acoustic_v08','run_phase_benchmark.py'),('acoustic_v10','run.py'),('acoustic_v11','run.py'),('acoustic_v12','run_v012.py')]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def csv_compare(expected,actual):
    with expected.open(newline='') as f: a=list(csv.reader(f))
    with actual.open(newline='') as f: b=list(csv.reader(f))
    result={'expected_rows_including_header':len(a),'actual_rows_including_header':len(b),'nonnumeric_mismatches':0,'max_abs_numeric_difference':0.,'max_scaled_numeric_difference':0.}
    if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)):
        return dict(result,shape_match=False,numeric_match=False)
    for x,y in zip(a,b):
        for u,v in zip(x,y):
            if u==v: continue
            try:
                uf,vf=float(u),float(v)
                if math.isnan(uf) and math.isnan(vf):continue
                if not (math.isfinite(uf) and math.isfinite(vf)):
                    result['nonnumeric_mismatches']+=1;continue
                err=abs(uf-vf);scaled=err/max(1.,abs(uf))
                result['max_abs_numeric_difference']=max(result['max_abs_numeric_difference'],err)
                result['max_scaled_numeric_difference']=max(result['max_scaled_numeric_difference'],scaled)
            except ValueError: result['nonnumeric_mismatches']+=1
    return dict(result,shape_match=True,numeric_match=result['nonnumeric_mismatches']==0 and result['max_scaled_numeric_difference']<1e-12)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=False)
    alias=Path('/mnt/data')
    if os.path.lexists(alias):raise SystemExit('Refusing existing /mnt/data; run in a clean container. No original script is rewritten.')
    alias.parent.mkdir(parents=True,exist_ok=True)
    alias.symlink_to(out,target_is_directory=True)
    records=[]
    try:
        for group in {g for g,_ in JOBS}:
            stage=out/('stars2_duration_success_v011' if group=='acoustic_v11' else group);stage.mkdir()
            for source in (ROOT/'sources'/group).glob('*.py'):shutil.copyfile(source,stage/source.name)
        # Use the recovered original prerequisite, not this replay's v0.11 output.
        prerequisite=ROOT/'sources/acoustic_v11/duration_sweep.csv'
        for group,name in JOBS:
            stage=out/('stars2_duration_success_v011' if group=='acoustic_v11' else group)
            if group=='acoustic_v12':shutil.copyfile(prerequisite,out/'stars2_duration_success_v011/duration_sweep.csv')
            if name=='stars_525mw_gain_scenarios_2026-10-29.py':shutil.copyfile(out/'stars_prism_three_module_toy_2026-10-29.csv',stage/'stars_prism_three_module_toy_2026-10-29.csv')
            original=ROOT/'sources'/group/name; script=stage/name
            if sha(original)!=sha(script):raise AssertionError('Staged source changed')
            result=subprocess.run([sys.executable,str(script)],cwd=stage,capture_output=True,text=True)
            if group=='acoustic_v11' and (stage/'duration_sweep.csv').exists():shutil.copyfile(stage/'duration_sweep.csv',out/'v011_generated_duration_sweep.csv')
            (out/(group+'_'+name+'.stdout.txt')).write_text(result.stdout)
            (out/(group+'_'+name+'.stderr.txt')).write_text(result.stderr)
            records.append({'group':group,'script':name,'source_sha256':sha(original),'returncode':result.returncode,'command':[sys.executable,str(script)],'random_seed':20261028 if group in ('acoustic_v08','acoustic_v10') else None})
        comparisons=[]
        golden=json.loads((ROOT/'GOLDEN_CSV_HASHES.json').read_text())
        for rel,digest in golden.items():
            group,name=rel.split('/',1)
            target=(out/name if group=='mirror' and name!='stars_525mw_gain_scenarios_2026-10-29.csv' else out/('stars2_duration_success_v012' if group=='acoustic_v12' else 'stars2_duration_success_v011' if group=='acoustic_v11' else group)/name)
            # v0.11's generated output was replaced above by its original prerequisite: compare its pre-replacement snapshot.
            if group=='acoustic_v11':target=out/'v011_generated_duration_sweep.csv'
            row={'source':rel,'expected_sha256':digest,'actual_sha256':sha(target) if target.exists() else None,'byte_identical':target.exists() and sha(target)==digest}
            expected=ROOT/'sources'/rel
            if target.exists() and expected.exists():row.update(csv_compare(expected,target))
            comparisons.append(row)
        receipt={'python':platform.python_version(),'platform':platform.platform(),'dependencies':{n:importlib.metadata.version(n) for n in ('numpy','pandas','scipy','matplotlib')},'original_environment':'Not recovered; this is the reconstruction environment, not a claim of original software-version identity.','filesystem_adaptation':'/mnt/data symlink to fresh run directory; sources unchanged','runs':records,'csv_comparisons':comparisons}
        (out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    finally:
        if alias.is_symlink() and alias.resolve()==out:alias.unlink()
    print(json.dumps({'runs':len(records),'successful_runs':sum(r['returncode']==0 for r in records),'csvs':len(comparisons),'byte_identical_csvs':sum(r['byte_identical'] for r in comparisons),'receipt':str(out/'REPLAY_RECEIPT.json')},indent=2))
    if any(r['returncode'] for r in records) or any(not r['byte_identical'] for r in comparisons):raise SystemExit(1)
if __name__=='__main__': main()
