"""Standalone scientific comparison plots. Requires matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--qa-png',type=Path)
    args=parser.parse_args()
    plt.rcParams['svg.hashsalt']='beyond-q-v1.1.1'
    d=np.genfromtxt(ROOT/'outputs/benchmark_curves.csv',delimiter=',',names=True)
    f,axes=plt.subplots(2,1,figsize=(9,7),layout='constrained')
    for name,label in [('T_10_storage','Storage'),('T_02_TES','Extraction stock')]:
        axes[0].plot(d['time_s']/86400,d[name+'_gold'],label=label+' / INL gold')
        axes[0].plot(d['time_s']/86400,d[name+'_reproduced'],'--',label=label+' / reproduction')
    axes[0].set(xlabel='Elapsed days',ylabel='T inventory (kg)',title='External computational benchmark — not physical validation')
    axes[0].legend(fontsize=9)
    axes[1].plot(d['time_s']/86400,d['T_10_storage_reproduced']-d['T_10_storage_continuous'])
    axes[1].set(xlabel='Elapsed days',ylabel='Storage difference (kg)',title='Recorded backward Euler result minus continuous-time oracle')
    for a in axes:a.grid(alpha=.2)
    f.savefig(ROOT/'outputs/benchmark.svg',metadata={'Date':None})
    if args.qa_png:f.savefig(args.qa_png,dpi=110)
    plt.close(f)

if __name__=='__main__':main()
