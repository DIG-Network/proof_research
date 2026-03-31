# Hypothesis: mod-M weighted subset sum collides across 5-set vs 6-set

## Analogy pass

1. **Abstract structure**  
   Each validator **i** has a **public** **scalar** **weight** **w_i** **(committed** **in** **C** **in** **a** **full** **scheme).** **A** **compact** **attestation** **might** **publish** **only** **Σ_{i∈S} w_i (mod M)** **—** **a** **single** **group** **/ ** **ring** **element** **—** **hoping** **this** **separates** **sub-quorum** **(|S|=5)** **from** **quorum** **(|S|=6)** **at** **n=10,** **t=6.** **We** **test** **whether** **such** **a** **summary** **can** **agree** **for** **some** **5**-**subset** **and** **some** **6**-**subset.**

2. **Where else this structure appears**  
   - **Subset-sum** **/ ** **knapsack:** **many** **distinct** **subsets** **map** **to** **the** **same** **sum** **mod** **M** **when** **M** **is** **small** **or** **weights** **align.**  
   - **Homomorphic** **fingerprints** **(CRT,** **Paillier** **toys):** **linear** **aggregates** **mod** **a** **composite** **often** **lose** **injective** **labeling** **of** **which** **indices** **fired.**  
   - **Universal** **hashing:** **random** **linear** **forms** **are** **collision-resistant** **per** **query** **but** **fixed** **public** **weights** **give** **structured** **collisions.**

3. **Machinery**  
   **Exhaust** **C(10,5)** **and** **C(10,6)** **sums** **mod** **M;** **intersect** **residue** **sets** **or** **scan** **small** **M** **/ ** **weight** **choices.**

4. **Transfer candidate**  
   **Concrete** **integer** **weights** **w_i = i+1** **(deterministic** **public** **labels)** **and** **small** **modulus** **M** **chosen** **so** **a** **cross-cardinality** **collision** **is** **guaranteed** **or** **quickly** **found** **by** **brute** **force.**

## Falsifiable claim

**Claim:** For **n = 10** **validators** **indexed** **0..9** **with** **w_i = i+1**, **there** **exists** **a** **modulus** **M** **with** **2 ≤ M ≤ 50** **such** **that** **some** **5**-**subset** **S** **and** **some** **6**-**subset** **T** **satisfy** **Σ_{i∈S} w_i ≡ Σ_{j∈T} w_j (mod M).** **(Exclude** **M=1** **as** **degenerate.)**

**PASS** ⇒ **one-number** **modular** **linear** **aggregate** **of** **fixed** **public** **weights** **does** **not** **by** **itself** **certify** **|S| ≥ 6** **vs** **|S| = 5** **in** **this** **toy** **—** **parallel** **to** **023** **(parity** **of** **count)** **but** **with** **nontrivial** **weights.**

**FAIL** ⇒ **no** **such** **M** **in** **1..50** **for** **this** **weight** **vector** **(unexpected)** **—** **would** **widen** **M** **or** **change** **weights.**
