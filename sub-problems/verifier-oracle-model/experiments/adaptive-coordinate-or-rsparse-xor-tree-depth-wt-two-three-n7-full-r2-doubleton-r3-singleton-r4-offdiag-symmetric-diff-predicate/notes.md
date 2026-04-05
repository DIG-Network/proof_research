# Notes

## dead_end

- **Symmetric difference as universal off-diagonal law:** For `coord + full r=2 + [p3[i],p3[j]] + p4[k]`, the condition `|T_i∩T_j|=1` and `Q=T_i△T_j` does **not** characterize `min_d=2`. Counterexamples in both directions (`md=2` with wrong `Q` or `|∩|≠1`; `md=3` with `Q=T_i△T_j`).

## observation

- **Replicated** prior structure scan counts (`1225` depth-2 cells; `35` on diagonal).
- **`315`** cells satisfy the naive symdiff predicate but stay at **`min_d=3`** — the set identity `Q=T_i△T_j` is **compatible** with infeasibility at depth 2 under this menu.
- Several **`|T_i∩T_j|=2`** pairs still hit **`min_d=2`** with quartics that are **not** `T_i△T_j` (symdiff has size `2` in that regime).

## insight

- The singleton **`3+4`** complement law **does not extend** to “`Q` equals a fixed Boolean combination of `T_i,T_j` independent of order” without extra case splits; lexicographic indexing `(i,j)` likely couples to **which** asymmetric set formula applies.

## question

- Is there a **short disjunction** of set templates (by `|T_i∩T_j|` and perhaps relative position) that exactly classifies the **`1190`** off-diagonal `min_d=2` cells?

## analogy

- **Parity / syndromes:** XOR of two triple parities does **not** reduce to a single quartic parity label in the DP sense; the **menu** is non-linear in how certificates compose.
