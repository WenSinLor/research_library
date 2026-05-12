---
citation_key: Fedder1994simulation
title: "Simulation of Microelectromechanical Systems"
authors: "Fedder"
year: 1994
created: 2026-05-12
paper_type: "simulation"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
---

# Fedder1994simulation — Simulation of Microelectromechanical Systems

## 1. Core contribution

This dissertation develops lumped-parameter simulation methods for microelectromechanical systems and demonstrates how those models can support device design, control, and microassembly. It derives first-order component models for plates, damping, springs, electrostatic actuators, and capacitive sensors, then implements them in SPICE and MATLAB workflows. The thesis also builds and tests an integrated MEMS control platform to verify the models under realistic operating conditions. Its contribution is a foundational modeling toolkit paired with experimental validation.

## 2. Method / mechanism / evidence

The work derives analytic expressions for several MEMS building blocks and uses them to simulate coupled mechanical-electrical behavior. A suspended polysilicon plate with capacitive sensing and electrostatic feedback actuators is fabricated as a control testbed, including sigma-delta force-balance operation. The thesis reports controlled vertical displacement and tilt, analyzes low-pressure limit-cycle oscillations, and shows that analytic loop models and simulations predict the observed behavior. A separate microassembly study demonstrates fuse-based temporary anchors, configurable springs, and aluminum microbridge welding for prestress and alignment.

## 3. Key takeaway and limitation

The key takeaway is that compact physical models can make MEMS systems simulatable at the design and control level without abandoning meaningful device physics. This is valuable because system behavior depends on the interaction of mechanics, sensing, actuation, and electronics. The main limitation is historical and methodological: the models are intentionally low-order and were developed for the fabrication processes and device classes available in the early 1990s. They remain instructive, but modern MEMS platforms may need richer multiphysics treatments.

## 4. Open question

How should lumped MEMS simulation frameworks be extended today to preserve interpretability while capturing stronger nonlinearities, fabrication variation, and multiphysics coupling?
