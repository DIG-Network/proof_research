# Hypothesis — complementary triple pairs ⟺ `min_d=2` (n=6, shell `{2,3}`)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py`.

**Context:** Experiment `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-scan-all-pairs` found **exactly 10** unordered pairs of `r=3` splits (with **full** `r=2` menu + coord) achieve **`min_d=2`**, and described them as the **complementary** disjoint 3+3 partitions of `[6]`. The scan did not mechanically check the **converse**: that **every** non-complementary pair has **`min_d=3`**.

**Falsifiable claim (biconditional):** For **every** unordered pair `{i,j}` of triple indices in lex order on `C(6,3)`, letting **`comp(i,j)`** mean the two triples are **disjoint** (hence partition `[6]`),

> `min_d(coord + full r=2 + {i,j} r=3 splits) = 2` **if and only if** `comp(i,j)`.

- If **any** pair violates the biconditional → **FAIL** (classification incomplete or wrong).
- If **all 190** pairs satisfy it → **PASS** (structural certificate; “only complementary cuts work” is exact, not empirical coincidence).

## Analogy pass (mandatory)

1. **Abstract structure:** Empirical classification of witnesses vs a **graph-theoretic** predicate (perfect matching / vertex cut into two triples); upgrade from “the witness set equals X” to “X is **equivalent** to the optimality predicate.”

2. **Analogous domains:** (i) **Matroid** circuit characterization — minimal dependent sets vs rank; (ii) **Error-correcting** — codewords at **minimum distance** vs combinatorial support patterns; (iii) **Graph minors** — forbidden configurations vs global connectivity.

3. **Machinery:** Exhaustive check over finite label space; same DP as parent.

4. **Transfer seed:** Turn the **10/190** observation into a **logical** statement testable in one linear scan.
