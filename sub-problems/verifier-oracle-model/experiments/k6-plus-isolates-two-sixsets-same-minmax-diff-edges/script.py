#!/usr/bin/env python3
"""
Host G: isolates {0,1,2,3} plus three disjoint edges (4,5), (6,7), (8,9) — induced
subgraphs can be K2+4isolates vs 2K2+2isolates on two different 6-sets; same
(lambda_max, lambda_min) = (1,-1) but different internal edge counts.
(K6 from entry 028 cannot induce 2K2, so we use this matching core.)
"""

from __future__ import annotations

import numpy as np


def adjacency_three_edges_plus_isolates(n: int = 10) -> np.ndarray:
    assert n == 10
    adj = np.zeros((n, n), dtype=float)
    pairs = [(4, 5), (6, 7), (8, 9)]
    for u, v in pairs:
        adj[u, v] = adj[v, u] = 1.0
    return adj


def induced_adjacency(adj_full: np.ndarray, vertices: list[int]) -> np.ndarray:
    idx = sorted(vertices)
    return adj_full[np.ix_(idx, idx)]


def edge_count_upper(a: np.ndarray) -> int:
    n = a.shape[0]
    return int(sum(1 for i in range(n) for j in range(i + 1, n) if a[i, j] != 0))


def minmax_eig(a: np.ndarray) -> tuple[float, float]:
    w = np.linalg.eigvalsh(a)
    return float(w.max()), float(w.min())


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    adj = adjacency_three_edges_plus_isolates(n)
    s1 = [0, 1, 2, 3, 4, 5]
    s2 = [0, 1, 4, 5, 6, 7]
    assert len(s1) == len(s2) == t
    assert set(s1) != set(s2)

    a1 = induced_adjacency(adj, s1)
    a2 = induced_adjacency(adj, s2)
    e1, e2 = edge_count_upper(a1), edge_count_upper(a2)
    assert e1 == 1 and e2 == 2

    p1, p2 = minmax_eig(a1), minmax_eig(a2)
    assert abs(p1[0] - p2[0]) < 1e-9 and abs(p1[1] - p2[1]) < 1e-9
    assert abs(p1[0] - 1.0) < 1e-9 and abs(p1[1] + 1.0) < 1e-9

    print(f"n={n} t={t}  host = 4 isolates + 3 disjoint edges on {{4..9}}")
    print(f"S1={s1}  |E|={e1}  (max,min)={p1}")
    print(f"S2={s2}  |E|={e2}  (max,min)={p2}")
    print("RESULT: PASS - same two-float adjacency extrema, different induced |E|")


if __name__ == "__main__":
    main()
