# Hypothesis: diagonal `i=j` cells — complement law in doubleton-triple language (n=7)

## Analogy pass

1. **Abstract structure:** The same `22050`-cell grid restricts to **`35`** diagonal cells where the two `r=3` XOR splits repeat the same triple `T_i`. The off-diagonal slice was characterized by wedge pairs; the diagonal is the regime where the menu collapses to “one informative triple, twice.”

2. **Analogous domains:** (i) Degenerate cases in stratified models (boundary of a chart). (ii) Diagonal entries in a Gram matrix vs off-diagonal correlations. (iii) Fixed-point locus of an involution swapping two identical labels.

3. **Machinery:** Restrict a global classifier to a submanifold; expect a simpler certificate (here: set complement).

4. **Transfer candidate:** Prior singleton-triple + singleton-quartic work showed `min_d=2` iff `Q = [7]\setminus T_i`. The doubleton grid’s diagonal should reproduce that law exactly.

## Falsifiable claim

For `n=7`, language = coordinate partition + full `r=2` XOR + **duplicate** `r=3` pair `(T_i, T_i)` + singleton `r=4` split `Q`, and for **all** `i` and quartic indices `k`:

`min_d == 2` if and only if `Q` is the bitmask complement of `T_i` inside `[7]`.

## Memory / prior context

- `…-n7-full-r2-singleton-r3-singleton-r4-complement-iff-check` (PASS): singleton triple menu.
- `…-offdiag-symmetric-diff-predicate` (FAIL globally) still had **diagonal** complement law as a sub-claim.
- Experiment 165 unified off-diagonal wedges; this experiment **isolates** the diagonal **`1225`**-cell slice (`35×35`).
