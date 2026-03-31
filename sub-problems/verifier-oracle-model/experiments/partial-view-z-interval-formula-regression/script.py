"""
Closed form for coordinate-probe feasibility (binary n-vector, Hamming weight).

Fix |Q| = k, R = n - k, z = wt(p) on Q. Total weight w is feasible iff
  max(0, w - R) <= z <= min(k, w).

Compare per-(n,k,t) cell counts from summing binom(k,z) over z-bands vs
full brute enumeration over all Q and all 2^k patterns.
"""

from itertools import combinations
import math

def feasible(z: int, r: int, target_wt: int) -> bool:
    need = target_wt - z
    return 0 <= need <= r


def z_interval(n: int, k: int, w: int) -> tuple[int, int]:
    """Inclusive integer z-range for which some completion has total weight w."""
    r = n - k
    lo = max(0, w - r)
    hi = min(k, w)
    return lo, hi


def in_interval(z: int, lo: int, hi: int) -> bool:
    return lo <= z <= hi


def cell(ok_sub: bool, ok_q: bool) -> str:
    if ok_sub and ok_q:
        return "both"
    if ok_sub and not ok_q:
        return "only_wt5"
    if not ok_sub and ok_q:
        return "only_wt6"
    return "neither"


def formula_counts_per_q(n: int, k: int, t: int) -> dict[str, int]:
    """Patterns on a fixed Q: sum_z binom(k,z) over each cell (totals 2^k)."""
    lo_sub, hi_sub = z_interval(n, k, t - 1)
    lo_q, hi_q = z_interval(n, k, t)
    out = {c: 0 for c in ("both", "only_wt5", "only_wt6", "neither")}
    for z in range(k + 1):
        ok_sub = in_interval(z, lo_sub, hi_sub)
        ok_q = in_interval(z, lo_q, hi_q)
        out[cell(ok_sub, ok_q)] += math.comb(k, z)
    return out


def formula_counts_global(n: int, k: int, t: int) -> dict[str, int]:
    """All (Q, p) pairs: C(n,k) choices of Q times per-Q pattern counts."""
    per = formula_counts_per_q(n, k, t)
    mult = math.comb(n, k)
    return {c: mult * per[c] for c in per}


def popcount(pat: int, k: int) -> int:
    z = 0
    for i in range(k):
        if (pat >> i) & 1:
            z += 1
    return z


def brute_counts(n: int, k: int, t: int) -> dict[str, int]:
    r = n - k
    counts = {c: 0 for c in ("both", "only_wt5", "only_wt6", "neither")}
    for _q in combinations(range(n), k):
        for pat in range(1 << k):
            z = popcount(pat, k)
            ok_sub = feasible(z, r, t - 1)
            ok_q = feasible(z, r, t)
            counts[cell(ok_sub, ok_q)] += 1
    return counts


def assert_equal(a: dict[str, int], b: dict[str, int], label: str) -> None:
    for k in a:
        if a[k] != b[k]:
            print("FAIL", label, k, a[k], b[k])
            raise SystemExit(1)


def main() -> None:
    # Per-Q weights sum to 2^k
    for n, k, t in ((10, 6, 6), (10, 9, 6)):
        pq = formula_counts_per_q(n, k, t)
        s = sum(pq.values())
        if s != 1 << k:
            print("FAIL per_q sum", n, k, t, s)
            raise SystemExit(1)

    # Regression: global formula vs brute for (10,6,k), k=4..9 (entries 037–042)
    for k in range(4, 10):
        f = formula_counts_global(10, k, 6)
        b = brute_counts(10, k, 6)
        assert_equal(f, b, f"n=10 k={k} t=6")

    # Spot-check small instances
    cases = [
        (7, 3, 4),
        (8, 5, 5),
        (12, 6, 7),
        (15, 10, 8),
        (6, 2, 3),
        (9, 9, 5),
    ]
    for n, k, t in cases:
        if t < 1 or t > n or k > n or k < 0:
            continue
        f = formula_counts_global(n, k, t)
        b = brute_counts(n, k, t)
        assert_equal(f, b, f"n={n} k={k} t={t}")

    print("PASS")
    print("  formula_counts_global == brute_counts for (10,6,k) k=4..9 and spot cases")


if __name__ == "__main__":
    main()
