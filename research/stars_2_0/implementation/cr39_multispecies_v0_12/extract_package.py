"""Recover primary source tables and experimental package without changing conventions."""
import argparse,hashlib,json,re,subprocess,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
SOURCES={
 'Schollmeier2023.xml':('https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10598230/fullTextXML','47036d5a9474dcb1fc395f524a362d2d75fc4e0ad2eef7f37e6ef795411c6cac'),
 'Schollmeier2023.pdf':('https://www.nature.com/articles/s41598-023-45208-x.pdf','3bf468794a030e5002e3c68db581b16d4c74a14b2f415a5dd5a40d6417a9caf9'),
 'Supplement2023.pdf':('https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-023-45208-x/MediaObjects/41598_2023_45208_MOESM1_ESM.pdf','605f7a28b699a92175e60c08e086f5e705d553d30f0362590ff20237d4dd9749')}

def extract(directory,download=False):
 for n,(u,h) in SOURCES.items():
  p=directory/n
  if download and not p.exists():
   b=urllib.request.urlopen(u,timeout=30).read()
   if hashlib.sha256(b).hexdigest()!=h:raise ValueError('source changed; inspect a new version')
   directory.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
  if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError('primary source identity mismatch')
 root=ET.parse(directory/'Schollmeier2023.xml').getroot();table=next(x for x in root.iter('table-wrap') if x.get('id')=='Tab1');rows=[]
 for tr in list(table.iter('tr'))[1:]:
  cells=[''.join(x.itertext()) for x in tr];rows.append(dict(label=cells[0],p1=float(cells[1]),p2=float(cells[2]),p3=float(cells[3]),p4=float(cells[4]),reported_residual_sigma_um=float(cells[5])))
 if len(rows)!=4:raise ValueError('table structure changed')
 main_text=subprocess.run(['pdftotext','-f','5','-l','5','-layout',str(directory/'Schollmeier2023.pdf'),'-'],capture_output=True,text=True,check=True).stdout
 for row in rows:
  label=' '.join(row['label'].split());matches=[]
  for line in main_text.splitlines():
   clean=' '.join(line.split())
   if clean.startswith(label+' '):
    nums=re.findall(r'(?<![A-Za-z])(?:\d+\.\d+|\d+)',clean[len(label):])
    if len(nums)==5:matches.append([float(v) for v in nums])
  target=[row[k] for k in ['p1','p2','p3','p4','reported_residual_sigma_um']]
  if target not in matches:raise ValueError('PDF/XML coefficient disagreement for '+label)
 latex=next(x for x in root.iter('disp-formula') if x.get('id')=='Equ2');latex=''.join(latex.find('.//tex-math').itertext())
 p=subprocess.run(['pdftotext','-f','4','-l','4','-layout',str(directory/'Supplement2023.pdf'),'-'],capture_output=True,text=True,check=True)
 if not all(v in p.stdout for v in ['0.040','0.060','0.035','0.025']):raise ValueError('supplement table anchor missing')
 return dict(source_doi='10.1038/s41598-023-45208-x',attribution='Schollmeier et al., Scientific Reports13,18155(2023), CC BY4.0; source-defined values retained',
  source_sha256={n:h for n,(u,h) in SOURCES.items()},table1_PDF_and_XML_numeric_agreement=True,equation2_latex=latex,table1=rows,
  supplement_table_S1=dict(method='Visually verified PDFpage4 transcription; pdftotext numeric anchors checked',rows=[
   dict(ion='H',sigma_L_range_um=[.040,.060],eta_L_range_um=[.020,.030],sigma_effective_um=.060),
   dict(ion='He',sigma_L_range_um=[.030,.060],eta_L_range_um=[.010,.035],sigma_effective_um=.050),
   dict(ion='C',sigma_L_range_um=[.008,.050],eta_L_range_um=[.010,.010],sigma_effective_um=.025)],
   semantics='Source Landau/Gaussian width parameters; not parameter covariance, confidence interval or interchangeable Gaussian standard deviation. Supplement prose mentions He widths0.4–0.6um while TableS1 lists0.030–0.060um; reconcile before use.'),
  conditions=dict(detector='TASTRAK',etchant='NaOH',concentration_mol_L=6.25,temperature_C=70.,etch_minutes=30,diameter_method='HWHM fitted image profile, not a grayscale threshold diameter',microscope_resolution_um=.4,microscope_pixel_nm=40.7),
  filter_array=dict(nominal_stacks=[dict(material='Mylar',thickness_um=1.),*[dict(material='Al',thickness_um=x) for x in [2.,4.5,8.,12.5,25.]]],thickness_tolerance_um=None,full_transmission_tables=None,density_and_composition_tolerances=None,mesh_or_aperture_transmission=None),
  geometry=dict(CR39_distance_m_approx=1.7,CR39a_angle_to_target_normal_deg=45,CR39b_angle_to_target_normal_deg=65,TP2_angle_to_target_normal_deg_approx=35,images_per_filter=100,image_field_um=[114,85],detector_area_mm=[20,20],effective_solid_angle_sr=None),
  reported_campaign_adjustments=dict(pit_diameter_shifts_typical_percent=[-3,3],proton_calibration_shift_percent_approx=-15,proton_CR39_to_TP_flux_ratio_approx=2.,interpretation='Reported calibration/diagnostic discrepancies, not new correction factors for Stars or independent uncertainty distributions'),
  analytic_spectrum_parameters=[dict(id='CR39b_H',ion='H',equation=4,N0_per_sr_J=1e11,kBT_MeV=4.36),dict(id='CR39b_C',ion='C',equation=3,N0_per_sr_J=1.4e10,kBT_MeV=2.01)],
  spectrum_semantics='Published analytic parameter replay only, not raw data reconstruction. Eq3 has N0/E and divergent integrated count as E_min tends to0; do not silently interpret N0 as a total count. Explicit finite domains required.',
  data_availability='Numerical experimental data available from Marvel Fusion upon reasonable request; raw pit/image/spectrum package not recovered or requested in this release',
  production_response_status='BLOCKED_LITERAL_EQUATION_TABLE_RECONCILIATION_AND_MATCHED_RAW_DATA')

def main():
 a=argparse.ArgumentParser();a.add_argument('--sources',type=Path,required=True);a.add_argument('--download',action='store_true');a.add_argument('--out',type=Path,required=True);a=a.parse_args()
 if a.out.exists():raise FileExistsError('preserve earlier extraction')
 d=extract(a.sources,a.download);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(coefficient_rows=len(d['table1']),filter_stacks=len(d['filter_array']['nominal_stacks']),status=d['production_response_status'])))
if __name__=='__main__':main()
