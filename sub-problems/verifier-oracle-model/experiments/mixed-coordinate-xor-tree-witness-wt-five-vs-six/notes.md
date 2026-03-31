# Notes — mixed-coordinate-xor-tree-witness-wt-five-vs-six

## Implementation

- **DP** **contract** **(** **matches** **066** **):** **`recurse_children`** **subtracts** **one** **when** **calling** **`exists_tree`** **on** **children.** **`exists_tree`** **therefore** **passes** **`depth_remaining`** **into** **`recurse_children`** **—** **not** **`depth_remaining - 1`** **(** **double** **decrement** **breaks** **feasibility** **).**
- **Naive** `build_witness(S,d)` **with** **`lru_cache` only** still **explores huge failing subtrees** before finding a global witness → **timeouts** on **|S|=462**, **d=5**.
- **Fix:** **two-phase** construction:
  1. Memoized **`exists_tree`** (identical to **`adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six/script.py`**).
  2. Memoized **`witness(S,d)`** that **only** descends along a split if **`recurse_children(exists_tree, …)`** is **True** for that split—mirrors **066**’s short-circuit order without probing doomed branches.

## Research

- **Principal variation** under fixed tie-breaking can be **structurally special** (here: **pure XOR chain** on disjoint pairs) even though the **language** allows coordinates—useful when comparing **verifier** **query** **cost** **models** (how many XOR vs coordinate probes in the **witness** **the** **prover** **ships**).
- **Next (optional):** print **multiple** witnesses (second-success XOR split, or force-first-coordinate when solvable) to stress **proof** **size** **/ ** **gate** **mix** **sensitivity**.
