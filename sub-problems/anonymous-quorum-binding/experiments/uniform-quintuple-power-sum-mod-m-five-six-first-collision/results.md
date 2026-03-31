# Results — uniform quintuple power sums mod M (5-set vs 6-set, n=10)

**Outcome:** PASS

**Setup:** `w_i = i+1`, `n=10`. For each subset of size 5 and 6, compute `S_k = Σ w_i^k` for `k=1..5`. Scan `M` from 2 upward for the first 5-vs-6 collision on `(S1,…,S5) mod M`.

**Finding:** `FIRST_COLLISION_M = 2`, `mod_key = (1,1,1,1,1)`.

**Witness:** Same index pattern as Entry **075**: five-set indices `(4,6,7,8,9)` (weights 5,7,8,9,10), raw `(39, 319, 2709, 23683, 211749)`; six-set `(0..5)` (weights 1..6), raw `(21, 91, 441, 2275, 12201)`.

**Structural note:** For any integer `w` and `k≥1`, `w^k ≡ w (mod 2)`. Hence `S_k(S) ≡ Σ w_i (mod 2)` for every `k` — the five modular coordinates are **redundant** at `M=2`; stacking more moments cannot increase the mod-2 resolution of this encoding.
