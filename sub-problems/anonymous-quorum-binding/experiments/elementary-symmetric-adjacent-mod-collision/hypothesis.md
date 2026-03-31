# Hypothesis: **C(t,d)−C(t−1,d)** **=** **C(t−1,d−1)** **(Pascal)** **⇒** **mod** **M** **collision** **iff** **M** **|** **C(t−1,d−1)**

## Analogy pass

1. **Abstract structure.** **Fixed-degree** **symmetric** **polynomial** **in** **n** **binary** **indicators** **collapses** **to** **a** **function** **of** **|S|** **only;** **comparing** **|S|=t−1** **vs** **t** **is** **one** **step** **in** **|S|** **along** **the** **Pascal** **triangle.**

2. **Where else.** **Finite** **differences** **of** **polynomials;** **discrete** **calculus** **on** **binomial** **coefficients;** **coding** **—** **weight** **enumerators** **and** **MacWilliams** **style** **identities** **(distant** **cousin).**

3. **Machinery.** **C(t,d)=C(t−1,d)+C(t−1,d−1)** **⇒** **difference** **is** **C(t−1,d−1).** **Modular** **collision** **for** **the** **statistic** **C(|S|,d)** **across** **sizes** **t−1** **and** **t** **iff** **that** **difference** **≡0** **(mod** **M).**

4. **Transfer seed.** **046** **is** **d=2** **only;** **this** **experiment** **unifies** **all** **degrees** **d** **≥** **1** **in** **one** **identity** **and** **regresses** **numerically.**

## Falsifiable claim

**For** **all** **tested** **t,d** **with** **t≥d≥1:** **math.comb(t,d)−math.comb(t−1,d)** **equals** **math.comb(t−1,d−1).** **Entry** **046** **(t=6,d=2)** **is** **a** **subcase.**

**Expected:** **PASS.**
