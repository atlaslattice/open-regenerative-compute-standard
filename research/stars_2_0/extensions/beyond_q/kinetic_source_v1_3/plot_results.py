"""Reproducible scientific SVGs from benchmark CSVs."""
import csv,argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--qa-png',type=Path);a=ap.parse_args()
 read=lambda f:list(csv.DictReader((ROOT/'outputs'/f).read_text().splitlines()))
 plt.rcParams['svg.hashsalt']='bq-kinetic-v1.3'
 fig,axes=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
 data=read('weighted_spectra.csv')
 for source,color in [('nDD','#2571ad'),('nDT','#c46519')]:
  rows=[r for r in data if r['case']=='chain_on' and r['species']==source]
  total=sum(float(r['physical_atoms']) for r in rows)
  x=[(float(r['energy_high_eV'])+float(r['energy_low_eV']))/2e6 for r in rows]
  y=[float(r['physical_atoms'])/total for r in rows]
  axes[0].step(x,y,where='mid',label=source,color=color)
 axes[0].set(xlabel='Neutron energy (MeV)',ylabel='Fraction within each source type',title='Actual weighted neutron spectra')
 axes[0].legend();axes[0].grid(alpha=.2)
 rows=read('benchmark_summary.csv');names=['chain_on','seed_219','seed_319','half_dt','double_ppc','lower_multiplier']
 rr=[next(r for r in rows if r['case']==n) for n in names]
 axes[1].plot(range(len(rr)),[float(r['secondary_burn_fraction'])*1e8 for r in rr],'o',label='WarpX chain')
 axes[1].plot(range(len(rr)),[float(r['continuous_constant_birth_f'])*1e8 for r in rr],'x',label='Independent constant-birth approximation')
 axes[1].set_xticks(range(len(rr)),['Baseline','Seed219','Seed319','Half dt','2× particles','Lower multiplier'],rotation=35,ha='right')
 axes[1].set(ylabel='Secondary T burn fraction × 10⁸',title='Finite-window source benchmark (2 ps)');axes[1].grid(alpha=.2);axes[1].legend(fontsize=8)
 fig.suptitle('Frozen periodic collision network — not a reactor confinement calculation',fontsize=12)
 fig.savefig(ROOT/'outputs/benchmark.svg',metadata={'Date':None})
 if a.qa_png:fig.savefig(a.qa_png,dpi=120)
if __name__=='__main__':main()
