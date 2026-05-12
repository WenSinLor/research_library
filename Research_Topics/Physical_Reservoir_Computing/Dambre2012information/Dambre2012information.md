---
citation_key: Dambre2012information
title: "Information Processing Capacity of Dynamical Systems"
authors: "Dambre et al."
year: 2012
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - memory-capacity
  - dynamical-systems
---

# Dambre2012information — Information Processing Capacity of Dynamical Systems

## 1. Core contribution

This paper defines a general information processing capacity for dynamical systems driven by inputs. It shows how total accessible computation can be decomposed across orthogonal functions of past inputs, making the balance between memory and nonlinear transformation explicit. The central theoretical result is that total capacity is bounded by the number of linearly independent observable state variables and reaches that bound under suitable conditions. This gives reservoir computing a sharper systems-level capacity language.

## 2. Method / mechanism / evidence

The authors construct a function basis using orthogonal polynomials and quantify how well a linear readout can reconstruct each target function from system states. They prove capacity bounds and then illustrate the decomposition numerically on example dynamical systems, including the effect of noise. The paper distinguishes capacity spent on direct memory from capacity spent on nonlinear combinations of earlier inputs. The evidence is mainly analytical, supported by controlled computational examples.

## 3. Key takeaway and limitation

The key takeaway is that a reservoir's computational budget is finite and can be allocated differently across memory and nonlinear processing. This framework is useful because it evaluates latent capability rather than a single task score. Its main limitation is practical: capacity decompositions can become expensive or unwieldy for large task spaces, and the link from capacity profile to best hardware design is not automatic. The paper supplies a rigorous diagnostic, not a direct engineering optimizer.

## 4. Open question

How can information processing capacity be turned into a tractable design objective for real physical reservoirs with partial observability and measurement noise?
