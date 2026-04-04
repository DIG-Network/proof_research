# Hypothesis — minimal `r=3` XOR splits for `min_d=2` at `n=5`, `{2,3}`

## Analogy pass

1. **Abstract structure:** The XOR split menu is a generating set for adaptive decision trees; we ask for a **minimal augment** beyond the pair-XOR sub-menu that restores the same shallow separation certificate as the full `r=2..3` union.

2. **Analogous domains:**
   - **Circuit minimization:** Find a smallest extra gate that lowers depth when a sub-basis is insufficient.
   - **Matroid / basis exchange:** Identify a single element whose addition repairs rank (here: decision-theoretic “rank” as separability at depth 2).
   - **Design of experiments:** Main effects (pairs) may need one specific higher-order interaction to resolve aliasing.

3. **Machinery:** Greedy / exhaustive subset search over generators; witness extraction.

4. **Transfer seed:** After showing all ten `r=3` splits are **collectively** load-bearing vs pair-only (`min_d` 3→2), ask whether **many** triple splits are individually necessary or one (or few) **critical** triple parities suffice.

## Falsifiable claim

With `n=5`, shell `{2,3}`, and **full** `r=2` XOR menu fixed, **more than one** `r=3` split is required to achieve `min_d=2` (i.e. minimal `k ≥ 2`).

**Observed:** **Falsified** — **`k=1`** suffices; witness index **`0`** (lex-first triple **`(0,1,2)`**), **`11`** total XOR splits (**`10`** pair + **`1`** triple).

## Parent / lineage

- Parent driver: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py` (adds `--union-r3-indices`).
- Follows: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-only-min-d` (FAIL: pair-only `min_d=3`).
