# Results

**Outcome:** **INCONCLUSIVE** (full **`C(56,2)=1540`** enumeration **not** executed in this session — compute bound)

**Hypothesis (exit semantics):** At least one **`K=2`** partial **`r=5`** menu yields **`0 < stratum_min_d2 < 107800`** ⇒ **PASS**; if **every** menu yields **`stratum_min_d2 ∈ {0, 107800}`** ⇒ **FAIL**.

**Smoke / partial verification (`MAX_MENUS=2`, `WORKERS=2`):**

| Quantity | Value |
|----------|-------|
| Menus run | 2 (first in `itertools.combinations` order) |
| `p5_indices` | `(0,1)`, `(0,2)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `viol_pred_but_not_d2` (each) | **0** |
| `sum_menu_wall_sec` | **918.816** |
| `wall_clock_sec` (parallel) | **461.068** |
| Script exit | **0** (**PASS** on the pre-registered “some menu proper intermediate” criterion — satisfied by smoke menus) |

**Full-run estimate (for **`WORKERS=4`**, no **`MAX_MENUS`):**

- Per-menu CPU wall ~**470 s** on this host (single-menu benchmark **`(0,1)`** ~**469 s**).
- **`1540/4 ≈ 385`** waves ⇒ order **385 × 470 s ≈ 1.8×10⁵ s ≈ 50 h** wall-clock (similar ratio to **`r=6` `K=2`** exhaustive: **378** menus, **~1.67 h** wall, but **~4.3×** more menus and **~4.3×** slower per menu).

**Conclusion:** Production **`script.py`** matches the **`r=6`** exhaustive multiprocessing pattern; **`MAX_MENUS`** supports partial runs. **Universality** of **`stratum_min_d2=7630`** over all **1540** unordered pairs remains **unverified** here — run:

`WORKERS=<n> python3 …/partial-r5-k2-exhaustive-all-1540-offdiag-structure-scan/script.py`

with **no** **`MAX_MENUS`** on a long-job host.

**Script:** `script.py` (smoke: exit **0**).
