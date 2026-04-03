# Hypothesis

## Analogy pass (mandatory)

1. **Abstract structure:** The verifier-oracle model asks whether a fixed family of adaptive coordinate / XOR partition splits can refute depth-3 decision trees on the `{7,8}` shell of masks for `n=14`. Sharded runs showed every eighth of the full `r=9` XOR menu still yields `feasible=False` at `d=3`, but the **full** combined language (all `r`-sparse XOR menus for `r=2..13` simultaneously) was not closed because the default parent script redundantly sweeps each `r` before the expensive final union.

2. **Analogous domains:** (i) Branch-and-bound with a growing split library — completeness requires the full library, not a sub-library. (ii) SAT with learned clauses — adding all resolvents at once changes the search shape versus incrementally. (iii) Dynamic programming on subsets — memoization over the same predicate but different move sets is not comparable until the move set matches.

3. **Machinery elsewhere:** Product-of-state spaces; “one-shot” union of operators vs staged enumeration.

4. **Transfer seed:** Add a **single-shot** code path that runs only `coord + ⋃_{r=2}^{13} XOR_r` (same DP as the parent’s final block) so we can allocate the full `exists_tree` budget to that probe, optionally with `--memo-dict` to avoid LRU eviction artifacts.

## Falsifiable claim

With `--d-min 3 --d-max 3`, `--memo-dict`, and `max_exists_calls = 1.5e8`, the full `r=2..13` XOR union either:

- returns `feasible=False` at `d=3` (strengthening evidence the language does not refute depth 3 at this budget), or
- exhausts the budget (`exit 2` PARTIAL), or
- returns `feasible=True` (would falsify the “all False at d=3” pattern seen on large shards).
