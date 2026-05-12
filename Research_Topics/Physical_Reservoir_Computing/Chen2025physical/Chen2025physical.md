---
citation_key: Chen2025physical
title: "Physical Learning in Reprogrammable Metamaterials for Adaptation to Unknown Environments"
authors: "Chen et al."
year: 2025
created: 2026-05-12
paper_type: "experiment"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - mechanical-intelligence
  - embodied-intelligence
---

# Chen2025physical — Physical Learning in Reprogrammable Metamaterials for Adaptation to Unknown Environments

## 1. Core contribution

This paper demonstrates physical learning in a reprogrammable metamaterial that adapts its stiffness pattern to unknown loading conditions. Rather than learning a purely digital model, the structure updates its own material configuration so that a desired global deformation emerges from local responses. The core contribution is a model-free learning procedure that turns a deformable metamaterial into an adaptive physical system. It positions programmable mechanics as a route to embodied adaptation.

## 2. Method / mechanism / evidence

The authors encode target behavior through local strain objectives and iteratively update cell stiffnesses in hardware. Their experiments show autonomous adaptation to unknown loads in fewer than ten update rounds while reaching roughly percent-level shape error under the reported conditions. They also test robustness to sensor noise, structural damage, and fabrication imperfections, and the learning process continues to converge in those settings. The evidence is therefore direct physical adaptation, not only simulation.

## 3. Key takeaway and limitation

The key takeaway is that local mechanical programmability can support global behavior learning without requiring a high-fidelity environmental model. This is relevant to mechanical intelligence because adaptation occurs through the body's tunable structure itself. The main limitation is that the demonstrations focus on a bounded class of static deformation goals and load cases. The paper does not yet establish how the approach scales to richer dynamics, multi-objective behaviors, or long-lived autonomous operation.

## 4. Open question

Can the same physical-learning principle be extended from static reconfiguration to dynamic, closed-loop adaptation in changing environments?
