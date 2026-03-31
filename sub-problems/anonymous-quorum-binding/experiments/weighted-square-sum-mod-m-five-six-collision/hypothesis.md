# Hypothesis: quadratic power-sum mod M — 5-set vs 6-set collision

## Analogy pass

1. **Abstract structure:** The verifier sees **one** **number** **per** **anonymous** **subset** **S** **—** **here** **the** **second** **power** **sum** **Σ (i+1)²** **reduced** **mod** **M** **—** **and** **asks** **whether** **such** **a** **summary** **can** **encode** **|S|** **≥** **t** **vs** **|S|** **=** **t−1** **without** **`Link`.**

2. **Where else does this structure appear?**
   - **Method** **of** **moments** **/ ** **cumulants:** **low-order** **power** **sums** **of** **observations** **as** **compressed** **data** **about** **a** **sample** **—** **different** **sample** **sizes** **can** **match** **low** **moments.**
   - **Newton** **identities:** **link** **power** **sums** **to** **elementary** **symmetric** **polynomials** **—** **our** **047** **thread** **already** **showed** **modular** **elementary** **symmetric** **pitfalls** **across** **adjacent** **sizes.**
   - **L2** **feature** **aggregation** **in** **ML** **(sum** **of** **squared** **features** **per** **bag)** **—** **bags** **of** **different** **cardinality** **can** **share** **scalar** **summaries** **after** **quantization** **/ ** **hashing.**

3. **Machinery:** **Newton** **/ ** **symmetric** **function** **algebra;** **modular** **arithmetic** **collapsing** **injective** **integer** **statistics.**

4. **Transfer seed:** **Linear** **weights** **w_i=i+1** **already** **collapse** **mod** **2** **and** **in** **ℤ** **(034–035).** **Quadratic** **w_i=(i+1)²** **raises** **degree** **but** **still** **lives** **in** **a** **one-dimensional** **image** **mod** **M** **—** **expect** **early** **collisions** **for** **some** **small** **M** **(possibly** **larger** **than** **2).**

## Formal claim

**Indices** **0..9,** **public** **v_i=(i+1)².** **h_M(S)=Σ_{i∈S} v_i mod M.**

**H1:** **There** **exists** **M** **≥** **2** **and** **|F|=5,** **|G|=6** **with** **h_M(F)=h_M(G).** **Record** **the** **smallest** **such** **M** **and** **a** **witness.**

**H2** **(optional** **contrast):** **Unlike** **050** **(product** **mod** **2),** **quadratic** **sums** **mod** **2** **may** **not** **collapse** **all** **6-sets** **to** **one** **residue** **—** **enumerate** **residue** **sets** **for** **M=2** **for** **context.**

The **script** **brute-forces** **smallest** **M** **with** **a** **collision.**
