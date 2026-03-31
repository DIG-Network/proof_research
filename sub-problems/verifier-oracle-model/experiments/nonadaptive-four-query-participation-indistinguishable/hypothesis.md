# Hypothesis: four fixed membership queries do not separate |S|=5 vs 6

## Analogy pass

1. **Abstract structure**  
   Model **participation** **as** **v ∈ {0,1}ⁿ** **(indicator** **per** **validator).** **A** **restricted** **verifier** **may** **only** **read** **v** **on** **a** **fixed** **set** **Q** **of** **coordinates** **(non-adaptive** **membership** **oracle** **queries)** **before** **deciding** **whether** **Hamming(v) ≥ t.** **We** **ask** **whether** **|Q| = 4** **can** **ever** **be** **information-theoretically** **sufficient** **at** **n = 10,** **t = 6** **—** **i.e.** **whether** **two** **worlds** **(exactly** **five** **vs** **at** **least** **six** **ones)** **can** **agree** **on** **every** **coordinate** **in** **Q.**

2. **Where else this structure appears**  
   - **Property** **testing** **/ ** **decision** **trees:** **how** **many** **bit** **queries** **separate** **Hamming** **weight** **layers.**
   - **PAC** **learning** **lower** **bounds:** **fixed** **feature** **subset** **may** **not** **determine** **a** **global** **count.**
   - **Communication** **complexity:** **revelation** **of** **b** **bits** **of** **v** **leaves** **≥** **2^{n−b}** **extensions** **—** **many** **share** **the** **same** **prefix.**

3. **Machinery**  
   **Explicit** **construction** **of** **v⁽⁵⁾,** **v⁽⁶⁾** **with** **same** **restriction** **to** **Q** **and** **weights** **5** **and** **6;** **optional** **exhaust** **over** **all** **Q** **with** **|Q| = 4.**

4. **Transfer candidate**  
   **When** **n − |Q| ≥ 6,** **both** **patterns** **can** **realize** **all** **extra** **ones** **outside** **Q** **while** **matching** **zeros** **on** **Q** **—** **template** **for** **“query** **budget”** **obstructions** **alongside** **|π|** **bounds.**

## Falsifiable claim

**Claim:** **Let** **n = 10,** **t = 6.** **For** **every** **Q ⊂ {0,…,9}** **with** **|Q| = 4,** **there** **exist** **binary** **vectors** **a, b** **with** **wt(a) = 5,** **wt(b) = 6** **and** **a[i] = b[i]** **for** **all** **i ∈ Q** **(equivalently** **a|_Q = b|_Q).**

**PASS** ⇒ **no** **non-adaptive** **4-query** **membership** **strategy** **can** **distinguish** **sub-quorum** **from** **quorum** **in** **this** **idealized** **model** **without** **additional** **π** **—** **supports** **digest** **line** **on** **formalizing** **oracle** **/ ** **query** **budgets.**

**FAIL** ⇒ **some** **Q** **breaks** **the** **construction** **(would** **contradict** **the** **counting** **argument** **below** **if** **script** **is** **correct).**
