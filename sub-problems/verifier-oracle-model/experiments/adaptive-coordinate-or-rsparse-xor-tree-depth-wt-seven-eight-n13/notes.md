# Notes

- **Sharding:** **`python -u script.py --skip-baseline --r-single R`** per **`R`**; heaviest wall time **`r=3`** (~59 min DP), then **`r=8`** (~25 min), **`r=4`** (~7.7 min), **`r=2`** (~18 min).
- **`r=9`** then **`r=8`** in one shell succeeded (no **MemoryError** on this run); still prefer **one process per heavy **`r`** if the host has shown pressure.
- **Structural:** **`min_d(r)`** row and **union** depths **coincide** with **`(n=13,{6,7})`** (**`…-six-seven-n13-resolved`**) even though **`|domain|`** differs (**3003** vs **3432**).
