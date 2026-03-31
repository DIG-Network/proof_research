#!/usr/bin/env python3
"""
Host graph G = K_n: induced G[S] is K_|S|; lambda_max(A(G[S])) = |S| - 1 for |S| >= 1.
Positive control vs star experiment 025 (collision on leaf-only sets).
"""

from __future__ import annotations

import numpy as np


def induced_adjacency(adj_full: np.ndarray, vertices: list[int]) -> np.ndarray:
    idx = sorted(vertices)
    return adj_full[np.ix_(idx, idx)]


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    adj = np.ones((n, n), dtype=float) - np.eye(n, dtype=float)

    sa = list(range(5))
    sb = list(range(6))
    assert len(sa) == t - 1 and len(sb) == t

    aa = induced_adjacency(adj, sa)
    ab = induced_adjacency(adj, sb)

    la_max = float(np.linalg.eigvalsh(aa).max())
    lb_max = float(np.linalg.eigvalsh(ab).max())

    assert abs(la_max - (len(sa) - 1)) < 1e-9
    assert abs(lb_max - (len(sb) - 1)) < 1e-9
    assert len(sa) < t <= len(sb)
    assert la_max != lb_max

    print(f"K_{n} host  n={n}  t={t}")
    print(f"|S_a|={len(sa)} lambda_max={la_max}  |S_b|={len(sb)} lambda_max={lb_max}")
    print("RESULT: PASS - clique host graph: lambda_max recovers |S|-1, splits across quorum")


if __name__ == "__main__":
    main()
