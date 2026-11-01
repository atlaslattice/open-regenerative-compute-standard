"""Optional scientific figure: python plot.py (requires matplotlib)."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
rows=list(csv.DictReader((ROOT/'outputs/annual_products_finance.csv').open()))
fig,axs=plt.subplots(2,2,figsize=(12,8),constrained_layout=True)
def selected(frac):
    return [r for r in rows if float(r['fleet_modules'])==1 and float(r['He3_overall_recovery_assumed'])==frac
            and r['price_case']=='requested_prices' and r['offtake_case']=='fleet_cap_stress']
for frac,color in [(.375,'#aa6441'),(.75,'#247a73'),(.9,'#375c91')]:
    rs=selected(frac);years=[float(r['year']) for r in rs]
    axs[0,0].plot(years,[float(r['He3_product_candidate_STP_L'])/1e3 for r in rs],label=f'{100*frac:g}% overall recovery',color=color)
    axs[1,1].plot(years,[float(r['revenue_less_known_charges_USD'])/1e6 for r in rs],label=f'{100*frac:g}%',color=color)
base=selected(.75);years=[float(r['year']) for r in base]
axs[0,1].plot(years,[float(r['electricity_net_MWh'])/1e3 for r in base],label='Net annual energy',color='#247a73')
axs[0,1].plot(years,[float(r['electricity_import_MWh'])/1e3 for r in base],label='Gross imports',color='#aa6441')
axs[1,0].plot(years,[float(r['T_stock_end_kg']) for r in base],color='#375c91')
labels=[('He-3 product candidate','Thousand STP L/year'),('Annual net positive is not islanded','GWh/year'),
        ('Tritium inventory; exports physically deducted','kg'),('Revenue less KNOWN charges — NOT PROFIT','$ million/year')]
for ax,(title,label) in zip(axs.flat,labels):
    ax.set_title(title,fontsize=11);ax.set_ylabel(label);ax.set_xlabel('Calendar year');ax.grid(alpha=.2)
axs[0,0].legend(fontsize=8);axs[0,1].legend(fontsize=8);axs[1,1].legend(fontsize=8)
fig.suptitle('Beyond Q v2.0: single-module ASSUMED scenarios; G1–G5 OPEN\nA draw 100 MWe assumed; housing/OPEX/replacement costs unresolved',fontsize=12)
for ext in ['png','svg']:fig.savefig(ROOT/f'outputs/research_summary.{ext}',dpi=140)
