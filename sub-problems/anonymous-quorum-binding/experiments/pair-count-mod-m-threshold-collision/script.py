#!/usr/bin/env python3
"""
Unweighted pair statistic for a signer set S (characteristic vector):

  h(S) = #{unordered pairs {i,j} subset S} = C(|S|, 2) = |S|(|S|-1)/2

Toy binding question: can the verifier learn |S| in {t-1, t} from h(S) mod M?

Algebra: C(t,2) - C(t-1,2) = t-1  (for integer t >= 2)
So C(t-1,2) ≡ C(t,2) (mod M)  iff  M | (t-1).

Example t=6: C(5,2)=10, C(6,2)=15, difference 5 ⇒ M=5 gives both ≡ 0 (mod 5).
"""

from __future__ import annotations


def choose2(k: int) -> int:
    return k * (k - 1) // 2


def diff_adjacent(t: int) -> int:
    """C(t,2) - C(t-1,2) for t >= 2."""
    assert t >= 2
    return choose2(t) - choose2(t - 1)


def main() -> None:
    # Identity: difference equals t-1
    for t in range(2, 25):
        d = diff_adjacent(t)
        assert d == t - 1, (t, d)

    t = 6
    a, b = choose2(t - 1), choose2(t)
    assert (a, b) == (10, 15)
    M = t - 1
    assert M == 5
    assert a % M == b % M == 0

    # All divisors M>1 of (t-1) give modular collision for this pair of sizes
    delta = t - 1
    divs = [M for M in range(2, delta + 1) if delta % M == 0]
    assert 5 in divs

    print("PASS")
    print(f"  C({t-1},2)={a}, C({t},2)={b}, diff={delta}")
    print(f"  mod M={M}: both residues {a % M} (collision for t-1 vs t quorum edge)")
    print(f"  general: C(t,2)-C(t-1,2)=t-1 ⇒ modular collision iff M | (t-1)")


if __name__ == "__main__":
    main()
