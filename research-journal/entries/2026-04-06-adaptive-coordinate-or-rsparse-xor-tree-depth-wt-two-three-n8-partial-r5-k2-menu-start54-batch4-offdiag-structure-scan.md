# Experiment entry — 2026-04-06

**Date:** 2026-04-06  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start54-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Fifteenth contiguous window in deterministic `combinations` order: after **`MENU_START=50`** batch **`(0,51)…(0,54)`**, run menus at **`MENU_START=54`**, **`MAX_MENUS=4`** — covering **`(0,55)`** (last pair with first index **0**) and the first three **`(1,*)`** pairs **`(1,2)…(1,4)`** — to test whether **`stratum_min_d2=7630`** persists across the **`(0,*)` → `(1,*)`** boundary.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock ~**860.3 s** with **`WORKERS=2`**, **`sum_menu_wall_sec≈1488.3`**.

**Implications:**

- Extends finite evidence through the **`(0,55)`** endpoint and into **`(1,2)…(1,4)`**; the **7630** plateau is not confined to the **`(0,*)`** prefix alone in this window.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- Next contiguous window: **`MENU_START=58`**, **`MAX_MENUS=4`** (or larger batch on a long host).

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=54`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
