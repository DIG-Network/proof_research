#!/usr/bin/env python3
"""
n=14, popcount in {7,8} (C(14,7)+C(14,8)=6435 masks).

Same DP as n=13 {7,8} sweep: coord + r-sparse XOR r=2..(n-1), unions, full n-XOR.
Threshold slice for majority t=8: wt 7 vs wt 8.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from functools import lru_cache
from itertools import combinations
from typing import Sequence

N = 14
SHELLS = (7, 8)


class _BudgetExceeded(Exception):
    """Raised when --max-exists-calls budget is exhausted inside exists_tree."""


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in SHELLS]
    assert len(masks) == 6435
    return masks


def _lowbit_index(lsb: int) -> int:
    return lsb.bit_length() - 1


def read_vm_rss_kb() -> int | None:
    """Best-effort resident set size from Linux /proc (kB)."""
    if os.name != "posix":
        return None
    try:
        with open("/proc/self/status", encoding="utf-8") as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    if len(parts) >= 2:
                        return int(parts[1])
    except OSError:
        return None
    return None


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
    d_min: int = 1,
    max_exists_calls: int | None = None,
    log_cache_after_each_d: bool = False,
    memo_dict: bool = False,
    log_rss: bool = False,
    progress_every: int = 0,
) -> tuple[int | None, list[tuple[int, bool, float]], bool]:
    dom = len(masks)
    full_bits = (1 << dom) - 1
    log: list[tuple[int, bool, float]] = []

    memo_max = None if lru_maxsize is None or lru_maxsize <= 0 else lru_maxsize
    miss_calls = 0

    if memo_dict:

        def exists_tree_dict(bits: int, depth_remaining: int) -> bool:
            nonlocal miss_calls
            key = (bits, depth_remaining)
            memo_local: dict[tuple[int, int], bool] = exists_tree_dict.memo  # type: ignore[attr-defined]
            # Match lru_cache budget semantics: count every invocation (hits + misses).
            if max_exists_calls is not None:
                miss_calls += 1
                if (
                    progress_every > 0
                    and miss_calls % progress_every == 0
                ):
                    extra = ""
                    if log_rss:
                        rk = read_vm_rss_kb()
                        if rk is not None:
                            extra = f" VmRSS_kB={rk}"
                    print(
                        f"  progress exists_calls={miss_calls} "
                        f"memo_dict_size={len(memo_local)}{extra}",
                        flush=True,
                    )
                if miss_calls > max_exists_calls:
                    raise _BudgetExceeded()
            if key in memo_local:
                return memo_local[key]
            if pure_bits(bits, masks):
                out = True
            elif depth_remaining <= 0:
                out = False
            else:
                out = False
                for i in range(N):
                    b0, b1 = split_bits(bits, coord_parts, i)
                    if recurse_children_bits(exists_tree_dict, b0, b1, depth_remaining):
                        out = True
                        break
                if not out:
                    for xor_parts in xor_parts_list:
                        for pi in range(len(xor_parts)):
                            b0, b1 = split_bits(bits, xor_parts, pi)
                            if recurse_children_bits(
                                exists_tree_dict, b0, b1, depth_remaining
                            ):
                                out = True
                                break
                        if out:
                            break
            memo_local[key] = out
            return out

        exists_tree_dict.memo = {}  # type: ignore[attr-defined]

        def clear_memo() -> None:
            exists_tree_dict.memo.clear()  # type: ignore[attr-defined]

        def memo_size() -> int:
            return len(exists_tree_dict.memo)  # type: ignore[attr-defined]

        exists_tree_fn = exists_tree_dict
    else:

        @lru_cache(maxsize=memo_max)  # type: ignore[arg-type]
        def exists_tree_lru(bits: int, depth_remaining: int) -> bool:
            nonlocal miss_calls
            if max_exists_calls is not None:
                miss_calls += 1
                if progress_every > 0 and miss_calls % progress_every == 0:
                    extra = ""
                    if log_rss:
                        rk = read_vm_rss_kb()
                        if rk is not None:
                            extra = f" VmRSS_kB={rk}"
                    print(
                        f"  progress exists_calls={miss_calls} "
                        f"lru_currsize={exists_tree_lru.cache_info().currsize}{extra}",
                        flush=True,
                    )
                if miss_calls > max_exists_calls:
                    raise _BudgetExceeded()
            if pure_bits(bits, masks):
                return True
            if depth_remaining <= 0:
                return False
            for i in range(N):
                b0, b1 = split_bits(bits, coord_parts, i)
                if recurse_children_bits(exists_tree_lru, b0, b1, depth_remaining):
                    return True
            for xor_parts in xor_parts_list:
                for pi in range(len(xor_parts)):
                    b0, b1 = split_bits(bits, xor_parts, pi)
                    if recurse_children_bits(exists_tree_lru, b0, b1, depth_remaining):
                        return True
            return False

        def clear_memo() -> None:
            exists_tree_lru.cache_clear()

        def memo_size() -> int:
            return exists_tree_lru.cache_info().currsize

        exists_tree_fn = exists_tree_lru

    lo = max(1, d_min)
    hi = max(lo, d_max)
    min_d: int | None = None
    peak_rss_kb: int | None = None
    for d in range(lo, hi + 1):
        clear_memo()
        t0 = time.perf_counter()
        print(f"  probing d={d} ...", flush=True)
        try:
            ok = exists_tree_fn(full_bits, d)
        except _BudgetExceeded:
            elapsed = time.perf_counter() - t0
            log.append((d, False, elapsed))
            label = "memo_dict_size" if memo_dict else "LRU currsize"
            print(
                f"  PARTIAL: exceeded max_exists_calls={max_exists_calls} "
                f"(exists_tree invocations; {label}={memo_size()}) "
                f"after {elapsed:.4f}s",
                flush=True,
            )
            if log_rss:
                rss = read_vm_rss_kb()
                if rss is not None:
                    print(f"  VmRSS_after_partial_d={d}_kb={rss}", flush=True)
            return None, log, True
        elapsed = time.perf_counter() - t0
        log.append((d, ok, elapsed))
        if log_rss:
            rss = read_vm_rss_kb()
            if rss is not None:
                peak_rss_kb = rss if peak_rss_kb is None else max(peak_rss_kb, rss)
                print(f"  VmRSS_after_d={d}_kb={rss}", flush=True)
        if ok:
            min_d = d
            break
        if log_cache_after_each_d:
            label = "memo_dict_entries" if memo_dict else "exists_tree_cache_misses"
            print(
                f"  {label}_after_d={d}: {memo_size()}",
                flush=True,
            )
    if log_rss and peak_rss_kb is not None:
        print(f"  VmRSS_peak_kb={peak_rss_kb}", flush=True)
    return min_d, log, False


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
        help='comma-separated r values for one mixed language, e.g. "2,3,4,5" (coord + those r-sparse XOR menus)',
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
        "--full-r2-r13-union-only",
        action="store_true",
        help=(
            "after baseline, skip per-r and partial-union probes; run a single DP over "
            "coord + every r-sparse XOR partition menu for r=2..n-1 (full combined language)."
        ),
    )
    p.add_argument(
        "--lru-maxsize",
        type=int,
        default=4_000_000,
        metavar="N",
        help="LRU cap for DP memo (0 = unbounded; default 4M avoids OOM on heavy shards)",
    )
    p.add_argument(
        "--d-min",
        type=int,
        default=1,
        metavar="D",
        help="first depth to probe (default 1; use with --d-max to narrow a stuck range)",
    )
    p.add_argument(
        "--d-max",
        type=int,
        default=N,
        metavar="D",
        help="last depth to probe (default n)",
    )
    p.add_argument(
        "--max-exists-calls",
        type=int,
        default=None,
        metavar="K",
        help=(
            "stop after K recursive evaluations of exists_tree (each call hits lru_cache; "
            "counts hits and misses — budget on total DP work units); "
            "exit 2 with PARTIAL if exceeded mid-probe. Default: unlimited."
        ),
    )
    p.add_argument(
        "--memo-dict",
        action="store_true",
        help=(
            "use a plain dict for (bits, depth) memo instead of functools.lru_cache — "
            "no eviction; can reduce repeated work vs a capped LRU on deep searches "
            "(RAM grows with distinct states)."
        ),
    )
    p.add_argument(
        "--log-rss",
        action="store_true",
        help=(
            "after each depth probe (and on PARTIAL), print VmRSS from /proc/self/status "
            "(Linux only; no-op if unavailable)."
        ),
    )
    p.add_argument(
        "--progress-every",
        type=int,
        default=0,
        metavar="K",
        help=(
            "when --max-exists-calls is set, print progress every K exists_tree invocations "
            "(0 = disabled). With --log-rss, append VmRSS."
        ),
    )
    p.add_argument(
        "--xor-index-range",
        type=str,
        default=None,
        metavar="START:END",
        help=(
            "with --r-single only: after building the r-sparse XOR partition list, "
            "use only half-open slice [START,END) (Python slice semantics). "
            "If any shard finds d feasible, the full menu is at least as expressive "
            "(same coord splits + superset of XOR splits), so min_d for the full "
            "language is <= d for that witness."
        ),
    )
    p.add_argument(
        "--xor-index-indices",
        type=str,
        default=None,
        metavar="I,J,K,...",
        help=(
            "with --r-single only: after building the full r-sparse XOR partition list "
            "(canonical order from itertools.combinations), keep only these 0-based "
            "indices (comma-separated). Mutually exclusive with --xor-index-range."
        ),
    )
    args = p.parse_args()
    lru_cap: int | None = None if args.lru_maxsize == 0 else args.lru_maxsize
    memo_dict_flag = bool(args.memo_dict)
    log_rss_flag = bool(args.log_rss)
    r_max = min(args.r_max, N - 1)
    d_min = max(1, args.d_min)
    d_max = max(d_min, min(args.d_max, N))
    exists_budget: int | None = args.max_exists_calls
    log_cache_after_d = exists_budget is not None
    progress_every = max(0, args.progress_every)

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)

    def baseline() -> tuple[int | None, int | None]:
        md0, log0, part0 = min_depth_for_language(
            masks,
            coord_parts,
            [],
            N,
            lru_cap,
            d_min=1,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        print(f"coord_only min_d={md0} (d_max={N})", flush=True)
        for d, ok, sec in log0:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if part0:
            print("PARTIAL: baseline coord_only hit max_exists_calls", flush=True)
            sys.exit(2)

        full_par_parts = build_r_xor_partition_masks(masks, N)
        assert len(full_par_parts) == 1
        md_full, log_full, partf = min_depth_for_language(
            masks,
            coord_parts,
            [full_par_parts],
            N,
            lru_cap,
            d_min=1,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        print(f"coord_plus_full_{N}xor min_d={md_full}", flush=True)
        for d, ok, sec in log_full:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if partf:
            print("PARTIAL: baseline full_n_xor hit max_exists_calls", flush=True)
            sys.exit(2)
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

    if args.full_r2_r13_union_only:
        if args.r_single is not None or args.union_rs is not None:
            print(
                "FAIL: --full-r2-r13-union-only is incompatible with "
                "--r-single / --union-rs",
                flush=True,
            )
            sys.exit(1)
        parts_by_r = {r: build_r_xor_partition_masks(masks, r) for r in range(2, N)}
        xor_lists = [parts_by_r[r] for r in range(2, N)]
        total_splits = sum(len(x) for x in xor_lists)
        t0 = time.perf_counter()
        md_all, lg_all, part_all = min_depth_for_language(
            masks,
            coord_parts,
            xor_lists,
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        t1 = time.perf_counter()
        print(
            f"coord_plus_r2_through_r{N - 1} total_splits={total_splits} min_d={md_all} "
            f"dp_sec={t1 - t0:.3f}",
            flush=True,
        )
        for d, ok, sec in lg_all:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if part_all:
            print("PARTIAL: full r2..r13 union hit max_exists_calls", flush=True)
            sys.exit(2)
        if not args.skip_baseline:
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
        if args.xor_index_range is not None and args.xor_index_indices is not None:
            print(
                "FAIL: use only one of --xor-index-range and --xor-index-indices",
                flush=True,
            )
            sys.exit(1)
        xor_slice: slice | None = None
        xor_pick: Sequence[int] | None = None
        if args.xor_index_range is not None:
            if ":" not in args.xor_index_range:
                print("FAIL: --xor-index-range must be START:END", flush=True)
                sys.exit(1)
            a, b = args.xor_index_range.split(":", 1)
            try:
                start = int(a) if a.strip() != "" else 0
                end = int(b) if b.strip() != "" else None
            except ValueError:
                print("FAIL: --xor-index-range START and END must be integers", flush=True)
                sys.exit(1)
            xor_slice = slice(start, end)
        elif args.xor_index_indices is not None:
            raw = [x.strip() for x in args.xor_index_indices.split(",") if x.strip()]
            try:
                xor_pick = sorted(set(int(x) for x in raw))
            except ValueError:
                print(
                    "FAIL: --xor-index-indices must be comma-separated integers",
                    flush=True,
                )
                sys.exit(1)
            if not xor_pick:
                print("FAIL: --xor-index-indices is empty", flush=True)
                sys.exit(1)
        t0 = time.perf_counter()
        xp = build_r_xor_partition_masks(masks, r)
        if xor_slice is not None:
            total_xp = len(xp)
            xp = xp[xor_slice]
            print(
                f"xor_index_range={xor_slice.start}:{xor_slice.stop} "
                f"using {len(xp)}/{total_xp} r-sparse XOR partitions",
                flush=True,
            )
            if len(xp) == 0:
                print("FAIL: empty XOR partition slice", flush=True)
                sys.exit(1)
        elif xor_pick is not None:
            total_xp = len(xp)
            bad = [i for i in xor_pick if i < 0 or i >= total_xp]
            if bad:
                print(
                    f"FAIL: xor_index_indices out of range [0,{total_xp}): {bad[:8]}…",
                    flush=True,
                )
                sys.exit(1)
            xp = [xp[i] for i in xor_pick]
            head = ",".join(str(i) for i in xor_pick[:12])
            tail = f",…({len(xor_pick)} total)" if len(xor_pick) > 12 else ""
            print(
                f"xor_index_indices count={len(xor_pick)}/{total_xp} "
                f"first=[{head}{tail}]",
                flush=True,
            )
        t1 = time.perf_counter()
        md, lg, partial = min_depth_for_language(
            masks,
            coord_parts,
            [xp],
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        t2 = time.perf_counter()
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md} "
            f"build_sec={t1-t0:.3f} dp_sec={t2-t1:.3f}",
            flush=True,
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if partial:
            print("PARTIAL: r_single probe hit max_exists_calls", flush=True)
            sys.exit(2)
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
        xor_lists = [build_r_xor_partition_masks(masks, r) for r in rs]
        total = sum(len(x) for x in xor_lists)
        t0 = time.perf_counter()
        md_u, _, part_u = min_depth_for_language(
            masks,
            coord_parts,
            xor_lists,
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        t1 = time.perf_counter()
        print(
            f"coord_plus_union_rs={rs} total_splits={total} min_d={md_u} "
            f"dp_sec={t1-t0:.3f}",
            flush=True,
        )
        if part_u:
            print("PARTIAL: union_rs probe hit max_exists_calls", flush=True)
            sys.exit(2)
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
        md, lg, part_r = min_depth_for_language(
            masks,
            coord_parts,
            [xp],
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        t2 = time.perf_counter()
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md} "
            f"build_sec={t1-t0:.3f} dp_sec={t2-t1:.3f}",
            flush=True,
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}", flush=True)
        if part_r:
            print(f"PARTIAL: r={r} sweep hit max_exists_calls", flush=True)
            sys.exit(2)

    parts_by_r = {r: build_r_xor_partition_masks(masks, r) for r in range(2, r_max + 1)}
    if r_max >= 4:
        p2, p3, p4 = parts_by_r[2], parts_by_r[3], parts_by_r[4]
        md_234, _, part234 = min_depth_for_language(
            masks,
            coord_parts,
            [p2, p3, p4],
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        print(f"coord_plus_r2_r3_r4 min_d={md_234}", flush=True)
        if part234:
            print("PARTIAL: r2_r3_r4 union hit max_exists_calls", flush=True)
            sys.exit(2)
    else:
        print("coord_plus_r2_r3_r4 skipped (r-max < 4)", flush=True)

    if r_max >= 5:
        p2, p3, p4 = parts_by_r[2], parts_by_r[3], parts_by_r[4]
        md_2345, _, part2345 = min_depth_for_language(
            masks,
            coord_parts,
            [p2, p3, p4, parts_by_r[5]],
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        print(f"coord_plus_r2_through_r5 min_d={md_2345}", flush=True)
        if part2345:
            print("PARTIAL: r2_through_r5 hit max_exists_calls", flush=True)
            sys.exit(2)

    if r_max >= N - 1:
        md_all, _, part_all = min_depth_for_language(
            masks,
            coord_parts,
            [parts_by_r[r] for r in range(2, N)],
            d_max,
            lru_cap,
            d_min=d_min,
            max_exists_calls=exists_budget,
            log_cache_after_each_d=log_cache_after_d,
            memo_dict=memo_dict_flag,
            log_rss=log_rss_flag,
            progress_every=progress_every,
        )
        print(f"coord_plus_r2_through_r{r_max} min_d={md_all}", flush=True)
        if part_all:
            print("PARTIAL: r2_through_r_max hit max_exists_calls", flush=True)
            sys.exit(2)

    if md0 is None or md_full is None or md_full != 1:
        print("FAIL", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
