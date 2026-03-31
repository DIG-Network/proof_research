# 2026-03-30 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n9

**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n9/`

## Hypothesis tested

Same adaptive `exists_tree` DP as **097** (`n=9`, coord + r-sparse XOR), but domain **wt ∈ {5,6}** (210 masks) — same shell *weights* as **066–093** on `n=10`. **H1:** coord + full 9-XOR has `min_d=1`. **H2:** full `min_d(r)` sweep `r=2..8` and compare to `(10,{5,6})` ladder.

## Outcome

**PASS**

## Key finding

- **Coord-only `min_d=9`**; **coord + full 9-XOR `min_d=1`**.
- **`min_d(r)`:** `r=2→5`, `r∈{3,4,5,7}→3`, `r=6→4`, `r=8→2`. **Triple / quad / pentuple all tie at 3** (no strict `5→4→3→2` arity ladder like **066→090→091→093** on 462 masks).
- **Unions:** `r∈{2,3,4}→3`, `r≤5` and `r≤8` both **`→2`**.

## Implications

- **098:** Shrinking `n` with fixed `{5,6}` shells **flattens** the per-arity depth staircase observed on `(10,{5,6})`; interior `r=6` bump aligns with **097**-style non-monotonicity.
- Any “threshold certificate” story for this toy on `n=9` is **not** the `t−1` vs `t` slice (both shells are quorums when `t=5`).

## Analogy pass summary

Shell-separation toy at smaller `n` with weights matching **066**; cross-linked **097** `(9,{4,5})` and **096** `(8,{4,5})` arity-scan methodology.

## Invented space

None (`space-definition.md` not used).
