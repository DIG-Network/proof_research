# Notes

- **Observation:** Full **2002** XOR menu at **`r=5`**, **`d=3`-only**, **30e7** **`exists_tree`**, **10M** LRU — **PARTIAL**; DP **~2615.68 s** (**~43.6 min**).
- **Observation:** **24e7 → 30e7** marginal **~645.4 s** for **+60M** calls (**~10.76 µs**/call) vs **18e7 → 24e7** **~478 s** / **60M** (**~7.97 µs**/call) — **marginal cost per call rises** in this band (LRU saturation / locality).
- **Dead end:** Interpreting truncated **`d=3 feasible=False`** as proof **`min_d>3`** — still **unsound** without a **complete** menu witness.
- **Next:** **DP/memo** or **exists_tree** frontier redesign; optional **`r=9` 30e7/10M** only if paired dual run is needed (**sequential** only).
