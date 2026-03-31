# Results — vc-opening-budget

**Outcome:** **PASS** (as **idealized accounting** supporting the hypothesis — not a cryptographic theorem)

## Summary

| Pattern | Proof size (majority `t = Θ(n)`) | Sound `Link`? |
|--------|-----------------------------------|---------------|
| `t` independent Merkle paths | `Θ(t · λ · log n) = Θ(n log n)` bits (model) | Yes (per-index bind) |
| Single Merkle path only | `O(λ log n)` | **No** — does not attest ≥ `t` distinct leaves |
| Naive `t`-fold OR of constant proofs | `Θ(t · λ) = Θ(n)` bits | Structurally linear in `t` |

## Reasoning

- Entry **002** showed that **without** `Link`, constant-size `(K, σ)` is under-quorum forgeable. So any candidate must supply `Link` or equivalent.
- This experiment counts **generic** ways to realize `Link` via **independent** authentication of `t` leaves (Merkle) or **disjunctive** repetition. In the strict-majority regime, both blow past **sublinear in `n`** proof size.
- **KZG / polynomial commitments** could compress *multiple* openings in principle but (i) typical trusted-setup KZG is excluded by the main problem’s “no trusted setup,” and (ii) proving **Hamming weight** of a hidden 0/1 mask over committed values is not reduced to a single standard opening without a heavy proof layer (aligned with “no SNARK verifier”).

## Script

`python script.py` — prints budgets for several `n`, asserts large `proof_bits/n` for Merkle-`t`-paths at `n=2048`.
