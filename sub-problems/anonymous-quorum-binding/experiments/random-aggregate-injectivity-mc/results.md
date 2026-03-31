# Results — random-aggregate-injectivity-mc

**Outcome:** **PASS** (Monte Carlo — integer proxy)

## Protocol

- `n = 10`, strict-majority subsets `W = 386`.
- `pk_i ∼ Uniform({1,…,M})` with `M = 2^50`, `T = 400` trials, seed `42`.
- Per trial: compute `U` = number of distinct subset-sums over all strict-majority `S`.

## Observed

- **Fraction with `U = W`:** **1.0000** over `T = 400` trials (`M = 2^50`, seed `42`); **min `U`** observed **386** (= `W`).
- **Baseline (Entry 006 style):** `pk_i = 1000 + 13 i` gives **`U = 75`**, **`W = 386`**, gap **311**.

## Interpretation

1. **Toy arithmetic:** Random **large** independent summands make majority subset-sum collisions **rare** at `n = 10`; **small structured** keys are **not** a good proxy for “random group element” multisets.
2. **Security implication:** A verifier cannot rely on “subset-sum collisions are common” to shrink the effective quorum space under **honest key generation** — **`Link(C, K)`** remains the binding step; collision attacks belong to **malicious key registration / rogue-key** threat models (not simulated here).

## Script

`python script.py` — Monte Carlo + baseline; exit 0 on assertion.
