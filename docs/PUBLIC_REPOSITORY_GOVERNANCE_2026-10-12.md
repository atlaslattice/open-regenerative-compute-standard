# GitHub cleanup and publication policy — preserve provenance, expose readiness

2026-10-12. **PROPOSED ORGANIZATION STANDARD / NON-CANON.**

## Public by default, not unreviewed disclosure

Research-ready source material should be accessible in public forkable repositories under clearly stated licenses. Do not publish private third-party datasets, credentials, personal medical/family/security information, security-sensitive operational details, confidential contracts or unconsented source material just because it sits in a connected workspace. A historical private **quarantined** repository is intentionally not an active public canon; audit it first, redact where justified, then selectively publish eligible content with provenance.

## Every entry point must answer

1. What does this project do? What does it NOT do?
2. What runs today, exactly, with copy-paste instructions? Which test claims were independently executed?
3. What is merely designed, synthetic, measured, reported or unknown?
4. What source, timestamp, unit, baseline, contract and geographic boundary supports every key number?
5. Which consent/licensing restrictions and safety controls apply? Who can fork and what may they do?
6. Which missing data, validation, deployment permissions, money and labor are the blockers?

## Proposed folder layout

README.md — project summary / FIRST navigation;
src/ or simulator/ — active executable code;
examples/ — deterministic synthetic inputs;
tests/ — runnable validation;
sites/dongjiakou, sites/corpus-christi, sites/jupiter — profiles, data receipts and source lists;
research/ — papers and studies with evidence class;
policy/ — draft country-neutral and sovereign variations;
docs/ — contributor guide, readiness matrix and source crosswalk;
legacy/ — provenance-preserved older records only if migration authorized; old paths retained or redirected.

**Don't bulk-rename/delete existing archive paths.** Preserve Git history, branch lineage and citation URLs. 'No archives' means no unexplained, orphaned or hidden piles; retained historical artifacts should have an index and non-current status label, not be silently erased.

## Evidence status

MEASURED, REPORTED, DERIVED, MODELED, PROPOSED, UNKNOWN, QUARANTINED; plus source scope and date. Deployments, field measurements and partnership claims start as zero/unknown until verifiable.

## License and reproducibility

Every newly authored plain-text study in this documentation series may be adapted with attribution under CC BY 4.0, except external quotes and third-party included assets whose rights stay with their owners. Existing repositories retain their original licenses, which must be audited repo by repo. Forkability needs compatible license plus working build and fixtures, not just GitHub's Fork button.

## Implementation status

This file is navigational guidance, not a claim that hundreds of repos are already reorganized, private repos are safely published, or release/security scans passed. Actual repo inventory, permissions, and dependency check results must be obtained before such claims.