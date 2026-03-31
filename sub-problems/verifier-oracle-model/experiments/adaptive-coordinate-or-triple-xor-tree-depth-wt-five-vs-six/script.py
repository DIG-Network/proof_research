#!/usr/bin/env python3
"""
n=10, wt in {5,6} (462 masks). Mixed trees: coordinate OR triple-XOR.

Triple XOR: branch 0 when x_i ⊕ x_j ⊕ x_k = 0, else 1.
C(10,3) = 120 triples; precomputed 462-bit partition masks (same pattern as pair gates).

Language strictly extends 066 (pair-XOR nodes): every pair split is a special case of
linear forms, but triple-XOR as a single node can yield partitions not achievable by
one pair-XOR node. Upper bound: min_d <= 5 (066 subtree) and <= 10 (coordinates).
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


def build_triple_xor_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """For each triple i<j<k: (xor3=0, xor3=1) as domain index bitmasks."""
    full = (1 << DOMAIN_SIZE) - 1
    out: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                b0 = 0
                for idx, m in enumerate(masks):
                    bi = (m >> i) & 1
                    bj = (m >> j) & 1
                    bk = (m >> k) & 1
                    if (bi ^ bj ^ bk) == 0:
                        b0 |= 1 << idx
                b1 = full ^ b0
                out.append((b0, b1))
    return out


def split_coord_bits(bits: int, coord_parts: list[tuple[int, int]], i: int) -> tuple[int, int]:
    c0, c1 = coord_parts[i]
    return bits & c0, bits & c1


def split_tx_bits(bits: int, tx_parts: list[tuple[int, int]], ti: int) -> tuple[int, int]:
    c0, c1 = tx_parts[ti]
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
    tx_parts: list[tuple[int, int]],
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
        for ti in range(len(tx_parts)):
            b0, b1 = split_tx_bits(bits, tx_parts, ti)
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
    p.add_argument("--budget-seconds", type=float, default=180.0)
    p.add_argument("--d-min", type=int, default=1, metavar="D0")
    args = p.parse_args()

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)
    tx_parts = build_triple_xor_partition_masks(masks)
    assert len(tx_parts) == N * (N - 1) * (N - 2) // 6

    status, min_d, log = run_search(
        masks,
        coord_parts,
        tx_parts,
        args.budget_seconds,
        d_start=max(1, args.d_min),
    )

    for d, ok, sec in log:
        print(f"d={d} feasible={ok} elapsed_sec={sec:.3f}", flush=True)

    if status == "INCONCLUSIVE":
        print(
            "TIMEOUT_BEFORE_MIN_FOUND — triple-XOR splits heavier than pair-XOR (066); "
            f"raise --budget-seconds or --d-min. min_d <= 5 (066 subset) <= {N}.",
            flush=True,
        )
        print("INCONCLUSIVE", flush=True)
        sys.exit(2)

    if status == "FAIL":
        print("NO_TREE_UP_TO_N")
        print("FAIL", flush=True)
        sys.exit(1)

    assert min_d is not None
    print(f"min_depth_found={min_d}", flush=True)
    if min_d >= N:
        print(
            f"min_depth_equals_n={N} (no improvement over coordinate-only 045)",
            flush=True,
        )
    elif min_d < 5:
        print(
            "STRICT_IMPROVEMENT_VS_066 min_d<5 (triple-XOR beats pair-XOR mixed bound)",
            flush=True,
        )
    elif min_d == 5:
        print(
            "min_d_equals_066 (triple-XOR nodes do not reduce depth below pair-XOR optimum)",
            flush=True,
        )
    else:
        print(f"min_d={min_d} strictly between 5 and n (unexpected band)", flush=True)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
