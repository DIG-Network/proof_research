# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** choice of **exactly three** distinct XOR splits from the full `r=7` menu (`K(8,7)=8` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Exhaustive **`K=4`** (`C(8,4)=70`) menus all gave **`stratum_min_d2=107800`** (universal saturation). Smaller **`K=3`** (`C(8,3)=56`) is the next finite slice; if saturation already holds at **`K=3`**, that strengthens the structural picture before trying **`K=2`/`K=1`** or **`r=5`/`r=6`** splits.

## Analogy pass

1. **Abstract structure:** Nested families of languages **`L_K`** indexed by how many **`r=7`** generators are included; ask whether **`min_d2`** on a fixed finite stratum ever takes a value strictly between **`0`** and the **`K=8`** saturation plateau.

2. **Analogous domains:**
   - **Phase transitions in percolation:** as **`p`** increases, an order parameter jumps; here **`K`** plays the role of density—exhaust small **`K`** to see whether the jump is already complete.
   - **Matroid rank:** adding independent elements raises rank in steps; **`K`** may be below the rank needed for any “intermediate” **`d2`** count.
   - **Sufficient statistics:** **`K=4`** might already carry all information relevant to **`d2`** on this stratum; **`K=3`** tests strict sub-sufficiency.

3. **Machinery:** exact enumeration of **`combinations(range(8), 3)`** (56 menus); same per-menu scan as **`K=4`**.

4. **Seed:** Reuse the **`K=4`** exhaustive driver with **`K_P7=3`** and **`len(menus)=56`**.

## Memory / prior context (brief)

- **`…-partial-r7-k4-exhaustive-all-70-offdiag-structure-scan`**: **FAIL**, all 70 menus ⇒ **`stratum_min_d2=107800`**.
- Random **`K=4`**: same saturation.

This experiment exhausts the **`K=3`** partial-**`r=7`** envelope at **`n=8`** for this grid.
