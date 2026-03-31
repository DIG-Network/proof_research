# Entry — 2026-03-30 — six-bit-partial-view-feasibility-z-bands

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/six-bit-partial-view-feasibility-z-bands/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

For **n = 10**, **|Q| = 6**, **R = 4**, feasibility of **wt = 5** **vs** **wt = 6** extensions follows **z**-**bands** **z ∈ {0}** **neither,** **{1}** **only** **wt=5,** **{2,…,5}** **both,** **{6}** **only** **wt=6**; exhaustive **13440** **pairs.**

## Outcome

**PASS** — counts **11760** **/** **1260** **/** **210** **/** **210** **match** **binomial** **weights** **per** **z.**

## Key finding

**R = 4** **splits** **the** **6**-**bit** **prefix** **space** **into** **four** **feasibility** **types.** **Most** **mass** **(87.5%** **of** **patterns** **per** **Q)** **remains** **ambiguous** **between** **sub-quorum** **and** **quorum;** **new** **vs** **038:** **all-zero** **prefix** **admits** **neither** **target** **(max** **wt** **4),** **and** **all-one** **prefix** **admits** **only** **wt=6.**

## Implications

- **Document** **general** **(n,** **t,** **k)** **band** **formulas** **for** **oracle** **budget** **notes.**
- **k=7** **(R=3):** **wider** **exclusive** **bands** **—** **entry** **040.**

## Analogy pass summary

**Reachability** **in** **restricted** **integer** **intervals;** **erasure** **+** **weight** **targets;** **sequential** **test** **power** **—** **same** **counting** **kernel** **as** **037–038** **(extended** **with** **four** **cells** **at** **k=6).**
