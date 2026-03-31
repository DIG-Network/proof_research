# Hypothesis: weighted product mod M — 5-set vs 6-set collision

## Analogy pass

1. **Abstract structure:** A verifier sees only a **scalar** **derived** **from** **a** **hidden** **subset** **S** **⊆** **[n]** **via** **a** **fixed** **public** **per-index** **map** **w_i** **and** **a** **fold** **(here** **multiplicative** **mod** **M).** **Threshold** **soundness** **would** **require** **the** **fold** **to** **separate** **|S|** **=** **t−1** **from** **|S|** **=** **t** **for** **committed** **static** **weights.**

2. **Where else does this structure appear?**
   - **Likelihood** **ratios** **/ ** **sufficient** **statistics** **for** **product** **families** **(e.g.** **geometric** **means** **as** **minimal** **sufficient** **statistics** **in** **i.i.d.** **product** **models).**
   - **Primality** **testing** **/ ** **order** **arguments:** **multiplicative** **congruences** **mod** **M** **forget** **prime** **factor** **multiplicity** **structure** **unless** **M** **is** **chosen** **with** **care.**
   - **Homomorphic** **encryption** **toys:** **multiplicative** **slots** **compress** **exponent** **patterns** **mod** **φ(N)** **—** **collisions** **are** **the** **norm** **at** **small** **moduli.**

3. **Machinery:** **Additive** **case** **(034–035)** **—** **mod** **2** **parity** **and** **integer** **subset-sum** **coincidences;** **pair-count** **/ ** **elementary** **symmetric** **mod** **M** **(046–047)** **—** **Pascal** **on** **subset** **counts,** **not** **ordered** **weights.**

4. **Transfer seed:** **If** **Σ** **w_i** **already** **collides** **in** **ℤ** **or** **mod** **small** **M,** **∏** **w_i** **might** **still** **separate** **—** **or** **might** **collapse** **faster** **because** **many** **small** **prime** **factors** **zero** **out** **mod** **M.** **Test** **computational** **collision** **existence** **for** **w_i=i+1,** **n=10,** **t=6.**

## Formal claim

Let **indices** **0..n−1** **with** **public** **weight** **w_i=i+1.** **For** **M** **≥** **2,** **define** **h_M(S)=∏_{i∈S}(i+1)** **mod** **M.**

**H1:** **There** **exists** **some** **M** **≤** **M_max** **and** **subsets** **F,G** **⊆** **[10]** **with** **|F|=5,** **|G|=6** **such** **that** **h_M(F)=h_M(G).** **(Such** **an** **M** **is** **a** **documented** **pitfall** **for** **“product-only”** **binding.)**

**H2** **(refined):** **M=2** **residues:** **every** **6-set** **has** **product** **≡0** **(mod** **2)** **since** **only** **five** **odd** **weights** **exist** **in** **1..10).** **Some** **5-sets** **(all** **odd** **weights)** **have** **product** **≡1,** **but** **any** **5-set** **containing** **an** **even** **weight** **hits** **0** **—** **so** **residue** **0** **collides** **across** **sizes** **(smallest** **M** **is** **2).**

The **script** **prints** **M=2** **residue** **sets** **and** **the** **smallest** **M** **with** **a** **witness** **(expected** **2).**
