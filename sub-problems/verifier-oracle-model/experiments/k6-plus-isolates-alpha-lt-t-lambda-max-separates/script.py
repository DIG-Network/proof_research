#!/usr/bin/env python3
"""
G = K_6 on {4..9} plus isolates {0..3}. n=10, t=6 => alpha(G)=5 < t.
S_a: 4 isolates + one clique vertex -> independent -> lambda_max = 0.
S_b: 4 isolates + two adjacent clique vertices -> induced K_2 -> lambda_max = 1.
"""

from __future__ import annotations

import numpy as np


def adjacency_k6_plus_isolates(n: int = 10) -> np.ndarray:
    assert n == 10
    adj = np.zeros((n, n), dtype=float)
    core = list(range(4, n))
    for i in range(len(core)):
        for j in range(i + 1, len(core)):
            u, v = core[i], core[j]
            adj[u, v] = adj[v, u] = 1.0
    return adj


def induced_adjacency(adj_full: np.ndarray, vertices: list[int]) -> np.ndarray:
    idx = sorted(vertices)
    return adj_full[np.ix_(idx, idx)]


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    adj = adjacency_k6_plus_isolates(n)
    # alpha = 5: take all isolates + any one core vertex
    sa = [0, 1, 2, 3, 4]
    sb = [0, 1, 2, 3, 4, 5]
    assert len(sa) == t - 1 and len(sb) == t
    assert len(sa) < t <= len(sb)

    aa = induced_adjacency(adj, sa)
    ab = induced_adjacency(adj, sb)
    assert np.all(aa == 0)
    assert ab[4, 5] == 1.0 and ab[5, 4] == 1.0

    la = float(np.linalg.eigvalsh(aa).max())
    lb = float(np.linalg.eigvalsh(ab).max())
    assert abs(la - 0.0) < 1e-9
    assert abs(lb - 1.0) < 1e-9
    assert la < lb

    print(f"K_6 + 4 isolates  n={n}  t={t}  alpha(G)=5 < t")
    print(f"|S_a|={len(sa)} lambda_max={la}  |S_b|={len(sb)} lambda_max={lb}")
    print("RESULT: PASS - alpha < t: quorum witness lifts lambda_max off zero")


if __name__ == "__main__":
    main()
