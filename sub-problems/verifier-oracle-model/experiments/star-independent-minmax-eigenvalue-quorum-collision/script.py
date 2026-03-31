#!/usr/bin/env python3
"""
Star K_{1,m}: leaf-only subsets induce edgeless graphs -> all adjacency eigenvalues 0.
(λ_max, λ_min) = (0, 0) for any nonempty leaf set; collision across quorum threshold.
"""

from __future__ import annotations

import numpy as np


def induced_adjacency(adj_full: np.ndarray, vertices: list[int]) -> np.ndarray:
    idx = sorted(vertices)
    return adj_full[np.ix_(idx, idx)]


def minmax_eig_sym(a: np.ndarray) -> tuple[float, float]:
    w = np.linalg.eigvalsh(a)
    return float(w.max()), float(w.min())


def main() -> None:
    m = 9
    n = m + 1  # center 0, leaves 1..m
    t = n // 2 + 1  # strict majority

    adj = np.zeros((n, n), dtype=float)
    for leaf in range(1, n):
        adj[0, leaf] = adj[leaf, 0] = 1.0

    # Under quorum: t-1 leaves only; quorum: t leaves only
    sa = list(range(1, t))  # |S_a| = t-1
    sb = list(range(1, t + 1))  # |S_b| = t
    assert len(sa) == t - 1 and len(sb) == t
    assert len(sa) < t <= len(sb)

    aa = induced_adjacency(adj, sa)
    ab = induced_adjacency(adj, sb)
    assert aa.shape == (t - 1, t - 1) and ab.shape == (t, t)
    assert np.all(aa == 0) and np.all(ab == 0)

    pa = minmax_eig_sym(aa)
    pb = minmax_eig_sym(ab)
    assert pa == pb == (0.0, 0.0)

    print(f"star K_1,{m}  n={n}  t={t}")
    print(f"|S_a|={len(sa)} < t <= |S_b|={len(sb)}")
    print(f"(lambda_max,lambda_min) for G[S_a] = {pa}, for G[S_b] = {pb}")
    print("RESULT: PASS - two-number adjacency extremal spectrum aliases across quorum")


if __name__ == "__main__":
    main()
