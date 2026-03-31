# Notes

- **Cross-check:** **`r=6`**, **`cap=500_000`**, full **`d`** sweep → **`min_d=2`** in **<0.1 s** wall.
- **`d=2`**, **`r∈{5,7}`**, **`cap=4_000_000`:** **`memo_hits≈322_806`**, **`memo_misses≈324_415`** — **evictions** are **already** **frequent** at **shallow** **depth**.
- **`r=5`**, **`d=3`:** **15 min** **timeout** with **no** **completion** **after** **`d=3`** **starts** — **time** **blow-up**, **not** **silent** **incorrect** **`True`**.
