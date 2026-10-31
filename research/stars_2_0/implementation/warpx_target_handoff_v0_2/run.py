"""Reconstructed v0.2 runner; all numerical assumptions are verification fixtures."""
import argparse,json,hashlib,os,shutil,subprocess,math,time
from pathlib import Path
from scipy.constants import c,m_p,e
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runtime',required=True);p.add_argument('--map',required=True);p.add_argument('--handoff-dir',required=True);p.add_argument('--out',required=True);a=p.parse_args()
code=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
runtime=Path(a.runtime).resolve();mapfile=Path(a.map).resolve();model=Path(a.handoff_dir).resolve()
assert hashlib.sha256((model/'handoff.py').read_bytes()).hexdigest()=='cbb2ca13612dacea05329fa3fbd517cd1e2ab4fedfb25986a831bb8dcffe9d0b'
assert hashlib.sha256((model/'DEPENDENCY_LOCK.json').read_bytes()).hexdigest()=='cf48edbae73068f717e82953e1164cd343741a0676a7467f6528476dcf1937f4'
for f in code.glob('*.py'):
 if f.name!='run.py':shutil.copyfile(f,out/f.name)
env={**os.environ,'OMP_NUM_THREADS':'2','STELLAR_HANDOFF_DIR':str(model)};receipts=[]
def execute(label,args,cwd):
 start=time.time()
 with (cwd/(label+'.log')).open('x') as f:r=subprocess.run(args,cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT)
 receipts.append(dict(stage=label,returncode=r.returncode,command=args,elapsed_s=time.time()-start));print(label,r.returncode,flush=True)
 assert r.returncode==0,label
execute('MAP',[str(runtime/'bin/python'),str(out/'audit_map.py'),str(mapfile),str(out/'MAP.json')],out)
K=.675;gamma=1+K*1e6*e/(m_p*c*c);u=math.sqrt((gamma-1)*(gamma+1))
dirs=[[math.sin(math.atan(1/math.sqrt(2))),0,math.cos(math.atan(1/math.sqrt(2)))],[math.sin(math.radians(75)),0,math.cos(math.radians(75))],[0,0,-1]]
(out/'FIXTURE.json').write_text(json.dumps(dict(source_grade='SYNTHETIC_VERIFICATION',kinetic_MeV=K,directions=dirs,weights=[10000,20000,5000],position_m=[0,.0002,.0025],target_plane_z_m=.0035),indent=2)+'\n')
(out/'inputs').mkdir();(out/'runs').mkdir()
for name in ['field_on','field_off','half_dt']:
 dt=5e-13 if name=='half_dt' else 1e-12;steps=800 if name=='half_dt' else 400
 text=f'''# SYNTHETIC SOURCE/GEOMETRY; SOURCE-DERIVED MAP; NOT APPARATUS
max_step = {steps}
amr.n_cell = 40 40 40
amr.max_grid_size = 40
amr.max_level = 0
geometry.dims = 3
geometry.prob_lo = -0.001 -0.001 0
geometry.prob_hi = 0.001 0.001 0.0035
boundary.field_lo = pec pec pec
boundary.field_hi = pec pec pec
boundary.particle_lo = absorbing absorbing absorbing
boundary.particle_hi = absorbing absorbing absorbing
warpx.const_dt = {dt}
warpx.verbose = 0
warpx.use_filter = 0
algo.maxwell_solver = none
algo.particle_shape = 1
algo.particle_pusher = boris
warpx.grid_type = collocated
particles.species_names = proton
proton.mass = m_p
proton.charge = q_e
proton.injection_style = MultipleParticles
proton.do_not_deposit = 1
'''
 if name!='field_off':text+='particles.B_ext_particle_init_style = read_from_file\nparticles.read_fields_from_path = '+json.dumps(str(mapfile))+'\n'
 for j,axis in enumerate('xyz'):
  text+='proton.multiple_particles_pos_'+axis+' = '+' '.join(str([0,.0002,.0025][j]) for _ in dirs)+'\n'
  text+='proton.multiple_particles_u'+axis+' = '+' '.join(format(u*d[j],'.17g') for d in dirs)+'\n'
 text+='proton.multiple_particles_weight = 10000 20000 5000\n'
 for face in ['xlo','xhi','ylo','yhi','zlo','zhi']:text+='proton.save_particles_at_'+face+' = 1\n'
 text+=f'''warpx.reduced_diags_names = extrema number
extrema.type = ParticleExtrema
extrema.species = proton
extrema.intervals = 1
number.type = ParticleNumber
number.intervals = 1
diagnostics.diags_names = scrape
scrape.diag_type = BoundaryScraping
scrape.format = openpmd
scrape.openpmd_backend = h5
scrape.intervals = {steps}
'''
 inp=out/'inputs'/name;inp.write_text(text);dest=out/'runs'/name;dest.mkdir();execute(name,[str(runtime/'bin/warpx.3d'),str(inp)],dest)
execute('EXTRACT',[str(runtime/'bin/python'),str(out/'read_scrapes.py'),str(out)],out)
execute('COUPLE',[str(runtime/'bin/python'),str(out/'couple.py'),str(out)],out)
if (out/'test_bridge.py').exists():execute('TESTS',[str(runtime/'bin/python'),'-m','unittest','test_bridge','-v'],out)
(out/'RECEIPT.json').write_text(json.dumps(dict(status='PASS',stages=receipts,executable_sha256=hashlib.sha256((runtime/'bin/warpx.3d').read_bytes()).hexdigest(),model_sha256=hashlib.sha256((model/'handoff.py').read_bytes()).hexdigest(),map_sha256=hashlib.sha256(mapfile.read_bytes()).hexdigest(),scientific_freeze=False),indent=2)+'\n')
