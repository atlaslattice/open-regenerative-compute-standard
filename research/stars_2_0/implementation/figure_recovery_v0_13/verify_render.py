"""Check recovered vector coordinates against independent Poppler rasterization."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

import fitz
import numpy as np
from PIL import Image
from recover import write_json

def verify(pdf,run):
    run=Path(run);pkg=json.loads((run/'KUHLWEIN_FIG3.json').read_text())
    with tempfile.TemporaryDirectory() as temp:
        prefix=str(Path(temp)/'page4')
        subprocess.run(['pdftoppm','-cropbox','-f','4','-l','4','-scale-to','2400','-singlefile','-png',str(pdf),prefix],check=True)
        im=np.array(Image.open(prefix+'.png').convert('RGB')).astype(int)
    page=fitz.open(pdf)[3];sx=im.shape[1]/page.rect.width;sy=im.shape[0]/page.rect.height
    records=[]
    for trace in pkg['traces']:
        for energy in [.6,1.,1.6,2.4,3.2,3.8,4.2,4.8]:
            val=float(np.interp(energy,trace['energy_cm_MeV'],trace['relative_display_height']))
            px=(96.2204360961914+energy/6*(244.65444946289062-96.2204360961914))*sx
            py=(trace['y0_pdf_pt']-val*(trace['y0_pdf_pt']-trace['y1_pdf_pt']))*sy
            x=int(round(px));y=int(round(py))
            patch=im[y-6:y+7,x-2:x+3]
            if trace['role']=='data': mask=np.max(patch,axis=2)<110
            else:mask=(patch[:,:,0]>180)&(patch[:,:,1]>80)&(patch[:,:,1]<220)&(patch[:,:,2]<130)
            indices=np.argwhere(mask)
            distance=None if len(indices)==0 else float(np.min(np.abs(indices[:,0]+y-6-py)))
            records.append(dict(panel=trace['panel'],role=trace['role'],energy_cm_MeV=energy,
                                nearest_color_vertical_distance_pixels=distance,
                                status='OCCLUDED_OR_UNRESOLVED' if distance is None else 'VISIBLE'))
    visible=[r for r in records if r['nearest_color_vertical_distance_pixels'] is not None]
    maximum=max(r['nearest_color_vertical_distance_pixels'] for r in visible)
    receipt=dict(renderer='Poppler pdftoppm -cropbox, separate from PyMuPDF vector parser',queries=len(records),
                 visible_queries=len(visible),occluded_or_unresolved=len(records)-len(visible),
                 max_visible_vertical_distance_pixels=maximum,
                 preset_gate=dict(min_visible=24,max_vertical_distance_pixels=2),
                 recovery_coordinate_check_passed=len(visible)>=24 and maximum<=2,
                 observations=records,meaning='Figure coordinate/curve recovery check only, not an experimental validation gate')
    write_json(run/'RASTER_CROSSCHECK.json',receipt)
    return receipt

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pdf',default='sources/Kuhlwein2022.pdf');p.add_argument('--run',default='receipts/run001');a=p.parse_args()
    result=verify(a.pdf,a.run)
    if not result['recovery_coordinate_check_passed']:raise SystemExit('Raster cross-check failed')
