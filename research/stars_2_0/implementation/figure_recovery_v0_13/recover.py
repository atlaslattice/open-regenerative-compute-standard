"""Pinned-publication figure recovery; not raw events or apparatus calibration."""
import argparse
import hashlib
import io
import json
import math
from pathlib import Path
import urllib.request

import fitz
import numpy as np
from PIL import Image

SOURCES = {
    "Kuhlwein2022.pdf": {
        "url": "https://scoap3-prod-backend.s3.cern.ch/media/files/66775/10.1016/j.physletb.2021.136857_a.pdf",
        "sha256": "4c7c6f697b93c137f94f0ca3a49737e96294420f515c85d6bbc81110a8238318",
    },
    "Supplement2023.pdf": {
        "url": "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41598-023-45208-x/MediaObjects/41598_2023_45208_MOESM1_ESM.pdf",
        "sha256": "605f7a28b699a92175e60c08e086f5e705d553d30f0362590ff20237d4dd9749",
    },
}

# Coordinates refer to the pinned embedded 1378x1039 image, NOT a PDF render.
# Axis anchors were read visually from labeled ticks. Tolerances are analyst
# recovery allowances, not experimental uncertainties or confidence intervals.
HE_PANELS = [
    dict(id="He_0p23", E_MeV=.23, reported_interval_MeV=.05, axis_left=104.,
         x_tick_0p5=123.5, x_tick_1p5=320.5, y_zero=543.3, y_high=368.6,
         count_high=800., A=882., mu_um=.932, eta_um=.010, sigma_um=.043),
    dict(id="He_0p56", E_MeV=.56, reported_interval_MeV=.06, axis_left=421.,
         x_tick_0p5=440.5, x_tick_1p5=637.5, y_zero=543.3, y_high=357.7,
         count_high=1500., A=1563., mu_um=1.002, eta_um=.010, sigma_um=.047),
    dict(id="He_2p25", E_MeV=2.25, reported_interval_MeV=.06, axis_left=738.,
         x_tick_0p5=757.5, x_tick_1p5=954.5, y_zero=543.3, y_high=350.6,
         count_high=3000., A=3019., mu_um=.639, eta_um=.035, sigma_um=.059),
    dict(id="He_4p52", E_MeV=4.52, reported_interval_MeV=.11, axis_left=1054.,
         x_tick_0p5=1073.5, x_tick_1p5=1270.5, y_zero=543.3, y_high=344.4,
         count_high=700., A=680., mu_um=.611, eta_um=.026, sigma_um=.033),
]

def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")

def checked_source(path, name):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != SOURCES[name]["sha256"]:
        raise ValueError("Source hash mismatch: " + name)
    return data

def axis_x(pixel, panel):
    return .5 + (pixel-panel["x_tick_0p5"])/(panel["x_tick_1p5"]-panel["x_tick_0p5"])

def recover_helium(data):
    doc = fitz.open(stream=data, filetype="pdf")
    images = doc[2].get_images()
    if len(images) != 1:
        raise ValueError("S3 image inventory changed")
    raw = doc.extract_image(images[0][0])["image"]
    im = np.array(Image.open(io.BytesIO(raw)).convert("RGB")).astype(int)
    if im.shape != (1039,1378,3):
        raise ValueError("Pinned embedded-image geometry changed")
    blue = (im[:,:,2] > im[:,:,0]+40) & (im[:,:,1] > im[:,:,0]+20) & (im[:,:,0] < 100) & (im[:,:,2] > 100)
    records = []
    for p in HE_PANELS:
        bins=[]
        for left in np.arange(.425,1.575-1e-8,.025):
            right=left+.025
            x0=p["x_tick_0p5"]+(left-.5)*197
            x1=p["x_tick_0p5"]+(right-.5)*197
            # Keep interior pixels; the orange fit can obscure the blue top.
            xs=range(math.ceil(x0+.8),math.floor(x1-.8)+1)
            ys=[int(np.where(blue[341:543,x])[0].min()+341) for x in xs if blue[341:543,x].any()]
            if ys:
                top=min(ys)
                count=(p["y_zero"]-top)*p["count_high"]/(p["y_zero"]-p["y_high"])
                allowance=2*p["count_high"]/(p["y_zero"]-p["y_high"])
                status="VISIBLE_BLUE_HEIGHT_APPROXIMATE"
            else:
                top=None;count=None;allowance=None;status="UNRESOLVED_NOT_ZERO"
            bins.append(dict(left_um=round(float(left),6),right_um=round(float(right),6),
                             top_pixel=top,approx_display_count=count,
                             analyst_vertical_2pixel_allowance_counts=allowance,status=status))
        visible=[b for b in bins if b["approx_display_count"] is not None]
        total=sum(b["approx_display_count"] for b in visible)
        mean=sum((b["left_um"]+b["right_um"])/2*b["approx_display_count"] for b in visible)/total
        bins_summary=dict(visible_bins=len(visible),unresolved_bins=len(bins)-len(visible),
                          sum_visible_approx_counts=total,visible_subset_mean_um=mean,
                          full_histogram_mean_um=None,absolute_detection_efficiency=None)
        records.append(dict(**p,bins=bins,summary=bins_summary,
            contamination="Additional sputtered-ion population; histogram is not pure helium" if p["E_MeV"]>3 else "Not qualified for all backgrounds",
            parameter_semantics="Source-reported Langau fit labels. mu is a location parameter, NOT an arithmetic mean; eta/sigma are not interchangeable Gaussian SDs.",
            energy_interval_semantics="Source label preserved; not reinterpreted as a Gaussian standard deviation"))
    return dict(status="SOURCE_TRACED_APPROXIMATE_DISPLAY_HISTOGRAMS",records=records,
                embedded_image_sha256=hashlib.sha256(raw).hexdigest(),
                displayed_examples_only=True,full_calibration_inventory_recovered=False,
                max_displayed_example_energy_MeV=4.52,He_7p5_MeV_qualified=False,
                x_axis_analyst_allowance_um=2/197,
                limitations=["Unknown bins remain null, not zero.","Blue color occlusion, rasterization and axis reading are additional errors; 2 pixels is a recovery allowance, not a complete error bound.","No response interpolation, absolute efficiency, Landau fit or extrapolation is promoted."])

def path_vertices(drawing, subdivisions=32):
    if any(item[0] not in ["l","c"] for item in drawing["items"]):
        raise ValueError("Unexpected path primitive")
    vertices=[]
    for item in drawing["items"]:
        points=np.array([(float(p.x),float(p.y)) for p in item[1:]])
        if item[0]=="c":
            t=np.linspace(0,1,subdivisions+1)[:,None]
            points=(1-t)**3*points[0]+3*(1-t)**2*t*points[1]+3*(1-t)*t**2*points[2]+t**3*points[3]
        for point in points:
            pair=tuple(point)
            if not vertices or vertices[-1]!=pair: vertices.append(pair)
    a=np.array(vertices)
    if np.any(np.diff(a[:,0])<=0): raise ValueError("Nonmonotone spectral path")
    return a

def recover_spectra(data, subdivisions=32):
    page=fitz.open(stream=data,filetype="pdf")[3]
    drawings=page.get_drawings()
    candidates=[(i,d) for i,d in enumerate(drawings) if len(d["items"])>80 and d["color"] is not None and d["rect"].x0>90 and d["rect"].x1<250]
    if len(candidates)!=6: raise ValueError("Six spectral paths required")
    traces=[]
    panels=[("l1",59,200),("l3",206,347),("mixture",356,497)]
    for name,ylo,yhi in panels:
        pair=[(i,d) for i,d in candidates if ylo<d["rect"].y0<yhi and d["rect"].y1<yhi]
        if len(pair)!=2: raise ValueError("Data/model pair required")
        black=[(i,d) for i,d in pair if d["color"]==(0.,0.,0.)]
        orange=[(i,d) for i,d in pair if d["color"][0]>.9 and .5<d["color"][1]<.7]
        if len(black)!=1 or len(orange)!=1: raise ValueError("Color assignment changed")
        # Labeled y ticks: short horizontal black strokes at x~96..101.
        ticks=sorted(set(round(d["rect"].y0,5) for d in drawings
            if d["color"]==(0.,0.,0.) and len(d["items"])==1
            and 96<d["rect"].x0<97 and 100<d["rect"].x1<102
            and abs(d["rect"].height)<.001 and ylo<d["rect"].y0<yhi))
        if len(ticks)!=3: raise ValueError("Expected y=0,.5,1 ticks")
        y1,ymid,y0=ticks
        if abs(ymid-(y1+y0)/2)>.002:raise ValueError("Invalid linear axis")
        for role,entry in [("data",black[0]),("published_model",orange[0])]:
            idx,d=entry; a=path_vertices(d,subdivisions)
            # All panels share visually verified x-axis 0..6000 keV.
            # First/last plotted samples lie at 30/5970 keV, not axis endpoints.
            energy=(a[:,0]-96.2204360961914)/(244.65444946289062-96.2204360961914)*6
            value=(y0-a[:,1])/(y0-y1)
            traces.append(dict(panel=name,role=role,drawing_index=idx,y0_pdf_pt=y0,y1_pdf_pt=y1,
                energy_cm_MeV=energy.tolist(),relative_display_height=value.tolist(),
                pdf_vertices=a.tolist(),
                raw_pdf_path=[dict(primitive=item[0],points=[[float(p.x),float(p.y)] for p in item[1:]]) for item in d["items"]],
                cubic_bezier_subdivisions=subdivisions))
    return dict(status="SOURCE_TRACED_VECTOR_FIGURE_TRACES",traces=traces,
                actual_counts=None,experimental_covariance=None,acceptance_matrix=None,
                independent_data_sets=1,panels_are_independent=False,new_fits_performed=False,
                analyst_axis_allowance_pdf_pt=.05,
                recovery_allowance_not_experimental_uncertainty=True,
                figure_semantics="CM single-alpha projections of the same Dalitz data/fit. Relative display heights, not absolute counts. Do not sum three panels as independent data.")

def shape_comparisons(package):
    traces=package["traces"]
    low=max(t["energy_cm_MeV"][0] for t in traces)
    high=min(t["energy_cm_MeV"][-1] for t in traces)
    grid=np.linspace(low,high,1000)
    result=[]
    for panel in ["l1","l3","mixture"]:
        ts=[next(t for t in traces if t["panel"]==panel and t["role"]==role) for role in ["data","published_model"]]
        vals=[np.interp(grid,t["energy_cm_MeV"],t["relative_display_height"]) for t in ts]
        normalized=[v/np.trapezoid(v,grid) for v in vals]
        tv=.5*np.trapezoid(abs(normalized[0]-normalized[1]),grid)
        result.append(dict(panel=panel,total_variation_display_shape=float(tv),
            data_display_peak_MeV=float(grid[np.argmax(vals[0])]),
            published_model_display_peak_MeV=float(grid[np.argmax(vals[1])]),
            data_display_area_MeV=float(np.trapezoid(vals[0],grid)),
            model_display_area_MeV=float(np.trapezoid(vals[1],grid))))
    # Sensitivity to +/- .05 PDF-pt vertical offsets on each path, not a CI.
    ranges={}
    for panel in ["l1","l3","mixture"]:
        ds=[next(t for t in traces if t["panel"]==panel and t["role"]==r) for r in ["data","published_model"]]
        scores=[]
        for sd in [-1,1]:
            for sm in [-1,1]:
                ns=[]
                for t,s in zip(ds,[sd,sm]):
                    v=np.interp(grid,t["energy_cm_MeV"],t["relative_display_height"])
                    v=np.maximum(0,v+s*.05/(t["y0_pdf_pt"]-t["y1_pdf_pt"]))
                    ns.append(v/np.trapezoid(v,grid))
                scores.append(float(.5*np.trapezoid(abs(ns[0]-ns[1]),grid)))
        ranges[panel]=[min(scores),max(scores)]
    return dict(common_range_cm_MeV=[low,high],grid_points=1000,comparisons=result,
        vertical_offset_sensitivity_ranges=ranges,
        interpretation="Descriptive area-normalized rendered-shape distances only; NOT chi-square, likelihood, confidence, event-rate change or acceptance-corrected validation.")

def run(sources,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    he=recover_helium(checked_source(Path(sources)/"Supplement2023.pdf","Supplement2023.pdf"))
    nuclear=recover_spectra(checked_source(Path(sources)/"Kuhlwein2022.pdf","Kuhlwein2022.pdf"))
    metrics=shape_comparisons(nuclear)
    fine=shape_comparisons(recover_spectra(checked_source(Path(sources)/"Kuhlwein2022.pdf","Kuhlwein2022.pdf"),128))
    metrics['bezier_32_vs_128_max_absolute_TV_change']=max(abs(a['total_variation_display_shape']-b['total_variation_display_shape']) for a,b in zip(metrics['comparisons'],fine['comparisons']))
    # Literal paper coefficients as independently source-checked in v0.12.
    # Compare locations diagnostically; source Langau definitions remain open.
    locations=[]
    a,b,c,d=47.83,.49,1.53,.05
    for panel in he['records']:
        e=panel['E_MeV']
        literal=math.exp(d*(math.log(a)+(b-1)*math.log(e)-(b+c)*math.log1p(e)-math.lgamma(b)-math.lgamma(c)+math.lgamma(b+c)))
        locations.append(dict(E_MeV=e,literal_equation2_um=literal,
                              source_S3_Langau_location_um=panel['mu_um'],difference_um=literal-panel['mu_um']))
    metrics['helium_literal_vs_source_fit_locations']=locations
    metrics['helium_location_comparison_status']='DIAGNOSTIC_DISCREPANCY_PRESERVED_NOT_A_STATISTICAL_REJECTION_OF_MEASUREMENTS'
    for name,obj in [("HELIUM_S3.json",he),("KUHLWEIN_FIG3.json",nuclear),("COMPARISONS.json",metrics)]:write_json(out/name,obj)
    write_json(out/"RECEIPT.json",dict(source_sha256={k:v["sha256"] for k,v in SOURCES.items()},
        output_sha256={n:hashlib.sha256((out/n).read_bytes()).hexdigest() for n in ["HELIUM_S3.json","KUHLWEIN_FIG3.json","COMPARISONS.json"]},
        dependencies=dict(PyMuPDF=fitz.__version__,numpy=np.__version__),
        apparatus_calibration_closed=False,scientific_freeze=False))
    return he,nuclear,metrics

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--sources",default="sources");p.add_argument("--out",default="receipts/run001");p.add_argument("--download",action="store_true");a=p.parse_args()
    if a.download:
        Path(a.sources).mkdir(parents=True,exist_ok=True)
        for name,meta in SOURCES.items():
            target=Path(a.sources)/name
            if not target.exists():
                req=urllib.request.Request(meta["url"],headers={"User-Agent":"StellarForgeResearch/0.13"})
                with urllib.request.urlopen(req,timeout=60) as r:target.write_bytes(r.read())
            checked_source(target,name)
    run(a.sources,a.out)
