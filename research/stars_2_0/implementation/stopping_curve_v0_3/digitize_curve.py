"""Reconstruct Overley figure 7 from its original scan, not from mirror values.

Analysis of a scientific plot; no alteration of the source image.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import numpy as np
from PIL import Image
from scipy.ndimage import label, find_objects

ROOT = Path(__file__).resolve().parent


def digitize(png_path):
    im=np.asarray(Image.open(png_path).convert('L'))
    if im.shape != (2153,2600):
        raise ValueError('unexpected raster dimensions')
    # Pixel-to-axis calibration from the plotted ticks, manually inspected.
    ep=np.arange(8)*0.4
    xp=np.array([188.5,504,820,1136.5,1451,1767,2082.5,2400.5])
    stopping=np.arange(9)*2.
    yp=np.array([1802.5,1646,1490,1332,1176.5,1018.5,862.5,705.5,548.5])
    ax=np.polyfit(xp,ep,1);ay=np.polyfit(yp,stopping,1)
    # Interior plot mask excludes axes, annotations and annotation arrows.
    # Areas and mask are fixed from the scan; mirror coordinates never seed detection.
    yy,xx=np.indices(im.shape)
    mask=(im<70)&(xx>230)&(xx<2540)&(yy>650)&(yy<1760)
    mask &= (xx<1450)|((xx<2150)&(yy>1570))|((xx>=2150)&(yy>1620))
    ids,n=label(mask);points=[]
    for k,sl in enumerate(find_objects(ids),1):
        if sl is None:continue
        y,x=np.where(ids[sl]==k)
        if len(x)<50:continue
        px=float(x.mean()+sl[1].start);py=float(y.mean()+sl[0].start)
        points.append(dict(pixel_x=px,pixel_y=py,component_pixels=len(x),
            E_proton_LAB_MeV=float(np.polyval(ax,px)),
            epsilon_eV_cm2_atom=float(np.polyval(ay,py))*1e-15))
    points.sort(key=lambda p:p['E_proton_LAB_MeV'])
    if len(points)!=27:
        raise ValueError('point count changed; inspect the scan instead of silently changing extraction')
    return dict(points=points,axes=dict(x_pixels=xp.tolist(),E_MeV=ep.tolist(),
        y_pixels=yp.tolist(),epsilon_in_1e_minus15=stopping.tolist(),
        affine_E_from_x=ax.tolist(),affine_epsilon_units_from_y=ay.tolist()),
        raster_sha256=hashlib.sha256(Path(png_path).read_bytes()).hexdigest(),
        digitization_working_bounds=dict(E_MeV=0.008,epsilon_eV_cm2_atom=0.08e-15,
            meaning='conservative analysis allowances, NOT measured point errors or statistical confidence bounds'),
        source_experimental_error='4% total probable error, shared calibration; Gaussian interpretation not assigned')


def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    spec=json.loads((ROOT/'SOURCE.json').read_text())
    if hashlib.sha256(a.pdf.read_bytes()).hexdigest()!=spec['pdf_sha256']:
        raise ValueError('primary PDF identity mismatch')
    a.out.mkdir(parents=True,exist_ok=False)
    subprocess.run(['pdftoppm','-f','87','-l','87','-scale-to','2600','-png',str(a.pdf),str(a.out/'figure7')],check=True)
    result=digitize(a.out/'figure7-087.png')
    result['source']=spec
    (a.out/'DIGITIZED_CURVE.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (a.out/'POINTS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['points'][0]));w.writeheader();w.writerows(result['points'])
    print(json.dumps({'points':len(result['points']),'domain_MeV':[result['points'][0]['E_proton_LAB_MeV'],result['points'][-1]['E_proton_LAB_MeV']]}))


if __name__=='__main__':main()
