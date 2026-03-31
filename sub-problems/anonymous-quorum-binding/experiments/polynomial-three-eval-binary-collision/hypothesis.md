# Hypothesis: three Lagrange evaluations still alias binary leaf vectors

## Analogy pass

1. **Abstract structure**  
   Participation patterns live in $\{0,1\}^n$ (who signed). A degree-$(n-1)$ interpolant $P$ on nodes $0,\ldots,n-1$ is summarized by **three** field values $(P(r_1),P(r_2),P(r_3))$. We ask whether this **$O(1)$** summary can **inject** on all binary patterns — needed for any story that “constant openings of one polynomial bind the whole vector.”

2. **Where else this structure appears**  
   - **Linear sketches / JL-style projections:** A fixed linear map $\mathbb{F}_p^n \to \mathbb{F}_p^k$ restricts to $\{0,1\}^n$; injectivity requires the codomain large enough vs $2^n$.  
   - **Reed–Solomon / evaluation codes:** $k$ evaluations determine a degree-$(n-1)$ polynomial only if you already know it comes from a **low-degree** message; here the **message is unconstrained** except 0/1 on nodes — collisions are **codeword** collisions in a **nonlinear** restriction.  
   - **Hashing:** Domain size $2^n$, codomain size $\leq p^k$; pigeonhole when $2^n > p^k$.

3. **Machinery in those domains**  
   Sketches: need $k$ large enough (or structured sparsity). RS: MDS distance vs number of evaluation points. Hashing: pigeonhole guarantees **existence**; brute force **exhibits** small instances.

4. **Transfer candidate**  
   The map $v \mapsto (P_v(r_1),P_v(r_2),P_v(r_3))$ is **linear** in $v$ over $\mathbb{F}_p$. At most $p^3$ distinct triples. When $2^n > p^3$, two distinct binary vectors **must** collide; we **find** one by enumerating masks (feasible for $n=20$).

## Falsifiable claim

**Claim:** For $(n,p)=(20,97)$, nodes $0,\ldots,n-1$, distinct $r_1,r_2,r_3 \notin \{0,\ldots,n-1\}$, we have $2^n > p^3$ and brute-force bucketing finds **distinct** $v \neq w \in \{0,1\}^n$ with identical $(P_v(r_1),P_v(r_2),P_v(r_3))$.

**Interpretation if PASS:** Even **three** independent evaluation “openings” do **not** injectively label arbitrary binary participation in this encoding — extends **022** (one point) and **024** (two points, $2^n > p^2$).

**If FAIL:** Would contradict pigeonhole for these parameters (impossible if arithmetic correct); would debug implementation.
