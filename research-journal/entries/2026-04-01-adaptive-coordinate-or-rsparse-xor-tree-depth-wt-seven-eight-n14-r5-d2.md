# 2026-04-01 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d2

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14` (targeted `r=5` shard)  
**Context:** verifier-oracle-model  
**Outcome:** PASS

## Hypothesis tested

For **`n=14`**, **`|S| ∈ {7,8}`**, **coord + 5-sparse XOR** menu (**2002** splits), **`min_d > 2`** — equivalently **`d=2`** is **infeasible** — matching the **`n=13`** resolved row where **`min_d(5)=3`**.

## Finding

**Command:** `python3 …/script.py --skip-baseline --r-single 5 --d-min 2 --d-max 2 --lru-maxsize 0`

**Output:** `d=2 feasible=False`, **`dp_sec≈14.0`**, **`build_sec≈2.7`**, script **`PASS`**.

So **`min_d(5) ≥ 3`** on this host; the remaining open question for **`r=5`** is whether **`d=3`** is feasible (**prior runs** timed out on **`d=3`**).

## Implications

- **`n=14`** **`min_d` row** gains one **decided** **bit:** **`r=5`**, **`d=2`** **ruled out** **efficiently** (unbounded memo, **~17 s** wall).
- **`r=9` `d=3`**, **`r∈{2,3,4}`**, and **`r=5` `d=3`** remain **heavy / open** on bounded automation hosts.

## Analogy pass summary

Same structural story as the **`n=13`** **`{7,8}`** sweep: **`exists_tree`** DP on the **5-sparse XOR** refinement of the **Hamming shell** pair **(7,8)**; **low depth** **pruning** before attacking **`d=3`**.

## Pointer

**`results.md`**, **`script.py`** in `…/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/`.
