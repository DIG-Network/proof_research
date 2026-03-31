# Results — `lcm-public-weight-five-six-shell-collision`

**Outcome:** PASS

**Instance:** `n=10`, public weights `w_i = i+1`, shells `|S| ∈ {5,6}`.

## h_lcm

- Distinct LCM values: `|Im(h_lcm)|` on 5-sets = **30**, on 6-sets = **23**.
- Cross-shell intersection: **23** shared values (every 6-shell LCM is also realized on some 5-set).
- Sample: `h_lcm = 24` — five-set `(0,1,2,3,7)` vs six-set `(0,1,2,3,5,7)` (weights `1,2,3,4,8` vs `1,2,3,4,6,8`, both LCM `24`).

## Joint `(h_lcm, Σw)`

- Distinct joint keys: **197** on 5-shell, **152** on 6-shell.
- Cross-shell collisions: **80** shared keys.
- Sample: `(60, 25)` — five-set `(1,2,3,5,9)` vs six-set `(0,1,2,3,4,9)`.

## Reasoning

`h_lcm` is the **join** in the divisibility lattice on the prime-exponent vectors of `{w_i}`. As with **089** (gcd / meet), it is too coarse to encode **cardinality** of `S` at `t=6`: many 5-multisets “cover” the same prime height as a 6-set. Pairing with exact `Σw` (**088** pattern) still leaves **80** ambiguous joint keys across shells.

**Conclusion:** Neither `h_lcm` nor `(h_lcm, Σw)` is a standalone `Link`-grade witness for “`|S| ≥ 6`” on this toy.
