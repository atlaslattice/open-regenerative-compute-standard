"""OpenMC method QA with synthetic one-group pure absorber, not breeding data.

Unit sphere, centered isotropic source, Sigma_a=Sigma_t=1/cm, no scatter:
leakage=exp(-1), absorption=1-exp(-1). No tritium response is defined.
"""
import argparse,json,math,subprocess
from pathlib import Path
import numpy as np

def main():
    import openmc,openmc.mgxs
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--executable',required=True);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    groups=openmc.mgxs.EnergyGroups([0.,20e6])
    xs=openmc.XSdata('synthetic_absorber',groups);xs.order=0
    xs.set_total(np.array([1.]));xs.set_absorption(np.array([1.]))
    xs.set_scatter_matrix(np.zeros((1,1,1)))
    library=openmc.MGXSLibrary(groups);library.add_xsdata(xs)
    library.export_to_hdf5(a.output/'synthetic_mgxs.h5')
    material=openmc.Material(name='SYNTHETIC QA ONLY');material.set_density('macro',1.)
    material.add_macroscopic('synthetic_absorber')
    materials=openmc.Materials([material]);materials.cross_sections=str((a.output/'synthetic_mgxs.h5').resolve())
    surface=openmc.Sphere(r=1,boundary_type='vacuum');cell=openmc.Cell(fill=material,region=-surface)
    settings=openmc.Settings();settings.run_mode='fixed source';settings.energy_mode='multi-group'
    settings.batches=50;settings.particles=4000;settings.seed=3119
    settings.source=openmc.IndependentSource(space=openmc.stats.Point((0,0,0)),energy=openmc.stats.Discrete([14.1e6],[1.]))
    absorb=openmc.Tally(name='absorption');absorb.scores=['absorption'];absorb.estimator='analog'
    leak=openmc.Tally(name='leakage');leak.scores=['current'];leak.filters=[openmc.SurfaceFilter(surface)]
    model=openmc.Model(geometry=openmc.Geometry([cell]),materials=materials,settings=settings,tallies=openmc.Tallies([absorb,leak]))
    model.export_to_xml(directory=a.output)
    p=subprocess.run([str(Path(a.executable).resolve()),'-s','2'],cwd=a.output,text=True,capture_output=True)
    (a.output/'stdout.txt').write_text(p.stdout);(a.output/'stderr.txt').write_text(p.stderr)
    if p.returncode:raise RuntimeError(p.stderr)
    with openmc.StatePoint(a.output/'statepoint.50.h5',autolink=False) as sp:
        l=sp.get_tally(name='leakage');b=sp.get_tally(name='absorption')
        lm=float(l.mean.item());ls=float(l.std_dev.item());bm=float(b.mean.item())
        r=dict(kind='ACTUAL OPENMC METHOD QA / SYNTHETIC MACROSCOPIC DATA / NOT A BREEDING RESULT',
            expected_leakage=math.exp(-1),leakage=lm,leakage_standard_error=ls,
            absorption=bm,particle_residual=1-lm-bm,
            passes_4se=abs(lm-math.exp(-1))<=4*ls,
            input_source_energy_eV=14.1e6,
            energy_partition_qa='For this no-Q, no-scatter toy: E0*absorbed+E0*leaked=E0; not material kerma validation',
            source_energy_partition_residual_eV=14.1e6*(1-lm-bm))
    (a.output/'benchmark_result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))

if __name__=='__main__':main()
