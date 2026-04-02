# Notes

- **Observation:** Full **2002** XOR menu at **`r=5`**, **`d=3`-only**, **24e7** **`exists_tree`**, **10M** LRU — **PARTIAL**; DP **~1970.27 s** (**~32.8 min**).
- **Observation:** **+6×10⁷** calls over **18e7** added **~478 s** for **`r=5`**; **`r=9`** same step added **~473.6 s** — marginal **LRU-saturated** cost **matches** across shells at **10M**.
- **Observation:** **`r=5`** **24e7** **~7%** faster than **`r=9`** **24e7** (was **~9.3%** at **18e7**) — complement asymmetry **shrinks** slightly at higher cap but **persists**.
- **Dead end:** Treating **`d=3 feasible=False`** in the **PARTIAL** log as proof of **`min_d>3`** without a **complete** menu scan — still **unsound**; same caveat as **`r=9`** **24e7** run.
- **Next:** **`r=9`** or **`r=5`** **`30e7/10M`** (long wall), or **algorithmic** change to **`exists_tree`** frontier / memo to finish **2002** band without **linear** budget explosion.
