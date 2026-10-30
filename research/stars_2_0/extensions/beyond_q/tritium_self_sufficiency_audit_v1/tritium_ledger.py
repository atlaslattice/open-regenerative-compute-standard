#!/usr/bin/env python3
"""Beyond Q v1.0: deterministic analytical ledger. NO neutronics/plasma model."""
import csv, argparse
p=argparse.ArgumentParser()
p.add_argument("--burn",type=float,default=63.1,help="Reactor B T kg/full-power-year")
p.add_argument("--a-export",type=float,default=3.65,help="Optimistic A qualified kg/FPY; default is pre-processing potential not measured")
p.add_argument("--efficiency",type=float,default=1.0,help="B ultimate net recovered fraction, not single-pass extraction")
args=p.parse_args()
assert args.burn>0 and 0<=args.efficiency<=1 and args.a_export>=0
tbrs=(.95,.97,1.,1.02,1.04,1.05,1.1)
print("TBR,B_born_kg,B_recovered_kg,A_assumed_export_kg,campus_net_kg")
for t in tbrs:
  born=args.burn*t
  net=args.a_export+args.efficiency*born-args.burn
  print(f"{t:.2f},{born:.6f},{args.efficiency*born:.6f},{args.a_export:.6f},{net:.6f}")
assert abs((3.65+1.02*63.1-63.1)-4.912)<1e-9
assert abs((3.65+.85*1.02*63.1-63.1)-(-4.7423))<1e-9
