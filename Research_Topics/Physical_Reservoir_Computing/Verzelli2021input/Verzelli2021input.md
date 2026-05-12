---
citation_key: Verzelli2021input
title: "Input Representation in Recurrent Neural Networks Dynamics"
authors: "Verzelli et al."
year: 2020
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - memory-capacity
  - dynamical-systems
---

# Verzelli2021input — Input Representation in Recurrent Neural Networks Dynamics

## 1. Core contribution

This paper proposes a way to describe how linear recurrent reservoirs encode input histories by separating network structure from the specific input sequence. It expresses the state through a controllability matrix and an encoded-input term, making input representation more analyzable. The contribution is a topology-sensitive theoretical lens for understanding memory and representation richness in reservoirs. The extracted PDF is dated 2020 even though the folder key uses 2021.

## 2. Method / mechanism / evidence

The authors analyze linear reservoir dynamics through the rank and nullspace of the controllability matrix. They use this structure to compare reservoir topologies and show why cyclic connectivity can provide a rich yet parsimonious representation of past inputs. Numerical studies connect these structural claims to observed performance behavior. The paper's support is primarily mathematical, with experiments used to illustrate the representational conclusions.

## 3. Key takeaway and limitation

The key takeaway is that reservoir topology determines more than vague "complexity"; it directly shapes which input histories remain distinguishable in state space. This helps explain why some simple structured reservoirs work surprisingly well. The limitation is that the theory is built for linear reservoirs, while many physical RC substrates owe their usefulness to nonlinear device dynamics. The paper offers a clean foundation that still needs extension for richer physical systems.

## 4. Open question

How far can controllability-matrix reasoning be generalized to nonlinear physical reservoirs without losing the interpretability that makes it useful?
