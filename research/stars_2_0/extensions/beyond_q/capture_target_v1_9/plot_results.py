"""Conditional tritium birth/use accounting. Optional matplotlib."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import run as r

def main():
    x=next(x for x in r.paired.readcsv(r.OUT/'annual_dispatch.csv') if x['policy']=='captured350k_atom_equivalent' and float(x['B_gross_TBR_assumed'])==1 and x['year']=='1')
    fig,ax=plt.subplots(figsize=(9,5.5),layout='constrained')
    bars=[(0,[('DD T birth',float(x['T_DD_birth_kg']),'#467997'),('B blanket birth (assumed)',float(x['T_B_blanket_birth_kg']),'#8cacc0')]),
          (1,[('A internal DT burn',float(x['T_A_burn_kg']),'#a2735b'),('B DT burn',float(x['T_B_burn_kg']),'#d0a88f'),('Decay / processing / permeation',sum(float(x[k]) for k in ['T_decay_kg','T_process_loss_kg','T_permeation_kg']),'#ac9b6d'),('Retained stock growth',float(x['T_stock_change_kg']),'#54836a')])]
    for pos,segments in bars:
        bottom=0
        for label,value,color in segments:
            ax.bar(pos,value,bottom=bottom,color=color,label=label,width=.5)
            if value>4:ax.text(pos,bottom+value/2,f'{value:.2f} kg',ha='center',va='center',fontsize=10,color='white' if color in ('#467997','#54836a') else '#222')
            bottom+=value
    ax.set_xticks([0,1],['T births','T consumed, lost or retained']);ax.set_ylabel('Tritium kg in operating year 1');ax.set_title('350k L total-capture targets: conditional tritium ledger\nB continuously scheduled; gross B TBR=1 assumed; no T sales')
    ax.legend(loc='upper left',bbox_to_anchor=(1.02,1),frameon=False,fontsize=9);ax.spines[['top','right']].set_visible(False)
    fig.savefig(r.OUT/'tritium_350k.svg')
if __name__=='__main__':main()
