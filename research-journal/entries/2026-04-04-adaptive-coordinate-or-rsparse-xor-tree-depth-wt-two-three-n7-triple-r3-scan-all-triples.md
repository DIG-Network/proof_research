# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-triple-r3-scan-all-triples`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-triple-r3-scan-all-triples`

**Problem context:** verifier-oracle-model (`{2,3}` shell, adaptive coordinate + sparse XOR DP)

**Hypothesis tested:** At **n=7**, **coord + full `r=2` + three `r=3` XOR splits** might achieve **`min_d=2`** for **some** unordered triple of triple indices.

**Outcome:** **FAIL**

**Key finding:** Exhaustive **`C(35,3)=6545`** triples; **`witness_min_d2_count=0`**; wall **~18 s** with **4M** LRU. **No** depth-**2** certificate on this **3-triple** sparse menu — uniform **`min_d=3`**.

**Implications:**

- The **n=7** obstruction to **`min_d=2`** is **not** resolved by adding **one** more **`r=3`** parity beyond the **two-triple** menu.
- Further progress likely requires **more** triples, **higher**-arity XOR, or relaxing the “full **`r=2`**” side constraint.

**Analogy pass summary:** Monotone **query** **complexity** / **committee** **depth** — third **linear** **parity** **still** **insufficient** **to** **separate** **the** **shell** **at** **depth** **2**.

**Space-definition:** none
