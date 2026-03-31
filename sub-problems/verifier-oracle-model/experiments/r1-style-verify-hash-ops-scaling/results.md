# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Model** | Per-signer Merkle recompute: **1** leaf digest + **`depth = \lceil \log_2 n \rceil`** internal-node hashes; **`t = \lfloor n/2 \rfloor + 1`** signers. |

## Formula

`merkle_hash_ops ≈ t · (1 + depth(n))` for power-of-**2** **`n`**.

## Sample (excerpt)

| n | t | depth | t·(1+depth) |
|---|---|-------|-------------|
| 2048 | 1025 | 11 | **12300** |
| 8192 | 4097 | 13 | **57358** |

At **`n = 2048`**, **`t·(1+depth) / (n log₂ n) ≈ 0.546`**.

## Interpretation

- R1-style verification is **not** constant-time in **`n`**: Merkle checks alone scale **Θ(n log n)** when **`t = Θ(n)`**.
- Pairs **012** (**|π|** bits) with **verifier compute**: large **`n`** forces many hashes even before **`SigVerify`**.
