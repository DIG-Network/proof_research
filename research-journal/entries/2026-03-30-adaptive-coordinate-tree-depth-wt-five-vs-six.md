# Entry — 2026-03-30 — adaptive-coordinate-tree-depth-wt-five-vs-six

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-tree-depth-wt-five-vs-six/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

**Perfect** **classification** **of** **wt=5** **vs** **wt=6** **on** **n=10** **using** **only** **adaptive** **single-bit** **coordinate** **queries** **requires** **worst-case** **depth** **10** **(not** **4).**

## Outcome

**PASS** **—** **backtracking** **finds** **no** **tree** **with** **depth** **≤** **9;** **depth** **10** **suffices** **(e.g.** **read** **all** **bits).**

## Key finding

**Adjacent** **Hamming** **layers** **contain** **flips** **at** **every** **coordinate;** **two** **vectors** **differing** **only** **at** **j** **are** **indistinguishable** **until** **x[j]** **is** **queried** **—** **so** **every** **index** **must** **appear** **on** **some** **worst-case** **path** **⇒** **depth** **≥** **n.**

## Implications

- **Strengthens** **the** **digest** **line** **after** **037:** **adaptivity** **does** **not** **reduce** **worst-case** **coordinate** **complexity** **below** **n** **for** **this** **pair** **of** **weights.**
- **037** **remains** **the** **right** **non-adaptive** **certificate;** **045** **is** **the** **adaptive** **completion.**

## Analogy pass summary

**Axis-aligned** **decision** **trees** **vs** **adversarial** **near** **duplicates** **—** **standard** **active** **learning** **/ ** **comparison** **lower** **bound** **pattern.**
