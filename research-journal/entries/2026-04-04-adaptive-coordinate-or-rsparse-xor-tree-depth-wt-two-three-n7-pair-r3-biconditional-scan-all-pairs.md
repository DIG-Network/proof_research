# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-biconditional-scan-all-pairs`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-biconditional-scan-all-pairs`

**Context:** verifier-oracle-model (**n=7**, shell **`{2,3}`**, coord + full **`r=2`** + two **`r=3`** splits)

**Hypothesis tested:** Exhaustive check of **`min_d=2` ⟺ disjoint triples** over all **`C(35,2)=595`** pairs (confirms / quantifies the prior **200-pair** random sample).

**Outcome:** FAIL

**Key finding:** **`witness_min_d2_count=0`** — **no** pair achieves **`min_d=2`**. **All** **`595`** pairs have **`min_d=3`**. The **70** disjoint triple pairs ( **`7×C(6,3)/2`** ) are exactly the biconditional “violations” against the **n=6** predicate (**disjoint ⇒ depth 2**): they are **disjoint** but **`min_d=3`**. Wall time **~1.7 s** with **`4M`** LRU.

**Implications:**

- The **two-triple + full r=2** menu is **uniformly depth-3** at **n=7**; the **n=6** depth-2 phenomenon is **not** a monotone lift in **n**.
- The random-sample **FAIL** was **undercounting** disjoint violations (**23/200** vs **70** total disjoint pairs in the universe).

**Analogy pass summary:** Same as parent experiment — exhaustive finite classification vs graph-theoretic predicate.

**Scope:** Full **595** scan (**not** sampled).
