"""Cold-matter stopping estimates: explicit electronic, nuclear and mixing assumptions."""
import bisect,hashlib,json,math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
NA=6.02214076e23
# Approximate atomic masses used by the stopping parameterization, NOT event-generator rest masses.
PROJECTILES={'proton':(1,1.007825),'alpha':(2,4.002603)}
MATERIALS={'B11':[(5,11.009305,1.)],
    'BN_B11_N14':[(5,11.009305,.5),(7,14.003074,.5)],
    'OVERLEY_B10_ENRICHED':[(5,10.012937,.9596),(5,11.009305,.0404)]}
NUCLEAR_VARIANTS={'ZBL_SIMNRA_7_04':(32.53,.01321),'ZBL_GEANT4_10_7_4':(32.536,.01312)}

def load_tables():
    lock=json.loads((ROOT/'TABLE_LOCK.json').read_text());out={}
    for r in lock:
        raw=(ROOT/r['file']).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=r['sha256']:raise ValueError('table identity mismatch')
        t=json.loads(raw);out[(t['model'],t['projectile_Z'],t['target_Z'])]=t
    return out

def log_interpolate(x,y,q):
    if not math.isfinite(q) or not x[0]<=q<=x[-1]:raise ValueError('outside electronic table energy domain')
    i=min(bisect.bisect_right(x,q)-1,len(x)-2)
    f=math.log(q/x[i])/math.log(x[i+1]/x[i])
    return math.exp(math.log(y[i])+(math.log(y[i+1])-math.log(y[i]))*f)

def nuclear_zbl(E_MeV,z1,m1,z2,m2,variant):
    if variant not in NUCLEAR_VARIANTS:raise ValueError('unknown nuclear variant')
    if not all(math.isfinite(v) and v>0 for v in [E_MeV,z1,m1,z2,m2]):raise ValueError('invalid nuclear input')
    c,k=NUCLEAR_VARIANTS[variant];rm=(m1+m2)*(z1**.23+z2**.23)
    e=c*m2*(1000*E_MeV)/(z1*z2*rm)
    reduced=math.log1p(1.1383*e)/(2*(e+k*e**.21226+.19593*math.sqrt(e))) if e<=30 else math.log(e)/(2*e)
    return 8.462*z1*z2*m1/rm*reduced*1e-15

def stopping(tables,*,model,projectile,material,E_MeV,bn_electronic_multiplier=None,nuclear_variant='ZBL_SIMNRA_7_04'):
    if model not in ['srim96','srim13'] or projectile not in PROJECTILES or material not in MATERIALS:raise ValueError('unsupported model/particle/material')
    is_bn=material=='BN_B11_N14'
    if is_bn:
        if bn_electronic_multiplier is None or not math.isfinite(bn_electronic_multiplier) or bn_electronic_multiplier<=0:
            raise ValueError('BN requires explicit positive electronic mixing multiplier')
    elif bn_electronic_multiplier is not None:raise ValueError('BN multiplier cannot modify elemental stopping')
    z1,m1=PROJECTILES[projectile];se=sn=mass=boron_fraction=0.
    for z2,m2,fraction in MATERIALS[material]:
        t=tables[(model,z1,z2)]
        se+=fraction*log_interpolate(t['energy_keV_u'],t['electronic_stopping_in_1e_minus15_eV_cm2_atom'],E_MeV*1000/m1)*1e-15
        sn+=fraction*nuclear_zbl(E_MeV,z1,m1,z2,m2,nuclear_variant)
        mass+=fraction*m2
        if z2==5:boron_fraction+=fraction
    if is_bn:se*=bn_electronic_multiplier
    return dict(electronic_eV_cm2_per_average_atom=se,nuclear_eV_cm2_per_average_atom=sn,
        total_eV_cm2_per_average_atom=se+sn,total_MeV_cm2_g=(se+sn)*1e-6*NA/mass,
        average_atomic_mass_u=mass,boron_atom_fraction=boron_fraction,
        model=model,projectile=projectile,material=material,nuclear_variant=nuclear_variant,
        bn_electronic_multiplier=bn_electronic_multiplier,status='CALCULATED_MODEL_NOT_MEASURED_MATERIAL_TABLE',
        electronic_assumption='equal-velocity isotope transfer of elemental electronic stopping',
        compound_assumption='Bragg atomic-fraction additivity with explicit electronic multiplier' if is_bn else None)

def transport(tables,*,model,projectile,material,E_MeV,total_atoms_cm2,bn_electronic_multiplier=None,refinement=16):
    if not math.isfinite(total_atoms_cm2) or total_atoms_cm2<0:raise ValueError('invalid column')
    if isinstance(refinement,bool) or not isinstance(refinement,int) or not 1<=refinement<=32:raise ValueError('invalid refinement')
    z,m=PROJECTILES[projectile]
    def S(e):return stopping(tables,model=model,projectile=projectile,material=material,E_MeV=e,bn_electronic_multiplier=bn_electronic_multiplier)['total_eV_cm2_per_average_atom']
    # Refine each upstream log interval; retain a positive low-energy floor.
    source=tables[(model,z,5)]['energy_keV_u'];lo=source[0]*m/1000
    S(E_MeV) # domain/material guard even for zero column
    if total_atoms_cm2==0:return dict(status='MODEL_INTERVAL_TRANSMISSION',E_in_MeV=E_MeV,E_out_MeV=E_MeV,primary_loss_MeV=0.)
    grid=[lo]
    for a,b in zip(source,source[1:]):
        for j in range(1,refinement+1):
            e=a*(b/a)**(j/refinement)*m/1000
            if e<E_MeV:grid.append(e)
    if E_MeV>lo:grid.append(E_MeV)
    values=[S(e) for e in grid]
    column=0.
    for a,b,sa,sb in reversed(list(zip(grid,grid[1:],values,values[1:]))):
        slope=(sb-sa)/(b-a)
        available=1e6*((b-a)/sa if slope==0 else math.log1p((sb-sa)/sa)/slope)
        if column+available>=total_atoms_cm2:
            remainder=(total_atoms_cm2-column)*1e-6
            eout=b-remainder*sb if slope==0 else b+sb*math.expm1(-slope*remainder)/slope
            return dict(status='MODEL_INTERVAL_TRANSMISSION',E_in_MeV=E_MeV,E_out_MeV=eout,
                primary_loss_MeV=E_MeV-eout,total_atoms_cm2=total_atoms_cm2,
                boron_atoms_cm2=total_atoms_cm2*sum(f for z,_,f in MATERIALS[material] if z==5),
                lower_model_energy_MeV=lo,stopping_components_at_entry=stopping(tables,model=model,projectile=projectile,material=material,E_MeV=E_MeV,bn_electronic_multiplier=bn_electronic_multiplier))
        column+=available
    if total_atoms_cm2==0:return dict(status='MODEL_INTERVAL_TRANSMISSION',E_in_MeV=E_MeV,E_out_MeV=E_MeV,primary_loss_MeV=0.)
    return dict(status='LOW_ENERGY_MODEL_BOUNDARY_REACHED',E_out_MeV=None,stopped=None,lower_model_energy_MeV=lo,
        covered_atoms_cm2=column,unmodeled_atoms_cm2=total_atoms_cm2-column)
