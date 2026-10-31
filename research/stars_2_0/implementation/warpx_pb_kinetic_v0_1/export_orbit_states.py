"""Export retained numerical-test particles with current positions/time and SI momentum."""
import hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.constants import c,m_p,e
root=Path(__file__).resolve().parent
cases=json.loads((root/'ORBIT_CASES_v003.json').read_text());outputs=[]
for case in cases:
 if case['case'] not in ['uniform_half_dt','mirror_losscone_fine','mirror_reflect_fine']:continue
 run=root/'receipts'/(case['case']+'002');path=run/'diags/reducedfiles/extrema.txt'
 n=np.loadtxt(run/'diags/reducedfiles/number.txt');a=np.loadtxt(path)
 packet=None
 if n[-1,4]>0:
  row=a[-1];p=row[[8,10,12]];norm=float(np.linalg.norm(p));K=norm*norm/(math.sqrt(m_p*m_p+norm*norm/c**2)+m_p)
  packet=dict(species='proton',weight=float(n[-1,4]),position_m=row[[2,4,6]].tolist(),time_s=float(row[1]),momentum_kg_m_s=p.tolist(),unit_direction_LAB=(p/norm).tolist(),kinetic_MeV=K/(e*1e6),position_time_status='ACTUAL_WARPX_DIAGNOSTIC_STATE_NOT_SOURCE_TAG')
 outputs.append(dict(case=case['case'],evidence='SYNTHETIC_FIELD_VERIFICATION_EXECUTED_IN_WARPX',apparatus_id=None,frame='LAB',diagnostic_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),remaining_packet=packet,initial_weight=1,escaped_weight=float(1-n[-1,4]),escape_phase_space='NOT_RECONSTRUCTED_FROM_LAST_ACTIVE_SAMPLE',facility_wall_input_J=None))
with (root/'receipts'/'PARTICLE_INTERFACE001.json').open('x') as f:json.dump(outputs,f,indent=2,allow_nan=False);f.write('\n')
