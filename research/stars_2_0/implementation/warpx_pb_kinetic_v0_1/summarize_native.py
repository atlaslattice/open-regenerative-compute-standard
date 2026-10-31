import json,math
from pathlib import Path
import yt
import numpy as np
from scipy.constants import m_u,m_e,c,e
root=Path(__file__).resolve().parent
run=root/'receipts'/'upstream3d001'
ds=yt.load(str(run/'diags/diag1000001'));ad=ds.all_data()
m=4.00260325413*m_u-2*m_e
rows=[]
for i in range(1,6):
 sp='alpha'+str(i)
 w=ad[sp,'particle_weight'].v
 px=ad[sp,'particle_momentum_x'].v;py=ad[sp,'particle_momentum_y'].v;pz=ad[sp,'particle_momentum_z'].v
 psq=px*px+py*py+pz*pz
 energy=psq/(np.sqrt(m*m+psq/c**2)+m)
 rows.append(dict(subtest=i,alpha_macroparticles=len(w),weighted_alpha_births=math.fsum(w),weighted_fusion_events=math.fsum(w)/3,weighted_alpha_kinetic_energy_J=math.fsum(w*energy),interpretation='UPSTREAM_CONSTRUCTED_POPULATION_NOT_APPARATUS_OUTPUT'))
p=root/'receipts'/'NATIVE_SUMMARY001.json'
with p.open('x') as f:json.dump({'upstream_analysis_exit_code':0,'source_input_overrides':[],'layout':'NOMPI, OMP_NUM_THREADS=2; upstream CMake uses two MPI ranks','max_step':1,'particle_pushing':False,'particle_deposition':False,'subtests':rows},f,indent=2);f.write('\n')
print(json.dumps(rows,indent=2))
