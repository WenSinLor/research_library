---
citation_key: Hoffmann2022training
title: "Training Compute-Optimal Large Language Models"
authors: "Hoffmann et al."
year: 2022
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - scaling-laws
---

# Hoffmann2022training — Training Compute-Optimal Large Language Models

## 1. Core contribution

The paper revises the compute-optimal training rule for large language models by arguing that parameter count and training-token count should scale together. Across hundreds of transformer runs, it finds that many prominent models were undertrained relative to their size. The authors then demonstrate the implication with Chinchilla, a 70B-parameter model trained on 1.4T tokens that outperforms larger prior systems trained with similar compute. The core contribution is a new empirical compute-allocation law for language-model training.

## 2. Method / mechanism / evidence

The study fits scaling relations using more than 400 models spanning roughly 70M to over 16B parameters and 5B to 500B training tokens. It compares alternative ways of fixing compute budgets and estimates the loss-minimizing balance between model size and data. The paper then validates the rule by training Chinchilla and benchmarking it against Gopher and other large models on downstream tasks. The extracted text emphasizes that the compute-optimal frontier shifts toward substantially more data than earlier scaling prescriptions suggested.

## 3. Key takeaway and limitation

The key takeaway is that compute efficiency depends on matching model size to enough data, not simply scaling parameters upward. This changed how practitioners think about large-model training budgets and helped normalize data-rich training regimes. The limitation is that the conclusion is empirical and conditioned on the transformer language-model setting studied in 2022, including its data mixtures and evaluation choices. It should not be read as a universal law for every architecture or training objective.

## 4. Open question

How do compute-optimal scaling rules change when data quality, multimodal corpora, retrieval, or post-training objectives become major parts of the training pipeline?
