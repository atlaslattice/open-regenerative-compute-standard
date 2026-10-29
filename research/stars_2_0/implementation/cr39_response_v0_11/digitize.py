"""Digitize a condition-specific publisher figure; preserve image identity and limits."""
import argparse,hashlib,json,urllib.request
from pathlib import Path
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parent
BASE='https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs41365-019-0619-x/MediaObjects/'
SOURCES={10:('19ea0b76fd5024fe24d72a5b02b4b1d589447a0671f3f00b5d35447204609987',(969,791)),4:('0a369016da858917b016cd54d14bd8c5f64f589f260961da18d5c98548663e04',(1498,974))}
ENERGIES=[1.105,2.114,2.361,2.807,3.061,3.446,3.940,4.160,4.420,4.915]
# Manually inspected marker centers and error-cap endpoints; pixels are not physical fit parameters.
BLACK_MARKERS=[(260,361,321,400),(418,197,172,221),(456,248,221,274),(526,311,272,350),(566,393,357,429),(626,383,349,418),(704,441,407,475),(739,422,369,479),(779,498,446,550),(857,584,541,626)]

def source(n,directory,download):
 path=directory/f'Zhang2019_Fig{n}.png';url=BASE+f'41365_2019_619_Fig{n}_HTML.png'
 if download and not path.exists():
  b=urllib.request.urlopen(url,timeout=30).read()
  if hashlib.sha256(b).hexdigest()!=SOURCES[n][0]:raise ValueError('publisher image changed; inspect new version')
  path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(b)
 b=path.read_bytes()
 if hashlib.sha256(b).hexdigest()!=SOURCES[n][0]:raise ValueError('source identity mismatch')
 im=Image.open(path).convert('RGB')
 if im.size!=SOURCES[n][1]:raise ValueError('source dimensions changed')
 return np.asarray(im)

def recover(directory,download=False):
 a=source(10,directory,download);black=a.max(axis=2)<70;rows=[]
 for e,(x,y,top,bottom) in zip(ENERGIES,BLACK_MARKERS):
  if abs(x-(86+e*863/5.5))>2.5:raise ValueError('energy-marker association failed')
  if black[y-2:y+3,x-6:x+7].sum()<10:raise ValueError('expected black marker not recovered')
  for cap in [top,bottom]:
   if black[cap-1:cap+2,x-8:x+9].sum()<9:raise ValueError('error cap not recovered')
  rows.append(dict(E_alpha_MeV=e,mean_track_diameter_um=6+(710-y)*12/696,reported_core_spread_um=(bottom-top)*6/696,
   marker_pixel=[x,y],error_cap_y_pixels=[top,bottom],mean_digitization_allowance_um=.06,spread_digitization_allowance_um=.08))
 a=source(4,directory,download);black=a.max(axis=2)<70;edges=np.linspace(3.2,24.,53);counts=[];pixels=[]
 for d in (edges[:-1]+edges[1:])/2:
  xi=int(round(154+d*(1482-154)/24));occupied=black[20:897,xi-8:xi+9].sum(axis=1);loc=np.flatnonzero(occupied>=6)+20
  if xi>1040:loc=loc[loc>260] # printed statistics box is not the histogram
  if len(loc)==0:raise ValueError('histogram plateau missing')
  top=int(loc[0]);cy=float(loc[loc<=top+4].mean());pixels.append(cy);counts.append(max(0,(893.5-cy)*3000/(893.5-73)))
 counts=np.asarray(counts);center=(edges[:-1]+edges[1:])/2;mean=float(counts@center/counts.sum());sd=float(np.sqrt(counts@(center**2)/counts.sum()-mean**2))
 allowance=4*3000/(893.5-73) # two-pixel baseline and two-pixel line-position allowance, not stochastic noise
 return dict(source='Zhang et al., Nuclear Science and Techniques30,87(2019), DOI10.1007/s41365-019-0619-x',
  evidence_state='DIGITIZED_PUBLISHED_REFERENCE_NOT_APPARATUS_VALIDATED',
  conditions=dict(species='alpha',detector='TASTRAK',etchant='NaOH',concentration_mol_L=6.25,temperature_C=98.,etch_time_hours=1.,detector_dimensions_mm=[25,25,1.5],incidence='source experimental orientation; angular response not qualified',scope='original detector lot/storage/readout conditions; not BA or Zheng2026'),
  source_image_sha256={str(n):SOURCES[n][0] for n in SOURCES},mean_response_rows=rows,
  error_semantics='Figure10 error bars represent reported Gaussian-fit track-diameter spreads, not uncertainty of the mean response or a guaranteed Gaussian response. Digitization allowances are analyst-selected conservative pixel bounds, not confidence intervals.',
  figure4=dict(E_alpha_MeV=4.42,display_subset_edges_um=edges.tolist(),digitized_display_counts=counts.tolist(),plateau_y_pixels=pixels,
   per_bin_count_digitization_allowance=float(allowance),conditional_display_probabilities=(counts/counts.sum()).tolist(),digitized_display_total=float(counts.sum()),digitized_display_mean_um=mean,digitized_display_standard_deviation_um=sd,
   source_statistics=dict(entries=14740,raw_mean_um=9.773,raw_standard_deviation_um=1.482,gaussian_fit_mean_um=9.65,gaussian_fit_mean_error_um=.01,gaussian_fit_sigma_um=.9028,gaussian_fit_sigma_error_um=.0078,chi_squared=1140,degrees_of_freedom=22),
   scope='conditional distribution within digitized3.2–24um display subset; not raw events, absolute efficiency, or full-tail reconstruction',
   discrepancy='Digitized display standard deviation differs from source statistic; baseline, finite pixels and omitted display tails remain unresolved. Do not relabel as exact histogram reproduction.'))

def main():
 p=argparse.ArgumentParser();p.add_argument('--sources',type=Path,required=True);p.add_argument('--download',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('preserve existing extraction')
 d=recover(a.sources,a.download);a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
 print(json.dumps(dict(response_points=len(d['mean_response_rows']),histogram_subset_bins=len(d['figure4']['digitized_display_counts']),digitized_mean=d['figure4']['digitized_display_mean_um'],digitized_std=d['figure4']['digitized_display_standard_deviation_um'])))
if __name__=='__main__':main()
