# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-memo-dict`

**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=5`, full **2002** XOR menu, `d=3`-only)

**Hypothesis tested:** Scale **`--memo-dict`** from **3×10⁷** to **10⁸** **`exists_tree`** invocations to seek a complete **`d=3`** verdict or a larger **`memo_dict_size`** at **PARTIAL**.

**Outcome:** INCONCLUSIVE (exit **247**, **SIGKILL**/OOM class — **no** **`PARTIAL:`**, **no** `feasible=`).

**Key finding:** Run lasted **~3.35 h** then was killed mid-`probing d=3 …`. Confirms **full-menu** **`10⁸`** dict is **above** practical memory for this host on the **2002** **`r=5`** envelope; **3×10⁷** dict (**~12.3M** entries, **~112 s** DP) remains the best completed dict datapoint.

**Implications:**

- Next scaling should use **instrumented** smaller steps, **sharded** menus, or more RAM — not a repeat **10⁸** full-menu **`--memo-dict`** on this class of machine.
- **Exit 247** without **`PARTIAL:`** should be classified with prior **OOM** rows in the digest (distinct from budget **PARTIAL** exit **2**).

**Analogy pass summary:** Same as wrapper **`hypothesis.md`** — unbounded dict frontier vs host memory wall.
