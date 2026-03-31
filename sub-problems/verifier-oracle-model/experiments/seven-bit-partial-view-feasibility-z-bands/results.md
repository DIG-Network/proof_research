# Results: seven-bit-partial-view-feasibility-z-bands

## Outcome

**PASS**

## Inequalities

- **wt = 5:** **0 ≤ 5 − z ≤ 3** **⇔** **2 ≤ z ≤ 5**
- **wt = 6:** **0 ≤ 6 − z ≤ 3** **⇔** **3 ≤ z ≤ 6**

## Classification by **z** (on **|Q| = 7**)

| **z** | **wt=5** | **wt=6** | **Cell** | **#patterns / Q** |
|------|----------|----------|----------|-------------------|
| 0, 1 | no | no | **neither** | 1 + 7 = **8** |
| 2 | yes | no | **only_wt5** | **21** |
| 3, 4, 5 | yes | yes | **both** | 35 + 35 + 21 = **91** |
| 6 | no | yes | **only_wt6** | **7** |
| 7 | no | no | **neither** | **1** |

**Per Q:** **9** **neither,** **21** **only_wt5,** **91** **both,** **7** **only_wt6** **(sums** **to** **128).**

## Totals (**120** choices of **Q**)

| Cell | Count |
|------|-------|
| **both** | **10920** |
| **only_wt5** | **2520** |
| **only_wt6** | **840** |
| **neither** | **1080** |

## Interpretation

- **71.1%** **(91/128)** **of** **7**-**bit** **masks** **per** **Q** **still** **admit** **both** **wt=5** **and** **wt=6** **—** **down** **from** **87.5%** **at** **|Q|=6.**
- **Neither** **class** **gains** **mass:** **z=1** **(only** **one** **on** **Q)** **cannot** **reach** **wt≥5** **with** **3** **outside** **slots** **(max** **4);** **z=7** **cannot** **place** **wt=5** **or** **6** **(already** **over** **or** **inconsistent** **with** **outside** **capacity** **for** **5).**
