---
citation_key: Kou2018investigation,
title: "Investigation, Modeling, and Experiment of an MEMS S-Springs Vibrating Ring Gyroscope"
authors: "Kou et al."
year: 2018
created: 2026-05-12
paper_type: "experiment"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
---

# Kou2018investigation, — Investigation, Modeling, and Experiment of an MEMS S-Springs Vibrating Ring Gyroscope

## 1. Core contribution

This paper develops and validates an MEMS vibrating ring gyroscope supported by eight symmetric S-shaped springs. It contributes both a device design and an equivalent stiffness modeling approach intended to generalize beyond one spring geometry. The work connects resonator mechanics, electrode layout, fabrication, and device-level evaluation in one study. Its main claim is that the proposed S-spring architecture can be modeled accurately enough to guide resonant-frequency prediction and practical gyroscope design.

## 2. Method / mechanism / evidence

The authors design an electrostatically driven, capacitively sensed vibrating ring gyroscope, derive an equivalent stiffness model using vibration mechanics and Castigliano-style reasoning, and compare it against finite-element analysis and experiment. They fabricate the prototype and evaluate resonance behavior using processed device dimensions. The paper reports that theoretical and FEA predictions approach the measured resonance values closely after fabrication parameters are included, and it also reports room-temperature bias instability and angle random walk measurements. The evidence is therefore design-model-fabrication-experiment rather than simulation alone.

## 3. Key takeaway and limitation

The key takeaway is that mechanically interpretable reduced-order models can remain useful for MEMS sensor design when they are anchored to fabrication realities. The stiffness model gives a concrete pathway from geometry to resonant behavior. The main limitation is that the paper focuses on one gyroscope architecture and selected static performance metrics, so broader device robustness, temperature behavior, and system-level closed-loop performance are not exhausted. It is a focused design validation paper, not a complete MEMS inertial-navigation study.

## 4. Open question

How well does the S-spring equivalent-stiffness framework transfer to gyroscopes that operate under stronger fabrication variation, packaging effects, or active mode-matching control?
