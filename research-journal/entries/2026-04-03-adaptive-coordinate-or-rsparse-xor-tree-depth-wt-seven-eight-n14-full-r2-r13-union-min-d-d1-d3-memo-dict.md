# Journal entry

**Date:** 2026-04-03  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-full-r2-r13-union-min-d-d1-d3-memo-dict`  
**Context:** verifier-oracle-model (`n=14`, masks of weight 7 or 8)

## Hypothesis (short)

Full **`coord + ⋃_{r=2}^{13} XOR_r`** with **`--d-min 1 --d-max 3`** would reveal the true **`min_d`** (prior work only probed **`d=3`** in isolation).

## Outcome

**PASS** — **`min_d=2`**: **`d=1 feasible=False`**, **`d=2 feasible=True`**, **`dp_sec` ~0.23**, **`VmRSS_peak` ~68 MB**.

## Key finding

The **`d=3`-only** full-union run certified **some** depth-3 tree but **not** depth-minimality. With the **same** **`16368`**-split union language, a **depth-2** refutation already exists on the **`{7,8}`** shell.

## Implications

- Report **`min_d`** (scan from **`d_min=1`**) whenever the research question is threshold depth, not mere existence at a fixed **`d`**.
- Single-arity shard hardness at **`d=3`** contrasts with **much smaller** **`min_d`** once the **full** XOR menu is available.

## Analogy pass summary

See `hypothesis.md` (sequential deepening / monotone depth predicate).
