# Results — star-independent-minmax-eigenvalue-quorum-collision

**Outcome:** PASS

**Graph:** Star `K_{1,9}` on `n = 10` vertices (center `0`, leaves `1..9`). Strict majority `t = 6`.

**Sets:** `S_a = {1,…,5}` (only leaves), `|S_a| = 5 < t`. `S_b = {1,…,6}`, `|S_b| = 6 ≥ t`. Neither set contains the center, so both induced subgraphs are **edgeless**.

**Observable:** `(λ_max, λ_min)` of the **adjacency** matrix of `G[S]` (computed with `numpy.linalg.eigvalsh`).

**Observed:** Both induced adjacencies are zero matrices; `(0.0, 0.0)` for `S_a` and `S_b`.

**Reasoning:** Same **two-number** summary for **under-quorum** vs **quorum** participation patterns on this fixed public graph — the spectral thread’s simplest “compress induced subgraph to extremal eigenvalues” idea does not encode `|S|` here.

**Command:** `python script.py` → exit 0.
