# Notes

- **observation:** **`r=10`** at **5e7/8M** finishes **`d=3`** in **~55 s** with **1001** splits; LRU stays well under **8M** (no **PARTIAL**).
- **insight:** **Split count** is **not** monotonic with **hardness** in the simple band story: **1001** **<** **2002** **<** **3003**, yet **middle** band (**2002**) is the one that **PARTIAL**s here — **parity / XOR functional** still dominates over raw **C(n,r)**.
- **observation:** Correct **`C(14,10)=C(14,4)=1001`**; do not equate **`r=10`** with **`r=5`/`r=9`** on **split count** (those are **2002**).
- **question:** Whether **`r=4`** (**1001**, dual to **`r=10`**) matches this **easy** profile at **5e7/8M** — symmetric binomial check.
