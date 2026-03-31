# 2026-03-30 — quintuple coprime moduli, min M_i = 4 (5 vs 6)

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-min4-five-six-collision/`
- **Context:** anonymous-quorum-binding (**060**-style **floor** **on** **079**).

## Hypothesis tested

Lex-first **pairwise-coprime** **(M₁,…,M₅)** with **M_i≥4**, **M_i≤25**, **first** **5-vs-6** **collision** **on** **modular** **quintuple** **moments.**

## Outcome: **PASS**

**(** **4,5,7,9,17** **),** **key** **(0,4,1,8,10).** **Witness** **5-set** **(2,3,6,8,9)** **vs** **6-set** **(1,3,4,5,7,8)** **—** **both** **have** **p₁=28.**

## Key finding

**Banning** **M_i∈{2,3}** **does** **not** **prevent** **early** **aliasing:** **first** **collision** **still** **uses** **small** **moduli** **(** **≤17** **).** **Equal** **integer** **sum** **across** **shells** **(** **035** **)** **feeds** **p₁ mod M₁** **collisions** **while** **higher** **moments** **can** **still** **match** **mod** **coprime** **M₂…M₅.**

## Implications

- **Moment-only** **tags** **without** **shell** **/ ** **cardinality** **must** **confront** **integer** **relations** **like** **Σw** **agreement** **across** **|S|=5** **vs** **6.**
- **078** **injectivity** **of** **full** **ℤ⁵** **penta** **is** **consistent** **with** **this** **—** **projection** **loses** **that** **separation.**

## Analogy pass summary

**060** **/** **079** **combined** **—** **raised** **quantization** **floor,** **still** **mixed-radix** **aliasing.**
