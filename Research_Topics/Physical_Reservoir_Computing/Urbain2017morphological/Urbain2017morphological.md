---
citation_key: Urbain2017morphological
title: "Morphological Properties of Mass-Spring Networks for Optimal Locomotion Learning"
authors: "Urbain et al."
year: 2017
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - morphological-computation
  - robot-learning
---

# Urbain2017morphological — Morphological Properties of Mass-Spring Networks for Optimal Locomotion Learning

## 1. Core contribution

This paper examines how morphology influences locomotion learning in mass-spring robots. It argues that body size, compliance, and resonant frequency shape the ease with which learned controllers can exploit the body's dynamics. The contribution is a morphology-centered analysis of when soft structures support or hinder locomotor learning. It ties reservoir-like body dynamics to concrete movement outcomes.

## 2. Method / mechanism / evidence

The authors simulate mass-spring networks under locomotion tasks, comparing open-loop behavior and closed-loop learning with FORCE-style training. They vary morphology and analyze how the resulting dynamics affect limit cycles, movement robustness, and training performance. Larger or appropriately compliant structures can produce more favorable locomotion characteristics in the reported settings. The evidence is computational, with emphasis on controlled morphology comparisons.

## 3. Key takeaway and limitation

The main takeaway is that learning performance depends on the physics of the body, not just on the learning rule layered on top of it. Compliance and resonance can become assets when matched to the control objective. The main limitation is that the conclusions come from simulated mass-spring systems and may shift when fabrication, friction, sensing, and actuator saturation are introduced. The paper clarifies a design direction rather than final robot hardware guidance.

## 4. Open question

Can morphology search identify bodies that are simultaneously locomotion-efficient and computationally expressive across several tasks instead of one learned behavior?
