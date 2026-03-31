# Entry — 2026-03-30 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n7`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n7/`

**Context:** `verifier-oracle-model` (adaptive query / arity ladder beyond fixed `(10,{5,6})`)

**Hypothesis tested:** On **`n=7`**, shells **`|x|∈{3,4}`** (**70** masks, **`n=2t−1`** with **`t=4`**), compare **`min_d`** for **`coord + r`-sparse XOR** libraries (**`r=2,3,4`**) vs **coord-only** and **coord + full `n`-bit parity**; check whether **`r=4`** collapses depth like global parity.

**Outcome:** PASS (complete measurements; **H2** in `hypothesis.md` refuted)

**Key finding:** **Coord-only** **`min_d=7`**. **Coord + full 7-XOR** **`min_d=1`**. **Pair / triple / quad** libraries give **`min_d = 4 / 3 / 3`** respectively — **triple and quad tie**, unlike **`(10,{5,6})`** where **quad** strictly beat **triple** (**091**). **Union** of **pair+triple+quad** reaches **`min_d=2`**. So the **“each +1 arity drops `min_d` by 1”** ladder from the **10-variable** row is **not uniform** across **`(n, shells)`**.

**Implications:**

- **Verifier-oracle** budgeting should treat **`(n,t−1,t)`** as **first-class** when extrapolating from **066/091/093** certificates.
- **4-sparse XOR ≠ full `n`-parity** on **odd `n`**: **global parity** is **one** **degree-`n`** functional, **not** **reachable** as **a** **single** **4-sparse** **split** **on** **`n=7`**.

**Analogy pass summary:** Property testing / linear decision trees, coding syndromes, branch-and-bound over **70**-point domain — **extend** **049**/**093** **to** **smaller** **`n=2t−1`**.

**Invented space:** none.
