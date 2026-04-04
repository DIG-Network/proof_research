# Notes — complementary ⟺ `min_d=2` check

- **Implementation:** Rebuild `triples = list(combinations(range(6),3))` in lockstep with `build_r_xor_partition_masks(..., 3)` (same lex order).
- **Logic:** For each unordered pair `(i,j)`, compute `disjoint = not (set(triples[i]) & set(triples[j]))`, run `min_depth_for_language` with `[p2, [p3[i], p3[j]]]`, compare `(md == 2)` to `disjoint`.
- **No new DP:** Same cost profile as the all-pairs scan (~0.12 s wall on this host).
