---
citation_key: Sharma2020a
title: "A Neural Scaling Law from the Dimension of the Data Manifold"
authors: "Sharma and Kaplan"
year: 2020
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - scaling-laws
---

# Sharma2020a — A Neural Scaling Law from the Dimension of the Data Manifold

## 1. Core contribution

The paper proposes that neural scaling-law exponents can be explained by the intrinsic dimension of the data manifold. It argues that test loss decreases as a power law in model size because the effective approximation problem lives on a lower-dimensional data structure. The theory predicts an exponent that depends inversely on manifold dimension, and the paper compares that prediction against synthetic and real learning settings. This frames scaling laws as a geometric phenomenon rather than a purely empirical fit.

## 2. Method / mechanism / evidence

Sharma and Kaplan derive a relationship between loss scaling and intrinsic dimension, then test it using teacher-student random-network experiments. The paper also examines image classifiers and GPT-style language models to compare measured scaling behavior with dimensionality-based expectations. The extracted text presents both theoretical predictions and empirical checks, with cross-entropy and mean-squared-error cases discussed explicitly. The support is therefore a mixture of asymptotic reasoning and targeted numerical validation.

## 3. Key takeaway and limitation

The key idea is that scaling exponents may reveal something about data geometry, not only optimizer quality or architecture size. That gives researchers a conceptual handle for comparing task difficulty across domains. The limitation is that intrinsic dimension is itself hard to estimate reliably in large, structured datasets, and the proposed relation is not a universally proven law. The paper is best read as a geometric explanation with partial empirical support.

## 4. Open question

Can intrinsic-dimension estimates from real foundation-model datasets predict scaling behavior accurately enough to guide dataset construction and model planning?
