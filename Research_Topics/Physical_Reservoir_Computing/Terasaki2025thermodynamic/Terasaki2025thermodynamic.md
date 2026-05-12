---
citation_key: Terasaki2025thermodynamic
title: "Thermodynamic Limit in Learning Period Three"
authors: "Terasaki and Nakajima"
year: 2025
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# Terasaki2025thermodynamic — Thermodynamic Limit in Learning Period Three

## 1. Core contribution

This paper analyzes how random recurrent systems learn a period-three target in the thermodynamic limit. It shows that learning can reshape the attractor landscape in ways that create unstable learned periods, additional untrained attractors, and rich post-learning bifurcation structure. The contribution is a theoretical account of how recurrent learning externalizes dynamical complexity. It also connects naturally to broader reservoir questions about attractor embedding and confabulation.

## 2. Method / mechanism / evidence

The authors study a large-network limit, derive analytical structure for learned period-three behavior, and trace how attractors change after training. They report that post-learning bifurcations can generate many additional periodic behaviors, potentially extending beyond the directly trained target. The analysis is supported by numerical illustrations of the resulting attractor structure. The paper is primarily theoretical rather than application-oriented.

## 3. Key takeaway and limitation

The key takeaway is that recurrent learning can reorganize dynamical systems far beyond the nominal target it was trained on. That matters when reservoirs are used to embed or reproduce attractors. The main limitation is that the paper studies a deliberately stylized target and mathematical limit, so its direct implications for practical physical reservoirs remain indirect. It is a strong mechanism paper, not a deployment paper.

## 4. Open question

Which aspects of this post-learning attractor proliferation persist in finite, noisy, experimentally realized reservoir systems?
