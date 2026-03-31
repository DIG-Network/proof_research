#!/usr/bin/env python3
"""
n=10, wt in {5,6} (462 masks). Mixed trees: coordinate OR total XOR (all 10 bits).

Total XOR / global Hamming parity: branch 0 when x_0 ⊕ ... ⊕ x_9 = 0, else 1.
On this domain, popcount(m) mod 2 equals that XOR, so wt=6 → 0 and wt=5 → 1.
Hence one split separates the two shells → min_d = 1 (parity node alone).

Compare 091 (coord + quad-XOR, min_d=3): bounded-weight local parities without
the full n-bit XOR need more depth on this toy.
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


def build_total_parity_partition(masks: list[int]) -> tuple[int, int]:
    """⊕ all coordinate bits = popcount mod 2 on {0,1}^10."""
    full = (1 << DOMAIN_SIZE) - 1
    b0 = 0
    for idx, m in enumerate(masks):
        if popc(m) % 2 == 0:
            b0 |= 1 << idx
    b1 = full ^ b0
    return (b0, b1)


def split_coord_bits(bits: int, coord_parts: list[tuple[int, int]], i: int) -> tuple[int, int]:
    c0, c1 = coord_parts[i]
    return bits & c0, bits & c1


def split_pair_bits(bits: int, part: tuple[int, int]) -> tuple[int, int]:
    c0, c1 = part
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
    total_part: tuple[int, int],
    budget_s: float,
    d_start: int = 1,
) -> tuple[str, int | None, list[tuple[int, bool, float]]]:
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
        b0, b1 = split_pair_bits(bits, total_part)
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
    p.add_argument("--budget-seconds", type=float, default=60.0)
    p.add_argument("--d-min", type=int, default=1, metavar="D0")
    args = p.parse_args()

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)
    total_part = build_total_parity_partition(masks)
    b0, b1 = total_part
    n0, n1 = b0.bit_count(), b1.bit_count()
    print(f"total_parity_partition_sizes n_even={n0} n_odd={n1}", flush=True)
    assert n0 + n1 == DOMAIN_SIZE
    assert n0 > 0 and n1 > 0

    status, min_d, log = run_search(
        masks,
        coord_parts,
        total_part,
        args.budget_seconds,
        d_start=max(1, args.d_min),
    )

    for d, ok, sec in log:
        print(f"d={d} feasible={ok} elapsed_sec={sec:.3f}", flush=True)

    if status == "INCONCLUSIVE":
        print("TIMEOUT_BEFORE_MIN_FOUND", flush=True)
        print("INCONCLUSIVE", flush=True)
        sys.exit(2)

    if status == "FAIL":
        print("NO_TREE_UP_TO_N")
        print("FAIL", flush=True)
        sys.exit(1)

    assert min_d is not None
    print(f"min_depth_found={min_d}", flush=True)
    if min_d == 1:
        print(
            "ONE_NODE_TOTAL_PARITY shell wt=5 vs 6 separated by global Hamming parity",
            flush=True,
        )
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
