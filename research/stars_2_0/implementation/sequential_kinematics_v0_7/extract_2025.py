"""Recover published Table 2 values, retaining uncertainty definitions and censoring."""
import argparse,hashlib,json,re,subprocess,urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PDF_SHA='7707a7750640021307b29a4aa1dcc4bea8ce6a3769fc1030f8f96ab6d951b71b'
PDF_URL='https://inspirehep.net/files/4183e926f091677ca2e75076f79700c9'
DOI='10.1140/epja/s10050-025-01589-3'
TAG='PUBLISHED_60DEG_LAB_ALPHA_COUNTS_NORMALIZED_DIFFERENTIAL_QUANTITY'

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'

def parse_table(text):
    rows=[]
    for line in text.splitlines():
        s=line[:70].strip()
        if not re.match(r'^\d+\.\d+\s*±',s):continue
        if '<' in s:
            if '< 10−3' not in s:raise ValueError('unsupported censored-cell notation')
            s2=s.replace('< 10−3','CENSORED')
            nums=list(map(float,re.findall(r'\d+\.\d+',s2)))
            if len(nums)!=6:raise ValueError('censored row must preserve all six values')
            E,dE,a1,da1,total,dtotal=nums
            a0=dict(value_mb_sr=None,reported_plus_minus_mb_sr=None,upper_limit_mb_sr=.001,censoring='LESS_THAN',limit_confidence_level=None)
        else:
            nums=list(map(float,re.findall(r'\d+\.\d+',s)))
            if len(nums)!=8 or s.count('±')!=4:raise ValueError('row must preserve all eight values and four errors')
            E,dE,a0v,da0,a1,da1,total,dtotal=nums
            a0=dict(value_mb_sr=a0v,reported_plus_minus_mb_sr=da0,upper_limit_mb_sr=None,censoring=None,limit_confidence_level=None)
        rows.append(dict(E_proton_on_boron_MeV=E,reported_energy_plus_minus_MeV=dE,
            alpha0=a0,alpha1=dict(value_mb_sr=a1,reported_plus_minus_mb_sr=da1),
            total_reported=dict(value_mb_sr=total,reported_plus_minus_mb_sr=dtotal),
            possible_Al_support_alpha_contribution_explicitly_flagged_by_authors=E in [2.88,3.85,4.32,4.51,4.73],
            source_row=s))
    if len(rows)!=28 or len({r['E_proton_on_boron_MeV'] for r in rows})!=28:raise ValueError('expected exactly 28 distinct Table 2 rows')
    if any(a['E_proton_on_boron_MeV']<=b['E_proton_on_boron_MeV'] for a,b in zip(rows,rows[1:])):raise ValueError('published descending order changed')
    return dict(source_doi=DOI,source_pdf_sha256=PDF_SHA,source_location='Table 2, PDF page10 of12',
        extraction='pdftotext -f10 -l10 -layout, first70 text columns; matched against rendered source page',
        attribution='Mazzucconi et al., Eur.Phys.J.A61,114(2025); CC BY4.0 https://creativecommons.org/licenses/by/4.0/ ; structured transcription with added qualifications',
        observable=TAG,detector_angle_degrees=60,detector_angle_frame='LAB',
        incident_energy_frame='LAB at boron, inferred from elastic-proton spectra/FLUKA; not nominal accelerator setting',
        energy_uncertainty='reported +/- preserved; Sec2.3 ties it to a FWHM comparison; NOT automatically Gaussian1sigma or an energy-distribution kernel',
        yield_uncertainty='reported +/- preserved; combines counting, target, geometry and integrated-charge contributions; cross-row covariance/decomposition not recovered',
        source_total_label='Total CS',source_formula='Counts / (Nt Np dOmega)',
        multiplicity_to_event_cross_section='UNRESOLVED: no division by3 or4pi conversion authorized by this fixture',
        angular_extrapolation_to_total_cross_section='NOT_PERFORMED; paper uses isotropy assumption for its comparison',
        independent_campaign='different experimental campaign from TUNL2012; complete systematic independence not established',
        raw_event_spectra='not recovered; article offers data on reasonable request',
        rows=rows)

def extract(pdf):
    if hashlib.sha256(pdf.read_bytes()).hexdigest()!=PDF_SHA:raise ValueError('source PDF identity mismatch')
    r=subprocess.run(['pdftotext','-f','10','-l','10','-layout',str(pdf),'-'],capture_output=True,text=True,check=True)
    return parse_table(r.stdout)

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--download',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('choose a new output file')
    if a.download and not a.pdf.exists():
        b=urllib.request.urlopen(PDF_URL,timeout=30).read()
        if hashlib.sha256(b).hexdigest()!=PDF_SHA:raise ValueError('download identity mismatch')
        a.pdf.parent.mkdir(parents=True,exist_ok=True);a.pdf.write_bytes(b)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(encoded(extract(a.pdf)))
    print(encoded(dict(rows=28,output=str(a.out),event_cross_section_conversion='NOT_PERFORMED')))

if __name__=='__main__':main()
