# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-square-weights-extended-n-scan

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-square-weights-extended-n-scan`

**Context:** anonymous-quorum-binding (toy shell-separation / aggregate-tag track)

**Hypothesis tested:** For **`w_i=(i+1)^2`**, exact **`K=(min,max,Σ,Π)`** has **no** 5-vs-6 cross-shell collision for **`11 ≤ n ≤ 35`**.

**Outcome:** **FAIL** (hypothesis **falsified**)

**Key finding:** **First** collision at **`n=31`** with **`K=(1,961,1927,3113640000)`**. **5-set** indices **`(0,3,17,24,30)`** (weights **`1,16,324,625,961`**) vs **6-set** **`(0,1,4,5,29,30)`** (weights **`1,4,25,36,900,961`**). **No** collision for **`n=11..30`**. **098**’s **square** branch had only **`n≤18`** — **onset** is **between** **19** and **31**, **here** pinned to **31**.

**Implications:**

- **Square** weights **delay** **097**-style **failure** (**`31` vs `11`**) but **do not** **prevent** it **in** **this** **statistic**.
- **Schedule-dependent** **claims** should **report** **minimal** **`n`** **with** **collision**, **not** **only** **bounded** **negative** **scans**.

**Analogy pass summary:** See **`hypothesis.md`** — **parameter** **shift** **moves** **onset** **without** **guaranteeing** **robustness**.

**Space definition:** none
