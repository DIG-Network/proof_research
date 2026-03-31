# Results — k6-plus-isolates-alpha-lt-t-lambda-max-separates

**Outcome:** PASS

**Host graph:** **K_6** on **{4,…,9}** plus **4** isolated vertices **{0,1,2,3}**; **n = 10**, **t = 6**. **α(G) = 5** **(isolates** **+** **one** **core** **vertex)** **<** **t**.

**Witnesses:** **S_a = {0,1,2,3,4}** **(|S_a| = 5)** — independent; **S_b = {0,1,2,3,4,5}** **(|S_b| = 6)** — induced **K_2** on **{4,5}** plus isolates.

**Computed:** **λ_max** of induced adjacency (**numpy.linalg.eigvalsh**).

**Observed:** **λ_max(A(G[S_a])) = 0**, **λ_max(A(G[S_b])) = 1**; **strict** **increase** **across** **t**.

**Command:** `python script.py` → exit 0.
