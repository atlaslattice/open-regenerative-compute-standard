"""Recreate inspection figures from the extracted packages."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def plot(root):
    root=Path(root)
    he=json.loads((root/'HELIUM_S3.json').read_text())
    nuclear=json.loads((root/'KUHLWEIN_FIG3.json').read_text())
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(2,2,figsize=(10,7))
    for ax,p in zip(axes.flat,he['records']):
        b=[b for b in p['bins'] if b['approx_display_count'] is not None]
        x=np.array([(q['left_um']+q['right_um'])/2 for q in b]);y=[q['approx_display_count'] for q in b]
        ax.bar(x,y,width=.024,color='#247cad',label='Recovered visible blue bars')
        ax.axvline(p['mu_um'],color='#d36118',lw=1,label='Published Langau location')
        ax.set(title=f"He {p['E_MeV']:.2f} +/- {p['reported_interval_MeV']:.2f} MeV",xlabel='Pit diameter (um)',ylabel='Approximate displayed counts',xlim=(.4,1.6))
        if p['E_MeV']>3:ax.text(.98,.78,'Includes sputtered-ion population',ha='right',transform=ax.transAxes,fontsize=8)
    axes[0,0].legend(fontsize=8)
    fig.suptitle('Schollmeier 2023, Supplement Figure S3: published experimental histograms')
    fig.text(.5,.015,'Raster extraction; unresolved bins omitted, not zero. Fit location is not the histogram mean. No absolute efficiency.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.045,1,.95));fig.savefig(root/'helium_recovery.png',dpi=170);plt.close(fig)
    fig,axes=plt.subplots(1,3,figsize=(12,4),sharey=True)
    for ax,panel,label in zip(axes,['l1','l3','mixture'],['l = 1','l = 3','Coherent mixture']):
        for role,color,label2 in [('data','#222222','Published experimental trace'),('published_model','#e67e22','Published model trace')]:
            t=next(t for t in nuclear['traces'] if t['panel']==panel and t['role']==role)
            ax.plot(t['energy_cm_MeV'],t['relative_display_height'],color=color,label=label2)
        ax.set(title=label,xlabel='Alpha energy in CM (MeV)',xlim=(0,6))
    axes[0].set_ylabel('Relative figure height');axes[0].legend(fontsize=8)
    fig.suptitle('Kuhlwein 2022 Figure 3: recovered PDF vector paths')
    fig.text(.5,.015,'Same experimental data in all panels; projections of published Dalitz fits. No new fit or independent validation.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.06,1,.93));fig.savefig(root/'kuhlwein_recovery.png',dpi=170);plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--run',default='receipts/run001');a=p.parse_args();plot(a.run)
