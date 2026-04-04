# Hypothesis — n=7, three `r=3` XOR splits (exhaustive triples)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.

**Context:** At **n=7**, shell **`{2,3}`**, language **coord + full `r=2` XOR menu + two `r=3` splits** yields **`min_d=3`** for **all** **`C(35,2)=595`** unordered pairs of triple indices (**experiment** **`…-n7-pair-r3-biconditional-scan-all-pairs`**). Session state asked whether **three** triple-XOR splits can restore **`min_d=2`**.

**Falsifiable claim:** Exhaustively scan **all** **`C(35,3)=6545`** unordered triples **`(i,j,k)`** of triple indices. Let the XOR menu be **`[p2, [p3[i], p3[j], p3[k]]]`** (full **`r=2`** plus exactly **three** **`r=3`** parities).

- If **any** triple achieves **`min_d=2`** → **PASS** (three splits suffice somewhere on this sparse menu).
- If **none** achieve **`min_d=2`** → **FAIL** (uniform **`min_d=3`** persists for this **3-triple** slice; need more splits or a different language).

## Analogy pass (mandatory)

1. **Abstract structure:** Monotone **complexity** of a **decision problem** as we add **parity queries** (XOR splits) from a **finite menu**; ask for the **smallest** **cardinality** of a **subset** of queries that **drops** **depth** from **3** to **2**.

2. **Analogous domains:** (i) **Covering codes** — smallest set of **linear** tests **separating** **states**; (ii) **committee machines** — depth **2** **vs** **3** **in** **Boolean** **circuits**; (iii) **Design** **theory** — **blocks** **(triples)** **whose** **incidence** **matrix** **rank** **controls** **resolution**.

3. **Machinery:** Exhaustive **enumeration** **over** **combinations**; same **memoized** **`exists_tree`** **DP** **as** **pair** **scans**.

4. **Transfer seed:** **Third** **triple** **parity** **as** **extra** **degree** **of** **freedom** **after** **two-triple** **uniform** **failure** **at** **n=7**.
