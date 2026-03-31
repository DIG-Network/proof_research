# 2026-03-30 — adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**mixed** **gate** **follow-up** **to** **045** **/** **049**).

## Hypothesis tested

**D_mix** **≤** **9** **for** **perfect** **trees** **on** **wt∈{5,6},** **n=10,** **with** **internal** **nodes** **x_i** **or** **x_i⊕x_j** **(** **stronger** **hope:** **beat** **coordinate-only** **depth** **n** **).**

## Outcome: **PASS**

**D_mix** **=** **5** **(** **depths** **1–4** **impossible** **).** **Coordinate-only** **minimum** **=** **10** **(** **045** **).**

## Key finding

**Pair-XOR** **queries** **interleaved** **with** **coordinate** **bits** **yield** **a** **strict** **adaptive** **depth** **improvement** **on** **the** **threshold-shell** **toy** **—** **not** **merely** **the** **pair-only** **regime** **of** **049.**

## Implications

- **Verifier** **models** **should** **separate** **“coordinate** **budget”** **from** **“F₂** **pair-linear”** **budget** **—** **the** **latter** **can** **shrink** **decision** **depth** **substantially** **here.**
- **Does** **not** **solve** **`Link(C,K)`** **—** **oracle** **toy** **only.**

## Analogy pass summary

**Oblique** **decision** **splits** **/** **richer** **local** **basis** **than** **axis-aligned** **bits** **alone** **—** **measured** **depth** **drop** **10** **→** **5.**
