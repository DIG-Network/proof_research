# Hypothesis (falsifiable)

**Claim H1 (communication lower bound for naive Merkle + per-signer material).**  
Any proof system that makes the verifier convinced that each of at least `t` distinct validators from a committed set `V` of size `n` contributed a *separate* unaggregated public verification token (e.g. one Schnorr/BLS public key or one signature per signer, each accompanied by a Merkle co-path proving `pk_i ∈ Leaves(MerkleTree(V))`) must send **Ω(t · λ · log n)** bits in the worst case, hence **not o(n)** when `t = ⌊n/2⌋ + 1 = Θ(n)`.

*Falsifier:* Exhibit a sound construction in the stated model with `|π| = o(n) · poly(λ)` for `t = Θ(n)` that does **not** rely on SNARKs/STARKs or a new assumption beyond DL/pairings/RSA/ROM.

**Claim H2 (aggregate-key ambiguity without per-key or subset material).**  
For standard BLS-style linear aggregation over a pairing-friendly group, if the verifier holds only a **compact** commitment `C` to the multiset of validator public keys and an aggregate signature `σ` on message `m`, but **not** the aggregate public key `PK_S = ∑_{i∈S} pk_i` for the signing set `S` (nor an equivalent `O(λ)` unique handle determined by `S`), then **multiple** distinct subsets `S ≠ S'` (with different valid aggregates for the same `m`) are generally consistent with the same `(C, m, σ)` from the verifier’s view unless extra proof elements break the ambiguity.

*Falsifier:* Give a ROM/DL-secure `Verify(C, m, π)` that decides threshold validity **without** `π` containing `Θ(|S|)` linking information or a general-purpose ZK proof, when `|S|` may be `Θ(n)`.

**Survival clause (explicit relaxation).**  
If either claim is false, the surviving primitive must specify **which** ingredient escapes the model (e.g. `t = O(1)`, revealed aggregate key for a *known* cosigner set, linear `|π|`, stronger tool than excluded SNARKs).
