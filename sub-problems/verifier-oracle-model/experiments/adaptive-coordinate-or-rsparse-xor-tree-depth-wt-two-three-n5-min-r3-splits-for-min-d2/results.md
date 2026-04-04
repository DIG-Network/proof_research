# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2

**Outcome:** FAIL (hypothesis “minimal number of `r=3` splits needed with full `r=2` menu is ≥ 2” falsified)

## Setup

- `n=5`, mask shell popcount **`{2,3}`** (**20** masks).
- Parent: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py`.
- New flag **`--union-r3-indices`**: restrict the **`r=3`** XOR split list to a **0-based sublist** of the **`C(5,3)=10`** triples in lex order on `combinations(range(5),3)`.
- LRU cap: **`4_000_000`** (default path).

## Measured output

| Configuration | `r=3` restriction | total_splits | min_d |
|----------------|-----------------|-------------|-------|
| `union-rs 2,3` (full) | *(flag omitted)* | 20 | 2 |
| `union-rs 2,3` | `--union-r3-indices` empty → **no** triple splits | 10 | 3 |
| `union-rs 2,3` | `--union-r3-indices 0` | 11 | 2 |

**Exhaustive search** over subsets of triple indices for **`k=1`** found a witness immediately: **`r3_indices=[0]`** (**triple `(0,1,2)`**).

## Conclusion

Relative to the **fixed** full **`r=2`** XOR menu (**10** splits), **a single** **`r=3`** XOR split can be **sufficient** to recover **`min_d=2`**. The earlier **`r=3` “load-bearing”** conclusion (pair-only **`min_d=3`** vs full **`r=2..3`** **`min_d=2`**) reflects **collective** necessity of **some** triple parity **in the menu**, not that **many** distinct triple splits are each **individually** required in this toy slice.

## Reasoning

Index **`0`** is the XOR partition induced by **`i,j,k = 0,1,2`**: masks are split by **`parity` of** **`(bit0 ⊕ bit1 ⊕ bit2)`**. Together with **all** coordinate splits and **all** pair-XOR splits, this **one** extra split drives the adaptive-depth certificate from **`3` → `2`** for the **`{2,3}`** shell at **`n=5`**.
