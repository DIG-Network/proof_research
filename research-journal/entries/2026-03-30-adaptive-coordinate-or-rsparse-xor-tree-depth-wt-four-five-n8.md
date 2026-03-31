# Entry — 2026-03-30 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n8`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n8/`

**Context:** `verifier-oracle-model` (arity ladder / `min_d(r)` beyond **095**)

**Hypothesis tested:** On **`n=8`**, **`|x|∈{4,5}`**, measure **`min_d`** for **coord + `r`-sparse XOR** only (**`r=2..5`**), full **`n`**-parity, and unions; expect monotonicity or plateaus as on **`(7,{3,4})`** / **`(10,{5,6})`**.

**Outcome:** PASS (DP complete; **H2** refuted)

**Key finding:** **`min_d(r)`** is **not** monotone: **`r=4`** **alone** gives **`min_d=2`**, while **`r∈{2,3,5}`** **each** give **`min_d=4`**. So **5-sparse-only** is **worse** than **4-sparse-only** — opposite monotonicity to **091→093** on the **462**-set. **Union** **`r∈{2,3,4}`** or **`2..5`** still **`min_d=2`**. Logged as **BREAKTHROUGHS** **constraint** **096**.

**Implications:**

- **Single-arity** **F₂** **gate** **libraries** **need** **per-** **`(n,`** **shells** **)** **tables** **;** **do** **not** **extrapolate** **from** **`(10,{5,6})`** **alone** **.
- **Next** **:** **sweep** **`min_d(r)`** **landscape** **for** **other** **small** **`(n,`** **`t−1`** **vs** **`t)`** **.**

**Analogy pass summary:** **095** **/ ** **066–093** **row** **;** **coding** **syndrome** **refinements** **;** **even** **`n`** **,** **`n≠2t−1`** **geometry** **.**

**Invented space:** none.
