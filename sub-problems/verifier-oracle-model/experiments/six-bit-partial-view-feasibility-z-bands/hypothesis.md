# Hypothesis: |Q|=6, R=4 — feasibility bands for wt=5 vs wt=6 (n=10, t=6)

## Analogy pass

1. **Abstract structure.** With **R = n − |Q|** free bits, achievable global weights are **z + w** for **w ∈ [0, R]**. The **fiber** of a partial observation **(Q, p)** intersects **wt = t−1** iff **t−1 − z ∈ [0, R]**, and **wt = t** iff **t − z ∈ [0, R]**. As **R** **shrinks**, **integer** **bands** **for** **z** **partition** **patterns** **into** **four** **cells:** **both**, **sub-only**, **quorum-only**, **neither**.

2. **Where else.**
   - **Interval arithmetic / ILP** feasibility after fixing some decision variables.
   - **Erasure channels:** given **known** **symbols**, **which** **total** **Hamming** **weights** **remain** **reachable** **on** **the** **unobserved** **block**.
   - **Stopping rules** in **sequential** **testing:** **sample** **size** **too** **small** **to** **cross** **either** **threshold**.

3. **Machinery.** Solve **linear** **inequalities** **in** **one** **integer** **(w_out)** **per** **target** **weight.**

4. **Transfer seed.** **038** **at** **R=5** **gave** **z=0** **→** **no** **wt=6** **(still** **wt=5** **possible)** **and** **z≥1** **→** **both.** **At** **R=4,** **expect** **richer** **partition:** **z=0** **should** **exclude** **both** **(need** **≥5** **outside** **for** **wt=5),** **z=1** **only** **wt=5,** **z=2..5** **both,** **z=6** **only** **wt=6.**

## Falsifiable claim

Let **n = 10**, **|Q| = 6**, **R = 4**, **t_sub = 5**, **t = 6**, **z** = ones of **p** on **Q**.

- **wt=5** feasible iff **1 ≤ z ≤ 5** (equivalently **0 ≤ 5−z ≤ 4**).
- **wt=6** feasible iff **2 ≤ z ≤ 6** (**0 ≤ 6−z ≤ 4**).

**Exhaustive** over **C(10,6)·2^6 = 210·64 = 13440** **(Q, p)** **pairs** **—** **verify** **counts:** **neither** **210** **(z=0),** **only** **wt=5** **1260** **(z=1),** **both** **11760** **(z=2..5),** **only** **wt=6** **210** **(z=6).**

**Expected outcome:** **PASS.**

## Interpretation

Six **coordinate** **probes** **yield** **87.5%** **(56/64)** **per-Q** **ambiguous** **leaves** **for** **5** **vs** **6** **—** **up** **from** **31/32** **at** **|Q|=5** **but** **still** **most** **mass** **on** **“both.”** **New** **phenomenon:** **z=0** **→** **neither** **class** **(global** **wt** **≤4** **on** **Q** **zeros** **—** **actually** **max** **wt** **=** **z+R** **=** **4** **<** **5** **and** **<** **6).** **z=6** **→** **only** **quorum** **completion** **(all** **ones** **on** **Q,** **wt=6** **with** **zeros** **outside).**
