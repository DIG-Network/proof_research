#!/usr/bin/env python3
"""
F2 linear measurements: build n-1 independent parity pools r_j with r_j·d = 0
for d = x XOR y, so all pools agree on majority pattern x and minority pattern y.

n=8, t=5: x has 5 ones, y has 4 ones, same syndrome under those pools.
"""

from __future__ import annotations


def popcount(v: int) -> int:
    return v.bit_count()


def dot_f2(r: int, x: int, n: int) -> int:
    """r · x over F2 on n low bits (standard inner product mod 2)."""
    m = (1 << n) - 1
    return popcount((r & x) & m) & 1


def gf2_rank(bitrows: list[int], n: int) -> int:
    """Rank over F2; copies bitrows internally."""
    mat = bitrows[:]
    rnk = 0
    for col in range(n - 1, -1, -1):
        pivot = None
        for i in range(rnk, len(mat)):
            if (mat[i] >> col) & 1:
                pivot = i
                break
        if pivot is None:
            continue
        mat[rnk], mat[pivot] = mat[pivot], mat[rnk]
        for i in range(len(mat)):
            if i != rnk and ((mat[i] >> col) & 1):
                mat[i] ^= mat[rnk]
        rnk += 1
    return rnk


def independent_subset(cands: list[int], n: int, target: int) -> list[int]:
    """Greedy: extend while rank increases."""
    out: list[int] = []
    for r in cands:
        trial = out + [r]
        if gf2_rank(trial, n) == len(trial):
            out.append(r)
        if len(out) >= target:
            break
    return out


def main() -> None:
    n = 8
    t = n // 2 + 1
    # x: five low indices; y: four low indices
    x = (1 << 5) - 1  # bits 0..4
    y = (1 << 4) - 1  # bits 0..3
    assert popcount(x) == t
    assert popcount(y) == t - 1

    d = x ^ y
    assert d != 0

    cands = [r for r in range(1 << n) if dot_f2(r, d, n) == 0]
    assert len(cands) == 2 ** (n - 1)

    rows = independent_subset(cands, n, n - 1)
    assert len(rows) == n - 1
    assert gf2_rank(rows[:], n) == n - 1

    for j, r in enumerate(rows):
        bx = dot_f2(r, x, n)
        by = dot_f2(r, y, n)
        assert bx == by, f"row {j} mismatch"

    print(f"n={n} t={t} wt(x)={popcount(x)} wt(y)={popcount(y)} d=0x{d:02x}")
    print(f"independent parity pools: {len(rows)} (max possible dim orth complement = {n-1})")
    print("all pool outputs match on x and y")
    print("RESULT: PASS - F2-linear pools can hide majority vs one-below-threshold")


if __name__ == "__main__":
    main()
