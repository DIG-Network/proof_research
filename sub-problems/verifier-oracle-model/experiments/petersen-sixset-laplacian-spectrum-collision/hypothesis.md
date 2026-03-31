# Hypothesis: Petersen — two distinct 6-sets share induced Laplacian spectrum

## Analogy pass

1. **Abstract structure**  
   The verifier sees a **vector summary** **σ(S)** derived from a **fixed** public graph **G** and an **unknown** active vertex set **S** (the signing coalition). The question is whether **σ** can **inject** on **all** **|S| = t** **quorum** patterns — a prerequisite for “**π** = few graph-spectral features of **G[S]**” as a binding certificate.

2. **Where else this structure appears**  
   - **Spectral graph theory:** **Cospectral** graphs share the same adjacency / Laplacian spectrum but need not be isomorphic — **many** constructions (Godsil–McKay switching, etc.).  
   - **Quantum graphs / isospectral drums:** Different shapes with **same** Laplacian eigenvalues — **non-injectivity** of spectrum as a **shape** fingerprint.  
   - **Sufficient statistics:** A **fixed-length** spectral vector can fail to identify the **underlying** discrete object if **symmetry** or **degeneracy** collapses many instances to one **signature**.

3. **Machinery in those domains**  
   Graph theory: compute **L = D − A** on **G[S]**; compare **sorted** eigenvalue multisets. Physical analogs: **hearing the shape of a drum** — not always unique.

4. **Transfer candidate**  
   Use a **standard** **3-regular** **expander** host — the **Petersen** graph on **n = 10** vertices — and **exhaust** **all** **C(10,6)** **6**-subsets. If **two** **distinct** **S** yield **identical** **sorted** **Laplacian** spectra of **G[S]**, then even a **full** **6**-eigenvalue summary (not just **λ_max, λ_min**) **does not** **uniquely** **pin** the **coalition** on this host.

## Falsifiable claim

**Claim:** Let **G** be the **Petersen** graph on vertices **{0,…,9}**. There exist **distinct** **S ≠ T ⊂ V** with **|S| = |T| = 6** such that **L(G[S])** and **L(G[T])** have the **same** multiset of eigenvalues (numerically verified: sorted vectors agree within tolerance after symmetric **eigvalsh**).

**PASS** ⇒ **richer-than-extrema** spectral summary still **aliases** between **two** **quorum-sized** **patterns** on an **expander** **toy**.  
**FAIL** ⇒ **no** such pair among **210** **6**-subsets (would suggest **injective** Laplacian spectrum on this **family** — **unexpected** but **informative**).
