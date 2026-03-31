#!/usr/bin/env python3
"""
Petersen graph (10 vertices, 3-regular): enumerate all 6-subsets, Laplacian of G[S],
bucket by rounded sorted eigenvalues; exhibit two distinct S with same spectrum.
"""

from __future__ import annotations

import itertools

import numpy as np


def petersen_adjacency() -> np.ndarray:
    """Standard drawing: outer 0-1-2-3-4-0, inner 5-7-9-6-8-5, spokes i--(i+5)."""
    n = 10
    a = np.zeros((n, n), dtype=float)
    outer = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    inner = [(5, 7), (7, 9), (9, 6), (6, 8), (8, 5)]
    spokes = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    for u, v in outer + inner + spokes:
        a[u, v] = a[v, u] = 1.0
    return a


def induced_laplacian(adj_full: np.ndarray, verts: tuple[int, ...]) -> np.ndarray:
    idx = list(verts)
    sub = adj_full[np.ix_(idx, idx)]
    deg = sub.sum(axis=1)
    return np.diag(deg) - sub


def spectrum_key(lap: np.ndarray, decimals: int = 8) -> tuple[float, ...]:
    w = np.linalg.eigvalsh(lap)
    w.sort()
    return tuple(round(float(x), decimals) for x in w)


def main() -> None:
    adj = petersen_adjacency()
    assert adj.shape == (10, 10)
    assert int(adj.sum()) == 30  # 15 undirected edges, symmetric matrix

    seen: dict[tuple[float, ...], tuple[int, ...]] = {}
    for verts in itertools.combinations(range(10), 6):
        lap = induced_laplacian(adj, verts)
        key = spectrum_key(lap)
        if key in seen:
            other = seen[key]
            if set(other) != set(verts):
                print("Petersen n=10, |S|=6 quorum-sized subsets")
                print(f"S1 (sorted) = {sorted(other)}")
                print(f"S2 (sorted) = {sorted(verts)}")
                print(f"sorted Laplacian eigenvalues (shared) = {list(key)}")
                print("RESULT: PASS - two distinct 6-sets share induced Laplacian spectrum")
                return
        seen[key] = verts

    print("RESULT: FAIL - all 210 six-subsets have distinct Laplacian spectra (rounded key)")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
