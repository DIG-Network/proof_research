# 2026-03-31 — bitwise-and-or-weight-five-six-shell-collision

- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/bitwise-and-or-weight-five-six-shell-collision/`
- **Context:** anonymous-quorum-binding

## Hypothesis (short)

**Bitwise** **AND** **/** **OR** **of** **public** **weights** **w_i=i+1** **over** **S** **admits** **5-set** **vs** **6-set** **collisions** **(** **n=10** **).**

## Outcome: **PASS**

- **h_and:** **only** **3** **distinct** **values** **on** **|S|=5,** **1** **on** **|S|=6** **(** **all** **6-sets** **AND** **→** **0** **);** **value** **0** **shared** **across** **shells** **(** **e.g.** **weights** **1..5** **vs** **1..6** **).**
- **h_or:** **5** **/** **3** **distinct** **values,** **3** **cross-shell** **collisions** **(** **sample** **OR=7** **for** **{1..5}** **vs** **{1..6}** **).**

## Key finding

**Idempotent** **bit** **combines** **are** **too** **coarse** **for** **threshold** **shell** **separation** **here** **—** **parallel** **to** **additive** **mod-2** **(** **034** **)** **and** **XOR-of-indices** **(** **061** **)** **stories,** **different** **algebra.**

## Implications

- **Do** **not** **expect** **standalone** **`Link`** **from** **raw** **AND/OR** **of** **fixed** **public** **weights** **without** **extra** **structure.**
- **Joint** **tags** **mixing** **AND** **with** **linear** **stats** **would** **need** **a** **fresh** **hypothesis** **(** **062-style** **scan** **if** **pursued** **).**

## Analogy pass summary

**Multiset** **fingerprints;** **bitwise** **lattices;** **063** **multiplicative** **joint** **—** **seed:** **non-additive** **compression** **still** **merges** **5** **vs** **6** **shells.**
