# Experiment entry — 2026-04-07

**Date:** 2026-04-07  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start158-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Forty-first contiguous window in deterministic `combinations` order: after **`MENU_START=154`**, **`MAX_MENUS=4`** (**`(2,48)…(2,51)`**), run **`MENU_START=158`**, **`MAX_MENUS=4`**, **`WORKERS=2`** — menus **`(2,52)…(2,55)`** — to complete the **`(2,*)`** tail and test whether **`stratum_min_d2=7630`** persists.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock **~367 s** with **`WORKERS=2`**, **`sum_menu_wall_sec=728.008`**. Per-menu wall **~174–187 s** (faster than **`(2,48)…(2,51)`**).

**Implications:**

- Completes finite evidence through the **last** **`(2,*)`** pairs **`(2,52)…(2,55)`**; next menus in order begin the **`(3,*)`** block (**`MENU_START=162`**).
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- Next contiguous window: **`MENU_START=162`**, **`MAX_MENUS=4`**.

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=158`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
