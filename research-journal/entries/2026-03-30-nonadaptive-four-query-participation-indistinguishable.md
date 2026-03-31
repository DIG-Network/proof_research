# 2026-03-30 — nonadaptive-four-query-participation-indistinguishable

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/nonadaptive-four-query-participation-indistinguishable/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** **For** **n=10,** **t=6,** **every** **Q** **with** **|Q|=4** **admits** **binary** **a,** **b** **with** **wt(a)=5,** **wt(b)=6** **and** **a|_Q=b|_Q.**

**Outcome:** **PASS**

**Key finding:** **Uniform** **construction:** **zeros** **on** **Q,** **then** **5** **vs** **6** **ones** **on** **the** **six** **outside** **coordinates** **—** **checked** **all** **C(10,4)=210** **choices** **of** **Q.** **Non-adaptive** **four** **membership** **queries** **cannot** **separate** **sub-quorum** **from** **quorum** **in** **this** **idealized** **model** **without** **additional** **data.**

**Implications:**

- **Supports** **formalizing** **verifier** **oracle** **/ ** **query** **budget** **next** **to** **|π|** **and** **Merkle** **hash** **counts** **(**019**).**
- **Complements** **021** **(**F₂** **pools)** **and** **023** **(**parity**)** **as** **a** **clean** **bit-probe** **template.**

**Analogy pass summary:** **Property** **testing,** **decision** **trees,** **partial** **revelation** **of** **hidden** **vectors** **—** **seed:** **outside** **size** **≥** **t** **with** **queries** **all** **zero.**
