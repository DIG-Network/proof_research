# Results — clique-induced-adjacency-max-eigenvalue-recovers-size

**Outcome:** PASS

**Host graph:** Unweighted `K_10` on vertices `0..9`.

**Sets:** `S_a = {0,1,2,3,4}` (`|S_a| = 5 < t`), `S_b = {0,1,2,3,4,5}` (`|S_b| = 6 ≥ t`), `t = 6`.

**Computed:** `λ_max` of induced adjacency via `numpy.linalg.eigvalsh`.

**Observed:** `λ_max(A(G[S_a])) = 4` and `λ_max(A(G[S_b])) = 5` within floating-point tolerance (`|S|−1` rule).

**Reasoning:** Induced subgraph is `K_{|S|}`; spectrum has top eigenvalue `|S|−1`. Under-quorum vs quorum **separate** on this **one** scalar — contrast **025** (star + leaf-only ⇒ both `0`).

**Command:** `python script.py` → exit 0.
