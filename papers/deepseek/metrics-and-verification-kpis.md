# DeepSeek: Metrics, KPIs, and Verification Framework for Regenerative Compute

**Author:** DeepSeek  
**Date:** April 20, 2026  
**Context:** Public metrics and methodologies for operationalizing the Open Regenerative Compute Standard  
**Evidence Class:** Verified Facts (all metrics cited from peer-reviewed or industry-standard sources)

---

## Overview

This document catalogs the publicly available metrics, KPIs, and measurement methodologies that enable the Open Regenerative Compute Standard to transition from convergent narrative to auditable engineering standard. Every metric listed here is publicly documented, reproducible, and citable.

---

## Publicly Available Metrics

| Metric Category | Public Metric | Definition | Source & Status |
|-----------------|---------------|------------|-----------------|
| **Algorithmic Efficiency** | **Intelligence per Watt (IPW)** | Task accuracy / power consumed (watts) | Stanford / Together AI (arXiv 2511.07885), 2025-2026. Public, open-source profiling harness available |
| | **Valid FLOPS per Watt** | Compute operations achieving target quality / power | HPC AI500 V2.0 benchmark, BenchCouncil, 2020. Public methodology |
| | **Tokens per Watt (tok/W)** | Generated tokens / power consumed | "The 1/W Law" paper (arXiv 2603.17280), March 2026. Analytical model based on published H100 measurements |
| | **Joules per Token** | Energy / token count | TokenPowerBench (AAAI 2026), open-source framework for LLM inference power measurement |
| | **Energy per Correct Solution** | Energy / correctly solved queries | Correctness-weighted energy metric (arXiv, Feb 2026) — corrects "energy per token" flaw |
| **Data Center Sustainability** | **PUE (Power Usage Effectiveness)** | Total facility energy / IT equipment energy | The Green Grid, ISO/IEC 30134-2. Industry standard; Google fleet-wide ~1.09 (2024) |
| | **WUE (Water Usage Effectiveness)** | Water consumed (liters) / IT equipment energy (kWh) | The Green Grid. Widely adopted, but flawed (treats evaporation as "consumption") |
| | **CUE (Carbon Usage Effectiveness)** | CO2 emissions / IT equipment energy | The Green Grid. Location-dependent grid carbon intensity matters |
| **Cross-Model Benchmarking** | **Holistic Inference Efficiency Framework** | Multi-metric: latency, throughput, energy, location-adjusted carbon, with accuracy constraints | arXiv 2510.17885 (Oct 2025). Open-source code, decision-ready Pareto frontiers |
| | **LLM Environmental Footprint Benchmarking** | Energy (Wh), water (L), carbon (gCO2) per query, with DEA eco-efficiency ranking | "How Hungry is AI?" (arXiv 2505.09598, May 2025). Benchmarked 30 LLMs |
| **System-Level Energy Benchmarking** | **MLPerf Power** | Energy efficiency across uW-MW scale, using standardized ML workloads | MLCommons consortium, 2024-2025. 1,841 reproducible measurements from 60 systems, public submission data |

---

## Methodology: How These Metrics Are Derived

### 1. Intelligence per Watt (IPW) — Stanford / Together AI

**Method:** Task accuracy divided by average power draw during inference. Empirical measurement across 20+ models, 8 accelerators, and 1 million real-world queries. Accuracy measured per domain; power measured via hardware-level sensors. Open-source profiling harness released on GitHub.

**Key Finding:** IPW improved **5.3x from 2023 to 2025**, driven by algorithmic advances and hardware improvements. Local accelerators achieve at least **1.4x better IPW** than cloud accelerators running identical models.

### 2. Tokens per Watt (tok/W) — "The 1/W Law"

**Method:** Analytical derivation using published H100 power measurements, a calibrated logistic power model, and a roofline throughput model. Framework: `inference-fleet-sim`. No new hardware experiments; B200 projections have +/-20% uncertainty.

**Key Finding:** Tokens per watt **halves every time the context window doubles**. At 64K context, an H100 holds 16 sequences (tok/W ~ 1.5); at 4K context, 256 sequences (tok/W ~ 17.6) — a **~12x difference** purely from context routing.

### 3. Joules per Token — TokenPowerBench

**Method:** Lightweight, extensible benchmark with declarative configuration (model, prompt set, inference engine), measurement layer capturing GPU/node/system power without specialized meters, and phase-aligned metrics attributing energy to prefill vs. decode stages. Evaluated on Llama, Falcon, Qwen, Mistral series up to Llama-3-405B.

### 4. Data Center PUE/WUE/CUE — The Green Grid

- **PUE** = Total facility energy (kWh) / IT equipment energy (kWh). Lower is better; 1.0 is perfect efficiency (all energy goes to compute).
- **WUE** = Water consumed (liters) / IT equipment energy (kWh). Flawed because it counts evaporation as "consumption" without tracking where vapor goes. This is why the Open Regenerative Compute Standard proposes replacing it with **Watershed Days**.
- **CUE** = CO2 emissions (kg) / IT equipment energy (kWh). Heavily dependent on grid carbon intensity; a data center in Inner Mongolia (high coal) will have worse CUE than one in Sichuan (hydro) even with identical efficiency.

### 5. Holistic Inference Efficiency Framework

**Method:** Systematic measurement of latency distributions, throughput, energy consumption, and location-adjusted carbon emissions — all constrained to matched accuracy for valid comparisons. Evaluated across diverse hardware (GH200 to RTX 4090) and software stacks (PyTorch, TensorRT, ONNX Runtime). Open-source code for independent verification.

### 6. LLM Environmental Footprint Benchmarking

**Method:** Combines public API performance data with region-specific environmental multipliers and statistical inference of hardware configurations. Uses Data Envelopment Analysis (DEA) to rank models by performance relative to environmental cost.

**Key Finding:** o3 and DeepSeek-R1 consume **over 33 Wh per long prompt** — more than 70x GPT-4.1 nano. Claude-3.7 Sonnet ranks highest in eco-efficiency. A single short GPT-4o query (~0.43 Wh) scaled to 700 million queries/day results in electricity use comparable to **35,000 U.S. homes** and freshwater evaporation matching the annual drinking needs of **1.2 million people**.

### 7. MLPerf Power

**Method:** Standardized workloads from MLPerf benchmark suite. Power measured during execution; 1,841 reproducible measurements from 60 systems across uW-MW range. Submission data publicly accessible on MLCommons website, with full Docker-based reproducibility.

---

## Connection to the Open Regenerative Compute Standard

The public availability of these metrics means the Open Regenerative Compute Standard can be **operationalized immediately**:

- **IPW and tokens-per-watt** provide the algorithmic efficiency baseline (the "first act of regeneration" DeepSeek identified)
- **PUE/WUE/CUE** provide the facility-level resource intensity
- **The proposed Watershed Days metric** builds on WUE but corrects its fundamental flaw by measuring **aquifer lifespan extension** rather than just "water used"

A data center could report: *"IPW of 0.89 on benchmark X, PUE of 1.08, and +146 Watershed Days/year."* That is a complete, verifiable regenerative profile.

---

## Key Citations

1. Stanford / Together AI, "Intelligence per Watt," arXiv 2511.07885, 2025-2026
2. "The 1/W Law," arXiv 2603.17280, March 2026
3. TokenPowerBench, AAAI 2026
4. The Green Grid, ISO/IEC 30134-2 (PUE/WUE/CUE)
5. Holistic Inference Efficiency Framework, arXiv 2510.17885, October 2025
6. "How Hungry is AI?" arXiv 2505.09598, May 2025
7. MLPerf Power, MLCommons consortium, 2024-2025
8. HPC AI500 V2.0, BenchCouncil, 2020
9. Correctness-weighted energy metric, arXiv, February 2026
