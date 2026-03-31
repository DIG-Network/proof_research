#!/usr/bin/env python3
"""
n=10, wt in {5,6} (462 masks). Mixed trees: coordinate OR 5-sparse XOR only.

Pentuple XOR: branch 0 when x_i ⊕ x_j ⊕ x_k ⊕ x_l ⊕ x_m = 0 for i<j<k<l<m.
C(10,5) = 252 five-tuples; precomputed 462-bit partition masks.

Gate set is INCOMPARABLE with 091 (coord+quad): 091 has 4-XOR primitives
this omits; this has 5-XOR primitives 091 omits. 092 (total parity) is
also excluded here.

Answers BREAKTHROUGHS open Q: min depth with only 5-sparse parity nodes (+coords).
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


def build_pentuple_xor_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """For each 5-tuple i<j<k<l<m: (xor5=0, xor5=1) as domain index bitmasks."""
    full = (1 << DOMAIN_SIZE) - 1
    out: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m_idx in range(l + 1, N):
                        b0 = 0
                        for idx, mm in enumerate(masks):
                            p = (
                                ((mm >> i) & 1)
                                ^ ((mm >> j) & 1)
                                ^ ((mm >> k) & 1)
                                ^ ((mm >> l) & 1)
                                ^ ((mm >> m_idx) & 1)
                            )
                            if p == 0:
                                b0 |= 1 << idx
                        b1 = full ^ b0
                        out.append((b0, b1))
    return out


def split_coord_bits(bits: int, coord_parts: list[tuple[int, int]], i: int) -> tuple[int, int]:
    c0, c1 = coord_parts[i]
    return bits & c0, bits & c1


def split_px_bits(bits: int, px_parts: list[tuple[int, int]], pi: int) -> tuple[int, int]:
    c0, c1 = px_parts[pi]
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
    px_parts: list[tuple[int, int]],
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
        for pi in range(len(px_parts)):
            b0, b1 = split_px_bits(bits, px_parts, pi)
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
    p.add_argument("--budget-seconds", type=float, default=600.0)
    p.add_argument("--d-min", type=int, default=1, metavar="D0")
    args = p.parse_args()

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)
    px_parts = build_pentuple_xor_partition_masks(masks)
    expected = N * (N - 1) * (N - 2) * (N - 3) * (N - 4) // 120
    assert len(px_parts) == expected == 252

    status, min_d, log = run_search(
        masks,
        coord_parts,
        px_parts,
        args.budget_seconds,
        d_start=max(1, args.d_min),
    )

    for d, ok, sec in log:
        print(f"d={d} feasible={ok} elapsed_sec={sec:.3f}", flush=True)

    if status == "INCONCLUSIVE":
        print(
            "TIMEOUT_BEFORE_MIN_FOUND — 252 pentuple-XOR splits/node; "
            f"raise --budget-seconds or --d-min.",
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
    if min_d == 1:
        print("ONE_NODE_PENTUPLE_SEPARATES (unexpected)", flush=True)
    elif min_d == 2:
        print("min_d=2 (beats 091 quad-only min_d=3 on this toy)", flush=True)
    elif min_d == 3:
        print("min_d_equals_091_depth (pentuple+coord same min depth as quad+coord)", flush=True)
    else:
        print(f"min_d={min_d} vs_091=3", flush=True)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
