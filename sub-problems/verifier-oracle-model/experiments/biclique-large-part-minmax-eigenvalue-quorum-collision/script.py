#!/usr/bin/env python3
"""
K_{3,7} on n=10: the 7-vertex part is independent. Five vs six vertices there
induce empty graphs -> same (lambda_max, lambda_min) = (0,0) across t=6.
Intermediate density vs clique (026) and star (025).
"""

from __future__ import annotations

import numpy as np


def adjacency_k_ab(a_vertices: list[int], b_vertices: list[int], n: int) -> np.ndarray:
    adj = np.zeros((n, n), dtype=float)
    for i in a_vertices:
        for j in b_vertices:
            adj[i, j] = adj[j, i] = 1.0
    return adj


def induced_adjacency(adj_full: np.ndarray, vertices: list[int]) -> np.ndarray:
    idx = sorted(vertices)
    return adj_full[np.ix_(idx, idx)]


def minmax_eig_sym(a: np.ndarray) -> tuple[float, float]:
    w = np.linalg.eigvalsh(a)
    return float(w.max()), float(w.min())


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    L = [0, 1, 2]
    R = [3, 4, 5, 6, 7, 8, 9]
    assert len(L) == 3 and len(R) == 7

    adj = adjacency_k_ab(L, R, n)
    cross_edges = int(adj.sum() // 2)
    assert cross_edges == 21

    sa = R[:5]
    sb = R[:6]
    assert len(sa) == 5 and len(sb) == 6
    assert len(sa) < t <= len(sb)

    aa = induced_adjacency(adj, sa)
    ab = induced_adjacency(adj, sb)
    assert np.all(aa == 0) and np.all(ab == 0)

    pa, pb = minmax_eig_sym(aa), minmax_eig_sym(ab)
    assert pa == pb == (0.0, 0.0)

    print(f"K_3,7  n={n}  t={t}  cross_edges={cross_edges}")
    print(f"|S_a|={len(sa)}  |S_b|={len(sb)}  (max,min) = {pa} / {pb}")
    print("RESULT: PASS - dense bipartite: large-part independent quorum collision")


if __name__ == "__main__":
    main()
