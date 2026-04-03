# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-weight-five-six-minimal-n11-scan

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-five-six-minimal-n11-scan`

**Context:** anonymous-quorum-binding (toy shell-separation / aggregate-tag track)

**Hypothesis tested:** For `w_i=i+1` and exact `K=(min,max,Σ,Π)` on shells `|S|∈{5,6}`, is the **minimal** `n>10` admitting a **5-vs-6** cross-shell collision equal to **`n=11`** (rather than first appearing only at `n=12` as suggested by **096**)?

**Outcome:** **PASS** (hypothesis **confirmed** — minimal `n` is **11**)

**Key finding:** At **`n=11`**, `cross_shell_exact=1`. Shared key **`(1,11,31,2640)`** with **5-set** weights **`{1,5,6,8,11}`** (indices `0,4,5,7,10`) vs **6-set** **`{1,2,3,4,10,11}`** (`0,1,2,3,9,10`). Each shell has **462** distinct internal **`K`** values (full cardinality), but the two key sets intersect in **one** element. Together with **093** (`n=10`, no cross-shell collision), the **first** `n>10` where this quadruple fails to separate **`5`** vs **`6`** shells is **`11`**, not **`12`**.

**Implications:**

- **096**’s closed-form family at `n=12` is an **additional** collision mechanism, not the **minimal** threshold for this statistic and weight schedule.
- Any claim that separation “first breaks at twelve validators” for this toy is **false**; it breaks at **eleven**.

**Analogy pass summary:** Minimal counterexample / phase-transition scan: locate smallest ambient `n` where two graded layers collide under a fixed low-dimensional statistic.

**Space definition:** none
