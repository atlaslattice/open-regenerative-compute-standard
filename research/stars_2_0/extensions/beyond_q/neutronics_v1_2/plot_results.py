"""Reproducible standalone scientific plots from actual/conditional CSVs."""
from pathlib import Path
import argparse,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--qa-png',type=Path);a=p.parse_args()
    plt.rcParams['svg.hashsalt']='beyond-q-v1.2'
    rows=list(csv.DictReader((ROOT/'outputs/transport_summary.csv').open()))
    f,axes=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
    for axis,source in zip(axes,('DD','DT')):
        for cm in (60,90,120):
            values=[r for r in rows if r['case_id'].startswith(source+'_Li') and float(r['blanket_cm'])==cm and r['case_id'].endswith('cm'+str(cm))]
            values.sort(key=lambda r:float(r['li6']))
            axis.errorbar([100*float(r['li6']) for r in values],[float(r['T_per_source_neutron']) for r in values],
                yerr=[float(r['T_se_bound']) for r in values],marker='o',capsize=3,label=f'{cm} cm')
        axis.set(xlabel='Li-6 atom fraction (%)',ylabel='Salt T atoms / source neutron',title=source+' source')
        axis.grid(alpha=.2);axis.legend(title='Blanket thickness',fontsize=8)
    f.suptitle('Actual OpenMC in an assumed spherical testbed — not ARC validation',fontsize=11)
    f.savefig(ROOT/'outputs/transport_comparison.svg',metadata={'Date':None})
    if a.qa_png:f.savefig(a.qa_png,dpi=120)
    plt.close(f)
    f,axes=plt.subplots(2,1,figsize=(9,7),layout='constrained')
    for label in ['A0','A1','A2_grid_candidate']:
        rows=list(csv.DictReader((ROOT/f'outputs/{label}_daily.csv').open()))
        axes[0].plot([float(r['day']) for r in rows],[float(r['total_inventory']) for r in rows],label=label)
        axes[1].plot([float(r['day']) for r in rows],[float(r['b_store']) for r in rows],label=label)
    axes[0].set(ylabel='Mobile fuel inventory (kg-T)',title='Conditional fuel-cycle integration; all qualified-surplus fields unresolved')
    axes[1].set(xlabel='Calendar days',ylabel='B available storage (kg-T)')
    for ax in axes:ax.legend();ax.grid(alpha=.2)
    f.savefig(ROOT/'outputs/inventory_trajectories.svg',metadata={'Date':None});plt.close(f)

if __name__=='__main__':main()
