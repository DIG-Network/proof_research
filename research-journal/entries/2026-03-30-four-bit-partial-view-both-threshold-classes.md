# Entry — 2026-03-30 — four-bit-partial-view-both-threshold-classes

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/four-bit-partial-view-both-threshold-classes/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

For **n = 10**, **every** **Q** with **|Q| ≤ 4** and **every** partial assignment **p** on **Q** admits **both** a global **u** with **wt(u) = 5** and **v** with **wt(v) = 6** agreeing with **p** on **Q** (equivalently: simultaneous feasibility **0 ≤ 5−z ≤ R** and **0 ≤ 6−z ≤ R** for **z** ones on **Q**, **R = n − |Q|**).

## Outcome

**PASS** — all **4521** **(Q, p)** pairs satisfy both feasibility inequalities (**script.py** exhaustive enumeration).

## Key finding (2–5 sentences)

The **036** collision was per fixed **Q** with a **zero** mask on **Q**. Here, **every** **≤4**-bit **partial view** — **any** pattern on **any** **≤4** probe set — remains compatible with **both** weight **5** and weight **6** globally. So in this bit-probe toy, **adaptive** decision trees of depth **4** (distinct coordinate queries) **cannot** label any leaf **soundly** for **wt ≥ 6** vs **wt = 5**; the information-theoretic barrier is **not** an artifact of non-adaptivity alone.

## Implications

- Formalize **query budget** lemmas: **k ≤ n − t** style regimes vs **minimum separating** **k**.
- Next: analyze **|Q| = 5** at **(n, t) = (10, 6)** where **R = 5** may break universal ambiguity for some **p**.

## Analogy pass summary

**Decision-tree shattering**, **underdetermined discrete reconstruction**, **CSP partial extensions** — all point to **ambiguous cells** when **global** threshold constraints outrun **local** observations; **transferred** counting on **(z, R)**.
