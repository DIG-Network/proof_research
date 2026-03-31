#!/usr/bin/env python3
"""
n=12, wt in {6,7}: same exists_tree DP as adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12,
but memo is LRU-bounded OrderedDict instead of functools.lru_cache (unbounded).

Correctness: evicted entries are recomputed — no false positives vs unbounded memo.
Goal: see if r=5 / r=7 complete under RSS cap when unbounded memo OOMs.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from collections import OrderedDict
from itertools import combinations

N = 12
SHELLS = (6, 7)


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in SHELLS]
    assert len(masks) == 1716
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


class LRUBoolMemo:
    """LRU on (bits, depth_remaining) -> bool."""

    __slots__ = ("maxsize", "_od", "hits", "misses")

    def __init__(self, maxsize: int) -> None:
        if maxsize < 1:
            raise ValueError("maxsize must be >= 1")
        self.maxsize = maxsize
        self._od: OrderedDict[tuple[int, int], bool] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def clear(self) -> None:
        self._od.clear()
        self.hits = 0
        self.misses = 0

    def get(self, key: tuple[int, int]) -> bool | None:
        if key in self._od:
            self.hits += 1
            self._od.move_to_end(key)
            return self._od[key]
        self.misses += 1
        return None

    def set(self, key: tuple[int, int], val: bool) -> None:
        if key in self._od:
            del self._od[key]
        self._od[key] = val
        self._od.move_to_end(key)
        while len(self._od) > self.maxsize:
            self._od.popitem(last=False)


def min_depth_for_language_lru(
    masks: list[int],
    coord_parts: list[tuple[int, int]],
    xor_parts_list: list[list[tuple[int, int]]],
    d_max: int,
    memo_maxsize: int,
    verbose: bool = False,
) -> tuple[int | None, list[tuple[int, bool, float, int, int]], LRUBoolMemo]:
    dom = len(masks)
    full_bits = (1 << dom) - 1
    log: list[tuple[int, bool, float, int, int]] = []
    memo = LRUBoolMemo(memo_maxsize)

    def exists_tree(bits: int, depth_remaining: int) -> bool:
        key = (bits, depth_remaining)
        got = memo.get(key)
        if got is not None:
            return got
        if pure_bits(bits, masks):
            memo.set(key, True)
            return True
        if depth_remaining <= 0:
            memo.set(key, False)
            return False
        for i in range(N):
            b0, b1 = split_bits(bits, coord_parts, i)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                memo.set(key, True)
                return True
        for xor_parts in xor_parts_list:
            for pi in range(len(xor_parts)):
                b0, b1 = split_bits(bits, xor_parts, pi)
                if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                    memo.set(key, True)
                    return True
        memo.set(key, False)
        return False

    min_d: int | None = None
    for d in range(1, d_max + 1):
        memo.clear()
        if verbose:
            print(f"  [progress] starting d={d} cap={memo.maxsize} ...", flush=True)
        t0 = time.perf_counter()
        ok = exists_tree(full_bits, d)
        elapsed = time.perf_counter() - t0
        log.append((d, ok, elapsed, memo.hits, memo.misses))
        if ok:
            min_d = d
            break
    return min_d, log, memo


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--cap",
        type=int,
        default=4_000_000,
        help="max memo entries (LRU evict beyond this)",
    )
    p.add_argument(
        "--r-single",
        type=int,
        default=None,
        metavar="R",
        help="single-arity r for coord + r-sparse XOR (required unless --bench-h2)",
    )
    p.add_argument(
        "--verify-r6",
        action="store_true",
        help="cross-check: r=6 must give min_d=2 vs published table",
    )
    p.add_argument(
        "--max-wall-sec",
        type=float,
        default=0.0,
        help="abort after this many seconds total (0 = no limit)",
    )
    p.add_argument(
        "--d-max",
        type=int,
        default=None,
        metavar="D",
        help="only test d=1..D (default: n=%d)" % N,
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="print per-depth progress lines",
    )
    p.add_argument(
        "--bench-h2",
        action="store_true",
        help=(
            "regression: verify r=6 LRU, then timeout-bound r=5 d<=3 LRU "
            "(expect timeout → exit 1 falsifies LRU-as-fix)"
        ),
    )
    args = p.parse_args()

    if not args.bench_h2 and args.r_single is None:
        p.error("--r-single is required unless --bench-h2")

    if args.bench_h2:
        me = __file__
        r6 = subprocess.run(
            [
                sys.executable,
                me,
                "--r-single",
                "6",
                "--verify-r6",
                "--cap",
                "500000",
            ],
            check=False,
        )
        if r6.returncode != 0:
            print("FAIL: bench-h2 r=6 cross-check failed", flush=True)
            sys.exit(1)
        # Expect no completion within 120s at d=3 (time blow-up, not OOM).
        r5 = subprocess.run(
            [
                "/usr/bin/timeout",
                "120",
                sys.executable,
                me,
                "--r-single",
                "5",
                "--cap",
                "4000000",
                "--d-max",
                "3",
            ],
            check=False,
        )
        if r5.returncode == 124:
            print(
                "PASS bench-h2: r=6 LRU ok; r=5 d<=3 LRU timed out (expected)",
                flush=True,
            )
            print(
                "OUTCOME: FAIL hypothesis H2 — LRU not practical for r=5 min_d probe",
                flush=True,
            )
            sys.exit(1)
        if r5.returncode != 0:
            print(
                f"FAIL: bench-h2 unexpected r=5 subprocess exit {r5.returncode}",
                flush=True,
            )
            sys.exit(1)
        print(
            "INCONCLUSIVE: r=5 d<=3 finished within 120s — revisit caps/time limits",
            flush=True,
        )
        sys.exit(0)

    r = args.r_single
    if not (2 <= r <= N - 1):
        print(f"FAIL: r must be in 2..{N-1}", flush=True)
        sys.exit(1)

    if args.verify_r6 and r != 6:
        print("FAIL: --verify-r6 requires --r-single 6", flush=True)
        sys.exit(1)

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)
    xp = build_r_xor_partition_masks(masks, r)

    d_hi = args.d_max if args.d_max is not None else N
    if d_hi < 1 or d_hi > N:
        print(f"FAIL: d-max must be in 1..{N}", flush=True)
        sys.exit(1)

    wall0 = time.perf_counter()
    md, lg, last_memo = min_depth_for_language_lru(
        masks, coord_parts, [xp], d_hi, args.cap, verbose=args.verbose
    )
    wall = time.perf_counter() - wall0

    print(
        f"r={r} cap={args.cap} C(n,r)={len(xp)} min_d={md} wall_sec={wall:.3f}"
    )
    for d, ok, sec, hits, misses in lg:
        print(
            f"  d={d} feasible={ok} sec={sec:.4f} memo_hits={hits} memo_misses={misses}"
        )

    if args.max_wall_sec > 0 and wall > args.max_wall_sec:
        print("OUTCOME: FAIL (wall clock limit)", flush=True)
        sys.exit(1)

    if args.verify_r6:
        if md != 2:
            print(f"FAIL: expected min_d=2 for r=6, got {md}", flush=True)
            sys.exit(1)
        print("PASS (r=6 LRU agrees with published min_d=2)", flush=True)
        return

    if md is None:
        if d_hi < N:
            print(
                f"OUTCOME: INCONCLUSIVE (no feasible d in 1..{d_hi}; "
                "full min_d unknown)",
                flush=True,
            )
            sys.exit(0)
        print("OUTCOME: FAIL (no feasible d up to n)", flush=True)
        sys.exit(1)

    # r=5 or r=7: certify we got a numeric min_d without OOM
    print("PASS (completed under LRU cap)", flush=True)


if __name__ == "__main__":
    main()
