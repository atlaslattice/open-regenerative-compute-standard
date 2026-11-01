"""SI hollow-shell geometry shared by mesh and PIC adapters; no material model."""
import math

SOURCE = 'https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/hydrogen-boron-fusion-in-confined-geometries/D273DDE00ABB65D29D2053845A22A887'

def validate(p):
    for k in ('inner_radius_m', 'wall_m', 'aperture_radius_m'):
        if not math.isfinite(p[k]) or p[k] <= 0:
            raise ValueError(k)
    if p['aperture_radius_m'] >= p['inner_radius_m']:
        raise ValueError('aperture must be smaller than cavity')
    return p

def inside(p, x, y, z):
    validate(p)
    if not all(math.isfinite(v) for v in (x,y,z)):
        raise ValueError('nonfinite position')
    r2=x*x+y*y+z*z
    return (p['inner_radius_m']**2 < r2 < (p['inner_radius_m']+p['wall_m'])**2
            and not (z >= 0 and x*x+y*y < p['aperture_radius_m']**2))

def warpx_mask(p):
    """WarpX math-parser expression; multiply by independently qualified density."""
    validate(p)
    ri=p['inner_radius_m']; ro=ri+p['wall_m']; a=p['aperture_radius_m']
    return f'((x*x+y*y+z*z)>{ri*ri:.17g})*((x*x+y*y+z*z)<{ro*ro:.17g})*(1-((z>=0)*((x*x+y*y)<{a*a:.17g})))'

def gmsh_geo(p, h):
    validate(p)
    if not math.isfinite(h) or h <= 0 or h > p['wall_m']/2:
        raise ValueError('mesh size must be <= half wall thickness')
    # CAD works in micrometres to avoid OCC precision problems at tiny SI scales.
    # Mesh.ScalingFactor converts the written mesh back to metres.
    ri=p['inner_radius_m']*1e6; ro=ri+p['wall_m']*1e6; a=p['aperture_radius_m']*1e6
    h*=1e6
    return f'''SetFactory("OpenCASCADE");
Geometry.Tolerance = 1e-10;
Sphere(1) = {{0,0,0,{ro:.17g}}};
Sphere(2) = {{0,0,0,{ri:.17g}}};
// Rotate CAD parameter seams only; spheres and physical geometry are unchanged.
Rotate {{ {{0,1,0}}, {{0,0,0}}, Pi/7 }} {{ Volume{{1,2}}; }}
shell[] = BooleanDifference{{ Volume{{1}}; Delete; }}{{ Volume{{2}}; Delete; }};
Cylinder(3) = {{0,0,0,0,0,{2*ro:.17g},{a:.17g}}};
target[] = BooleanDifference{{ Volume{{shell[]}}; Delete; }}{{ Volume{{3}}; Delete; }};
Physical Volume("target_shell", 1) = {{target[]}};
boundary[] = Boundary{{ Volume{{target[]}}; }};
Physical Surface("unassigned_target_boundary", 2) = {{boundary[]}};
Mesh.CharacteristicLengthMin = {h:.17g};
Mesh.CharacteristicLengthMax = {h:.17g};
Mesh.Algorithm3D = 10;
Mesh.OptimizeNetgen = 1;
Mesh.MshFileVersion = 2.2;
Mesh.ScalingFactor = 1e-6;
'''

def analytic_volume(p):
    """Shell minus the +z cylindrical bore (a < ri)."""
    validate(p)
    ri=p['inner_radius_m']; ro=ri+p['wall_m']; a=p['aperture_radius_m']
    # Remaining volume: entire shell minus its portion inside the +z cylinder.
    return 2*math.pi/3*(ro**3-ri**3+(ro*ro-a*a)**1.5-(ri*ri-a*a)**1.5)

def material_ready(m):
    """Density/boron loading are essential, not inherited from cold pure B11."""
    for k in ('density_kg_m3','boron_mass_fraction','b11_atom_fraction'):
        v=m.get(k)
        if v is None or not isinstance(v,(float,int)) or not math.isfinite(v):
            raise ValueError('unqualified material: '+k)
    if m['density_kg_m3'] <= 0 or not 0 < m['boron_mass_fraction'] <= 1 or not 0 < m['b11_atom_fraction'] <= 1:
        raise ValueError('invalid material')
    for k in ('composition_citation','stopping_dataset','eos_dataset'):
        if not m.get(k): raise ValueError('unqualified material: '+k)
    return True
