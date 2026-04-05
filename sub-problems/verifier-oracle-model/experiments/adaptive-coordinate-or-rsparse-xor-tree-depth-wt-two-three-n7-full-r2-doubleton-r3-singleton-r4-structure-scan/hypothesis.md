# Hypothesis: n=7 full r=2 + multiset r=3 (two splits, pair with repetition) + one r=4

## Analogy pass

1. **Abstract structure:** The singleton `r=3` + singleton `r=4` grid showed `min_d=2` iff the quartic mask is the complement of the triple (a rigid `3+4` partition). Allowing **two** triple XOR splits (unordered pair of indices, repetition permitted) enlarges the query language; group-testing / parity-decoding analogies suggest new separations may appear without a complementary `4`-set.

2. **Analogous domains:** (i) **Group testing** — two pooled parity tests on overlapping triples vs. one quartic test. (ii) **Coding** — additional parity rows can change minimal decoding depth. (iii) **Decision trees** — redundant or correlated queries may or may not shrink depth.

3. **Machinery:** Same adaptive XOR-tree DP as parent; language is `coord + full r=2 + {xor_parts for two triples} + {one quad}`.

4. **Transfer seed:** Characterize **when** `min_d=2` occurs in the `630×35` grid (`C(35+1,2)` multiset pairs × quads). If the complement law survives only when the two triple indices coincide, that pins **multiplicity** as the minimal certificate for the `n=7` phenomenon.

## Falsifiable claims

**Primary:** Empirically classify all `(unordered pair of r=3 indices, r=4 index)` cells by `min_d` and report whether any cell with **distinct** triple indices (`i<j`) achieves `min_d=2`.

**Secondary:** When `i=j` (duplicate triple split — effectively one informative triple XOR), verify behavior matches the singleton triple case on that diagonal.

- **PASS (exit 0):** Scan completes; summary printed; no implementation errors.
- **FAIL (exit 1):** Baselines broken or script error.

## Lineage

- **Extends:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-complement-iff-check` (singleton `3+4` complement iff).
- **Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.
