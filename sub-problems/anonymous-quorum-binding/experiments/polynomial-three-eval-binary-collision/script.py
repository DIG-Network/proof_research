#!/usr/bin/env python3
"""
Binary leaf vectors v in {0,1}^n; Lagrange interpolant P on nodes 0..n-1.
Bucket by (P(r1), P(r2), P(r3)) mod p; pigeonhole when 2^n > p^3.
"""

from __future__ import annotations


def modinv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def lagrange_basis_at(r: int, nodes: list[int], p: int) -> list[int]:
    n = len(nodes)
    out: list[int] = []
    for i in range(n):
        xi = nodes[i]
        num, den = 1, 1
        for j in range(n):
            if j == i:
                continue
            xj = nodes[j]
            num = (num * (r - xj)) % p
            den = (den * (xi - xj)) % p
        out.append((num * modinv(den, p)) % p)
    return out


def eval_at_r(vals: list[int], L: list[int], p: int) -> int:
    return sum((vals[i] * L[i]) % p for i in range(len(vals))) % p


def main() -> None:
    p = 97
    n = 20
    assert 2**n > p**3, "pigeonhole: need 2^n > p^3"

    nodes = list(range(n))
    r1, r2, r3 = 90, 91, 92
    for r in (r1, r2, r3):
        assert r not in nodes

    L1 = lagrange_basis_at(r1, nodes, p)
    L2 = lagrange_basis_at(r2, nodes, p)
    L3 = lagrange_basis_at(r3, nodes, p)

    seen: dict[tuple[int, int, int], list[int]] = {}
    for mask in range(1 << n):
        v = [(mask >> i) & 1 for i in range(n)]
        e1 = eval_at_r(v, L1, p)
        e2 = eval_at_r(v, L2, p)
        e3 = eval_at_r(v, L3, p)
        key = (e1, e2, e3)
        if key in seen:
            u = seen[key]
            assert u != v
            print(f"p={p} n={n} r1={r1} r2={r2} r3={r3} shared triple={key}")
            print(f"Hamming distance={sum(u[i] != v[i] for i in range(n))}")
            print("RESULT: PASS - three evaluations do not injectively label all binary patterns")
            return
        seen[key] = v

    print("RESULT: FAIL - no binary collision found (unexpected under pigeonhole)")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
