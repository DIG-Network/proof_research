# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** choice of **exactly two** distinct XOR splits from the full `r=7` menu (`K(8,7)=8` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Exhaustive **`K=3`** (`C(8,3)=56`) and **`K=4`** (`C(8,4)=70`) menus all gave **`stratum_min_d2=107800`** (universal saturation). **`K=2`** (`C(8,2)=28`) is the next smaller slice; if saturation already holds at **`K=2`**, that further tightens the partial-**`r=7`** picture before **`K=1`** or **`r=5`/`r=6`** splits.

## Analogy pass

1. **Abstract structure:** Nested families of languages **`L_K`** indexed by how many **`r=7`** generators are included; ask whether **`min_d2`** on a fixed finite stratum ever takes a value strictly between **`0`** and the **`K=8`** saturation plateau.

2. **Analogous domains:**
   - **Phase transitions / percolation:** reducing **`K`** tests whether the order parameter is already at its terminal value before the smallest nontrivial menus.
   - **Matroid rank / basis:** **`K=2`** may still span the same “information” about **`d2`** on this stratum as larger **`K`**.
   - **Sufficient statistics:** if **`K=3`** was already sub-sufficient for saturation, **`K=2`** cannot escape the plateau.

3. **Machinery:** exact enumeration of **`combinations(range(8), 2)`** (28 menus); same per-menu scan as **`K=3`/`K=4`**.

4. **Seed:** Reuse the **`K=3`** exhaustive driver with **`K_P7=2`** and **`len(menus)=28`**.

## Memory / prior context (brief)

- **`…-partial-r7-k3-exhaustive-all-56-offdiag-structure-scan`**: **FAIL**, all 56 menus ⇒ **`stratum_min_d2=107800`**.
- **`…-partial-r7-k4-exhaustive-all-70-offdiag-structure-scan`**: **FAIL**, all 70 menus ⇒ **`stratum_min_d2=107800`**.

This experiment exhausts the **`K=2`** partial-**`r=7`** envelope at **`n=8`** for this grid.
