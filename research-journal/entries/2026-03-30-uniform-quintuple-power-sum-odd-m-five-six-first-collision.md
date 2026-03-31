# 2026-03-30 — quintuple power sums, first odd M collision (5 vs 6)

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quintuple-power-sum-odd-m-five-six-first-collision/`
- **Context:** anonymous-quorum-binding (**076** follow-up: remove **M=2** from scan).

## Hypothesis tested

**M_odd\*** = least **odd** **M≥3** with a **5-vs-6** collision on **(S₁,…,S₅) mod M** for **w_i=i+1**, **n=10**.

## Outcome: **PASS**

**M_odd\*** **= 3**, **mod_key (0,1,0,1,0)**. Witness **same** as **075/076**: **5-set** **(5,7,8,9,10)** vs **6-set** **(1..6)**.

## Key finding

The **first odd** modulus is already enough to merge the two shells on **five** power sums; no “buffer” beyond excluding **2**.

## Implications

- **Odd M** alone does **not** rescue uniform single-modulus moment tags at coarse scale.
- Per-moment **different** moduli or **exact** integer fingerprints (**064**-style) remain the contrasting axes.

## Analogy pass summary

**Band-limited aliasing** after removing the parity channel — next coarsest grid (**mod 3**) still aliases the same pair of subset types.
