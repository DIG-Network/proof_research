# Results: five-bit-partial-view-feasibility-z0

## Outcome

**PASS**

## Setup

- **n = 10**, **|Q| = 5**, **R = 5** outside coordinates.
- **z** = Hamming weight of the observed pattern **p** restricted to **Q**.
- **wt = 5** extension: **0 ≤ 5 − z ≤ R**.
- **wt = 6** extension: **0 ≤ 6 − z ≤ R**.

## Counts (exhaustive)

| Cell | Count | Meaning |
|------|-------|---------|
| Both **wt=5** and **wt=6** | **7812** | **31** patterns per **Q** (**z ≥ 1**) |
| **wt=5** only (no **wt=6**) | **252** | **z = 0** only (all zeros on **Q**) |
| **wt=6** only | **0** | — |
| Neither | **0** | — |

**Total:** **C(10,5) × 2^5 = 8064**.

## Reasoning

**wt=6** needs **6 − z** ones outside; with **R = 5** this holds iff **z ≥ 1**. **wt=5** needs **5 − z** outside; for **z ∈ {0,…,5}** this always lies in **[0, 5]**.

## Implication

Five **distinct** **membership** **queries** **can** **rule** **out** **quorum** **(wt ≥ 6)** **only** **when** **the** **five** **observed** **bits** **are** **all** **zero** — **still** **7812/8064 ≈ 96.9%** **of** **partial** **views** **remain** **ambiguous** **between** **wt = 5** **and** **wt = 6**.
