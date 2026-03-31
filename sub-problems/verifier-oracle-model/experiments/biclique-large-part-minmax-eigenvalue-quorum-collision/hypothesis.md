# Hypothesis: K_{3,7} admits quorum-crossing (λ_max, λ_min) collision on one part

## Analogy pass

1. **Abstract structure**  
   **026** showed **maximum** edge density (**clique**) makes **λ_max** of **G[S]** track **|S|**. **025** showed **star** + **independent** **placement** of **S** **collapses** **spectra**. We ask whether **intermediate** global density (**dense** but **bipartite**) still allows **thick** **independent** **sets** so that **two** **different** **|S|** straddling **t** yield **identical** **extremal** **adjacency** **eigenvalues**.

2. **Where else this structure appears**  
   - **Turán-type / extremal graph theory:** **K_{a,b}** maximizes edges under **no** **K_{r+1}** for suitable parameters — **high** average degree coexists with **large** **bipartite** **color class**.  
   - **Coding / Hamming schemes:** **Bipartite** **expansion** in **LDPC** graphs — **short** **cycles** and **structure** matter; **one** **side** can be **large** **independent**.  
   - **Statistical block models:** **Two** **communities** with **cross** **links** only — **activity** confined to **one** **block** hides **internal** **interaction** **signals**.

3. **Machinery in those domains**  
   **Independence number** **α(G) = max(a,b)** for **K_{a,b}**; **spectrum** of **bipartite** **H** is **symmetric**; **empty** **induced** **subgraph** ⇒ **null** **adjacency**.

4. **Transfer candidate**  
   For **G = K_{3,7}** (**n = 10**), **α(G) = 7**. For **t = 6**, take **S_a**, **S_b** as **5** and **6** vertices **entirely** inside the **7**-vertex **part**. **No** **edges** **within** **a** **part** ⇒ **G[S_a]**, **G[S_b]** **edgeless** ⇒ **λ_max = λ_min = 0** **both**, yet **|S_a| < t ≤ |S_b|**.

## Falsifiable claim

**Claim:** With **G = K_{3,7}** on **10** labeled vertices (parts **L** **|L|=3**, **R** **|R|=7**), **t = 6**, there exist **S_a ⊆ R**, **|S_a| = 5**, and **S_b ⊆ R**, **|S_b| = 6**, such that **A(G[S_a])** and **A(G[S_b])** are **zero** and **λ_max = λ_min = 0** for **each**.

**Interpretation if PASS:** **Dense** **non-clique** **host** (**21** **cross** **edges** **out** of **45** **possible** in **K_{10}**) still **fails** **min/max** **spectral** **quorum** **certificate** if **quorums** may **concentrate** on a **maximum** **independent** **set** — narrows digest **“intermediate** **density”** **gap**: **bipartite** **+** **large** **part** **behaves** like **025**, **not** **026**.

**If FAIL:** Construction or **n,t** **arithmetic** **error**.
