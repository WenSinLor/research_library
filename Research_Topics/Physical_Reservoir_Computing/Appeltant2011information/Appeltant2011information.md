---
citation_key: Appeltant2011information
title: "Information Processing Using a Single Dynamical Node as Complex System"
authors: "Appeltant et al."
year: 2011
created: 2026-05-12
paper_type: "experiment"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# Appeltant2011information — Information Processing Using a Single Dynamical Node as Complex System

## 1. Core contribution

The paper shows that a reservoir computer does not need a large recurrent network of physical nodes: a single nonlinear node with delayed feedback can emulate a high-dimensional reservoir through time multiplexing. The authors reinterpret sampled points along one delay interval as virtual nodes and train only a linear readout, preserving the reservoir-computing paradigm. Their claim is that delay systems can provide the required nonlinear transformation and fading memory with far simpler hardware. This establishes a practical architecture for physical reservoir computing based on compact delay dynamics.

## 2. Method / mechanism / evidence

The system uses a Mackey-Glass-type delayed nonlinear node, masked inputs, and virtual nodes spaced along the delay line. The authors validate the idea experimentally on isolated spoken-digit recognition using an electronic implementation, and numerically on NARMA-10 dynamical system modeling. They report word error rates as low as 0.2% experimentally and 0.14% in simulation for speech recognition, plus NARMA-10 error down to NRMSE = 0.15 under favorable parameter choices. The paper also studies how feedback gain, input gain, delay length, and virtual-node spacing affect performance, showing that the architecture is effective but parameter-sensitive.

## 3. Key takeaway and limitation

The key takeaway is that temporal structure can substitute for spatial network size: one delayed physical node can act like many interacting reservoir units. That insight made delay-based physical reservoirs technically attractive because they reduce hardware complexity while retaining competitive benchmark performance. The main limitation is that virtual nodes are fed serially rather than in parallel, which introduces a speed tradeoff relative to conventional node arrays. The results also depend on careful tuning of reservoir parameters and do not by themselves prove task-agnostic optimality.

## 4. Open question

How far can single-node delay reservoirs be scaled across tasks before serial processing, parameter sensitivity, or memory-performance tradeoffs make multi-node or hybrid physical architectures preferable?
