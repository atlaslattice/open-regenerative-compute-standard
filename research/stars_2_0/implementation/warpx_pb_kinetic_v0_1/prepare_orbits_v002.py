"""Create named numerical fixtures; no recovered apparatus or coil specification."""
import json,math
from pathlib import Path
from scipy.constants import c,m_p,e
ROOT=Path(__file__).resolve().parent
K=675e3*e
gamma=1+K/(m_p*c*c)
u=math.sqrt((gamma-1)*(gamma+1))
cases=[('uniform_dt',45,2,0,2e-10,1000),('uniform_half_dt',45,2,0,1e-10,2000),('mirror_losscone',10,2,4/25,2e-10,6000),('mirror_reflect',45,2,4/25,2e-10,6000),('mirror_reflect_half_dt',45,2,4/25,1e-10,12000)]
(ROOT/'inputs_v002').mkdir(exist_ok=True)
manifest=[]
for name,pitch,B0,a,dt,n in cases:
 s=f'''# SYNTHETIC NUMERICAL FIELD FIXTURE; NOT APPARATUS PARAMETERS
max_step = {n}
amr.n_cell = 8 8 8
amr.max_grid_size = 8
amr.blocking_factor = 8
amr.max_level = 0
geometry.dims = 3
geometry.prob_lo = -1 -1 -5
geometry.prob_hi = 1 1 5
boundary.field_lo = pec pec pec
boundary.field_hi = pec pec pec
boundary.particle_lo = absorbing absorbing absorbing
boundary.particle_hi = absorbing absorbing absorbing
warpx.verbose = 0
warpx.const_dt = {dt}
warpx.use_filter = 0
algo.particle_shape = 1
algo.particle_pusher = boris
particles.species_names = proton
proton.species_type = hydrogen1
proton.injection_style = SingleParticle
proton.single_particle_pos = 0 0 0
proton.single_particle_u = {u*math.sin(math.radians(pitch)):.17g} 0 {u*math.cos(math.radians(pitch)):.17g}
proton.single_particle_weight = 1
proton.do_not_deposit = 1
particles.B_ext_particle_init_style = parse_B_ext_particle_function
particles.Bx_external_particle_function(x,y,z,t) = -({B0*a})*x*z
particles.By_external_particle_function(x,y,z,t) = -({B0*a})*y*z
particles.Bz_external_particle_function(x,y,z,t) = {B0}*(1+({a})*z*z)
warpx.reduced_diags_names = extrema number energy
extrema.type = ParticleExtrema
extrema.species = proton
extrema.intervals = 10
number.type = ParticleNumber
number.intervals = 10
energy.type = ParticleEnergy
energy.intervals = 10
'''
 p=ROOT/'inputs_v002'/name;p.open('x').write(s)
 manifest.append(dict(case=name,pitch_deg=pitch,B0_T=B0,quadratic_coefficient_m2=a,dt_s=dt,steps=n,initial_kinetic_energy_eV=675e3,physical_particle_weight=1,field='Bx=-B0*a*x*z; By=-B0*a*y*z; Bz=B0*(1+a*z^2)',divergence='0 exactly',source='NEW_SYNTHETIC_NUMERICAL_VERIFICATION_FIXTURE',collision_model='NONE',fusion_model='NONE',self_fields='NO_PARTICLE_DEPOSITION; EXTERNAL_FIELD_TEST_PARTICLE',boundary='particle absorbing; field PEC zero-self-field; z_throat +/-5m; on-axis mirror ratio5 when a=.16m^-2'))
(ROOT/'ORBIT_CASES_v002.json').write_text(json.dumps(manifest,indent=2)+'\n')
