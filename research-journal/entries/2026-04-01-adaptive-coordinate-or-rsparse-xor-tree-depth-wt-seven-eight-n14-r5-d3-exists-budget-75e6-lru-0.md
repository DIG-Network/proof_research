# Experiment: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-0

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-0/`  
**Context:** verifier-oracle-model  

**Hypothesis tested:** Same **`max_exists_calls = 7.5×10⁷`** as **75e6/12M LRU** but **`--lru-maxsize 0`** completes with **PARTIAL** or **feasible** on sufficient RAM (no LRU eviction).

**Outcome:** **INCONCLUSIVE** — **exit 247** after **~5085 s** (**~85 min**); stdout stuck at **`probing d=3 …`**; no **`feasible=`** or **`PARTIAL:`**.

**Key finding:** **Unbounded** memo **still** hit **host** **kill** **before** **75M** **cap** **or** **root** **decision** on this machine — **not** a **timeout** **124** **line**. **Slower** **death** **than** **12M** **LRU** **(~8** **min)** **but** **same** **failure** **class**.

**Implications:**

- **`r=5` `d=3`** **on** **`n=14` `{7,8}`** **still** **not** **certified** **here** **;** **compare** **`r=6`** **PASS** **at** **5e7/8M**.
- **Next** **honest** **attempt** **needs** **more** **RAM** **or** **process** **sharding** **/** **external** **run** **;** **avoid** **assuming** **`lru-maxsize`** **0** **fixes** **OOM** **on** **this** **class** **of** **host**.

**Analogy pass summary:** **Bounded** **vs** **unbounded** **transposition** **table** **;** **hypothesis** **falsified** **in** **“completes”** **sense** **—** **kill** **still** **occurs**.

**Space-definition:** none.
