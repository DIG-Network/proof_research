# Results — nonadaptive-four-query-participation-indistinguishable

## Outcome: **PASS**

## Model

- **n = 10** **validators,** **participation** **vector** **v ∈ {0,1}¹⁰.**
- **Strict** **majority** **t = 6;** **sub-quorum** **witness** **uses** **Hamming** **weight** **5.**
- **Verifier** **may** **read** **v** **only** **on** **a** **fixed** **set** **Q** **with** **|Q| = 4** **(non-adaptive** **membership** **queries).**

## Statement verified

For **every** **one** **of** **C(10,4) = 210** **choices** **of** **Q,** **there** **exist** **a, b** **with** **wt(a) = 5,** **wt(b) = 6** **and** **a|_Q = b|_Q.**

## Construction (same for all Q)

- **a|_Q = b|_Q = 0** **on** **all** **queried** **coordinates.**
- **Let** **outside** **=** **{0,…,9} \ Q** **(six** **indices).**
- **a:** **ones** **on** **the** **first** **five** **outside** **indices** **(in** **increasing** **order),** **zeros** **elsewhere** **outside.**
- **b:** **ones** **on** **all** **six** **outside** **indices.**

Then **wt(a) = 5,** **wt(b) = 6,** **and** **the** **four** **queried** **bits** **agree** **(all** **zero).**

## Conclusion

**Information-theoretically,** **for** **each** **fixed** **Q** **with** **|Q| = 4,** **there** **is** **at** **least** **one** **shared** **pattern** **on** **Q** **(here** **all** **zeros)** **that** **extends** **both** **to** **wt = 5** **and** **to** **wt = 6.** **So** **a** **verifier** **that** **only** **sees** **v|_Q** **cannot** **know** **from** **that** **observation** **alone** **that** **the** **world** **must** **be** **above** **or** **below** **threshold** **—** **without** **extra** **π** **or** **more** **queries.** **(Not** **every** **of** **the** **16** **patterns** **on** **Q** **need** **be** **ambiguous;** **one** **ambiguous** **pattern** **per** **Q** **suffices** **for** **this** **template.)** **Aligns** **with** **pairing** **|π|** **with** **query** **budgets** **in** **the** **digest.**

## Repro

```bash
python script.py
```
