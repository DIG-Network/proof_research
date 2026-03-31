# Results — linear-weights-integer-sum-five-six-collision

## Outcome: **PASS**

## Parameters

- **n = 10**, **w_i = i + 1** **(values** **1..10)**, **strict** **majority** **t = 6.**

## Witness (first hit in script enumeration order)

- **Common** **integer** **sum** **= 21.**
- **|S| = 5:** **indices** **(1, 2, 3, 4, 6)** **→** **weights** **2+3+4+5+7 = 21.**
- **|T| = 6:** **indices** **(0, 1, 2, 3, 4, 5)** **→** **weights** **1+2+3+4+5+6 = 21.**

## Conclusion

A **single** **integer** **additive** **summary** **Σ w_i** **(no** **modular** **reduction)** **still** **cannot** **distinguish** **sub-quorum** **(|S|=5)** **from** **quorum** **(|T|=6)** **for** **this** **public** **weight** **vector.** **Strengthens** **034** **(which** **used** **mod** **2);** **equality** **holds** **mod** **any** **M** **including** **large** **primes** **(e.g.** **97).**

## Repro

```bash
python script.py
```
