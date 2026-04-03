# Notes

- **Parent change:** added `--full-r2-r13-union-only` to run **only** the **`coord + ⋃_{r=2}^{13} XOR_r`** probe (skip redundant per-`r` sweeps). With **`--skip-baseline`**, **`max_exists_calls`** is **not** consumed by **`d=1..14`** coord-only baseline when probing a narrow **`d`** band.
- **Surprise / correction:** **`d=3 feasible=True`** for the **full union** contrasts with **`d=3 feasible=False`** on **large** **`r=5`/`r=9`** **sub-menus** — the missing splits were in **other** **`r`** **values**, not only more budget on **`r=9`**.
- **Next:** If the research question needs **`min_d`** under the **full** language across **all** depths, run **`d_min=1`** (or default) **without** **`d_max=3`** **only** when RAM allows; the **union** DP may still be heavy for **`d>3`** **probes** **unless** **memo** **stays** **small** **(** **this** **run** **did** **not** **stress** **that** **)** .
