# Hypothesis: |Q|=8, R=2 — z-bands for wt=5 vs wt=6 (n=10, t=6)

## Analogy pass

1. **Abstract structure.** **Shrinking** **R** **narrows** **the** **overlap** **of** **feasible** **z** **for** **adjacent** **targets** **t−1** **and** **t.** **Low** **z** **fails** **both** **(cannot** **reach** **t−1** **on** **outside);** **high** **z** **fails** **both** **(cannot** **reduce** **to** **t** **or** **t−1);** **middle** **splits** **into** **exclusive** **and** **shared** **bands.**

2. **Where else.** **Two** **thresholds** **on** **a** **sum** **with** **bounded** **slack** **—** **reliability** **engineering** **(spare** **capacity);** **bioassay** **dose** **response** **with** **detection** **limits.**

3. **Machinery.** **Same** **pair** **of** **inequalities** **as** **038–040,** **k=8.**

4. **Transfer seed.** **040** **at** **R=3** **gave** **neither** **on** **three** **z** **values** **at** **low/high** **ends** **plus** **91/128** **both.** **R=2** **should** **expand** **neither** **to** **z=2** **(max** **wt=4)** **and** **z=7,8,** **narrow** **“both”** **to** **z=4,5** **only.**

## Falsifiable claim

**n = 10**, **|Q| = 8**, **R = 2.**

- **wt=5** **iff** **3 ≤ z ≤ 5** **(need** **0..2** **ones** **outside).**
- **wt=6** **iff** **4 ≤ z ≤ 6.**

**Cells:** **z ∈ {0,1,2,7,8}** **neither;** **z=3** **only_wt5;** **z ∈ {4,5}** **both;** **z=6** **only_wt6.**

**Exhaustive** **C(10,8)·2^8 = 45·256 = 11520** **pairs.** **Per** **Q:** **neither** **46,** **only_wt5** **56,** **both** **126,** **only_wt6** **28.**

**Expected:** **PASS.**
