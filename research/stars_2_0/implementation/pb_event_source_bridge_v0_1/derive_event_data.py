"""Derive source-defined event cross sections from Sikora–Weller coefficients.
No conversion of the restricted Spraker observable is performed here.
"""
from html.parser import HTMLParser
from pathlib import Path
from decimal import Decimal
import csv,hashlib,json,math

class Table(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.depth=0;self.rows=[];self.row=None;self.cell=None
    def handle_starttag(self,tag,attrs):
        if tag=='table':self.depth+=1
        if self.depth and tag=='tr':self.row=[]
        if self.depth and tag in {'td','th'}:self.cell=[]
    def handle_data(self,data):
        if self.depth and self.cell is not None:self.cell.append(data)
    def handle_endtag(self,tag):
        if self.depth and tag in {'td','th'} and self.cell is not None:
            self.row.append(' '.join(''.join(self.cell).split()));self.cell=None
        if self.depth and tag=='tr' and self.row:
            self.rows.append(self.row);self.row=None
        if tag=='table':self.depth-=1

def extract(raw,table_number):
    p=Table();p.feed(raw.decode());out=[]
    for row in p.rows:
        try:e=Decimal(row[0])
        except Exception:continue
        coefficients=[]
        for cell in row[1:]:
            parts=cell.replace('−','-').split('±')
            if len(parts)!=2:raise ValueError('coefficient/error pair missing')
            v,s=map(lambda x:Decimal(x.strip()),parts)
            if not v.is_finite() or not s.is_finite() or s<0:raise ValueError('invalid coefficient')
            coefficients.append({'value_mb_sr':str(v),'stat_error_mb_sr':str(s)})
        n=3 if table_number==1 else 5
        if len(coefficients)!=n:raise ValueError('wrong coefficient count')
        out.append({'table':table_number,'channel':'alpha0' if table_number==3 else 'alpha1','E_lab_MeV':str(e),'coefficients':coefficients})
    if len(out)!={1:16,2:25,3:18}[table_number]:raise ValueError('table row count changed')
    return out

def derive(records):
    by={}
    for r in records:
        key=(r['E_lab_MeV'],r['channel'])
        if key in by:raise ValueError('duplicate source coefficient row')
        by[key]=r
    energies=sorted({Decimal(e) for e,ch in by if ch=='alpha1'})
    out=[]
    for E in energies:
        r=next(v for (e,ch),v in by.items() if Decimal(e)==E and ch=='alpha1')
        r0=next((v for (e,ch),v in by.items() if Decimal(e)==E and ch=='alpha0'),None)
        x=float(r['coefficients'][0]['value_mb_sr']);dx=float(r['coefficients'][0]['stat_error_mb_sr'])
        z=0 if r0 is None else float(r0['coefficients'][0]['value_mb_sr']);dz=0 if r0 is None else float(r0['coefficients'][0]['stat_error_mb_sr'])
        factor=4*math.pi/3/1000
        out.append({'E_lab_MeV':str(E),'sigma_event_b':factor*(x+z),'alpha1_event_component_b':factor*x,'alpha0_event_component_b':None if r0 is None else factor*z,
                    'stat_error_b_if_channel_fits_independent':factor*math.hypot(dx,dz),
                    'stat_error_b_max_positive_correlation':factor*(dx+dz),
                    'alpha0_handling':'not tabulated below 2.1 MeV; follows publication selected-channel coverage' if r0 is None else 'explicit table3 coefficient included',
                    'observable':'PUBLICATION_MODEL_EXTRAPOLATED_FUSION_EVENT_CROSS_SECTION'})
    if len(out)!=41:raise ValueError('expected 41 alpha1 grid values')
    return out

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--sources',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=False);records=[];hashes={}
    for n in [1,2,3]:
        f=a.sources/f'sikora_table{n}.html';raw=f.read_bytes();hashes[f.name]=hashlib.sha256(raw).hexdigest();records+=extract(raw,n)
    rows=derive(records)
    (a.out/'COEFFICIENTS.json').write_text(json.dumps(records,indent=2)+'\n')
    (a.out/'EVENT_CROSS_SECTIONS.json').write_text(json.dumps(rows,indent=2,allow_nan=False)+'\n')
    (a.out/'SOURCE_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps({'source_rows':len(records),'event_grid_rows':len(rows),'sample650':next(r for r in rows if float(r['E_lab_MeV'])==.65)},indent=2))
