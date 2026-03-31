#!/usr/bin/env python3
"""
Monte Carlo: strict-majority subset sums -- U distinct sums vs W subsets.

Compare random large pk_i vs small structured pk_i (sanity baseline).
"""

from __future__ import annotations

import itertools
import math
import random
from typing import List, Set, Tuple


def majority_subsets(n: int) -> List[Tuple[int, ...]]:
    t = n // 2 + 1
    out: List[Tuple[int, ...]] = []
    for k in range(t, n + 1):
        out.extend(itertools.combinations(range(n), k))
    return out


def count_U_W(pks: List[int], subs: List[Tuple[int, ...]]) -> Tuple[int, int, int]:
    sums: Set[int] = set()
    for s in subs:
        sums.add(sum(pks[i] for i in s))
    W = len(subs)
    U = len(sums)
    return W, U, W - U


def trial_random(n: int, M: int, rng: random.Random) -> Tuple[int, int, bool]:
    pks = [rng.randrange(1, M + 1) for _ in range(n)]
    subs = majority_subsets(n)
    W, U, _ = count_U_W(pks, subs)
    return W, U, U == W


def main() -> None:
    print("=== random-aggregate-injectivity-mc ===\n")
    rng = random.Random(42)
    n = 10
    subs = majority_subsets(n)
    W_ref = len(subs)
    M = 1 << 50  # large range

    T = 400
    hits = 0
    min_U = 10**9
    for _ in range(T):
        W, U, ok = trial_random(n, M, rng)
        assert W == W_ref
        min_U = min(min_U, U)
        if ok:
            hits += 1

    frac = hits / T
    print(f"n={n}, strict-majority W={W_ref}, M=2^50, trials={T}")
    print(f"fraction with U=W (injective on majority subsets): {frac:.4f}")
    print(f"min U observed: {min_U}")

    # Baseline: small affine keys (often U < W)
    pks_small = [1000 + 13 * i for i in range(n)]
    _, U_small, gap = count_U_W(pks_small, subs)
    print(f"\nBaseline affine small pk: U={U_small}, W={W_ref}, gap={gap}")

    assert frac >= 0.95, "expect near-total injectivity for random large pk at n=10"

    print("\nVERDICT: PASS -- random large integers: U=W in most trials; small affine: U<W.")

if __name__ == "__main__":
    main()
