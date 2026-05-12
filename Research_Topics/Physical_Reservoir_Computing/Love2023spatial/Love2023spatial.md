---
citation_key: Love2023spatial
title: "Spatial Analysis of Physical Reservoir Computers"
authors: "Love et al."
year: 2023
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - memory-capacity
  - dynamical-systems
---

# Love2023spatial — Spatial Analysis of Physical Reservoir Computers

## 1. Core contribution

This paper introduces spatially resolved measures for analyzing physical reservoirs rather than collapsing them into one global score. It argues that memory and nonlinearity can vary across a substrate, and that this spatial heterogeneity matters for readout design and task performance. The contribution is a localized diagnostic toolkit applied to magnetic skyrmion textures. It shifts analysis from "does the reservoir work?" toward "where in the reservoir is useful computation located?"

## 2. Method / mechanism / evidence

The authors define local measures of memory and nonlinear information processing, then apply them to simulated magnetic reservoirs. They compare how these local properties change with operating conditions and connect the resulting maps to task performance on Mackey-Glass prediction. The study shows both global and local tradeoffs between memory-rich and nonlinear regions. The evidence is numerical but specifically structured to reveal spatial design information unavailable from aggregate metrics alone.

## 3. Key takeaway and limitation

The key takeaway is that physical reservoirs often contain internal computational geography, and readout placement should exploit it. Spatial metrics can therefore inform sensor positioning and parameter selection. The main limitation is that the demonstrated analysis depends on a model system and chosen observables; experimental access to equally clean local diagnostics may be harder. The paper is a useful design lens that still needs broad hardware translation.

## 4. Open question

Can spatial capability maps be measured or approximated directly on experimental reservoirs well enough to guide sensor placement in practice?
