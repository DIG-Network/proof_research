# Entry 050 — weighted-product-mod-m-five-six-collision

**Date:** 2026-03-30  
**Context:** `sub-problems/anonymous-quorum-binding`  
**Experiment:** `experiments/weighted-product-mod-m-five-six-collision/`

## Hypothesis tested

For **public** **w_i=i+1** **on** **n=10,** **does** **h_M(S)=∏_{i∈S}(i+1)** **mod** **M** **separate** **|S|=5** **from** **|S|=6** **for** **small** **M?** **(Multiplicative** **analog** **of** **034.)**

## Outcome: **PASS**

## Key finding

**Smallest** **collision** **modulus** **is** **M=2:** **all** **6-sets** **have** **even** **product** **⇒** **h_2≡0;** **many** **5-sets** **also** **hit** **0** **(e.g.** **F=(0,1,2,3,4)** **→** **120).** **Explicit** **collision** **with** **G=(0,1,2,3,4,5)** **→** **720,** **both** **≡0** **(mod** **2).** **So** **product** **mod** **M** **is** **not** **a** **threshold** **witness** **here** **any** **more** **than** **additive** **parity** **summaries.**

## Implications

- **Digest** **thread** **on** **modular** **/ ** **symmetric** **summaries:** **add** **multiplicative** **mod** **fold** **—** **fails** **at** **M=2** **via** **even** **factor.**
- **Next:** **richer** **integer** **invariants** **(square-free** **core,** **CRT)** **or** **return** **to** **verifier-oracle** **taxonomy** **with** **049’s** **equivariance** **tags.**

## Analogy pass summary

**Likelihood** **/ ** **geometric-mean** **statistics;** **multiplicative** **congruences;** **HE** **toy** **—** **seed** **was** **“product** **might** **behave** **differently** **from** **sum”** **—** **outcome:** **still** **collapses** **at** **M=2.**
