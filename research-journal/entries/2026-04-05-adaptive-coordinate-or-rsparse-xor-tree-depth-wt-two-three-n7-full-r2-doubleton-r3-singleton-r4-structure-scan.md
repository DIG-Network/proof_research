# Experiment entry — 2026-04-05

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-structure-scan`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`, adaptive coordinate + XOR-tree DP)

**Hypothesis tested:** Enumerate languages `coord + full r=2 + two r=3 XOR splits (unordered multiset pair) + one r=4` on the full `630×35 = 22050` grid and measure whether depth-2 certificates require diagonal duplication `i=j` of the triple split or also occur for distinct triple pairs `i<j`.

**Outcome:** PASS (scan completed; baselines OK)

**Key finding:** Histogram `min_d=2` on **1225** cells and `min_d=3` on **20825**. Of the depth-2 cells, **35** lie on the diagonal `i==j` (duplicate triple XOR — reduces to one informative triple) and **1190** have **distinct** `i<j`. So **two different** triple parities plus one quartic still yield `min_d=2` for a **5.7%** slice of off-diagonal cells — strictly richer than “only complementarity for a single triple.” Wall time **~30.6 s**, LRU **4M**.

**Implications:**

- The singleton `3+4` complement classification does **not** describe the full multiset-triple + quartic envelope: **non-redundant** triple pairs matter.
- A next experiment could seek a closed predicate for the **1190** off-diagonal witnesses (bitmask / incidence relation between the two triples and the quad).

**Analogy pass summary:** Group testing with correlated parity pools; second triple parity can interact with a quartic parity to shorten the adaptive decision tree in some configurations.

**Space-definition:** none
