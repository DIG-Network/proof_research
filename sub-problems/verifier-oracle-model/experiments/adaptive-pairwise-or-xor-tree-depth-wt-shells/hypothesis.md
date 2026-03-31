# Hypothesis: pairwise OR / XOR decision trees vs AND (048) and coordinates (045)

## Analogy pass

1. **Abstract structure:** Same as **048:** adaptive binary decision trees must **purely** separate two Hamming-weight shells `|x| ∈ {T−1, T}` on `{0,1}^n`, but each internal node may only branch on a **pair predicate** chosen from a small menu (**AND**, **OR**, **XOR**).

2. **Where else does this structure appear?**
   - **Boolean circuit bases:** `{∧,∨,⊕}` on **literals** **span** **different** **function** **algebras;** **canonical** **DNF/CNF** **vs** **parity** **(Fourier)** **representations** **stress** **different** **gates.**
   - **Fault trees / reliability:** **OR** **nodes** **fire** **if** **any** **child** **path** **is** **active** **—** **structurally** **a** **union** **of** **minterms** **vs** **AND** **intersection.**
   - **Phylogenetic / pooled tests:** **“any** **positive** **in** **this** **pair?”** **(OR)** **vs** **“both** **positive?”** **(AND)** **vs** **“odd** **count?”** **(XOR)** **are** **different** **symptoms** **of** **the** **same** **hidden** **bit** **vector.**

3. **Machinery there:** **Circuit** **lower** **bounds** **reason** **about** **gate** **mix;** **reliability** **block** **diagrams** **compose** **OR/AND;** **group** **testing** **with** **OR** **pools** **detects** **any** **defective** **in** **a** **bucket.**

4. **Transfer seed:** **048** **showed** **pairwise** **AND** **can** **cost** **depth** **>** **n** **(5,3)** **or** **=** **n** **(6,4).** **De** **Morgan:** **x_i ∨ x_j = ¬(¬x_i ∧ ¬x_j)** **—** **OR** **on** **x** **is** **AND** **on** **complemented** **bits,** **but** **our** **domain** **is** **not** **closed** **under** **complement** **(weights** **flip** **n−|x|),** **so** **OR** **behavior** **on** **fixed** **wt** **shells** **is** **not** **isomorphic** **to** **AND** **on** **the** **same** **shell** **union.** **XOR** **is** **linear** **over** **F₂** **(a** **2-bit** **parity** **pool);** **may** **track** **closer** **to** **coordinate** **/ ** **linear** **probe** **limits** **(021).**

## Formal hypotheses (outcomes)

**H1:** **OR** **tracks** **AND** **on** **(5,3).** **Result:** **yes** **(both** **min** **depth** **6** **>** **n).**

**H2:** **OR** **on** **(6,4)** **matches** **AND** **depth** **6.** **Result:** **no** **—** **OR** **min** **depth** **is** **9** **(strictly** **worse** **than** **AND’s** **6).**

**H3:** **XOR** **always** **admits** **a** **finite** **perfect** **tree** **on** **these** **shell** **pairs.** **Result:** **no** **—** **when** **n** **=** **2T** **−** **1,** **complement** **invariance** **makes** **XOR-only** **trees** **impossible** **(proof** **in** **`results.md`).**

**H4:** **When** **XOR** **is** **possible,** **min** **depth** **can** **be** **≪** **n.** **Result:** **yes** **for** **(6,4):** **min** **depth** **3.**

The script implements the **impossibility** **shortcut** **for** **XOR** **when** **n=2t−1** **and** **otherwise** **exhaustive** **min-depth** **search.**
