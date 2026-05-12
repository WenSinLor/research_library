---
citation_key: Wang2025re
title: "Re-Purposing a Modular Origami Manipulator Into an Adaptive Physical Computer for Machine Learning and Robotic Perception"
authors: "Wang and Li"
year: 2025
created: 2026-05-12
paper_type: "experiment"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - mechanical-intelligence
  - embodied-intelligence
---

# Wang2025re — Re-Purposing a Modular Origami Manipulator Into an Adaptive Physical Computer for Machine Learning and Robotic Perception

## 1. Core contribution

This paper repurposes a modular origami manipulator into an adaptive physical computer for machine learning and robotic perception. It argues that changing the manipulator's bistable configuration alters the reservoir state space and can improve different downstream tasks. The contribution is an embodied reservoir whose mechanical configuration becomes a task-tuning mechanism. It ties adaptive structure to both benchmark computation and perception tasks.

## 2. Method / mechanism / evidence

The authors evaluate the origami system on NARMA-style emulation, payload estimation, payload orientation inference, and input reconstruction. Different structural configurations produce different task advantages, demonstrating that the physical kernel is not computationally fixed. The experiments show a tradeoff between configurations optimized for generic temporal computation and those better suited to perception. The evidence is physical and comparative across several tasks.

## 3. Key takeaway and limitation

The key takeaway is that morphology can become a reprogrammable hyperparameter of embodied computing. A single manipulator need not use one configuration for every task if its geometry can be retuned. The main limitation is that the right configuration remains task dependent, and the paper does not yet provide a fully autonomous method for deciding which physical state to select. It demonstrates adaptivity, but not closed-loop self-optimization.

## 4. Open question

Can adaptive mechanical reservoirs choose their own configuration online from task feedback instead of relying on offline comparison across candidate morphologies?
