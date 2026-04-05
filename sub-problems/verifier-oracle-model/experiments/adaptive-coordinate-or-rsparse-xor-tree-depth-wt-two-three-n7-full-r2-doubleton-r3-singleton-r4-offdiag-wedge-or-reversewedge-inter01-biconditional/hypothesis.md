# Hypothesis: union of ordered wedges characterizes `min_d=2` on `|T_i∩T_j|∈{0,1}`

## Abstract structure

Same adaptive language as experiment 161: coordinate splits, full `r=2` XOR, two distinct `r=3` XOR splits (`i<j`), one `r=4` XOR split `Q`. Off-diagonal stratum `s=\mathrm{popc}(T_i\cap T_j)\in\{0,1\}`. Ordered wedge `W_{i,j}` alone was **sound** but **incomplete** for `min_d=2` (many depth-2 cells with `Q\neq W_{i,j}`). Symmetric difference alone also failed. The natural symmetric repair is to **union the two orientations**.

## Analogy pass

1. **Core relationship:** When a directed predicate is incomplete, the undirected symmetrization `(P(i,j)\lor P(j,i))` is the minimal symmetric envelope of a single orientation.

2. **Analogous domains:**
   - **Undirected graph as union of two orientations:** an edge exists if either direction is asserted.
   - **Two-sided tests in statistics:** reject if either tail is extreme.
   - **Bruhat order vs weak order:** sometimes the meaningful set is the union of two Schubert cells related by a simple reflection.

3. **Machinery:** symmetric closure, union of acceptance regions, Coxeter group symmetries.

4. **Transfer candidate:** Define `W_{i,j}` as in experiment 161 and test
   \[
   \min\_d = 2 \iff \bigl(Q=W_{i,j}\ \lor\ Q=W_{j,i}\bigr)
   \]
   on `i<j` and `s\in\{0,1\}`.

## Falsifiable claim

On the `|∩|∈{0,1}` off-diagonal stratum, `min_d=2` if and only if `Q` equals the ordered wedge for `(i,j)` **or** for `(j,i)` (same bitmask language as 161).

## Memory / prior context

- **161** ordered wedge alone: FAIL (385 `min_d=2` with `Q\neq W`, `wedge_not_d2=0`).
- **160** symdiff alone on same stratum: FAIL.

Parent: `…-offdiag-ordered-wedge-inter01-biconditional`.
