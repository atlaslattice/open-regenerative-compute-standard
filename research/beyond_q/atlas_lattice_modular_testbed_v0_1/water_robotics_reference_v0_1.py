"""Deterministic illustrative water/robot maintenance simulation. All defaults HYPOTHETICAL."""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Config:
    days: int = 365
    daily_water_demand_m3: float = 20.0
    nominal_recovery_fraction: float = 0.92
    daily_degradation: float = 0.001
    fault_threshold: float = 0.75
    inspection_every_days: int = 7
    repair_duration_days: int = 2
    repair_consumes_spares: int = 1
    initial_spares: int = 6
    resupply_day: int | None = None
    resupply_spares: int = 0
    daily_power_kwh: float = 90.0

def simulate(c: Config = Config()):
    if c.days < 1 or not 0 <= c.nominal_recovery_fraction <= 1 or not 0 < c.fault_threshold <= 1:
        raise ValueError("invalid model parameters")
    if c.inspection_every_days <= 0 or c.repair_duration_days <= 0 or c.initial_spares < 0:
        raise ValueError("invalid maintenance parameters")
    efficiency, spares, downtime, events = 1.0, c.initial_spares, 0, []
    supplied = recovered = makeup = energy = outage = 0.0
    for day in range(1, c.days + 1):
        if c.resupply_day == day:
            spares += c.resupply_spares
            events.append({"day":day,"event":"resupply","quantity":c.resupply_spares})
        if downtime:
            outage += c.daily_water_demand_m3
            events.append({"day":day,"event":"maintenance_downtime"})
            downtime -= 1
            if downtime == 0:
                efficiency = 1.0
                events.append({"day":day,"event":"repair_completed"})
            continue
        efficiency = max(0.0, efficiency - c.daily_degradation)
        recovery = min(1.0, c.nominal_recovery_fraction * efficiency)
        supplied += c.daily_water_demand_m3
        recovered += c.daily_water_demand_m3 * recovery
        makeup += c.daily_water_demand_m3 * (1.0 - recovery)
        energy += c.daily_power_kwh
        if day % c.inspection_every_days == 0:
            events.append({"day":day,"event":"robotic_inspection","condition":round(efficiency,6)})
            if efficiency < c.fault_threshold:
                if spares >= c.repair_consumes_spares:
                    spares -= c.repair_consumes_spares
                    downtime = c.repair_duration_days
                    events.append({"day":day,"event":"qualified_repair_started","spares_used":c.repair_consumes_spares})
                else:
                    events.append({"day":day,"event":"unrepaired_fault_no_qualified_spare"})
    return {"model":"hypothetical_water_robotics_reference_v0_1","config":asdict(c),
            "metrics":{"water_served_m3":round(supplied,6),"water_recovered_m3":round(recovered,6),
                       "makeup_water_m3":round(makeup,6),"unserved_demand_m3":round(outage,6),
                       "electricity_kwh":round(energy,6),"qualified_spares_remaining":spares,
                       "repair_events":sum(e["event"]=="qualified_repair_started" for e in events)},
            "events":events}

if __name__ == "__main__":
    print(json.dumps(simulate(),indent=2))
