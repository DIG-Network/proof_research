# Notes

- **observation:** All **`16`** RNG trials (**`SEED=0`**) produced identical **`stratum_min_d2=7630`**; wedge predicate remained **vacuous** (**`stratum_pred=0`**) as in **`K=1`** partial **`r=5`**.
- **insight:** Adding a second **`r=5`** split doubles the **`K=1`** count from **`3850`** to **`7630`** in this sample — suggestive of a simple arithmetic pattern (**`2×3850−70=7630`** is numerically exact; **`70=len(p4)`** — may be coincidental pending theory).
- **question:** Does **every** unordered pair of **`r=5`** splits yield **`7630`**, or does the sample hit a high-symmetry subset only? Exhaustive **`1540`** menus needed.
- **dead_end (local):** Treating random **`16`** trials as proof of universality would be wrong; use only as existence / structure hint.
- **next:** Run exhaustive **`C(56,2)`** with **`WORKERS`** (expect ~**`4×`** wall vs partial **`r=6`** **`K=2`** if per-menu time similar) **or** derive closed form for **`7630`**.
