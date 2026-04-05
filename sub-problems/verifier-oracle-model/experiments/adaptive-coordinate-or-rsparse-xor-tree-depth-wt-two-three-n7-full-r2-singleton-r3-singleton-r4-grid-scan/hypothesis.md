# Hypothesis: n=7 full r=2 + one r=3 + one r=4 — grid scan

## Analogy pass

1. **Abstract structure:** Fix a finite family of binary partitions of a mask alphabet (coordinate splits + XOR splits at arity 2, 3, 4). The adaptive XOR-tree model asks for the minimum decision-tree depth that accepts the full mask set under those splits. Sparse menus are subsets of the full multi-arity union; threshold-style “majority shell” geometry interacts with which parities are available.

2. **Analogous domains:** (i) **Computational learning theory** — hypothesis classes defined by nested halfspace / parity queries; adding queries can shrink or leave VC-style depth unchanged. (ii) **Combinatorial group testing** — which pooled tests (XOR parities) detect a property with few rounds. (iii) **Error-correcting codes** — which parity checks (rows) are needed so a decoder succeeds; dropping checks can raise required depth.

3. **Machinery in those domains:** Certificate size vs. query complexity; covering designs; minimal test sets for separability.

4. **Transfer seed:** The prior experiment showed **full** `r=3` menu (35 splits) plus **any** single `r=4` still yields `min_d=2` uniformly. The **group testing** analogy suggests that **one** triple parity might be insufficient to pair with a quartic to still achieve depth 2 — i.e. some `(r3, r4)` pairs might force `min_d ≥ 3`.

## Falsifiable claim

**Primary:** There exists at least one pair `(i,j)` with `i,j ∈ {0,…,34}` (one `r=3` split index, one `r=4` split index) such that, with coordinate splits, **full** `r=2` XOR menu, exactly that one `r=3` XOR split, and exactly that one `r=4` XOR split, the minimum adaptive-tree depth satisfies `min_d ≥ 3`.

- **PASS (exit 0):** At least one grid cell has `min_d ≥ 3`.
- **FAIL (exit 1):** All `C(7,3)×C(7,4) = 35×35 = 1225` pairs yield `min_d = 2`.

## Lineage

- **Extends / contrasts:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once` (full `r=3` + singleton `r=4` → uniform `min_d=2`).
- **Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.
