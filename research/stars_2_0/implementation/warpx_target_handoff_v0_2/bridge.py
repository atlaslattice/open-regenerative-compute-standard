"""Finite, one-way domain-scrape routing. No source or surface state is imputed."""
import math,copy
C=299792458.;QE=1.602176634e-19;MEV_J=1.602176634e-13;MP=1.67262192595e-27

def finite(x):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite numeric value required')
 return x

def kinetic(r):
 p=r['momentum_kg_m_s'];m=finite(r['mass_kg']);w=finite(r['weight'])
 if len(p)!=3 or m<=0 or abs(m/MP-1)>1e-6 or w<0:raise ValueError('positive-mass proton and nonnegative weight required')
 if abs(finite(r['charge_C'])/QE-1)>1e-8:raise ValueError('proton charge required')
 q=math.fsum(finite(x)**2 for x in p)
 return q/(math.sqrt(m*m+q/C**2)+m)/MEV_J

def route(records,geometry,dt,aperture=None):
 if records is None:return {'status':'MISSING_BOUNDARY_DATA','arrivals':None,'losses':None}
 if finite(dt)<=0 or finite(geometry['B_upper_T'])<0:raise ValueError('invalid dt/field bound')
 arrivals=[];losses=[];seen=set()
 for raw in records:
  r=copy.deepcopy(raw);rid=r['id'];face=r['face']
  if not isinstance(rid,str) or not rid or rid in seen:raise ValueError('ambiguous repeated boundary ID')
  seen.add(rid)
  if face not in ('xlo','xhi','ylo','yhi','zlo','zhi'):raise ValueError('unsupported boundary')
  K=kinetic(r);p=r['momentum_kg_m_s'];pos=r['position_m']
  if len(pos)!=3:raise ValueError('three coordinates required')
  for x in pos:finite(x)
  norm=math.sqrt(math.fsum(x*x for x in p));m=r['mass_kg'];gamma=math.sqrt(1+norm*norm/(m*C)**2)
  if norm==0:raise ValueError('zero momentum crossing')
  v=[x/(gamma*m) for x in p];axis='xyz'.index(face[0]);sign=-1 if face.endswith('lo') else 1
  plane=geometry['lo_m'][axis] if sign<0 else geometry['hi_m'][axis]
  if sign*v[axis]<=0:raise ValueError('inward boundary momentum')
  back=(pos[axis]-plane)/v[axis]
  if back<0 or back>dt*(1+1e-7):raise ValueError('crossing outside final timestep')
  t=finite(r['time_s']);step=r['step']
  if isinstance(step,bool) or not isinstance(step,int) or step<1 or abs(t-step*dt)>1e-10*max(t,dt):raise ValueError('step/time mismatch')
  if r['delta_s']!=0:raise ValueError('non-domain/EB time convention unsupported')
  entry=[x-u*back for x,u in zip(pos,v)];entry[axis]=plane
  packet=dict(id=rid,face=face,weight=r['weight'],kinetic_MeV=K,unit_direction_LAB=[x/norm for x in p],position_m=entry,time_s=t-back,time_bracket_s=[max(0,t-dt),t],raw_position_m=pos,raw_time_s=t,surface_status='DERIVED_FINAL_DRIFT_NOT_EXACT_SURFACE',step_distance_m=norm/(gamma*m)*dt,angular_step_bound_rad=QE*geometry['B_upper_T']*dt/(gamma*m))
  if face=='zhi':
   radius=geometry['hi_m'][0] if aperture is None else finite(aperture)
   if radius<=0:raise ValueError('positive aperture required')
   margin=radius-max(abs(entry[0]),abs(entry[1]))
   if abs(margin)<=packet['step_distance_m']:raise ValueError('near-aperture ambiguity')
   if margin>0:arrivals.append(packet);continue
   packet['loss_kind']='TARGET_APERTURE_MISS'
  else:packet['loss_kind']='OTHER_DOMAIN_FACE'
  losses.append(packet)
 return dict(status='ROUTED_DERIVED_SURFACE',arrivals=arrivals,losses=losses)

def check_source(n,k,records):
 if records is None:return dict(status='MISSING_DATA',particle_residual=None,energy_residual_MeV=None)
 if finite(n)<0 or finite(k)<0:raise ValueError('negative source')
 total=math.fsum(finite(r['weight']) for r in records);energy=math.fsum(r['weight']*kinetic(r) for r in records)
 dn=n-total;dk=k-energy
 if abs(dn)>1e-10*max(1,n) or abs(dk)>1e-10*max(1,k):raise ValueError('incomplete/duplicated boundary balance')
 return dict(status='PASS',particle_residual=dn,energy_residual_MeV=dk)
