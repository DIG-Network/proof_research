# Hypothesis: same integer linear weight-sum for |S|=5 vs |S|=6

## Analogy pass

1. **Abstract structure**  
   **034** **showed** **Σ w_i (mod M)** **can** **agree** **for** **a** **5**-**subset** **and** **a** **6**-**subset** **already** **at** **M=2** **(parity).** **A** **natural** **strengthening** **asks** **whether** **the** **unreduced** **integer** **sum** **Σ w_i** **—** **the** **value** **a** **verifier** **would** **see** **if** **π** **is** **exactly** **one** **ℤ** **scalar** **—** **can** **also** **coincide** **across** **cardinalities** **5** **vs** **6** **for** **fixed** **public** **weights.**

2. **Where else this structure appears**  
   - **Partition** **/ ** **subset-sum** **coincidences:** **equal** **subset** **sums** **with** **different** **subset** **sizes** **(e.g.** **coin** **weighing** **puzzles).**  
   - **Knapsack** **density:** **many** **small** **integers** **admit** **multiple** **representations** **of** **the** **same** **total** **mass.**  
   - **Anonymous** **aggregation** **(e.g.** **ring** **signatures** **toys):** **sum** **of** **committed** **tags** **may** **hide** **which** **subset** **fired** **if** **sums** **collide.**

3. **Machinery**  
   **Exhaust** **C(10,5)** **and** **C(10,6)** **integer** **sums** **for** **w_i = i+1;** **intersect** **sum** **values** **or** **sort** **and** **match.**

4. **Transfer candidate**  
   **Concrete** **collision** **witness** **on** **n=10,** **weights** **1..10** **—** **shows** **even** **“no** **modulus”** **single** **additive** **fingerprint** **does** **not** **encode** **quorum** **vs** **sub-quorum** **in** **this** **model.**

## Falsifiable claim

**Claim:** With **w_i = i+1** **for** **i ∈ {0,…,9}**, **there** **exist** **a** **5**-**subset** **S** **and** **a** **6**-**subset** **T** **such** **that** **Σ_{i∈S} w_i = Σ_{j∈T} w_j** **as** **integers** **(hence** **mod** **every** **M).**

**PASS** ⇒ **one** **ℤ** **aggregate** **is** **insufficient** **for** **threshold** **certification** **here** **—** **strictly** **stronger** **than** **034’s** **mod-2** **example.**

**FAIL** ⇒ **no** **such** **pair** **(contradicts** **standard** **subset-sum** **search;** **would** **indicate** **implementation** **error).**
