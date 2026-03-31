# Hypothesis: two Lagrange evals can inject on **{0,1}^n** when **2^n < p²**

## Analogy pass

1. **Abstract structure.** **Map** **n** **binary** **leaf** **values** **through** **a** **degree** **<n** **polynomial** **to** **k** **field** **samples.** **Injectivity** **on** **the** **hypercube** **requires** **enough** **output** **entropy** **(image** **size** **≥** **2^n)** **and** **no** **accidental** **algebraic** **collisions** **—** **capacity** **vs** **structure.**

2. **Where else.** **Compressed** **sensing** **needs** **RIP** **/ ** **incoherence**, **not** **just** **m** **≥** **k;** **hash** **surjectivity** **vs** **random** **oracle;** **code** **minimum** **distance** **vs** **alphabet** **size.**

3. **Machinery.** **024** **uses** **2^n** **>** **p²** **⇒** **forced** **collision** **(pigeonhole).** **Here** **flip** **regime:** **2^n** **<** **p²** **⇒** **injective** **labeling** **into** **F_p²** **exists** **as** **set** **map;** **question** **is** **whether** **the** **specific** **Lagrange** **family** **hits** **such** **a** **pair** **(r1,r2).**

4. **Transfer seed.** **Exhaustive** **search** **over** **(r1,r2)** **∈** **F_97** **\** **nodes** **for** **n=10** **finds** **at** **least** **one** **injective** **pair** **—** **bounding** **024** **as** **large-n** **phenomenon** **relative** **to** **p.**

## Falsifiable claim

For **n=10,** **p=97,** **nodes** **0..9,** **some** **distinct** **r1,r2** **∉** **nodes** **yield** **pairwise** **distinct** **(P_v(r1),P_v(r2))** **for** **all** **v** **∈** **{0,1}^10.** **Exhaustive** **search** **reports** **first** **witness** **and** **count** **of** **injective** **pairs.** **Expected:** **PASS.**
