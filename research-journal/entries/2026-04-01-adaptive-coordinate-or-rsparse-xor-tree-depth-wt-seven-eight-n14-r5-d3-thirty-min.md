# 2026-04-01 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-thirty-min

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-thirty-min`  
**Context:** verifier-oracle-model  
**Outcome:** INCONCLUSIVE

## Hypothesis tested

A **30-minute** (**1800 s**) wall-clock cap on **`n=14`**, **`{7,8}`**, **`coord + r=5` sparse XOR**, **`d=3`-only** (**`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0`**) is enough to finish the **`exists_tree`** probe and print **`d=3 feasible=`**, resolving whether the **3-minute** timeout was only a **short-budget** artifact.

## Finding

**Timeout:** **`timeout 1800`** ended with **exit 124** after **~1800 s**, still stuck at **`probing d=3 …`** with **no** **`d=3 feasible=`** line. **10×** the **180 s** budget did **not** surface a decision — same **qualitative** behavior as **`r=9` `d=3`** long probes.

## Implications

**`r=5` `d=3`** remains **open**; treat as **multi-hour** / **large-RAM** class alongside **`r=9` `d=3`**. **Wrapper** **`script.py`** reproduces **`timeout 1800`** on the parent **`n=14`** script.

## Analogy pass summary

Fixed **depth** does not cap **DP breadth**; **scaled** wall-clock probes separate **minute-scale** from **hour-scale** shards.

## Pointer

**`results.md`**, **`hypothesis.md`**, **`script.py`** in the experiment folder.
