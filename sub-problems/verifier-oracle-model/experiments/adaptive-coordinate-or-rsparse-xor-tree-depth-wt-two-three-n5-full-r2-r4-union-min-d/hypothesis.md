# Hypothesis

**Outcome (2026-04-03):** **FAIL** — union `min_d=2` (see `results.md`).

**Claim (pre-run):** For `n=5`, with the mask shell **all** nonempty subsets of Hamming weight in `{2,3}` (20 masks), the mixed language **coordinate splits** plus the **full XOR union** over arities `r = 2,3,4` still has **minimum decision-tree depth `min_d = 1`** (same qualitative behavior as the 10-mask weight-2-only shell with union `r=2..3`).

**Falsification:** Any run that reports `min_d >= 2` for `coord + XOR_2 ∪ XOR_3 ∪ XOR_4` on this shell.

## Analogy pass

1. **Abstract structure:** A finite alphabet of bitmasks indexes a family of binary partitions (coordinate and parity-on-r-subsets). The **minimal depth** of an adaptive decision tree that separates “pure” leaf languages measures how many rounds of such splits are needed to certify membership in the shell-defined language.

2. **Analogous domains:** (a) **Decision tree complexity** of Boolean functions on structured attributes. (b) **Query complexity** in combinatorial group testing when tests are restricted to a fixed menu of hyperplane splits. (c) **Certificate size** in proof systems where each line is a split from a finite template.

3. **Machinery there:** Lower bounds often come from **adversarial path** arguments or **information-theoretic** counting; upper bounds from explicit **single-split** certificates when one partition refines the language.

4. **Transfer seed:** The prior **`n=5`, weight-2-only** experiment showed **`min_d=1`** even after a nontrivial XOR union. **Enlarging the shell** adds masks but might still leave a **single coordinate (or XOR) split** that separates all non-pure states—unless the larger alphabet creates a **mixed-weight obstruction** that forces depth 2. This experiment checks that boundary.

## Memory / lineage

- **Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py` (extended with `--shells`).
- **Related:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-full-r2-r3-union-min-d` (**FAIL**, expected `min_d=2`, observed `1`).
- **Contrast:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-full-r2-r4-union-min-d` (**PASS**, `min_d=2` for `n=6`).
