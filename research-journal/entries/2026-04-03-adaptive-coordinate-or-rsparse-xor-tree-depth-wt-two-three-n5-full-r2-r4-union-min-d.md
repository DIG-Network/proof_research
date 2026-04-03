# Experiment: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d`  
**Context:** verifier-oracle-model  

## Hypothesis (short)

For `n=5` with mask shell weights `{2,3}` (20 masks) and XOR union `r=2..4`, `min_d` would remain **1** (like the smaller 10-mask, `r=2..3` union case).

## Outcome: **FAIL**

Union language reports **`min_d=2`** (`25` splits, **`dp_sec` ~0**). Hypothesis falsified.

## Key finding

Enlarging the `n=5` shell from **10** weight-2 masks to **20** `{2,3}` masks and extending the union to **`r=2..4`** raises the minimum depth from **1** to **2**. The earlier “`n=5` has `min_d=1` for XOR union” phenomenon is **not** stable under the shell used at `n=6`.

## Implications

- When stating the **`min_d=2` full-union ladder**, qualify that **`n=5`** can still hit **`min_d=1`** only for **restricted shells** (e.g. weight-2-only + smaller union).
- Parent driver gained **`--shells`** for controlled shell ablations.

## Analogy pass summary

See `hypothesis.md` (decision-tree / group-testing analogy; single-split certificate vs mixed-weight obstruction).
