# Experiment entry — 2026-04-06

**Date:** 2026-04-06  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start6-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Third contiguous window in deterministic `combinations` order after **`MENU_START=2`** batch **`(0,3)…(0,6)`**: run menus **7–10** (`(0,7)` through `(0,10)`) to test whether **`stratum_min_d2=7630`** persists further along the **`(0,*)`** prefix of the pair enumeration.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock ~**799 s** with **`WORKERS=2`**, **`sum_menu_wall_sec≈1566.7`**.

**Implications:**

- Extends finite evidence that the **7630** plateau holds for **`(0,7)…(0,10)`**, not only earlier **`(0,*)`** pairs.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- Next contiguous window: **`MENU_START=10`**, **`MAX_MENUS=4`** (or larger batch on a long host).

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=6`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
