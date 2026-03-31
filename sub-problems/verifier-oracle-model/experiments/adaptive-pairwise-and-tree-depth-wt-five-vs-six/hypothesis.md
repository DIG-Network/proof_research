# Hypothesis: adaptive pairwise-AND trees vs coordinate-only lower bound

## Analogy pass

1. **Abstract structure:** A verifier adaptively asks Boolean questions about a hidden participation vector `x ∈ {0,1}^n`, restricted to two Hamming-weight classes (one below threshold vs at threshold). The questions must be drawn from a **query alphabet** (here: coordinate reads vs **pairwise ANDs**). We want the **minimum worst-case decision-tree depth** to **purely** classify every mask in the union of the two classes.

2. **Where else does this structure appear?**
   - **Property testing / juntas:** Non-adaptive vs adaptive query models over the hypercube; **AND** gates are **nonlinear** over **F₂** (degree-2 monomials), analogous to reading **interaction** terms in a **Walsh** expansion.
   - **Circuit complexity:** Depth measures for computing the **exact Hamming weight** or **threshold** from **allowed gate** types; **AND** of two inputs is a **restricted** **nonlinear** probe vs **variables** (literals).
   - **Group testing with conjunction tests:** A test **passes** only if **all** members of a **pair** are **defective** (both active); this is structurally **pairwise AND** on participation bits.

3. **Machinery in those domains:** Property testers bound query complexity with **Fourier** concentration; **decision trees** over **general** predicates branch on **richer** **splits** than **coordinates**; **conjunction** tests in **GT** can **identify** **sets** **faster** than **individual** **probes** in **some** **regimes**.

4. **Transfer seed:** **045** showed **coordinate-only** trees need **depth** **n** **(here 10)** **worst case** for **wt ∈ {5,6}** because **adjacent** **masks** **differ** **on** **one** **hidden** **bit** **and** **agree** **on** **all** **other** **coordinates**. **Pairwise AND** can **sometimes** **distinguish** **such** **pairs** **in** **one** **query** **(if** **the** **flipped** **bit** **pairs** **with** **a** **1** **elsewhere).** **Hypothesis:** **there** **exists** **a** **pairwise-AND** **decision** **tree** **of** **depth** **<** **n** **that** **separates** **all** **wt=5** **from** **all** **wt=6** **masks** **(n=10).**

**Falsifiable claim (original target):** On `(N,T)=(10,6)`, some perfect pairwise-AND tree has depth **≤ n−1 = 9**.

**What we measured:** Exhaustive min-depth backtracking for **small** `(n,t)` where `C(n,·)` keeps the domain tiny. **(10,6)** remains **out of budget** (462 masks, 45 branches per node).

## Formal hypothesis (tested instances)

**H1 (optimistic):** Pairwise-AND separation of `popcount ∈ {t−1,t}` achieves **strictly smaller** worst-case depth than coordinate-only **n** on at least one nontrivial toy.

**Observed:** **False** on `(5,3)` **(min depth 6 > n=5)** **and** **not** **better** **than** **n** **on** **(6,4)** **(min depth 6 = n).**

**H2 (alignment with 045):** On `(6,4)`, min pairwise-AND depth **≥ n−1** fails (i.e. depth **5** insufficient); min depth **= n**.

**Observed:** **Consistent** **—** **min** **depth** **=** **6.**

The script computes minimum `D` with memoized `exists_tree(S, D)` over all pair splits `i<j`.
