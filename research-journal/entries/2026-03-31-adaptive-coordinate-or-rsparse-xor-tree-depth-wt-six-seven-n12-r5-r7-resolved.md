# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-r5-r7-resolved

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/` (same folder as **2026-03-31** partial **PASS**; this entry records **completion** of **standalone** **`r=5`** **/** **`r=7`** **and** **refreshed** **`results.md`** **/** **`hypothesis.md`** **.)

**Context:** `verifier-oracle-model` — **n=12**, **wt ∈ {6,7}**, **1716** masks.

**Hypothesis (delta):** Resolve **missing** **`min_d(5)`**, **`min_d(7)`** **rows** **that** **were** **OOM** **/** **exit** **137** **in** **monolithic** **or** **prior** **rerun** **attempts** **.**

**Outcome:** **PASS**

**Key findings:**

- **Per-process** **`python script.py --skip-baseline --r-single r`** **completes** **`r=5`** **and** **`r=7`** **(** **~393s** **and** **~313s** **DP** **respectively** **on** **this** **host** **)** **—** **no** **disk** **memo** **needed** **;** **isolate** **peak** **LRU** **footprint** **.**
- **Full** **`min_d(r)`**, **`r=2..11`:** **`6,4,3,4,2,4,3,4,3,2`**. **Interior** **bumps** **`r∈{5,7,9}`** **;** **`r=6`** **and** **`r=11`** **at** **depth** **2** **.**
- **Formal** **H2** **(** **hypothesis** **prefix** **non-increasing** **`r=2..5`** **)** **is** **false** **(** **`4→3→4`** **)** **.**

**Implications:**

- **Supersedes** **INCONCLUSIVE** **`…-n12-rerun-r5-r7`** **for** **resource** **diagnosis** **:** **shard** **by** **`r`** **,** **not** **SQLite-per-state** **.**
- **099-style** **`min_d(6),min_d(7)>min_d(5)`** **still** **absent** **:** **`min_d(6)=2`**, **`min_d(5)=min_d(7)=4`** **.**

**Analogy pass:** unchanged from **`hypothesis.md`** **(** **scale** **098–100** **to** **`(12,{6,7})`** **)** **.**

**Space-definition:** none.
