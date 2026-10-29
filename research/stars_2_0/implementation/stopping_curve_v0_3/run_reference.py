"""Offline reference run and explicit stopping sensitivity cases, not calibration fitting."""
import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys

from transport_interval import load_curve,transmit,MATERIAL

ROOT=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('output already exists')
    curve=load_curve(ROOT/'CURVE.json');points=curve['points']
    result=subprocess.run([sys.executable,'-m','unittest','-v','test_transport'],cwd=ROOT,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stdout+result.stderr)
    reference=[transmit(points,E_in_LAB_MeV=.65,atoms_cm2=n,material=MATERIAL) for n in [0,1e17,1e18,1e19,1e24]]
    sensitivities=[]
    # Coherent source scale and digitization offsets, not independent point noise.
    for scale,offset,energy_shift in itertools.product([.96,1.04],[-.08e-15,.08e-15],[-.008,.008]):
        changed=copy.deepcopy(points)
        for r in changed:
            r['epsilon_eV_cm2_atom']=r['epsilon_eV_cm2_atom']*scale+offset
            r['E_proton_LAB_MeV']+=energy_shift
        sensitivities.append(dict(source_stopping_scale=scale,digitization_stopping_offset_eV_cm2_atom=offset,
            digitization_energy_axis_shift_MeV=energy_shift,
            result=transmit(changed,E_in_LAB_MeV=.65,atoms_cm2=1e18,material=MATERIAL)))
    receipt=dict(python=platform.python_version(),tests='10 PASS',seed=None,randomness='none',
        source_status='PRIMARY_FIGURE_DIGITIZED_AND_ANCHOR_CHECKED',
        interpolation_status='EXPLICIT_NUMERICAL_MODEL',apparatus_transmission_validation='NOT_RUN',
        material=MATERIAL,curve_points=len(points),source_observable='measured energy-loss atomic stopping; no recovered Se/Sn separation',
        sensitivity_interpretation='eight coherent stress scenarios, NOT a confidence interval; source probable-error convention is not Gaussian 1-sigma',
        imposed_atom_columns='assumed verification inputs, not a proposed target specification',
        alpha_stopping='FULL_NUMERIC_DATA_NOT_RECOVERED',fusion_yield='NOT_COMPUTED',
        code_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.glob('*.py')})
    a.out.mkdir(parents=True,exist_ok=False)
    outputs={'REFERENCE.json':reference,'SENSITIVITIES.json':sensitivities,'RECEIPT.json':receipt}
    for name,data in outputs.items():(a.out/name).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    (a.out/'TEST_LOG.txt').write_text(result.stdout+result.stderr)
    (a.out/'MANIFEST.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in a.out.iterdir()},indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
