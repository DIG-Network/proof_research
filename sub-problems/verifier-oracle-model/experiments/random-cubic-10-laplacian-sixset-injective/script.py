#!/usr/bin/env python3
"""
Search for a simple 3-regular graph on 10 vertices such that all C(10,6)=210
induced 6-set Laplacian spectra (sorted, rounded to 8 decimals) are pairwise distinct.

Uses networkx.random_regular_graph(3, 10, seed=...) for reproducible labeled cubics
(follow-up to Petersen 032; configuration model dropped as unnecessarily slow).
"""

from __future__ import annotations

import itertools

import networkx as nx
import numpy as np

N_VERT = 10
SUBSET_SIZE = 6  # quorum |S| for n=10
NUM_SUBSETS = 210
DECIMALS = 8
MAX_SEEDS = 100_000


def induced_laplacian(adj_full: np.ndarray, verts: tuple[int, ...]) -> np.ndarray:
    idx = list(verts)
    sub = adj_full[np.ix_(idx, idx)]
    deg = sub.sum(axis=1)
    return np.diag(deg) - sub


def spectrum_key(lap: np.ndarray) -> tuple[float, ...]:
    w = np.linalg.eigvalsh(lap)
    w.sort()
    return tuple(round(float(x), DECIMALS) for x in w)


def sixset_laplacian_injective(adj: np.ndarray) -> bool:
    seen: set[tuple[float, ...]] = set()
    for verts in itertools.combinations(range(N_VERT), SUBSET_SIZE):
        key = spectrum_key(induced_laplacian(adj, verts))
        if key in seen:
            return False
        seen.add(key)
    return len(seen) == NUM_SUBSETS


def main() -> None:
    for seed in range(MAX_SEEDS):
        g = nx.random_regular_graph(3, N_VERT, seed=seed)
        adj = nx.to_numpy_array(g, dtype=float)
        assert int(adj.sum()) == 30
        if sixset_laplacian_injective(adj):
            print(f"Found injective host: networkx seed={seed}")
            print(adj.astype(int))
            print(
                "RESULT: PASS - random cubic has 210 distinct 6-set Laplacian spectra"
            )
            return

    print(
        f"RESULT: FAIL - no injective graph in seeds 0..{MAX_SEEDS - 1} "
        f"({MAX_SEEDS} labeled 3-regular samples)"
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
