"""Hash-bound extraction of published alpha spectra. Original XLS files unchanged."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import urllib.request

import xlrd

ROOT = Path(__file__).resolve().parent
ANGLES = ('30', '45', '60', '75', '90', '115', '135', '160')


def load_source(folder, number):
    index = json.loads((ROOT / 'SOURCE_INDEX.json').read_text())
    spec = next(s for s in index if s['number'] == number)
    path = Path(folder) / spec['filename']
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != spec['sha256']:
        raise ValueError('primary workbook identity mismatch: ' + path.name)
    return xlrd.open_workbook(file_contents=raw)


def extract_pair(book, sheet, error_sheet, *, angle_lab_deg=None):
    s, e = book.sheet_by_name(sheet), book.sheet_by_name(error_sheet)
    if (s.nrows, s.ncols) != (e.nrows, e.ncols):
        raise ValueError('spectrum/error dimensions differ')
    if s.nrows != 102:
        raise ValueError('unexpected energy bin count')
    for col in range(1, s.ncols):
        if s.cell_value(0, col) != e.cell_value(0, col):
            raise ValueError('proton energy mismatch')
    rows = []
    for i in range(2, s.nrows):
        energy = s.cell_value(i, 0)
        if energy != e.cell_value(i, 0):
            raise ValueError('alpha energy mismatch')
        if not math.isclose(energy, 0.045 + (i-2)*0.09, abs_tol=1e-12):
            raise ValueError('unexpected bin centers')
        for j in range(1, s.ncols):
            ep, value, error = s.cell_value(0, j), s.cell_value(i, j), e.cell_value(i, j)
            if not all(isinstance(x, (float, int)) and math.isfinite(x) for x in (ep, value, error)) or value < 0 or error < 0:
                raise ValueError('invalid source cell')
            cell = xlrd.formula.colname(j) + str(i+1)
            rows.append(dict(record_id=sheet+':'+cell, sheet=sheet, value_cell=cell,
                error_sheet=error_sheet, error_cell=cell,
                E_proton_LAB_MeV=ep, E_alpha_CM_center_MeV=energy,
                bin_width_MeV=0.09, detector_angle_LAB_deg=angle_lab_deg,
                X_CM_mb_sr_per_source_bin=value, statistical_error_CM_mb_sr=error,
                observable='DETECTED_ALPHA_COUNTS_PER_LUMINOSITY_PER_CM_SOLID_ANGLE_BIN',
                coverage='ABOVE_ARTICLE_RANGE_REQUIRES_RECONCILIATION' if ep > 3.8 else 'WITHIN_ARTICLE_ENERGY_RANGE',
                source_cell_status='REPORTED_ZERO_ACCEPTANCE_UNQUALIFIED' if value == 0 else 'REPORTED_NONZERO',
                angle_status='SHEET_NAME_MATCHES_ARTICLE_LAB_DETECTOR' if angle_lab_deg is not None else 'NOT_EXPLICIT_IN_LOW_ENERGY_SHEET'))
    return rows


def extract_all(book):
    rows = []
    for angle in ANGLES:
        rows += extract_pair(book, angle, angle+'err', angle_lab_deg=float(angle))
    rows += extract_pair(book, 'Ep 150-400', 'Ep 150-400 err')
    if len(rows) != 22100 or len({r['record_id'] for r in rows}) != len(rows):
        raise ValueError('unexpected record count or duplicate cell ID')
    return rows


def compare_predictions(rows, predictions):
    """Residuals for exactly matching CM observables; no fit or reduced-chi2 claim."""
    observed = {r['record_id']: r for r in rows}
    out, seen = [], set()
    for p in predictions:
        key = p['record_id']
        if key not in observed or key in seen:
            raise ValueError('unknown or duplicate prediction ID')
        seen.add(key)
        r = observed[key]
        if p.get('observable') != r['observable'] or p.get('frame') != 'CM':
            raise ValueError('observable/frame mismatch: LAB cannot substitute for CM')
        value = p['prediction_CM_mb_sr_per_source_bin']
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError('invalid prediction')
        if r['coverage'] != 'WITHIN_ARTICLE_ENERGY_RANGE' or not r['X_CM_mb_sr_per_source_bin'] or not r['statistical_error_CM_mb_sr']:
            raise ValueError('source acceptance or coverage unresolved for residual calculation')
        residual = value-r['X_CM_mb_sr_per_source_bin']
        out.append(dict(record_id=key, residual_CM_mb_sr=residual,
            standardized_residual_STAT_ONLY=residual/r['statistical_error_CM_mb_sr']))
    if not out:
        raise ValueError('empty predictions')
    return dict(status='RESIDUAL_DIAGNOSTIC_NOT_VALIDATION', compared_cells=len(out),
        total_available_cells=len(rows), rows=out,
        omissions='No inferred degrees of freedom, fit, independence, systematic covariance or held-out validation.')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--sources', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--download', action='store_true')
    p.add_argument('--predictions', type=Path)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('output already exists')
    index = json.loads((ROOT/'SOURCE_INDEX.json').read_text())
    if a.download:
        a.sources.mkdir(parents=True, exist_ok=True)
        for spec in index:
            target = a.sources/spec['filename']
            if target.exists():
                continue
            raw = urllib.request.urlopen(spec['url'], timeout=30).read()
            if hashlib.sha256(raw).hexdigest() != spec['sha256']:
                raise ValueError('download hash mismatch')
            with target.open('xb') as f:
                f.write(raw)
    book = load_source(a.sources, 2)
    rows = extract_all(book)
    elastic = load_source(a.sources, 1)
    anchor = next(r for r in rows if r['sheet']=='90' and r['E_proton_LAB_MeV']==1.4 and math.isclose(r['E_alpha_CM_center_MeV'],4.635))
    notes = [book.sheet_by_name('Notes').cell_value(i,0) for i in range(23)]
    summary = dict(status='SOURCE_REPRODUCED_NOT_APPARATUS_CALIBRATED', python=platform.python_version(), xlrd=xlrd.__version__,
        spectrum_cells=len(rows), matched_error_cells=len(rows),
        above_article_range_cells=sum(r['coverage']!='WITHIN_ARTICLE_ENERGY_RANGE' for r in rows),
        reported_zero_cells=sum(r['X_CM_mb_sr_per_source_bin']==0 for r in rows),
        anchor=dict(record=anchor, paper_rounded_value_mb_sr=4.28,
            rounded_match=round(anchor['X_CM_mb_sr_per_source_bin'],2)==4.28),
        source_notes=notes, alpha_elastic_workbook_sheets=[(s.name,s.nrows,s.ncols) for s in elastic.sheets()],
        sources=index, code_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.glob('*.py')})
    comparison = None if a.predictions is None else compare_predictions(rows, json.loads(a.predictions.read_text()))
    a.out.mkdir(parents=True, exist_ok=False)
    with (a.out/'SPECTRA.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (a.out/'RECEIPT.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    if comparison is not None:
        (a.out/'PREDICTION_RESIDUALS.json').write_text(json.dumps(comparison,indent=2,allow_nan=False)+'\n')
    (a.out/'MANIFEST.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in a.out.iterdir()},indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ('status','spectrum_cells','matched_error_cells','above_article_range_cells','reported_zero_cells')}))


if __name__ == '__main__':
    main()
