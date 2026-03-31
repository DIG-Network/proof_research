# Outcome: **PASS**

## Setup

**n** **=** **10,** **public** **weights** **w_i** **=** **i+1** **(** **1..10** **).** **Shells** **|S|** **∈** **{5,6}.**

- **h_gcd(S)** **=** **gcd({w_i** **:** **i** **∈** **S}).**
- **J(S)** **=** **(h_gcd(S),** **Σ_{i∈S}** **w_i)** **(** **exact** **integers** **).**

## Counts

| Fingerprint | Distinct on \|S\|=5 | Distinct on \|S\|=6 | Cross-shell collisions |
|-------------|---------------------|---------------------|-------------------------|
| **h_gcd** | **2** | **1** | **1** **(value** **1** **only** **)** |
| **J** | 27 | 25 | **20** |

## Witnesses

- **h_gcd** **=** **1:** **5-set** **indices** **(0,1,2,3,4)** **(** **weights** **1..5** **),** **6-set** **(0..5)** **(** **1..6** **).** **Empirically** **every** **6-subset** **of** **{1,…,10}** **in** **this** **model** **has** **gcd** **1** **(** **only** **one** **distinct** **h_gcd** **on** **the** **210** **six-sets** **—** **e.g.** **omit** **weight** **1:** **gcd(2,3,4,5,6,7)=1** **).**
- **J** **=** **(1,** **21):** **same** **tuple** **as** **Entry** **088** **sample** **K_and** **(** **5-set** **(0,1,2,4,9),** **6-set** **(0..5)** **).**

## Interpretation

**h_gcd** **is** **even** **coarser** **than** **087** **h_and** **on** **the** **6-shell** **(** **one** **value** **vs** **one** **value** **for** **AND** **too** **—** **both** **collapse** **);** **here** **gcd** **is** **always** **1** **on** **every** **6-subset** **of** **{1,…,10}.** **Joint** **with** **Σw** **still** **has** **20** **cross-shell** **keys** **(** **088** **parallel** **).**

**Corollary:** **(gcd,** **Σw** **mod** **M)** **cannot** **separate** **those** **20** **witness** **pairs** **for** **any** **M.**

## Script

`python script.py` **→** **exit** **0,** **PASS.**
