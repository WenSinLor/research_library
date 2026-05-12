---
citation_key: Matsumura2025phase
title: "Phase Transitions from Linear to Nonlinear Information Processing in Neural Networks"
authors: "Matsumura and Haga"
year: 2025
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - memory-capacity
  - dynamical-systems
---

# Matsumura2025phase — Phase Transitions from Linear to Nonlinear Information Processing in Neural Networks

## 1. Core contribution

This paper analyzes when recurrent neural systems shift from primarily linear information processing toward nonlinear processing. It reports a phase-transition-like change in information capacity as reservoir nonlinearity increases in the presence of noise. The central contribution is a statistical-physics style account of how processing character changes in large networks. It separates this transition from the more familiar order-chaos narrative.

## 2. Method / mechanism / evidence

The authors study capacity decompositions in random networks and derive behavior in the thermodynamic limit. They show that processing capacity can jump discontinuously from linear-dominant to nonlinear-dominant regimes, with the critical point controlled by noise strength and task-relevant settings. Numerical experiments accompany the theory and illustrate finite-size behavior. The support is therefore theoretical with computational confirmation.

## 3. Key takeaway and limitation

The main takeaway is that memory and nonlinearity are not merely smoothly traded; network processing may reorganize sharply across parameter regimes. This matters for reservoirs because small tuning changes can qualitatively alter what computations are accessible. The limitation is that the work focuses on idealized random network settings, so translation to device-specific physical reservoirs is not automatic. It clarifies mechanism more than application.

## 4. Open question

Do comparable processing transitions appear in experimentally accessible physical reservoirs, and can they be exploited for task-adaptive tuning?
