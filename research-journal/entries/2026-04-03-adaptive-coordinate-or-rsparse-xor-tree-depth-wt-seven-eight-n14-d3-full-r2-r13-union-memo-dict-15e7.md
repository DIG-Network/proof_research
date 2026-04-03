# Journal entry

**Date:** 2026-04-03  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-d3-full-r2-r13-union-memo-dict-15e7`  
**Context:** verifier-oracle-model (`n=14`, masks of weight 7 or 8)

## Hypothesis (short)

Single-shot **`coord + ⋃_{r=2}^{13} XOR_r`**, **`d=3`**, **`--memo-dict`**, **`1.5×10⁸`** **`exists_tree`** cap would either finish **`d=3`** (**True/False**) or **`PARTIAL`**.

## Outcome

**PASS** — **`d=3 feasible=True`** in **~0.13 s** DP, **`VmRSS_peak` ~68 MB**, cap unused.

## Key finding

The **full multi-arity** XOR split library **refutes** **`d=3`** for this shell **trivially** under **exact** memoization, while **single-`r`** **`r=5`/`r=9`** menus required **huge** budgets and stayed **`False`** on tested shards. The “open full-menu **`d=3`**” thread was an **expressivity** gap (**missing `r` values**), not a **numeric** **budget** **artifact** on **`r=9`** alone.

## Implications

- Re-prioritize **language design** (which splits matter) over **scaling** **single-arity** **XOR** **shards** for this **`n=14`** **`{7,8}`** slice.
- Keep **`--skip-baseline`** when using **`max_exists_calls`** for **narrow** **`d`** probes.

## Analogy pass summary

See `hypothesis.md` (single-shot union of operators vs staged per-`r` enumeration).
