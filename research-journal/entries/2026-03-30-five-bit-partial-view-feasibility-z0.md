# Entry — 2026-03-30 — five-bit-partial-view-feasibility-z0

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/five-bit-partial-view-feasibility-z0/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

For **n = 10**, **|Q| = 5**, **R = 5**, **wt = 6** extension exists iff **z ≥ 1** (ones on **Q**); **wt = 5** always exists for **z ∈ {0,…,5}**. Exhaustive over **8064** **(Q, p)**.

## Outcome

**PASS** — **7812** partial views admit **both** classes; **252** (**z = 0** only) admit **wt = 5** but **not** **wt = 6**; **0** **wt = 6**-only.

## Key finding

At **five** **coordinate** **probes**, **quorum** **(wt ≥ 6)** **is** **information-theoretically** **ruled** **out** **only** **when** **all** **five** **bits** **are** **0**. **All** **other** **5**-**bit** **views** **remain** **ambiguous** **between** **wt = 5** **and** **wt = 6** — **sharp** **transition** **from** **037** **(k ≤ 4)**.

## Implications

- **Lemma** **shape:** **t − z > n − |Q|** **⇔** **no** **quorum** **completion**; **first** **hits** **at** **|Q| = n − t + 1** **with** **minimal** **z**.
- **Adaptive** **depth** **5:** **only** **the** **all-zero** **5**-**tuple** **path** **separates**; **31/32** **pattern** **mass** **per** **Q** **still** **fails**.

## Analogy pass summary

**Knapsack** **capacity** **on** **remaining** **slots**; **partial** **MDP** **reachability**; **erasure** **+** **Hamming** **weight** **intervals** — **counting** **(t − z)** **vs** **R**.
