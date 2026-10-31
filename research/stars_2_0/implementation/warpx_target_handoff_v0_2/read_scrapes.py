import sys,json,hashlib
from pathlib import Path
import openpmd_api as io
root=Path(sys.argv[1]);result={}
for name in ['field_on','field_off','half_dt']:
 rows=[]
 for f in sorted((root/'runs'/name).glob('diags/scrape/particles_at_*/*.h5')):
  s=io.Series(str(f),io.Access.read_only)
  for index in s.iterations:
   species=s.iterations[index].particles['proton'];d={}
   for key,record in species.items():
    for component,q in record.items():d[(key,component)]=(q.load_chunk(),q.unit_SI)
   s.flush();scalar=io.Mesh_Record_Component.SCALAR
   def get(key,component=scalar):
    a,u=d[(key,component)];return a*u
   for i,ident in enumerate(d[('id',scalar)][0]):
    rows.append(dict(id=str(int(ident)),face=f.parent.name.removeprefix('particles_at_'),weight=float(get('weighting')[i]),mass_kg=float(get('mass')[i]),charge_C=float(get('charge')[i]),position_m=[float(get('position',x)[i]+get('positionOffset',x)[i]) for x in 'xyz'],momentum_kg_m_s=[float(get('momentum',x)[i]) for x in 'xyz'],time_s=float(get('timeScraped')[i]),step=int(d[('stepScraped',scalar)][0][i]),delta_s=float(get('deltaTimeScraped')[i]),file=str(f.relative_to(root)),sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
  s.close()
 result[name]=rows
with (root/'SCRAPES.json').open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
