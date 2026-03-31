# 2026-03-30 — quintuple mod coprime (M₁,…,M₅), lex-first 5 vs 6 collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-five-six-collision/`
- **Context:** anonymous-quorum-binding (**059** extended to **five** moments / **five** moduli).

## Hypothesis tested

Lex-first **pairwise-coprime** **(M₁,…,M₅)** with **M_i≥2**, **M_i≤18** yields a **5-vs-6** collision on **(p_k mod M_k)_{k=1..5}**.

## Outcome: **PASS**

**First** **hit** **(2,3,5,7,13),** **key** **(1,1,4,4,5).** **Witness:** **5-set** **(1,2,3,7,10)** **vs** **6-set** **(1,2,3,5,6,8).**

**Note:** **(2,3,5,7,11)** **is** **coprime** **and** **lex** **earlier** **but** **is** **not** **the** **first** **collision** **—** **no** **shell** **merge** **at** **M₅=11** **in** **this** **enumeration.**

## Key finding

**059**-style **coprime** **per-coordinate** **folding** **still** **collides** **at** **small** **moduli** **(** **largest** **13** **here** **).** **Fifth** **coordinate** **can** **postpone** **relative** **to** **(2,3,5,7,11)** **but** **does** **not** **produce** **a** **large** **safe** **tuple.**

## Implications

- **Heterogeneous** **moduli** **help** **somewhat** **vs** **uniform** **M=2** **(** **078** **exact** **still** **finest** **).** **Compact** **threshold** **certificate** **remains** **elusive** **in** **this** **family.**

## Analogy pass summary

**Mixed-radix** **CRT** **toy** **—** **same** **as** **059** **thread,** **dimension** **five.**
