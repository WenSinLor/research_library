---
citation_key: Terajima2025multifunctional
title: "Multifunctional Physical Reservoir Computing in Soft Tensegrity Robots"
authors: "Terajima et al."
year: 2025
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - soft-robotics
  - embodied-intelligence
  - robot-learning
  - dynamical-systems
---

# Terajima2025multifunctional — Multifunctional Physical Reservoir Computing in Soft Tensegrity Robots

## 1. Core contribution

This paper studies multifunctional physical reservoir computing in soft tensegrity robots. It argues that one body-environment system can support several learned behaviors and attractor-like operating modes when used as a reservoir. The contribution is a dynamical account of multifunctionality, including behavior retrieval and the appearance of untrained attractors. It expands embodied PRC from single-task control toward richer behavioral repertoires.

## 2. Method / mechanism / evidence

The authors simulate tensegrity robots and train readouts so the same physical reservoir supports multiple target attractors or behaviors. They analyze basins of attraction, multistability, and how initial conditions or internal state can retrieve different learned patterns. The study also identifies untrained attractors that arise from the learned closed-loop system. The evidence is numerical but directly focused on embodied robot dynamics.

## 3. Key takeaway and limitation

The main takeaway is that body dynamics can host more than one learned mode, which makes physical reservoirs relevant to adaptive embodied control rather than one-off pattern generation. At the same time, multistability introduces ambiguity because unintended attractors may appear. The main limitation is that the study is simulation-based and does not yet show the same repertoire on hardware subject to real-world disturbances. It establishes a useful dynamical picture that still needs experimental grounding.

## 4. Open question

How can embodied reservoirs support multiple useful behaviors while suppressing or exploiting the unintended attractors that appear between them?
