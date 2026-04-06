# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Exhaustive **`C(56,2)=1540`** unordered pairs of **`r=5`** XOR splits (**`K=2`**) — same success criterion as prior scans: some menu with **`0 < stratum_min_d2 < 107800`**. Secondary: **`min = max = 7630`** would prove the random-16 plateau universal.

**Outcome:** **INCONCLUSIVE** — full **1540**-menu run not completed (**~50 h** wall-clock estimated at **4** workers from per-menu **~470 s**). **Smoke** **`MAX_MENUS=2`**, **`WORKERS=2`**: both menus **`(0,1)`**, **`(0,2)`** ⇒ **`stratum_min_d2=7630`**, script **exit 0**.

**Key finding:** Delivers production multiprocessing driver + **`MAX_MENUS`** partial mode. Per-menu cost is **~7×** the **`r=6` `K=2`** cell (**7630** vs **107800** depth-2 witnesses), so exhaustive **`r=5` `K=2`** is much heavier than the **378**-menu **`r=6`** scan despite only **~4×** more menus.

**Implications:**

- Long-job host needed for definitive **`min`/`max`** over **1540**.
- If full run confirms **`7630`** everywhere, pursue closed form **`2×3850−70`** vs **`len(p4)=70`**.

**Analogy pass summary:** Complete enumeration removes sampling bias from the random-16 **`K=2`** probe; compute cost is the limiting factor.

**Space definition:** none
