---
citation_key: Cazalets2025reshaping
title: "Reshaping Reservoirs with Unsupervised Hebbian Adaptation"
authors: "Cazalets and Dambre"
year: 2025
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# Cazalets2025reshaping — Reshaping Reservoirs with Unsupervised Hebbian Adaptation

## 1. Core contribution

The paper proposes Hebbian Architecture Generation, an unsupervised way to reshape reservoir connectivity from data instead of keeping a random graph fixed. Starting from an almost empty network, the method grows connections between units that co-activate, producing task-adapted reservoir structure without gradient training of recurrent weights. The central claim is that structural self-organization can improve reservoir usefulness while preserving the light training philosophy of reservoir computing. This moves adaptation from readout fitting alone into the reservoir architecture itself.

## 2. Method / mechanism / evidence

The authors define a Hebbian connectivity-growth rule and evaluate the resulting reservoirs across time-series classification and forecasting tasks. They compare against standard Echo State Networks and against reservoirs using other adaptation rules such as intrinsic plasticity and Anti-Oja learning. The strongest reported gains appear in classification settings, where the generated structures consistently improve accuracy. Forecasting results are also competitive, but the advantage is less uniform than in classification.

## 3. Key takeaway and limitation

The useful idea is that task exposure can sculpt a reservoir before supervised readout training, rather than treating reservoir topology as a random nuisance parameter. The method appears especially promising when the input distribution contains repeated activation patterns that connectivity can exploit. Its main limitation is that the benefit is not equally strong across all task families, and the paper leaves open how scaling, stability, and architecture growth behave in more constrained physical substrates. The approach is compelling as a design mechanism, but not yet a universal replacement for conventional reservoir tuning.

## 4. Open question

How well can Hebbian reservoir reshaping survive the wiring, locality, and noise constraints of actual physical reservoir hardware?
