---
citation_key: Kaplan2020scaling
title: "Scaling Laws for Neural Language Models"
authors: "Kaplan et al."
year: 2020
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - scaling-laws
---

# Kaplan2020scaling — Scaling Laws for Neural Language Models

## 1. Core contribution

The paper reports that neural language-model loss follows smooth power-law trends as model size, dataset size, and compute are increased. These trends hold over large scale ranges and suggest that model performance is often more predictable from total scale than from many architectural details. The authors use those regularities to discuss how fixed training compute should be allocated. The contribution is an empirical scaling framework for planning language-model development.

## 2. Method / mechanism / evidence

The paper measures cross-entropy loss across families of autoregressive transformer language models with varied width, depth, dataset size, and compute. It fits separate power laws for parameter count, training data, and compute, then derives compute-efficient operating points from those fitted relations. The extracted text also argues that large models can be more compute-efficient than small models when trained short of full convergence. The evidence is a broad numerical sweep rather than a purely analytic derivation.

## 3. Key takeaway and limitation

The main lesson is that language-model performance exhibits strong, regular scale dependence that can guide experimental planning and hardware budgeting. This paper made scaling laws a central methodology for reasoning about model growth. Its main limitation is that the compute-optimal allocation analysis was later challenged and refined by data-richer studies such as Hoffmann et al. 2022. The observed laws are useful empirical regularities, not immutable theoretical constants.

## 4. Open question

Which scaling relations remain stable when training data composition, optimization recipes, and downstream adaptation change materially?
