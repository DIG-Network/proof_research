# Results: four-bit-partial-view-both-threshold-classes

## Outcome

**PASS**

## Setup

- **n = 10**, compare global Hamming weights **wt = 5** (strictly below **t = 6**) vs **wt = 6** (at threshold).
- Enumerate every **Q ⊆ {0,…,9}** with **|Q| ≤ 4** and every binary pattern **p** on **Q** (**2^|Q|** patterns).
- Let **z** = number of ones of **p** on **Q**, **R = n − |Q|** outside positions.
- **Feasibility:** extension to **wt = 5** iff **0 ≤ 5 − z ≤ R**; to **wt = 6** iff **0 ≤ 6 − z ≤ R**.

## Result

For all **4521** pairs **(Q, p)** checked, both feasibility conditions hold simultaneously.

## Reasoning

For **|Q| ≤ 4**, **R ≥ 6**. For **z ≤ 4**, we have **5 − z ∈ [1, 5]** and **6 − z ∈ [2, 6]**, hence both needs lie in **[0, R]** with **R ≥ 6**. So **every** **≤4**-bit partial view is compatible with **both** a global weight-5 and a global weight-6 vector.

## Implication (vs Entry 036)

**036** fixed **|Q| = 4** and exhibited **one** colliding pair per **Q** (zeros on **Q**). This experiment strengthens: **no** choice of **≤4** revealed bits (not only the all-zero mask) disambiguates **wt = 5** vs **wt = 6**. Therefore **adaptive** depth-4 **distinct-index** membership trees cannot **soundly** separate sub-quorum from quorum in this information-theoretic toy — the obstruction is **per leaf partial assignment**, not only non-adaptive **Q**.
