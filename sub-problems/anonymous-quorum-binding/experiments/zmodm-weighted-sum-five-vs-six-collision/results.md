# Results — zmodm-weighted-sum-five-vs-six-collision

## Outcome: **PASS**

## Parameters

- **n = 10**, **w_i = i + 1** **(integers** **1..10)**, **strict** **majority** **t = 6**.
- **Scan:** **M = 2, 3, …, 50**; **first** **hit** **reported.**

## Witness

- **M = 2**, **residue** **r = 1**.
- **|S| = 5:** **indices** **(4, 6, 7, 8, 9)** **→** **weights** **5+7+8+9+10 = 39 ≡ 1 (mod 2).**
- **|T| = 6:** **indices** **(0, 1, 2, 3, 4, 5)** **→** **weights** **1+2+3+4+5+6 = 21 ≡ 1 (mod 2).**

## Interpretation

**Mod-2** **reduction** **of** **the** **weighted** **sum** **is** **the** **parity** **of** **the** **integer** **sum** **—** **with** **these** **weights** **it** **collapses** **to** **a** **coarse** **invariant** **(here** **both** **sides** **odd),** **so** **a** **sub-quorum** **5**-**set** **and** **a** **quorum** **6**-**set** **can** **share** **the** **same** **one-word** **aggregate.** **Relates** **to** **verifier-oracle** **023** **(parity** **of** **participant** **count)** **but** **uses** **fixed** **linear** **weights** **rather** **than** **raw** **k** **alone.**

## Repro

```bash
python script.py
```
