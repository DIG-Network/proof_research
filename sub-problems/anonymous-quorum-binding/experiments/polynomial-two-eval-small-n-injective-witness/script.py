#!/usr/bin/env python3
"""
n=10, p=97: 2^n = 1024 < p^2 = 9409 — pigeonhole does not force collisions on F_p^2.

Exhaustive search over distinct evaluation points r1,r2 not in nodes {0..n-1}
for Lagrange interpolant P on those nodes; test injectivity of
  v in {0,1}^n  ->  (P(r1), P(r2)) in F_p^2.

Contrast: polynomial-two-eval-binary-collision uses n=16 so 2^n > p^2 (forced collision).
"""

from __future__ import annotations

from itertools import combinations


def modinv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def lagrange_basis_at(r: int, nodes: list[int], p: int) -> list[int]:
    out: list[int] = []
    for i, xi in enumerate(nodes):
        num, den = 1, 1
        for j, xj in enumerate(nodes):
            if j == i:
                continue
            num = (num * (r - xj)) % p
            den = (den * (xi - xj)) % p
        out.append((num * modinv(den, p)) % p)
    return out


def eval_at_r(vals: list[int], L: list[int], p: int) -> int:
    return sum((vals[i] * L[i]) % p for i in range(len(vals))) % p


def is_injective_on_hypercube(r1: int, r2: int, n: int, p: int) -> bool:
    nodes = list(range(n))
    L1 = lagrange_basis_at(r1, nodes, p)
    L2 = lagrange_basis_at(r2, nodes, p)
    seen: set[tuple[int, int]] = set()
    for mask in range(1 << n):
        v = [(mask >> i) & 1 for i in range(n)]
        e1 = eval_at_r(v, L1, p)
        e2 = eval_at_r(v, L2, p)
        key = (e1, e2)
        if key in seen:
            return False
        seen.add(key)
    return True


def find_collision_pair(r1: int, r2: int, n: int, p: int) -> tuple[list[int], list[int]] | None:
    nodes = list(range(n))
    L1 = lagrange_basis_at(r1, nodes, p)
    L2 = lagrange_basis_at(r2, nodes, p)
    seen: dict[tuple[int, int], list[int]] = {}
    for mask in range(1 << n):
        v = [(mask >> i) & 1 for i in range(n)]
        key = (eval_at_r(v, L1, p), eval_at_r(v, L2, p))
        if key in seen:
            return seen[key], v
        seen[key] = v
    return None


def main() -> None:
    p, n = 97, 10
    assert 2**n < p * p

    nodes = set(range(n))
    candidates = [x for x in range(p) if x not in nodes]

    first_injective: tuple[int, int] | None = None
    injective_count = 0
    for r1, r2 in combinations(candidates, 2):
        if is_injective_on_hypercube(r1, r2, n, p):
            injective_count += 1
            if first_injective is None:
                first_injective = (r1, r2)

    if first_injective is None:
        print("FAIL: no injective (r1,r2) found in exhaustive search")
        raise SystemExit(1)

    # Contrast: same (r1,r2) as n=16 collision experiment — at n=10 should still collide or not?
    r_a, r_b = 90, 91
    assert r_a not in nodes and r_b not in nodes
    col = find_collision_pair(r_a, r_b, n, p)
    if col is None:
        print("NOTE: (90,91) injective at n=10 (unexpected for contrast)")
    else:
        u, v = col
        assert u != v

    print("PASS")
    print(f"  n={n} p={p}: 2^n={2**n} < p^2={p*p}")
    print(f"  first_injective_pair={first_injective}")
    print(f"  total_injective_pairs_among_C({len(candidates)},2)={injective_count}")
    if col is not None:
        du = sum(u[i] != v[i] for i in range(n))
        print(f"  collision_for_(90,91): Hamming_distance={du}")

    assert first_injective == (10, 26), "regression: known minimal witness"


if __name__ == "__main__":
    main()
