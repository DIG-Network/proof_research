# Notes

- Counts are **order-of-magnitude** guides; constants differ by Merkle variant (binary vs. Keccak trees), SNARK-free batching tricks, etc.
- The experiment does **not** rule out a **novel** commitment where `Link` is constant-size under a new assumption — it stress-tests **obvious** VC compositions.
- Synergy with **aggregated-key-link-game:** efficient `Link` is necessary; this experiment suggests **standard** Merkle/OR patterns for `Link` are **not** sublinear at majority `t`.
- **IPA / Bulletproofs** on committed `w`: proving `w ∈ {0,1}^n` and `sum w_i ≥ t` inside one proof is precisely the kind of **circuit-level** statement the main problem excludes as “SNARK-like” unless reframed without a circuit verifier — track as future definitional experiment.
