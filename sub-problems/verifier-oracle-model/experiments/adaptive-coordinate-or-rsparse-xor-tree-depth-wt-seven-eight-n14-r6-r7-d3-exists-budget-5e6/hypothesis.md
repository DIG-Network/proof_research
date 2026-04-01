# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, with `--max-exists-calls 5_000_000` and `d=3`-only probes, **`r=7`** finishes with a definite `feasible=` line while **`r=6`** remains in the same **PARTIAL** class as **`r=5`** (budget exhausted before decision).

**Rationale:** The full `n=13` `{7,8}` row has `min_d(7)=3` with a relatively shallow DP; `r=7` on `n=14` is the same arity as one shell. By contrast `r=5` and `r=6` sit in the harder mid-`r` band where prior multi-hour runs stalled on `d=3`.

## Analogy pass

1. **Abstract structure:** Adaptive decision trees over a finite mask alphabet; each internal node applies a split from a library (coordinate vs `r`-sparse XOR). **Min depth** to separate two Hamming shells is found by memoized recursion whose state space size varies sharply with split geometry.

2. **Analogous domains:**
   - **Branching random walks / criticality:** Some branching rules hit a “subcritical” region where witness search stays shallow; others explode before hitting a leaf.
   - **SAT / CSP:** Same clause width does not imply same hardness—**structure** of constraints dominates.
   - **Dynamic programming on subsets:** Number of DP states can be **non-monotone** in a discrete parameter (`r`).

3. **Machinery in those domains:** Phase transitions; width vs structure; state-graph size estimates.

4. **Transfer seed:** Treat **`r`** as a discrete control parameter and **measure** whether the **same computational budget** yields a **complete** vs **partial** `exists_tree` trajectory—mirroring “critical slowing down” on one side and “easy certification” on the other.

## Parents

- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e6` (same budget shard for `r=5`).
