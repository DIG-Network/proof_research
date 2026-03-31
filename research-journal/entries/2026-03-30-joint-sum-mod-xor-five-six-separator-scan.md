# 2026-03-30 — joint-sum-mod-xor-five-six-separator-scan

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-mod-xor-five-six-separator-scan/`
- **Context:** anonymous-quorum-binding (toy **Link** / threshold shell separation, **w_i=i+1**, **n=10**, **|S|∈{5,6}**).

## Hypothesis tested

Smallest **M ≥ 2** such that **T_M(S) = (Σw mod M, ⨁w)** **has** **disjoint** **images** **on** **5-** **vs** **6-subsets** **—** **or** **structural** **obstruction.**

## Outcome: **PASS**

**57** **exact** **(integer** **sum,** **XOR)** **keys** **appear** **in** **both** **shells** **⇒** **no** **M** **can** **separate** **(same** **sum** **mod** **M** **and** **same** **XOR).** **Sample** **(31,5):** **5-set** **indices** **(1,2,6,8,9)** **vs** **6-set** **(0,1,2,5,8,9)** **(and** **another** **6-set).**

## Key finding

Joint **(Σ mod M, XOR)** **on** **public** **1..10** **weights** **is** **not** **a** **5/6** **separator** **—** **stronger** **than** **061** **+** **034** **alone:** **XOR** **does** **not** **disambiguate** **when** **paired** **with** **sum** **mod** **M** **here.

## Implications

- **Do** **not** **iterate** **modulus** **scans** **for** **this** **joint** **tag** **family** **on** **this** **toy.**
- **Next:** **richer** **public** **vectors,** **message-linked** **weights,** **or** **non-scalar** **certificates** **/ ** **other** **sub-problems.**

## Analogy pass summary

**Multi-sensor** **fusion** **/ ** **product** **codes** **—** **tested** **orthogonal** **combining** **(Z/MZ** **×** **GF(2)-style** **XOR);** **finite** **shell** **geometry** **still** **admits** **57** **exact** **collisions.**
