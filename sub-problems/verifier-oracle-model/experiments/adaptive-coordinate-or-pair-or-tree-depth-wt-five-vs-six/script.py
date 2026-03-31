#!/usr/bin/env python3
"""
n=10, domain: all x in {0,1}^10 with popcount in {5,6} (462 masks).

Adaptive binary decision trees. Each internal node is either:
  - coordinate: branch on bit x_i
  - pair OR: branch on (x_i OR x_j), i.e. 0 iff both bits are 0

Leaves must be pure (all same popcount). Memoized existence test exists_tree(bits, d).

Subset encoding: 462-bit integer (bit k <=> k-th mask in sorted order). Avoids per-split
tuple allocation.

**Runtime note:** This DP is far heavier than the mixed XOR variant (066): pair-OR splits
fan out to many distinct subsets. Splits use **precomputed 462-bit partition masks**
(coordinate and pair-OR) so each split is two ANDs (major speedup vs per-mask scans).

This script uses a per-depth **seconds budget** (default 90s). If the budget is exceeded
before the first feasible d is found, it prints partial negatives and exits 2 (INCONCLUSIVE
for the *exact* min-d claim).

Upper bound (always): min_d <= n = 10 because coordinate-only trees exist at depth n (045).

Compare: adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six (XOR mixed, min d=5).
"""

from __future__ import annotations

import argparse
import sys
import time
from functools import lru_cache

N = 10
DOMAIN_SIZE = 462


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in (5, 6)]
    assert len(masks) == DOMAIN_SIZE
    return masks


def _lowbit_index(lsb: int) -> int:
    return lsb.bit_length() - 1


def pure_bits(bits: int, masks: list[int]) -> bool:
    if bits == 0:
        return True
    first_w: int | None = None
    b = bits
    while b:
        lsb = b & -b
        k = _lowbit_index(lsb)
        w = popc(masks[k])
        if first_w is None:
            first_w = w
        elif w != first_w:
            return False
        b ^= lsb
    return True


def build_coord_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """For each coordinate i, bitmasks over domain indices: (subset where x_i=0, where x_i=1)."""
    out: list[tuple[int, int]] = []
    for i in range(N):
        b0 = 0
        b1 = 0
        for k, m in enumerate(masks):
            if (m >> i) & 1:
                b1 |= 1 << k
            else:
                b0 |= 1 << k
        out.append((b0, b1))
    return out


def build_or_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """For each pair (i,j) lex, (subset where x_i OR x_j = 0, where = 1)."""
    out: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            b0 = 0
            b1 = 0
            for k, m in enumerate(masks):
                if (((m >> i) & 1) | ((m >> j) & 1)) & 1:
                    b1 |= 1 << k
                else:
                    b0 |= 1 << k
            out.append((b0, b1))
    return out


def split_coord_bits(bits: int, coord_parts: list[tuple[int, int]], i: int) -> tuple[int, int]:
    c0, c1 = coord_parts[i]
    return bits & c0, bits & c1


def split_or_bits(bits: int, or_parts: list[tuple[int, int]], pair_idx: int) -> tuple[int, int]:
    c0, c1 = or_parts[pair_idx]
    return bits & c0, bits & c1


def recurse_children_bits(
    exists_fn, b0: int, b1: int, depth_remaining: int
) -> bool:
    if b0 == 0:
        return exists_fn(b1, depth_remaining - 1)
    if b1 == 0:
        return exists_fn(b0, depth_remaining - 1)
    return exists_fn(b0, depth_remaining - 1) and exists_fn(
        b1, depth_remaining - 1
    )


def run_search(
    masks: list[int],
    coord_parts: list[tuple[int, int]],
    or_parts: list[tuple[int, int]],
    budget_s: float,
    d_start: int = 1,
) -> tuple[str, int | None, list[tuple[int, bool, float]]]:
    """
    Returns (status, min_d_or_none, log).
    status: PASS (found min), FAIL (no tree up to n), INCONCLUSIVE (timeout before min found).
    """
    full_bits = (1 << DOMAIN_SIZE) - 1
    log: list[tuple[int, bool, float]] = []

    @lru_cache(maxsize=None)
    def exists_tree(bits: int, depth_remaining: int) -> bool:
        if pure_bits(bits, masks):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(N):
            b0, b1 = split_coord_bits(bits, coord_parts, i)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        for pi in range(len(or_parts)):
            b0, b1 = split_or_bits(bits, or_parts, pi)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        return False

    deadline = time.perf_counter() + budget_s
    min_d: int | None = None

    for d in range(max(1, d_start), N + 1):
        if time.perf_counter() >= deadline:
            return "INCONCLUSIVE", None, log
        exists_tree.cache_clear()
        t0 = time.perf_counter()
        ok = exists_tree(full_bits, d)
        elapsed = time.perf_counter() - t0
        log.append((d, ok, elapsed))
        if ok:
            min_d = d
            break
        if time.perf_counter() >= deadline:
            return "INCONCLUSIVE", None, log

    if min_d is None:
        return "FAIL", None, log

    return "PASS", min_d, log


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--budget-seconds",
        type=float,
        default=90.0,
        help="Wall time budget for scanning d=1..n (default 90).",
    )
    p.add_argument(
        "--d-min",
        type=int,
        default=1,
        metavar="D0",
        help="Start depth loop at D0 (use 7 after d<7 ruled out locally).",
    )
    args = p.parse_args()

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)
    or_parts = build_or_partition_masks(masks)

    status, min_d, log = run_search(
        masks,
        coord_parts,
        or_parts,
        args.budget_seconds,
        d_start=max(1, args.d_min),
    )

    for d, ok, sec in log:
        print(f"d={d} feasible={ok} elapsed_sec={sec:.3f}")

    if status == "INCONCLUSIVE":
        print(
            "TIMEOUT_BEFORE_MIN_FOUND — pair-OR mixed DP heavier than XOR (066); "
            f"raise --budget-seconds or use compiled search for exact min_d. "
            f"Trivial upper bound: min_d <= {N} (coordinates)."
        )
        print("INCONCLUSIVE")
        sys.exit(2)

    if status == "FAIL":
        print("NO_TREE_UP_TO_N")
        print("FAIL")
        sys.exit(1)

    assert min_d is not None
    print(f"min_depth_found={min_d}")
    if min_d >= N:
        print(f"min_depth_equals_n={N} (no improvement over coordinate-only 045)")
    else:
        print(f"STRICT_IMPROVEMENT min_d={min_d} < n={N}")
    print("PASS")


if __name__ == "__main__":
    main()
