# Results — k6-plus-isolates-two-sixsets-same-minmax-diff-edges

**Outcome:** PASS

**Host graph G (see hypothesis):** Isolated **{0,1,2,3}**; edges **(4,5),** **(6,7),** **(8,9)** **only** (**1-regular** **core** **on** **{4,…,9}**). **n = 10**, **t = 6**.

**Sets:** **S_1 = {0,1,2,3,4,5}**, **S_2 = {0,1,4,5,6,7}** (**both** **|S| = t**).

**Induced edge counts:** **|E(G[S_1])| = 1**, **|E(G[S_2])| = 2**.

**Observable:** **(λ_max, λ_min)** **of** **induced** **adjacency** **(numpy.linalg.eigvalsh)**.

**Observed:** **(1.0, −1.0)** **for** **both** **induced** **subgraphs**.

**Reasoning:** **K_2** **+** **isolates** **and** **2K_2** **+** **isolates** **share** **top/bottom** **adjacency** **eigenvalues** **±1** **with** **multiplicity** **padding** **by** **zeros**.

**Command:** `python script.py` → exit 0.
