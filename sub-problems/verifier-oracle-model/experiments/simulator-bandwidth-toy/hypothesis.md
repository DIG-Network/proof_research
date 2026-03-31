# Hypothesis

**H1 (distinction):** **Signer anonymity** does **not** require an injective map `S ↦ π` (many quorums may share the same accepting `π`). Therefore **no** information-theoretic lower bound on `|π|` follows from “number of majority subsets” alone.

**H2 (aggregate-key channel):** Fix concrete integer public keys `pk_0,…,pk_{n−1}` and `Agg(S) = ∑_{i∈S} pk_i`. Let `U` be the number of **distinct** values of `Agg(S)` as `S` ranges over **strict-majority** subsets. Any proof format that **uniquely specifies** `Agg(S)` among these possibilities (e.g. sending `K` in full, or an optimal code over `U` labels) needs **at least** `⌈log₂ U⌉` bits **in the worst case over S** for that specification task — independent of ZK.

**H3 (simulator metaphor):** If an ideal functionality reveals only `K` to the simulator (not `S`), and the real-world `π` must be a function of what the simulator knows, then **lossless** emulation of the `K`-marginal still allows **constant-size** `K` (one group element). The hard part is **not** specifying `K` in bits but **proving** `Link(C, K)` (Entry **004**) without SNARK/linear material.

**Falsification of H2:** Exhibit majority subsets `S₁ ≠ S₂` with `Agg(S₁) = Agg(S₂)` for the scripted keys (collision), making `U < W`. (Script: already `U < W` for affine `pk_i = 1000 + 13 i` at `n ∈ {6,8,10}`.)

**Scope:** Toy arithmetic + counting; not a UC proof.
