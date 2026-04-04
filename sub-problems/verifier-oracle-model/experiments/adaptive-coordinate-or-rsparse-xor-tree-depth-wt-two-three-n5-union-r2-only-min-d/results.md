# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-only-min-d

**Outcome:** FAIL (hypothesis falsified)

## Measured output

Parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py` with `--shells 2,3 --union-rs 2 --lru-maxsize 4000000`:

- `coord_only min_d=5`
- `coord_plus_full_5xor min_d=1`
- `coord_plus_union_rs=[2] total_splits=10 min_d=3` (`dp_sec` ~ 0)

Prior reference (same shell, `--union-rs 2,3`): `total_splits=20`, `min_d=2` (experiment `…-n5-union-r2-r3-only-min-d`).

## Conclusion

On the `{2,3}` mask shell at `n=5`, **pair-XOR-only** (`r=2` union, 10 splits) yields **`min_d=3`**, not `2`. The **10 triple-XOR splits** (`r=3`) in the `r=2..3` union are **load-bearing** for reducing adaptive depth from 3 to 2 in this slice — not redundant after expanding the mask alphabet to weight 3.

## Reasoning

The earlier result that `r=4` was unnecessary for `min_d=2` (shell `{2}` could reach `min_d=1` with `r=2..4`) is orthogonal: here the **weight-3 masks** change the separation problem so that **arity-3 XOR** becomes part of the minimal-depth menu, not only arity-2.
