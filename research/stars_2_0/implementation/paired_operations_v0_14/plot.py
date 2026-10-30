import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import tail_models,overlap_probability

def plot(stability,run):
    stability=json.loads(Path(stability).read_text());run=Path(run);result=json.loads((run/'RESULTS.json').read_text())
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(11,4.5))
    dose=np.array(stability['peak_dose_Gy']);x=np.arange(1,len(dose)+1)
    axes[0].plot(x,dose,color='#176e91',lw=.7);axes[0].axhline(dose.mean(),color='#de861a',lw=1)
    axes[0].set(xlabel='Retained observation index',ylabel='Peak dose (Gy)',title=f'Published source: {dose.mean():.2f} +/- {dose.std():.2f} Gy (SD)')
    for idx,c,label in [(1,'#176e91','x centroid'),(3,'#ba543b','y centroid')]:
        y=np.array([r['props'][idx] for r in stability['beam_fit_rows']]);axes[1].plot(x,y-y.mean(),color=c,lw=.8,label=label)
    axes[1].set(xlabel='Retained beam-fit index',ylabel='Centroid minus mean (mrad)',title='Measured pointing variation, including drift');axes[1].legend()
    fig.suptitle('EVIDENCE-CONSTRAINED: reproduced published source stability')
    fig.text(.5,.015,'Streeter et al.2025 / Zenodo14236097. Selected300 records; not all-attempt success, acoustic benefit or fusion output.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.05,1,.93));fig.savefig(run/'EVIDENCE_CONSTRAINED.png',dpi=180);plt.close(fig)
    fig,axes=plt.subplots(1,3,figsize=(13,4.6))
    energy=np.linspace(2.25,8,180)
    for method in ['linear','exponential','power_law']:
        y=np.array([tail_models(float(e))[method] for e in energy]);inside=energy<=4.52
        l,=axes[0].plot(energy[inside],y[inside],lw=1,label=method)
        axes[0].plot(energy[~inside],y[~inside],'--',color=l.get_color(),lw=1)
    axes[0].scatter([2.25,4.52],[.639,.611],color='black',zorder=5,label='Published fit locations')
    axes[0].axvline(7.5,color='#777777',lw=.7);axes[0].set(xlabel='Alpha energy (MeV)',ylabel='Langau location (um)',title='Derived detector-location extrapolation');axes[0].legend(fontsize=8)
    for curve in result['exploratory']['jitter_scenarios']:
        rec=curve['records'];xx=[r['jitter_sigma_ratio'] for r in rec]
        axes[1].plot(xx,[r['empirical_selected_sample_overlap_fraction'] for r in rec],label=f"Window={curve['acceptance_halfwidth_over_reference_SD']:g} reference SD")
    axes[1].set(xlabel='Assumed pointing-jitter scale / reference',ylabel='Selected-sample physical overlap fraction',title='Hypothetical narrowing of measured deviations');axes[1].legend(fontsize=8)
    delay=np.linspace(0,1,100);p0=overlap_probability(1,1);p1=overlap_probability(.5,1)
    for bad in [0.,.2,1.]:
        ratio=(p1+(1-p1)*bad)/(p0+(1-p0)*bad)
        axes[2].plot(delay,ratio/(1+delay),label=f'Outside-window relative energy={bad:g}')
    axes[2].axhline(1,color='black',lw=.7);axes[2].set(xlabel='Extra serial preparation / baseline cycle',ylabel='Energy per time / reference',title='Preparation overhead can offset success gains');axes[2].legend(fontsize=8)
    fig.suptitle('EXPLORATORY POTENTIAL: extrapolation and reliability pathways')
    fig.text(.5,.015,'Dashed detector curves are extrapolated; jitter, physical window and serial-delay models are scenarios. No measured acoustic gain or net electricity.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.06,1,.92));fig.savefig(run/'EXPLORATORY_POTENTIAL.png',dpi=180);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--stability',default='receipts/stability001/STABILITY_DATA.json');p.add_argument('--run',required=True);a=p.parse_args();plot(a.stability,a.run)
