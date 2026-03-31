# Notes

- **Why depth can exceed n:** A coordinate read is one bit of information per query. An AND query is a **nonlinear** function of two bits; in the worst case the optimal strategy may need **more** than **n** rounds to separate two Hamming-weight shells (already seen at (5,3)).

- **Relation to 045:** Coordinate trees need depth **n** on (10,6) because two patterns that differ on a single hidden index agree on every other coordinate. Pairwise AND can **split** a **single-bit** **superset** **pair** **(y = x ∪ {j})** **in** **one** **query** **(j,k)** **when** **x_k = 1**, **but** **global** **separation** **of** **the** **full** **weight** **shell** **union** **still** **costs** **depth** **≥** **n** **on** **(6,4)** **and** **more** **on** **(5,3)** **in** **this** **model.**

- **Compute:** `(8,5)` and `(10,6)` exhaustive min-depth searches were **not** run to completion here (branching factor C(n,2) and large domains). A bounded search for `(10,6)` at depth `n−1` also timed out in an earlier draft; the **small-n** **table** **is** **the** **controlled** **result.**

- **Next:** Other non-coordinate oracles (OR, mod-3 sum on pairs, etc.) or formalize **verifier** **resource** **metrics** **separate** **from** **decision-tree** **depth.**
