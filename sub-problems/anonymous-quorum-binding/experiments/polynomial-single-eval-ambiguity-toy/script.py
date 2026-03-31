#!/usr/bin/env python3
"""
Lagrange interpolation at nodes 0..n-1; show many w share same P(r) as fixed v.

Field F_p, p prime; one evaluation imposes one linear constraint on n values.
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
    p = 1009
    n = 8
    nodes = list(range(n))
    r = 900
    assert r not in nodes

    L = lagrange_basis_at(r, nodes, p)
    # Ensure last basis element invertible for solving w_{n-1}
    assert L[-1] % p != 0

    v = [(i + 1) % p for i in range(n)]
    c = eval_at_r(v, L, p)

    # Free first n-1 coordinates, solve for w_{n-1}
    w = [0] * n
    for i in range(n - 1):
        w[i] = (v[i] + 7 + i * 13) % p  # arbitrary != v[i] typically
    acc = sum((w[i] * L[i]) % p for i in range(n - 1)) % p
    w[n - 1] = ((c - acc) % p) * modinv(L[n - 1], p) % p

    assert w != v
    assert eval_at_r(w, L, p) == c == eval_at_r(v, L, p)

    diff = sum(1 for i in range(n) if w[i] != v[i])
    print(f"p={p} n={n} r={r} shared_P(r)={c}")
    print(f"Hamming(v,w)={diff}")
    print("RESULT: PASS - one evaluation leaves non-unique assignment vector")


if __name__ == "__main__":
    main()
