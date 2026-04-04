#!/usr/bin/env python3
"""
n=5 driver: coord + r-sparse XOR r=2..(n-1), unions, full n-XOR.

Default shell is popcount in {2} only (C(5,2)=10 masks). Use --shells to include
other weights, e.g. --shells 2,3 for twenty {2,3} masks (mirrors n=6 shell slice).
"""

from __future__ import annotations

import argparse
import math
import sys
import time
from functools import lru_cache
from itertools import combinations

N = 5


def popc(m: int) -> int:
    return m.bit_count()


def build_masks(shells: tuple[int, ...]) -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in shells]
    expected = sum(math.comb(N, w) for w in shells)
    if len(masks) != expected:
        raise RuntimeError(f"mask count mismatch: got {len(masks)}, expected {expected}")
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


def build_r_xor_partition_masks(masks: list[int], r: int) -> list[tuple[int, int]]:
    dom = len(masks)
    full = (1 << dom) - 1
    out: list[tuple[int, int]] = []
    for idxs in combinations(range(N), r):
        b0 = 0
        for ki, mm in enumerate(masks):
            p = 0
            for i in idxs:
                p ^= (mm >> i) & 1
            if p == 0:
                b0 |= 1 << ki
        b1 = full ^ b0
        out.append((b0, b1))
    return out


def split_bits(bits: int, parts: list[tuple[int, int]], pi: int) -> tuple[int, int]:
    c0, c1 = parts[pi]
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


def min_depth_for_language(
    masks: list[int],
    coord_parts: list[tuple[int, int]],
    xor_parts_list: list[list[tuple[int, int]]],
    d_max: int,
    lru_maxsize: int | None,
) -> tuple[int | None, list[tuple[int, bool, float]]]:
    dom = len(masks)
    full_bits = (1 << dom) - 1
    log: list[tuple[int, bool, float]] = []

    memo_max = None if lru_maxsize is None or lru_maxsize <= 0 else lru_maxsize

    @lru_cache(maxsize=memo_max)  # type: ignore[arg-type]
    def exists_tree(bits: int, depth_remaining: int) -> bool:
        if pure_bits(bits, masks):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(N):
            b0, b1 = split_bits(bits, coord_parts, i)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        for xor_parts in xor_parts_list:
            for pi in range(len(xor_parts)):
                b0, b1 = split_bits(bits, xor_parts, pi)
                if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                    return True
        return False

    min_d: int | None = None
    for d in range(1, d_max + 1):
        exists_tree.cache_clear()
        t0 = time.perf_counter()
        ok = exists_tree(full_bits, d)
        elapsed = time.perf_counter() - t0
        log.append((d, ok, elapsed))
        if ok:
            min_d = d
            break
    return min_d, log


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--r-max",
        type=int,
        default=N - 1,
        help="max r for single-arity sweep (default n-1)",
    )
    p.add_argument(
        "--r-single",
        type=int,
        default=None,
        metavar="R",
        help="only run coord/full + single-arity language for this r (fresh process; lowers peak RAM)",
    )
    p.add_argument(
        "--union-rs",
        type=str,
        default=None,
        metavar="LIST",
        help='comma-separated r values for one mixed language, e.g. "2,3" (coord + those r-sparse XOR menus)',
    )
    p.add_argument(
        "--union-r3-indices",
        type=str,
        default=None,
        metavar="LIST",
        help=(
            "when union-rs includes 3: comma-separated 0-based indices into the C(n,3) triple-XOR "
            "splits (lex order on combinations(range(n),3)). Omit to use all triple splits."
        ),
    )
    p.add_argument(
        "--skip-baseline",
        action="store_true",
        help="with --r-single or --union-rs, skip coord-only and full-n-XOR checks",
    )
    p.add_argument(
        "--baseline-only",
        action="store_true",
        help="only run coord-only + coord+full-n-XOR (no r sweep; fast sanity)",
    )
    p.add_argument(
        "--lru-maxsize",
        type=int,
        default=4_000_000,
        metavar="N",
        help="LRU cap for DP memo (0 = unbounded; default 4M avoids OOM on heavy shards)",
    )
    p.add_argument(
        "--shells",
        type=str,
        default="2",
        metavar="LIST",
        help='comma-separated Hamming weights included in mask shell, e.g. "2" (default) or "2,3"',
    )
    args = p.parse_args()
    lru_cap: int | None = None if args.lru_maxsize == 0 else args.lru_maxsize
    r_max = min(args.r_max, N - 1)

    shells = tuple(int(x.strip()) for x in args.shells.split(",") if x.strip())
    if not shells:
        print("FAIL: --shells must be non-empty", flush=True)
        sys.exit(1)
    for w in shells:
        if not (1 <= w <= N):
            print(f"FAIL: shell weight {w} must be in 1..{N}", flush=True)
            sys.exit(1)

    masks = build_masks(shells)
    coord_parts = build_coord_partition_masks(masks)

    def baseline() -> tuple[int | None, int | None]:
        md0, log0 = min_depth_for_language(masks, coord_parts, [], N, lru_cap)
        print(f"coord_only min_d={md0} (d_max={N})", flush=True)
        for d, ok, sec in log0:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)

        full_par_parts = build_r_xor_partition_masks(masks, N)
        assert len(full_par_parts) == 1
        md_full, log_full = min_depth_for_language(
            masks, coord_parts, [full_par_parts], N, lru_cap
        )
        print(f"coord_plus_full_{N}xor min_d={md_full}", flush=True)
        for d, ok, sec in log_full:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        return md0, md_full

    md0: int | None = None
    md_full: int | None = None
    if not args.skip_baseline:
        md0, md_full = baseline()
    else:
        print("skip_baseline=1 (coord-only and full parity not run)", flush=True)

    if args.baseline_only:
        if md0 is None or md_full is None or md_full != 1:
            print("FAIL", flush=True)
            sys.exit(1)
        print("PASS", flush=True)
        return

    if args.r_single is not None:
        r = args.r_single
        if not (2 <= r <= N - 1):
            print(f"FAIL: r-single must be in 2..{N-1}", flush=True)
            sys.exit(1)
        t0 = time.perf_counter()
        xp = build_r_xor_partition_masks(masks, r)
        t1 = time.perf_counter()
        md, lg = min_depth_for_language(masks, coord_parts, [xp], N, lru_cap)
        t2 = time.perf_counter()
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md} "
            f"build_sec={t1-t0:.3f} dp_sec={t2-t1:.3f}",
            flush=True,
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if not args.skip_baseline and (
            md0 is None or md_full is None or md_full != 1
        ):
            print("FAIL", flush=True)
            sys.exit(1)
        print("PASS", flush=True)
        return

    if args.union_rs is not None:
        rs = [int(x.strip()) for x in args.union_rs.split(",") if x.strip()]
        for r in rs:
            if not (2 <= r <= N - 1):
                print(f"FAIL: union-rs entries must be in 2..{N-1}", flush=True)
                sys.exit(1)
        if args.union_r3_indices is not None and 3 not in rs:
            print("FAIL: --union-r3-indices requires 3 in --union-rs", flush=True)
            sys.exit(1)
        xor_lists: list[list[tuple[int, int]]] = []
        for r in rs:
            xp = build_r_xor_partition_masks(masks, r)
            if r == 3 and args.union_r3_indices is not None:
                idxs = [int(x.strip()) for x in args.union_r3_indices.split(",") if x.strip()]
                n3 = math.comb(N, 3)
                for i in idxs:
                    if not (0 <= i < n3):
                        print(
                            f"FAIL: union-r3-indices must be in 0..{n3-1}, got {i}",
                            flush=True,
                        )
                        sys.exit(1)
                xp = [xp[i] for i in idxs]
            xor_lists.append(xp)
        total = sum(len(x) for x in xor_lists)
        t0 = time.perf_counter()
        md_u, _ = min_depth_for_language(masks, coord_parts, xor_lists, N, lru_cap)
        t1 = time.perf_counter()
        print(
            f"coord_plus_union_rs={rs} total_splits={total} min_d={md_u} "
            f"dp_sec={t1-t0:.3f}",
            flush=True,
        )
        if not args.skip_baseline and (
            md0 is None or md_full is None or md_full != 1
        ):
            print("FAIL", flush=True)
            sys.exit(1)
        print("PASS", flush=True)
        return

    for r in range(2, r_max + 1):
        t0 = time.perf_counter()
        xp = build_r_xor_partition_masks(masks, r)
        t1 = time.perf_counter()
        md, lg = min_depth_for_language(masks, coord_parts, [xp], N, lru_cap)
        t2 = time.perf_counter()
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md} "
            f"build_sec={t1-t0:.3f} dp_sec={t2-t1:.3f}",
            flush=True,
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)

    parts_by_r = {r: build_r_xor_partition_masks(masks, r) for r in range(2, r_max + 1)}
    if r_max >= 4:
        p2, p3, p4 = parts_by_r[2], parts_by_r[3], parts_by_r[4]
        md_234, _ = min_depth_for_language(masks, coord_parts, [p2, p3, p4], N, lru_cap)
        print(f"coord_plus_r2_r3_r4 min_d={md_234}", flush=True)
    else:
        print("coord_plus_r2_r3_r4 skipped (r-max < 4)", flush=True)

    if r_max >= 5:
        p2, p3, p4 = parts_by_r[2], parts_by_r[3], parts_by_r[4]
        md_2345, _ = min_depth_for_language(
            masks, coord_parts, [p2, p3, p4, parts_by_r[5]], N, lru_cap
        )
        print(f"coord_plus_r2_through_r5 min_d={md_2345}", flush=True)

    if r_max >= N - 1:
        md_all, _ = min_depth_for_language(
            masks,
            coord_parts,
            [parts_by_r[r] for r in range(2, N)],
            N,
            lru_cap,
        )
        print(f"coord_plus_r2_through_r{r_max} min_d={md_all}", flush=True)

    if md0 is None or md_full is None or md_full != 1:
        print("FAIL", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
