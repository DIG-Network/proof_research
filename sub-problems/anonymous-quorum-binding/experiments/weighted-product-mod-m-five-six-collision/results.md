# Results: weighted product mod M (|S| = 5 vs 6, n = 10)

## Outcome: **PASS**

## Setup

Indices `0..9`, public weights `w_i = i+1` (values `1..10`).  
`h_M(S) = ∏_{i∈S}(i+1) mod M`.

## Findings

- **M = 2:** **6-subsets** **always** **include** **an** **even** **weight** **⇒** **h_2(S)=0** **for** **all** **|S|=6.** **5-subsets** **can** **be** **all-odd** **weights** **⇒** **h_2=1** **or** **include** **an** **even** **⇒** **h_2=0.** **Residue** **sets:** **5-sets** **{0,1},** **6-sets** **{0};** **intersection** **{0}.**
- **Smallest** **collision** **modulus:** **M = 2.** **Witness** **(lexicographic** **first** **hit** **in** **search):**  
  **F = (0,1,2,3,4)** **→** **∏ = 120 ≡ 0 (mod 2),**  
  **G = (0,1,2,3,4,5)** **→** **∏ = 720 ≡ 0 (mod 2).**

So **multiplicative** **modular** **compression** **fails** **at** **the** **same** **smallest** **modulus** **as** **the** **additive** **parity** **pitfall** **in** **034,** **but** **the** **mechanism** **is** **“even** **factor** **zeros** **the** **product”** **rather** **than** **linear** **parity** **of** **Σ** **w_i.**

## Interpretation

**∏ w_i (mod M)** **is** **not** **a** **threshold** **certificate** **for** **t=6** **on** **this** **weight** **vector** **—** **already** **at** **M=2** **with** **explicit** **5-** **vs** **6-set** **collision** **on** **residue** **0.**

## Reproducibility

```bash
python script.py
```
