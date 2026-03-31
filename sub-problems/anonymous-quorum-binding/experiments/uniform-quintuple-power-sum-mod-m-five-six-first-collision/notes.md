# Notes

- **Proof sketch (mod 2):** Odd weights contribute 1 mod 2 to every `S_k`; even weights contribute 0. So `(S1,…,S5) mod 2` is always `(b,b,b,b,b)` with `b = (# odd weights in S) mod 2`. Any 5-set and 6-set with the same odd-count parity collide at `M=2` regardless of how many moments are kept.
- **Implication for toy “moment certificates”:** Under a **single** uniform modulus, if `M=2` is in the scan range, **no** finite list of raw power sums adds independent bits mod 2 beyond the first — characteristic-two collapse, not a numerical accident.
- **Next (if we want `M* > 2`):** Must break the mod-2 identification: e.g. **odd** modulus first step, **per-moment** different moduli (already studied in 059–060 style), **non-integer** or **non-power** summaries, or weights chosen so higher moments are not congruent to lower mod small `M`.
