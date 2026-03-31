#!/usr/bin/env python3
"""
Classify 2-bit Boolean gates f(a,b) for invariance under simultaneous negation:
  f(a,b) == f(1-a, 1-b)  for all a,b in {0,1}.

If true, then under global x -> x XOR (1,...,1), every pair-probe on (x_i,x_j)
returns the same bit as before the flip — the mechanism behind entry 049.

Gates checked: AND, OR, XOR, XNOR (1 iff a==b).
"""

from __future__ import annotations

from collections.abc import Callable


def invariant_under_two_bit_complement(f: Callable[[int, int], int]) -> bool:
    for a in (0, 1):
        for b in (0, 1):
            if f(a, b) != f(1 - a, 1 - b):
                return False
    return True


def main() -> None:
    gates = {
        "and": lambda a, b: a & b,
        "or": lambda a, b: a | b,
        "xor": lambda a, b: a ^ b,
        "xnor": lambda a, b: 1 - (a ^ b),  # equality a==b as int 0/1
    }

    print("gate  invariant_under_(a,b)->(1-a,1-b)")
    for name, g in gates.items():
        inv = invariant_under_two_bit_complement(g)
        print(f"  {name:4s}  {inv}")
        # brute truth table for the record
        for a in (0, 1):
            for b in (0, 1):
                assert 0 <= g(a, b) <= 1

    assert invariant_under_two_bit_complement(gates["xor"])
    assert invariant_under_two_bit_complement(gates["xnor"])
    assert not invariant_under_two_bit_complement(gates["and"])
    assert not invariant_under_two_bit_complement(gates["or"])

    # NAND / NOR for completeness
    nand = lambda a, b: 1 - (a & b)
    nor = lambda a, b: 1 - (a | b)
    print(f"  {'nand':4s}  {invariant_under_two_bit_complement(nand)}")
    print(f"  {'nor':4s}  {invariant_under_two_bit_complement(nor)}")

    print("PASS")


if __name__ == "__main__":
    main()
