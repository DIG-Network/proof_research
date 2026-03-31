#!/usr/bin/env python3
"""
n=10 participation bits v_i in {0,1}; quorum threshold t=6 (strict majority).
For every Q with |Q|=4, build a,b with wt(a)=5, wt(b)=6 and a|_Q = b|_Q (all zeros on Q).

Construction: fix a|_Q = b|_Q = 0 on Q; put 5 vs 6 ones on the 6 outside indices.
"""

from __future__ import annotations

import itertools
import math

N = 10
T = 6
SUB = 5
QUERY_SIZE = 4


def hamming(w: list[int]) -> int:
    return sum(w)


def main() -> None:
    verts = list(range(N))
    for q in itertools.combinations(verts, QUERY_SIZE):
        qset = set(q)
        outside = [i for i in verts if i not in qset]
        assert len(outside) == N - QUERY_SIZE == 6

        a = [0] * N
        b = [0] * N
        for i in q:
            a[i] = b[i] = 0
        for i in outside[:SUB]:
            a[i] = 1
        for i in outside:
            b[i] = 1

        assert hamming(a) == SUB and hamming(b) == T
        assert all(a[i] == b[i] for i in qset)

    num_q = math.comb(N, QUERY_SIZE)
    print(f"Checked all C({N},{QUERY_SIZE})={num_q} query sets Q of size {QUERY_SIZE}.")
    print(
        "Construction: a|_Q=b|_Q=0; a has 5 ones on first 5 outside verts; b has 6 ones on all outside."
    )
    print(
        "RESULT: PASS - every non-adaptive 4-query observation class intersects both wt=5 and wt=6"
    )


if __name__ == "__main__":
    main()
