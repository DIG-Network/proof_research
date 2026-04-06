# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** choice of **exactly one** XOR split from the full `r=5` menu (`C(8,5)=56` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Full **`r=5`** XOR menu alone already yields universal **`stratum_min_d2=107800`** (strict-subset scan). Partial menus might still admit an intermediate statistic; **`K=1`** is the smallest nontrivial slice (**`56`** menus). This tests whether **`r=5`** behaves like **`r=6`**/`r=7` at singleton submenu size.

## Analogy pass

1. **Abstract structure:** Monotone family by number of **`r=5`** generators; test whether **`K=1`** already lies in the closure that saturates **`stratum_min_d2`**.

2. **Analogous domains:**
   - **Percolation:** minimal edge sets that connect the giant component.
   - **Matroid closure:** one generator may span the same flat as a larger dependent set.
   - **Phase transitions:** cliff between sparse and saturated statistics at first high-arity inclusion.

3. **Machinery:** Exhaustive **`C(56,1)`** enumeration; same per-menu aggregation as partial **`r=6`**/**`r=7`** scans.

4. **Seed:** Port the **`K=1` partial `r=6`** driver with **`p5`**, **`len=56`**, and **`combinations(range(56), 1)`**.

## Memory / prior context (brief)

- **`…-strict-subsets-r5-r6-r7-offdiag-structure-scan`**: full **`r=5`** alone ⇒ **`stratum_min_d2=107800`**.
- **`…-partial-r6-k1-exhaustive-all-28-offdiag-structure-scan`**: every partial **`r=6`** singleton ⇒ **`107800`**.

This experiment tests whether partial **`r=5`** at **`K=1`** differs from partial **`r=6`** on the same statistic.
