# Hypothesis: two Lagrange evaluations still alias binary leaf vectors

## Analogy pass

1. **Abstract structure**  
   We encode an $n$-bit participation pattern (who signed) as values on nodes $0,\ldots,n-1$ and summarize it by **few** polynomial evaluations $P(r_1), P(r_2)$ in $\mathbb{F}_p$. The question is whether such a **small summary** can act as an injective fingerprint of the pattern — a prerequisite for any “encode the set as a polynomial, open at constant points” binding story without listing leaves.

2. **Where else this structure appears**  
   - **Compressed sensing / sketching:** A measurement matrix $A \in \mathbb{F}^{k \times n}$ maps sparse (here **0/1**) signals to $k \ll n$ coordinates; injectivity on the signal set is the central question.  
   - **Error-correcting codes:** Evaluation of a message polynomial at $k$ points yields a $k$-symbol syndrome; distinct codewords can collide if $k$ is below the minimum distance regime.  
   - **Hashing / birthday bounds:** A map from a large finite domain into a smaller codomain forces collisions once the domain exceeds the codomain size.

3. **Machinery in those domains**  
   Sketches: RIP / spark conditions for uniqueness. Codes: Singleton bound, MDS vs actual $k$. Hashing: pigeonhole + explicit birthday search.

4. **Transfer candidate**  
   For fixed nodes, the map $v \mapsto (P_v(r_1), P_v(r_2))$ is **linear** in $v$ over $\mathbb{F}_p$. Restricting $v \in \{0,1\}^n$ gives $2^n$ inputs into a set of size at most $p^2$. When $2^n > p^2$, **pigeonhole** forces a collision; we can **exhibit** it by brute force for small parameters.

## Falsifiable claim

**Claim:** For concrete parameters $(n,p,r_1,r_2)$ with nodes $0,\ldots,n-1$, distinct $r_1,r_2 \notin \{0,\ldots,n-1\}$, and $2^n > p^2$, there exist **distinct** binary vectors $v \neq w \in \{0,1\}^n$ such that the unique polynomial $P$ of degree $\leq n-1$ interpolating $(i,v_i)$ matches that for $w$ at both $r_1$ and $r_2$.

**Interpretation if PASS:** Two standard “openings” are **insufficient** to bind a **full** binary participation vector in this encoding — extending Entry **022** (single opening) along the same polynomial thread.

**If no collision found (for chosen parameters):** Would **FAIL** the specific numeric claim; would try larger $n$ or different $p,r$ before abandoning the pigeonhole line.
