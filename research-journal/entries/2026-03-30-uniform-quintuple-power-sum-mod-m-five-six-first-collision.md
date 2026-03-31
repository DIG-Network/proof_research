# 2026-03-30 — uniform quintuple power sum mod M (5-set vs 6-set)

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quintuple-power-sum-mod-m-five-six-first-collision/`
- **Context:** anonymous-quorum-binding (follow-up to **075**: add **fifth** power, single uniform **M**).

## Hypothesis tested

**M\*** = least **M≥2** with a **5-vs-6** collision on **(S₁,…,S₅) mod M** for **w_i=i+1**, **n=10**. Structural expectation: **M\*** still **2** because **w^k ≡ w (mod 2)** for **k≥1**, so all five coordinates agree mod 2 with **S₁ mod 2**.

## Outcome: **PASS**

**M\*** **= 2**, **mod_key (1,1,1,1,1)**. Same witness pair as **075**: **5-set** **(5,7,8,9,10)** vs **6-set** **(1..6)**.

## Key finding

The fifth moment does not change the **first-collision modulus**; more strongly, **any** number of power sums **k≥1** are **algebraically redundant mod 2** for integer weights (**parity of odd-weight count** is the only bit).

## Implications

- Uniform-modulus power-sum vectors cannot gain “extra dimensions” at **M=2** by listing more **k**; separation requires **M** odd, **heterogeneous** moduli, or a different statistic.
- Stops the naive “add another moment” line under this exact toy unless the modulus pipeline changes.

## Analogy pass summary

**Quantization + dependent sensors:** extra coordinates that are deterministic functions of earlier ones in **ℤ/2ℤ** do not sharpen the grid.
