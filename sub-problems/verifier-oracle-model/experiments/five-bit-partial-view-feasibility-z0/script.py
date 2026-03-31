"""
n=10, |Q|=5, R=5: classify partial patterns by feasibility of wt=5 vs wt=6 extensions.

Checks hypothesis:
- wt=6 possible iff z >= 1 (equivalently 6-z <= R=5)
- wt=5 possible for all z in 0..5
"""

from itertools import combinations

N = 10
K = 5
R = N - K
WT_SUB = 5
WT_Q = 6


def pattern_ones_count(q_mask: tuple[int, ...], pat: int) -> int:
    z = 0
    for i in range(len(q_mask)):
        if (pat >> i) & 1:
            z += 1
    return z


def feasible(z: int, r: int, target_wt: int) -> bool:
    need = target_wt - z
    return 0 <= need <= r


def main() -> None:
    both = 0
    only_sub = 0  # wt5 yes, wt6 no
    only_quorum = 0  # wt5 no, wt6 yes (expect 0)
    neither = 0

    for q_mask in combinations(range(N), K):
        for pat in range(1 << K):
            z = pattern_ones_count(q_mask, pat)
            ok5 = feasible(z, R, WT_SUB)
            ok6 = feasible(z, R, WT_Q)
            if ok5 and ok6:
                both += 1
            elif ok5 and not ok6:
                only_sub += 1
            elif not ok5 and ok6:
                only_quorum += 1
            else:
                neither += 1

            # Theorem check per pattern
            pred6 = z >= 1  # 6-z in [1,6] intersect [0,5] => z>=1
            if ok6 != pred6:
                print("FAIL: wt=6 feasibility mismatch")
                print(f"  Q={q_mask} pat={pat:05b} z={z} ok6={ok6} pred6={pred6}")
                raise SystemExit(1)
            if not ok5:
                print("FAIL: wt=5 should always be feasible for |Q|=5, z<=5")
                print(f"  Q={q_mask} pat={pat:05b} z={z}")
                raise SystemExit(1)

    total = both + only_sub + only_quorum + neither
    print("PASS")
    print(f"  n={N} |Q|={K} R={R} total_partial_assignments={total}")
    print(f"  both_wt5_and_wt6={both}")
    print(f"  only_wt5_no_wt6_(z=0_patterns)={only_sub}")
    print(f"  only_wt6_no_wt5={only_quorum}")
    print(f"  neither={neither}")
    assert only_sub == 252 * 1, "z=0 unique pattern per Q"
    assert both == 252 * 31
    assert only_quorum == 0 and neither == 0


if __name__ == "__main__":
    main()
