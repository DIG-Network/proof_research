# Results — sublinear-pi-merkle-clash

**Outcome:** **PASS** (numerical accounting — not a theorem)

## Model

- **M1:** `t = ⌊n/2⌋ + 1` independent paths; **`bits_per_path = ⌈log₂ n⌉ · λ + O(log n)`** (same as `vc-opening-budget`).
- **Cap:** stylized **`B(n) = λ · (log₂ n)²`** with **`λ = 256`** — grows **polylog** in `n`, strictly **`o(n)`** in multiplicative sense vs **`n log n`** M1 total.

## Finding

For **`n`** from **128** to **8192**, **`M1_total / B(n)`** grows large; at **`n = 2048`**, **`M1_total / B(n) ≈ 94`** (script asserts **`> 85×`** as a regression check).

## Interpretation

- **Entry 011** (**R1**) and **Entry 003** (**M1**) are consistent: **per-signer Merkle** gives **soundness** but **not** **sublinear** `π` at **majority** `t`.
- A **main-compliant** scheme must **avoid** naive **M1** without replacing it by **R7** (or violating other constraints).

## Script

`python script.py` — prints table; exit code 0.
