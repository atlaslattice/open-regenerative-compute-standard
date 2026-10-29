"""Preserve the 2019v1 preprint table, including duplicated-energy ambiguities."""
import argparse,collections,hashlib,json,re,subprocess,urllib.request
from pathlib import Path

PDF_SHA='9839275f558087a54f2c865ae65540528b46575a19a913739d38bfd8af16f8a4'
URL='https://arxiv.org/pdf/1908.04064v1'

def parse(text):
    rows=[]
    for line in text.splitlines():
        for match in re.finditer(r'(?<!\d)(\d{3,4})\s+(\d+(?:\.\d+)?)\((\d+)\)',line):
            E,central,error=match.groups();decimals=len(central.split('.')[1]) if '.' in central else 0
            rows.append(dict(record_id=f'PREPRINT_V1_TABLE1_{len(rows)+1:03}',E_proton_LAB_keV=int(E),
                alpha0_angle_integrated_mb=float(central),reported_error_mb=int(error)*10.**(-decimals),source_token=central+'('+error+')'))
    if len(rows)!=45:raise ValueError('expected45 table entries; source layout changed')
    counts=collections.Counter(r['E_proton_LAB_keV'] for r in rows)
    duplicates=sorted(E for E,n in counts.items() if n>1)
    if duplicates!=[950,1900]:raise ValueError('preprint ambiguity signature changed; inspect source')
    for row in rows:
        row['source_energy_duplicated']=row['E_proton_LAB_keV'] in duplicates
        row['eligible_for_future_fit']=not row['source_energy_duplicated']
    return dict(source='Munch et al., arXiv1908.04064v1, Table1 / PDFpage4; related journal DOI10.1140/epja/s10050-019-00016-8',
        source_pdf_sha256=PDF_SHA,source_url=URL,publication_identity='PREPRINT_V1_NOT_VERIFIED_JOURNAL_TABLE',
        observable='ALPHA0_CHANNEL_ANGLE_INTEGRATED_CROSS_SECTION',energy_frame='LAB',
        uncertainty='parenthesized errors transcribed; caption approx10% except lowest two12%; full covariance and exact statistical convention not recovered',
        duplicate_energies_keV=duplicates,duplicate_policy='all four entries retained and excluded from automatic fitting; no guessed energy correction or deduplication',
        pure_2minus_source_scope='not the same as full reaction: alpha0 can receive other parent-state contributions',rows=rows)

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--download',action='store_true');a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve earlier extraction')
    if a.download and not a.pdf.exists():
        b=urllib.request.urlopen(URL,timeout=30).read()
        if hashlib.sha256(b).hexdigest()!=PDF_SHA:raise ValueError('source download identity mismatch')
        a.pdf.parent.mkdir(parents=True,exist_ok=True);a.pdf.write_bytes(b)
    if hashlib.sha256(a.pdf.read_bytes()).hexdigest()!=PDF_SHA:raise ValueError('source PDF identity mismatch')
    r=subprocess.run(['pdftotext','-f','4','-l','4','-layout',str(a.pdf),'-'],capture_output=True,text=True,check=True)
    d=parse(r.stdout);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(entries=len(d['rows']),ambiguous_entries=sum(r['source_energy_duplicated'] for r in d['rows']),source_PDF_warnings=r.stderr)))

if __name__=='__main__':main()
