# Entry 052 — weighted-square-sum-mod-m-five-six-collision

**Date:** 2026-03-30  
**Context:** `sub-problems/anonymous-quorum-binding`  
**Experiment:** `experiments/weighted-square-sum-mod-m-five-six-collision/`

## Hypothesis tested

**Public** **v_i=(i+1)²;** **does** **h_M(S)=Σ v_i mod M** **separate** **|S|=5** **from** **|S|=6** **on** **n=10** **for** **small** **M?**

## Outcome: **PASS**

## Key finding

**Smallest** **collision** **M=2** **(residue** **1):** **F=(0..4)** **sum** **squares** **55,** **G=(0..5)** **91,** **both** **odd.** **Mod** **2** **both** **shells** **achieve** **residues** **0** **and** **1** **—** **unlike** **050’s** **product** **mod** **2** **where** **all** **6-sets** **were** **0** **—** **but** **threshold** **binding** **still** **fails** **at** **the** **same** **minimal** **modulus.**

## Implications

- **Extends** **034** **/ ** **050** **/ ** **047** **thread:** **low-order** **scalar** **summaries** **(linear,** **quadratic,** **product,** **elementary** **symmetric)** **each** **document** **their** **own** **collision** **geometry** **—** **none** **replace** **`Link`.**

## Analogy pass summary

**Moments** **/ ** **Newton** **identities;** **L2** **bag** **features** **—** **seed:** **quadratic** **might** **mix** **parity** **classes** **differently** **than** **linear;** **outcome:** **still** **M=2** **collision.**
