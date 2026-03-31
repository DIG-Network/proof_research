# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Type** | Toy **F₂** linear-algebra demo (not a deployed primitive). |

## Instance

- **n = 8**, **t = 5**.
- **x** = participation vector with **5** ones (bits **0..4**), **y** with **4** ones (bits **0..3**).
- **d = x ⊕ y** has **Hamming weight 1** (**d = 0x10**).

## Construction

- All **r** with **r·d = 0** over **F₂** (half of **{0,1}ⁿ**).
- Greedy subset of **m = n − 1 = 7** **linearly independent** such **r** (full rank in the **(n−1)**-dimensional subspace orthogonal to **d**).

## Check

For each selected **r_j**: **r_j·x = r_j·y** (all pool bits agree on **x** vs **y**).

## Interpretation

**Fixed** families of **parity-only** linear probes cannot **by themselves** encode strict-majority vs **one-below** separation unless the family is **injective** on the relevant pattern set — here **n−1** **independent** probes still **collapse** this majority/minority pair. Real schemes need **nonlinear** / **cryptographic** binding (hashes, **Merkle**, pairings, etc.), consistent with **`Link`** bottlenecks in earlier entries.
