# Results

**Outcome:** **PASS** (exit code 0 — hypothesis confirmed)

**Setup:** `n=12`, public weights `w_i = i+1`, shells `|S| ∈ {5,6}`.

**Statistic:** `K(S) = (min w, max w, Σ w, ∏ w)` as exact integers.

**Measured:**

- `distinct_K_5 = 792` (= `C(12,5)` — still injective on the 5-shell alone)
- `distinct_K_6 = 924` (= `C(12,6)` — still injective on the 6-shell alone)
- `cross_shell_exact = 2` — **two** distinct keys shared by a 5-set and a 6-set

**Witnesses (both shells use weights `1..12`):**

1. `K = (1, 11, 31, 2640)`  
   - 5-set indices `(0, 4, 5, 7, 10)` → weights `(1, 5, 6, 8, 11)`  
   - 6-set indices `(0, 1, 2, 3, 9, 10)` → weights `(1, 2, 3, 4, 10, 11)`

2. `K = (1, 12, 32, 2880)`  
   - 5-set `(0, 4, 5, 7, 11)` → `(1, 5, 6, 8, 12)`  
   - 6-set `(0, 1, 2, 3, 9, 11)` → `(1, 2, 3, 4, 10, 12)`

**Conclusion:** Unlike **`n=10`** (**093**), the exact quadruple **`K` is not injective** on `C(12,5) ∪ C(12,6)`. Shell separation for this joint statistic is **not monotonic** in universe size: adding validators **`11` and `12`** enables cross-shell collisions that were absent at **`n=10`**. This aligns with **095**’s modular-collapse story at **`n=12`** while sharpening that **exact** integer data still merges for **some** pairs before any modulus.
