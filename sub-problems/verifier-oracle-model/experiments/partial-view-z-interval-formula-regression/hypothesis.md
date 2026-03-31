# Hypothesis: closed-form cell counts for partial-view threshold feasibility

## Analogy pass

1. **Abstract structure.** **Fix** **a** **k**-**coordinate** **probe** **of** **an** **n**-**bit** **string.** **Feasibility** **of** **global** **Hamming** **weight** **w** **depends** **only** **on** **z** **=** **ones** **on** **the** **probe** **and** **R** **=** **n** **−** **k** **slack** **outside** **—** **a** **one**-**dimensional** **integer** **interval** **per** **target** **w.**

2. **Where else.** **Discrete** **tomography** **(projections** **determine** **feasible** **fiber);** **balls** **in** **Hamming** **metric** **as** **intervals** **in** **z** **when** **coordinates** **split** **into** **two** **blocks;** **generating** **functions** **(coefficient** **of** **x^w** **in** **(1+x)^R** **after** **fixing** **z** **ones** **on** **Q).**

3. **Machinery.** **Inequality** **0** **≤** **w** **−** **z** **≤** **R** **⇔** **z** **∈** **[max(0,w−R),** **min(k,w)].** **Sum** **binom(k,z)** **over** **z** **in** **set**-**theoretic** **cells** **for** **pair** **(w_sub,** **w_q)** **=** **(t−1,** **t).**

4. **Transfer seed.** **Entries** **038–042** **computed** **bands** **by** **hand;** **this** **experiment** **packages** **the** **same** **rule** **as** **code** **and** **checks** **Σ_z** **binom(k,z)** **×** **C(n,k)** **against** **full** **enumeration.**

## Falsifiable claim

For **all** **tested** **(n,** **k,** **t)** **(including** **n=10,** **t=6,** **k=4..9** **and** **spot** **cases),** **global** **counts** **from** **the** **z**-**interval** **formula** **equal** **brute** **enumeration** **over** **every** **Q** **and** **every** **2^k** **pattern.**

**Expected:** **PASS.**
