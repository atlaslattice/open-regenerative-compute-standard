#!/usr/bin/env python3
"""ORCS source-evidence and material-allocation guard v0.1. Python stdlib only.

Research ledger validator, NOT a physical manufacturing, food safety or legal
certification. Never infer certified edible material from municipal waste.
"""
from __future__ import annotations
import argparse
import ast
import json
import math
import re
import sys
from pathlib import Path

EVIDENCE_CLASSES = {
    'MEASURED/ADMINISTRATIVE', 'SAMPLED_2026', 'DERIVED_NOT_MEASURED',
    'OPERATOR_REPORTED', 'EXTERNAL_PRIMARY_2026_LAB',
    'EXTERNAL_PRIMARY_2017_BENCH', 'INSTITUTION_REPORTED',
}
BLOCKED_FOOD_SOURCES = {'sewage', 'biosolids', 'grit', 'grease_trap',
                        'municipal_mixed', 'landfill_mixed', 'industrial_brine',
                        'hazardous', 'unknown_mixed'}


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def arithmetic(expr):
    """Numeric arithmetic only; no eval, imports, functions or variables."""
    def rec(node):
        if isinstance(node, ast.Expression):
            return rec(node.body)
        if isinstance(node, ast.Constant) and number(node.value):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div):
            a, b = rec(node.left), rec(node.right)
            if isinstance(node.op, ast.Add): return a + b
            if isinstance(node.op, ast.Sub): return a - b
            if isinstance(node.op, ast.Mult): return a * b
            return a / b
        if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
            return rec(node.operand) * (-1 if isinstance(node.op, ast.USub) else 1)
        raise ValueError('Only numeric arithmetic is allowed in derived formulas')
    return rec(ast.parse(expr, mode='eval'))


def validate_evidence(ledger):
    errors = []
    if ledger.get('schema') != 'orcs.evidence-ledger.v1':
        errors.append('schema: unsupported evidence schema')
    if not isinstance(ledger.get('records'), list):
        return errors + ['records: expected a list']
    if not isinstance(ledger.get('unknowns'), list):
        errors.append('unknowns: expected an explicit list')
    seen = set()
    for pos, rec in enumerate(ledger['records']):
        loc = f'records[{pos}]'
        if not isinstance(rec, dict):
            errors.append(loc + ': expected object')
            continue
        rid = rec.get('id')
        if not isinstance(rid, str) or not rid.strip():
            errors.append(loc + ': missing id')
            continue
        if rid in seen:
            errors.append(loc + ': duplicate id')
        seen.add(rid)
        cls = rec.get('evidence')
        if cls not in EVIDENCE_CLASSES:
            errors.append(loc + ': unknown evidence class')
        if not (isinstance(rec.get('source'), str) and rec['source'].startswith('https://')):
            errors.append(loc + ': source must be https URL')
        if not isinstance(rec.get('scope'), str) or not rec['scope'].strip():
            errors.append(loc + ': missing scope')
        val = rec.get('value')
        if not number(val) and not (isinstance(val, list) and val and all(number(v) for v in val)):
            errors.append(loc + ': numeric value or range required')
        cross_year = bool(re.search(r'cross.?year|fy2025.*2026|2026.*fy2025',
                          ' '.join(str(rec.get(k, '')) for k in ('id','scope','unit','formula')), re.I))
        if cross_year and cls != 'DERIVED_NOT_MEASURED':
            errors.append(loc + ': cross-year estimate promoted to measured claim')
        if cls == 'DERIVED_NOT_MEASURED':
            if not isinstance(rec.get('formula'), str) or not rec['formula']:
                errors.append(loc + ': derived calculation missing formula')
            else:
                try:
                    calc = arithmetic(rec['formula'])
                    if not number(val) or abs(calc - val) > .51:
                        errors.append(loc + ': derived value does not reconcile')
                except (ValueError, ZeroDivisionError, SyntaxError, TypeError, OverflowError) as err:
                    errors.append(loc + f': invalid formula {err}')
            if not cross_year and not rec.get('assumption_basis'):
                errors.append(loc + ': missing derived assumption basis')
        if isinstance(cls, str) and cls.startswith('EXTERNAL_PRIMARY'):
            if not re.search(r'lab|external|bench|not maui', str(rec.get('scope', '')), re.I):
                errors.append(loc + ': external study incorrectly framed as local production')
    return errors


def validate_allocations(document):
    """Fractions cover the same starting lot, not nutrient yields or saleable products."""
    errors = []
    if document.get('schema') != 'orcs.resource-allocation.v1':
        errors.append('allocation schema must be orcs.resource-allocation.v1')
    lots, allocations = document.get('source_lots'), document.get('allocations')
    if not isinstance(lots, list) or not isinstance(allocations, list):
        return errors + ['source_lots and allocations must be lists']
    by_id = {}
    for i, lot in enumerate(lots):
        if not isinstance(lot, dict):
            errors.append(f'lot[{i}]: expected object')
            continue
        lid = lot.get('lot_id')
        if not lid or lid in by_id:
            errors.append(f'lot[{i}]: duplicate/missing id')
            continue
        if not isinstance(lot.get('source_category'), str):
            errors.append(f'lot[{i}]: source category UNKNOWN')
        if not isinstance(lot.get('provenance'), str) or not lot['provenance']:
            errors.append(f'lot[{i}]: provenance UNKNOWN')
        by_id[lid] = lot
    fractions = {}
    ids = set()
    for i, a in enumerate(allocations):
        if not isinstance(a, dict):
            errors.append(f'allocation[{i}]: expected object')
            continue
        aid, lid = a.get('allocation_id'), a.get('lot_id')
        if not aid or aid in ids:
            errors.append(f'allocation[{i}]: missing/duplicate allocation id')
        ids.add(aid)
        if lid not in by_id:
            errors.append(f'allocation[{i}]: unknown source lot {lid}')
            continue
        fraction = a.get('source_fraction')
        if not number(fraction) or not 0 <= fraction <= 1:
            errors.append(f'allocation[{i}]: fraction must be a number in [0,1]')
            continue
        fractions[lid] = fractions.get(lid, 0.) + fraction
        if a.get('food_grade_product'):
            lot = by_id[lid]
            if lot.get('source_category') in BLOCKED_FOOD_SOURCES:
                errors.append(f'allocation[{i}]: restricted source cannot imply edible product')
            if not (lot.get('verified_food_grade') is True
                    and a.get('downstream_media_food_grade_verified') is True
                    and a.get('strain_and_product_regulatory_review') is True):
                errors.append(f'allocation[{i}]: food-grade source, media and product review required')
        if a.get('realized_credit', 0) != 0:
            if not (a.get('observed_receipt') and a.get('audited_attribution')):
                errors.append(f'allocation[{i}]: nonzero credit requires observed and audited receipts')
    for lid, total in fractions.items():
        if total > 1.000000001:
            errors.append(f'lot {lid}: double-counted physical source fractions (>1)')
    return errors


def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ledger', type=Path)
    parser.add_argument('--allocations', type=Path)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        ledger = json.loads(args.ledger.read_text(encoding='utf8'))
        errors = validate_evidence(ledger)
        if args.allocations:
            errors += validate_allocations(json.loads(args.allocations.read_text(encoding='utf8')))
    except (OSError, json.JSONDecodeError, UnicodeError) as err:
        errors = [str(err)]
    result = {'status': 'PASS' if not errors else 'FAIL', 'errors': errors,
              'records_checked': len(ledger['records']) if 'ledger' in locals() and isinstance(ledger.get('records'), list) else 0,
              'limitations': 'Local consistency checks; not independent verification of sources, lab or physical processes'}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result['status'], result['records_checked'], 'records')
        for error in errors:
            print('ERROR', error, file=sys.stderr)
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(cli())
