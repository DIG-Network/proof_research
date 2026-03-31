# Results: min-max-sum-triple-weight-five-six-shell-collision

**Outcome:** **PASS**

## Setup

- **n=10**, **indices** **0..9**, **w_i = i+1** **(** **1..10** **)**.
- **Shells:** **|S|=5** **(** **252** **subsets** **),** **|S|=6** **(** **210** **subsets** **)**.
- **K(S) = (min_{i∈S} w_i, max_{i∈S} w_i, Σ_{i∈S} w_i)** **∈** **ℤ³** **(exact).**
- **K_M(S) = (min, max, Σw mod M)** **for** **M ≥ 2.**

## Counts

| Map | Distinct keys on \|S\|=5 | Distinct keys on \|S\|=6 | Cross-shell intersection |
|-----|--------------------------|---------------------------|--------------------------|
| **K** | 126 | 95 | **41** |

**Lexicographically** **smallest** **exact** **collision** **key:** **(1, 7, 22)**

- **5-set** **indices** **(0, 2, 4, 5, 6)** **→** **weights** **1,3,5,6,7**
- **6-set** **indices** **(0, 1, 2, 3, 4, 6)** **→** **weights** **1,2,3,4,5,7**

## Mod scan

- **Smallest** **M** **with** **a** **5-vs-6** **collision** **for** **K_M:** **M = 2**
- **Cross-shell** **keys** **for** **K_2:** **25**
- **Sample** **K_2** **collision:** **(1, 6, 1)** **mod** **2** **on** **sum** **—** **5-set** **(0,1,2,4,5)** **vs** **6-set** **(0,1,2,3,4,5)**

## Interpretation

**Order** **statistics** **plus** **total** **mass** **do** **not** **separate** **the** **5** **and** **6** **shells** **on** **this** **fixed** **weight** **vector** **;** **folding** **Σ** **mod** **2** **already** **merges** **shells** **(** **same** **spirit** **as** **034** **/** **065** **)** **even** **with** **(min,max)** **fixed** **exactly.**
