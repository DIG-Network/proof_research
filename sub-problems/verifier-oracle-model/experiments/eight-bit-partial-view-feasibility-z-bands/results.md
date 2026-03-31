# Results: eight-bit-partial-view-feasibility-z-bands

## Outcome

**PASS**

## Inequalities

- **wt = 5:** **0 ≤ 5 − z ≤ 2** **⇔** **3 ≤ z ≤ 5**
- **wt = 6:** **0 ≤ 6 − z ≤ 2** **⇔** **4 ≤ z ≤ 6**

## By **z** (**|Q| = 8**)

| **z** | **wt=5** | **wt=6** | **Cell** | **# / Q** |
|------|----------|----------|----------|-----------|
| 0, 1, 2 | no | no | **neither** | 1+8+28 = **37** |
| 3 | yes | no | **only_wt5** | **56** |
| 4, 5 | yes | yes | **both** | 70+56 = **126** |
| 6 | no | yes | **only_wt6** | **28** |
| 7, 8 | no | no | **neither** | 8+1 = **9** |

**Per Q:** **neither** **46,** **only_wt5** **56,** **both** **126,** **only_wt6** **28** **(256** **total).**

## Totals (**45** choices of **Q**)

| Cell | Count |
|------|-------|
| **both** | **5670** |
| **only_wt5** | **2520** |
| **only_wt6** | **1260** |
| **neither** | **2070** |

## Interpretation

- **49.2%** **(126/256)** **of** **8**-**bit** **masks** **per** **Q** **still** **admit** **both** **wt=5** **and** **wt=6** **—** **first** **time** **below** **half** **in** **this** **(n,t)** **series.**
- **Neither** **region** **is** **18%** **of** **patterns** **per** **Q** **(46/256),** **up** **from** **9/128** **≈** **7%** **at** **k=7.**
