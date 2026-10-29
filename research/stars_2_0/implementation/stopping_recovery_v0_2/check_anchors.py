"""Recovered stopping measurements, unit conversion and mirror-anchor check.

No whole-curve promotion, transport range construction or isotope transfer.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path

NA = Decimal('6.02214076e23')
ROOT = Path(__file__).resolve().parent
MIRROR_SHA256 = 'ab93971d116d0ef37ce64fa0f83153daf771ab46eba98ee72510dd84b16a7c97'


def atomic_to_mass_stopping(epsilon_eV_cm2_atom, molar_mass_g_mol):
    e, m = Decimal(str(epsilon_eV_cm2_atom)), Decimal(str(molar_mass_g_mol))
    if not e.is_finite() or not m.is_finite() or e < 0 or m <= 0:
        raise ValueError('invalid atomic stopping or molar mass')
    return e*Decimal('1e-6')*NA/m


def check(mirror_path=None, pdf_path=None):
    source=json.loads((ROOT/'OVERLEY_SOURCE.json').read_text())
    if pdf_path is not None:
        if hashlib.sha256(Path(pdf_path).read_bytes()).hexdigest()!=source['pdf_sha256']:
            raise ValueError('primary PDF identity mismatch')
    anchors=[]
    for r in source['anchors']:
        value=atomic_to_mass_stopping(r['epsilon_eV_cm2_atom'],source['target']['molar_mass_g_mol_as_reported'])
        anchors.append(dict(**r,mass_stopping_MeV_cm2_g_at_reported_molar_mass=str(value),
            uncertainty_convention='reported total probable error 4%; no Gaussian likelihood assigned'))
    matched=[]
    if mirror_path is not None:
        raw=Path(mirror_path).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=MIRROR_SHA256:
            raise ValueError('mirror identity mismatch')
        records=[line.split() for line in raw.decode().splitlines() if line.strip()]
        for a in anchors:
            e=Decimal(str(a['E_proton_LAB_MeV']))*1000
            expected=Decimal(str(a['epsilon_eV_cm2_atom']))/Decimal('1e-15')
            hits=[r for r in records if Decimal(r[0])==e and r[2]=='A']
            if len(hits)!=1 or Decimal(hits[0][1])!=expected:
                raise ValueError('mirror does not match absolute anchor')
            matched.append(dict(E_keV=str(e),epsilon_in_1e_minus15_eV_cm2_atom=str(expected),mirror_label='A',exact_match=True))
    return dict(status='TWO_PRIMARY_STOPPING_ANCHORS_SOURCE_QUALIFIED',anchors=anchors,
        mirror_matches=matched,primary_pdf_hash_verified=pdf_path is not None,
        mirror_conclusion='A is consistent with Overley at two exact anchors; full label/reference assignment and curve digitization remain open',
        source=source, restrictions=['Actual target is B10 enriched, not pure B11, BN or B4C.',
            'Atomic-to-mass conversion is a unit conversion, not evidence for isotope/material transfer.',
            'No interpolation, low-energy extrapolation, CSDA range or missing nuclear-component assumption is introduced.',
            'Do not count a mirror, thesis and related article as independent experiments.'])


def main():
    p=argparse.ArgumentParser();p.add_argument('--mirror',type=Path);p.add_argument('--pdf',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=check(a.mirror,a.pdf)
    a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'ANCHOR_RECEIPT.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'status':result['status'],'primary_anchors':len(result['anchors']),'mirror_matches':len(result['mirror_matches'])}))


if __name__=='__main__':main()
