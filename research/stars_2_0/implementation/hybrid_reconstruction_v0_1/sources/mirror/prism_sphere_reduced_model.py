"""Exploratory PRISM-like mirror + hollow-sphere source interface model.
NOT validated plasma/PIC fusion physics. Hypothetical inputs only.
"""
import csv
from math import exp

SOURCE_PROTONS = 1e10  # illustration per hypothetical laser shot, NOT measured
USEFUL_SPECTRAL_FRACTION = 0.05  # hypothetical in relevant reaction window
P_ENCOUNTER = 1e-5  # arbitrary conditional fusion probability per effective pass
SURVIVAL_PER_RETURN = 0.80  # non-reactive retention per transit
N_VALUES = [1, 3, 10, 30]
CAPTURE_VALUES = [0.1, 0.3, 0.6]
Q_J = 8.7e6 * 1.602176634e-19

def run(capture, max_passes, survival=SURVIVAL_PER_RETURN):
    # For each successful pass, nonreacting protons surviving to next pass only.
    alive = SOURCE_PROTONS * USEFUL_SPECTRAL_FRACTION * capture
    reactions = 0.0
    for _ in range(max_passes):
        born = alive * P_ENCOUNTER
        reactions += born
        alive = (alive-born) * survival
    return reactions

baseline = SOURCE_PROTONS * USEFUL_SPECTRAL_FRACTION * P_ENCOUNTER
rows=[]
for c in CAPTURE_VALUES:
    for n in N_VALUES:
        b=run(c,n)
        rows.append({'capture_fraction_assumed':c,'max_passes_assumed':n,'return_survival_assumed':SURVIVAL_PER_RETURN,
                     'fusion_events_proxy':round(b,3),'alpha_particles_proxy':round(3*b,3),
                     'fusion_energy_microjoules':round(b*Q_J*1e6,6),
                     'relative_to_one_pass_source':round(b/baseline,4)})

out='/mnt/data/prism_sphere_exploratory_sweep.csv'
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print('baseline events',baseline,'baseline microjoule',baseline*Q_J*1e6)
for r in rows: print(r)
