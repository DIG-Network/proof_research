#!/usr/bin/env python3
"""
Binary leaf vectors v in {0,1}^n; Lagrange interpolant P on nodes 0..n-1.
Brute-force bucket by (P(r1), P(r2)) mod p; pigeonhole guarantees collision when 2^n > p^2.
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
    n = 16
    assert 2**n > p * p, "pigeonhole: need 2^n > p^2 for guaranteed collision existence"

    nodes = list(range(n))
    r1, r2 = 90, 91
    for r in (r1, r2):
        assert r not in nodes

    L1 = lagrange_basis_at(r1, nodes, p)
    L2 = lagrange_basis_at(r2, nodes, p)

    seen: dict[tuple[int, int], list[int]] = {}
    for mask in range(1 << n):
        v = [(mask >> i) & 1 for i in range(n)]
        e1 = eval_at_r(v, L1, p)
        e2 = eval_at_r(v, L2, p)
        key = (e1, e2)
        if key in seen:
            u = seen[key]
            assert u != v
            print(f"p={p} n={n} r1={r1} r2={r2} shared (P(r1),P(r2))={key}")
            print(f"Hamming distance={sum(u[i] != v[i] for i in range(n))}")
            print("RESULT: PASS - two evaluations do not injectively label all binary patterns")
            return
        seen[key] = v

    print("RESULT: FAIL - no binary collision found (unexpected under pigeonhole)")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
