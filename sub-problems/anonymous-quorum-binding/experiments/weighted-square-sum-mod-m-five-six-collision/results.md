# Results: Σ(i+1)² mod M — |S| = 5 vs 6 (n = 10)

## Outcome: **PASS**

## Setup

**v_i = (i+1)²** **for** **i ∈ {0,…,9}.** **h_M(S) = Σ_{i∈S} v_i mod M.**

## Findings

- **M = 2:** **Residue** **sets** **for** **5-sets** **and** **6-sets** **are** **both** **{0,1}** **—** **unlike** **the** **product** **mod** **2** **pattern** **in** **050** **(where** **all** **6-sets** **were** **0),** **quadratic** **parity** **does** **not** **pin** **|S|=6** **to** **a** **single** **class.** **Nevertheless** **intersection** **is** **full,** **so** **5-** **vs** **6-set** **collisions** **exist** **mod** **2.**

- **Smallest** **collision** **modulus:** **M = 2,** **residue** **1.** **Witness** **(lex-first** **in** **search):**  
  **F = (0,1,2,3,4)** **→** **Σv = 1+4+9+16+25 = 55 ≡ 1 (mod 2),**  
  **G = (0,1,2,3,4,5)** **→** **+ 36 → 91 ≡ 1 (mod 2).**

## Interpretation

**Even** **degree-two** **power** **sums** **mod** **small** **M** **do** **not** **repair** **threshold** **binding:** **already** **at** **M=2** **a** **5-set** **and** **a** **6-set** **share** **the** **same** **compressed** **value.** **Compared** **to** **050,** **the** **M=2** **“geometry”** **of** **residues** **differs** **(both** **sizes** **realize** **both** **bits),** **but** **the** **minimal** **collision** **modulus** **is** **still** **2.**

## Reproducibility

```bash
python script.py
```
