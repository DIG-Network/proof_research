# Hypothesis

**H:** In a linear Merkle-per-signer witness, if `Verify` checks (i) enough distinct valid paths into `C`, (ii) `|S| ≥ t`, and (iii) `SigVerify(K, m, σ)` for a **prover-supplied** field `K`, but **does not** enforce **`K = \sum_{i \in S} pk_i`** (or the correct group law) over the **same** opened public keys, then an adversary can make verification accept with a tuple where the **claimed** aggregate `K` is **not** the aggregation of the keys attested by the paths — even when `|S| ≥ t` and paths are valid.

**Falsification:** No accepting transcript exists under the toy APIs below, or the sound verifier incorrectly accepts.

**Expected outcome:** **PASS** (attack succeeds on flawed interface); reinforces that **`Link(C,K)`-grade binding in the R1-style stack includes an **algebraic consistency** check between opened leaves and `K`**, not only membership paths + a separate signature on `K`.
