# Results: polynomial-two-eval-small-n-injective-witness

## Outcome

**PASS**

## Setup

- **n = 10,** **p = 97,** **Lagrange** **nodes** **0,…,9.**
- **2^n = 1024** **<** **p² = 9409** **(image** **has** **room** **for** **all** **binary** **patterns).**

## Findings

| Quantity | Value |
|----------|-------|
| **First** **injective** **(r1,r2)** **(lex** **on** **combinations)** | **(10,** **26)** |
| **Injective** **pairs** **among** **C(87,2)** **=** **3741** **valid** **(r1,r2)** | **95** |
| **(90,** **91)** **(024-style):** **collision** **on** **hypercube** | **yes** **(witness** **vectors** **Hamming** **distance** **8)** |

## Interpretation

- **024** **does** **not** **rule** **out** **two-point** **Lagrange** **fingerprints** **for** **small** **n** **at** **fixed** **p;** **it** **only** **exhibits** **collision** **once** **2^n** **exceeds** **p²** **(and** **then** **some** **pairs** **still** **collide** **earlier** **by** **structure).**
- **Binding** **via** **two** **published** **evaluations** **still** **fails** **the** **main** **problem** **at** **large** **n** **without** **scaling** **p** **or** **adding** **more** **samples** **/ ** **structure** **—** **same** **thread** **as** **022/024/031.**
