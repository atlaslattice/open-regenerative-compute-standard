"""Audit compact committed results; regenerated meshes are checked if present."""
import hashlib,json
from pathlib import Path

def main():
    root=Path(__file__).resolve().parent
    current=root/'run006'; r=json.loads((current/'RECEIPT.json').read_text())
    checks=0; omitted=[]
    def check(v):
        nonlocal checks
        if not v: raise AssertionError('audit check failed after '+str(checks))
        checks+=1
    check(r['actual_apparatus_net_power_W'] is None)
    check(hashlib.sha256((root/'PROFILES.json').read_bytes()).hexdigest()==r['profiles_sha256'])
    for name,h in r['implementation_sha256'].items():
        check(hashlib.sha256((root/name).read_bytes()).hexdigest()==h)
    for name,h in r['files_sha256'].items():
        f=current/name
        if not f.exists() and f.suffix=='.msh': omitted.append(name); continue
        check(f.exists() and hashlib.sha256(f.read_bytes()).hexdigest()==h)
    for v in r['results']:
        check(v['material_gate']=='BLOCKED_UNQUALIFIED')
        check(v['CAD_mask_comparison_points']==1000 and v['CAD_mask_mismatches']==0)
        check(v['cad_relative_error']<1e-5 and v['mesh_relative_error']<.02)
        check(v['cad_length_unit_m']==1e-6 and v['exported_mesh_length_unit_m']==1.0)
        expected='PASS_NUMERICAL_MESH_ONLY' if v['min_inverse_condition_number']>=.01 else 'BLOCKED_SLIVER_ELEMENTS'
        check(v['mesh_gate']==expected)
    registry=json.loads((root/'MODULE_RETENTION_v002.json').read_text())
    check(len(registry['original_C_inventory'])==26)
    print(json.dumps({'checks_passed':checks,'omitted_generated_meshes':omitted,'status':'PASS_RECEIPT_AUDIT_NOT_PHYSICAL_VALIDATION'},indent=2))

if __name__=='__main__': main()
