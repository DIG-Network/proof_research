# Results — unbound-quorum-field-attack

**Outcome:** **PASS** (the **attack** succeeds — the **naive “+k̂” extension** is **unsound**)

## Construction

- `n = 8`, `t = 5`, integer keys `pk_i`, toy `σ = H(m‖K)`.
- **Under-quorum:** `S` of size **`t − 1`**, `K = Agg(S)`, honest `σ` for that `K`.
- **Proof:** `π = (K, σ, \hat{k})` with **lied** **` \hat{k} = t`**.

## Finding

- **`Verify`** that only checks **` \hat{k} ≥ t`** and **`SigVerify(K, m, σ)`** **accepts** despite **`|S| = t − 1`**.

## Interpretation

- Any **sublinear** `π` that hopes to encode “**≥ t** signers” via an **explicit counter** must **bind** that counter to the **same** algebraic witness that fixes `K` / signatures — i.e. reduce to **`Link`** or **R1**-scale material, not a few **uncommitted** bits.

## Script

`python script.py` — asserts attack accepts; exit code 0.
