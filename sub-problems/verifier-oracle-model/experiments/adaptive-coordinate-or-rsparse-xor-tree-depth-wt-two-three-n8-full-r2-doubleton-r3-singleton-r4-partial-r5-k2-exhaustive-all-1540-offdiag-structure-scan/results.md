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

---

## Follow-up partial batch (2026-04-06): `MENU_START=2`, `MAX_MENUS=4`

**Driver change:** `script.py` accepts **`MENU_START`** (skip the first *S* menus in `itertools.combinations` order) together with **`MAX_MENUS`** for contiguous windows.

**Run:** `MENU_START=2 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,3)`, `(0,4)`, `(0,5)`, `(0,6)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1697.639** |
| `wall_clock_sec` | **868.629** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** intermediate statistic persists for this **next** block of four menus after `(0,1)` and `(0,2)`; **1540**-menu universality is still not proven.

---

## Follow-up partial batch (2026-04-06): `MENU_START=6`, `MAX_MENUS=4`

**Run:** `MENU_START=6 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,7)`, `(0,8)`, `(0,9)`, `(0,10)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1566.734** |
| `wall_clock_sec` | **798.529** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,7)…(0,10)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=10`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=14`, `MAX_MENUS=4`

**Run:** `MENU_START=14 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,15)`, `(0,16)`, `(0,17)`, `(0,18)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1371.939** |
| `wall_clock_sec` | **687.848** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,15)…(0,18)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=18`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=26`, `MAX_MENUS=4`

**Run:** `MENU_START=26 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,27)`, `(0,28)`, `(0,29)`, `(0,30)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1144.973** |
| `wall_clock_sec` | **573.505** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,27)…(0,30)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=30`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=30`, `MAX_MENUS=4`

**Run:** `MENU_START=30 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,31)`, `(0,32)`, `(0,33)`, `(0,34)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1085.766** |
| `wall_clock_sec` | **542.924** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,31)…(0,34)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=34`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=34`, `MAX_MENUS=4`

**Run:** `MENU_START=34 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,35)`, `(0,36)`, `(0,37)`, `(0,38)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **983.873** |
| `wall_clock_sec` | **492.556** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,35)…(0,38)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=38`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=42`, `MAX_MENUS=4`

**Run:** `MENU_START=42 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,43)`, `(0,44)`, `(0,45)`, `(0,46)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **888.724** |
| `wall_clock_sec` | **444.880** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,43)…(0,46)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=46`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=46`, `MAX_MENUS=4`

**Run:** `MENU_START=46 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,47)`, `(0,48)`, `(0,49)`, `(0,50)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **826.172** |
| `wall_clock_sec` | **413.317** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(0,47)…(0,50)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=50`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-06): `MENU_START=54`, `MAX_MENUS=4`

**Run:** `MENU_START=54 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(0,55)`, `(1,2)`, `(1,3)`, `(1,4)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1488.267** |
| `wall_clock_sec` | **860.264** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for this window (**ends** the **`(0,*)`** streak at **`(0,55)`** and **begins** the **`(1,*)`** block with **`(1,2)…(1,4)`**); **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=58`**, **`MAX_MENUS=4`**.

---

## Follow-up partial batch (2026-04-07): `MENU_START=66`, `MAX_MENUS=4`

**Run:** `MENU_START=66 MAX_MENUS=4 WORKERS=2 python3 …/script.py`

| Quantity | Value |
|----------|-------|
| Menus | 4 — `p5_indices` `(1,13)`, `(1,14)`, `(1,15)`, `(1,16)` |
| `stratum_min_d2` (each) | **7630** |
| `stratum_pred` (each) | **0** |
| `viol_d2_not_pred` (each) | **7630** |
| `min_stratum_d2_across_menus` / `max_…` | **7630** / **7630** |
| `sum_menu_wall_sec` | **1389.104** |
| `wall_clock_sec` | **696.543** |
| Script exit | **0** (**PASS** on **0 < stratum_min_d2 < 107800**) |

**Conclusion:** The **7630** statistic persists for **`(1,13)…(1,16)`**; **1540**-menu universality remains unproven. Next contiguous window: **`MENU_START=70`**, **`MAX_MENUS=4`**.
