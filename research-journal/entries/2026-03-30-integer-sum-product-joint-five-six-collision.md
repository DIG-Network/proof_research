# 2026-03-30 — integer-sum-product-joint-five-six-collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/integer-sum-product-joint-five-six-collision/`
- **Context:** anonymous-quorum-binding (toy **5** **vs** **6** **shell** **separation,** **w_i=i+1,** **n=10**).

## Hypothesis tested

**Some** **5-set** **and** **6-set** **share** **exact** **integer** **(Σ(i+1),** **Π(i+1)).**

## Outcome: **PASS**

**37** **collisions;** **sample** **(27,** **1680):** **5-set** **(1,5,6,7,8)** **vs** **6-set** **(1,2,3,4,7,10)** **(index** **lists** **in** **results).** **Implies** **(Σ mod M,** **Π mod M)** **fails** **for** **all** **M** **for** **those** **pairs.**

## Key finding

**Additive** **+** **multiplicative** **exact** **pair** **still** **does** **not** **separate** **shells** **on** **fixed** **1..10** **weights** **—** **orthogonal** **to** **062’s** **(sum,XOR)** **but** **same** **“exact** **cross-shell** **key”** **pattern.**

## Implications

- **Do** **not** **expect** **(Σ,Π)** **alone** **as** **a** **threshold** **certificate** **on** **this** **toy.**
- **Pivot** **to** **≥3** **independent** **integer** **statistics,** **dynamic** **weights,** **or** **other** **sub-problems.**

## Analogy pass summary

**Newton** **/ ** **Viete** **moments** **vs** **elementary** **symmetric** **functions** **—** **tested** **(first** **moment,** **top-degree** **product);** **finite** **n=10** **geometry** **still** **admits** **many** **cross-shell** **matches.**
