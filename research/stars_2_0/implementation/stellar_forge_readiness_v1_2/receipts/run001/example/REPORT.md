# Stellar Forge readiness v.1.2

Observation-policy evaluation only; no laser connection, saturation proof or fusion prediction.

{
  "all_attempts": 4,
  "ready_attempts": 2,
  "status_counts": {
    "ABORTED": 1,
    "READY_IN_TRACE": 2,
    "TIMEOUT_NOT_READY": 1
  },
  "readiness_times_s_conditional_on_ready": [
    3.0,
    6.0
  ],
  "note": "timeouts/aborts retained; conditional times are not an unbiased comparison of different policies"
}

All attempted preparations, including timeouts and aborts, are retained in ATTEMPTS.jsonl. Raw sensor values, specimen and calibration metadata and subsequent-outcome placeholders are preserved.
