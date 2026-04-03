# Outcome: **FAIL** (hypothesis falsified)

**Command (wrapper):** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d/script.py`

**Parent invocation:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py --shells 2,3 --union-rs 2,3,4 --lru-maxsize 4000000`

## Measured values

| Quantity | Value |
|----------|-------|
| Shell | Hamming weights `{2,3}` → **20** masks (`C(5,2)+C(5,3)`) |
| Union | `r ∈ {2,3,4}` → **25** XOR splits (`10+10+5`) |
| `coord_only min_d` | **5** |
| `coord_plus_full_5xor min_d` | **1** |
| **`coord + ⋃_{r=2}^4 XOR_r` `min_d`** | **2** |
| `dp_sec` (union) | ~0.000 |

## Reasoning

The prior **`n=5`**, **weight-2-only** (10 masks), **union `r=2..3`** experiment showed **`min_d=1`**, falsifying a “`min_d=2` at `n=5`” conjecture for that narrow shell. After **adding all weight-3 masks** and **extending the union to `r=2..4`** (matching the `n=6` driver’s arity menu shape), the **full XOR union language requires depth 2**: the hypothesis that the enlarged `n=5` configuration would still admit a depth-1 certificate is **false**.

**Implication:** The **`min_d=2` “full union” phenomenon is not exclusive to `n≥6`** once the mask shell is large enough to mirror the `{2,3}` slice used at `n=6`; the earlier `n=5` **`min_d=1`** result was **shell-dependent**, not a universal `n=5` bound.
