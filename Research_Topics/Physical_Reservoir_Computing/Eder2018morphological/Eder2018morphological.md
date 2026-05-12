---
citation_key: Eder2018morphological
title: "Morphological Computation-Based Control of a Modular, Pneumatically Driven, Soft Robotic Arm"
authors: "Eder et al."
year: 2018
created: 2026-05-12
paper_type: "experiment"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - soft-robotics
  - morphological-computation
  - embodied-intelligence
  - robot-learning
---

# Eder2018morphological — Morphological Computation-Based Control of a Modular, Pneumatically Driven, Soft Robotic Arm

## 1. Core contribution

The paper shows that a soft pneumatic arm can act as a computational resource for control rather than only as a plant to be stabilized. Its body dynamics are treated as a reservoir, while simple learned readouts generate pressure commands for target motions. The central contribution is an experimental demonstration of morphological computation for trajectory control in a modular soft robot. It argues that compliant dynamics can support control synthesis instead of merely complicating it.

## 2. Method / mechanism / evidence

The authors sense the arm's internal state, train linear regression readouts, and use the resulting controller to reproduce circular, oval, and spiral end-effector trajectories. They evaluate behavior under multiple motion patterns and report that the learned system can generate useful trajectories from the soft body's own dynamics. Additional tests examine disturbance handling and payload changes. The experimental results support the idea that the arm's morphology supplies temporal and nonlinear structure valuable to the controller.

## 3. Key takeaway and limitation

The practical lesson is that a compliant robotic body can shoulder part of the computation needed for movement generation. That can simplify control design when rich body dynamics are already present. The main limitation is that performance is not uniform across all target paths, especially when trajectories overlap or become harder to separate through the available body state. The paper also points toward hybrid strategies rather than claiming pure morphology solves every control problem.

## 4. Open question

How should soft robot morphology, sensor placement, and readout design be co-optimized so that the same body supports a broader repertoire of controllable trajectories?
