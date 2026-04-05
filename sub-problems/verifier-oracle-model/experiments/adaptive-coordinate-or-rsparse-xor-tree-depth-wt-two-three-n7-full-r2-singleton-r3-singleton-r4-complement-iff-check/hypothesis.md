# Hypothesis: n=7 grid — min_d=2 iff complementary 3+4 cut

## Analogy pass

1. **Abstract structure:** Same adaptive XOR-tree DP as the prior `35×35` grid: coordinate splits + full `r=2` XOR + one `r=3` split + one `r=4` split. Each cell is labeled by minimum decision-tree depth.

2. **Analogous domains:** (i) **Formal verification** — replaying a claimed invariant with an independent checker. (ii) **Finite combinatorics** — characterizing the witness set of a predicate on a product set. (iii) **Coding theory** — when a small set of parity checks (here one triple + one quad) already implies a global partition structure.

3. **Machinery:** Exhaustive enumeration; set complement on `[7]`; bijection `C(7,3) ↔ C(7,4)` via `T ↦ [7]\setminus T`.

4. **Transfer seed:** The PASS grid experiment recorded (in prose) that the **35** depth-2 cells are exactly complementary pairs. This experiment **programs** both directions of the iff on all **1225** cells.

## Falsifiable claim

Let `T ⊂ [7]` be the triple for `r=3` index `i` and `Q ⊂ [7]` the quadruple for `r=4` index `j` (lex order from `itertools.combinations`).

**Claim A:** Every cell with `min_d = 2` satisfies `Q = [7] \setminus T`.

**Claim B:** Every cell with `Q = [7] \setminus T` satisfies `min_d = 2`.

**Claim C:** Every cell with `Q ≠ [7] \setminus T` satisfies `min_d ≥ 3`.

Together, **A+C** imply `min_d = 2` iff complementarity (given this language).

- **PASS (exit 0):** A, B, and C all hold on the full grid.
- **FAIL (exit 1):** Any counterexample to A, B, or C.

## Lineage

- **Refines / verifies:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-grid-scan` (PASS; structural claim was narrative).
- **Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.
