# Hypothesis — exhaustive biconditional at n=7 (shell `{2,3}`)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.

**Context:** At **n=6**, **`min_d(coord + full r=2 + two r=3 splits) = 2`** iff the two triples are **disjoint** (complementary **3+3**). Random sample **200/595** at **n=7** (**`…-n7-pair-r3-random-sample-biconditional-check`**) found **23** cases with **disjoint** triples but **`min_d=3`**, falsifying the naive lift of that biconditional.

**Falsifiable claim (exhaustive):** Scan **all** **`C(35,2)=595`** unordered pairs of triple indices. For each pair **`(i,j)`**, let **`disjoint`** mean the triples share no vertex.

> `min_d == 2` **if and only if** `disjoint`.

- If **any** violation → **FAIL** (predicate wrong; report full violation count and sample rows).
- If **violations=0** → **PASS** (unexpected repair of the random-sample picture — would contradict the sample unless sample was buggy).

**Expected:** **FAIL** with **violations > 0**, matching the sampled direction; this run **confirms counts** on the full **595** universe (not a statistical estimate).

## Analogy pass (mandatory)

1. **Abstract structure:** Finite label space; test logical equivalence between a **graph-theoretic** predicate (edge-disjoint **3-sets** on **7** vertices) and a **computational** predicate (**DP** **min** **depth** **2**).

2. **Analogous domains:** (i) **Forbidden minor** / **obstruction** lists — global property vs local patterns; (ii) **SAT** phase transition — rare witnesses vs majority regime; (iii) **Design theory** — when two blocks determine a **resolution** vs leave a **hole**.

3. **Machinery:** Exhaustive enumeration; same memoized **exists_tree** DP as **n=6** biconditional script.

4. **Transfer seed:** Replace **sampling** **uncertainty** with a **single** **linear** **scan** **certificate** over **595** pairs.
