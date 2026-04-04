# Notes — minimal `r=3` witness at `n=5`, `{2,3}`

## Observation

- **Witness uniqueness at `k=1` was not tested** — the script **stops** at the **first** `k=1` index with `min_d=2`. Other singletons may also work.
- **Parent change:** `--union-r3-indices` only applies when **`3 ∈ union-rs`**; indices are validated against **`0..C(n,3)-1`**.

## Next steps

- Optionally **scan all 10** singletons and record **which** indices yield `min_d=2` vs `3` (full **`r=2`** fixed).
- If useful, extend the same **sub-menu** idea to larger **`n`** drivers (restricted triple sublists) — **not** done here.

## Analogy tag

**Generator minimality** vs **individual necessity** — collective menu effects can collapse to **few** critical parity queries.
