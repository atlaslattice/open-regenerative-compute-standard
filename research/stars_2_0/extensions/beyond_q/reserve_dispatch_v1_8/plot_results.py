"""Scientific dispatch comparison; optional matplotlib dependency."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import run as r

def main():
    rows=r.paired.readcsv(r.OUT/'annual_dispatch.csv');stocks=r.paired.readcsv(r.OUT/'weekly_stocks.csv')
    policies=['always_on','reserve_only','reserve_He3_10k','reserve_He3_100k','reserve_He3_500k']
    labels=['Always on','Reserve only','He3 10k L/y','He3 100k L/y','He3 500k L/y']
    hours=[sum(float(x['A_on_hours']) for x in rows if x['policy']==p and float(x['B_gross_TBR_assumed'])==1) for p in policies]
    fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
    axs[0].barh(labels,hours,color=['#6f8ca1','#467b61','#467b61','#467b61','#b68555']);axs[0].invert_yaxis();axs[0].set_xlabel('A operating hours, startup + three model years')
    for j,h in enumerate(hours):axs[0].text(h+200,j,f'{h:,.0f}',va='center',fontsize=9)
    axs[0].set_xlim(0,31000)
    for p,label in zip(policies,labels):
        points=[x for x in stocks if x['policy']==p and float(x['B_gross_TBR_assumed'])==1]
        axs[1].plot([float(x['time_hours'])/8766 for x in points],[float(x['T_B_storage_kg']) for x in points],label=label)
    axs[1].axhline(10,color='#555',ls=':',lw=1);axs[1].axhline(20,color='#555',ls=':',lw=1);axs[1].set_xlabel('Elapsed model years');axs[1].set_ylabel('B stored T (kg)');axs[1].legend(fontsize=8,frameon=False)
    for ax in axs:ax.spines[['top','right']].set_visible(False)
    fig.suptitle('Conditional reserve / isotope-production dispatch\nAssumed B TBR=1; A blanket=0; no certified product or physical validation',fontsize=12)
    fig.savefig(r.OUT/'dispatch.svg')
if __name__=='__main__':main()
