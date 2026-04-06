# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** choice of **exactly one** XOR split from the full `r=7` menu (`K(8,7)=8` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Exhaustive **`K∈{2,3,4}`** partial-**`r=7`** menus all gave universal **`stratum_min_d2=107800`**. **`K=1`** is the minimal nontrivial slice; if saturation already holds here, the partial-**`r=7`** line is fully closed at **`n=8`** for this statistic before pivoting to **`r=5`/`r=6`** submenus.

## Analogy pass

1. **Abstract structure:** Monotone family **`L_K`** by number of **`r=7`** generators; test whether the **`min_d2`** plateau is already reached at **`K=1`**.

2. **Analogous domains:**
   - **Percolation:** the terminal saturated phase may appear at minimal bond density.
   - **Matroid / rank:** a single generator may already lie in the closure that forces **`d2`** on every stratum cell.
   - **Sufficient statistics:** if **`K=2`** was redundant, **`K=1`** is the last chance for a strict intermediate value.

3. **Machinery:** enumerate **`range(8)`** as singleton index tuples; same per-menu scan as **`K=2`**.

4. **Seed:** Reuse the **`K=2`** driver with **`K_P7=1`** and **`len(menus)=8`**.

## Memory / prior context (brief)

- **`…-partial-r7-k2-exhaustive-all-28-offdiag-structure-scan`**: **FAIL**, all 28 menus ⇒ **`stratum_min_d2=107800`**.

This experiment exhausts the **`K=1`** partial-**`r=7`** envelope at **`n=8`** for this grid.
