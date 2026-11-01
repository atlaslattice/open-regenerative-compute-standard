"""Build geometry bindings and, optionally, execute Gmsh. Never predicts yield."""
import argparse, hashlib, importlib.metadata, json, platform, random, sys
from pathlib import Path
from geometry import validate, inside, warpx_mask, gmsh_geo, analytic_volume, material_ready

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--profiles',default=str(Path(__file__).with_name('PROFILES.json')))
    a.add_argument('--out',required=True)
    a.add_argument('--mesh',action='store_true')
    args=a.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=False)
    profiles=json.loads(Path(args.profiles).read_text()); receipt={'python':sys.version,'platform':platform.platform(),'profiles_sha256':hashlib.sha256(Path(args.profiles).read_bytes()).hexdigest(),'results':[],'actual_apparatus_net_power_W':None}
    for p in profiles['geometry_profiles']:
        validate(p); d=out/p['id']; d.mkdir()
        h=p['wall_m']/2 # Numerical meshing choice, not a material observation.
        (d/'target.geo').write_text(gmsh_geo(p,h))
        binding={'units':'m','axis_convention':'entrance along +z','mask':warpx_mask(p),'density_per_m3':None,'material':profiles['ceramic_material'],'status':'GEOMETRY_ONLY_NOT_A_RUNNABLE_PHYSICS_DECK','no_legacy_column_bank_reinterpretation':True}
        (d/'WARPX_GEOMETRY.json').write_text(json.dumps(binding,indent=2)+'\n')
        r={'profile':p['id'],'geometry_evidence':p['evidence'],'analytic_volume_m3':analytic_volume(p),'material_gate':'BLOCKED_UNQUALIFIED','mesh_executed':False}
        try: material_ready(profiles['ceramic_material'])
        except ValueError as e: r['material_gate_reason']=str(e)
        else: raise RuntimeError('default ceramic material unexpectedly qualified')
        if args.mesh:
            import gmsh
            import numpy as np
            gmsh.initialize(); gmsh.option.setNumber('General.Terminal',0)
            try:
                gmsh.open(str(d/'target.geo')); vols=gmsh.model.getEntities(3)
                cad_volume=sum(gmsh.model.occ.getMass(dim,tag) for dim,tag in vols)*1e-18
                rng=random.Random(20261101)
                extent=p['inner_radius_m']+p['wall_m']
                mismatches=0
                for _ in range(1000):
                    xyz=[rng.uniform(-extent,extent) for _ in range(3)]
                    cad_inside=any(gmsh.model.isInside(dim,tag,[x*1e6 for x in xyz])>0 for dim,tag in vols)
                    mismatches+=int(cad_inside != inside(p,*xyz))
                if mismatches: raise RuntimeError('CAD and PIC mask disagree')
                gmsh.model.mesh.generate(3)
                gmsh.write(str(d/'target.msh'))
                types,tags,nodes=gmsh.model.mesh.getElements(3)
                count=sum(len(t) for t in tags)
                if count == 0: raise RuntimeError('empty volume mesh')
                qualities=gmsh.model.mesh.getElementQualities(np.concatenate(tags),'minSJ')
                if min(qualities)<=0: raise RuntimeError('inverted mesh')
                shape_quality=gmsh.model.mesh.getElementQualities(np.concatenate(tags),'minSICN')
                quality_gate='PASS_NUMERICAL_MESH_ONLY' if min(shape_quality) >= .01 else 'BLOCKED_SLIVER_ELEMENTS'
                mesh_volume=float(sum(gmsh.model.mesh.getElementQualities(np.concatenate(tags),'volume')))*1e-18
                mesh_error=abs(mesh_volume/r['analytic_volume_m3']-1)
                if mesh_error > .02: raise RuntimeError('mesh volume error exceeds numerical2% gate')
                cad_error=abs(cad_volume/r['analytic_volume_m3']-1)
                if cad_error > 1e-5: raise RuntimeError('CAD/analytic volume mismatch')
                r.update(mesh_executed=True,mesh_gate=quality_gate,classification_fixture_seed=20261101,CAD_mask_comparison_points=1000,CAD_mask_mismatches=mismatches,gmsh_version=gmsh.__version__,gmsh_distribution=importlib.metadata.version('gmsh'),volume_elements=count,min_scaled_jacobian=float(min(qualities)),min_inverse_condition_number=float(min(shape_quality)),mesh_volume_m3=mesh_volume,mesh_relative_error=mesh_error,cad_volume_m3=cad_volume,cad_relative_error=cad_error)
                gmsh.model.add('readback'); gmsh.merge(str(d/'target.msh'))
                _,coords,_=gmsh.model.mesh.getNodes()
                max_radius=float(np.linalg.norm(np.asarray(coords).reshape(-1,3),axis=1).max())
                if abs(max_radius/extent-1) > .001: raise RuntimeError('mesh SI export scale mismatch')
                r.update(cad_length_unit_m=1e-6,exported_mesh_length_unit_m=1.0,exported_max_radius_m=max_radius)
            finally: gmsh.finalize()
        receipt['results'].append(r)
    receipt['files_sha256']={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.rglob('*')) if p.is_file()}
    receipt['implementation_sha256']={n:hashlib.sha256(Path(__file__).with_name(n).read_bytes()).hexdigest() for n in ('run.py','geometry.py')}
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': main()
