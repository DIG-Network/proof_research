# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/`

**Context:** `verifier-oracle-model` — adaptive decision trees, coord + **r**-sparse **F₂** XOR primitives, domain **n=12**, **wt ∈ {6,7}** (**1716** masks), majority **t=7**.

**Hypothesis (summary):** Extend **098–100** **`{5,6}`** sweeps to **`{6,7}`** at **n=12**; compare **`min_d(r)`** phenomenology to **099**/**100**.

**Outcome:** **PASS** (with **partial** standalone **`r=5`**, **`r=7`** due to **OOM** on this host).

**Key findings:**

- **Coord-only** **`min_d=12`**, **coord + full 12-XOR** **`min_d=1`**.
- **Standalone** **`min_d(r)`** **known** for **r ∈ {2,3,4,6,8,9,10,11}**; **r=5** and **r=7** **killed** (**792** splits each — memo **RSS** too large here). **r=6** and **r=11** yield **`min_d=2`**; **r=10** **gives** **3** — **non-monotone** **in** **r**.
- **Unions:** **`r∈{2,3,4}`** **`→3`**, **`r∈{2,3,4,5}`** **`→3`**, **`r∈{2,…,11}`** **`→2`** (**4082** splits total). **`{5,6}`** **and** **`{6,7}`** **unions** **each** **`min_d=2`** **without** **needing** **standalone** **r=5**/**7** **runs**.

**Implications:**

- **Full-menu** **union** **depth** **matches** **`n=11`** **`{5,6}`** **(** **`2`** **)** **on** **this** **slice** **.**
- **099-style** **`min_d(6),min_d(7)>min_d(5)`** **regression** **not** **replicated** **in** **the** **visible** **rows** **(** **`r=6`** **is** **already** **2** **)** **.**

**Analogy pass:** See **`hypothesis.md`** (scale **098–100** to **next** **majority** **pair** **;** **parity** **lemma** **for** **full** **n**-**XOR** **).

**Space-definition:** none.
