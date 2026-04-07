# Experiment entry — 2026-04-07

**Date:** 2026-04-07  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start130-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Thirty-fourth contiguous window in deterministic `combinations` order: after **`MENU_START=126`**, **`MAX_MENUS=4`** (**`(2,20)…(2,23)`**), run **`MENU_START=130`**, **`MAX_MENUS=4`**, **`WORKERS=2`** — menus **`(2,24)…(2,27)`** — to test whether **`stratum_min_d2=7630`** persists deeper in the **`(2,*)`** block.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock **~571 s** with **`WORKERS=2`**, **`sum_menu_wall_sec≈1141.742`**. Per-menu wall **~282–289 s** (similar to the **`(2,20)…(2,23)`** window).

**Implications:**

- Extends finite evidence through **`(2,24)…(2,27)`**; the **7630** plateau continues in the **`(2,*)`** segment.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- Next contiguous window: **`MENU_START=134`**, **`MAX_MENUS=4`** (or larger batch on a long host).

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=130`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
