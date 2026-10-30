"""OpenMC fixed-source spherical-shell research testbed, NOT ARC V3A.

All dimensions/compositions are explicit surrogate assumptions. FENDL data
are 293.6 K; no molten-salt operating-temperature qualification is claimed.
Each run launches one neutron per source history, independently for DD/DT.
"""
import argparse,hashlib,json,math,os,platform,subprocess
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def case(li6=.075,source='DT',alloy='inconel_surrogate',blanket_cm=90.,
         port_fraction=0.,multiplier=True,structure_scale=1.,nonbreeder=False,
         vacuum=False,seed=119,particles=2000,batches=30):
    if source not in ('DD','DT') or not 0<=li6<=1 or not 0<=port_fraction<.5:
        raise ValueError('invalid source/composition/coverage')
    if min(blanket_cm,structure_scale,particles,batches)<=0:raise ValueError('invalid positive input')
    return dict(schema='beyond-q-transport-1.2',geometry='spherical_shell_testbed',
        geometry_evidence='ASSUMED: NOT ARC V3A',li6=li6,source=source,alloy=alloy,
        blanket_cm=blanket_cm,port_fraction=port_fraction,multiplier=multiplier,
        structure_scale=structure_scale,nonbreeder=nonbreeder,vacuum=vacuum,
        temperature_K=293.6,salt_density_g_cm3=1.94,seed=seed,particles=particles,batches=batches,
        cavity_cm=100.,first_wall_cm=.3,inner_structure_cm=1.,coolant_cm=2.,
        multiplier_cm=1.,outer_structure_cm=3.,tank_cm=3.,shield_cm=25.,probe_cm=5.)

def build(c,xs):
    import openmc
    openmc.reset_auto_ids()
    def material(name,rho,comp,kind='wo'):
        m=openmc.Material(name=name,temperature=c['temperature_K']);m.set_density('g/cm3',rho)
        for nuclide,v in comp.items():
            if v<=0:continue
            if any(ch.isdigit() for ch in nuclide):m.add_nuclide(nuclide,v,percent_type=kind)
            else:m.add_element(nuclide,v,percent_type=kind)
        return m
    compositions={
     'inconel_surrogate':(8.19,{'Ni':.53,'Cr':.19,'Fe':.18,'Nb':.05,'Mo':.03,'Ti':.01,'Al':.01}),
     'eurofer_surrogate':(7.8,{'Fe':.895,'Cr':.09,'W':.01,'V':.005}),
     'vanadium_4cr4ti':(6.1,{'V':.92,'Cr':.04,'Ti':.04})}
    rho,comp=compositions[c['alloy']]
    steel=material('ASSUMED major-element '+c['alloy'],rho,comp)
    w=material('W',19.3,{'W':1})
    be=material('Be multiplier',1.85,{'Be9':1},'ao')
    shield=material('B4C nonbreeding shield',2.52,{'B':4,'C':1},'ao')
    salt=material('ASSUMED FLiBe',c['salt_density_g_cm3'],{'Li6':2*c['li6'],'Li7':2*(1-c['li6']),'Be9':1,'F19':4},'ao')
    tank=material('ASSUMED SS316 major elements',8.,{'Fe':.66,'Cr':.17,'Ni':.12,'Mo':.03,'Mn':.02})
    salt_fill=shield if c['nonbreeder'] else salt
    r=c['cavity_cm'];inner=openmc.Sphere(r=r,name='source cavity')
    cells=[openmc.Cell(name='source void',region=-inner)]
    layers=[('armour',c['first_wall_cm'],w),('inner_structure',c['inner_structure_cm']*c['structure_scale'],steel),
        ('coolant_channel',c['coolant_cm'],None if c['nonbreeder'] else salt),
        ('multiplier',c['multiplier_cm'],be if c['multiplier'] else None),
        ('outer_structure',c['outer_structure_cm']*c['structure_scale'],steel),
        ('blanket',c['blanket_cm'],salt_fill),('tank',c['tank_cm'],tank),('shield',c['shield_cm'],shield)]
    hole=None
    if c['port_fraction']:
        # Explicit polar void cone: solid-angle fraction f=(1-cos(theta))/2.
        theta=math.acos(1-2*c['port_fraction'])
        hole=-openmc.ZCone(r2=math.tan(theta)**2)&+openmc.ZPlane(z0=0)
    previous=inner;salt_cells=[]
    for name,width,fill in layers:
        r+=width;surface=openmc.Sphere(r=r)
        region=+previous&-surface
        if hole is not None:region &= ~hole
        cell=openmc.Cell(name=name,region=region,fill=None if c['vacuum'] else fill)
        cells.append(cell)
        if fill is salt and not c['vacuum']:salt_cells.append(cell)
        previous=surface
    if hole is not None:cells.append(openmc.Cell(name='explicit penetration void',region=hole&+inner&-previous))
    probe_inner=r;r+=c['probe_cm'];outer=openmc.Sphere(r=r,boundary_type='vacuum')
    probe=openmc.Cell(name='magnet-facing probe void',region=+previous&-outer);cells.append(probe)
    probe_volume=4*math.pi/3*(r**3-probe_inner**3)
    mats=openmc.Materials(list({cell.fill.id:cell.fill for cell in cells if cell.fill is not None}.values()))
    mats.cross_sections=str(Path(xs).resolve())
    settings=openmc.Settings();settings.run_mode='fixed source';settings.batches=c['batches']
    settings.particles=c['particles'];settings.seed=c['seed'];settings.photon_transport=False
    settings.temperature={'default':c['temperature_K'],'method':'nearest','tolerance':1.}
    energy=2.45e6 if c['source']=='DD' else 14.1e6
    settings.source=openmc.IndependentSource(space=openmc.stats.Point((0,0,0)),
        angle=openmc.stats.Isotropic(),energy=openmc.stats.Discrete([energy],[1.]))
    settings.statepoint={'batches':[c['batches']]}
    tallies=[]
    for estimator in ('tracklength','collision'):
        t=openmc.Tally(name='salt_T_'+estimator);t.scores=['H3-production'];t.estimator=estimator
        # If no salt exists, global production is reported separately, not misclassified as Li breeding.
        t.filters=[openmc.CellFilter(salt_cells)] if salt_cells else [openmc.CellFilter(cells[0])]
        tallies.append(t)
    if salt_cells:
        for nuclide in (['Li6'] if c['li6']==1 else ['Li7'] if c['li6']==0 else ['Li6','Li7']):
            t=openmc.Tally(name=nuclide+'_T');t.nuclides=[nuclide];t.scores=['H3-production']
            t.filters=[openmc.CellFilter(salt_cells)];tallies.append(t)
    for name,scores in [('global_balance',['absorption','scatter','nu-scatter']),('global_heat',['heating']),('global_T',['H3-production'])]:
        t=openmc.Tally(name=name);t.scores=scores;tallies.append(t)
    t=openmc.Tally(name='leakage');t.filters=[openmc.SurfaceFilter(outer)];t.scores=['current'];tallies.append(t)
    t=openmc.Tally(name='probe_flux');t.filters=[openmc.CellFilter(probe),openmc.EnergyFilter([0,1e5,20e6])];t.scores=['flux'];tallies.append(t)
    model=openmc.Model(geometry=openmc.Geometry(cells),materials=mats,settings=settings,tallies=openmc.Tallies(tallies))
    return model,dict(probe_volume_cm3=probe_volume,source_energy_eV=energy,
        normalization='per unit source neutron; B=1 neutron/DT event; A DD=0.5 neutron/primary DD event at equal branches',
        neutron_heating='MT301 kerma heating (not local photon transport); full deposited heat/energy closure UNRESOLVED',
        all_material_definitions=[dict(m.to_xml_element().attrib)|{'xml':__import__('lxml').etree.tostring(m.to_xml_element()).decode()} for m in mats])

def run(c,xs,directory,executable='openmc'):
    import openmc
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    model,metadata=build(c,xs);model.export_to_xml(directory=directory)
    (directory/'case.json').write_text(json.dumps(c,indent=2)+'\n')
    data_manifest=Path(xs).parent/'data_manifest.json'
    provenance=dict(case=c,metadata=metadata,openmc_version=openmc.__version__,python=platform.python_version(),
        platform=platform.platform(),executable_sha256=sha(executable),data_manifest_sha256=sha(data_manifest),
        input_hashes={x.name:sha(x) for x in directory.glob('*.xml')},
        geometry_qualified=False,physical_validation=False)
    (directory/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    process=subprocess.run([str(Path(executable).resolve()),'-s','2'],cwd=directory,text=True,capture_output=True,
        env=dict(os.environ,OPENMC_CROSS_SECTIONS=str(Path(xs).resolve()),OMP_NUM_THREADS='2'))
    (directory/'stdout.txt').write_text(process.stdout);(directory/'stderr.txt').write_text(process.stderr)
    if process.returncode:raise RuntimeError(f'OpenMC failed in {directory}: '+process.stderr[-1200:])
    return process_result(directory)

def process_result(directory):
    import openmc
    directory=Path(directory);c=json.loads((directory/'case.json').read_text());raw={};flat={}
    sp_path=directory/f"statepoint.{c['batches']}.h5"
    with openmc.StatePoint(sp_path,autolink=False) as sp:
        for tally in sp.tallies.values():
            raw[tally.name]=dict(scores=tally.scores,nuclides=tally.nuclides,estimator=tally.estimator,
                mean=tally.mean.tolist(),std_dev=tally.std_dev.tolist(),sum=tally.sum.tolist(),sum_sq=tally.sum_sq.tolist(),
                n_realizations=int(tally.num_realizations))
            # Scalar aggregation uses covariance-conservative sum of marginal SEs,
            # not quadrature pretending cell tallies are independent.
            for score in tally.scores:
                canonical='H3-production' if score=='(n,Xt)' else score
                flat[tally.name+':'+canonical]=dict(mean=float(tally.get_values(scores=[score]).sum()),
                    se_bound=float(tally.get_values(scores=[score],value='std_dev').sum()))
    get=lambda key:flat[key]['mean']
    balance=1+get('global_balance:nu-scatter')-get('global_balance:scatter')-get('global_balance:absorption')-get('leakage:current')
    bound=sum(flat[k]['se_bound'] for k in ['global_balance:nu-scatter','global_balance:scatter','global_balance:absorption','leakage:current'])
    a=flat['salt_T_tracklength:H3-production'];b=flat['salt_T_collision:H3-production']
    estimator_difference=abs(a['mean']-b['mean']);estimator_bound=3*(a['se_bound']+b['se_bound'])
    result=dict(schema='beyond-q-transport-result-1.2',kind='ACTUAL_OPENMC_TRANSPORT_IN_ASSUMED_GEOMETRY',
        case=c,tallies=flat,neutron_balance_residual=balance,neutron_balance_se_bound=bound,
        particle_balance_pass=abs(balance)<=max(5*bound,1e-10),
        estimator_difference=estimator_difference,estimator_3se_bound=estimator_bound,
        estimators_agree=estimator_difference<=max(estimator_bound,1e-10),
        statepoint_sha256=sha(sp_path),provenance_sha256=sha(directory/'provenance.json'),
        geometry_qualified=False,energy_closure='UNRESOLVED for material runs; vacuum analytic check separate',
        qualified_usable_surplus_kg=None,physical_validation=False)
    (directory/'raw_tallies.json').write_text(json.dumps(raw,indent=2)+'\n')
    (directory/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--xs',required=True);p.add_argument('--executable',required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--source',choices=['DD','DT'],default='DT')
    args=p.parse_args();print(json.dumps(run(case(source=args.source),args.xs,args.output,args.executable),indent=2))
