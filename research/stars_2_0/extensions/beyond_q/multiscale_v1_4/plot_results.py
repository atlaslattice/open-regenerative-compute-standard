"""Standalone scientific plots from actual/conditional results."""
from pathlib import Path
import argparse,csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--qa-png',type=Path);a=ap.parse_args()
 read=lambda name:list(csv.DictReader((ROOT/'outputs'/name).read_text().splitlines()))
 plt.rcParams['svg.hashsalt']='bq-v14'
 f,ax=plt.subplots(2,2,figsize=(12,8),layout='constrained')
 data=read('drag_trajectories.csv')
 for species,label in [('T_e','Electron drag'),('T_i','Ion drag'),('T_both','Combined drag')]:
  rr=[r for r in data if r['case']=='drag_100' and r['species']==species]
  ax[0,0].plot([float(r['time_s']) for r in rr],[float(r['WarpX_energy_eV'])/1e3 for r in rr],label=label)
 ax[0,0].set(xlabel='Physical time (s)',ylabel='Triton kinetic energy (keV)',title='Actual WarpX trace-ion drag; prescribed background');ax[0,0].legend(fontsize=8)
 scan=read('slowing_escape_sensitivity.csv')
 for n in (5e19,1e20,2e20):
  rr=[r for r in scan if float(r['ne_m3'])==n and float(r['Te_eV'])==1e4];rr.sort(key=lambda r:float(r['tau_fast_s']))
  ax[0,1].semilogx([float(r['tau_fast_s']) for r in rr],[float(r['p_total_burn']) for r in rr],'o-',label=f'n = {n:.0e} m⁻³')
 ax[0,1].set(xlabel='Imposed fast and thermal residence (s)',ylabel='Eventual T burn probability',title='Reduced candidate; escape/transition uncalibrated');ax[0,1].legend(fontsize=8)
 for identity,label in [('historical_20_1130','Historical 20 / 1130 MW'),('dual_laser_1100_1100','Dual laser 1100 / 1100 MW')]:
  rr=read(identity+'_A1_trajectory.csv');hours=[float(r['time_hours']) for r in rr]
  ax[1,0].plot(hours,[float(r['b_store']) for r in rr],label=label)
  ax[1,1].plot(hours,[float(r['total_inventory'])-10 for r in rr],label=label)
 ax[1,0].set(xlabel='Plant clock (hours)',ylabel='B available storage (kg-T)',title='Conditional eight-hour B storage; initial 10 kg')
 ax[1,1].set(xlabel='Plant clock (hours)',ylabel='Change in total mobile inventory (kg-T)',title='Stock growth is not qualified usable surplus')
 for aa in ax.flat:aa.grid(alpha=.2)
 for aa in ax[1,:]:aa.legend(fontsize=8)
 f.suptitle('Beyond Q v1.4 — multiscale research; all physical gates remain open',fontsize=13)
 f.savefig(ROOT/'outputs/multiscale.svg',metadata={'Date':None})
 if a.qa_png:f.savefig(a.qa_png,dpi=120)
if __name__=='__main__':main()
