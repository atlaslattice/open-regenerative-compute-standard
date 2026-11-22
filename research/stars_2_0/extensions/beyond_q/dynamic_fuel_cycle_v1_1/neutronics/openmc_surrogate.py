#!/usr/bin/env python3
"""Conditional OpenMC toroidal-shell input generator; NOT V3A engineering geometry.

--preflight works without OpenMC; --export-only exports when dependency exists;
--run executes a research surrogate. No results from this generator were run
in the authoring environment. Geometry/source/material values are assumptions.
Ports are NOT represented: no scalar correction is silently applied to TBR.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import sys

def preflight():
    xs=os.environ.get('OPENMC_CROSS_SECTIONS')
    exists=bool(xs and Path(xs).is_file())
    return dict(python_package=bool(importlib.util.find_spec('openmc')),
                executable=shutil.which('openmc'),cross_sections_xml=xs,
                cross_sections_exists=exists,
                cross_sections_sha256=hashlib.sha256(Path(xs).read_bytes()).hexdigest() if exists else None,
                status='BLOCKED' if not (importlib.util.find_spec('openmc') and shutil.which('openmc') and exists) else 'DEPENDENCIES_PRESENT; data coverage/geometry still require review')

def main():
    p=argparse.ArgumentParser();p.add_argument('--preflight',action='store_true')
    p.add_argument('--export-only',action='store_true');p.add_argument('--run',action='store_true')
    p.add_argument('--li6',type=float,default=.075);p.add_argument('--blanket-cm',type=float,default=90.)
    p.add_argument('--source',choices=['B','A_legacy18'],default='B')
    p.add_argument('--alloy',choices=['inconel_surrogate','vanadium_4cr4ti','eurofer_surrogate'],default='inconel_surrogate')
    p.add_argument('--output',type=Path,default=Path('openmc_surrogate_run'))
    args=p.parse_args();check=preflight();print(json.dumps(check,indent=2))
    if args.preflight:return
    if not (args.export_only or args.run):p.error('choose --preflight, --export-only or --run')
    if not 0<=args.li6<=1 or not 0<args.blanket_cm<=150:p.error('invalid surrogate dimensions/composition')
    if check['status']=='BLOCKED':raise SystemExit('BLOCKED: install OpenMC Python API/executable and configure real HDF5 cross sections; no transport results produced')
    import openmc
    def mat(name,density,composition,kind='ao'):
        m=openmc.Material(name=name);m.set_density('g/cm3',density)
        for e,v in composition.items():
            if any(c.isdigit() for c in e):m.add_nuclide(e,v,percent_type=kind)
            else:m.add_element(e,v,percent_type=kind)
        return m
    salt=mat('ASSUMED Li2BeF4 rho=1.94',1.94,{'Li6':2*args.li6,'Li7':2*(1-args.li6),'Be9':1,'F19':4})
    tungsten=mat('W armour',19.3,{'W':1})
    alloy_data={
      'inconel_surrogate':(8.19,{'Ni':.53,'Cr':.19,'Fe':.18,'Nb':.05,'Mo':.03,'Ti':.01,'Al':.01}),
      'vanadium_4cr4ti':(6.1,{'V':.92,'Cr':.04,'Ti':.04}),
      'eurofer_surrogate':(7.8,{'Fe':.895,'Cr':.09,'W':.01,'V':.005})}
    density,comp=alloy_data[args.alloy];alloy=mat('ASSUMED '+args.alloy,density,comp,'wo')
    be=mat('Be multiplier',1.85,{'Be9':1})
    steel=mat('ASSUMED SS316 surrogate',8.,{'Fe':.66,'Cr':.17,'Ni':.12,'Mo':.03,'Mn':.02},'wo')
    shield=mat('ASSUMED B4C shield surrogate',2.52,{'B':4,'C':1})
    # Major/minor radii approximate published plasma basis only; circular shells
    # do not reproduce shaping, divertor, ports, supports or licensed shielding.
    R=462.;radius=118.
    boundaries=[openmc.ZTorus(a=R,b=radius,c=radius,name='plasma envelope')]
    layers=[('W',.3,tungsten),('inner structure',1.,alloy),('channel',2.,salt),
            ('Be multiplier',1.,be),('outer structure',3.,alloy),
            ('blanket',args.blanket_cm,salt),('tank',3.,steel),('shield',25.,shield)]
    cells=[openmc.Cell(name='source void',region=-boundaries[0])]
    breeder_cells=[]
    for name,width,material in layers:
        radius+=width
        surface=openmc.ZTorus(a=R,b=radius,c=radius,name=name+' outer')
        cell=openmc.Cell(name=name,fill=material,region=+boundaries[-1]&-surface)
        cells.append(cell);boundaries.append(surface)
        if material is salt:breeder_cells.append(cell)
    outer=openmc.Sphere(r=1000,boundary_type='vacuum')
    cells.append(openmc.Cell(name='outer void',region=+boundaries[-1]&-outer))
    geometry=openmc.Geometry(cells)
    settings=openmc.Settings();settings.run_mode='fixed source';settings.batches=50
    settings.particles=20000;settings.seed=119
    space=openmc.stats.CylindricalIndependent(openmc.stats.Discrete([R],[1]),
             openmc.stats.Uniform(0,2*math.pi),openmc.stats.Discrete([0],[1]))
    energy=openmc.stats.Discrete([14.1e6],[1]) if args.source=='B' else openmc.stats.Discrete([2.45e6,14.1e6],[.728,.272])
    settings.source=openmc.IndependentSource(space=space,angle=openmc.stats.Isotropic(),energy=energy)
    production=openmc.Tally(name='Li tritium births per source neutron')
    production.filters=[openmc.CellFilter(breeder_cells)]
    production.nuclides=['Li6','Li7'];production.scores=['H3-production']
    heat=openmc.Tally(name='neutron-only local heat eV per source; NOT extra fusion Q')
    heat.filters=[openmc.CellFilter(cells[:-1])];heat.scores=['heating-local']
    leakage=openmc.Tally(name='outer leakage per source')
    leakage.filters=[openmc.SurfaceFilter(outer)];leakage.scores=['current']
    fast=openmc.Tally(name='outer shield fast tracklength; not flux without volume')
    fast.filters=[openmc.CellFilter(cells[-2]),openmc.EnergyFilter([1e5,20e6])];fast.scores=['flux']
    model=openmc.Model(geometry=geometry,materials=openmc.Materials([salt,tungsten,alloy,be,steel,shield]),
                       settings=settings,tallies=openmc.Tallies([production,heat,leakage,fast]))
    args.output.mkdir(parents=True,exist_ok=True)
    model.export_to_xml(directory=args.output)
    metadata=dict(scope='ASSUMED axisymmetric toroidal surrogate; NOT V3A',openmc_version=openmc.__version__,
                  input_args={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
                  dependencies=check,ports='ABSENT; G2 remains open',
                  data_hdf5_hashes='REQUIRED before quantitative publication; XML hash alone insufficient',
                  materials='Simplified assumed compositions; not qualified alloy specifications')
    (args.output/'provenance.json').write_text(json.dumps(metadata,indent=2)+'\n')
    if args.run:model.run(cwd=args.output)

if __name__=='__main__':main()
