# Hypothesis: min/max adjacency eigenvalues miss quorum on a star

## Analogy pass

1. **Abstract structure**  
   Validators sit at vertices of a **fixed public graph** `G`. An active set `S ⊆ V` induces `G[S]`. One hopes a **tiny** summary of `G[S]` — in spectral graph theory, often **eigenvalues** of `A(G[S])` or `L(G[S])` — could certify that `|S|` is large (quorum) without listing `S`. We test whether an **O(1)-sized** spectral statistic is **injective** on `|S|` near the threshold.

2. **Where else this structure appears**  
   - **Spectral graph theory:** Expansion and connectivity are often read off **Laplacian** spectra, but **coarse** summaries (e.g. a few extremal eigenvalues) need not determine **subgraph order**.  
   - **Statistical physics / spin models:** Effective summaries of a subsystem (few modes) can **degenerate** when the subsystem has **no internal coupling** — all modes flat.  
   - **Dimensionality reduction / PCA:** Projecting to **top and bottom** singular values loses **rank** / **size** when the matrix is **all zeros**.

3. **Machinery in those domains**  
   Cheeger inequalities link **λ₂** to cuts; **interlacing** for induced subgraphs; **nullity** of `A` counts **components** for bipartite pieces — but **extrema-only** views discard **multiplicity** and **dimension**.

4. **Transfer candidate**  
   On a **star** `K_{1,m}`, any subset of **leaves only** induces an **edgeless** graph. Then `A(G[S]) = 0`, so **every** eigenvalue is `0` and **λ_max = λ_min = 0` regardless of `|S|` (as long as `S` is nonempty and leaf-only). Pick `|S_a| < t ≤ |S_b|` with both **leaf-only** → same **two-number** summary **across** the quorum cut.

## Falsifiable claim

**Claim:** Fix `G` the star on `n = m + 1` vertices (one center, `m` leaves). Let `t = ⌊n/2⌋ + 1`. There exist sets `S_a, S_b` of **only leaves** with `|S_a| < t ≤ |S_b|` such that the induced subgraphs are **edgeless**, hence  
`λ_max(A(G[S_a])) = λ_min(A(G[S_a])) = λ_max(A(G[S_b])) = λ_min(A(G[S_b])) = 0`.

**Interpretation if PASS:** A natural **2-float** “spectral fingerprint” `(λ_max, λ_min)` of **induced adjacency** on a **fixed** graph does **not** separate **under-quorum** vs **quorum** in this model — analog to **023** (lossy count summary) and **024** (few polynomial values), in the **spectral** thread.

**If FAIL:** Would require our arithmetic on `n,t` or graph construction to be wrong (unlikely).
