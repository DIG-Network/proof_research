# 2026-03-30 — adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model` — **091** **breakthrough** **asked** **whether** **all** **5**-**sparse** **F₂** **parities** **(** **+** **coords** **)** **yield** **`min_d=2`** **or** **stay** **at** **3** **(** **quad-only** **)** **;** **exclude** **092** **total** **parity.**

**Hypothesis tested:** **Exhaustive** **`exists_tree`** **for** **coord** **+** **252** **pentuple** **XORs** **only.**

**Outcome:** **PASS** **`min_d=2`** **(** **d=1** **false** **,** **d=2** **true** **~0.005** **s** **).**

**Key finding:** **5**-**sparse-only** **beats** **4**-**sparse-only** **on** **depth** **(** **2** **vs** **3** **)** **despite** **incomparable** **primitive** **lists** **(** **no** **quad** **nodes** **in** **093** **).**

**Implications:**
- **Answers** **091** **BREAKTHROUGHS** **first** **open** **question** **:** **`min_d=2`**, **not** **3.**
- **On** **(10,{5,6}),** ** arity** **R=5** **without** **full** **parity** **is** **sharper** **than** **R=4** **for** **this** **adaptive** **separator.**

**Analogy pass summary:** **weight-5** **syndrome** **rows** **/** **k**-**junta** **tests** **—** **seed:** **C(10,5)** **partitions.**
