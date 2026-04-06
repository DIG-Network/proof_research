# Notes

- **Observation:** Parallelism is near-linear here: **`sum_menu_wall / wall_clock ≈ 4`**, consistent with **4** independent worker processes and **`chunksize=1`**.
- **Insight:** Finite closure: for **`n=8`**, base **`{2,3,4}`**, this stratum, **any** nonempty partial **`r=6`** submenu at **`K∈{1,2}`** appears **saturated** at **`107800`** — adding a **second** split never introduces **`0 < d2 < 107800`**.
- **Contrast:** Partial **`r=5`**, **`K=1`** remains the **`n=8`** arity where **`K=1`** already shows the intermediate **`3850`** plateau (**PASS** in the exhaustive **`56`**-menu scan).
- **Next:** Exhaustive **`K=2`** partial **`r=5`** (**`C(56,2)=1540`** menus, heavier), or combinatorial explanation of **`3850`**, or shift certificate family / **`n`**.
