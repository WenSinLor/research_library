---
citation_key: Lukosevicius2009reservoir
title: "Reservoir Computing Approaches to Recurrent Neural Network Training"
authors: "Lukosevicius and Jaeger"
year: 2009
created: 2026-05-12
paper_type: "review"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# Lukosevicius2009reservoir — Reservoir Computing Approaches to Recurrent Neural Network Training

## 1. Core contribution

This review organizes the reservoir computing paradigm as a family of recurrent-network training approaches centered on fixed internal dynamics and trainable readouts. It explains how Echo State Networks, Liquid State Machines, and related methods fit under a shared conceptual umbrella. The contribution is a durable taxonomy of reservoir construction, adaptation, and output training. It also situates reservoir computing against broader recurrent neural network practice of its time.

## 2. Method / mechanism / evidence

The authors synthesize theoretical principles, algorithmic variants, readout choices, and hardware or unconventional realizations reported in the literature. They discuss initialization, spectral scaling, readout fitting, regularization, and known failure modes. The review also compares algorithmic alternatives and identifies when RC is appealing from a training or implementation standpoint. Its support is literature integration rather than a single new experimental system.

## 3. Key takeaway and limitation

The enduring takeaway is that RC succeeds by decoupling temporal feature generation from supervised training complexity. That separation remains central in later software and physical reservoirs. The main limitation is historical scope: the survey predates much of today's physical RC hardware, later theoretical refinements, and current benchmark practices. It is foundational context, not a current census of the field.

## 4. Open question

Which ideas from the original RC taxonomy remain most predictive for modern physical reservoirs whose constraints differ sharply from software ESNs?
