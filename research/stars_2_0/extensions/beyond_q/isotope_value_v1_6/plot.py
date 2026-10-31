"""Optional scientific figure; requires matplotlib (generated with 3.10.8)."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
rows=list(csv.DictReader((root/'outputs/terminal_allocations.csv').read_text().splitlines()))
r=next(r for r in rows if r['A_case']=='A1' and r['He3_case']=='capture90' and r['reserve_T_kg']=='10.0')
fig,axs=plt.subplots(1,2,figsize=(10,5),layout='constrained')
for ax,title,keys,labels,colors in [
 (axs[0],'He-3: all modeled births', ['He3_mobile_kg','He3_capture_loss_kg','He3_inaccessible_decay_kg','He3_retained_kg','He3_quality_held_kg','He3_terminal_sale_candidate_kg'],['Collection holdup','Capture loss','Inaccessible T-decay He-3','Retained stock','Quality hold (assumed)','Sale candidate (unqualified)'],['#92a8b4','#d48570','#c0bec4','#4a7685','#bfa868','#609b75']),
 (axs[1],'Tritium: remaining terminal inventory',['T_pipeline_held_kg','T_storage_after_sale_kg','T_terminal_sale_candidate_kg'],['Processing / mobile hold','Retained for D-T fuel / reserve','External sale (disabled)'],['#92a8b4','#4a7685','#609b75'])]:
 bottom=0
 for key,label,color in zip(keys,labels,colors):
  value=float(r[key]);ax.bar(0,value,bottom=bottom,label=label,color=color);bottom+=value
 ax.set_title(title);ax.set_ylabel('kg');ax.set_xticks([]);ax.legend(loc='upper left',bbox_to_anchor=(1.01,1),fontsize=8,frameon=False);ax.spines[['top','right']].set_visible(False)
fig.suptitle('A1 staged year — conditional isotope allocation\nPrescribed fusion; assumed collection, recovery and reserves',fontsize=12)
fig.savefig(root/'outputs/isotope_allocation.svg')
