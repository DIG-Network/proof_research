# Outcome: **PASS** (hypothesis confirmed)

**Command (wrapper):** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d/script.py`

**Parent invocation:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py --shells 2 --union-rs 2,3,4 --lru-maxsize 4000000`

## Measured values

| Quantity | Value |
|----------|-------|
| Shell | Hamming weight `{2}` only → **10** masks |
| Union | `r ∈ {2,3,4}` → **25** XOR splits (`10+10+5`) |
| `coord_only min_d` | **1** |
| `coord_plus_full_5xor min_d` | **1** |
| **`coord + ⋃_{r=2}^4 XOR_r` `min_d`** | **1** |
| `dp_sec` (union) | ~0.000 |

## Reasoning

We held the **`n=5`** mask shell at **weight 2 only** (the same **10** masks as in the earlier **`r=2..3`** union experiment) but **extended the XOR union to `r=2..4`**, matching the **split-count shape** used in the **`{2,3}` shell + `r=2..4`** configuration (**25** total XOR splits). The DP reports **`min_d=1`**.

Therefore the **`min_d=2`** outcome in **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d` is not explained by adding `r=4` XOR splits in isolation**. The qualitative jump is tied to **including weight-3 masks** in the alphabet (the **`{2,3}`** shell / **20** masks), interacting with the enlarged union — consistent with **`min_d` being shell-dependent**, not a universal `n=5` constant.
