# Hypothesis: **C(|S|,2) mod M** **can** **agree** **for** **|S|=t−1** **vs** **|S|=t**

## Analogy pass

1. **Abstract structure.** **A** **scalar** **summary** **of** **a** **subset** **S** **is** **published** **mod** **M** **to** **save** **bits;** **threshold** **soundness** **needs** **different** **residues** **for** **|S|=t−1** **and** **|S|=t.**

2. **Where else.** **Hash** **truncation** **(mod** **2^k);** **Bloom** **filter** **collisions;** **moments** **mod** **p** **in** **streaming** **sketches.**

3. **Machinery.** **Second** **elementary** **symmetric** **polynomial** **on** **binary** **indicator** **equals** **C(|S|,2)** **—** **depends** **only** **on** **|S|** **for** **unweighted** **pairs.** **Adjacent** **sizes** **differ** **by** **C(t,2)−C(t−1,2)=t−1.**

4. **Transfer seed.** **034** **modular** **linear** **Σ** **w_i;** **035** **integer** **linear** **collision;** **here** **pure** **pair** **count** **with** **closed** **modulus** **condition** **M** **|** **(t−1).**

## Falsifiable claim

**For** **t=6,** **M=5:** **C(5,2)=10** **and** **C(6,2)=15** **are** **congruent** **mod** **5** **(both** **0).** **In** **general** **C(t,2)≡C(t−1,2)** **(mod** **M)** **iff** **M** **divides** **t−1** **(for** **t≥2).**

**Expected:** **PASS** **(algebra** **+** **script** **checks).**
