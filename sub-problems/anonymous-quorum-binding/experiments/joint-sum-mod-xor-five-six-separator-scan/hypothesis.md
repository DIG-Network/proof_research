# Hypothesis — joint (Σw mod M, XOR w) separates 5-shell from 6-shell for some M

## Analogy pass

1. **Abstract structure:** **061** showed **XOR** **alone** **collides** **5 vs 6** **(same** **witness** **as** **057).** **034–060** showed **Σw mod M** **alone** **collides** **for** **small** **M.** **Joint** **tags** **can** **shrink** **collision** **fiber** **when** **coordinates** **are** **algebraically** **independent** **enough** **on** **the** **finite** **family** **C(10,5)∪C(10,6).**

2. **Where else:**
   - **Multi-sensor** **fusion:** **combining** **orthogonal** **measurements** **reduces** **ghost** **matches**.
   - **Product** **codes:** **separate** **constraints** **in** **different** **rings** **(Z/MZ** **×** **GF(2)^k**-**style)** **lift** **to** **fewer** **false** **positives**.
   - **Biometrics:** **score** **vectors** **beat** **single** **scalar** **thresholds** **for** **equal-error** **tradeoffs**.

3. **Machinery:** **T_M(S) = (Σ_{i∈S} w_i mod M, ⨁_{i∈S} w_i)** with **w_i=i+1**. **Search** **smallest** **M ≥ 2** **such** **that** **no** **5-set** **and** **6-set** **share** **the** **same** **T_M** **(key** **sets** **disjoint** **across** **shells).**

4. **Transfer candidate:** If **some** **moderate** **M** **separates**, **noncommutative** **+** **modular** **linear** **might** **be** **a** **toy** **separator** **without** **SNARKs** **(still** **not** **a** **full** **Link(C,K)** **solution).** If **no** **M** **up** **to** **cap**, **bounded** **INCONCLUSIVE** **/ ** **negative** **evidence** **for** **this** **pair** **in** **range**.

## Falsifiable claim

For **n=10**, **w_i=i+1**, find **smallest** **M ∈ [2, scan_max]** **with** **{T_M(S): |S|=5} ∩ {T_M(S): |S|=6} = ∅**. **Report** **M** **or** **INCONCLUSIVE** **if** **none**.
