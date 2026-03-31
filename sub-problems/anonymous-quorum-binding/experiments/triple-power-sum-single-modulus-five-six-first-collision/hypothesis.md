# Hypothesis — first M where (p₁,p₂,p₃) mod M collides across 5 vs 6 shells

## Analogy pass

1. **Abstract structure:** **064** **proved** **exact** **integer** **(p₁,p₂,p₃)** **is** **injective** **on** **C(10,5)∪C(10,6)** **for** **w_i=i+1** **—** **full** **moment** **vector** **separates** **shells.** **059–060** **used** **independent** **moduli** **per** **coordinate** **and** **saw** **immediate** **collisions** **at** **tiny** **(M₁,M₂,M₃).** **Missing** **link:** **uniform** **single** **modulus** **M** **applied** **to** **all** **three** **power** **sums** **—** **when** **does** **the** **first** **5-vs-6** **key** **collision** **appear** **as** **M** **grows** **from** **2?**

2. **Where else:**
   - **Quantization** **/ ** **rate-distortion:** **coarse** **bins** **merge** **distinguishable** **signals** **—** **smallest** **bin** **width** **with** **alias.**
   - **CRT** **/ ** **lattice** **reduction:** **simultaneous** **congruences** **mod** **one** **M** **vs** **factored** **moduli** **behave** **differently.**
   - **Numerical** **ODE** **stiffness:** **projecting** **a** **trajectory** **to** **low** **precision** **loses** **separation** **between** **nearby** **orbits.**

3. **Machinery:** **Exhaustive** **precompute** **(p₁,p₂,p₃)** **∈** **ℤ³** **for** **each** **5-** **and** **6-subset.** **Scan** **M=2,3,…** **until** **∃** **5-set** **A,** **6-set** **B** **with** **p_k(A)≡p_k(B)** **(mod** **M)** **for** **k=1,2,3** **simultaneously.** **Record** **minimal** **M** **and** **one** **witness.**

4. **Transfer candidate:** **If** **minimal** **M** **is** **small,** **any** **verifier** **using** **O(log M)** **bits** **per** **coordinate** **still** **risks** **shell** **merging** **—** **quantifies** **064** **vs** **059** **in** **the** **uniform-modulus** **regime.**

## Falsifiable claim

**Let** **M\*** **be** **the** **least** **integer** **≥2** **such** **that** **some** **5-subset** **and** **6-subset** **share** **(p₁ mod M\*,** **p₂ mod M\*,** **p₃ mod M\*).** **The** **experiment** **computes** **M\*** **and** **a** **witness** **(PASS** **when** **found** **within** **scan** **cap).**
