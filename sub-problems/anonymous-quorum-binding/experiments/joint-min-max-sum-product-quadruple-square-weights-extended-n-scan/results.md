# Results — joint-min-max-sum-product-quadruple-square-weights-extended-n-scan

**Outcome:** **FAIL** (hypothesis **falsified**)

**Hypothesis (recap):** For **`w_i=(i+1)^2`**, exact **`K=(min,max,Σ,Π)`** has **no** 5-vs-6 cross-shell collision for **`11 ≤ n ≤ 35`**.

**Observation:** **First** collision occurs at **`n=31`**.

**Witness**

- **`K = (1, 961, 1927, 3113640000)`**
- **5-set (indices 0-based):** `(0, 3, 17, 24, 30)` → weights **`[1, 16, 324, 625, 961]`**
- **6-set:** `(0, 1, 4, 5, 29, 30)` → weights **`[1, 4, 25, 36, 900, 961]`**

**Scan band:** **`n = 11 .. 30`** — no collision; **`n = 31`** — collision (script stops).

**Runtime (single run, cold):** on the order of **a few seconds** total for the full **`n=11..31`** sweep (combinatorial counts grow with **`C(n,5)+C(n,6)`**).

**Implication:** The **square** schedule **does** eventually admit the same failure mode as **linear** weights; **098**’s “no collision through **`n=18`**” is **not** evidence of a large **`n`** barrier — only a **delayed** onset (**`n=31`** here vs **`n=11`** for **`i+1`**).
