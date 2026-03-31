# Hypothesis: |Q|=7, R=3 — z-bands for wt=5 vs wt=6 (n=10, t=6)

## Analogy pass

1. **Abstract structure.** As **R = n − |Q|** **shrinks**, the **integer** **intervals** **for** **outside** **ones** **that** **realize** **wt = t−1** **or** **wt = t** **slide** **along** **z.** **Endpoints** **z = 0** **and** **z = |Q|** **can** **fall** **outside** **both** **intervals** **(neither),** **or** **land** **in** **exactly** **one** **(exclusive** **cells).**

2. **Where else.** **Feasible** **region** **for** **linear** **Diophantine** **inequalities** **with** **one** **slack** **variable;** **truncated** **binomial** **support** **in** **group** **testing** **with** **bounded** **pool** **capacity.**

3. **Machinery.** **Inequalities** **0 ≤ t−1−z ≤ R** **and** **0 ≤ t−z ≤ R** **clipped** **to** **z ∈ [0, |Q|].**

4. **Transfer seed.** **039** **at** **R=4** **gave** **four** **cells** **with** **neither** **only** **at** **z=0** **and** **z=6** **impossible** **for** **|Q|=6.** **At** **R=3,** **expect** **wider** **neither** **(z=0,1** **too** **few** **ones** **on** **Q** **to** **reach** **5** **with** **only** **3** **outside;** **z=7** **too** **many** **on** **Q** **for** **wt=5** **or** **6),** **only_wt5** **at** **z=2,** **both** **z=3,4,5,** **only_wt6** **at** **z=6.**

## Falsifiable claim

**n = 10**, **|Q| = 7**, **R = 3**. **wt=5** **iff** **2 ≤ z ≤ 5**; **wt=6** **iff** **3 ≤ z ≤ 6**. **Cell** **by** **z:**

| **z** | **Cell** |
|------|----------|
| 0, 1, 7 | **neither** |
| 2 | **only_wt5** |
| 3, 4, 5 | **both** |
| 6 | **only_wt6** |

**Exhaustive** **C(10,7)·2^7 = 120·128 = 15360** **pairs.** **Expected** **totals:** **neither** **1080,** **only_wt5** **2520,** **both** **10920,** **only_wt6** **840.**

## Expected outcome

**PASS.**
