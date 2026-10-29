"""Hash-verified evidence selection; source quantities are not silently interchangeable."""
import argparse,csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load_catalog():
 c=json.loads((ROOT/'DATASET_CATALOG.json').read_text())
 for d in c['datasets']:
  if hashlib.sha256((ROOT/d['file']).read_bytes()).hexdigest()!=d['sha256']:raise ValueError('dataset changed '+d['id'])
 return c

def authorize(dataset_id,role,*,projectile,material,energy_LAB_MeV,state=None):
 c=load_catalog();matches=[d for d in c['datasets'] if d['id']==dataset_id]
 if len(matches)!=1:raise ValueError('unknown dataset')
 d=matches[0]
 if role not in d['permitted_roles']:raise ValueError('observable/role mismatch; no implicit multiplicity or frame conversion')
 scope=d['scope']
 if projectile!=scope.get('projectile') or material!=scope.get('material'):raise ValueError('projectile/material applicability mismatch')
 if scope.get('state') is not None and state!=scope['state']:raise ValueError('material state mismatch')
 lo,hi=scope.get('energy_LAB_MeV',[None,None])
 if lo is not None and not lo<=energy_LAB_MeV<=hi:raise ValueError('energy applicability mismatch')
 return d

def audit(metadata_only=False):
 c=load_catalog();summary=[]
 for d in c['datasets']:
  p=ROOT/d['file'];rows=None;excluded=None;availability='BUNDLED_REFERENCE_FILE'
  if 'generated_data' in d:
   g=d['generated_data'];generated=ROOT/g['file'];rows=g['rows']
   if not metadata_only and generated.exists():
    if hashlib.sha256(generated.read_bytes()).hexdigest()!=g['sha256']:raise ValueError('generated spectrum identity mismatch')
    p=generated;availability='RECONSTRUCTED_DATA_HASH_VERIFIED'
   else:
    availability='NUMERICAL_SPECTRA_REQUIRE_RECONSTRUCTION; anchor receipt verified'
    summary.append(dict(id=d['id'],rows=rows,entries_excluded_from_automatic_use=None,permitted_roles=d['permitted_roles'],experimental_ancestry_group=d['experimental_ancestry_group'],availability=availability));continue
  if p.suffix=='.csv':
   with p.open(newline='') as f:
    records=list(csv.DictReader(f));rows=len(records)
    excluded=sum(row['source_cell_status']=='REPORTED_ZERO_ACCEPTANCE_UNQUALIFIED' or row['coverage']!='WITHIN_ARTICLE_ENERGY_RANGE' or row['angle_status']!='SHEET_NAME_MATCHES_ARTICLE_LAB_DETECTOR' for row in records)
  else:
   v=json.loads(p.read_text())
   if isinstance(v,list):rows=len(v)
   elif 'rows' in v:
    rows=len(v['rows']);excluded=sum(not row.get('eligible_for_future_fit',True) for row in v['rows']) if any('eligible_for_future_fit' in row for row in v['rows']) else None
   elif 'points' in v:rows=len(v['points'])
  summary.append(dict(id=d['id'],rows=rows,entries_excluded_from_automatic_use=excluded,permitted_roles=d['permitted_roles'],experimental_ancestry_group=d['experimental_ancestry_group'],availability=availability))
 return dict(status='HASH_VERIFIED_EVIDENCE_BUNDLE_NOT_A_JOINT_CALIBRATION',datasets=summary,coherent_exclusive_fit_dataset=None,notes='No reinterpretation of probable error, FWHM, upper limits, duplicate energies or source-defined units. Eligible rows alone do not establish apparatus compatibility.')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);a.add_argument('--metadata-only',action='store_true');a=a.parse_args()
 if a.out.exists():raise FileExistsError('preserve earlier audit')
 r=audit(metadata_only=a.metadata_only);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
