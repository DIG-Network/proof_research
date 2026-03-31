# Hypothesis

**H:** Consider a **constant-size** proof shape `π = (K, σ, \hat{k})` where `\hat{k}` is a **claimed** quorum size (a few bits), and a naive verifier:

1. Parses `\hat{k}` and requires `\hat{k} ≥ t`;
2. Checks a standard signature equation `SigVerify(K, m, σ)`;
3. **Does not** cryptographically **bind** `\hat{k}` to the set that determined `K` (no `Link`, no Merkle, no SNARK).

**Claim:** A **full-key** adversary can produce an **accepting** transcript while only **`t − 1`** validators **actually** signed (same class as Entry **002**), by choosing `K` from the undersized coalition and **lying** `\hat{k} = t`.

**Falsification:** Under the scripted toy `SigVerify`, the constructed attack does **not** yield `accept`.

**Scope:** Rules out a trivial “R7” of **appending an unauthenticated counter** to `(K, σ)`.
