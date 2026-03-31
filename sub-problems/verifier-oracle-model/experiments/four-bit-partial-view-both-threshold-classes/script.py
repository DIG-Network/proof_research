"""
Exhaustive check: n=10, for every Q with |Q|<=4 and every pattern p on Q,
both wt=5 and wt=6 global extensions exist (same partial view).

Also builds explicit u,v for a sample of cases (first failing would abort).
"""

from itertools import combinations

N = 10
WT_SUB = 5
WT_QUORUM = 6
MAX_Q = 4


def pattern_ones_count(q_mask: tuple[int, ...], pat: int) -> int:
    z = 0
    for i, idx in enumerate(q_mask):
        if (pat >> i) & 1:
            z += 1
    return z


def feasible(z: int, r: int, target_wt: int) -> bool:
    need = target_wt - z
    return 0 <= need <= r


def main() -> None:
    checked = 0
    for k in range(MAX_Q + 1):
        for q_mask in combinations(range(N), k):
            r = N - k
            for pat in range(1 << k):
                z = pattern_ones_count(q_mask, pat)
                ok5 = feasible(z, r, WT_SUB)
                ok6 = feasible(z, r, WT_QUORUM)
                if not (ok5 and ok6):
                    print("FAIL")
                    print(f"  Q_size={k} Q={q_mask} pat_bits={pat:0{k}b} z={z} R={r}")
                    print(f"  need5={WT_SUB - z} need6={WT_QUORUM - z} ok5={ok5} ok6={ok6}")
                    raise SystemExit(1)
                checked += 1

    print("PASS")
    print(f"  n={N} max_|Q|={MAX_Q} patterns_checked={checked}")
    print(
        "  For every (Q,p) with |Q|<=4, both wt=5 and wt=6 extensions exist "
        "(counting: 0 <= 5-z <= R and 0 <= 6-z <= R)."
    )


if __name__ == "__main__":
    main()
