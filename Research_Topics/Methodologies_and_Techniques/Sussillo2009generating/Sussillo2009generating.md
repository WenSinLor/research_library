---
citation_key: Sussillo2009generating
title: "Generating Coherent Patterns of Activity from Chaotic Neural Networks"
authors: "Sussillo and Abbott"
year: 2009
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - dynamical-systems
---

# Sussillo2009generating — Generating Coherent Patterns of Activity from Chaotic Neural Networks

## 1. Core contribution

The paper introduces FORCE learning for training chaotic recurrent neural networks to produce coherent, task-specific outputs. Instead of suppressing recurrence, the method uses initially irregular network activity as a rich substrate and rapidly shapes the readout so output errors stay small during learning. The trained networks generate temporal patterns, respond to inputs, and switch among multiple outputs. The contribution is a practical online learning rule for turning complex recurrent dynamics into controlled behavior.

## 2. Method / mechanism / evidence

FORCE learning uses a recursive least-squares-style update that repeatedly adjusts output weights while feedback remains active. The paper demonstrates generated waveforms, memory-dependent transformations, switching tasks, and motor-like patterns derived from human motion data. The extracted text highlights that the networks begin in a chaotic regime yet can converge to stable task performance once the output error is held in check. The evidence comes from simulation studies across several dynamical tasks.

## 3. Key takeaway and limitation

The main takeaway is that high-dimensional recurrent dynamics can be trained by controlling a small supervised interface while leaving the bulk network structure intact. This became influential for later work on recurrent computation and reservoir-adjacent training methods. The limitation is that the results are model-based simulations, and biological plausibility or hardware scalability is not resolved by the paper. Performance also depends on staying in a regime where the initial chaotic dynamics are neither too weak nor too hard to tame.

## 4. Open question

What aspects of FORCE learning remain effective when recurrent dynamics are constrained by real physical substrates or noisy analog implementations?
