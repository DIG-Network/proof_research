# Hypothesis

**H:** If `Verify(C, m, π)` recomputes a Merkle root from sibling paths in `π` but **does not** require equality with the verifier’s **actual** commitment `C` (e.g. it trusts a `declared_root` field inside `π`, or compares the recomputed root only to itself), then an adversary can pass verification using a proof that is valid relative to **`C' ≠ C`** — in particular, a tree built over a **different** key list where the adversary holds a **true** strict majority and a valid toy signature, while the on-chain `C` commits to an unrelated validator set.

**Falsification:** No such separation is possible in a minimal API, or the attack cannot be instantiated with explicit Merkle recomputation.

**Expected outcome:** Attack succeeds on the flawed interface; reinforces that **`Link`-grade binding includes `root(recomputed from π) == C`** for any Merkle-style witness, not only binding of `K`.
