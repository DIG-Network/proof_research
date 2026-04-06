# Notes

- **Observation:** Every one of the **28** `K=2` menus matches the **`K=3`/`K=4`** pattern: full stratum has `min_d=2`, wedge predicate never fires (`pred=0`), all `107800` depth-2 cells violate `d2 ⇒ pred`.
- **Timing:** ~**21–37s** per menu, **~597s** total — roughly half the per-menu cost of **`K=3`** (two `r=7` splits vs three), consistent with the XOR-list length scaling the `min_depth_for_language` work.
- **Next:** Exhaustive **`K=1`** (**8** menus) on the same grid; if still saturated, pivot to **partial `r=5` / `r=6`** submenus or a different certificate family.
- **Dead end (local):** Expecting an intermediate **`stratum_min_d2`** by dropping from **`K=3`** to **`K=2`** partial **`r=7`** — ruled out on this stratum.
