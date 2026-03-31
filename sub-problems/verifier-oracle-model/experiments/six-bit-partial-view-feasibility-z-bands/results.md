# Results: six-bit-partial-view-feasibility-z-bands

## Outcome

**PASS**

## Setup

- **n = 10**, **|Q| = 6**, **R = 4**, targets **wt = 5** and **wt = 6**.
- **z** = number of ones of **p** on **Q** (**0 … 6**).
- **wt = 5** iff **0 ≤ 5 − z ≤ R** iff **1 ≤ z ≤ 5**.
- **wt = 6** iff **0 ≤ 6 − z ≤ R** iff **2 ≤ z ≤ 6**.

## Classification by **z**

| **z** | **wt=5** | **wt=6** | **Cell** |
|------|----------|----------|----------|
| 0 | no | no | **neither** |
| 1 | yes | no | **only_wt5** |
| 2–5 | yes | yes | **both** |
| 6 | no | yes | **only_wt6** |

## Exhaustive counts (**210** choices of **Q**, **64** patterns each)

| Cell | Count | Per **Q** (patterns) |
|------|-------|----------------------|
| **both** | **11760** | **56** |
| **only_wt5** | **1260** | **6** |
| **only_wt6** | **210** | **1** |
| **neither** | **210** | **1** |

**Total:** **13440**.

## Interpretation

- **87.5%** **(56/64)** **of** **6**-**bit** **masks** **per** **Q** **still** **admit** **both** **wt=5** **and** **wt=6** **—** **down** **from** **96.875%** **(31/32)** **at** **|Q|=5** **but** **still** **dominant.**
- **All-zero** **on** **Q** **(z=0):** **max** **global** **wt** **=** **R** **=** **4** **<** **5** **—** **no** **completion** **to** **either** **threshold** **class** **(for** **this** **pair** **5** **vs** **6).**
- **All-one** **on** **Q** **(z=6):** **only** **wt=6** **(zeros** **outside);** **cannot** **complete** **to** **wt=5.**
