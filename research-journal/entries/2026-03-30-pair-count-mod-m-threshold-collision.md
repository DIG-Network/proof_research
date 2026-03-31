# Entry — 2026-03-30 — pair-count-mod-m-threshold-collision

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/pair-count-mod-m-threshold-collision/`
- **Context:** `anonymous-quorum-binding`

## Hypothesis tested

**Unweighted** **pair** **count** **C(|S|,2)** **mod** **M** **collides** **for** **|S|=t−1** **vs** **t** **when** **M** **|** **(t−1);** **exhibit** **t=6,** **M=5.**

## Outcome

**PASS**

## Key finding

**C(t,2)−C(t−1,2)=t−1** **⇒** **modular** **threshold** **ambiguity** **exactly** **when** **M** **divides** **t−1** **(e.g.** **10≡15≡0** **(mod** **5)).**

## Implications

- **Extends** **the** **digest’s** **“modular** **/ ** **integer** **aggregate”** **thread** **beyond** **linear** **Σ** **w_i.**
- **Still** **not** **a** **set** **commitment** **binder** **—** **only** **a** **size** **statistic** **pitfall** **for** **homomorphic** **toys.**

## Analogy pass summary

**Sketch** **truncation** **/ ** **moment** **mod** **reduction** **—** **same** **collision** **theme** **as** **034.**
