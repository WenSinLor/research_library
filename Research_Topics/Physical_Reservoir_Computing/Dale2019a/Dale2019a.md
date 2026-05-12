---
citation_key: Dale2019a
title: "A Substrate-Independent Framework to Characterize Reservoir Computers"
authors: "Dale et al."
year: 2019
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - physical-reservoir-computing
  - reservoir-computing
  - memory-capacity
---

# Dale2019a — A Substrate-Independent Framework to Characterize Reservoir Computers

## 1. Core contribution

The paper introduces CHARC, a substrate-independent framework for characterizing reservoir computers through behavior rather than implementation details. Its central claim is that different reservoirs can be compared in a common behavioral space even when their physical or numerical substrates differ sharply. The framework is meant to support design, exploration, and fairer comparison of unconventional reservoirs. It is especially relevant to physical reservoir computing, where implementation heterogeneity is a persistent obstacle.

## 2. Method / mechanism / evidence

CHARC maps reservoirs into a behavior space defined by task-independent measures such as kernel rank, generalization rank, and memory capacity. The authors use novelty search to explore that space across Echo State Networks, delay reservoirs, and a carbon nanotube composite substrate. They show that different substrate classes occupy distinguishable but partially overlapping regions, and that behavioral coverage helps explain later task performance. The evidence is comparative: shared metrics reveal relationships that task scores alone would hide.

## 3. Key takeaway and limitation

The important idea is that reservoir assessment should distinguish "what behaviors are reachable" from "how one benchmark happened to score." That distinction is valuable when comparing physical substrates with very different control knobs. The main limitation is that any characterization framework still depends on the chosen measures, and the paper cannot prove that its particular behavior axes are sufficient for all downstream tasks. CHARC is a strong organizing tool, but not the final word on reservoir comparability.

## 4. Open question

Which behavioral descriptors best predict performance across future physical reservoirs whose dynamics differ substantially from the benchmarked substrates?
