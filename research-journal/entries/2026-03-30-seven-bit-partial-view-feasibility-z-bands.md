# Entry — 2026-03-30 — seven-bit-partial-view-feasibility-z-bands

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/seven-bit-partial-view-feasibility-z-bands/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

**n = 10**, **|Q| = 7**, **R = 3:** **z-bands** **neither** **for** **z ∈ {0,1,7},** **only_wt5** **for** **z=2,** **both** **for** **z ∈ {3,4,5},** **only_wt6** **for** **z=6;** **15360** **exhaustive** **pairs.**

## Outcome

**PASS** — **10920** **/** **2520** **/** **840** **/** **1080.**

## Key finding

**R = 3** **widens** **the** **neither** **region** **(9/128** **per** **Q)** **vs** **039’s** **2/64;** **ambiguous** **5** **vs** **6** **drops** **to** **91/128** **≈** **71%.** **z=1** **joins** **z=0** **as** **neither** **(cannot** **reach** **wt≥5** **with** **3** **outside** **bits).**

## Implications

- **Optional** **041:** **k=8,** **R=2** **band** **table.**
- **Close** **the** **(n=10,t=6)** **coordinate-probe** **series** **at** **k=9** **/** **k=10** **if** **needed** **for** **a** **closed** **lemma** **statement.**

## Analogy pass summary

**Interval** **clipping** **with** **shrinking** **R;** **same** **template** **as** **038–039** **with** **more** **boundary** **z** **values** **in** **neither.**
