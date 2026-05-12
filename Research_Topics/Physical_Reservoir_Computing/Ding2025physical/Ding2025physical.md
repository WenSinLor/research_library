---
citation_key: Ding2025physical
title: "Physical Reservoir Computing for Biomedical Applications"
authors: "Ding et al."
year: 2025
created: 2026-05-12
paper_type: "review"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - neuromorphic-computing
---

# Ding2025physical — Physical Reservoir Computing for Biomedical Applications

## 1. Core contribution

This review surveys how physical reservoir computing could support biomedical edge intelligence. It organizes the field around hardware reservoirs, biomedical signal types, readout strategies, and deployment requirements such as latency, energy use, bandwidth, and privacy. The paper's main contribution is a domain-specific map of where PRC is already being applied and where it could matter clinically or in wearables. It connects device physics to application constraints rather than reviewing reservoirs in isolation.

## 2. Method / mechanism / evidence

The authors synthesize work on ECG, EEG, EMG, PCG, PPG, and multimodal biosignals together with electronic, photonic, spintronic, and other hardware reservoirs. They discuss how ANN-style and spiking readouts are paired with physical reservoirs in representative biomedical pipelines. The review also compares claimed benefits against practical barriers such as limited hardware maturity, training complexity, and reliability. Its evidence base is literature aggregation across application examples and device demonstrations.

## 3. Key takeaway and limitation

The key takeaway is that biomedical PRC is attractive where continuous temporal sensing meets tight power and data-movement budgets. Physical reservoirs may reduce front-end computational burden, but only if the device, readout, and biosignal preprocessing chain are co-designed. The main limitation is that the field remains fragmented, with many proofs of concept but fewer clinically realistic end-to-end demonstrations. The review identifies a direction, not a settled deployment recipe.

## 4. Open question

What hardware and training stack can make PRC reliable enough for long-duration biomedical use outside carefully controlled laboratory datasets?
