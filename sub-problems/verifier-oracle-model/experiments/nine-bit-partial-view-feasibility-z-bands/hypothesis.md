# Hypothesis: |Q|=9, R=1 — z-bands for wt=5 vs wt=6 (n=10, t=6)

## Analogy pass

1. **Abstract structure.** When **R = 1**, **each** **target** **weight** **allows** **at** **most** **two** **values** **of** **z** **(need** **0** **or** **1** **outside** **one).** **The** **intersection** **for** **t−1** **and** **t** **can** **shrink** **to** **a** **single** **z** **(here** **z = t−1** **when** **t−1** **and** **t** **both** **need** **≤1** **outside** **one).**

2. **Where else.** **Quantization** **with** **one** **bit** **of** **slack;** **digital** **comparator** **with** **1** **LSB** **uncertainty** **spanning** **two** **thresholds.**

3. **Machinery.** **Same** **feasibility** **inequalities;** **R=1** **forces** **narrow** **bands.**

4. **Transfer seed.** **041** **had** **“both”** **on** **z=4,5.** **With** **R=1,** **wt=5** **⇔** **z∈{4,5},** **wt=6** **⇔** **z∈{5,6},** **so** **“both”** **only** **at** **z=5** **(single** **Hamming** **layer).**

## Falsifiable claim

**n = 10**, **|Q| = 9**, **R = 1.**

- **wt=5** **iff** **z ∈ {4,5}**
- **wt=6** **iff** **z ∈ {5,6}**

**Cells:** **z ∈ {0,1,2,3,7,8,9}** **neither;** **z=4** **only_wt5;** **z=5** **both;** **z=6** **only_wt6.**

**Per** **Q:** **neither** **176,** **only_wt5** **126,** **both** **126,** **only_wt6** **84** **(512** **patterns).**

**Total** **C(10,9)·512 = 5120** **pairs.** **Expected** **PASS.**
