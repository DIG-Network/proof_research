# Journal entry: 2026-03-31 — lru-memo-exists-tree-n12-r5-r7

**Date:** 2026-03-31  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/lru-memo-exists-tree-n12-r5-r7`  
**Context:** verifier-oracle-model (follow-up to **disk-memo-microbench-exists-tree-n12** and **OOM** on **standalone** **`r=5`/`r=7`**)

**Hypothesis tested:** **LRU-capped** **`(bits, depth)`** memo preserves **correctness** and may **bound** **RSS** so **standalone** **`min_d(5)`**/**`min_d(7)`** finish on **low-RAM** hosts.

**Outcome:** **FAIL** (for **H2** / **practical** **drop-in**); **H1** **PASS** (**`r=6`** **cross-check** **`min_d=2`**).

**Finding:** **`OrderedDict`** **LRU** **matches** **unbounded** memo on **`r=6`** (**`cap=500_000`**). For **`r∈{5,7}`**, **`d≤2`** **finishes** **~1 s** with **`cap=4_000_000`** (**~323k** hits/**misses** at **`d=2`**). **`r=5`**, **`d=3`** **does** **not** **complete** in **120 s** (**`--bench-h2`** **inner** **`timeout`**) nor in **900 s** **manual** **probe** — **eviction** **amplifies** **work** **more** **than** **disk** **latency** **did** **for** **per-state** **persistence**.

**Implications:**

- **Mathematical** **`min_d(5),min_d(7)`** **on** **`(12,{6,7})`** **are** **already** **certified** **by** **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-r5-r7-resolved`** **(** **unbounded** **memo** **/** **process** **sharding** **)** **—** **this** **experiment** **only** **rules** **out** **LRU** **as** **a** **bounded-RAM** **implementation** **shortcut**.
- **Further** **engineering** **for** **low-RAM** **hosts** **needs** **state** **compression** **or** **new** **DP** **structure**, **not** **per-key** **eviction** **on** **`(bits,depth)`**.

**Analogy pass summary:** **CPU** **cache** **eviction** **↔** **DP** **memo** **cap**; **miss** **penalty** **dominates** **when** **working** **set** **≫** **cache**.

**Pointer:** **`results.md`**, **`script.py --bench-h2`** for **automated** **regression**.
