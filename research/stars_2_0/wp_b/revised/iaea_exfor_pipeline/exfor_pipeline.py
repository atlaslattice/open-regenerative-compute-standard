#!/usr/bin/env python3
"""IAEA EXFOR acquisition / strict experimental table normalization.
Requires Python 3.9+, standard library only. No fabricated nuclear datasets.
"""
import argparse,csv,datetime,hashlib,json,pathlib,re,urllib.request
from urllib.parse import urlparse
CM=11.006562/(11.006562+1.00727647)
def fetch(url,out):
    p=urlparse(url)
    if p.scheme!="https" or p.hostname not in ("nds.iaea.org","www-nds.iaea.org") or not p.path.startswith("/dataexplorer/api/"):
        raise ValueError("Unrecognized IAEA Data Explorer endpoint")
    req=urllib.request.Request(url,headers={"Accept":"application/json","User-Agent":"Stars2-EXFOR-Research/0.1"})
    with urllib.request.urlopen(req,timeout=35) as f: raw=f.read(24000001)
    if len(raw)>24000000:raise ValueError("Response too large")
    obj=json.loads(raw)
    out.mkdir(parents=True,exist_ok=True)
    (out/"response.json").write_bytes(raw)
    (out/"manifest.json").write_text(json.dumps({
        "origin":"IAEA EXFOR Data Explorer","request_url":url,
        "retrieved_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),
        "data_status":"RAW_UNVALIDATED",
        "warning":"Inspect EXFOR reaction code, channel, energy frame and units before integration."
    },indent=2)+"\n")
    print("Saved RAW response; type:",type(obj).__name__,"bytes:",len(raw))
def parse_exfortable(path,out):
    raw=path.read_bytes();lines=raw.decode("utf-8-sig").splitlines()
    comments=[s.lstrip("# ").strip() for s in lines if s.lstrip().startswith("#")]
    full="\n".join(comments)
    headings=[s for s in comments if "E_in_" in s and "data(" in s]
    if len(headings)!=1 or "E_in_lab(MeV)" not in headings[0] or "data(B)" not in headings[0]:
        raise ValueError("Ambiguous/unsupported units or frame; only E_in_lab(MeV), data(B)")
    reaction=re.search(r"Reaction code:\s*(.+)",full)
    entry=re.search(r"Entry id:\s*([A-Za-z0-9-]+)",full)
    origin=re.search(r"Master file:\s*(https?://\S+)",full)
    if not reaction or ",SIG" not in reaction.group(1).upper() or not entry or not origin:
        raise ValueError("Missing SIG reaction, EXFOR entry/pointer or master source")
    parts=(entry.group(1).split("-")+["","",""])[:3]
    fields=["entry","subentry","pointer","energy_frame","energy_lab_keV","energy_cm_keV","sigma_b","sigma_unc_b","source_url","status"]
    rows=[]
    for s in lines:
        if not s.strip() or s.lstrip().startswith("#"):continue
        cols=s.split()
        if len(cols)!=4:raise ValueError("Unexpected number of observable columns")
        import math
        e,de,y,dy=map(float,cols)
        if not all(map(math.isfinite,(e,de,y,dy))) or min(e,de,y,dy)<0:
            raise ValueError("Negative or nonfinite row")
        rows.append(dict(zip(fields,[*parts,"LAB",e*1000,e*1000*CM,y,dy,origin.group(1),"EXPERIMENTAL_NOT_EVALUATED"])))
    if not rows:raise ValueError("No numeric data")
    out.mkdir(parents=True,exist_ok=True)
    with (out/"normalized_experimental.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    (out/"manifest.json").write_text(json.dumps({
        "source_sha256":hashlib.sha256(raw).hexdigest(),"source_file":path.name,
        "reaction":reaction.group(1),"rows":len(rows),
        "frame":"LAB","conversion":"E_CM=E_lab*11.006562/(11.006562+1.00727647)",
        "upstream_license":"CC-BY-SA-4.0 (exfortables_py); preserve attribution"
    },indent=2)+"\n")
    print("Normalized",len(rows),"experimental rows")
def test():
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d=pathlib.Path(td);p=d/"fixture.txt"
        p.write_text("# Entry id: A1234-002-0\n# Reaction code: (5-B-11(P,A)4-BE-8,,SIG)\n# Master file: https://github.com/IAEA-NDS/exfor_master/blob/main/example.x4\n# E_in_lab(MeV) dE_in_lab(MeV) data(B) ddata(B)\n0.675 0.001 1.0 0.1\n")
        parse_exfortable(p,d/"out")
        with (d/"out"/"normalized_experimental.csv").open() as f:r=next(csv.DictReader(f))
        assert abs(float(r["energy_cm_keV"])-618.4)<1
        assert r["entry"]=="A1234"
    print("Fixture test PASS. Synthetic fixture is NOT a physical cross section.")
if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__); sub=ap.add_subparsers(dest="cmd",required=True)
    f=sub.add_parser("fetch");f.add_argument("--url",required=True);f.add_argument("--out",default="data/exfor/raw")
    p=sub.add_parser("parse-exfortable");p.add_argument("file");p.add_argument("--out",default="data/exfor/normalized")
    sub.add_parser("test")
    args=ap.parse_args()
    if args.cmd=="fetch":fetch(args.url,pathlib.Path(args.out))
    elif args.cmd=="parse-exfortable":parse_exfortable(pathlib.Path(args.file),pathlib.Path(args.out))
    else:test()
