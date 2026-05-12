---
citation_key: Aven2024lattice
title: "Lattice Reservoirs: Symmetry Breaking and Information Flow in Physical Reservoir Computing"
authors: "Aven et al."
year: 2024
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# Aven2024lattice — Lattice Reservoirs: Symmetry Breaking and Information Flow in Physical Reservoir Computing

## 1. Core contribution

This paper studies reservoir computers whose topology is constrained to regular spatial lattices, motivated by the local connectivity of many physical substrates. It argues that such lattice reservoirs can remain computationally useful despite extremely simple, fixed structure and uniform edge weights. The central finding is that directed edges, or more generally symmetry breaking that enables information flow, are crucial for strong performance. The authors also show that lattice structure makes reservoir internals easier to inspect than in unstructured random networks.

## 2. Method / mechanism / evidence

The authors simulate square, hexagonal, and triangular lattice reservoirs and compare them with classical Echo State Networks on the NARMA-10 benchmark. Undirected lattices saturate at weaker performance, while directed lattice reservoirs improve with size and approach or exceed ESN performance in several cases. A directed square lattice with global input reaches lower reported NARMA-10 error than the ESN baseline at comparable size, despite using drastically fewer distinct weights. They also introduce greedy shrinking, growing, and edge-restoration analyses, which reveal task-relevant motifs such as a memory-bearing core stem augmented by surrounding computational nodes.

## 3. Key takeaway and limitation

The main takeaway is that physical constraints on topology do not automatically doom reservoir performance; carefully structured local connectivity can work well if the topology supports directional information flow. This matters for real physical reservoirs because global input and highly regular coupling may be much easier to implement than dense, randomized wiring. The paper's main limitation is that its conclusions are derived from simulated ESN-style lattice reservoirs and primarily one benchmark, so the degree to which the same topology principles transfer across tasks and physical substrates remains open. Some observed advantages may also depend on the particular search and evaluation setup used for shrinking or growing reservoirs.

## 4. Open question

Which symmetry-breaking mechanisms and lattice design rules remain effective when these reservoirs are realized in actual physical media with substrate-specific noise, nonideal coupling, and tasks beyond NARMA-10?
