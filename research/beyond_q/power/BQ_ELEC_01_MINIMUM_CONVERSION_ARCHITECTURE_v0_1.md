# BQ-ELEC-01 — Minimum Conversion and Electrical Independence Gate
**Version 0.1 | options only: no approved topology**
Model E1 (AC-first), E2 (thermal turbine generation → appropriate HVDC conversion → dedicated loads), E3 (segregated hybrid AC/DC). Each requires published per-stage input/output/efficiency, loss destination, protective isolation, fault current, startup, partial-grid failure, backup ride-through, maintainability and no common-cause unsafe dependency between D-D, D-T and computing.

| Stage | Input unit | Output unit | Efficiency | Loss destination | Gate |
|---|---|---|---|---|---|
| Thermal conversion | MWth | shaft MWe | UNRESOLVED | heat rejection | OPEN |
| Generator | MW shaft | MWe | UNRESOLVED | local heat | OPEN |
| AC/DC distribution | MWe | MWe | UNRESOLVED | local heat | OPEN |
| D-D RF conditioning | MWe | delivered MW RF | UNRESOLVED | cabinet heat | OPEN |
| RF plasma absorption | delivered MW RF | plasma deposition MW | UNRESOLVED | reflected/dissipated | OPEN |
| Reactor cooling/cryogenics | MWe | service | UNRESOLVED | heat | OPEN |
| QPU / HPC rails | MWe | chip/control power | UNRESOLVED | waste heat | OPEN |

**Design rule:** No current selected until power, voltage, protection and fault architecture established. All reactors retain independent safe-state electric capability even if normal power is shared.
