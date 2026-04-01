# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-ninety-min

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14` (continuation probe)  
**Context:** verifier-oracle-model  
**Outcome:** INCONCLUSIVE

## Hypothesis tested

If **`r=9`**, **`d=3`** feasibility for **`n=14`**, **`{7,8}`** is decidable on the **~15 GiB** automation host, a **90-minute** wall-clock run on **`d=3` only** (unbounded memo, no recomputation of **`d=1,2`**) should finish and print **`feasible=true/false`**.

## Finding

**Negative for decidability at this budget:** **`timeout 5400` (90 min)** on **`python3 …/script.py --skip-baseline --r-single 9 --lru-maxsize 0 --d-min 3 --d-max 3`** ended with **exit 124** after printing only **`probing d=3 ...`**. **`script.py`** was extended with **`--d-min` / `--d-max`** (baseline path still probes full **`1..n`**). **`results.md`** / **`notes.md`** updated in the same experiment folder.

## Implications

**`r=9` `d=3`** remains **open**; next attempts need **longer wall-clock**, **more RAM**, or **algorithmic / sharding** changes—not just skipping **`d=1,2`**.

## Analogy pass summary

Same as parent **`n=14 {7,8}`** sweep: exact **`exists_tree`** DP scaling on low-**`r`** / interior **9-sparse** XOR menu.

## Pointer

**`results.md`** and **`script.py`** in `…/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/`.
