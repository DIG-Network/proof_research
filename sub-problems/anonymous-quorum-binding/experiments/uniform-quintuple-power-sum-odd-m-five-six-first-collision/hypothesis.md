# Hypothesis — quintuple power sums, smallest **odd** M (5 vs 6)

## Analogy pass

1. **Abstract structure:** After **076**, uniform **M=2** makes all power sums **k≥1** agree mod 2 with **Σw**. We change the **measurement ring** to **odd** moduli only to ask: what is the **coarsest odd** scale at which two shells still collide on **(S₁,…,S₅)**?

2. **Analogues (≥3):**
   - **Band-pass filtering:** Dropping the DC / parity channel and asking when the next harmonic aliases two signals.
   - **CRT / lifting:** Working mod **2** vs mod **odd** factors as independent “frequency” components of **ℤ**.
   - **Experimental design:** Removing a confounded binary factor to see the next-smallest effect size.

3. **Machinery:** Restrict **M** to **2ℕ+1** so **ℤ/Mℤ** has odd characteristic; **w^k** no longer collapses to **w** mod **M** by parity alone.

4. **Transfer seed:** **M=3** is the smallest odd modulus; **059** showed triples hit **(2,3,5)**-style coprime tuples quickly — odd **M** may still be **3** or **5** for five tuples.

## Falsifiable claims

Let **w_i=i+1**, **n=10**, **S_k(S)=Σ_{i∈S} w_i^k**, **k=1..5**.

**M_odd\*** = minimum **odd** **M≥3** such that some **5-set** and **6-set** share **(S₁,…,S₅) mod M**.

- **H1:** **M_odd\*** is small (**3** or **5**), i.e. odd moduli still collapse shells almost immediately.
- **H2:** **M_odd\*** is noticeably larger than **3** (would suggest more “room” before aliasing once **2** is excluded).

Exhaustive scan over odd **M** up to **`--scan-max`** (default **50001** so we include odd values up to 50001).
