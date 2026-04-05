# Journal entry — 2026-04-05 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), after exhaustive closure of the **`r=3`-only ladder** through **`C(35,7)`** septuples (all `min_d=3` on **coord + full `r=2` + seven `r=3`**).

**Hypothesis tested (pre-registered):** **No** single **`r=4`** XOR split added to **full `r=2` + full `r=3`** keeps the menu at **`min_d≥3`** — i.e. **singleton `r=4` augments** would **not** reach **`min_d=2`**.

**Outcome:** **FAIL** for that hypothesis — **all `35/35`** quartic choices give **`min_d=2`** (`witness_min_d2_count=35`, `min_d_ge3_count=0`), **`57`** splits total each run, **`wall_sec≈0.053`**, **`lru_cap=4_000_000`**.

**Key finding:** **One** **`r=4`** XOR parity is **universally** sufficient for **`min_d=2`** **once** the **full** **`r=3`** XOR menu is present (together with full **`r=2`**). This is **strictly sparser** than the **`91`**-split **`union r∈{2,3,4}`** certificate and **contrasts sharply** with the **`r=3`-only** extension ladder (**seven** extra triples still **`min_d=3`**).

**Implications:**

- **`r=4`** is a **sharp** **arity** **transition** for **`min_d`** at this slice: **quartic** **parity** **unlocks** **depth** **`2`** **immediately** **after** **full** **triple** **coverage**, whereas **more** **triples** **alone** **do** **not**.
- Reconciles with **`union {2,3}`** vs **`{2,4}`** **`56`**-split **`min_d=3`** facts: **full `r=3`** **menu** **is** **load-bearing** **for** **enabling** **singleton** **`r=4`** **to** **collapse** **depth**.

**Analogy pass summary:** See `hypothesis.md` — matroid-rank / single-measurement pivot (hypothesis direction was wrong empirically).
