# Results

**Outcome:** **FAIL** (exit code 1 — hypothesis falsified)

**Setup:** `n=10`, public weights `w_i = i+1`, shells `|S| ∈ {5,6}`.

**Statistic:** `K(S) = (min w, max w, Σ w, ∏ w)` as exact integers.

**Measured:**
- `distinct_K_5 = 252` (= `C(10,5)` — injective on the 5-shell)
- `distinct_K_6 = 210` (= `C(10,6)` — injective on the 6-shell)
- `cross_shell_exact = 0` — **no** 5-set and 6-set share the same `K`

**Conclusion:** On this toy, combining **extrema** with **both** additive and multiplicative mass **does** separate the adjacent shells: `K` is injective on `C(10,5) ∪ C(10,6)`. This contrasts with **091** / **092** / **063**, where dropping one of `{min,max}` or using only two coordinates allowed many cross-shell collisions.
