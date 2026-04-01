# 2026-04-01 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-three-min

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-three-min`  
**Context:** verifier-oracle-model  
**Outcome:** INCONCLUSIVE

## Hypothesis tested

A **180 s** wall-clock cap on **`n=14`**, **`{7,8}`**, **`coord + r=5` sparse XOR**, **`d=3`-only** (**`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0`**) either finishes and prints **`feasible=`**, or proves the shard is **lightweight**.

## Finding

**Timeout:** **`timeout 180`** ended with **exit 124** after **`probing d=3 …`** with **no** **`d=3 feasible=`** line. **Same qualitative pattern** as the **`r=9` `d=3`** ninety-minute probe — **`d=3`** layer appears **wide** / **expensive**, not **sub-minute**.

## Implications

**`r=5` `d=3`** remains **undecided** at this budget; **longer** wall-clock, **more RAM**, or **algorithmic / sharding** work still required (**wrapper** **`script.py`** reproduces the command).

## Analogy pass summary

**DP width** at a fixed **depth probe** can still be huge — **timeout** as **empirical** complexity probe.

## Pointer

**`results.md`**, **`hypothesis.md`**, **`script.py`** in the experiment folder.
