"""Static scientific summary; optional matplotlib dependency."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import compare as c

def main():
 rows=c.readcsv(c.OUT/'annual_isotopes.csv')
 fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
 for ax,config,label in zip(axs,['arc_1100_1130','dual_laser_1100_1100'],['ARC-reference source','Laser prescribed-power source']):
  values=[];labels=[]
  for mode,schedule in [('B_replacement_A1','continuous'),('B_replacement_A1','A_90day'),('zero_breeding','A_90day'),('B_replacement_A1','cold_start')]:
   r=next(x for x in rows if x['configuration']==config and x['blanket_mode']==mode and x['schedule']==schedule)
   labels.append(('B replacement' if mode!='zero_breeding' else 'Zero breeding')+'\n'+{'continuous':'Continuous','A_90day':'A off 90 days','cold_start':'Cold startup'}[schedule]);values.append(max(0,float(r['T_unserved_B_burn_kg'])))
  ax.bar(range(4),values,color=['#357a65','#357a65','#bc6b43','#bc6b43']);ax.set_xticks(range(4),labels,fontsize=8);ax.set_title(label);ax.set_ylabel('Unserved B tritium demand (kg)');ax.set_ylim(0,15)
  for j,v in enumerate(values):ax.text(j,v+.2,f'{v:.3f}',ha='center',fontsize=9)
  ax.spines[['top','right']].set_visible(False)
 fig.suptitle('Conditional startup / outage controls\nB replacement TBR=1 is assumed; no physical self-sufficiency claim',fontsize=12)
 fig.savefig(c.OUT/'outage_controls.svg')
if __name__=='__main__':main()
