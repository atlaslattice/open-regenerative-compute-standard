"""Audit a source-derived unit interpretation; do not overwrite the original dataset."""
import json,hashlib
from pathlib import Path
import numpy as np
import openpmd_api as io
root=Path(__file__).resolve().parent
src=root/'example-femm-3d.original.h5'
raw=src.read_bytes();expected='fddd0a849d8f5ffc8ce9cd00fdc3dedd4ff62161'
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==expected
s=io.Series(str(src),io.Access.read_only);B=s.iterations[1].meshes['B']
spacing=np.array(B.grid_spacing);offset=np.array(B.grid_global_offset);arrays={}
for k in ['x','y','z']:arrays[k]=B[k].load_chunk()
s.flush()
arrays={k:np.array(v,copy=True) for k,v in arrays.items()}
info={'original_grid_unit_SI':B.grid_unit_SI,'original_grid_spacing':spacing.tolist(),'original_grid_offset':offset.tolist(),'original_axes':B.axis_labels,'original_sha256':hashlib.sha256(raw).hexdigest(),'original_git_blob':expected,'source_FEM_length_units':'millimeters','B_component_unit_SI':{k:B[k].unit_SI for k in arrays},'B_component_minmax_T':{k:[float(v.min()),float(v.max())] for k,v in arrays.items()},'interpretation':'SOURCE_UNIT_INCONSISTENCY_OR_UNDOCUMENTED_RESCALING; NOT A CLAIM OF AUTHOR INTENT OR LAB VALIDATION','derived_spatial_scale':.001}
(root/'maps').mkdir(exist_ok=True)
variants=[]
for name,spatial,unitSI in [('metadata_only_mm',1,.001),('canonical_mm',.001,1)]:
 path=root/'maps'/(name+'.h5');assert not path.exists()
 dest=io.Series(str(path),io.Access.create)
 for field in ['B','E']:
  mesh=dest.iterations[1].meshes[field];mesh.grid_spacing=(spacing*spatial).tolist();mesh.grid_global_offset=(offset*spatial).tolist();mesh.grid_unit_SI=unitSI;mesh.axis_labels=['x','y','z'];mesh.geometry=io.Geometry.cartesian
  mesh.unit_dimension={io.Unit_Dimension.M:1,io.Unit_Dimension.I:-1,io.Unit_Dimension.T:-2} if field=='B' else {io.Unit_Dimension.M:1,io.Unit_Dimension.L:1,io.Unit_Dimension.I:-1,io.Unit_Dimension.T:-3}
  for k in ['x','y','z']:
   comp=mesh[k];comp.position=[0,0,0];comp.unit_SI=1;comp.reset_dataset(io.Dataset(np.dtype('float64'),arrays[k].shape))
   if field=='B':comp.store_chunk(arrays[k])
   else:comp.make_constant(0.)
 dest.flush();dest.close()
 check=io.Series(str(path),io.Access.read_only)
 for k in arrays:
  a=check.iterations[1].meshes['B'][k].load_chunk();check.flush();assert np.array_equal(a,arrays[k])
 check.close()
 variants.append({'variant':name,'file':str(path.relative_to(root)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'B_values_bit_identical':True,'gridSpacing_multiplier':spatial,'gridUnitSI':unitSI})
info['derived_variants']=variants
np.savez(root/'maps/FIELD_ARRAYS.npz',Bx=arrays['x'],By=arrays['y'],Bz=arrays['z'],spacing=spacing,offset=offset)
(root/'receipts').mkdir(exist_ok=True)
(root/'receipts/MAP_AUDIT.json').write_text(json.dumps(info,indent=2)+'\n')
s.close();print(json.dumps(info,indent=2))
