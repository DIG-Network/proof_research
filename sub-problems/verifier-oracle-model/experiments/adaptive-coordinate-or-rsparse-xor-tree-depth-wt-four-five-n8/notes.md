# Notes

## Unsticking / design

Follows **095** open thread: vary `(n, shells)` while holding the coord + `r`-sparse XOR DP fixed. Pick `(8,{4,5})` so `n` is even and `n≠2t−1` for `t=5` — complement `x↦x⊕1ⁿ` maps wt 5 → 3, not a swap of `{4,5}`, so this is not the **049** pure-pair symmetry class.

## Surprise

Single-arity libraries do not have monotone `min_d(r)`: `r=4` is the sweet spot (`min_d=2`), while `r∈{2,3,5}` tie at `4`. Some 4-XOR splits align with a short path for this shell pair; 5-XORs on 8 bits form a different hyperplane family that does not subsume those splits when only one arity is allowed as a primitive gate label.

## Next

- Sweep more `(n,{t−1,t})` rows for local minima of `r ↦ min_d(r)`.
- Relate `r=n/2` (here 4) vs optimal `r` (speculative).
