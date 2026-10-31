"""Execute admitted weighted joint records in WarpX; numerical fixture only."""
import json,hashlib,math,subprocess,os
from pathlib import Path
from admission import admit,input_fragment
root=Path(__file__).resolve().parent
case=next(r for r in json.loads((root/'receipts/MAP_RUNS.json').read_text()) if r['case']=='canonical_mm_675keV')
u=case['normalized_u'];norm=math.sqrt(sum(x*x for x in u))
source=dict(jointness='JOINT_RECORDS',species='proton',frame='LAB',units={'position':'m','time':'s','kinetic_energy':'MeV','weight':'physical_particles'},normalization='ABSOLUTE_PHYSICAL_PARTICLES_PER_SNAPSHOT',evidence={'kind':'NUMERICAL_VERIFICATION','source_ref':'inputs/canonical_mm_675keV; new weight=7 verification choice','input_sha256':hashlib.sha256((root/'inputs/canonical_mm_675keV').read_bytes()).hexdigest()},snapshot_time_s=0,records=[dict(id='verification_p1',weight=7,kinetic_MeV=.675,position_m=case['initial_position_m'],unit_direction_LAB=[x/norm for x in u],time_s=0)])
field=dict(grid_unit_SI=1,component_unit_SI=[1,1,1],axis_labels=['x','y','z'],map_sha256=hashlib.sha256((root/'maps/canonical_mm.h5').read_bytes()).hexdigest(),source_ref='Derived canonical-mm interpretation of pinned FEMM map, not STARS field map',domain_lo_m=[-.001,-.001,0],domain_hi_m=[.001,.001,.005],time_dependence='STATIC')
result=admit(source,field)
for name,obj in [('ADAPTER_SOURCE.json',source),('ADAPTER_FIELD.json',field),('ADMISSION_RECEIPT.json',result)]:
 with (root/'receipts'/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
base=(root/'inputs/canonical_mm_675keV').read_text().splitlines()
base=[s for s in base if not s.startswith('proton.injection_style') and not s.startswith('proton.single_particle_')]
inp=root/'inputs/admitted_weight7'
with inp.open('x') as f:f.write('\n'.join(base)+'\n'+input_fragment(result))
out=root/'receipts/admitted_weight7';out.mkdir(exist_ok=False)
with (out/'RUN.log').open('x') as f:r=subprocess.run([str(Path(os.environ.get('STELLAR_WARPX_ENV',str(root.parent/'warpx_runtime_v0_1/env')))/'bin/warpx.3d'),str(inp)],cwd=out,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
assert r.returncode==0
import numpy as np
old=root/'receipts/canonical_mm_675keV/diags/reducedfiles'
a=np.loadtxt(old/'extrema.txt');b=np.loadtxt(out/'diags/reducedfiles/extrema.txt')
na=np.loadtxt(old/'number.txt');nb=np.loadtxt(out/'diags/reducedfiles/number.txt')
active=na[:,4]>0
assert np.allclose(na[:,4]*7,nb[:,4],rtol=0,atol=0)
error=float(np.max(np.abs(a[active,2:14]-b[active,2:14])))
assert error<1e-12
with (root/'receipts/ADAPTER_EXECUTION_CHECK.json').open('x') as f:json.dump({'status':'PASS','max_absolute_position_or_momentum_component_difference_SI':error,'all_number_weights_exactly_scaled_by':7,'source_grade':'NUMERICAL_VERIFICATION','self_fields':False,'physical_reaction_count':'NOT_MODELED'},f,indent=2);f.write('\n')
print('Joint-record adapter executed; trajectory preserved and physical weights scaled exactly7x.')
