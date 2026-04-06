# Notes

- **Observation:** All **28** rows are **numerically identical** on the aggregated stratum statistics (`107800`, `pred=0`, full `d2∧¬pred`); only **wall_sec** varies with **cache warmth**.
- **Dead end (local):** For **`n=8`**, **`K=1`** partial **`r=6`** does **not** produce **`0 < stratum_min_d2 < 107800`**; next structural probe is **`K≥2`** partial **`r=6`** or **`K=1`** partial **`r=5`** (**56** menus), unless the research pivots away from this stratum statistic.
- **Insight:** **`r=6`** and **`r=7`** partial singletons behave the same on this grid: **one** high-arity split suffices for **full** stratum saturation (`107800/107800`).
