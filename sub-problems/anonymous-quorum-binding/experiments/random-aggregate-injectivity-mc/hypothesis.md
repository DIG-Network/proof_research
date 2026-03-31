# Hypothesis

**H:** For independent draws `pk_0,…,pk_{n−1}` uniform on `{1,…,M}` with **large** `M` (stand-in for random scalars / hashed-to-curve behavior in a prime-order group), the restriction of the map `S ↦ ∑_{i∈S} pk_i` to **strict-majority** subsets `S` is **injective** with probability **1 − o(1)** over the draw, for fixed small `n` used in exhaustive enumeration.

**Operational test:** Monte Carlo over `T` draws; for each draw compute `W` (# strict-majority subsets) and `U` (# distinct subset-sums). Record fraction with `U = W`.

**Falsification:** Observed fraction of `U = W` materially below 1 for the chosen `(n, M, T)` (e.g. < 0.95 with `T ≥ 200`).

**Contrast:** Entry **006** showed **structured / small-magnitude** integers often have **`U < W`**; this experiment tests whether **“cryptography-like” randomness** restores **aggregate injectivity** on majority subsets at small `n`.

**Scope:** Integer sum proxy only — not a theorem about elliptic-curve multiset addition.
