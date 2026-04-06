# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** choice of **exactly one** XOR split from the full `r=6` menu (`C(8,6)=28` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Full **`r=6`** XOR menu already forces universal **`stratum_min_d2=107800`** (strict-subset scan). Partial menus might admit an intermediate statistic before saturation; **`K=1`** is the smallest nontrivial slice (**`28`** menus).

## Analogy pass

1. **Abstract structure:** Monotone family by number of **`r=6`** generators; test whether **`K=1`** already lies in the closure that saturates **`stratum_min_d2`**.

2. **Analogous domains:**
   - **Percolation:** a single bond can already connect the giant component on some lattices.
   - **Matroid closure:** one dependent element may span the same flat as many generators.
   - **Phase transitions:** the cliff between **`0`** and full saturation may occur at minimal menu size.

3. **Machinery:** Exhaustive **`C(28,1)`** enumeration; same per-menu aggregation as partial **`r=7`** scans.

4. **Seed:** Port the **`K=1` partial `r=7`** driver with **`p6`**, **`len=28`**, and **`combinations(range(28), 1)`**.

## Memory / prior context (brief)

- **`…-strict-subsets-r5-r6-r7-offdiag-structure-scan`**: full **`r=6`** alone ⇒ **`stratum_min_d2=107800`**.
- **`…-partial-r7-k1-exhaustive-all-8-offdiag-structure-scan`**: every partial **`r=7`** singleton ⇒ **`107800`**.

This experiment tests whether partial **`r=6`** behaves differently from partial **`r=7`** on the same statistic.
