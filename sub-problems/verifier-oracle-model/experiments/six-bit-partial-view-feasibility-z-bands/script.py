"""
n=10, |Q|=6, R=4: classify (Q,p) by feasibility of wt=5 vs wt=6 extensions.

Predicted bands (z = ones on Q):
  z=0: neither (need 5 or 6 ones in 4 outside slots)
  z=1: only wt=5
  z=2..5: both
  z=6: only wt=6
"""

from itertools import combinations

N = 10
K = 6
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
    if z == 0:
        return "neither"
    if z == 1:
        return "only_wt5"
    if 2 <= z <= 5:
        return "both"
    if z == 6:
        return "only_wt6"
    raise ValueError(z)


def main() -> None:
    counts: dict[str, int] = {k: 0 for k in ("both", "only_wt5", "only_wt6", "neither")}

    for q_mask in combinations(range(N), K):
        for pat in range(1 << K):
            z = popcount(pat, K)
            ok5 = feasible(z, R, WT_SUB)
            ok6 = feasible(z, R, WT_Q)
            c = cell(ok5, ok6)
            counts[c] += 1
            if c != predicted_cell(z):
                print("FAIL: z mismatch")
                print(f"  Q={q_mask} pat={pat:06b} z={z} ok5={ok5} ok6={ok6} cell={c} pred={predicted_cell(z)}")
                raise SystemExit(1)

    total = sum(counts.values())
    print("PASS")
    print(f"  n={N} |Q|={K} R={R} total={total}")
    for k in ("both", "only_wt5", "only_wt6", "neither"):
        print(f"  {k}={counts[k]}")
    assert total == 13440
    assert counts["neither"] == 210
    assert counts["only_wt5"] == 1260
    assert counts["both"] == 11760
    assert counts["only_wt6"] == 210


if __name__ == "__main__":
    main()
