# Experiment entry — 2026-04-07

**Date:** 2026-04-07  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start234-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Sixtieth contiguous window in deterministic `combinations` order: after **`MENU_START=230`**, **`MAX_MENUS=4`** (**`(4,21)…(4,24)`**), run **`MENU_START=234`**, **`MAX_MENUS=4`**, **`WORKERS=2`** — next four menus: split-index pairs **`(4,25)…(4,28)`** as printed by the driver — to test whether **`stratum_min_d2=7630`** persists.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock **`wall_clock_sec≈563.7`** with **`WORKERS=2`**, **`sum_menu_wall_sec=1126.321`**. Per-menu wall **~** **`275–289 s`** (slightly faster than the **`(4,21)…(4,24)`** block).

**Implications:**

- Extends finite evidence through split pairs **`(4,25)…(4,28)`**; next contiguous window **`MENU_START=238`**, **`MAX_MENUS=4`**.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- **`7630`** invariant holds for **seventy-six** menus in this contiguous sweep (including this batch).

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=234`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
