# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Type** | Finite-field **Lagrange** / **RS-style** ambiguity (not a full PCS). |

## Parameters

- **p = 1009**, **n = 8**, nodes **x_i = i**, query **r = 900 ∉ {0,…,7}**.
- Reference vector **v_i = i+1 (mod p)**; **c = Σ v_i L_i(r)**.

## Construction

- Choose **w_0,…,w_6** freely (script uses a deterministic offset from **v**).
- Solve **w_7** so **Σ w_i L_i(r) = c** using **L_7(r) ≠ 0**.

## Observed

- **w ≠ v** (here **Hamming distance 8**).
- **Same** single evaluation **P(r) = 901** for both **v** and **w**.

## Interpretation

**One** algebraic evaluation constraint does **not** pin down the **n** leaf values encoding the set — consistent with **RS** intuition (**one** symbol ≠ full message) and with the need for **binding** multi-openings / commitments in real **PCS** plus separate **threshold** logic. Pairs with **021** (**linear** parity ambiguity) under “**few probes**” themes.
