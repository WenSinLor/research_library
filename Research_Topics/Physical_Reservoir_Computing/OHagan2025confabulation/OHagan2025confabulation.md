---
citation_key: OHagan2025confabulation
title: "Confabulation Dynamics in a Reservoir Computer: Filling in the Gaps with Untrained Attractors"
authors: "O'Hagan et al."
year: 2025
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - dynamical-systems
---

# OHagan2025confabulation — Confabulation Dynamics in a Reservoir Computer: Filling in the Gaps with Untrained Attractors

## 1. Core contribution

This paper studies "confabulation" in reservoir computers: the emergence of plausible but untrained attractors after learning dynamical behavior. It argues that these additional attractors are not merely trivial data scarcity artifacts but can arise from the reservoir's learned dynamical geometry. The contribution is a systematic treatment of untrained attractor formation and interpolation-like behavior. It reframes some reservoir failure modes as structured dynamics worth understanding directly.

## 2. Method / mechanism / evidence

The authors analyze tasks involving reconstruction of one or multiple attractors and interpolation between related or unrelated target dynamics. They vary training structure and reservoir settings, then inspect when new attractors appear after learning. The paper reports that more data does not automatically remove confabulation and that attractor count, spacing, and reservoir properties all matter. Its support comes from dynamical-systems analysis and simulation.

## 3. Key takeaway and limitation

The key takeaway is that learned reservoirs can invent internally consistent but unintended dynamics, which matters for prediction, control, and generative use. These emergent attractors may sometimes be informative, but they are also a risk when the task demands faithful reconstruction. The main limitation is that the work centers on deliberately structured dynamical examples, so the broader prevalence of confabulation across physical reservoirs is not yet established. The paper sharpens the question more than it closes it.

## 4. Open question

How can reservoir training detect or constrain unintended attractors without suppressing the representational flexibility that makes recurrent dynamics useful?
