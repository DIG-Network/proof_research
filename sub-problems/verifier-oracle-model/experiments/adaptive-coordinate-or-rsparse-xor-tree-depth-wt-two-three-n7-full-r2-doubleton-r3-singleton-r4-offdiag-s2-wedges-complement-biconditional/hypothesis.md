# Hypothesis — `s=2` stratum: `W_ij ∨ W_ji ∨ C_ij` vs `min_d=2`

## Analogy pass

1. **Abstract structure:** On the `|T_i ∩ T_j| = 2` stratum, feasible depth-2 quads are a **finite label set** determined by symmetric-difference geometry; prior global glue used **`W_ij ∨ C_ij`** and missed **`W_ji`**.

2. **Where else:** (i) **Oriented matroids** — the same geometric object can appear with two consistent orientations; (ii) **Directed cuts** — reversing edge direction swaps two canonical side-complements; (iii) **Case-split compilers** — missing one disjunct in a DNF yields false negatives but not false positives.

3. **Machinery:** Complete the disjunctive normal form on the stratum by adjoining the **reverse wedge** alongside **`C`**.

4. **Transfer candidate:** On **`s=2`**, test the **symmetric** predicate **`Q ∈ {W(i,j), W(j,i), C(i,j)}`** against **`min_d = 2`**, restricted to **`i < j`** off-diagonal grid cells.

## Falsifiable claim

For **`n=7`**, shell **`{2,3}`**, language **`coord + full r=2 + doubleton r=3 (i<j) + singleton r=4`**, for every cell with **`i < j`** and **`|T_i ∩ T_j| = 2`**:

**`min_d = 2` if and only if** **`(Q = W(i,j)) ∨ (Q = W(j,i)) ∨ (Q = C(i,j))`**, with **`W`** and **`C`** as in experiment **163**.

## Prior context

- Experiment **163** (FAIL): global stratified predicate used **`W_ij ∨ W_ji`** on **`s∈{0,1}`** and **`W_ij ∨ C_ij`** on **`s=2`**, producing **210** false negatives where **`Q = W_ji`** on **`s=2`**.
- Expectation: adding **`W_ji`** to the **`s=2`** branch **repairs** those false negatives; remaining question is whether **`pred ∧ md≠2`** appears (false positives).
