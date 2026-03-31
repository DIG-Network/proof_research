# Notes — polynomial-two-eval-binary-collision

- **Contrast with 022:** Single-eval toy used arbitrary field leaves; here the **hypercube** `{0,1}^n` matches “signer present / absent” more closely. Two evals give **2** linear constraints; codomain size **p²** — collision once `2^n > p²`.
- **Not a field-size impossibility:** For **small** `n` and **large** `p`, the map can be injective on `{0,1}^n` (e.g. `n = 10`, `p = 1009` gives `1024` inputs into `~10^6` buckets). The **PASS** claim is **existential** for exhibited parameters, not “always ambiguous for every `(n,p,r₁,r₂)`.”
- **Next angles:** Constant **k** evaluations give image size ≤ `p^k`; pigeonhole on binary patterns needs `2^n > p^k` to **force** collisions. For **sublinear** `k` and **cryptographic** `p`, `n` can still be large enough that **few** openings cannot label all patterns — quantitative barrier for “polynomial sketch + O(1) openings” without extra structure.
- **Unsticking / encoding:** Stays inside **polynomial / coding** analogy; parallel track from digest remains **spectral / expander** certificates (not yet run).
