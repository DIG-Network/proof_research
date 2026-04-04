# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-only-vs-r2-r4-only-min-d`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-only-vs-r2-r4-only-min-d`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), after **`{2,3,4}`** union **`min_d=2`** (**`91`** splits) and exhaustive **sparse** **`r=3`** ladder through **`C(35,6)`** (**all** **`min_d=3`**).

**Hypothesis tested:** **Primary:** **coord + union `r∈{2,3}`** only has **`min_d ≥ 3`** (**full `r=4`** **needed** **vs** **dropping** **it** **from** **`{2,3,4}`** **)** **. **Secondary:** record **`min_d`** for **`r∈{2,4}`** only.

**Outcome:** **PASS** **(** **primary** **)** **—** **`min_d=3`** **for** **`{2,3}`** **only** **(** **`dp_sec≈0.0036`** **)** **.**

**Key finding:** **Also** **`min_d=3`** **for** **`{2,4}`** **only** **(** **`dp_sec≈0.0024`** **)** **.** **So** **both** **full** **`r=3`** **and** **full** **`r=4`** **menus** **are** **necessary** **for** **`min_d=2`** **in** **this** **union** **family** **at** **this** **slice** **:** **neither** **arity** **alone** **(** **with** **`r=2`** **)** **suffices** **,** **even** **though** **each** **pair** **menu** **has** **the** **same** **`56`** **splits** **as** **the** **other** **.**

**Implications:**

- **Refines** **`…-n7-union-r2-r3-r4-min-d`:** **`r=4`** **is** **not** **merely** **“** **helpful** **”** **—** **omitting** **it** **kills** **`min_d=2`** **on** **the** **full-menu** **union** **pattern** **.**

- **Surprising** **symmetry** **:** **`r=2+r=4`** **does** **not** **substitute** **for** **`r=3`** **(** **still** **`min_d=3`** **)** **;** **the** **`91`**-split **`{2,3,4}`** **witness** **uses** **genuine** **multi-arity** **overlap** **.**

**Analogy pass summary:** See `hypothesis.md` — ablation / generating-set view on parity menus.
