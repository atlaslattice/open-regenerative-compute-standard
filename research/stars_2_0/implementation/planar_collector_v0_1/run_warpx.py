"""Prescribed uniform-E alpha trajectories: numerical verification, not electrodes."""
import argparse,hashlib,json,math,os,subprocess,time
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--runtime',required=True);p.add_argument('--models',required=True);p.add_argument('--out',required=True);a=p.parse_args();runtime=Path(a.runtime).resolve();root=Path(a.models).resolve();out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
C=299792458.;MEV_J=1.602176634e-13;QE=1.602176634e-19
M=json.loads((root/'coupled_reference_v0_5/MASS_SOURCE.json').read_text())['alpha_MeV'];mass=M*MEV_J/C**2;T=3.;p0=math.sqrt(T*(T+2*M))*MEV_J/C;rows=[];checks=[]
for label,mu,E,dt in [('normal',1.,-1e8,1e-12),('normal_half_dt',1.,-1e8,5e-13),('grazing',.1,-1e8,1e-12),('grazing_half_dt',.1,-1e8,5e-13),('accelerating',1.,1e8,1e-12),('zero_field',.1,0.,1e-12)]:
 steps=round(5e-10/dt);dest=out/label;dest.mkdir();px=p0*math.sqrt(1-mu*mu);pz=p0*mu
 text=f'''# NUMERICAL FIXTURE: one nominal alpha, prescribed uniform field, no deposition
max_step = {steps}
amr.n_cell = 8 8 8
amr.max_grid_size = 8
amr.max_level = 0
geometry.dims = 3
geometry.prob_lo = -0.05 -0.05 -0.05
geometry.prob_hi = 0.05 0.05 0.05
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
particles.species_names = alpha
alpha.mass = {mass:.17g}
alpha.charge = 2*q_e
alpha.injection_style = MultipleParticles
alpha.do_not_deposit = 1
alpha.multiple_particles_pos_x = 0
alpha.multiple_particles_pos_y = 0
alpha.multiple_particles_pos_z = 0
alpha.multiple_particles_ux = {px/(mass*C):.17g}
alpha.multiple_particles_uy = 0
alpha.multiple_particles_uz = {pz/(mass*C):.17g}
alpha.multiple_particles_weight = 1
particles.E_ext_particle_init_style = constant
particles.E_external_particle = 0 0 {E}
warpx.reduced_diags_names = extrema number
extrema.type = ParticleExtrema
extrema.species = alpha
extrema.intervals = 1
number.type = ParticleNumber
number.intervals = 1
'''
 inp=dest/'inputs';inp.write_text(text);start=time.time()
 with (dest/'EXECUTION.log').open('x') as f:r=subprocess.run([str(runtime/'bin/warpx.3d'),str(inp)],cwd=dest,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError(label+' failed')
 trace=np.loadtxt(dest/'diags/reducedfiles/extrema.txt');t=trace[:,1];z=trace[:,6];px_num=trace[:,8];pz_num=trace[:,12];p2=px_num**2+trace[:,10]**2+pz_num**2
 kinetic=p2/(np.sqrt(mass*mass+p2/C**2)+mass)/MEV_J
 exact_pz=pz+2*QE*E*t;exact_total=np.sqrt((mass*C*C)**2+C*C*(px*px+exact_pz**2));initial_total=(M+T)*MEV_J
 if E:exact_z=(exact_total-initial_total)/(2*QE*E)
 else:exact_z=t*pz*C*C/initial_total
 energy_res=kinetic-2*QE*E*z/MEV_J-T
 row={'case':label,'dt_s':dt,'field_V_m':E,'mu':mu,'max_position_error_m':float(np.max(abs(z-exact_z))),'max_momentum_relative_error':float(np.max(abs(pz_num-exact_pz))/p0),'max_energy_potential_residual_MeV':float(np.max(abs(energy_res))),'final_kinetic_MeV':float(kinetic[-1]),'final_z_m':float(z[-1]),'final_normal_momentum_kg_m_s':float(pz_num[-1]),'runtime_s':time.time()-start};rows.append(row)
 for name,passed in [('pz_exact_uniform_force',row['max_momentum_relative_error']<1e-10),('px_conserved',float(np.max(abs(px_num-px)))/p0<1e-10),('trajectory_position',row['max_position_error_m']<1e-8),('energy_plus_potential',row['max_energy_potential_residual_MeV']<1e-5)]:checks.append({'name':label+'_'+name,'passed':bool(passed)})
 print(label,row['max_energy_potential_residual_MeV'],flush=True)
for base in ['normal','grazing']:
 x=next(r for r in rows if r['case']==base);y=next(r for r in rows if r['case']==base+'_half_dt');checks.append({'name':base+'_position_error_refines','passed':y['max_position_error_m']<x['max_position_error_m']/3})
checks.append({'name':'grazing_particle_reflected','passed':next(r for r in rows if r['case']=='grazing')['final_normal_momentum_kg_m_s']<0})
(out/'RESULTS.json').write_text(json.dumps({'status':'PRESCRIBED_UNIFORM_E_TEST_PARTICLE_ONLY','results':rows,'checks':checks,'executable_sha256':hashlib.sha256((runtime/'bin/warpx.3d').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'apparatus_net_power':None},indent=2)+'\n');print('checks',sum(x['passed'] for x in checks),'/',len(checks));assert all(x['passed'] for x in checks)
