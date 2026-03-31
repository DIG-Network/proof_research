# Results — biclique-large-part-minmax-eigenvalue-quorum-collision

**Outcome:** PASS

**Host graph:** Complete bipartite **K_{3,7}** on vertices **{0,…,9}**, parts **L = {0,1,2}**, **R = {3,…,9}**; **21** cross edges (dense vs **45** in **K_{10}**).

**Threshold:** **t = 6** (strict majority on **n = 10**).

**Active sets:** **S_a = {3,4,5,6,7}** (**5** vertices, all in **R**), **S_b = {3,4,5,6,7,8}** (**6** vertices, all in **R**). No edges inside **R** ⇒ induced adjacencies are **zero** matrices.

**Observable:** **(λ_max, λ_min)** of induced adjacency via `numpy.linalg.eigvalsh`.

**Observed:** **(0.0, 0.0)** for **both** **S_a** and **S_b**; **|S_a| < t ≤ |S_b|**.

**Command:** `python script.py` → exit 0.
