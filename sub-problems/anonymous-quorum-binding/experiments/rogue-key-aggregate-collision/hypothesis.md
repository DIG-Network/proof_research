# Hypothesis

**H:** If an adversary **chooses** validator public keys (modeled as integers `pk_i` with additive aggregation `Agg(S) = ∑_{i∈S} pk_i`), they can force **two distinct strict-majority subsets** `S₁ ≠ S₂` to satisfy `Agg(S₁) = Agg(S₂)`.

**Consequence (toy):** Any verifier policy that treats “matching aggregate `K`” as **sufficient** evidence of a **unique** quorum coalition (without **`Link` / set binding**) is **unsound** under **malicious key registration**, even when honest random keys would yield injective aggregates (Entry **007**).

**Falsification:** No construction on small `n` after exhaustive check over a bounded search space — we instead give an **explicit** closed-form assignment.

**Scope:** Integer-sum proxy; real BLS-style rogue-key attacks use **group law** and **proof-of-possession** mitigations — this isolates the **combinatorial** ambiguity.
