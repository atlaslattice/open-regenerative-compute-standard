"""Actual upstream stopping QA, trace drag, and drag+DT reaction benchmarks."""
from pathlib import Path
import os,sys,json,subprocess,hashlib,shutil,argparse
ROOT=Path(__file__).resolve().parent

def trace_input():
 s='''# Prescribed trace-ion collision benchmark; no fields or confinement.
max_step = 100
warpx.const_dt = 0.001
warpx.do_electrostatic = labframe
warpx.verbose = 0
warpx.random_seed = 119
amr.n_cell = 8 8 8
amr.max_level = 0
geometry.dims = 3
geometry.prob_lo = -1 -1 -1
geometry.prob_hi = 1 1 1
boundary.field_lo = periodic periodic periodic
boundary.field_hi = periodic periodic periodic
algo.particle_shape = 1
my_constants.mt = 3.0160492779*m_u-m_e
my_constants.md = 2.01410177812*m_u-m_e
my_constants.K = 1.e6*q_e
my_constants.u = sqrt(2*K/(mt*clight*clight)+(K/(mt*clight*clight))^2)
particles.species_names = T_e T_i T_both T_control
'''
 for name in ['T_e','T_i','T_both','T_control']:
  s+=f'''{name}.species_type = tritium
{name}.injection_style = MultipleParticles
{name}.multiple_particles_pos_x = 0
{name}.multiple_particles_pos_y = 0
{name}.multiple_particles_pos_z = 0
{name}.multiple_particles_ux = 0
{name}.multiple_particles_uy = 0
{name}.multiple_particles_uz = u
{name}.multiple_particles_weight = 1
{name}.do_not_push = 1
{name}.do_not_deposit = 1
'''
 s+='collisions.collision_names = e1 i1 e2 i2\n'
 for name,species,bg in [('e1','T_e','electrons'),('i1','T_i','ions'),('e2','T_both','electrons'),('i2','T_both','ions')]:
  s+=f'{name}.type = background_stopping\n{name}.species = {species}\n{name}.background_type = {bg}\n{name}.background_density = 1.e20\n{name}.background_temperature = '+('1.e4' if bg=='electrons' else '2.e4')+'*q_e/kb\n'
  if bg=='ions':s+=f'{name}.background_mass = md\n{name}.background_charge_state = 1\n'
 s+='''warpx.reduced_diags_names = energy number
energy.type = ParticleEnergy
energy.intervals = 1
energy.precision = 17
number.type = ParticleNumber
number.intervals = 1
number.precision = 17
diagnostics.diags_names = diag1
diag1.diag_type = Full
diag1.intervals = 100
diag1.fields_to_plot = rho
'''
 return s

def coupled_input():
 s=trace_input();start=s.index('particles.species_names');end=s.index('warpx.reduced_diags_names')
 block='''particles.species_names = T D He4 neutron
T.species_type = tritium
T.injection_style = NRandomPerCell
T.num_particles_per_cell = 100
T.profile = constant
T.density = 1.e12
T.momentum_distribution_type = parse_momentum_function
T.momentum_function_ux(x,y,z) = 0
T.momentum_function_uy(x,y,z) = 0
T.momentum_function_uz(x,y,z) = u
D.species_type = deuterium
D.injection_style = NRandomPerCell
D.num_particles_per_cell = 200
D.profile = constant
D.density = 1.e20
D.momentum_distribution_type = gaussian
D.ux_th = 0.003265007901313691
D.uy_th = 0.003265007901313691
D.uz_th = 0.003265007901313691
He4.species_type = helium4
neutron.species_type = neutron
'''
 for name in ('T','D','He4','neutron'):block+=f'{name}.do_not_push = 1\n{name}.do_not_deposit = 1\n'
 block+='''collisions.collision_names = stop_e stop_i DT
stop_e.type = background_stopping
stop_e.species = T
stop_e.background_type = electrons
stop_e.background_density = 1.e20
stop_e.background_temperature = 1.e4*q_e/kb
stop_i.type = background_stopping
stop_i.species = T
stop_i.background_type = ions
stop_i.background_density = 1.e20
stop_i.background_temperature = 2.e4*q_e/kb
stop_i.background_mass = md
stop_i.background_charge_state = 1
DT.type = nuclearfusion
DT.species = D T
DT.product_species = He4 neutron
DT.event_multiplier = 100
'''
 return s[:start]+block+s[end:]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--cache',type=Path,required=True);a=ap.parse_args()
 exe=a.executable.resolve();base=a.cache.resolve();base.mkdir(parents=True,exist_ok=True)
 (ROOT/'inputs/trace_triton_drag').write_text(trace_input());(ROOT/'inputs/drag_and_DT').write_text(coupled_input())
 cases=[('upstream',ROOT/'upstream/Examples/Tests/ion_stopping/inputs_test_3d_ion_stopping',[]),('drag_100',ROOT/'inputs/trace_triton_drag',[]),('drag_200',ROOT/'inputs/trace_triton_drag',['max_step=200','warpx.const_dt=0.0005','diag1.intervals=200']),('coupled_100',ROOT/'inputs/drag_and_DT',[]),('coupled_200',ROOT/'inputs/drag_and_DT',['max_step=200','warpx.const_dt=0.0005','diag1.intervals=200']),('coupled_no_drag',ROOT/'inputs/drag_and_DT',['collisions.collision_names=DT'])]
 records=[]
 for name,inp,overrides in cases:
  dest=ROOT/'outputs/warpx'/name;dest.mkdir(parents=True,exist_ok=True);d=base/name;d.mkdir(exist_ok=True)
  q=subprocess.run([str(exe),str(inp),*overrides],cwd=d,text=True,capture_output=True,env=dict(os.environ,OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='1'))
  (dest/'stdout.txt').write_text(q.stdout);(dest/'stderr.txt').write_text(q.stderr)
  record=dict(case=name,exit_code=q.returncode,overrides=overrides,input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),executable_sha256=hashlib.sha256(exe.read_bytes()).hexdigest(),physical_validation=False)
  if q.returncode==0:
   shutil.copyfile(d/'warpx_used_inputs',dest/'warpx_used_inputs')
   if name=='upstream':
    x=subprocess.run([sys.executable,str(ROOT/'upstream/Examples/Tests/ion_stopping/analysis.py'),str(d/'diags/diag1000010')],cwd=d,text=True,capture_output=True)
    (dest/'upstream_analysis.txt').write_text(x.stdout+x.stderr);record['analysis_exit']=x.returncode
   else:
    for f in (d/'diags/reducedfiles').glob('*.txt'):shutil.copyfile(f,dest/f.name)
  records.append(record);print(record,flush=True)
 (ROOT/'outputs/warpx_status.json').write_text(json.dumps(records,indent=2)+'\n')
 if any(r['exit_code'] or r.get('analysis_exit',0) for r in records):raise SystemExit(1)
if __name__=='__main__':main()
