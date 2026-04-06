#!/usr/bin/env python3
r"""
n=8, shell {2,3,4}: exhaustive partial r=6 submenu (K=2 of 28 splits) — off-diagonal s012 structure scan.

Enumerates all C(28,2)=378 unordered pairs of indices into the full r=6 XOR split list, appends those
two splits only to coord + full r=2 + doubleton r=3 + singleton r=4, and aggregates on s∈{0,1,2}:

  - stratum_min_d2 count
  - wedge predicate hits (diagnostic)
  - biconditional violation counts

Uses multiprocessing (default WORKERS=4, override with env WORKERS).

Hypothesis: some menu yields 0 < stratum_min_d2 < 107800.

Exit 0 if such a menu exists; exit 1 otherwise.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import time
from itertools import combinations
from multiprocessing import Pool, cpu_count
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8/script.py"
)

K_P6 = 2
LRU_CAP = 4_000_000
N_EXPECT = 8
FULL_MASK = (1 << N_EXPECT) - 1
STRATUM_TOTAL = 107_800


def _load_parent():
    spec = importlib.util.spec_from_file_location("n8driver", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def subset_mask(idxs: tuple[int, ...]) -> int:
    m = 0
    for i in idxs:
        m |= 1 << i
    return m


def popc(m: int) -> int:
    return m.bit_count()


def wedge_mask(t_a: int, t_b: int) -> int:
    only_a = t_a & (FULL_MASK ^ t_b)
    union = t_a | t_b
    exterior = FULL_MASK ^ union
    return only_a | exterior


def run_one_menu(
    mod,
    masks: list[int],
    coord: list[tuple[int, int]],
    p2: list[tuple[int, int]],
    p3: list[tuple[int, int]],
    p4: list[tuple[int, int]],
    p6: list[tuple[int, int]],
    p6_idx: tuple[int, ...],
) -> tuple[int, int, int, int, float]:
    triples = list(combinations(range(N_EXPECT), 3))
    quads = list(combinations(range(N_EXPECT), 4))

    viol_d2_not_pred = 0
    viol_pred_but_not_d2 = 0
    count_stratum_d2 = 0
    count_stratum_pred = 0

    partial_p6 = [p6[i] for i in p6_idx]

    t0 = time.perf_counter()
    for i in range(len(p3)):
        for j in range(i, len(p3)):
            for k in range(len(p4)):
                xor_lists: list[list[tuple[int, int]]] = [
                    p2,
                    [p3[i], p3[j]],
                    [p4[k]],
                    partial_p6,
                ]

                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )

                if i >= j:
                    continue

                t_i = subset_mask(triples[i])
                t_j = subset_mask(triples[j])
                q_mask = subset_mask(quads[k])

                s_inter = popc(t_i & t_j)
                if s_inter not in (0, 1, 2):
                    continue

                w_ij = wedge_mask(t_i, t_j)
                w_ji = wedge_mask(t_j, t_i)
                pred = (q_mask == w_ij) or (q_mask == w_ji)
                if pred:
                    count_stratum_pred += 1

                if md == 2:
                    count_stratum_d2 += 1
                    if not pred:
                        viol_d2_not_pred += 1
                elif pred and md is not None and md != 2:
                    viol_pred_but_not_d2 += 1

    wall = time.perf_counter() - t0
    return (
        count_stratum_d2,
        count_stratum_pred,
        viol_d2_not_pred,
        viol_pred_but_not_d2,
        wall,
    )


_G_MOD = None
_G_MASKS = None
_G_COORD = None
_G_P2 = None
_G_P3 = None
_G_P4 = None
_G_P6 = None


def _pool_init() -> None:
    global _G_MOD, _G_MASKS, _G_COORD, _G_P2, _G_P3, _G_P4, _G_P6
    _G_MOD = _load_parent()
    assert _G_MOD.N == N_EXPECT
    _G_MASKS = _G_MOD.build_masks()
    _G_COORD = _G_MOD.build_coord_partition_masks(_G_MASKS)
    _G_P2 = _G_MOD.build_r_xor_partition_masks(_G_MASKS, 2)
    _G_P3 = _G_MOD.build_r_xor_partition_masks(_G_MASKS, 3)
    _G_P4 = _G_MOD.build_r_xor_partition_masks(_G_MASKS, 4)
    _G_P6 = _G_MOD.build_r_xor_partition_masks(_G_MASKS, 6)


def _pool_task(
    idx_tuple: tuple[int, ...],
) -> tuple[tuple[int, ...], int, int, int, int, float]:
    assert _G_MOD is not None and _G_MASKS is not None
    d2, ph, v_d2, v_pd, wall = run_one_menu(
        _G_MOD,
        _G_MASKS,
        _G_COORD,
        _G_P2,
        _G_P3,
        _G_P4,
        _G_P6,
        idx_tuple,
    )
    return (idx_tuple, d2, ph, v_d2, v_pd, wall)


def main() -> None:
    workers_env = os.environ.get("WORKERS", "").strip()
    if workers_env:
        workers = max(1, int(workers_env))
    else:
        workers = max(1, min(4, cpu_count() or 1))

    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    p6 = mod.build_r_xor_partition_masks(masks, 6)
    assert len(p3) == 56 and len(p4) == 70 and len(p6) == 28

    if K_P6 <= 0 or K_P6 > len(p6):
        print(f"FAIL: need 0 < K_P6 <= {len(p6)}", flush=True)
        sys.exit(1)

    md_full, _ = mod.min_depth_for_language(
        masks,
        coord,
        [mod.build_r_xor_partition_masks(masks, mod.N)],
        mod.N,
        LRU_CAP,
    )
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    menus = list(combinations(range(len(p6)), K_P6))
    assert len(menus) == 378

    print(
        f"workers={workers} STRATUM_TOTAL={STRATUM_TOTAL} menus={len(menus)} k_p6={K_P6}",
        flush=True,
    )
    print(
        "idx p6_indices stratum_min_d2 stratum_pred viol_d2_not_pred viol_pred_not_d2 wall_sec",
        flush=True,
    )

    found_proper = False
    total_wall = 0.0
    min_d2_over_menus = STRATUM_TOTAL + 1
    max_d2_over_menus = -1

    t_all = time.perf_counter()
    if workers == 1:
        for idx, idx_tuple in enumerate(menus, start=1):
            d2, pred_hits, v_d2, v_pd, wall = run_one_menu(
                mod, masks, coord, p2, p3, p4, p6, idx_tuple
            )
            total_wall += wall
            min_d2_over_menus = min(min_d2_over_menus, d2)
            max_d2_over_menus = max(max_d2_over_menus, d2)
            print(
                f"{idx} {idx_tuple} {d2} {pred_hits} {v_d2} {v_pd} {wall:.3f}",
                flush=True,
            )
            if 0 < d2 < STRATUM_TOTAL:
                found_proper = True
    else:
        with Pool(processes=workers, initializer=_pool_init) as pool:
            results = pool.map(_pool_task, menus, chunksize=1)

        # Preserve deterministic ordering by idx_tuple / menu order
        menu_to_row = {r[0]: r for r in results}
        for idx, idx_tuple in enumerate(menus, start=1):
            row = menu_to_row[idx_tuple]
            _, d2, pred_hits, v_d2, v_pd, wall = row
            total_wall += wall
            min_d2_over_menus = min(min_d2_over_menus, d2)
            max_d2_over_menus = max(max_d2_over_menus, d2)
            print(
                f"{idx} {idx_tuple} {d2} {pred_hits} {v_d2} {v_pd} {wall:.3f}",
                flush=True,
            )
            if 0 < d2 < STRATUM_TOTAL:
                found_proper = True

    wall_all = time.perf_counter() - t_all
    print(
        f"STRATUM_TOTAL={STRATUM_TOTAL} menus={len(menus)} k_p6={K_P6} workers={workers} "
        f"proper_nonempty_proper={found_proper} sum_menu_wall_sec={total_wall:.3f} "
        f"wall_clock_sec={wall_all:.3f} "
        f"min_stratum_d2_across_menus={min_d2_over_menus} "
        f"max_stratum_d2_across_menus={max_d2_over_menus}",
        flush=True,
    )
    if found_proper:
        print(
            "PASS: at least one K=2 partial r=6 menu yields 0<stratum_min_d2<107800",
            flush=True,
        )
        sys.exit(0)
    print(
        "FAIL: every K=2 partial r=6 menu yields stratum_min_d2 in {0,107800} on this stratum",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
