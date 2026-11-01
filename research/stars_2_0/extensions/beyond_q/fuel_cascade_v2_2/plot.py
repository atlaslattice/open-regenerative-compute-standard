"""Optional standalone scientific figures: requires matplotlib."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
rows=list(csv.DictReader((ROOT/'outputs/annual_finance.csv').open()))
fig,axs=plt.subplots(1,2,figsize=(12,4.6),constrained_layout=True)
colors={'strict_unresolved':'#8a5361','sequential_predecessors':'#247a73','eligible_pool':'#335d98','fixed_calendar':'#9a7b38'}
for name,color in colors.items():
    selected=[r for r in rows if r['scenario']==name and float(r['He3_overall_recovery_assumed'])==.375
              and r['price_case']=='requested_1500' and r['offtake_case']=='full_offtake_sensitivity']
    years=[float(r['year']) for r in selected]
    axs[0].step(years,[float(r['active_modules']) for r in selected],where='post',label=name,color=color)
    axs[1].plot(years,[float(r['electricity_net_MWh'])/1e6 for r in selected],label=name,color=color)
axs[0].set_title('Operating campuses: policy comparison');axs[0].set_ylabel('Campus count')
axs[1].set_title('Annual net electricity under assumed plant draws');axs[1].set_ylabel('TWh/year')
for ax in axs:ax.set_xlabel('Calendar year');ax.grid(alpha=.2)
axs[0].legend(fontsize=8)
fig.suptitle('Beyond Q v2.2 — conditional rollout, NOT a forecast\n3-year construction; 1-year operating window; capacity 50; G1–G5 OPEN',fontsize=12)
fig.savefig(ROOT/'outputs/rollout_comparison.png',dpi=150)
fig.savefig(ROOT/'outputs/rollout_comparison.svg')
