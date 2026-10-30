#!/usr/bin/env python3
from pathlib import Path
import argparse,csv,hashlib,json,math,platform,subprocess
from fit_candidate import sigma_cm_m2,stationary_boron_lab_to_cm_keV
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    # Compile original WarpX formulas/constants; shims only supply CPU/double aliases and integer powers.
    command=['g++','-std=c++20','-O2','-I'+str(ROOT/'harness_include'),'-I'+str(ROOT/'vendor/Source'),str(ROOT/'kernel_probe.cpp'),'-o',str((a.out/'kernel_probe').resolve())]
    compiled=subprocess.run(command,capture_output=True,text=True)
    (a.out/'COMPILE.txt').write_text(compiled.stdout+compiled.stderr)
    if compiled.returncode:raise RuntimeError('Kernel harness compilation failed')
    grid=[0.]+[10**(-1+i*5/300) for i in range(301)]+[147.9,148.,148.1,399.999999,400.,400.000001,667.999999,668.,668.000001,9759.999999,9760.,9760.000001,50000.]
    native=subprocess.run([str((a.out/'kernel_probe').resolve())],input='\n'.join(map(str,grid))+'\n',capture_output=True,text=True,check=True)
    lines=[list(map(float,l.split())) for l in native.stdout.splitlines()]
    assert len(lines)==len(grid)
    errs=[]
    for requested,(e,x) in zip(grid,lines):
        y=sigma_cm_m2(e,allow_buck_tail=True)
        assert math.isfinite(x) and x>=0
        if x or y:
            err=abs(x-y)/max(abs(x),abs(y));assert err<1e-12,(e,x,y,err);errs.append(err)
        else:assert x==y==0
    guards=0
    for invalid in [-1,True,float('nan'),float('inf')]:
        for fn in [sigma_cm_m2,stationary_boron_lab_to_cm_keV]:
            try:fn(invalid)
            except ValueError:guards+=1
            else:raise AssertionError('Invalid input accepted')
    try:sigma_cm_m2(50000)
    except ValueError:guards+=1
    else:raise AssertionError('High-energy tail silently admitted')
    rows=[]
    for e in [150.,160.,161.5,162.,164.,180.,200.,220.,600.,675.,1000.,3800.]:
        cm=stationary_boron_lab_to_cm_keV(e)
        rows.append({'proton_LAB_keV_stationary_B11':e,'pair_CM_kinetic_keV':cm,'candidate_sigma_event_barn':sigma_cm_m2(cm)/1e-28,'evidence':'SOURCE_CODE_REPRODUCED_PUBLICATION_FIT_NOT_APPARATUS_CALIBRATION'})
    with (a.out/'LAB_TO_CM_CANDIDATE.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    low_grid=[140+i*.01 for i in range(1601)];peak=max(low_grid,key=sigma_cm_m2)
    report={'status':'SCALAR_KERNEL_AUDIT_ONLY_NOT_WARPX_PIC_RUN','python':platform.python_version(),'compiler':subprocess.run(['g++','--version'],capture_output=True,text=True).stdout.splitlines()[0],'compile_command':command,'native_cpp_comparison_points':len(grid),'maximum_relative_difference':max(errs),'input_guard_cases_passed':guards,'low_resonance_grid_peak_CM_keV':peak,'low_resonance_grid_peak_sigma_barn':sigma_cm_m2(peak)/1e-28,'source_commit':'a389dc54a27136176bdd48f7bfd36da62a873a61','code_hashes':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in list((ROOT/'vendor').rglob('*.H'))+list((ROOT/'harness_include').glob('*.H'))+[ROOT/'kernel_probe.cpp',ROOT/'fit_candidate.py',ROOT/'run_kernel_audit.py']},'physical_fit_uncertainty':'Not recovered or propagated in this audit','full_pic_simulation_executed':False,'stellar_forge_reference_replaced':False}
    (a.out/'RECEIPT.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('code_hashes','compile_command')},indent=2))
if __name__=='__main__':main()
