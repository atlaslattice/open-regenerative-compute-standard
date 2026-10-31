"""Named FEMM map loader/unit controls; no Stars geometry or source spectrum."""
import json,math,os,subprocess,time
from pathlib import Path
from scipy.constants import c,e,m_p
root=Path(__file__).resolve().parent
exe=Path(os.environ.get('STELLAR_WARPX_ENV',str(root.parent/'warpx_runtime_v0_1/env')))/'bin/warpx.3d'
cases=[('original_low',1.,'example-femm-3d.original.h5',False,4.40917904849092e-7,300),('metadata_only_negative_control',1.,'maps/metadata_only_mm.h5',False,4.40917904849092e-7,300),('canonical_mm_low',.001,'maps/canonical_mm.h5',False,4.40917904849092e-10,300),('original_no_B',1.,None,False,4.40917904849092e-7,300),('original_675keV',1.,'example-femm-3d.original.h5',True,1e-9,300),('canonical_mm_675keV',.001,'maps/canonical_mm.h5',True,1e-12,300),('canonical_mm_low_half_dt',.001,'maps/canonical_mm.h5',False,2.20458952424546e-10,600)]
(root/'inputs').mkdir(exist_ok=True)
rows=[]
for name,scale,mapfile,high,dt,steps in cases:
 ux,uz=9.506735958279367e-5,.00013435537232359165
 if high:
  gamma=1+675e3*e/(m_p*c*c);u=math.sqrt((gamma-1)*(gamma+1));angle=math.atan2(ux,uz);ux,uz=u*math.sin(angle),u*math.cos(angle)
 fields='' if mapfile is None else f'particles.B_ext_particle_init_style = read_from_file\nparticles.read_fields_from_path = "{root/mapfile}"\n'
 txt=f'''# SOURCE-DERIVED MAP BENCHMARK; NOT STARS APPARATUS
max_step = {steps}
amr.n_cell = 40 40 40
amr.max_grid_size = 40
amr.max_level = 0
geometry.dims = 3
geometry.prob_lo = {-scale} {-scale} 0
geometry.prob_hi = {scale} {scale} {5*scale}
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
proton.injection_style = SingleParticle
proton.single_particle_pos = 0 {0.2*scale} {2.5*scale}
proton.single_particle_u = {ux} 0 {uz}
proton.single_particle_weight = 1
proton.do_not_deposit = 1
{fields}
warpx.reduced_diags_names = extrema number
extrema.type = ParticleExtrema
extrema.species = proton
extrema.intervals = 1
number.type = ParticleNumber
number.intervals = 1
'''
 inp=root/'inputs'/name
 with inp.open('x') as f:f.write(txt)
 out=root/'receipts'/name;out.mkdir(exist_ok=False)
 start=time.time()
 with (out/'RUN.log').open('x') as f:r=subprocess.run([str(exe),str(inp)],cwd=out,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
 rows.append(dict(case=name,scale_m_per_source_length=scale,map=mapfile,kinetic_energy_eV=675e3 if high else (math.sqrt(1+ux*ux+uz*uz)-1)*m_p*c*c/e,normalized_u=[ux,0,uz],initial_position_m=[0,.2*scale,2.5*scale],dt_s=dt,steps=steps,returncode=r.returncode,runtime_s=time.time()-start,source_evidence='UPSTREAM_NUMERICAL_PARTICLE_FIXTURE' if not high else 'NEW_675KEV_NUMERICAL_SENSITIVITY_NOT_MEASURED_BEAM'))
 print(name,r.returncode,flush=True)
(root/'receipts/MAP_RUNS.json').write_text(json.dumps(rows,indent=2)+'\n')
assert all(r['returncode']==0 for r in rows)
