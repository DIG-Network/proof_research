# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quadruple-r3-scan-all-quadruples`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quadruple-r3-scan-all-quadruples`

**Problem context:** verifier-oracle-model (`{2,3}` shell, adaptive coordinate + sparse XOR DP)

**Hypothesis tested:** At **n=7**, **coord + full `r=2` + four `r=3` XOR splits** might achieve **`min_d=2`** for **some** unordered quadruple of triple indices.

**Outcome:** **FAIL**

**Key finding:** Exhaustive **`C(35,4)=52360`** quadruples; **`witness_min_d2_count=0`**; wall **~132 s** with **4M** LRU. **No** depth-**2** certificate on this **4-triple** sparse menu — still uniform **`min_d=3`**.

**Implications:**

- The **`n=7`** obstruction persists through **four** triple-XOR parities on the **full `r=2`** side; **not** resolved by the **triple-scan** generalization alone.
- Next finite slices are **much** larger (**`C(35,5)`**) or require **different** arity / partial unions (**`k`** of **`r=3`** **+** **`r=2`** only, etc.).

**Analogy pass summary:** **Parity-check / rank** view — **four** triple-linear measurements **still** **insufficient** for **depth-2** separation **vs** the **`n=7`** **shell**.

**Space-definition:** none
