# 2026-04-01 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r234-d2

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r234-d2`  
**Context:** verifier-oracle-model  
**Outcome:** PASS

## Hypothesis tested

For **`n=14`**, **`|S| ∈ {7,8}`**, **coord + r-sparse XOR** with **`r ∈ {2,3,4}`**, depth **`d=2`** is **infeasible** (**`min_d ≥ 3`** for each single-arity menu), consistent with the **`n=13`** resolved row where **`min_d(2),min_d(3),min_d(4) > 2`**.

## Finding

Three **`--skip-baseline`** shards with **`--d-min 2 --d-max 2 --lru-maxsize 0`** on the parent **`…-n14/script.py`**:

- **`r=2`:** **`d=2 feasible=False`**, **`dp_sec≈0.03`**
- **`r=3`:** **`d=2 feasible=False`**, **`dp_sec≈0.43`**
- **`r=4`:** **`d=2 feasible=False`**, **`dp_sec≈2.8`**

Prior **`timeout`** reports on **`r=2..4`** were from **full** **`min_d`** sweeps probing **deeper** **`d`**, not from **`d=2`** in isolation.

**Ancillary:** **`r=5` `d=3`-only** with **`timeout 300`** → **exit 124** (no line in **5 min** on this host).

## Implications

- **`n=14`** **`min_d(r)`** row gains **three** **decided** **lower** **bits:** **`r∈{2,3,4}`** all have **`min_d ≥ 3`**.
- Remaining **heavy** work: **`r=5` `d=3`**, **`r=9` `d=3`**, **unions** on **long-wall** hosts.

## Analogy pass summary

Low-**`r`** sparse XOR acts as a **weak measurement** on the **`{7,8}`** shell pair; **shallow** trees need **informative** splits — empirical **`exists_tree`** matches **coding / group-testing** intuition.

## Pointer

**`results.md`**, **`script.py`** in `…/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r234-d2/`.
