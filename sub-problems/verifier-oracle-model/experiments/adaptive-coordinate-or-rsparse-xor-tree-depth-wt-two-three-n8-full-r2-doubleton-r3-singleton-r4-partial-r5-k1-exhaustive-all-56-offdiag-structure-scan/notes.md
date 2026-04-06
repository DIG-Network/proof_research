# Notes

- **Observation:** All **56** **`K=1`** partial **`r=5`** menus agree on **`stratum_min_d2=3850`**; no menu explored a different count in this run.
- **Contrast:** **Partial `r=6` `K=1`** (**28** menus) gave **`107800`** everywhere — same as **full `r=6`**. **Partial `r=5`** is **not** in that closure at singleton size.
- **Wedge diagnostic:** **`stratum_pred=0`** throughout (quartic never matches **`W_ij`**/**`W_ji`** on this stratum under this language), so **`3850`** cells are **`d2∧¬pred`** — the **`n=7`**-style wedge certificate does not organize these witnesses.
- **Cost:** Per-menu wall time dropped from **`≈502s`** (menu 1, cold LRU) to **`≈168s`** (menu 56) as cache warmed; total **`≈16093s`** sequential.
- **Next steps:** **`K≥2`** partial **`r=5`** to see when/if **`stratum_min_d2`** jumps toward **`107800`**; or relate **`3850`** to a closed form / symmetry argument; **`K=2`** partial **`r=6`** (**378** menus) remains open for **`r=6`** line.
