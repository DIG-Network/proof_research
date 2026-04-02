# Results

**Outcome:** INCONCLUSIVE (exit code 2 from wrapper: PARTIAL on both `r=5` and `r=9`, no `d=3` witness).

| Run | `exists_tree` budget | LRU | DP wall (s) | build (s) | Result |
|-----|----------------------|-----|-------------|-----------|--------|
| `r=5`, XOR indices `1,3,…,2001` | `1.2×10⁸` | 8M | 975.95 | 2.64 | PARTIAL at cap; `d=3 feasible=False` (incomplete) |
| `r=9`, same menu | `1.2×10⁸` | 8M | 859.96 | 4.11 | PARTIAL at cap; `d=3 feasible=False` (incomplete) |

Total sequential wall ≈ **1836 s** (~**30.6 min**).

**Comparison (same budget/LRU, sibling even-interleave `0,2,…,2000`):** ~941 s + ~941 s ≈ **1882 s** (~31.4 min). The complementary coset is slightly **faster** for this host (`r=5` a few percent slower than sibling’s ~941 s, `r=9` noticeably faster than sibling’s ~941 s), but both still **PARTIAL** with LRU saturated (`currsize=8000000`).
