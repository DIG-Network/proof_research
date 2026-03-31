"""
n=10, |Q|=9, R=1: classify (Q,p) by feasibility of wt=5 vs wt=6.

Predicted (z = ones on Q):
  z in {0,1,2,3,7,8,9}: neither
  z = 4: only_wt5
  z = 5: both
  z = 6: only_wt6

Total: C(10,9)*512 = 10*512 = 5120
"""

from itertools import combinations

N = 10
K = 9
R = N - K
WT_SUB = 5
WT_Q = 6


def popcount(pat: int, k: int) -> int:
    z = 0
    for i in range(k):
        if (pat >> i) & 1:
            z += 1
    return z


def feasible(z: int, r: int, target_wt: int) -> bool:
    need = target_wt - z
    return 0 <= need <= r


def cell(ok5: bool, ok6: bool) -> str:
    if ok5 and ok6:
        return "both"
    if ok5 and not ok6:
        return "only_wt5"
    if not ok5 and ok6:
        return "only_wt6"
    return "neither"


def predicted_cell(z: int) -> str:
    if z in (0, 1, 2, 3, 7, 8, 9):
        return "neither"
    if z == 4:
        return "only_wt5"
    if z == 5:
        return "both"
    if z == 6:
        return "only_wt6"
    raise ValueError(z)


def main() -> None:
    counts = {k: 0 for k in ("both", "only_wt5", "only_wt6", "neither")}

    for q_mask in combinations(range(N), K):
        for pat in range(1 << K):
            z = popcount(pat, K)
            ok5 = feasible(z, R, WT_SUB)
            ok6 = feasible(z, R, WT_Q)
            c = cell(ok5, ok6)
            counts[c] += 1
            if c != predicted_cell(z):
                print("FAIL")
                print(f"  Q={q_mask} pat={pat:09b} z={z} ok5={ok5} ok6={ok6} cell={c} pred={predicted_cell(z)}")
                raise SystemExit(1)

    total = sum(counts.values())
    print("PASS")
    print(f"  n={N} |Q|={K} R={R} total={total}")
    for k in ("both", "only_wt5", "only_wt6", "neither"):
        print(f"  {k}={counts[k]}")
    assert total == 5120
    assert counts["neither"] == 1760
    assert counts["only_wt5"] == 1260
    assert counts["both"] == 1260
    assert counts["only_wt6"] == 840
    print("  per_Q: neither=176 only_wt5=126 both=126 only_wt6=84 (of 512)")


if __name__ == "__main__":
    main()
