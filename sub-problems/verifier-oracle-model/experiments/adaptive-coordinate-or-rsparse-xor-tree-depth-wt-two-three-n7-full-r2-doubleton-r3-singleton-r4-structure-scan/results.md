# Results: n=7 full r=2 + multiset r=3 (pair) + singleton r=4 — structure scan

**Outcome:** PASS (scan completed; baselines OK)

## Summary

Exhaustive grid over **22050** languages:

- `coord` + **full** `r=2` (21 splits) + **two** `r=3` XOR splits indexed by unordered pair `(i,j)` with `0 ≤ i ≤ j < 35` (**630** pairs) + **one** `r=4` split (**35** choices).

**`min_d` histogram**

| min_d | count |
|------:|------:|
| 2 | 1225 |
| 3 | 20825 |

**Depth-2 breakdown**

| regime | cells with min_d=2 |
|--------|-------------------|
| Diagonal `i == j` (duplicate triple split — effectively one informative triple XOR) | **35** |
| Off-diagonal `i < j` (two distinct triple XOR splits) | **1190** |

So **1190** cells use **two different** triple indices and still achieve **`min_d = 2`**. This shows that the singleton `3+4` complement phenomenon is **not** fragile to replacing “one triple split” by “two copies of the same triple split” only: **distinct** triple pairs also admit depth-2 certificates for many quartics.

**Timing:** `wall_sec ≈ 30.6` (LRU cap 4M; same machine class as prior n=7 scans).

## Interpretation

- Along **`i == j`**, there are **1225** cells total; only **35** have `min_d=2`, matching the singleton triple + quartic story (complement alignment for that single triple).
- Along **`i < j`**, **1190 / 20825 ≈ 5.7%** of cells hit `min_d=2`, so a second triple XOR materially **adds** depth-2 languages beyond the diagonal slice — the structure is **not** “depth-2 iff duplicate triple + complement quartic.”

## Implications

- Any certificate language for the `n=7`, `{2,3}` shell at this arity pattern must account for **non-redundant** pairs of triple parities, not only multiset repetition on one triple.
- Next step (optional): characterize the **1190** off-diagonal depth-2 cells (e.g. relation between the two triples and the quartic), analogous to the complement biconditional for the singleton grid.
