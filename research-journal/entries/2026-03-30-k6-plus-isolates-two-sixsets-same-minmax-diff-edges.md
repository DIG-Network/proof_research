# 2026-03-30 — k6-plus-isolates-two-sixsets-same-minmax-diff-edges

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/k6-plus-isolates-two-sixsets-same-minmax-diff-edges/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** **Two** **distinct** **6**-**subsets** **S_1,** **S_2** **with** **different** **induced** **edge** **counts** **but** **identical** **(λ_max,** **λ_min)** **of** **induced** **adjacency** **—** **host** **=** **4** **isolates** **+** **3** **disjoint** **edges** **(K_6** **cannot** **induce** **2K_2;** **see** **hypothesis)**.

**Outcome:** **PASS**

**Key finding:** **S_1** **gives** **K_2** **+** **4** **isolates** **(|E|=1),** **S_2** **gives** **2K_2** **+** **2** **isolates** **(|E|=2);** **both** **(1,** **−1).** **Constant-size** **spectral** **extrema** **do** **not** **determine** **induced** **edge** **count** **at** **fixed** **|S|=t.**

**Implications:**

- **Complements** **028:** **α<t** **can** **help** **5** **vs** **6,** **but** **two-float** **summary** **still** **collapses** **across** **distinct** **t**-**patterns** **on** **natural** **hosts**.
- **Digest** **open** **on** **multi-eigenvalue** **/constant** **summary:** **partially** **addressed** **for** **(λ_max,λ_min)** **pair**.

**Analogy pass summary:** **Moments** **/** **disjoint-union** **spectra** **—** **seed:** **repeated** **±1** **blocks** **preserve** **extrema**.
