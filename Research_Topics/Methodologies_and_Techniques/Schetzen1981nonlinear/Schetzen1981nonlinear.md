---
citation_key: Schetzen1981nonlinear
title: "Nonlinear System Modeling Based on the Wiener Theory"
authors: "Schetzen"
year: 1981
created: 2026-05-12
paper_type: "review"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - dynamical-systems
---

# Schetzen1981nonlinear — Nonlinear System Modeling Based on the Wiener Theory

## 1. Core contribution

This tutorial explains nonlinear system modeling through Wiener theory and its relation to Volterra representations. It lays out how nonlinear systems can be decomposed into orthogonal functional components under stochastic excitation. The paper is meant to make Wiener-kernel methods usable for modeling practice, not to introduce a single isolated theorem. Its contribution is a structured account of the theory, estimation methods, and experimental considerations behind Wiener models.

## 2. Method / mechanism / evidence

Schetzen reviews the Wiener series, its relationship to Volterra kernels, and identification procedures under white Gaussian, nonwhite Gaussian, and some non-Gaussian inputs. The extracted text discusses cross-correlation methods for estimating Wiener kernels and introduces measurement stability to reason about error in experimentally obtained models. Worked derivations and comparisons among excitation cases serve as the paper's evidence. The article is therefore methodological and expository rather than experimental in the modern benchmark sense.

## 3. Key takeaway and limitation

The enduring takeaway is that Wiener theory offers a principled, orthogonal expansion for nonlinear system identification when the excitation assumptions are appropriate. It also clarifies why input statistics matter to kernel estimation and model interpretation. The limitation is that practical usefulness depends on whether the target system fits the representation assumptions and whether higher-order kernels can be estimated stably. Complexity grows quickly as nonlinear order increases.

## 4. Open question

How can Wiener-style nonlinear identification remain tractable for high-dimensional systems without losing the interpretability that made the framework attractive?
