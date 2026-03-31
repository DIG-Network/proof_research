# Hypothesis — quintuple coprime moduli, **min M_i = 4** (lex-first collision)

## Analogy pass

1. **Abstract structure:** **060** raised **059**’s floor to **M_i≥4** and got lex-first triple **(4,5,7)**. **079** extended **059** to **five** moments with **min 2** → **(2,3,5,7,13)**. We raise **all** **M_i** to **≥4** and ask for the lex-first **5-vs-6** collision on **(p_k mod M_k)_{k=1..5}**.

2. **Analogues (≥3):** Same as **079** / **060** — **quantization grid** **coarsening** **with** **forbidden** **tiny** **moduli** **(2,3)**.

3. **Machinery:** Identical enumeration to **079** except **`--min-m 4`** and **`--scan-max`** large enough to witness a hit.

4. **Transfer seed:** Expect lex-first tuple **near** **(4,5,7,9,11)** **or** **(4,5,7,11,13)** **style** **—** **still** **small** **primes** **/ ** **coprimes,** **not** **a** **large** **safe** **region.**

## Falsifiable claims

- **H1:** Within **`[4, scan_max]`** **per** **coordinate,** **pairwise** **coprime,** **lex** **order,** **a** **collision** **exists** **for** **moderate** **`scan_max`** **(** **default** **25** **).**
- **H2:** **INCONCLUSIVE** **at** **default** **cap** **→** **increase** **`--scan-max`.**

Script: **PASS** **on** **first** **collision,** **exit** **1** **INCONCLUSIVE** **if** **none.**
