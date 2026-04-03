# Results: joint-min-max-sum-mod-product-mod-m-five-six-first-collision

**Outcome:** PASS (hypothesis confirmed)

**Setup:** `n=10`, public weights `w_i=i+1` (indices `0..9`), shells `|S|∈{5,6}`.

**Statistic:** `K_M(S) = (min w, max w, Σ w mod M, Π w mod M)`.

**Finding:** The **smallest** `M≥2` with a **5-vs-6** cross-shell collision is **`M=2`**.

**Witness:** `K_2 = (1, 6, 1, 0)`  
- 5-set (indices): `(0, 1, 2, 4, 5)` → weights `(1,2,3,5,6)` → sum `17≡1 (mod 2)`, product `180≡0 (mod 2)`  
- 6-set: `(0, 1, 2, 3, 4, 5)` → weights `(1..6)` → sum `21≡1 (mod 2)`, product `720≡0 (mod 2)`

**Contrast:** Exact integer quadruple `(min,max,Σ,Π)` is injective on the union (**093**); folding **both** `Σ` and `Π` mod `M` still hits cross-shell merge at the **same floor** `M=2` as the **triple** folds in **091** (sum mod `M` only) and **092** (product mod `M` only) when `(min,max)` are kept exact.

**Interpretation:** Modular **parity** on **both** mass coordinates does not preserve the shell separation established by the exact **093** quadruple in this toy universe.
