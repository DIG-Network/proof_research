# Entry — 2026-03-30 — partial-view-z-interval-formula-regression

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/partial-view-z-interval-formula-regression/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

**z**-**interval** **feasibility** **for** **global** **wt** **w** **yields** **per**-**Q** **cell** **weights** **Σ** **binom(k,z);** **global** **counts** **=** **C(n,k)** **times** **those** **weights;** **matches** **brute** **for** **(10,6,k)** **k=4..9** **and** **spot** **triples.**

## Outcome

**PASS**

## Key finding

**The** **entire** **037–042** **enumeration** **series** **is** **encoded** **by** **interval** **intersection** **on** **z** **plus** **binomial** **weights** **—** **no** **new** **cryptographic** **content,** **but** **a** **durable** **reference** **implementation.**

## Implications

- **Digest** **/** **future** **hypotheses** **can** **point** **here** **for** **(n,t,k)** **cell** **sizes** **without** **re**-**running** **exhaustive** **loops.**
- **Next** **natural** **step** **outside** **this** **toy:** **adaptive** **query** **trees** **or** **binding** **threads** **in** **`anonymous-quorum-binding`.**

## Analogy pass summary

**Discrete** **tomography** **/** **binomial** **slice** **of** **Hamming** **ball** **—** **interval** **in** **z** **only.**
