# Hypothesis: on K_n, λ_max of induced adjacency recovers |S|

## Analogy pass

1. **Abstract structure**  
   Entry **025** showed a **fixed** graph **G** and a **two-float** summary of **G[S]** can **alias** across the quorum cut when **S** lies in a **large independent** set (empty induced subgraph). Here we ask whether a **different** fixed **G** removes that degeneracy so a **single** spectral statistic becomes a **sufficient statistic** for **|S|** in the induced-subgraph toy.

2. **Where else this structure appears**  
   - **Design of experiments / interaction models:** In a **fully crossed** factor design, every subset of factors has **pairwise interactions** visible unless size \< 2 — analogous to **clique** edges.  
   - **Statistical mechanics (mean-field):** **Dense** coupling (all-to-all) makes **collective** observables (e.g. **magnetization**-like scalars) track **population** size; **sparse** graphs allow **bulk** to hide in **non-interacting** modes (**025**).  
   - **Spectral graph theory:** The **adjacency** spectrum of **K_k** is **(k−1, −1, …, −1)** — **λ_max** encodes **k** linearly.

3. **Machinery in those domains**  
   Complete graphs have **closed-form** spectra; **interlacing** is trivial in the extreme **clique** case; **rank-one** shift from **J−I** pattern.

4. **Transfer candidate**  
   If **G = K_n** (validators = vertices, edges = all pairs), then **G[S] ≅ K_{|S|}** for any **S**, hence **λ_max(A(G[S])) = |S| − 1** for **|S| ≥ 1**. Then **(λ_max, λ_min)** (even **λ_max** alone) **separates** **|S_a| = t−1** from **|S_b| = t** — the **opposite** outcome of **025**.

## Falsifiable claim

**Claim:** Let **G = K_n** on vertices **{0,…,n−1}**. For any nonempty **S ⊆ V**, with **A_S** the adjacency of **G[S]**,  
**λ_max(A_S) = |S| − 1**.  
Consequently for **n = 10**, **t = 6**, **S_a** any **5** vertices and **S_b** any **6** vertices, **λ_max(A_{S_a}) = 4** and **λ_max(A_{S_b}) = 5** — strictly separated across **t**.

**Interpretation if PASS:** The **spectral-summary** obstruction in **025** is **not universal**; it depends on **host-graph** geometry (**large** **α(G)** vs **clique**). Any “spectral certificate of quorum” narrative must say **why** the **committed** interaction pattern is **not** **star-like** (or more generally **why** quorums cannot **live** in an **independent** **thick** region).

**If FAIL:** Would indicate an implementation or linear-algebra error (unlikely).
