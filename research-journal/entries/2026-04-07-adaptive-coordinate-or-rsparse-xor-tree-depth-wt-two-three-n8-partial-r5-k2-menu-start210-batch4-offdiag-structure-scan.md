# Experiment entry — 2026-04-07

**Date:** 2026-04-07  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`  
**Slug (this run):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-partial-r5-k2-menu-start210-batch4-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, partial `r=5`, `K=2`)

**Hypothesis tested:** Fifty-fourth contiguous window in deterministic `combinations` order: after **`MENU_START=206`**, **`MAX_MENUS=4`** (**`(3,48)…(3,51)`**), run **`MENU_START=210`**, **`MAX_MENUS=4`**, **`WORKERS=2`** — thirteenth **`(3,*)`** block of four: menus **`(3,52)…(3,55)`** — to test whether **`stratum_min_d2=7630`** persists.

**Outcome:** **PASS** (same exit semantics as the driver: **0 < stratum_min_d2 < 107800** for every menu in the batch)

**Key finding:** All four menus yielded **`stratum_min_d2=7630`**, **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives. **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=7630`**. Wall-clock **`wall_clock_sec≈374.4`** with **`WORKERS=2`**, **`sum_menu_wall_sec=747.982`**. Per-menu wall **~179–195 s** (faster than the **`(3,48)…(3,51)`** block).

**Implications:**

- Extends finite evidence in **`(3,*)`** through **`(3,52)…(3,55)`**; next contiguous window **`MENU_START=214`**, **`MAX_MENUS=4`**.
- Full **`C(56,2)=1540`** universality remains **open**; long-job host should still run without **`MAX_MENUS`**.
- **`7630`** invariant holds for **fifty-two** menus in the **`(3,*)`** stratum tested so far in this contiguous sweep (plus prior non-contiguous evidence).

**Analogy pass summary:** Same as parent experiment (enumeration / complete configuration space vs random sample).

**Pointer:** Script `script.py` in the experiment folder; env **`MENU_START=210`**, **`MAX_MENUS=4`**, **`WORKERS=2`**.
