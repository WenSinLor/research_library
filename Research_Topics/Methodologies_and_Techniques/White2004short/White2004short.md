---
citation_key: White2004short
title: "Short-Term Memory in Orthogonal Neural Networks"
authors: "White et al."
year: 2004
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - memory-capacity
---

# White2004short — Short-Term Memory in Orthogonal Neural Networks

## 1. Core contribution

This paper studies how linear recurrent networks store temporal input histories in their transient states. It derives the memory behavior of distributed shift-register architectures and random orthogonal recurrent connectivity, showing that usable memory capacity scales with network size. The contribution is a precise theoretical treatment of short-term memory without relying on attractor-based persistent activity. It directly informs later thinking about reservoir memory and recurrent-state representational capacity.

## 2. Method / mechanism / evidence

The authors define a memory function measuring how well a linear readout reconstructs past scalar inputs from the current network state. They analytically evaluate this quantity for structured and random orthogonal connectivity and analyze the effects of noise and perturbations. Numerical results support the derived memory curves and identify an optimal spectral regime for orthogonal networks. The paper shows that orthogonal recurrence can distribute temporal information efficiently across state dimensions.

## 3. Key takeaway and limitation

The key takeaway is that recurrent networks can carry rich short-term memory in transient dynamics, and that orthogonal structure helps preserve that history. Memory capacity need not be understood only through fixed-point or attractor mechanisms. The main limitation is that the analysis focuses on linear recurrent systems, so it does not settle how memory interacts with nonlinear computation in practical reservoirs or biological circuits. It is foundational on memory scaling, but deliberately narrow in dynamical scope.

## 4. Open question

How should recurrent architectures trade orthogonal memory preservation against the nonlinear transformations required for harder temporal computations?
