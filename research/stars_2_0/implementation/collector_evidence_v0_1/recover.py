"""Published TMX figure-point recovery, affine digitization and limited curve check."""
import argparse,csv,hashlib,itertools,json,platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
from terminal_ledger import terminal_ledger
p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--out',required=True);a=p.parse_args();root=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
cfg=json.loads((root/'FIGURE15_MARKERS.json').read_text());download=json.loads((root/'DOWNLOAD.json').read_text());pdf=Path(a.pdf)
if hashlib.sha256(pdf.read_bytes()).hexdigest()!=download['sha256']:raise ValueError('source PDF hash mismatch')
# Recheck the image against archived marker coordinates without redistributing it.
import fitz
from PIL import Image
from io import BytesIO
from scipy.ndimage import label,find_objects,center_of_mass
doc=fitz.open(pdf);page=doc[cfg['source_pdf_page_1based']-1];image=doc.extract_image(page.get_images()[0][0]);im=Image.open(BytesIO(image['image'])).convert('L')
if list(im.size)!=cfg['native_image_size_px']:raise ValueError('source image changed')
im=np.array(im.crop(cfg['crop_native_px']));labels,_=label(im>127);holes=[]
for i,s in enumerate(find_objects(labels),1):
 if s is None:continue
 y,x=s[0].start,s[1].start;h,w=s[0].stop-y,s[1].stop-x;area=int(np.sum(labels[s]==i))
 if 2<=w<=11 and 2<=h<=11 and 4<=area<=80:
  cy,cx=center_of_mass(labels[s]==i);holes.append([cx+x,cy+y])
markers=np.array(cfg['markers']);dist=np.min(np.linalg.norm(markers[:,None,:]-np.array(holes)[None,:,:],axis=2),axis=1)
closed=np.arange(len(markers))!=6
if np.max(dist[closed])>.03:raise ValueError('closed marker centroid does not match source')
anchors=np.array([r['pixel'] for r in cfg['affine_anchors']]);values=np.array([r['value'] for r in cfg['affine_anchors']])
def transform(points,base):return np.column_stack([points,np.ones(len(points))])@np.linalg.solve(np.column_stack([base,np.ones(3)]),values)
xy=transform(markers,anchors);low=np.full_like(xy,np.inf);high=np.full_like(xy,-np.inf);eps=cfg['coordinate_reading_bound_px']
# Correlated global axis errors + individual marker-reading errors. A bounded
# analyst sensitivity set, not measurement errors or a stochastic posterior.
for shift in itertools.product([-eps,eps],repeat=6):
 shifted=anchors+np.array(shift).reshape(3,2)
 for mx,my in itertools.product([-eps,eps],repeat=2):
  v=transform(markers+[mx,my],shifted);low=np.minimum(low,v);high=np.maximum(high,v)
with (out/'FIGURE15_COLLECTOR_POINTS.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['point','voltage_V','net_collector_current_A','digitization_low_V','digitization_high_V','digitization_low_A','digitization_high_A','group_nearest_102V_tap'])
 for i,((V,I),(lv,li),(hv,hi)) in enumerate(zip(xy,low,high)):w.writerow([i,float(V),float(I),float(lv),float(hv),float(li),float(hi),int(round(V/102))])
V,I=xy.T
# This is our reconstruction of the displayed plateau/exponential-tail curve.
def curve(V,x):
 plateau,phi,Ti=x;return plateau*np.exp(-np.maximum(0,V-phi)/Ti)
published=np.array([cfg['source_model_annotation'][k] for k in ['plateau_A','phi_V','Ti_eV']])
groups=np.round(V/102).astype(int);train=groups<9;test=~train
fit=least_squares(lambda x:curve(V[train],x)-I[train],published,bounds=([1e-6,0,1],[1.,1500.,5000.]),xtol=1e-13,ftol=1e-13,gtol=1e-13)
facts=json.loads((root/'TMX_REPORTED_VALUES.json').read_text());b=facts['body_VI_record'];abstract=facts['abstract_record'];abnet=abstract['collector_W']-abstract['suppressor_draw_W']
ledger=terminal_ledger([{'id':'collector','voltage_V':b['collector_V'],'net_positive_charge_current_into_electrode_A':b['collector_A']},{'id':'suppressor','voltage_V':b['suppressor_V'],'net_positive_charge_current_into_electrode_A':b['suppressor_drain_A']}],b['incident_ion_A']*b['average_ion_energy_eV'])
ratios=facts['body_model_rounded_current_ratios'];paper_model_eta=(ratios['collector_over_incident']*b['collector_V']-ratios['suppressor_over_incident']*abs(b['suppressor_V']))/b['average_ion_energy_eV']
checks=[{'name':'all_19_collector_points_preserved','passed':len(xy)==19},{'name':'18_closed_markers_match_source_pixels','passed':bool(np.max(dist[closed])<.03)},{'name':'fit_numeric_solver_converged','passed':bool(fit.success)},{'name':'fit_no_parameter_at_computational_bound','passed':bool(np.all(fit.active_mask==0))},{'name':'whole_voltage_groups_held_out','passed':bool(set(groups[train]).isdisjoint(set(groups[test])))},{'name':'net_terminal_arithmetic','passed':abs(ledger['net_terminal_out_W']-66.6)<1e-10},{'name':'abstract_arithmetic','passed':abs(abnet-67.)<1e-12},{'name':'published_rounded_model_eta','passed':abs(paper_model_eta-.47)<.001},{'name':'apparatus_gain_not_assigned','passed':ledger['wall_plug_net_power_W'] is None}]
report={'status':'PUBLISHED_EXPERIMENT_FIGURE_DATA_AND_TERMINAL_ACCOUNTING_RECOVERED','source_pdf_sha256':download['sha256'],'native_image_sha256':hashlib.sha256(image['image']).hexdigest(),'abstract_arithmetic':{'net_W':abnet,'net_over_declared_incident':abnet/abstract['incident_W']},'body_VI_arithmetic':ledger,'source_model_rounded_ratio_eta':paper_model_eta,'digitization_max_centroid_recheck_distance_px':float(max(dist[closed])),'digitization_bounds':'analyst ±3px on affine anchors and marker centers; no experimental uncertainty claim','curve_reconstruction':{'published_annotation':published.tolist(),'heldout_groups':sorted(set(groups[test].tolist())),'train_points':int(sum(train)),'heldout_points':int(sum(test)),'fit_parameters_plateauA_phiV_TieV':fit.x.tolist(),'published_curve_RMSE_A':float(np.sqrt(np.mean((curve(V,published)-I)**2))),'heldout_fit_RMSE_A':float(np.sqrt(np.mean((curve(V[test],fit.x)-I[test])**2))),'independence':'Within-figure voltage-group split, same experimental campaign; not independent experiment or calibration acceptance. No recovered point covariance or per-shot errors.','meaning':'Exploratory curve check of net terminal current, not a validated incoming alpha distribution'},'checks':checks,'software':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'code_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ['recover.py','terminal_ledger.py']},'STARS_pB_net_wall_plug_W':None}
(out/'RESULTS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
# Original visualization of recovered facts; no scanned figure redistribution.
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained');ax.errorbar(V,I,xerr=np.maximum(xy[:,0]-low[:,0],high[:,0]-xy[:,0]),yerr=np.maximum(xy[:,1]-low[:,1],high[:,1]-xy[:,1]),fmt='o',ms=4,label='Published ion-collector markers (digitized)');grid=np.linspace(0,1150,400);ax.plot(grid,curve(grid,published),label='Curve reconstructed from paper annotations');ax.plot(grid,curve(grid,fit.x),'--',label='Fit on voltage groups below 9');ax.scatter(V[test],I[test],s=80,facecolors='none',edgecolors='red',label='Held-out voltage groups 9 and 10');ax.set(xlabel='Collector bias (V)',ylabel='Net collector current (A)',title='TMX published benchmark: Figure 15 recovery');ax.text(.02,.03,'Bars: digitization sensitivity only; experimental errors unavailable.\nBarr & Moir (1983), DOI 10.13182/FST83-A20820',transform=ax.transAxes,fontsize=8);ax.legend(fontsize=8);ax.grid(alpha=.2);fig.savefig(out/'FIGURE15_RECOVERY.png',dpi=160);plt.close(fig)
print('checks',sum(c['passed'] for c in checks),'/',len(checks));print('fit',fit.x,'heldout_RMSE_A',report['curve_reconstruction']['heldout_fit_RMSE_A']);assert all(c['passed'] for c in checks)
