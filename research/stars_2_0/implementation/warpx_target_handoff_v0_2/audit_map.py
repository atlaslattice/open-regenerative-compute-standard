import sys,json,hashlib
from pathlib import Path
import numpy as np
import openpmd_api as io
p=Path(sys.argv[1]);s=io.Series(str(p),io.Access.read_only);b=s.iterations[1].meshes['B']
assert b.grid_unit_SI==1 and b.axis_labels==['x','y','z']
a=np.array(b.grid_spacing);lo=np.array(b.grid_global_offset);hi=lo+(np.array(b['x'].shape)-1)*a
assert np.all(a>0) and np.all(lo<=np.array([-.001,-.001,0])) and np.all(hi>=np.array([.001,.001,.0035]))
limits={}
for x in 'xyz':
 assert b[x].unit_SI==1;v=b[x].load_chunk();s.flush();assert np.all(np.isfinite(v));limits[x]=[float(v.min()),float(v.max())]
s.close()
with Path(sys.argv[2]).open('x') as f:json.dump(dict(map_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),B_upper_T=float(np.sqrt(sum(max(abs(v) for v in pair)**2 for pair in limits.values()))),lo_m=[-.001,-.001,0],hi_m=[.001,.001,.0035],evidence='SOURCE_DERIVED_MM_MAP_AND_NEW_VERIFICATION_TARGET_PLANE'),f,indent=2);f.write('\n')
