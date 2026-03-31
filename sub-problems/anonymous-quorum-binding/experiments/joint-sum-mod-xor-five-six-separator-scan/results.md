# Results — joint (Σw mod M, XOR w) separator scan

## Outcome: **PASS** (structural refutation)

- **Exact** **keys** **(integer** **Σ w_i,** **⨁ w_i):** **57** **values** **lie** **in** **both** **the** **|S|=5** **and** **|S|=6** **shells** **(n=10,** **w_i=i+1).**
- **Therefore** **T_M(S)=(Σw mod M,** **XOR w)** **cannot** **separate** **the** **two** **shells** **for** **any** **M** **≥** **2:** **matching** **integer** **sum** **⇒** **matching** **sum** **mod** **M** **and** **matching** **XOR.**
- **Empirical** **scan** **M=2..50000** **found** **no** **disjoint** **key** **sets** **—** **consistent** **with** **impossibility** **(not** **merely** **bounded** **search).**

## Witness (sample key (31, 5))

- **5-set** **(indices):** **(1,2,6,8,9)** **→** **weights** **(2,3,7,9,10),** **sum=31,** **xor=5.**
- **6-set** **(indices):** **e.g.** **(0,1,2,5,8,9)** **→** **weights** **(1,2,3,6,9,10),** **sum=31,** **xor=5** **(second** **6-set** **also** **listed** **in** **notes).**

## Script output (excerpt)

```
exact_(sum,xor)_collisions_between_shells=57
IMPOSSIBILITY: same (sum mod M, xor) for every M for those pairs
sample_key=(31, 5)
PASS
```
