"""Execute exact recovered source and independently audit its declared physical observables."""
import argparse,csv,hashlib,importlib.util,json,math,platform,subprocess,sys
from pathlib import Path
import numpy,scipy
from calibrate import check_dependencies

ROOT=Path(__file__).resolve().parent
EXPECTED='2db27298ea7f11c24cf891b4b784a5e21a8417c0207a3089f51bd037c44e522e'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'
def csv_rows(p):
    with p.open(newline='') as f:return list(csv.DictReader(f))

def inspect_outputs(out):
    check_dependencies()
    source=ROOT/'original/stars_v04_original_extracted.py'
    if sha(source)!=EXPECTED:raise ValueError('original source identity mismatch')
    # Import mass-correct reference without changing the archived generator.
    spec=importlib.util.spec_from_file_location('reference_mass_kinematics',ROOT.parent/'coupled_reference_v0_5/kinematics.py')
    k=importlib.util.module_from_spec(spec);spec.loader.exec_module(k)
    rows=csv_rows(out/'stars_2_0_wp_b_v04_correlated_3alpha_events.csv')
    energy=[];pz=[]
    for r in rows:
        E=float(r['E_proton_lab_keV'])*1e-3
        energy.append(float(r['E_sum_lab_MeV'])-(E+k.Q))
        longitudinal=sum(math.sqrt(float(r[f'E_lab_alpha{i}_MeV'])*(float(r[f'E_lab_alpha{i}_MeV'])+2*k.MA))*float(r[f'mu_lab_alpha{i}']) for i in [1,2,3])
        pz.append(longitudinal-math.sqrt(E*(E+2*k.MP)))
    sweep=csv_rows(out/'stars_2_0_wp_b_v04_s2_collector_window_sweep.csv')
    optima={name:float(max(sweep,key=lambda r:float(r[name]))['thickness_um']) for name in ['E_alpha_exit_rear_uJ','E_alpha_exit_4pi_uJ','E_collector_window_accepted_uJ']}
    return dict(source_sha256=sha(source),matches_Tidal_Lantern_extracted_hash=True,
        matches_Gemini_prior_claimed_hash=False,prior_claimed_hash='0fdfcc1d4cdf6c177ee19fa0fb23a3588b1bdca2464036b7b91b29398bc93cf8',
        numpy=numpy.__version__,scipy=scipy.__version__,python=platform.python_version(),
        generated_csvs={f.name:dict(bytes=f.stat().st_size,sha256=sha(f),rows=len(csv_rows(f))) for f in sorted(out.glob('*.csv'))},
        seed=20261027,event_rows=len(rows),mass_correct_reference_Q_MeV=k.Q,
        max_abs_physical_energy_residual_MeV=max(map(abs,energy)),
        max_abs_physical_longitudinal_momentum_residual_MeV_c=max(map(abs,pz)),
        max_internal_scaled_momentum_residual=max(float(r['momentum_residual_norm']) for r in rows),
        max_internal_kinetic_energy_residual_MeV=max(float(r['energy_residual_MeV']) for r in rows),
        reference_physical_conservation_tolerance_MeV=1e-8,
        physical_mass_conservation_status='FAIL' if max(map(abs,energy))>1e-8 or max(map(abs,pz))>1e-8 else 'PASS',
        full_physical_momentum_audit='not possible from exported CSV: alpha azimuths / full vectors absent; longitudinal failure alone suffices',
        sampled_optima_um=optima,qualified_for_calibrated_source=False,
        reason='effective target mass, Galilean kinematics, fixed uncalibrated branch ratio; main thickness sweep uses separate hard-coded spectra',
        promotion='blocked; retain original as surrogate and implement a separately versioned mass-correct sequential model before source fit')

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve earlier run')
    source=ROOT/'original/stars_v04_original_extracted.py'
    raw=(ROOT/'original/GEMINI_V04_ATTACHMENT.md').read_bytes()
    if b''.join(raw.splitlines(keepends=True)[1:-1])!=source.read_bytes() or sha(source)!=EXPECTED:raise ValueError('source extraction identity mismatch')
    a.out.mkdir(parents=True,exist_ok=False)
    r=subprocess.run([sys.executable,str(source)],cwd=a.out,capture_output=True,text=True)
    (a.out/'STDOUT.txt').write_text(r.stdout);(a.out/'STDERR.txt').write_text(r.stderr)
    if r.returncode:raise RuntimeError('original execution failed; outputs preserved')
    result=inspect_outputs(a.out)
    (a.out/'REPRODUCTION.json').write_text(encoded(result));print(encoded(result))

if __name__=='__main__':main()
