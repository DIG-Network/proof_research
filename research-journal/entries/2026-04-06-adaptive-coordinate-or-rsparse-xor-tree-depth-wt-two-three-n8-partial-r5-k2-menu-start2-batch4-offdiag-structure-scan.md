# Experiment entry — 2026-04-06

**Date:** 2026-04-06  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start2-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Continuation of the **1540**-menu exhaustive driver: after adding **`MENU_START`**, run menus **3–6** in deterministic `combinations` order (`(0,3)` through `(0,6)`) to see whether **`stratum_min_d2`** stays on the **7630** plateau away from the first two pairs.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock ~**869 s** with **`WORKERS=2`**, **`sum_menu_wall_sec≈1697.6`**.

**Implications:**

- Strengthens (still finite) evidence that the **7630** plateau is not an artifact of the first **`combinations`** pairs only.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- Driver now supports **`MENU_START`** + **`MAX_MENUS`** for arbitrary contiguous windows in the menu order.

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=2`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
